#!/usr/bin/env python3
"""Build the rule bundle for one task, within the token budget.

Selection is deterministic:
  1. company/ files with scope: always.
  2. Skill, if given.
  3. All files of the chosen role (the agent's own rules).
  4. Up to --max-files company task files and template files whose `when:` line best matches the task text.
  5. Stop adding when the budget would be exceeded.

Examples:
  python3 scripts/load.py --templates software,web-panel,web-commerce --role backend \
      --skill api-design --task "add refund endpoint to admin panel"
  python3 scripts/load.py --role code-reviewer --skill code-review --list
Output: the bundle on stdout (or the file list with --list), a summary on stderr.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHARS_PER_TOKEN = 4
DEFAULT_BUDGET = 5000
MAX_TASK_FILES = 5
STOPWORDS = {"a", "an", "and", "any", "for", "in", "of", "on", "or", "the", "to", "with", "when", "add", "new"}


def tokens(text: str) -> int:
    return len(text) // CHARS_PER_TOKEN


def stem(word: str) -> str:
    """Crude English stemmer so 'refund', 'refunds', 'refunding' match."""
    for suffix in ("ing", "es", "s"):
        if word.endswith(suffix) and len(word) - len(suffix) >= 4:
            return word[: -len(suffix)]
    return word


def words(text: str) -> set:
    return {stem(w) for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOPWORDS and len(w) > 2}


def when_line(text: str) -> str:
    match = re.search(r"^when:\s*(.+)$", text, re.M)
    return match.group(1) if match else ""


def score(path: Path, text: str, task_words: set) -> int:
    trigger = words(when_line(text)) | words(path.stem.replace("-", " "))
    return len(trigger & task_words)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--templates", default="software", help="comma-separated template folders")
    parser.add_argument("--role", help="role folder doing the task")
    parser.add_argument("--skill", help="skill folder name")
    parser.add_argument("--task", default="", help="short task description for matching")
    parser.add_argument("--budget", type=int, default=DEFAULT_BUDGET)
    parser.add_argument("--max-files", type=int, default=MAX_TASK_FILES)
    parser.add_argument("--list", action="store_true", help="print file list only")
    args = parser.parse_args()

    chosen, used = [], 0

    def add(path: Path) -> bool:
        nonlocal used
        cost = tokens(path.read_text(encoding="utf-8"))
        if used + cost > args.budget:
            print(f"skip (budget): {path.relative_to(ROOT)}", file=sys.stderr)
            return False
        chosen.append(path)
        used += cost
        return True

    company_task = []
    for path in sorted((ROOT / "company").glob("*.md")):
        if re.search(r"^scope:\s*always\s*$", path.read_text(encoding="utf-8"), re.M):
            add(path)
        else:
            company_task.append(path)

    if args.skill:
        skill = ROOT / "skills" / args.skill / "SKILL.md"
        if not skill.is_file():
            print(f"unknown skill: {args.skill}", file=sys.stderr)
            return 2
        add(skill)

    role_dir = ROOT / "roles" / args.role if args.role else None
    template_dirs = [ROOT / "templates" / t.strip() for t in args.templates.split(",") if t.strip()]
    for folder in template_dirs + ([role_dir] if role_dir else []):
        if not folder.is_dir():
            print(f"unknown folder: {folder.relative_to(ROOT)}", file=sys.stderr)
            return 2

    if role_dir:
        for path in sorted(role_dir.glob("*.md")):
            add(path)

    task_words = words(args.task)
    candidates = []
    template_files = [path for folder in template_dirs for path in sorted(folder.glob("*.md"))]
    for path in company_task + template_files:
        match = score(path, path.read_text(encoding="utf-8"), task_words)
        if match:
            candidates.append((match, path))
    candidates.sort(key=lambda c: (-c[0], str(c[1])))

    for _, path in candidates[: args.max_files]:
        add(path)

    if args.list:
        print("\n".join(p.relative_to(ROOT).as_posix() for p in chosen))
    else:
        for path in chosen:
            print(f"<!-- {path.relative_to(ROOT).as_posix()} -->")
            print(path.read_text(encoding="utf-8").strip(), end="\n\n")
    print(f"{len(chosen)} files, ~{used}/{args.budget} tokens", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

# agent-playbook

Rule files and skills for the agent team.

## Structure
| Folder | Loaded | Content |
|---|---|---|
| `company/` | every task | Company-wide rules. Small by design. |
| `templates/<type>/` | when `when:` matches | Rules per project type. `software` applies to all code. |
| `roles/<role>/` | when that role works and `when:` matches | Role rules. |
| `skills/` | on demand | Step-by-step procedures (SKILL.md). |

`INDEX.md` lists every file with its trigger and size — agents read it to pick files instead of loading folders.

## Loading budget
- Prompt limit 5000 tokens. `company/` total target ≤ 2500.
- Per task: `company/` + at most ~5 matching task files.

## Authoring rules
- md = what and why; skill = how. Skills reference md files, never copy them.
- One topic, one file. Link (`roles/backend/…md`) instead of repeating.
- Frontmatter: `scope` (always|task), `when` (task files), `owner`, `status` (draft|approved), optional `review: expert-required (…)`.
- Imperative bullets, no filler. Always ≤ ~400 tokens/file, task ≤ ~600.
- Files marked `review: expert-required` can't become `approved` without a named expert.
- QA tests running software; security-reviewer reviews code/design; code-reviewer reviews quality.

## Before committing
```
python3 scripts/check.py
```
Checks frontmatter, links and budgets, and regenerates `INDEX.md`.

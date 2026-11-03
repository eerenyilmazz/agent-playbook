# Agent Instructions

You work under the rules in this repo. Follow this protocol on every task.

## 1. Load
- Always: every file in `company/`.
- Then only files matching the task — use `INDEX.md` (`when:` column) or run:
  `python3 scripts/load.py --templates <types> --role <role> [--skill <skill>] --task "<task>"`
- Project types and overrides come from the project's README (format: `docs/project-readme-template.md`).
- Never load whole folders. Stay under 5000 tokens.

## 2. Precedence (highest first)
1. The user's explicit instruction for this task.
2. Project README overrides.
3. `company/` rules.
4. Template, then role files.
5. Skill steps.
If two rules conflict, follow the higher one and say so in your output.

## 3. Work
- Follow the skill's steps when one applies; produce its output format.
- Use `examples/` as the quality bar for PRs, ADRs, postmortems, API errors and commits.
- State risk level (low/medium/high) and whether anything is breaking.
- Files with `review: expert-required` are guidance, not legal truth: flag decisions that depend on them for human review.

## 4. Don't
- Don't restate rules into project code or docs; link to the file.
- Don't edit this repo's rules during a project task. Propose the change instead (see README → Adding or changing a file).

## 5. Report a gap
If a needed rule is missing or wrong, end your output with:
`Playbook gap: <file or topic> — <what's missing/wrong> — <suggested fix>`

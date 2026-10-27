# agent-playbook

All rule files and skills for the agent team: company rules, project templates, roles and skills.

## Structure
- `company/` — Rules loaded for every task (always). Kept short.
- `templates/` — Rules loaded by project type (task).
- `roles/` — Role-specific rules.
- `skills/` — Step-by-step procedures (SKILL.md).

## Rules
- An md says "what and why"; a skill says "how". Skills don't copy rules — they reference the md.
- Each topic lives in exactly one file.
- All `always` files together must fit the 5000-token prompt limit.
- Every file has `owner` and `status` (draft/approved) fields.
- Legal, compliance and payment files cannot be marked approved without expert sign-off.

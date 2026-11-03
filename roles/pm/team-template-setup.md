---
scope: task
when: Starting a new project; choosing templates and roles
owner: Eren
status: draft
---
# Team and Template Setup

## Steps
1. Pick template folders from `templates/` (e.g. `software` + `web` + `web-panel`). `software` applies to all code projects.
2. Pick only the roles the project needs from `roles/`.
3. Project README: goal, scope, out of scope, stack, owner, templates, roles, overrides (e.g. budgets, browser matrix).
4. Backlog with acceptance criteria.
5. First risk register.

## Loading (keeps prompts small)
- `company/` → always.
- A template/role file → only when its `when:` line matches the task.
- Target ≤ 5 task files per task; check `scripts/check.sh` budgets.

## Gaps
Missing rule → add it to the right file in this repo (one topic, one place), not to the project.

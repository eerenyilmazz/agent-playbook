---
scope: task
role: pm
owner: Eren
status: draft
---
# Team and Template Setup

How the PM sets up a new project.

## Steps
1. Identify the project type and pick the template(s) from `templates/` (e.g. web + web-panel).
2. Pick the roles needed from `roles/`. Don't add roles the project doesn't need.
3. Confirm which `company/` rules apply (all of them, by default).
4. Create the project README with: goal, scope, out of scope, stack, owner, chosen templates and roles, any overrides (e.g. different performance budget).
5. Create the initial backlog with acceptance criteria.
6. Write the first risk register (see risk-management.md).

## Loading rules
- `company/` files: always loaded.
- Template files: loaded for tasks of that type.
- Role files: loaded for the role doing the task.
- Keep the loaded set for one task within the prompt budget.

## Gaps
If a project needs a rule that doesn't exist, add it to the right file in this repo (one topic, one place) instead of writing it in the project.

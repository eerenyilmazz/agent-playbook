---
scope: always
owner: Eren
status: draft
---
# Documentation Standard

## Every repo
- `README.md`: purpose, run locally, run tests, env var names, owner, chosen templates/roles.
- `CHANGELOG.md`: per release — Added / Changed / Fixed / Removed / Security. Breaking first. User language, not commit dumps.
- `docs/adr/`: decisions that are expensive to reverse. Template: templates/software/architecture-decision-record.md.
- API contract: OpenAPI (REST) or schema files for events, versioned with the code.
- `docs/runbook.md` for anything in production: deploy, rollback, alerts, common fixes.

## Rule precedence
User's task instruction > project README overrides > company > template > role > skill. On conflict follow the higher one and say so.

## Rules
- Docs change in the same PR as the code.
- One fact, one place; link instead of copy.
- Accepted ADRs are immutable; supersede with a new one.
- Out-of-date doc = bug.

---
scope: always
owner: Eren
status: draft
---
# Documentation Standard

## README (every repo)
- What the project does (2–3 sentences).
- How to run it locally.
- How to run the tests.
- Required environment variables (names, not values).
- Owner.

## ADR (architecture decision record)
Written for any decision that is expensive to reverse. Full template: architecture-decision-record.md (single source).
- File: `docs/adr/0001-short-title.md`
- Sections: Context, Decision, Alternatives, Consequences, Status (proposed/accepted/superseded).
- Accepted ADRs are never edited; a new ADR supersedes them.

## Changelog
- `CHANGELOG.md`, one section per release.
- Headings: Added, Changed, Fixed, Removed.
- Breaking changes go first and are clearly marked.
- Written for the user; don't paste the commit list.

## General
- Docs are updated in the same PR as the code.
- No duplication: each fact lives in one place; others link to it.

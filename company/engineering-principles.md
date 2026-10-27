---
scope: always
owner: Eren
status: draft
---
# Engineering Principles

## Code
- Preserve existing structure. No rewrites; only small, reversible changes.
- Layers: Controller → Service → Domain → Infrastructure. No business logic in controllers.
- Functions are short and single-purpose. No magic numbers/strings; use constants.
- Constructor injection. No unnecessary abstraction.

## Naming
- Names say what they do: `calculateTotal`, `isExpired`. No abbreviations.
- Comments explain "why", not "what".

## Small diffs
- One PR does one thing. Target: under 400 lines.
- Refactoring and behavior changes never share a PR.
- Changes that break an API, schema or UI are flagged explicitly.

## Definition of done
1. Code compiles; existing tests pass.
2. New code has at least unit tests.
3. Acceptance criteria met (see acceptance-criteria.md).
4. Code review approved.
5. Docs and changelog updated if needed.
6. Rollback path is known.

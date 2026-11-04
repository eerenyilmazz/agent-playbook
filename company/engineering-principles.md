---
scope: always
owner: Eren
status: draft
---
# Engineering Principles

## Precedence
User's task instruction > project overrides > company > template > role > skill. On conflict follow the higher one and say so.

## Change safety
- Production is live: backward compatible; breaking changes need explicit request, label, risk note.
- Small, reversible changes; risky behavior behind a flag. No rewrites.
- State risk level (low/medium/high) and why.

## Code
- Controller → Service → Domain → Infrastructure. Controllers: request/response and validation only.
- APIs use DTOs, never entities. Constructor injection. No magic values.
- No abstraction without a second use case. Comments explain why.
- Config in environment; fail fast if missing.

## Diffs
One PR, one purpose, < 400 lines. Never mix refactor and behavior change. Contract changes (API, schema, event, UI) flagged.

## Done
Builds; existing tests pass, none weakened · new logic tested, bug fix has failing-first test · acceptance criteria met · reviewed · docs/changelog updated · rollback known, logs/metrics in place.

---
scope: always
owner: Eren
status: draft
---
# Engineering Principles

## Change safety
- Production is live. Backward compatible; breaking changes need explicit request, label, risk note.
- Small, isolated, reversible changes. No rewrites.
- Risky behavior changes behind a feature flag.
- Every task states risk level (low/medium/high) and why.

## Code
- Layers: Controller → Service → Domain → Infrastructure. Controllers: request/response and validation only.
- Entities never leave the service boundary; APIs use DTOs.
- Constructor injection. Short single-purpose functions. No magic values.
- No abstraction without a second use case. Comments explain why.
- Config in environment, not code. Fail fast on missing config.

## Diffs
- One PR, one purpose, < 400 lines. Refactor and behavior change never mixed.
- API, schema, event or UI contract change = flagged as potentially breaking.

## Definition of done
1. Builds; all existing tests pass; none weakened.
2. New logic has unit tests; bug fixes have a failing-first test.
3. Acceptance criteria met.
4. Reviewed and approved.
5. Docs/changelog updated.
6. Rollback path known; observability (logs/metrics) in place.

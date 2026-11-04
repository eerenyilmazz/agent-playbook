---
scope: always
owner: Eren
status: draft
---
# Engineering Principles

**Precedence:** task instruction > project overrides > company > template > role > skill. On conflict follow the higher one and say so.

- Production is live: stay backward compatible; breaking changes only on request, labeled, with a risk note.
- Small, reversible changes; risky behavior behind a flag; no rewrites. State risk level (low/medium/high) and why.
- Controller → Service → Domain → Infrastructure. No logic in controllers. APIs use DTOs, never entities.
- Constructor injection. No magic values. No abstraction without a second use case.
- Done = builds · existing tests pass, none weakened · new logic tested · acceptance criteria met · reviewed · docs updated · rollback known. Never report an unrun check as passed.

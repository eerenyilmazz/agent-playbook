---
scope: task
when: Reviewing or approving an ADR
owner: Eren
status: draft
---
# ADR Approval

Format: templates/software/architecture-decision-record.md.

## Flow
1. Author opens PR with ADR `proposed`.
2. Affected roles review (backend, frontend, security, devops) within an agreed time (default 2 working days).
3. Decision-maker: accept · request changes · reject (with reason).
4. Accept → status `accepted`, merge.

## Checklist
- Real problem stated, not just the solution.
- ≥ 2 genuine options, incl. do nothing.
- Downsides and lock-in listed.
- Security, data, cost and ops impact covered.
- Backward compatibility and migration path.
- Rollback stated, even if expensive.

## Rules
- Rejected ADRs kept as `rejected` with reason.
- No irreversible work before acceptance.

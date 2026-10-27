---
scope: task
role: decision-maker
owner: Eren
status: draft
---
# ADR Approval

The ADR template is in templates/software/architecture-decision-record.md. This file covers the approval process.

## Process
1. Author writes the ADR with status `proposed` and opens a PR.
2. Relevant roles review (backend, frontend, security, devops as needed) within an agreed time.
3. Decision-maker approves, requests changes, or rejects with a reason.
4. On approval, status becomes `accepted` and the PR is merged.

## Approval checklist
- Context explains the real problem, not just the solution.
- At least two alternatives were genuinely considered.
- Consequences include the downsides.
- Security, data and cost impact are covered.
- Rollback path is stated, even if expensive.
- Backward compatibility is addressed.

## Rules
- No hard-to-reverse implementation starts before the ADR is accepted.
- A rejected ADR is kept with status `rejected` and the reason, so it isn't proposed again unchanged.

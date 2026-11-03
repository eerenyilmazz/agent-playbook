---
scope: task
when: Any decision between options; escalations
owner: Eren
status: draft
---
# Decision Framework

## Classify
- **Reversible (two-way door):** decide fast; closest owner decides; note it in the task.
- **Hard to reverse (one-way door):** options + trade-offs + ADR.

## Request must include
Question (1 sentence) · ≥ 2 options incl. "do nothing" · cost, risk, time, lock-in per option · recommendation + reason · decision deadline.

## Decide
1. Reversible? → decide now.
2. Check hard constraints: budget, deadline, legal, security, backward compatibility.
3. Score with cost-risk-matrix.md.
4. Default to the least risky, most reversible option unless clearly worse on value.
5. Record: ADR (one-way) or task note (two-way). Name the owner.

## Rules
- Reopen only with new information.
- Disagree and commit once decided.

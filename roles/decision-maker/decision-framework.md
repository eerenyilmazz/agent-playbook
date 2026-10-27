---
scope: task
role: decision-maker
owner: Eren
status: draft
---
# Decision Framework

## Two kinds of decisions
- **Reversible (two-way door):** Decide fast, with the information at hand. The team member closest to the work can decide.
- **Hard to reverse (one-way door):** Slow down. Requires options, trade-offs and an ADR.

## Every decision request includes
- The question, in one sentence.
- At least two options (doing nothing counts).
- For each option: cost, risk, time, and what it makes harder later.
- A recommendation with the reason.
- Deadline for the decision.

## How to decide
1. Is it reversible? If yes, decide now.
2. Check against constraints: budget, deadline, legal, security, backward compatibility.
3. Score options with the cost-risk matrix (cost-risk-matrix.md).
4. Prefer the option that is least risky and easiest to undo, unless there's a clear reason not to.
5. Record the decision: ADR for hard-to-reverse, a short note in the task for the rest.

## Rules
- A decision without an owner is not a decision.
- Revisit a decision only with new information, not because someone disagrees again.

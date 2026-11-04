---
scope: task
when: Reviewing a PR; approve or request changes
owner: Eren
status: draft
---
# Review Rubric

Procedure: code-review skill. Mistake list: common-mistakes.md.

## Score each area: pass · concern · fail
| Area | Pass means |
|---|---|
| Intent | PR states what, why, risk, test evidence, rollback |
| Correctness | Does what it claims, edge cases handled |
| Contracts | No unflagged API/schema/event/log/UI break |
| Architecture | Layers respected, no logic in controllers/templates, no needless abstraction |
| Security | Rules in company/security-details.md met |
| Performance | Within templates/software/performance-budget.md |
| Tests | New logic tested, nothing weakened |
| Readability | Clear names, small functions, no magic values |
| Ops | Logs/metrics present, migration safe, rollback possible |

## Verdict
- Any **fail** → request changes (blocker).
- Only **concern** → approve with comments, or request changes if risk is high.
- All **pass** → approve.

## Reviewer conduct
Review within 1 working day · comment on code, not people · explain why · offer a fix · approve once blockers are resolved, don't re-litigate nits.

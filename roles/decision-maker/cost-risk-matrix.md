---
scope: task
role: decision-maker
owner: Eren
status: draft
---
# Cost-Risk Matrix

## Score each option (1 = low, 5 = high)
| Criterion | What it means |
|---|---|
| Cost | Money + effort to build |
| Run cost | Ongoing hosting, licenses, maintenance |
| Risk | Chance and impact of failure |
| Reversibility | How hard to undo (5 = very hard) |
| Time | Time to deliver |
| Value | Benefit delivered (higher is better) |

## Reading the result
- **High value, low risk:** Do it.
- **High value, high risk:** Do it in small steps, behind flags, with a rollback plan.
- **Low value, low risk:** Do it only if it's cheap.
- **Low value, high risk:** Don't.

## Risk = likelihood × impact
| | Low impact | Medium | High |
|---|---|---|---|
| **High likelihood** | Medium | High | Critical |
| **Medium** | Low | Medium | High |
| **Low** | Low | Low | Medium |

Critical risks need a mitigation before work starts. High risks need an owner and a plan.

## Rules
- Scores are discussed, not just written; write one line on why for each.

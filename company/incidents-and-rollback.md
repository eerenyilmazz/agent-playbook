---
scope: task
when: Production broken; planning a rollback
owner: Eren
status: draft
---
# Incidents and Rollback

Procedure: incident-postmortem skill. This file sets the rules.

## Severity
| Sev | Meaning | Response |
|---|---|---|
| 1 | Outage, data loss, security breach | Immediately, all hands |
| 2 | Major feature broken, no workaround | Within 1 hour |
| 3 | Minor, workaround exists | Next working day |

## Response
1. Name one incident lead. Mitigate first, diagnose second.
2. Prefer rollback or flag-off over a live fix.
3. Keep a timestamped log of observations and actions.
4. Update stakeholders at a fixed interval until resolved.
5. Security or personal-data incidents: also follow data-and-privacy notification rules.

## Rollback rules
- Every release has a tested rollback path before it ships.
- Irreversible migrations are declared before release and need a backup.

## Postmortem (Sev 1–2, within 5 working days)
Summary · impact · timeline · root cause (technical + process) · what worked / didn't · actions with owner and date. Blameless.

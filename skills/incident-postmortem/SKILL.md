---
name: incident-postmortem
description: Handle a production incident from detection to resolution, then write a blameless postmortem with actions. Use when production is broken, degraded or a security/data incident occurs.
---
# Incident and Postmortem

Rules (severity, rollback, postmortem fields): company/incidents-and-rollback.md. Data/security incidents also: templates/software/data-and-privacy.md, roles/security-reviewer/secret-leak-check.md.

## During the incident
1. **Declare.** Set severity (Sev 1–3), name the incident lead, open one channel/log.
2. **Assess** (≤ 10 min): what's broken, who's affected, since when, what changed recently (deploys, config, flags, traffic, provider status).
3. **Mitigate first:** roll back last deploy · turn off flag · scale · fail over · block bad traffic. Don't debug in production while users suffer.
4. **Log** every action with time (UTC) and result.
5. **Communicate** at fixed intervals (Sev 1: 30 min, Sev 2: 60 min): status, impact, next update time.
6. **Resolve:** confirm metrics back to normal for an agreed period; announce resolution.
7. **Preserve evidence:** logs, dashboards, timeline before they rotate.

## Postmortem (Sev 1–2 within 5 working days)
```
# Incident YYYY-MM-DD: title
Severity · Duration · Lead
## Summary        3 sentences
## Impact         users, data, money, SLA
## Timeline       UTC: detection → mitigation → resolution
## Root cause     technical + process; use "5 whys"
## Detection      how found; could we find it sooner?
## What went well / badly
## Actions        | action | owner | due | type: prevent/detect/mitigate |
```

## Rules
Blameless: describe systems and decisions, not people. Every action has an owner and a date and is tracked to closure. Review actions at the next sprint planning.

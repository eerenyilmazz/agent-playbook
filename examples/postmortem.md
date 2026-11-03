# Example: Postmortem

```
# Incident 2026-09-18: checkout failing for card payments
Severity: 1 · Duration: 47 min · Lead: on-call backend

## Summary
A config change rotated the payment provider API key in production but not in the secret
manager. All card payments failed with 401 for 47 minutes. Rolled back the config; no data lost.

## Impact
~380 failed checkout attempts; estimated 120 lost orders; no double charges.

## Timeline (UTC)
10:02 config deploy · 10:06 error-rate alert · 10:09 incident declared · 10:21 cause found
10:24 rollback · 10:49 error rate normal for 25 min, resolved

## Root cause
Technical: key rotated in provider dashboard, old key revoked immediately.
Process: rotation runbook had no "update secret manager first, revoke old key last" order.

## Detection
Alert fired after 4 min. Could be faster with a synthetic checkout every minute.

## Went well / badly
+ Fast alert, clean rollback.  − 12 min to find cause; provider errors not in dashboard.

## Actions
| Action | Owner | Due | Type |
|---|---|---|---|
| Rotation runbook: add-new → deploy → verify → revoke-old | devops | 2026-09-25 | prevent |
| Synthetic checkout probe every 60 s | QA | 2026-10-02 | detect |
| Provider error codes on payments dashboard | backend | 2026-10-02 | mitigate |
```

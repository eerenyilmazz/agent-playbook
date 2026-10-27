---
scope: always
owner: Eren
status: draft
---
# Incidents and Rollback

The step-by-step procedure lives in the incident-postmortem skill. This file defines the rules.

## Production incidents
1. Stop the impact first, then look for the root cause.
2. Rollback is the first choice (previous release or disabling a feature flag). No live fixes in production.
3. Record what was observed, what was done, and when.
4. Notify affected users/clients of the status.

## Hotfixes
- Branch `hotfix/` from `main`. Scope is the issue only.
- Review is never skipped, only expedited.
- After merge: tag the release and add a changelog entry.

## Rollback rules
- Every release has a known rollback path before it ships.
- If a data migration cannot be reversed, say so explicitly before release.

## Postmortem template
- **Summary:** What happened, how long, who was affected.
- **Timeline:** Detection, response, resolution times.
- **Root cause:** Technical and process.
- **What went well / what went badly.**
- **Action items:** With owner and due date.

Postmortems are blameless; they fix the system, not the person.

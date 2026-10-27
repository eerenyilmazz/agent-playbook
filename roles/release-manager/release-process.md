---
scope: task
role: release-manager
owner: Eren
status: draft
---
# Release Process

Step-by-step checklist: release-checklist skill. Git and versioning rules: company/git-and-versioning.md.

## Before release
- Scope frozen; every item meets the definition of done.
- QA sign-off with known issues listed (roles/qa-security/regression-suite.md).
- Changelog written; breaking changes highlighted.
- Rollback path confirmed and tested; irreversible migrations stated explicitly.
- Release window agreed; avoid Fridays and holidays for high-risk releases.
- Stakeholders and support informed of user-facing changes.

## During release
- Follow the checklist; one person runs it, one person watches.
- Smoke tests right after deploy.
- Watch error rates, latency and key business metrics for an agreed period.

## After release
- Tag and publish release notes.
- Disable feature flags only after the feature is stable.
- If something goes wrong: roll back first, then investigate (company/incidents-and-rollback.md).

## Go / no-go
Any open critical bug, failed smoke test, or missing rollback plan is a no-go.

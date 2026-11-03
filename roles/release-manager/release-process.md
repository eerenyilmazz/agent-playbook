---
scope: task
when: Planning, running or approving a release
owner: Eren
status: draft
---
# Release Process

Checklist: release-checklist skill. Versioning: company/git-and-versioning.md.

## Before
- Scope frozen; all items meet definition of done.
- QA sign-off with known issues (roles/qa-security/regression-suite.md).
- Changelog ready; breaking changes highlighted.
- Rollback tested; irreversible migrations declared with backup.
- Window agreed; no high-risk releases before weekends/holidays.
- Support and stakeholders informed of user-facing changes.

## During
One runs the checklist, one watches. Smoke tests right after deploy. Watch errors, latency and key business metrics for an agreed period.

## After
Tag + release notes. Remove flags only once stable. Problem → rollback first (company/incidents-and-rollback.md).

## No-go if
Open critical bug · failed smoke test · no rollback plan · missing sign-off.

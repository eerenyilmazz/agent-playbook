---
name: release-checklist
description: Run a production release from freeze to post-release watch, with go/no-go gates and rollback. Use when shipping any backend, web or desktop release.
---
# Release Checklist

Rules: roles/release-manager/release-process.md, company/git-and-versioning.md, company/incidents-and-rollback.md. Mobile stores: store-submission skill. Desktop: electron-release skill.

## T-1 day: prepare
- [ ] Scope frozen; all items done per company/engineering-principles.md.
- [ ] QA sign-off received (tested / not tested / known issues).
- [ ] No open Critical/High security findings.
- [ ] Changelog written; breaking changes first.
- [ ] Migrations reviewed; irreversible ones declared; backup plan set (db-migration skill).
- [ ] Rollback path written and rehearsed on staging.
- [ ] Feature flags listed with default state.
- [ ] Window agreed (not before weekend/holiday if high risk); runner + watcher named.
- [ ] Support/stakeholders notified.

## Go / no-go
Any unchecked box above → **no-go**, or written acceptance from the decision-maker.

## Release
1. Tag `vX.Y.Z` from `main`; CI builds the artifact.
2. Deploy to staging → smoke tests pass.
3. Backup verified if migrations run.
4. Deploy to production (rolling/blue-green).
5. Smoke tests in production.
6. Enable flags gradually if planned.

## Watch (agreed window, default 60 min)
- [ ] Error rate and p95 latency within normal range.
- [ ] Key business metric normal (logins, orders, etc.).
- [ ] No new alert or spike in logs.
Breach → **roll back first**, then open incident.

## Close
- [ ] Release notes published.
- [ ] Release marked done; follow-ups ticketed (flag cleanup, contract phase of migrations).

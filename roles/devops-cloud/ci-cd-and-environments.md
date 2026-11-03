---
scope: task
when: CI/CD pipelines, environments, infrastructure, deploys
owner: Eren
status: draft
---
# CI/CD and Environments

## Environments
- Local · staging · production. Staging mirrors prod config.
- Same immutable artifact promoted across environments; config via env vars/secret manager.
- Infrastructure as code; manual console changes forbidden or recorded and back-ported.

## CI (every PR)
Build · tests · lint · SAST · dependency + secret scan. Cache dependencies; target < 10 min.

## CD
- Automated, repeatable deploys; versioned images (`version` + commit SHA).
- Zero downtime: rolling or blue/green; readiness/liveness probes.
- Migrations per roles/backend/database-migrations.md.
- Rollback = redeploy previous artifact; rehearsed.
- Production deploys require approval and are logged.

## Operations
- Metrics, logs, traces and alerts per service; each alert has a runbook entry.
- SLOs for key services; alerts on SLO burn, not raw noise.
- Automated backups; restore tested at least quarterly.
- Least privilege + MFA on cloud accounts; OIDC for CI credentials.
- Budget alerts; tag resources by project.

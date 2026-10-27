---
scope: task
role: devops-cloud
owner: Eren
status: draft
---
# CI/CD and Environments

Note: a separate draft for this role exists elsewhere and has not been reviewed; merge it here.

## Environments
- At least: local, staging, production. Staging mirrors production configuration.
- Configuration via environment variables; same build artifact promoted through environments.
- Infrastructure as code (Terraform, etc.); no manual console changes without recording them.

## CI
- Every PR: build, tests, lint, dependency and secret scan.
- Main branch builds produce a versioned, immutable artifact (image tagged with version/commit).

## CD
- Deploys are automated and repeatable; anyone authorized can deploy and roll back.
- Zero-downtime deploys (rolling or blue/green). Database migrations follow roles/backend/database-migrations.md.
- Rollback = redeploy the previous artifact, tested regularly.

## Operations
- Health checks, metrics, logs and alerts for every service.
- Alerts are actionable; each one has a short runbook.
- Backups are automated and restores are tested on a schedule.
- Least-privilege access to cloud accounts; MFA everywhere.
- Cost is monitored with budget alerts.

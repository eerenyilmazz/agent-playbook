---
scope: task
when: Reviewing for leaked credentials; handling a leak
owner: Eren
status: draft
---
# Secret Leak Check

## Prevent
- Secret scanning pre-commit and in CI (e.g. gitleaks); push protection on the Git host.
- `.env`, keys, credential files in `.gitignore`; examples use placeholders.
- Short-lived credentials (OIDC for CI → cloud) instead of long-lived keys.

## Review for secrets in
Code · config · tests · docs/comments · logs/errors · URLs · analytics · frontend/mobile bundles (shipped = public) · CI logs and artifacts · container images.

## On leak
1. Revoke and rotate immediately.
2. Check usage logs for abuse.
3. Remove from code; history rewrite optional, never sufficient.
4. Record as incident (company/incidents-and-rollback.md).

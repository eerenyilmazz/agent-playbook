---
scope: task
role: security-reviewer
owner: Eren
status: draft
---
# Secret Leak Check

Base rules: company/security-basics.md (Secrets).

## Prevention
- Secret scanning in CI and as a pre-commit hook (e.g. gitleaks); push protection enabled on the Git host.
- `.env`, key files and credential files are in `.gitignore`.
- Example config files contain placeholders, never real values.

## In every review, look for
- Keys, tokens, passwords or connection strings in code, config, tests, docs or comments.
- Secrets in logs, error messages, URLs or analytics events.
- Secrets in frontend bundles or mobile apps (anything shipped to clients is public).
- Secrets in CI logs or build artifacts.

## If a secret leaks
1. Revoke and rotate it immediately — this is the actual fix.
2. Check access logs for use of the leaked secret.
3. Remove it from the code; rewriting git history is optional and never enough by itself.
4. Record it as an incident (company/incidents-and-rollback.md).

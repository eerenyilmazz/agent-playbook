---
scope: task
when: Auth, sessions, uploads, secrets, headers, deps
owner: Eren
status: draft
---
# Security Details

Single source for security rules. Summary that loads on every task: security-basics.md. Role files and skills link here.

## Secrets and config
- Never in code, commits, logs, URLs or client bundles. Load from env/secret manager.
- Leaked = revoke and rotate now. History rewrite alone is not a fix.
- Config in environment, not code. Fail fast on missing config.

## Input and output
- All external input is untrusted (body, query, headers, files, webhooks). Validate server-side, allow-list where possible.
- Parameterized queries only. Encode output for its context.
- Uploads: check type by content, size limit, store outside web root, random names.

## Auth
- Passwords hashed with Argon2id or bcrypt. MFA for admin access.
- Every endpoint enforces authorization, including object ownership. Default deny.
- Rate-limit login, reset, OTP and expensive endpoints.
- Sessions/tokens: short-lived, revocable, `Secure; HttpOnly; SameSite` cookies.

## Transport
- TLS everywhere. Security headers (CSP, HSTS, X-Content-Type-Options).
- Errors never expose stack traces, SQL or versions.
- Least privilege for services, DB users and cloud roles.

## Dependencies
- Justify each new one; pin via lock file; scan in CI; critical CVEs fixed immediately.

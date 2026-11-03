---
scope: always
owner: Eren
status: draft
---
# Security Basics

Single source. Role files and skills reference this; they don't restate it.

## Secrets
- Never in code, commits, logs, URLs or client bundles. Load from env/secret manager.
- Leaked = revoke and rotate now. History rewrite alone is not a fix.

## Input and output
- All external input is untrusted (body, query, headers, files, webhooks). Validate server-side, allow-list where possible.
- Parameterized queries only. Encode output for its context.
- Uploads: check type by content, size limit, store outside web root, random names.

## Auth
- Passwords hashed with Argon2id or bcrypt. MFA for admin access.
- Every endpoint enforces authorization, including object ownership. Default deny.
- Rate-limit login, reset, OTP and expensive endpoints.
- Sessions/tokens: short-lived, revocable, `Secure; HttpOnly; SameSite` cookies.

## Transport and config
- TLS everywhere. Security headers (CSP, HSTS, X-Content-Type-Options).
- Errors never expose stack traces, SQL or versions.
- Least privilege for services, DB users and cloud roles.

## Dependencies
- Justify each new one; pin via lock file; scan in CI; critical CVEs fixed immediately.

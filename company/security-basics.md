---
scope: always
owner: Eren
status: draft
---
# Security Basics

Minimum on every task. Details (single source): security-details.md.

- No secrets in code, commits, logs, URLs or client bundles. Leaked → revoke and rotate now.
- All external input is untrusted: validate server-side, parameterized queries, encode output.
- Every endpoint enforces authorization, including object ownership. Default deny.
- Passwords Argon2id/bcrypt; rate-limit auth endpoints; MFA for admins.
- TLS everywhere; errors never expose internals; least privilege everywhere.
- New dependency: justified, pinned, scanned.

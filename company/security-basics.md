---
scope: always
owner: Eren
status: draft
---
# Security Basics

This file is the single source of truth. Detailed checks live in the security-reviewer role and the security-audit skill, which reference this file.

## Secrets
- Passwords, tokens and API keys never go into code, commits or logs.
- Secrets come from environment variables or a secret manager. `.env` is in `.gitignore`.
- A leaked secret is revoked and rotated immediately; deleting it from history is not enough.

## Input validation
- All external data is untrusted: requests, files, headers, webhooks.
- Validate on the server. Client-side validation is for UX only.
- Parameterized queries only. No SQL built by string concatenation.
- Encode output for its context (HTML, URL, JSON).

## Authorization
- Every endpoint checks authorization itself. Default: deny.
- Error messages never expose internals (stack traces, SQL).

## Dependency risk
- Before adding a dependency: is it maintained, is the license OK, is it really needed?
- Pin versions (commit the lock file).
- Scan for known vulnerabilities regularly; critical ones are not deferred.

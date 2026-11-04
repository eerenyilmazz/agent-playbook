---
scope: task
when: Security-testing auth, payments, uploads, roles
owner: Eren
status: draft
---
# OWASP Checks (Testing)

QA **tests**; security-reviewer **reviews**. Rules: company/security-details.md. Based on OWASP Top 10 / ASVS (use current edition).

- **Access control:** swap ids (IDOR), lower-privilege role, other tenant, direct API calls bypassing UI.
- **Crypto/transport:** HTTPS only, HSTS, secure cookie flags, no sensitive data in URLs.
- **Injection:** SQL, XSS, command, template, header payloads in every input incl. file names.
- **Insecure design:** negative/huge values, step skipping, replay, race (parallel requests).
- **Misconfig:** no default creds, debug endpoints, directory listing, verbose errors; security headers present; CORS not `*` with credentials.
- **Components:** dependency scan clean of critical/high.
- **Auth:** brute-force limits, session expiry, logout invalidates, reset tokens single-use and expiring, no user enumeration.
- **Integrity:** uploads validated; no unsafe deserialization; webhooks signature-checked.
- **Logging:** security events present in audit trail.
- **SSRF:** URL inputs can't reach internal/metadata addresses.

Automate with a DAST scan (e.g. ZAP baseline) in CI for web apps.

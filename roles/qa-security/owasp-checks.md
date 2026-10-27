---
scope: task
role: qa-security
owner: Eren
status: draft
---
# OWASP Checks (Testing)

QA **tests** these; the security-reviewer **reviews code and design**. Base rules: company/security-basics.md.

Checklist based on the OWASP Top 10 (check the current edition):
- **Broken access control:** Change ids in URLs/requests to access others' data. Try actions with a lower-privilege role.
- **Cryptographic failures:** HTTPS everywhere, secure cookies (`Secure`, `HttpOnly`, `SameSite`), no sensitive data in URLs.
- **Injection:** Try SQL, script and command payloads in every input, including headers and file names.
- **Insecure design:** Business rules can't be bypassed (negative quantities, skipping steps, replaying requests).
- **Misconfiguration:** No default credentials, debug pages, directory listings or verbose errors in production. Security headers present.
- **Vulnerable components:** Dependency scan is clean of critical issues.
- **Authentication failures:** Brute-force protection, session expiry, logout invalidates the session, password reset can't be abused.
- **Integrity failures:** Uploaded files validated by type and size; no unsafe deserialization.
- **Logging failures:** Security events are logged (see templates/web-panel/audit-trail.md).
- **SSRF:** URL inputs can't reach internal addresses.

## Rules
- Run on every release touching auth, payments, uploads or permissions.

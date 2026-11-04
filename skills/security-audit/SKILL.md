---
name: security-audit
description: Audit a feature, PR or codebase for security issues in code, design, dependencies and secrets. Use before releases touching auth, payments, personal data, uploads or permissions, or on request.
---
# Security Audit

Rules: company/security-details.md. Checklists: roles/security-reviewer/abuse-cases.md, roles/security-reviewer/dependency-audit.md, roles/security-reviewer/secret-leak-check.md, roles/qa-security/owasp-checks.md. Threats: roles/qa-security/threat-modeling.md.

## Steps
1. **Scope.** List what's in: endpoints, data stores, integrations, roles. State what's out.
2. **Map.** Quick data-flow sketch with trust boundaries (reuse the feature's threat model if one exists).
3. **Secrets.** Run secret scan on the repo and history; check config, CI, bundles.
4. **Dependencies.** Run the ecosystem scanner; list critical/high with fix version.
5. **AuthN/AuthZ.** For each endpoint: who can call it, object-level check, tenant filter, rate limit.
6. **Input/output.** Validation, parameterized queries, encoding, uploads, deserialization, SSRF, redirects.
7. **Abuse cases.** Walk abuse-cases.md against the business logic.
8. **Config.** Headers, CORS, cookies, TLS, error verbosity, debug endpoints.
9. **Data.** Personal data in logs/analytics; encryption; retention (templates/software/data-and-privacy.md).
10. **Rate** each finding with roles/decision-maker/cost-risk-matrix.md.
11. **Report** and hand testable items to QA.

## Finding format
```
[Critical|High|Medium|Low] Title
Where: file:line / endpoint
Impact: what an attacker gets
Evidence: request / code snippet (no real secrets)
Fix: concrete change
Test: how QA verifies the fix
```

## Exit
Critical/High open → release no-go (roles/release-manager/release-process.md). Accepted risks recorded with owner.

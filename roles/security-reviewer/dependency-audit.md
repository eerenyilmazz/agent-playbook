---
scope: task
when: Adding or updating dependencies; vulnerability triage
owner: Eren
status: draft
---
# Dependency Audit

## New dependency
- Needed? Could stdlib or an existing dependency do it?
- Maintained: recent releases, active issues, > 1 maintainer.
- Not a typo-squat; verified publisher where available.
- License fits (watch GPL/AGPL in closed-source).
- Transitive weight acceptable; no surprising install scripts.

## Ongoing
- CI scanning (Dependabot / OWASP Dependency-Check / npm audit / OSV).
- SLA: critical immediately · high ≤ 7 days · medium/low in planning.
- Non-applicable CVE documented with reason, not silently ignored.
- Lock files committed; updates via PRs with green tests; batch minor updates regularly.
- SBOM generated for released artifacts.
- Unused dependencies removed.

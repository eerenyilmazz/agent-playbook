---
scope: task
role: security-reviewer
owner: Eren
status: draft
---
# Dependency Audit

Base rules: company/security-basics.md (Dependency risk).

## For a new dependency
- Is it necessary, or can the standard library / an existing dependency do it?
- Maintained? Recent releases, responsive to issues, more than one maintainer.
- Popular enough to be scrutinized; not a typo-squat of a known package name.
- License compatible with the project (watch copyleft licenses for closed-source work).
- Transitive dependencies reviewed: how much does it pull in?
- No install scripts doing unexpected things.

## Ongoing
- Automated vulnerability scanning in CI (e.g. Dependabot, OWASP Dependency-Check, npm audit).
- Severity SLA: critical fixed immediately, high within days, medium/low in normal planning.
- A vulnerability that doesn't apply (code path not used) is documented, not just ignored.
- Lock files are committed; updates come through PRs with passing tests.
- Unused dependencies are removed.

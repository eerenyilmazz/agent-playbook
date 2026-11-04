---
scope: task
when: Designing auth, payment, upload or data features
owner: Eren
status: draft
---
# Threat Modeling

Done at design time; one page per feature; updated when design changes.

## Steps
1. **Diagram:** components, data flows, trust boundaries.
2. **STRIDE at each boundary:** Spoofing · Tampering · Repudiation · Information disclosure · Denial of service · Elevation of privilege.
3. **Input:** roles/security-reviewer/abuse-cases.md.
4. **Rate:** roles/decision-maker/cost-risk-matrix.md.
5. **Mitigate** high/critical; accepted risks get an owner.
6. **Convert** mitigations into tests (owasp-checks.md, regression-suite.md).

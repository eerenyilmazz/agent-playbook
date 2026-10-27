---
scope: task
role: qa-security
owner: Eren
status: draft
---
# Threat Modeling

Done at design time for new features that touch auth, payments, personal data, uploads, external integrations or permissions.

## Steps
1. **Draw it:** A simple diagram of components, data flows and trust boundaries (where data crosses from untrusted to trusted).
2. **Ask STRIDE at each boundary:**
   - **S**poofing — can someone pretend to be another user/system?
   - **T**ampering — can data be changed in transit or at rest?
   - **R**epudiation — can someone deny an action? (audit trail)
   - **I**nformation disclosure — can data leak?
   - **D**enial of service — can it be overloaded?
   - **E**levation of privilege — can someone gain rights they shouldn't have?
3. **Rate** each threat with the cost-risk matrix (roles/decision-maker/cost-risk-matrix.md).
4. **Mitigate** high and critical threats; record accepted risks with an owner.
5. **Turn mitigations into tests** (owasp-checks.md, regression-suite.md).

## Rules
- Keep it short — one page per feature. Update it when the design changes.
- Abuse scenarios from roles/security-reviewer/abuse-cases.md are used as input.

---
scope: task
template: software
owner: Eren
status: draft
review: expert-required (legal / KVKK / GDPR)
---
# Data and Privacy

> Draft. Not legal advice. Must be reviewed by a qualified expert before being marked approved.

## Principles
- Collect only what the feature needs (data minimization).
- Every personal data field has a stated purpose and retention period.
- Personal data is never used for a new purpose without a new legal basis.

## Engineering rules
- Personal data is not written to logs. Mask or hash identifiers if needed.
- Sensitive data is encrypted at rest and always in transit (TLS).
- Access to personal data is role-based and audited.
- Test and staging environments use anonymized or synthetic data, never raw production data.
- Deletion requests must be technically possible: know every place the data is stored, including backups.

## Turkey (KVKK) / EU (GDPR) checklist
- Privacy notice (aydınlatma metni) shown where data is collected.
- Explicit consent recorded where it is the legal basis; consent can be withdrawn.
- Cross-border transfer of data (including cloud hosting abroad) checked with the expert.
- Data breach procedure known; regulators expect fast notification (KVKK: 72 hours). Confirm current rules with the expert.
- Registration obligations (e.g. VERBİS) checked with the expert.

## Owner
Each project names a person responsible for privacy decisions.

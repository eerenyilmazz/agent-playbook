---
scope: task
when: Handling personal data; logging, storage, retention, deletion
owner: Eren
status: draft
review: expert-required (KVKK/GDPR)
---
# Data and Privacy

> Draft, not legal advice. Needs expert sign-off before `approved`.

## Principles
- Collect only what the feature needs. Each personal field has a purpose, legal basis and retention period.
- No reuse for a new purpose without a new basis.

## Engineering
- No personal data in logs, URLs or analytics; mask/hash identifiers.
- Encrypt in transit (TLS) and at rest for sensitive data.
- Access is role-based and audited.
- Non-prod uses synthetic or anonymized data only.
- Maintain a data map: every store of personal data, including backups and third parties.
- Deletion and export requests must be executable from that map.
- Retention enforced by jobs, not by memory.

## KVKK / GDPR checklist (confirm with expert)
- Privacy notice (aydınlatma metni) at collection point.
- Explicit consent recorded and withdrawable where it's the basis.
- Cross-border transfer (incl. foreign cloud) reviewed.
- Breach notification: KVKK expects ~72 h; process known in advance.
- VERBİS registration obligation checked.

## Owner
Each project names the person accountable for privacy decisions.

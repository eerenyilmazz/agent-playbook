---
scope: task
when: Personal data: storage, logs, retention, transfers
owner: Eren
status: draft
review: expert-required (KVKK/GDPR)
verified: 2026-11-03 (secondary sources)
---
# Data and Privacy

> Not legal advice. Facts below checked against law-firm summaries on the verified date; confirm with an expert before `approved`.

## Principles
- Collect only what the feature needs. Each personal field has purpose, legal basis, retention period.
- No reuse for a new purpose without a new basis.

## Engineering
- No personal data in logs, URLs or analytics; mask/hash identifiers.
- Encrypt in transit (TLS) and at rest for sensitive data. Role-based, audited access.
- Non-prod: synthetic/anonymized data only.
- Data map of every store (incl. backups, processors, SDKs); deletion/export must run from it.
- Retention enforced by scheduled jobs.

## KVKK (Turkey)
- **Privacy notice** (aydınlatma metni) at every collection point; explicit consent recorded and withdrawable when it's the basis.
- **Breach:** notify the Board without delay and within **72 hours** of learning of it (Board decision 2019/10); notify affected persons as soon as reasonably possible. Keep an incident record either way.
- **Cross-border transfer** (incl. foreign cloud/SaaS, KVKK art. 9 as amended 2024): adequacy decision, or appropriate safeguards — Board's **standard contract unchanged**, BCRs, or undertaking — or narrow exceptions/occasional transfers. A signed standard contract must be **notified to the Authority within 5 business days**.
- **VERBİS:** exempt only if < 50 employees **and** balance sheet < 100M TL; if the main activity is processing special-category data (health etc.) the limits are < 10 employees and < 10M TL (decisions 2025/1572, 2025/2393). Otherwise register.

## GDPR (EU users)
Lawful basis per purpose · DPA with processors · breach notice to authority within 72 h · data subject rights within 1 month.

## Owner
Each project names the person accountable for privacy decisions.

---
scope: task
template: web-commerce
owner: Eren
status: draft
review: expert-required (accountant / lawyer)
---
# Tax, Returns and Compliance

> Draft. Not legal or tax advice. Every rule here must be confirmed by an accountant or lawyer before approval.

## Tax
- Tax rates are configuration, never hard-coded. Rates and categories change.
- Prices shown to consumers include tax; the breakdown is stored per order line.
- Invoicing (e-invoice / e-archive in Turkey) is integrated through an approved provider; confirm obligations with the accountant.

## Returns and withdrawal
- Consumer distance-sales rules apply (in Turkey: Mesafeli Sözleşmeler Yönetmeliği). A right of withdrawal applies to most products — confirm the current period and exceptions with the expert.
- Return reasons, dates and refund amounts are recorded and linked to the order.

## Required pages and texts
- Distance sales contract, preliminary information form, return/refund policy, privacy notice, cookie policy, terms of use.
- The customer explicitly accepts the required texts at checkout; the accepted version is stored with the order.

## Rules
- Legal texts are versioned. A change creates a new version; old orders keep theirs.
- Nothing in this file is "approved" until the owner field names the responsible expert.

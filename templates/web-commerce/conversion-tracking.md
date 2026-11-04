---
scope: task
when: Analytics events, funnels, tags, A/B tests
owner: Eren
status: draft
---
# Conversion Tracking

## Standard events
`view_item → add_to_cart → begin_checkout → add_payment_info → purchase` · plus `search`, `remove_from_cart`, `refund`.

## Rules
- One tracking plan defines every event and parameter; no ad-hoc events.
- `purchase` once per order (order id, value, currency, items); dedupe by order id.
- Send purchases server-side where possible; browser-only undercounts.
- No raw personal data in events.
- Consent first: no marketing/analytics tags before consent (Consent Mode or equivalent).
- Tag manager changes are reviewed and versioned like code.

## Quality
- New events verified in debug view before release.
- Weekly: analytics purchases vs real orders; alert above an agreed gap.

## A/B tests
Pre-define metric, sample size and duration. No early stopping. One change per test.

---
scope: task
template: web-commerce
owner: Eren
status: draft
---
# Conversion Tracking

## Funnel events (standard names)
`view_item` → `add_to_cart` → `begin_checkout` → `add_payment_info` → `purchase`.
Also: `search`, `remove_from_cart`, `refund`.

## Rules
- Event names and parameters are defined in one tracking plan; no ad-hoc events.
- `purchase` is sent once per order, with order id, value, currency and items. Deduplicate by order id.
- Server-side confirmation for purchases where possible; browser-only tracking undercounts.
- No personal data (email, phone, name) in analytics events unless hashed and legally allowed.
- Tracking respects cookie consent; no marketing tags before consent.

## Quality
- Every new event is tested in a debug view before release.
- Compare analytics purchases with real orders weekly; investigate gaps over a set threshold.

## Experiments
- A/B tests define the success metric and duration before starting.
- Don't stop a test early because it "looks good".

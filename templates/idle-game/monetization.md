---
scope: task
when: Ads, in-app purchases, subscriptions in games
owner: Eren
status: draft
review: expert-required (store policy/consumer law)
---
# Monetization

## Models
Rewarded ads (opt-in) · IAP (currency, boosts, remove ads) · optional pass/subscription. Interstitials rare, never at key moments.

## Rules
- Rewarded ads always optional with a clear fair reward.
- Server-side receipt validation before granting; handle refunds/revocations.
- Restore purchases for non-consumables and subscriptions.
- "Remove ads" removes forced ads permanently.
- Prices from the store (localized), never hard-coded.
- No dark patterns: fake timers, hidden costs, confusing currency conversion.
- Child audience: store family policies + child-directed ad settings; expert check.
- Paid random rewards: disclose odds; check local law.
- Ad consent (GDPR/UMP or equivalent) before personalized ads.

## Measure
ARPDAU, payer conversion, ads/DAU together with D1/D7/D30 retention. Never trade retention for short-term revenue.

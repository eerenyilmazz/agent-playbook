---
scope: task
when: Cart, inventory, pricing, discounts, order lifecycle
owner: Eren
status: draft
---
# Cart, Stock and Orders

## Cart
- Server computes all totals (price, discount, shipping, tax). Re-validate price and stock at checkout.
- Guest cart merges on login. Cart expires after a defined period.

## Stock
- Reserve at checkout start with TTL; release on timeout/failure.
- Atomic decrement or optimistic locking — no overselling.
- Every stock change logged with reason (sale, return, adjustment, reservation).

## Orders
- Snapshot name, price, tax, discount, address at purchase.
- Status changes via an explicit state machine; invalid transitions rejected.
- Human-readable unique order number; internal ids not exposed.
- Customer notified on key transitions.

## Pricing and discounts
- One pricing service; rules not in controllers/UI.
- Coupon limits (per user, total, date, min basket) enforced server-side and atomically.

Returns/legal: tax-returns-compliance.md. Payments: payment-flow.md.

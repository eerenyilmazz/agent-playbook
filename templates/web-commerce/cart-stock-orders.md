---
scope: task
template: web-commerce
owner: Eren
status: draft
---
# Cart, Stock and Orders

## Cart
- Prices and stock in the cart are re-validated at checkout; the client's numbers are never trusted.
- Guest carts merge into the user cart on login.
- Cart total is calculated on the server, including discounts, shipping and tax.

## Stock
- Stock is reserved at checkout start for a short, defined time, and released if payment doesn't complete.
- Stock decrements use atomic updates or optimistic locking to prevent overselling.
- Stock changes are logged with a reason (sale, return, manual adjustment).

## Orders
- An order snapshots product name, price, tax and address at the time of purchase; later product edits don't change it.
- Order status transitions are explicit and validated (state machine). Invalid transitions are rejected.
- Order numbers are human-readable and unique; internal ids are not exposed.
- Customers receive a confirmation for every key status change.

## Rules
- Price and discount logic lives in one service, not spread across controllers or UI.
- Cancellation and return rules: see tax-returns-compliance.md.

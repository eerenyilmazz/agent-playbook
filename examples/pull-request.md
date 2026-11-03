# Example: Pull Request

**Title:** `feat(orders): add partial refund endpoint`

```
## What
Adds POST /api/v1/orders/{orderId}/refunds for partial and full refunds from the admin panel.

## Why
Support currently refunds through the provider dashboard; refunds are not linked to orders (ticket ORD-142).

## Risk: medium
Touches payments. Mitigations: behind flag `orders.partial-refund` (off by default),
idempotency key required, new permission `orders.refund`, audited.

## Breaking: no
New endpoint and new nullable column `refunds.reason`. Existing APIs unchanged.

## Tests
- Unit: RefundPolicyTest (over-refund, currency mismatch, already refunded)
- Integration: RefundControllerIT with provider sandbox stub (success, decline, timeout, duplicate key)
- Manual: refunded 2 test orders on staging, verified provider report

## Rollback
Disable flag. Migration is additive (V42), no rollback needed.

## Checklist
- [x] OpenAPI updated  - [x] CHANGELOG  - [x] audit event added  - [x] no secrets/PII in logs
```

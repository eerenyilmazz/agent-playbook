---
scope: task
template: web-commerce
owner: Eren
status: draft
review: expert-required (payments / compliance)
---
# Payment Flow

> Draft. Payment provider and compliance details must be confirmed by an expert before approval.

## Rules
- Card data never touches our servers. Use the provider's hosted page or SDK (tokenization) to stay out of PCI DSS scope as much as possible.
- 3D Secure is supported and used where required.
- The source of truth for payment status is the provider's server-to-server callback (webhook), not the browser redirect.
- Webhooks are verified (signature) and processed idempotently.
- Every payment attempt has a unique idempotency key; retries never double-charge.
- Order state and payment state are separate: `pending → paid → fulfilled`, `failed`, `refunded`, `partially_refunded`.
- Amounts are stored as integers in minor units (kuruş/cents) with a currency code. No floating point.

## Failure handling
- Timeouts and unknown results are reconciled by querying the provider, not by guessing.
- A daily reconciliation compares our records with the provider's report.

## Refunds
- Refunds go through the provider API and are linked to the original payment.
- Refund permissions are separate and audited.

## Testing
- Test with the provider's sandbox: success, decline, 3DS challenge, timeout, duplicate webhook.

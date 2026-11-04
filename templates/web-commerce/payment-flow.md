---
scope: task
when: Payments, checkout, refunds, providers
owner: Eren
status: draft
review: expert-required (payments/compliance)
verified: 2026-11-03 (secondary sources)
---
# Payment Flow

> Draft. Provider and compliance details need expert confirmation.

## Rules
- Card data never touches our servers: hosted page/iframe or provider SDK tokenization (minimizes PCI DSS scope).
- PCI DSS 4.0.1 SAQ A (since 31 Mar 2025) still requires the page hosting the iframe/redirect to be protected from malicious scripts: keep a script inventory, strict CSP, Subresource Integrity on third-party scripts, and change monitoring on checkout pages.
- 3D Secure supported and used where required.
- Truth = provider webhook (signature-verified), not the browser redirect.
- Idempotency key per attempt; retries never double-charge. Webhooks processed idempotently.
- Money: integer minor units + ISO currency. No floats.
- Separate states: order (`pending → confirmed → fulfilled → cancelled`) and payment (`initiated → authorized → captured | failed | refunded | partially_refunded`).

## Failures
- Unknown/timeout result → query provider; never guess.
- Daily reconciliation vs provider report; mismatches alert.

## Refunds
Via provider API, linked to the original payment, separate permission, audited, partial refunds supported.

## Test (sandbox)
Success, decline, 3DS challenge, timeout, duplicate webhook, out-of-order webhook, partial refund.

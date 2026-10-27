---
scope: task
role: backend
owner: Eren
status: draft
---
# Idempotency and Queues

## Idempotency
- Any operation a client may retry (payments, orders, webhooks) accepts an idempotency key.
- The server stores the key with the result; a repeated key returns the same result without repeating the side effect.
- Keys expire after a defined period.
- Consumers of messages and webhooks are idempotent: processing the same message twice has no extra effect.

## Queues and messaging
- Assume at-least-once delivery. Exactly-once is not guaranteed; idempotency handles duplicates.
- Use the transactional outbox pattern when a DB change and a message must both happen.
- Retries use exponential backoff with a max attempt count.
- Messages that keep failing go to a dead-letter queue, with alerting. DLQs are monitored and handled, not ignored.
- Message schemas are versioned; consumers tolerate unknown fields. Breaking schema changes need a new version.
- Message ordering is only assumed where the broker guarantees it (e.g. per partition key).

## Observability
- Track queue depth, consumer lag, processing time and DLQ count.

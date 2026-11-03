---
scope: task
when: Retries, webhooks, messaging, background jobs
owner: Eren
status: draft
---
# Idempotency and Queues

## Idempotency
- Retryable writes (payments, orders, webhooks) accept an `Idempotency-Key`.
- Store key + request hash + result; same key → same result, no repeat side effect; different body with same key → 422.
- Keys expire after a defined window.
- All consumers idempotent (dedupe by message id or natural key).

## Messaging
- Assume at-least-once. Duplicates handled by idempotency.
- DB change + message → transactional outbox.
- Retries: exponential backoff + jitter, max attempts → dead-letter queue with alert.
- Versioned schemas; consumers ignore unknown fields; breaking change = new version/topic.
- Order only where the broker guarantees it (partition key).
- Poison messages never block the queue.

## Jobs
Scheduled jobs: single-run guarantee (lock/leader), resumable, and observable.

## Observe
Queue depth, consumer lag, processing time, DLQ size.

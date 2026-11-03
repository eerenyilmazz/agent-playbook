# Example: ADR

```
# 0007. Use transactional outbox for order events
Status: accepted
Date: 2026-10-12 · Deciders: backend lead, decision-maker

## Context
Order service saves orders and then publishes OrderCreated to the broker. When the broker is
down after the DB commit, events are lost (3 incidents in Q3). Billing and email depend on them.

## Decision
Write events to an `outbox` table in the same transaction as the order; a relay publishes them
and marks them sent. Consumers deduplicate by event id.

## Options
- Publish after commit (current) — loses events on broker failure.
- Distributed transaction (XA) — heavy, poor broker support, slows writes.
- Change data capture (Debezium) — robust but new infrastructure we don't run yet.
- Do nothing — incidents continue.

## Consequences
+ No lost events; replay possible.
− Extra table and relay job; events delayed by relay interval (~1 s).
− Consumers must be idempotent (already required by playbook).

## Risk
Medium — relay failure stalls events. Mitigation: relay lag metric + alert at 60 s.

## Rollback
Switch the relay off and re-enable direct publish (kept behind flag for one release).
Outbox table stays; drop it in a later migration.
```

---
scope: task
when: Any schema or data change in a server database
owner: Eren
status: draft
---
# Database Migrations

Procedure: db-migration skill.

## Rules
- Only via Flyway/Liquibase. No manual changes in any environment.
- Applied migrations are immutable; fix forward.
- Additive by default. Rename/drop only through expand/contract.
- Each PR states: reversible? rollback script or data-loss risk.
- Must run while old and new app versions are live (zero downtime).
- Schema and large data backfills in separate migrations.

## Expand / contract
1. Expand: add new column/table; app writes both.
2. Backfill in batches.
3. Switch reads to new.
4. Contract in a later release: remove old.

## Safety
- New `NOT NULL`: add nullable → backfill → constrain (or with a cheap default).
- Big tables: online/concurrent index creation; batched updates; lock timeout set.
- Rehearse on production-sized copy; measure duration.
- Backup verified before destructive steps.

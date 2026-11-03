---
name: db-migration
description: Plan, write, test and run a zero-downtime server database migration (Flyway/Liquibase), including expand/contract for breaking changes. Use for any schema or bulk data change.
---
# DB Migration

Rules: roles/backend/database-migrations.md. Desktop/local data: templates/desktop/local-data-migration.md.

## 1. Classify
| Change | Type |
|---|---|
| Add table, nullable column, index | Additive — single release |
| Add NOT NULL column | Additive in 3 steps (nullable → backfill → constraint) |
| Rename/drop/retype column or table | Breaking — expand/contract over ≥ 2 releases |
| Bulk data update | Data migration — batched, separate from schema |

State in the PR: type, reversible (yes/no), data-loss risk, estimated duration.

## 2. Write
- New versioned file; never edit an applied one.
- Large tables: concurrent/online index; set `lock_timeout`; batch updates (e.g. 1–10k rows) with commits between batches.
- Write the rollback script, or state why it's impossible.

## 3. Expand / contract (breaking only)
1. Release A: add new structure; app writes old + new.
2. Backfill job in batches; verify counts match.
3. Release B: app reads new.
4. Release C (after B is stable): drop old.
Each step independently deployable and rollback-safe.

## 4. Test
- Run on a fresh DB and on a production-sized copy; record duration and locks.
- Run app tests on the migrated schema.
- Check old app version still works on the new schema.

## 5. Run
- Verified backup/snapshot before destructive steps.
- Run via the pipeline, not by hand; watch locks, replication lag, error rates.
- Failure → stop, roll back per plan, open incident if users are affected.

## 6. Close
Verify data; ticket the contract step; update docs/ADR if the model changed.

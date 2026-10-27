---
scope: task
role: backend
owner: Eren
status: draft
---
# Database Migrations

Step-by-step procedure: db-migration skill. This file defines the rules.

## Rules
- All schema changes go through a migration tool (Flyway / Liquibase). No manual changes in any environment.
- Applied migrations are never edited. Fix forward with a new migration.
- Prefer additive changes: add columns/tables; avoid renames and drops.
- Every migration has a rollback plan. If it can't be reversed, state the data-loss risk in the PR.
- Migrations must work with both the old and new application version running (zero-downtime).

## Expand / contract for breaking changes
1. **Expand:** Add the new column/table. App writes to both old and new.
2. **Migrate:** Backfill data in batches.
3. **Switch:** App reads from the new one.
4. **Contract:** In a later release, remove the old column.

## Safety
- New `NOT NULL` columns get a default or are added nullable then backfilled.
- Large tables: create indexes concurrently/online; backfill in small batches.
- Test the migration on a copy of production-sized data before release.
- Back up before any destructive migration.

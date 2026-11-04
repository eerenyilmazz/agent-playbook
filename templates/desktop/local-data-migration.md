---
scope: task
when: Desktop local data, paths, shutdown, logs
owner: Eren
status: draft
---
# Local Data Migration

Server DB migrations: roles/backend/database-migrations.md.

## Rules
- Local data carries a schema version.
- On startup, run migrations in order from stored to current version.
- Back up before migrating; restore on failure.
- Migrations idempotent; tested against real samples from every released version (kept in repo, run in CI).
- Never delete user data without explicit user action.
- Newer-than-known version (downgrade) detected: don't write, show a clear message.

## Locations
- OS-standard app data dir, never the install dir.
- Document every storage location so reset/uninstall are complete.

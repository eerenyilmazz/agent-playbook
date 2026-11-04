---
scope: task
when: Desktop apps: local database, settings, file formats, cross-platform paths, shutdown, logs
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

## Cross-platform and shutdown
- Handle path separators, line endings and filename case across Windows, macOS, Linux.
- On quit, finish or safely cancel running work; never leave half-written files.
- Logs and crash reports in a known location, free of user data and secrets.

## Locations
- OS-standard app data dir, never the install dir.
- Document every storage location so reset/uninstall are complete.

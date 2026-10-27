---
scope: task
template: desktop
owner: Eren
status: draft
---
# Local Data Migration

Server-side database migrations: roles/backend/database-migrations.md.

## Rules
- Local data (database, settings, files) has a schema version number.
- On startup, the app runs migrations in order from the stored version to the current one.
- Back up the local data before migrating; restore it if the migration fails.
- Migrations are idempotent and tested with real old-version data samples.
- Never delete user data in a migration without explicit user action.
- Unknown newer versions (user downgraded) are detected: don't corrupt, show a clear message.

## Locations
- Use the OS-standard app data directory, not the install directory.
- Document every place the app stores data, so uninstall and reset work.

## Testing
- Keep sample data files from each released version; CI migrates them to the latest version.

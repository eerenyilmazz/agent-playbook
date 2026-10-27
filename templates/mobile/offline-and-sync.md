---
scope: task
template: mobile
owner: Eren
status: draft
---
# Offline and Sync

## Decide per feature
For each feature, state: works offline / read-only offline / online only. Document it.

## Rules
- Local database is the UI's source of truth for offline features; network updates it.
- Writes made offline go to an outbox queue with a client-generated id, sent when online.
- The server handles retries idempotently using that id.
- Conflict policy is defined per entity: last-write-wins, server-wins, or merge. Never undefined.
- Sync is incremental (changes since a timestamp/version), not full downloads.
- The user sees sync status: pending changes, last synced time, failures.
- Network calls have timeouts and exponential backoff; no tight retry loops draining battery.

## Local data
- Local schema has versioned migrations; app updates never lose unsynced data.
- Clear local data on logout if it belongs to the user.

## Testing
- Test airplane mode, flaky network, app killed mid-sync, and two devices editing the same item.

---
scope: task
when: Offline support, local storage, data sync on mobile
owner: Eren
status: draft
---
# Offline and Sync

## Per feature, declare
Offline full · offline read-only · online only. Documented in the feature spec.

## Rules
- Local DB is the UI source for offline features; network updates it.
- Offline writes → outbox with client-generated UUID; server processes idempotently.
- Conflict policy per entity: last-write-wins, server-wins, or merge — never undefined.
- Incremental sync via version/updated-at cursor; deletes synced as tombstones.
- Timeouts + exponential backoff with jitter; respect battery/data saver; sync via OS background schedulers.
- Visible sync status: pending, last synced, failed (with retry).

## Local data
- Versioned schema migrations; never lose unsynced data on update.
- Clear user data on logout.

## Test
Airplane mode, flaky network, kill mid-sync, two devices editing one item, clock skew.

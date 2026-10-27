---
scope: task
template: desktop
owner: Eren
status: draft
---
# Auto Update

Release procedure: electron-release skill. This file defines the rules.

## Rules
- Updates are signed; the app verifies the signature before installing.
- Updates are served over HTTPS from a controlled location.
- Release channels: stable and beta at minimum. Users choose; default is stable.
- Staged rollout for stable when the update server supports it.
- The app never updates in the middle of user work: download in background, install on restart or with user consent.
- A failed update leaves the current version working; the user is informed.
- A minimum-supported-version check exists to force updates for critical security fixes.

## Compatibility
- Local data format changes include a migration (see local-data-migration.md).
- Downgrading is not supported unless explicitly designed; document it.

## Monitoring
- Track update success/failure rates and version distribution.

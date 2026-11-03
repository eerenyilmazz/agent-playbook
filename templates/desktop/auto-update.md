---
scope: task
when: Desktop app update mechanism and release channels
owner: Eren
status: draft
---
# Auto Update

Release procedure: electron-release skill.

## Rules
- Updates signed; app verifies signature before install. HTTPS only, controlled host.
- Channels: stable (default) and beta.
- Staged rollout on stable when supported; ability to pause a rollout.
- Download in background; install on restart or with consent — never mid-work.
- Failed update leaves the current version working and informs the user.
- Minimum-supported-version check for critical security fixes.
- Delta updates where supported to cut download size.

## Compatibility
- Local data changes ship with migrations (local-data-migration.md).
- Downgrade unsupported unless designed; documented.

## Monitor
Update success/failure rate, version distribution, crash rate per version.

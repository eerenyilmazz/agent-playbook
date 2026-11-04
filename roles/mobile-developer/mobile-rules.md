---
scope: task
when: Writing iOS/Android/cross-platform app code
owner: Eren
status: draft
---
# Mobile Developer Rules

Project rules: templates/mobile/.

## Architecture
- UI · presentation/state · data layers separated; no network/DB from UI.
- Follow the existing pattern (e.g. MVVM); new framework needs an ADR.
- Central navigation; deep links tested.

## Rules
- Main thread for UI only. Touch targets ≥ 44 pt (iOS) / 48 dp (Android).
- Survive lifecycle: background, process death, restore, rotation — no lost input.
- Every network call: timeout, error state, retry.
- Secrets in Keychain/Keystore; none in the bundle.
- Images sized and cached; lists virtualized; startup time tracked (cold start target set per project).
- Old app versions keep working against the API.
- Crash reporting + analytics before first release.
- Risky features behind remote flags.

## Tests
Unit for presentation/data; UI tests for critical flows; real devices from the device matrix before release.

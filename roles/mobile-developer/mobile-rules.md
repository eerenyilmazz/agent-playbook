---
scope: task
role: mobile-developer
owner: Eren
status: draft
---
# Mobile Developer Rules

Project rules: templates/mobile/ (store-release, permissions-and-privacy, offline-and-sync, device-matrix).

## Architecture
- Separate UI, state/presentation and data layers. No network or database calls from UI code.
- Follow the project's existing architecture (e.g. MVVM). No new framework without an ADR.
- Navigation in one place; deep links tested.

## Rules
- Main thread is for UI only; I/O and heavy work run in the background.
- Handle lifecycle correctly: background, kill, restore, rotation. No lost user input.
- Every network call: timeout, error state, retry option.
- Sensitive data in Keychain/Keystore; no secrets in the app bundle.
- Images sized and cached; lists virtualized.
- Old app versions keep working against the API (backward compatibility).
- Crash reporting and basic analytics integrated before the first release.
- Feature flags for risky features (mobile can't roll back instantly).

## Testing
- Unit tests for presentation and data logic; UI tests for critical flows.
- Test on real devices from the device matrix before release.

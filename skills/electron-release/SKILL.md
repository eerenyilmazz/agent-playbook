---
name: electron-release
description: Build, sign, notarize and publish a desktop (Electron or similar) release with auto-update and staged rollout. Use when shipping a desktop app version.
---
# Desktop Release

Rules: templates/desktop/signing-and-notarization.md, templates/desktop/auto-update.md, templates/desktop/local-data-migration.md. General gates: release-checklist skill.

## Steps
1. **Prepare.** Release checklist gates passed. Version bumped (SemVer) in package metadata; changelog ready.
2. **Migrations.** Local data migrations tested against sample data from every released version (CI green).
3. **Build in CI** from tag `vX.Y.Z` for each target (macOS arm64/x64, Windows x64, Linux).
4. **Sign:**
   - macOS: Developer ID + hardened runtime → notarize → staple → verify with `spctl -a -vv` and `stapler validate`.
   - Windows: sign binaries and installer with timestamp → verify with `signtool verify /pa`.
   - Linux: sign packages or publish SHA-256 checksums.
5. **Electron hardening check:** `contextIsolation` on, `nodeIntegration` off in renderers, sandbox on, strict CSP, no remote content with Node access, Electron version supported.
6. **Smoke test** each installer on a clean VM: installs without warnings, launches, updates from previous version, existing user data intact.
7. **Publish** to beta channel first; collect crash/update metrics.
8. **Stable rollout** staged (e.g. 10% → 50% → 100%); pause if crash or update-failure rate rises.
9. **Close:** release notes published, download page updated, old artifacts retained for rollback.

## Rollback
Pause rollout; publish previous version as a newer build number if users must be moved back (auto-updaters don't downgrade).

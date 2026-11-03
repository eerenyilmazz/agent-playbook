---
scope: task
when: Building desktop installers for distribution
owner: Eren
status: draft
---
# Signing and Notarization

## macOS
Developer ID certificate · hardened runtime · minimal entitlements · notarized · ticket stapled.

## Windows
Code signing certificate (keys now required on HSM/hardware token or cloud signing service) · every signature timestamped · signed installer and binaries.

## Linux
Signed packages or published checksums (SHA-256).

## Rules
- Sign only in CI; keys in secret manager/HSM, never in repo or laptops.
- Track cert expiry with reminders ≥ 30 days ahead.
- Unsigned/un-notarized builds never reach users.
- Verify on a clean machine: opens without OS warnings.

---
scope: task
template: desktop
owner: Eren
status: draft
---
# Signing and Notarization

## macOS
- Signed with a Developer ID certificate, hardened runtime enabled.
- Notarized by Apple and the ticket stapled to the app/installer.
- Entitlements limited to what the app needs.

## Windows
- Signed with a code signing certificate (EV or OV; EV builds SmartScreen reputation faster).
- Timestamp every signature so it stays valid after the certificate expires.

## Linux
- Packages (deb/rpm/AppImage) signed or published with checksums.

## Rules
- Signing happens only in CI. Certificates and keys live in a secret manager or hardware token, never in the repo.
- Certificate expiry dates are tracked with reminders well in advance.
- An unsigned or un-notarized build never reaches users.
- After signing, verify on a clean machine that the OS opens the app without warnings.

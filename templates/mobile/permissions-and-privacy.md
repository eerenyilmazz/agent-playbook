---
scope: task
when: Mobile permissions, SDKs, tracking, on-device data
owner: Eren
status: draft
review: expert-required (privacy)
---
# Permissions and Privacy (Mobile)

General rules: templates/software/data-and-privacy.md.

## Permissions
- Only what's needed; request in context, never all at launch.
- Pre-permission screen explains the benefit.
- Denial handled gracefully with a path to Settings.
- Specific usage strings (iOS) and rationale (Android).
- Extra review for background location, contacts, photos, mic, camera.
- Prefer limited/partial access (photo picker, approximate location) when enough.

## Privacy
- Store disclosures match the actual data flow, including SDKs.
- Each SDK reviewed for data collection before adding; iOS privacy manifest present.
- Cross-app tracking only with ATT consent (iOS).
- Secrets/tokens in Keychain/Keystore, never plain prefs or bundle.
- In-app account deletion when sign-up exists.
- Screens with sensitive data excluded from screenshots/app switcher where needed.

---
scope: task
template: mobile
owner: Eren
status: draft
review: expert-required (privacy)
---
# Permissions and Privacy

General privacy rules: templates/software/data-and-privacy.md.

## Permissions
- Ask only for permissions the app truly needs, and only at the moment the feature is used (not on first launch).
- Explain why before the system prompt (pre-permission screen).
- The app keeps working when a permission is denied; the feature degrades gracefully with a way to enable it later.
- Usage description strings (iOS) and permission rationale (Android) are clear and specific.
- Background location, contacts, photos and microphone get extra review before being added.

## Privacy
- Store disclosures (App Privacy details, Data safety form) match the real data flow, including third-party SDKs.
- Every third-party SDK is reviewed for what it collects before adding.
- Tracking across apps requires the platform's tracking consent (e.g. iOS ATT).
- Sensitive data stored in the platform secure storage (Keychain / Keystore), not plain preferences.
- Account deletion is available inside the app if accounts can be created.

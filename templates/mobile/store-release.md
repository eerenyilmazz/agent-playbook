---
scope: task
when: Publishing or updating an iOS/Android app
owner: Eren
status: draft
---
# Store Release

Procedure: store-submission skill.

## Build
- Version name SemVer; build number strictly increasing.
- Built and signed in CI from a tag, never locally.
- Signing keys/certs in a secret manager; backup + access list documented. Android: Play App Signing enabled.

## Listing
- Description, screenshots, age rating, privacy labels / Data safety form match real behavior (incl. SDKs).
- Live privacy policy URL; account deletion path if accounts exist.
- Target API level / SDK requirements of the current store deadline met.

## Rollout
- Internal → TestFlight/closed track → staged production (e.g. 5 → 20 → 50 → 100%).
- Halt if crash-free users fall below the agreed threshold (e.g. 99.5%) or ANRs spike.

## Rules
- No instant rollback on mobile: risky features behind remote flags.
- Backend stays compatible with all supported app versions.
- Forced/soft update mechanism exists.
- Log every review rejection and fix.

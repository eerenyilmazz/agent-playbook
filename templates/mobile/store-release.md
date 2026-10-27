---
scope: task
template: mobile
owner: Eren
status: draft
---
# Store Release

Step-by-step procedure: store-submission skill. This file defines the rules.

## Before submission
- Version name (SemVer) and build number incremented; build number always increases.
- Release built in CI from a tagged commit, never from a laptop.
- Signing keys and certificates stored in a secret manager; access is limited and documented. Losing the Android upload key or Apple certificates blocks releases.
- Store listing updated: description, screenshots, privacy details/data safety form, age rating.
- Privacy policy URL is live and matches what the app actually collects.

## Rollout
- Internal / TestFlight / closed testing first.
- Staged rollout on production (e.g. 5% → 20% → 50% → 100%), watching crash rate and reviews at each step.
- Halt the rollout if crash-free users drop below the agreed threshold.

## Rules
- Mobile releases can't be rolled back instantly. Risky features ship behind remote feature flags.
- Keep backend APIs backward compatible with older app versions still in use.
- A forced-update mechanism exists for critical fixes.
- Review guideline rejections are logged with the fix, so they aren't repeated.

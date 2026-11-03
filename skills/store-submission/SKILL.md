---
name: store-submission
description: Prepare and submit an iOS App Store or Google Play release, from build to staged rollout. Use when publishing or updating a mobile app.
---
# Store Submission

Rules: templates/mobile/store-release.md, templates/mobile/permissions-and-privacy.md, templates/mobile/device-matrix.md. General gates: release-checklist skill.

## Steps
1. **Gates.** QA sign-off on the device matrix; no Critical/High security findings; backend compatible with the new and all supported old versions.
2. **Version.** SemVer version name; build number incremented.
3. **Build in CI** from tag; signed (iOS distribution cert + profile; Android upload key, Play App Signing).
4. **Compliance check:**
   - Target SDK / Xcode / API level meets current store requirements.
   - iOS privacy manifest and Play Data safety form match actual data use (incl. SDKs).
   - Permission strings specific; account deletion available if sign-up exists.
   - Privacy policy URL live.
5. **Listing.** Release notes (user language), screenshots if UI changed, age rating, review notes + demo account for reviewers.
6. **Test track.** TestFlight / internal or closed testing; smoke test on real devices; check crash reporting receives data.
7. **Submit** for review. Rejection → log reason + fix in the release notes file; resubmit.
8. **Staged rollout:** e.g. 5% → 20% → 50% → 100% over days; check crash-free users, ANRs, reviews at each step.
9. **Halt** if thresholds breached; ship fix as a new build (no store rollback). Use remote flags to disable bad features immediately.
10. **Close.** Tag recorded; release notes published; minimum supported version updated if needed.

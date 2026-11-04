---
scope: task
when: QA planning tests, release sign-off
owner: Eren
status: draft
---
# Regression Suite

Boundary: **QA tests running software.** Code/design review is security-reviewer and code-reviewer. Test layers: templates/software/test-pyramid.md.

## Sets
- **Smoke (minutes):** login, main screen, core flow. Every deploy.
- **Core (automated):** critical journeys + every escaped bug. Every PR or nightly.
- **Release:** core + exploratory testing of changed areas.

## Rules
- Test in risk order: data loss, money, permissions, most-used flows first; test neighbors of changed code too.
- Every finding: steps, expected, actual, environment, evidence (output or screenshot).
- Each production bug adds a regression test before closing.
- Flaky tests fixed or quarantined within 2 working days.
- Tests own their data (seeded/created); no manual setup.
- Obsolete tests removed with the feature, noted in PR.
- Smoke or core failure blocks release.

## Sign-off
Tested · not tested · known issues · risk level · go/no-go recommendation.

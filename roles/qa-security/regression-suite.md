---
scope: task
role: qa-security
owner: Eren
status: draft
---
# Regression Suite

Test layers and general rules: templates/software/test-pyramid.md.

## Contents
- **Smoke set (minutes):** Can users log in, reach the main screen, complete the core flow? Runs on every deploy.
- **Core regression (automated):** Critical journeys and every bug that reached production. Runs on every PR or nightly.
- **Full regression (before release):** Core + manual checks for areas changed in the release.

## Rules
- Every production bug adds a regression test before the fix is closed.
- Flaky tests are fixed or quarantined within a set time; a flaky suite gets ignored.
- The suite is maintained: obsolete tests are removed when features are removed, with a note.
- Release is blocked if smoke or core regression fails.
- Test data is created by the tests (or seeded), not dependent on manual setup.

## Release sign-off
QA signs off with: what was tested, what wasn't, known issues, and risk level.

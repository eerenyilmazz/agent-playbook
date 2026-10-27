---
scope: task
template: software
owner: Eren
status: draft
---
# Test Pyramid

## Layers
- **Unit (most):** One class/function, no I/O, milliseconds. Business rules live here.
- **Integration (some):** Real database, queue or HTTP boundary (e.g. Testcontainers). Verifies wiring and queries.
- **End-to-end (few):** Critical user journeys only (login, checkout, core flow). Slow and brittle; keep the count low.

## Rules
- Existing tests must never be deleted or weakened to make a change pass.
- Every bug fix ships with a test that fails before the fix.
- Tests are deterministic: no real time, randomness or network without control.
- Test names describe behavior: `returnsZeroWhenCartIsEmpty`.
- One reason to fail per test.

## What to test
- Business rules, edge cases, error paths, boundaries (0, 1, max, null, empty).
- Not getters/setters or framework code.

## Coverage
- Coverage is a signal, not a goal. New code: meaningful tests for every branch of business logic.
- A drop in coverage on a PR is explained in the PR description.

## Regression
The regression suite is owned by QA: see roles/qa-security/regression-suite.md.

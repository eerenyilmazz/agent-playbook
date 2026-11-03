---
name: test-writing
description: Write unit, integration or contract tests for new code, bug fixes or legacy code before refactoring. Use whenever tests are needed or missing.
---
# Test Writing

Rules: templates/software/test-pyramid.md.

## Steps
1. **Pick the layer.** Pure logic → unit. Query/mapping/transaction → integration. API/event consumed by others → contract. Critical journey → E2E (rarely).
2. **List cases** before coding: happy path · each business rule · boundaries (null, empty, 0, 1, max) · invalid input · unauthorized · failure of each dependency.
3. **Bug fix:** write the test that reproduces the bug; see it fail; then fix.
4. **Legacy code before refactor:** write characterization tests that lock current behavior (even odd behavior); refactor only when green.
5. **Structure:** Arrange · Act · Assert. One behavior per test. Name: `<does>When<condition>`.
6. **Isolation:** inject clock, ids, randomness. Mock only boundaries you own the contract of; prefer real DB via Testcontainers over mocking repositories.
7. **Data:** builders/factories with sensible defaults; set only what the test cares about.
8. **Assertions:** assert outcomes and state, not internal calls, unless the call is the behavior (e.g. message published).
9. **Run** the whole suite; check new tests fail if the code is broken (flip a condition once).
10. **Speed:** unit < 100 ms each; slow tests tagged and moved to nightly.

## Done when
Every case from step 2 is covered or consciously skipped (noted in PR); no existing test weakened.

---
scope: task
when: Writing or changing tests; planning test coverage
owner: Eren
status: draft
---
# Test Pyramid

## Layers
- **Unit (most):** no I/O, ms each. All business rules and edge cases.
- **Integration (some):** real DB/broker/HTTP via Testcontainers or similar. Queries, mappings, transactions.
- **Contract (APIs/events):** consumer-driven or schema tests so providers can't silently break clients.
- **E2E (few):** critical journeys only.

## Rules
- Never delete or weaken an existing test to pass a change.
- Bug fix = test that fails before the fix.
- Deterministic: inject clock and randomness; no real external network.
- Name by behavior: `rejectsOrderWhenStockIsZero`. One reason to fail.
- Cover boundaries: null, empty, 0, 1, max, invalid, unauthorized.
- Skip trivial code (getters, framework wiring).

## Coverage
Signal, not target. Business-logic branches must be covered; a coverage drop is explained in the PR.

## CI budget
Unit + integration under 10 min on PRs. Slow suites run nightly.

Regression suite ownership: roles/qa-security/regression-suite.md.

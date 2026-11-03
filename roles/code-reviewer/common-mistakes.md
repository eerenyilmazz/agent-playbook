---
scope: task
when: Reviewing any pull request
owner: Eren
status: draft
---
# Common Mistakes

Look for these in every review. Label each comment: **blocker** · **should** · **nit**.

## Correctness
Unhandled null/empty · off-by-one · float money · time-zone-less dates · race conditions · behavior change hidden in a refactor.

## Contracts
Entity in API response · field renamed/removed/meaning changed without breaking flag · enum value removed · migration without expand/contract · changed log format.

## Architecture
Logic in controller/template · field injection · single-use abstraction · cross-layer calls · new dependency without justification.

## Transactions and performance
Unjustified `@Transactional` change · external call in transaction · N+1 · unbounded list · missing index · blocking call on hot path.

## Errors and logs
Swallowed exception · log-and-rethrow · secrets/PII in logs · wrong log level.

## Tests
No test for the fix · weakened/deleted tests · time/order/network dependent tests.

## Hygiene
Magic values · commented-out code · debug leftovers · unrelated changes · TODO without ticket.

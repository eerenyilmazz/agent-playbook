---
scope: task
role: code-reviewer
owner: Eren
status: draft
---
# Common Mistakes

Review rubric lives in the existing review-rubric file. This is the list of mistakes to actively look for.

## Correctness
- Null/empty not handled; off-by-one at boundaries.
- Money as floating point; dates without time zone.
- Changed behavior hidden inside a "refactor".

## API and data
- Entity exposed in an API response instead of a DTO.
- API field renamed/removed or meaning changed without being flagged as breaking.
- Migration that drops or renames without expand/contract.

## Architecture
- Business logic in controllers or templates.
- Field injection instead of constructor injection.
- New abstraction with a single implementation and no reason.

## Transactions and performance
- `@Transactional` added/removed without reason; external calls inside a transaction.
- N+1 queries; unpaginated lists; missing index on a new query.

## Errors and logs
- Swallowed exceptions; logging and rethrowing (double logs).
- Secrets or personal data in logs; changed log formats.

## Tests
- No test for the fix; tests weakened or deleted to pass.
- Tests depending on real time, order or network.

## Hygiene
- Magic numbers/strings; commented-out code; leftover debug output; unrelated changes in the same PR.

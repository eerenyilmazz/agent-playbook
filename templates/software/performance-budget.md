---
scope: task
template: software
owner: Eren
status: draft
---
# Performance Budget

Numbers below are defaults. A project may override them in its own README.

## Backend
- API p95 latency: < 300 ms for reads, < 800 ms for writes.
- No N+1 queries. Every list endpoint is paginated.
- Every database query on a hot path uses an index; check with `EXPLAIN`.
- External calls have timeouts and are never made inside a DB transaction.

## Frontend
- Largest Contentful Paint (LCP): < 2.5 s.
- Interaction to Next Paint (INP): < 200 ms.
- Cumulative Layout Shift (CLS): < 0.1.
- Initial JS bundle: watch growth; a PR adding > 50 KB gzipped explains why.

## Rules
- Measure before optimizing. No speculative optimization.
- A regression beyond the budget blocks release unless the decision-maker accepts it in writing.
- Load tests run before launches and major traffic changes.
- Caching is added only with a clear invalidation rule.

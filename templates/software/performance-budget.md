---
scope: task
when: Endpoints, queries, pages; performance
owner: Eren
status: draft
---
# Performance Budget

Defaults; a project may override in its README.

## Backend
- p95: reads < 300 ms, writes < 800 ms. p99 tracked.
- No N+1. Every list is paginated (max page size enforced).
- Hot-path queries use an index — verify with `EXPLAIN`.
- Timeouts on every outbound call; circuit breaker for unstable dependencies.
- No external calls inside DB transactions. Keep transactions short.
- Connection pools sized and monitored.

## Frontend (Core Web Vitals, p75)
- LCP < 2.5 s · INP < 200 ms · CLS < 0.1.
- PR adding > 50 KB gzipped JS explains why. Lazy-load routes.

## Rules
- Measure first (profiler, APM, `EXPLAIN`); no speculative optimization.
- Cache only with a defined key, TTL and invalidation rule.
- Exceeding budget blocks release unless the decision-maker accepts it in writing.
- Load-test before launches and expected traffic spikes.

---
name: perf-profile
description: Find and fix a performance problem with measurement — backend latency, slow queries, frontend Web Vitals or game frame time. Use when something is slow or a budget is exceeded.
---
# Performance Profiling

Budgets: templates/software/performance-budget.md, templates/game/performance-and-fps.md.

## Steps
1. **Define.** Which operation, which metric (p95, LCP, frame time), current value, target, environment.
2. **Reproduce** with production-like data and load. No repro → add instrumentation first.
3. **Measure, don't guess.** Pick the tool:
   - Backend: APM/traces, JFR/async-profiler, slow query log, `EXPLAIN (ANALYZE)`.
   - Frontend: Lighthouse, DevTools Performance, bundle analyzer, RUM data.
   - Game: engine profiler on target device, GPU frame capture.
4. **Locate the biggest cost.** Usually one of: N+1/missing index · external call · lock contention · serialization · large payload · render blocking resources · per-frame allocation/draw calls.
5. **Hypothesis → one change.** Smallest fix for the biggest cost. No unrelated tweaks.
6. **Re-measure** same setup. Keep only changes with real gain; revert the rest.
7. **Guard.** Add a regression check (benchmark, query count assertion, Lighthouse budget, perf test).
8. **Record** before/after numbers in the PR.

## Common fixes (in order of preference)
Remove work → do it once (fetch join, batch) → index → cache with clear invalidation → async/background → scale hardware.

## Rules
Measure first. Correctness over speed. Caching and concurrency changes count as medium risk minimum.

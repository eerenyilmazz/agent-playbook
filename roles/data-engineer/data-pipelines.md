---
scope: task
role: data-engineer
owner: Eren
status: draft
---
# Data Pipelines

Privacy rules: templates/software/data-and-privacy.md.

## Design
- Every pipeline has: source, owner, schedule, destination, freshness target, and what happens on failure.
- Pipelines are idempotent: re-running for the same period gives the same result (no duplicates).
- Incremental loads by watermark/partition, with the ability to backfill a date range.
- Raw data is kept unchanged; transformations write to separate layers (raw → clean → reporting).

## Quality
- Data checks on every run: row counts, nulls in required fields, uniqueness, value ranges, freshness.
- Failed checks stop downstream steps and alert the owner.
- Schema changes in sources are detected; breaking changes are handled before they reach reports.

## Rules
- Transformations are code in version control, reviewed like any other code.
- Personal data is minimized, masked or pseudonymized in analytics layers.
- Metrics have one definition in one place; dashboards use it instead of recalculating.
- Costs (compute, storage) monitored; large queries reviewed.

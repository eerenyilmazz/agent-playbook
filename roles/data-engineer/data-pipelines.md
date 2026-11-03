---
scope: task
when: ETL/ELT pipelines, analytics data, reporting
owner: Eren
status: draft
---
# Data Pipelines

Privacy: templates/software/data-and-privacy.md.

## Design
- Each pipeline declares: source, owner, schedule, destination, freshness SLA, failure behavior.
- Idempotent: re-run for a period gives the same result.
- Incremental by watermark/partition; backfill any date range.
- Layers: raw (unchanged) → clean → reporting.

## Quality
- Checks every run: row counts, required non-nulls, uniqueness, ranges, freshness.
- Failed check stops downstream and alerts the owner.
- Source schema changes detected before they hit reports (data contracts where possible).

## Rules
- Transformations in version control, reviewed, tested.
- Personal data minimized/pseudonymized in analytics layers.
- One metric, one definition (semantic layer); dashboards don't recalculate.
- Partition/cluster large tables; review expensive queries; cost monitored.

---
scope: task
when: Building data tables, lists, filters or forms in a panel
owner: Eren
status: draft
---
# Table and Form Patterns

## Tables
- Server-side paging, sorting, filtering for growing data; enforce max page size.
- Filter/sort/page in the URL.
- States: loading (skeleton), empty (with next action), error (with retry).
- Numbers/dates right-aligned, locale-formatted; consistent column order.
- Bulk actions: show affected count; confirm destructive ones.
- Large exports run async server-side and notify when ready.
- Prefer cursor/keyset pagination for big or fast-changing tables.

## Forms
- Reactive forms; validators in dedicated files; same rules enforced server-side.
- Validate on blur and submit; plain-language messages beside the field.
- Map server field errors back to fields; general errors at top.
- Disable submit while pending; server is idempotent against double submit.
- Warn on unsaved changes. Confirm destructive actions, stating consequence.
- Optimistic locking (version field) to prevent overwriting others' edits.
- Long forms → sections or steps.

---
scope: task
template: web-panel
owner: Eren
status: draft
---
# Table and Form Patterns

## Tables
- Server-side pagination, sorting and filtering for any list that can grow.
- Current filters, sort and page are reflected in the URL so views can be shared and survive refresh.
- Every table has defined states: loading, empty (with a hint on what to do), error (with retry).
- Columns with numbers and dates are right-aligned and consistently formatted.
- Bulk actions show how many rows are affected and ask for confirmation when destructive.
- Exports run server-side for large datasets.

## Forms
- Reactive forms; validators live in dedicated files, not templates.
- Validate on blur and on submit; show errors next to the field in plain language.
- Server errors are mapped back to the right fields.
- Submit button is disabled while submitting; double submit is prevented on the server too (idempotency).
- Unsaved changes warn before leaving the page.
- Destructive actions (delete, cancel) require explicit confirmation and say what will happen.

## Rules
- Reuse the shared table/form components; don't build one-offs.
- Large forms are split into sections or steps, not one long page.

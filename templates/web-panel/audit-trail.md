---
scope: task
when: Admin actions, sensitive data changes, compliance logging
owner: Eren
status: draft
---
# Audit Trail

## Record
Who (user, role, impersonator) · what (action) · target (type + id) · when (UTC) · where (IP, client) · before/after for key fields · trace id.

## Always audit
Login/logout/failures, permission changes, exports, deletions, financial actions, settings, access to sensitive records.

## Rules
- Append-only; no update/delete via the app. Separate store from app logs.
- Written in the same transaction as the change, or via outbox — never best-effort.
- Minimal personal data (see templates/software/data-and-privacy.md).
- Defined retention; archived, not dropped silently.
- Searchable by user, entity, action, date range.
- Viewing the audit trail requires a permission and is itself audited.

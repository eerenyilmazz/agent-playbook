---
scope: task
template: web-panel
owner: Eren
status: draft
---
# Audit Trail

## What to record
- Who (user id, role, impersonation if any), what (action), on what (entity type + id), when (UTC), from where (IP / client).
- Before and after values for changes to important fields.
- Always audited: login/logout, failed logins, permission changes, data exports, deletions, financial actions, settings changes.

## Rules
- Audit records are append-only. No update or delete through the application.
- Audit logs are separate from application logs and have their own retention period.
- Personal data in audit records is limited to what is needed (see templates/software/data-and-privacy.md).
- Writing the audit record happens in the same transaction as the change, or via a reliable outbox — never "best effort".
- Audit logs are searchable by user, entity and date range in the admin panel.

## Access
- Viewing the audit trail is itself a permission and is itself audited.

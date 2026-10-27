---
scope: task
template: web-panel
owner: Eren
status: draft
---
# Permissions and Roles

## Model
- Role-based access control: users → roles → permissions.
- Permissions are fine-grained and named by action: `orders.read`, `orders.refund`, `users.delete`.
- Code checks permissions, never role names. Roles are just bundles.
- Default: deny. A new endpoint has no access until a permission is assigned.

## Enforcement
- Every check happens on the server. Hiding a button in the UI is UX, not security.
- Object-level checks: a user with `orders.read` can still only see orders in their scope (tenant, branch, own records).
- Multi-tenant data is always filtered by tenant at the query level.

## Administration
- Assigning admin or permission-management rights is itself a permission.
- A user cannot raise their own privileges.
- Permission changes are written to the audit trail (see audit-trail.md).

## Testing
- Each sensitive endpoint has tests for: allowed role, forbidden role, wrong tenant/owner.

## Rules
- Removing or renaming a permission is a breaking change; migrate existing roles first.

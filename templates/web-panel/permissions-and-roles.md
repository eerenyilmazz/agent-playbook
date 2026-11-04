---
scope: task
when: Access control, roles, multi-tenant data
owner: Eren
status: draft
---
# Permissions and Roles

## Model
- RBAC: users → roles → permissions. Permissions named `resource.action` (`orders.refund`).
- Code checks permissions, never role names.
- Default deny: new endpoints have no access until mapped.

## Enforcement
- Server-side, always. Hidden UI is UX, not security.
- Object-level: permission + scope (tenant, branch, owner) checked on every read and write.
- Multi-tenant: tenant filter applied centrally (query layer/filter), never per-query by hand.
- Admin impersonation is explicit, time-limited, and audited.

## Administration
- Granting permissions is itself a permission; nobody elevates themselves.
- Permission changes take effect promptly (short cache/token TTL) and are audited.

## Tests
Each sensitive endpoint: allowed, forbidden role, other tenant/owner, unauthenticated.

## Compatibility
Renaming/removing a permission is breaking — migrate roles first.

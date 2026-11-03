---
name: api-design
description: Design or change a REST API or event contract safely — resources, errors, versioning, pagination, idempotency — and produce an OpenAPI spec. Use before implementing any new or changed endpoint.
---
# API Design

Rules: company/engineering-principles.md, company/documentation-standard.md, roles/backend/errors-and-logging.md, roles/backend/idempotency-and-queues.md, company/security-basics.md.

## Steps
1. **Use cases.** List consumer, action, data needed. Design from the consumer, not the table.
2. **Resources.** Plural nouns, nested max one level: `/orders/{id}/items`. Actions that aren't CRUD → sub-resource (`/orders/{id}/cancellation`).
3. **Methods.** GET (safe) · POST (create, non-idempotent → `Idempotency-Key`) · PUT (replace, idempotent) · PATCH (partial) · DELETE (idempotent).
4. **DTOs.** Separate request/response DTOs; never entities. camelCase; ISO-8601 UTC dates; money as `{amount: minor units, currency}`; ids as strings.
5. **Lists.** Paginate always (cursor for large/changing data); max page size; filter/sort params documented.
6. **Errors.** RFC 9457 body + stable `code` per failure case (examples/api-error.md). List every code in the spec.
7. **Security.** Auth scheme, required permission per operation, object-level rule, rate limit.
8. **Concurrency.** `ETag`/`If-Match` or version field for updates that can collide.
9. **Spec.** Write/update OpenAPI in the same PR; examples for each request/response/error.
10. **Compatibility check** (changed APIs):
    - Safe: add optional field, add endpoint, add enum value only if clients tolerate unknowns.
    - Breaking: remove/rename field, change type/meaning, make optional required, change status codes or error codes.
    - Breaking → new version (`/v2` or new media type), deprecate old with `Deprecation`/`Sunset` headers, migration note, timeline.
11. **Review** with consumers before implementation; add contract tests.

## Events
Same steps: versioned schema, additive changes, consumers ignore unknown fields, breaking → new event version.

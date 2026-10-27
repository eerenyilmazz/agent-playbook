---
scope: task
role: backend
owner: Eren
status: draft
---
# Errors and Logging

## Errors
- Centralized exception handling (e.g. `@ControllerAdvice`). Controllers don't catch and format errors themselves.
- A standard error response body for every API: `code`, `message`, `details`, `traceId`. Consider RFC 9457 (Problem Details).
- Error codes are stable strings (`ORDER_NOT_FOUND`), so clients can rely on them.
- Correct HTTP status: 400 validation, 401 unauthenticated, 403 forbidden, 404 not found, 409 conflict, 422 business rule, 500 unexpected.
- Never expose stack traces, SQL or internal class names to clients.
- Don't swallow exceptions. Either handle them meaningfully or let them propagate.

## Logging
- Use SLF4J with parameterized messages: `log.info("Order {} created", id)`.
- Levels: ERROR (needs action), WARN (unexpected but handled), INFO (business events), DEBUG (diagnostics, off in prod).
- Don't change existing log formats; dashboards and alerts may depend on them.
- Every request carries a correlation/trace id through all logs and downstream calls.
- Never log secrets, tokens, passwords or personal data.
- Log an exception once, at the place it's handled, with the stack trace.

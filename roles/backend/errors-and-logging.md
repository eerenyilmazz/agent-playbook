---
scope: task
when: Error handling, API error responses, logging, observability
owner: Eren
status: draft
---
# Errors and Logging

## Errors
- Central handler (`@ControllerAdvice`); controllers don't format errors.
- One error body for all APIs, RFC 9457 style: `type, title, status, detail, code, traceId, errors[]`.
- Stable error codes (`ORDER_NOT_FOUND`) — part of the API contract.
- Status: 400 invalid · 401 unauthenticated · 403 forbidden · 404 · 409 conflict · 422 business rule · 429 rate limit · 5xx unexpected.
- No internals in responses. No swallowed exceptions.

## Logging
- SLF4J parameterized: `log.info("Order {} created", id)`.
- ERROR = needs action · WARN = handled anomaly · INFO = business event · DEBUG = off in prod.
- Existing formats unchanged (alerts depend on them). Structured (JSON) for new services.
- Trace id propagated through logs, HTTP and messages (MDC / OpenTelemetry).
- No secrets or personal data.
- Log an exception once, where handled, with stack trace. No log-and-rethrow.

## Metrics
RED per endpoint (rate, errors, duration) plus key business counters.

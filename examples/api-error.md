# Example: API Error Responses

Format: roles/backend/errors-and-logging.md (RFC 9457 style).

**422 — business rule**
```json
{
  "type": "https://api.example.com/errors/refund-exceeds-captured",
  "title": "Refund exceeds captured amount",
  "status": 422,
  "detail": "Requested 15000 but only 12000 is refundable.",
  "code": "REFUND_EXCEEDS_CAPTURED",
  "traceId": "4bf92f3577b34da6a3ce929d0e0e4736"
}
```

**400 — validation**
```json
{
  "type": "https://api.example.com/errors/validation",
  "title": "Invalid request",
  "status": 400,
  "code": "VALIDATION_FAILED",
  "traceId": "a1b2c3d4e5f60718293a4b5c6d7e8f90",
  "errors": [
    { "field": "amount", "code": "MUST_BE_POSITIVE", "message": "must be greater than 0" },
    { "field": "currency", "code": "UNSUPPORTED", "message": "supported: TRY, EUR, USD" }
  ]
}
```

**Never**
```json
{ "error": "org.hibernate.exception.ConstraintViolationException: could not execute statement [ERROR: duplicate key ...]" }
```

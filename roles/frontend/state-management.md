---
scope: task
role: frontend
owner: Eren
status: draft
---
# State Management

## Where state lives
- **Component state:** UI-only state (open/closed, input focus). Keep it local.
- **Feature state:** Shared within one feature; held in a feature service/facade.
- **Server state:** Data from the API; cached, refetched, invalidated — not copied into many places.
- **Global state:** Only for truly app-wide data (current user, settings). Needs a justification.
- **URL state:** Filters, tabs, pagination — anything that should survive refresh or be shareable.

## Rules
- Follow the project's existing pattern (services with observables/signals, or a store). Don't introduce a new state library without an ADR.
- Prefer the `async` pipe (or signals) over manual subscriptions; manual subscriptions must be cleaned up.
- State is immutable: create new objects, don't mutate.
- Components read state through a facade/service; they don't call HTTP directly.
- Derived values are computed, not stored separately.
- Loading, error and empty are explicit states, not inferred from `null`.

---
scope: task
when: Frontend data flow, stores, caching API data
owner: Eren
status: draft
---
# State Management

## Where state lives
- **Component:** UI-only (open, focus).
- **Feature:** feature service/facade.
- **Server:** cached API data with refetch/invalidation — never copied into many places.
- **URL:** filters, tabs, paging.
- **Global:** only app-wide (user, settings), justified.

## Rules
- Follow the existing project pattern; new state library needs an ADR.
- `async` pipe or signals; manual subscriptions cleaned up (`takeUntilDestroyed`).
- Immutable updates. Derived values computed, not stored.
- Components use facades; never call HTTP directly.
- Explicit loading/error/empty states (not `null` guessing).
- Cancel stale requests (`switchMap`); dedupe concurrent identical requests.

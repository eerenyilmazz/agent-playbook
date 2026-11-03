---
scope: task
when: Making a decision that is expensive to reverse
owner: Eren
status: draft
---
# Architecture Decision Record

Single source for the ADR format. Approval flow: roles/decision-maker/adr-approval.md.

## Write one when
Choosing or changing a database, framework, API style, auth model, hosting, integration pattern, or anything a future dev will ask "why?" about.

## File
`docs/adr/NNNN-short-title.md` — sequential, never reused, ≤ 1 page.

```
# NNNN. Title
Status: proposed | accepted | rejected | superseded by NNNN
Date: YYYY-MM-DD · Deciders: …

## Context      problem, constraints, forces
## Decision     one or two sentences
## Options      each with why-not (incl. "do nothing")
## Consequences pros, cons, what gets harder
## Risk         level + mitigation
## Rollback     how to undo, and the cost
```

## Rules
- Accepted ADRs are immutable; supersede, don't edit.
- No irreversible implementation before `accepted`.

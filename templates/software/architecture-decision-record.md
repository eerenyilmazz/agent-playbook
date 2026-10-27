---
scope: task
template: software
owner: Eren
status: draft
---
# Architecture Decision Record (ADR)

Single source for the ADR template. Other files link here.

## When to write one
- The decision is expensive to reverse (database, framework, API style, hosting, auth model).
- More than one reasonable option exists.
- Someone will later ask "why did we do it this way?"

## Location and naming
`docs/adr/NNNN-short-title.md`, numbered sequentially, never reused.

## Template
```
# NNNN. Title
Status: proposed | accepted | superseded by NNNN
Date: YYYY-MM-DD
Deciders: names/roles

## Context
The problem and the forces at play (constraints, deadlines, team skills).

## Decision
What we will do, in one or two sentences.

## Alternatives considered
- Option A — why not
- Option B — why not

## Consequences
Positive, negative, and what becomes harder later.

## Rollback
How we would undo this, and at what cost.
```

## Rules
- Accepted ADRs are immutable. Changes come as a new ADR that supersedes the old one.
- Keep it under one page. Link to details instead of pasting them.
- Approval process: see roles/decision-maker/adr-approval.md.

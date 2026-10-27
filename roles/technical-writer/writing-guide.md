---
scope: task
role: technical-writer
owner: Eren
status: draft
---
# Writing Guide

Documentation structure and required docs: company/documentation-standard.md.

## Style
- Write for the reader's task: what are they trying to do?
- Short sentences, active voice, present tense.
- One idea per paragraph; use lists for steps and options.
- Steps are numbered, start with a verb, and include the expected result.
- Use the same term for the same thing everywhere; define terms once.
- Code samples are complete, tested and copy-pasteable.
- No marketing language in technical docs.

## Types
- **Tutorial:** Learning by doing, for beginners.
- **How-to:** Steps to achieve one goal.
- **Reference:** Complete, accurate facts (API, config).
- **Explanation:** Why things work the way they do.
Don't mix types in one page.

## Maintenance
- Docs change in the same PR as the code.
- Every page has an owner; outdated pages are fixed or removed.
- User-facing release notes follow the changelog rules.

---
scope: task
when: Writing docs, guides, release notes, rule files
owner: Eren
status: draft
---
# Writing Guide

Required docs: company/documentation-standard.md.

## Style
- Write for the reader's task. Short sentences, active voice, present tense.
- Lists for steps/options; steps numbered, start with a verb, state the expected result.
- One term per concept; define once.
- Code samples complete, tested, copy-pasteable.
- No marketing language.

## Doc types (don't mix)
Tutorial (learn) · How-to (one goal) · Reference (facts) · Explanation (why).

## Rule files in this repo
- Frontmatter: `scope`, `when` (task files), `owner`, `status`, optional `review`.
- Imperative bullets, no filler, no restating other files — link instead.
- Always files ≤ ~400 tokens each; task files ≤ ~600.

## Maintenance
Docs change with the code; every page has an owner; stale pages fixed or removed.

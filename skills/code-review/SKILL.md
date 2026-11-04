---
name: code-review
description: Review a pull request for correctness, contract safety, architecture, tests and hygiene. Use for any PR review request.
---
# Code Review

Rules live in: company/engineering-principles.md, company/git-and-versioning.md, roles/code-reviewer/common-mistakes.md, roles/code-reviewer/review-rubric.md. Load the template/role files whose `when:` matches the changed code.

## Steps
1. **Understand intent.** Read the PR description. Missing what/why/risk/test/rollback → request it before reviewing code.
2. **Size and scope.** > 400 lines or mixed refactor + behavior → ask to split.
3. **Contracts first.** Scan for API, DTO, schema, event, permission, log-format or UI changes. Any found → confirm it's flagged breaking or proven compatible.
4. **Risky areas.** Auth, payments, migrations, transactions, concurrency, personal data → read line by line; involve security-reviewer if auth/data/uploads changed.
5. **Walk the diff** against roles/code-reviewer/common-mistakes.md.
6. **Tests.** New logic tested? Bug fix has failing-first test? Any test deleted or weakened → blocker.
7. **Run it** if possible: build, tests, the changed flow.
8. **Write comments.** Each: label (blocker/should/nit) · file:line · problem · why it matters · suggested fix. Praise good decisions briefly.
9. **Verdict.**
   - Approve: no blockers.
   - Request changes: ≥ 1 blocker.
   - Comment: only should/nit.

Good PR description: examples/pull-request.md.

## Output format
```
Verdict: approve | request changes | comment
Risk: low | medium | high — reason
Breaking: yes/no — what
Blockers: …
Should: …
Nits: …
```

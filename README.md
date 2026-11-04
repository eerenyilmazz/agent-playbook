# agent-playbook

Rule files and skills for an AI agent team doing software work: backend, web, admin panels, e-commerce, mobile, games and desktop apps.

Agents load a small set of **company rules** on every task, then only the **template**, **role** and **skill** files that match the task. This keeps prompts small and rules consistent.

> All files are `draft` until reviewed. Files marked `review: expert-required` contain legal, tax, payment or store-policy rules and must be confirmed by a qualified expert before they are marked `approved`.

---

## Contents

- [Repository layout](#repository-layout)
- [Quick start](#quick-start)
- [How agents load files](#how-agents-load-files)
- [Token budget](#token-budget)
- [Templates](#templates)
- [Roles](#roles)
- [Skills](#skills)
- [File format](#file-format)
- [Status and review](#status-and-review)
- [Adding or changing a file](#adding-or-changing-a-file)
- [Checks and CI](#checks-and-ci)
- [ArkeLab](#arkelab)
- [Conventions](#conventions)

---

## Repository layout

```
agent-playbook/
├── company/              # company-wide rules: 2 always, 4 task (6 files)
├── templates/<type>/     # loaded by project type (8 types, 28 files)
├── roles/<role>/         # loaded by the role doing the work (14 roles, 28 files)
├── skills/<name>/SKILL.md# step-by-step procedures (12 skills)
├── examples/             # quality bar: PR, ADR, postmortem, API errors, commits
├── docs/                 # human-only docs, never loaded by agents
│   ├── compliance-sources.md
│   └── project-readme-template.md
├── scripts/check.py      # validation + INDEX.md generator
├── scripts/load.py       # builds the rule bundle for one task
├── AGENTS.md             # protocol every agent follows (entry point)
├── INDEX.md              # generated routing table: file → trigger → size
└── .github/workflows/    # CI running the checks
```

## Quick start

### Requirements

- **Python 3.8 or newer** (`python3 --version`). The scripts use only the standard library (`argparse`, `re`, `sys`, `pathlib`), so there is nothing to `pip install` and no virtual environment is needed. CI runs them with the Python 3 that ships with `ubuntu-latest`.
- **Git** to clone the repo and open pull requests.
- No network access is needed to run the scripts; token counts are estimates (characters ÷ 4), not calls to a tokenizer.

### Steps

1. Point your agent system at `AGENTS.md` (loading protocol, rule precedence, gap reporting).
2. Copy `docs/project-readme-template.md` into each project's README; fill in templates, roles and overrides.
3. Build the rules for a task:
   ```bash
   python3 scripts/load.py --templates software,web-panel,web-commerce --role backend \
       --skill api-design --task "add refund endpoint to admin panel"
   ```
   Prints the bundle to stdout (use `--list` for file names only) and the token total to stderr.

## How agents load files

1. **Always:** `company/` files with `scope: always` (engineering-principles, security-basics). The other company files (security-details, git, incidents, documentation) load like task files, by `when:`.
2. **Route:** read `INDEX.md` and pick files whose `when:` trigger matches the task.
3. **Templates:** only for the project types in the project README (e.g. `software` + `web` + `web-panel`). `software` applies to every code project.
4. **Roles:** only the role doing the task (a backend task loads `roles/backend/…`, not `roles/frontend/…`).
5. **Skills:** only when the task is that procedure (e.g. a PR review loads `skills/code-review`).

`scripts/load.py` does this deterministically: `company/` always files → skill → all files of the role → up to 5 company-task and template files ranked by how well their `when:` line matches `--task` → stops at the budget.

Typical load: 8–14 files, 2300–4000 tokens. Never load whole folders.

### Rule precedence (highest first)
1. User's explicit instruction for the task
2. Project README overrides
3. `company/`
4. Templates, then roles
5. Skill steps

**Example — "add a refund endpoint to the admin panel"** (backend, api-design): `company/` always + `skills/api-design` + `roles/backend/*` + `payment-flow`, `permissions-and-roles`, `audit-trail`, `performance-budget`, `table-and-form-patterns` → 11 files, ~3200 tokens.

## Token budget

Prompt limit is **5000 tokens**. Sizes are estimated as characters ÷ 4.

| Scope | Limit | Current |
|---|---|---|
| All `always` files together | ≤ 2500 tokens · ≤ 2400 chars without frontmatter (ArkeLab) | ~350 tokens · ~1300 chars |
| One `always` file | ≤ 400 tokens · ≤ 1200 chars (ArkeLab) | — |
| One task file (template/role) | ≤ 600 | — |
| Per task total | ≤ 5000 tokens (ArkeLab: 5000 chars for the whole prompt) | always + ~5 files |

`scripts/check.py` fails if a budget is exceeded. Exact per-file sizes are in `INDEX.md`.

## Templates

| Type | Files | Use for |
|---|---|---|
| `software` | architecture-decision-record, test-pyramid, performance-budget, data-and-privacy | Every code project |
| `web` | accessibility, seo-and-performance, browser-support, design-system | Public sites and web UIs |
| `web-panel` | permissions-and-roles, table-and-form-patterns, audit-trail | Admin/back-office panels, multi-tenant apps |
| `web-commerce` | payment-flow, cart-stock-orders, tax-returns-compliance, conversion-tracking | Online stores, checkout |
| `mobile` | store-release, permissions-and-privacy, offline-and-sync, device-matrix | iOS/Android apps |
| `game` | game-loop, performance-and-fps, asset-pipeline | Any game |
| `idle-game` | economy-balance, offline-earnings, monetization | Idle/incremental games (with `game`) |
| `desktop` | auto-update, signing-and-notarization, local-data-migration | Electron or other desktop apps |

## Roles

| Role | Files | Responsibility |
|---|---|---|
| `pm` | prioritization, risk-management, sprint-cadence, team-template-setup | Backlog, risks, sprints, project setup |
| `decision-maker` | decision-framework, cost-risk-matrix, adr-approval | Decisions, escalations, ADR approval |
| `frontend` | state-management, component-rules, i18n | UI code |
| `backend` | database-migrations, errors-and-logging, idempotency-and-queues | Server code |
| `qa-security` | regression-suite, owasp-checks, threat-modeling | **Tests running software** |
| `code-reviewer` | review-rubric, common-mistakes | **Reviews code quality** |
| `security-reviewer` | abuse-cases, dependency-audit, secret-leak-check | **Reviews code and design for security** |
| `devops-cloud` | ci-cd-and-environments | Pipelines, environments, operations |
| `ux-designer` | ux-principles | Flows, screens, handoff |
| `mobile-developer` | mobile-rules | App code |
| `game-developer` | game-dev-rules | Game code |
| `data-engineer` | data-pipelines | ETL, analytics data |
| `technical-writer` | writing-guide | Docs and rule files |
| `release-manager` | release-process | Release planning and go/no-go |

Boundary rule: **QA tests, reviewers review.** QA does not review code; reviewers do not own test suites.

## Skills

| Skill | Use when |
|---|---|
| `code-review` | Reviewing any pull request |
| `security-audit` | Before releases touching auth, payments, personal data, uploads, permissions |
| `release-checklist` | Shipping any backend, web or desktop release |
| `db-migration` | Any schema or bulk data change |
| `api-design` | Before implementing a new or changed endpoint or event |
| `test-writing` | Writing tests, or locking behavior before refactoring |
| `perf-profile` | Something is slow or over budget |
| `incident-postmortem` | Production is broken; afterwards for the postmortem |
| `a11y-audit` | Before releasing UI |
| `electron-release` | Shipping a desktop version |
| `store-submission` | Publishing an iOS/Android update |
| `economy-balance` | Designing or rebalancing an idle game economy |

Skills say **how**; rule files say **what and why**. Skills link to rule files and never copy them.

## Examples

Filled-in references agents use as the quality bar (loaded only when a skill or rule points to them):

| File | Linked from |
|---|---|
| `examples/pull-request.md` | code-review skill |
| `examples/adr.md` | ADR template |
| `examples/postmortem.md` | incident-postmortem skill |
| `examples/api-error.md` | api-design skill |
| `examples/commits.md` | git-and-versioning |

## File format

Rule files (`company/`, `templates/`, `roles/`):

```yaml
---
scope: always | task
when: <one-line trigger>        # required for task files
owner: <person>
status: draft | approved
review: expert-required (<area>) # optional
verified: YYYY-MM-DD (<source type>) # optional, for fact-heavy files
---
# Title
- imperative bullets
```

Skill files (`skills/<name>/SKILL.md`):

```yaml
---
name: <must match folder name>
description: <what it does and when to use it>
---
```

## Status and review

| Status | Meaning |
|---|---|
| `draft` | Usable; agents follow it, but it has not been reviewed by the owner |
| `approved` | Reviewed by the owner (and the expert, if `review` is set) |

Files currently needing expert review:

| File | Expert |
|---|---|
| `templates/software/data-and-privacy.md` | KVKK/GDPR lawyer |
| `templates/web-commerce/payment-flow.md` | Payments/PCI specialist |
| `templates/web-commerce/tax-returns-compliance.md` | Accountant + lawyer |
| `templates/idle-game/monetization.md` | Store policy / consumer law |
| `templates/mobile/permissions-and-privacy.md` | Privacy lawyer |

Evidence for their facts: `docs/compliance-sources.md` (re-check yearly and before any commerce or mobile launch). To approve: put the expert's name in `owner`, set `status: approved`, commit.

## Adding or changing a file

1. **Find the home.** One topic lives in exactly one file. Search first; extend the existing file if the topic fits.
2. **Pick the folder.** Company-wide → `company/` (keep tiny). Project type → `templates/<type>/`. Role → `roles/<role>/`. Procedure → `skills/<name>/SKILL.md`.
3. **Write tight.** Imperative bullets, no filler, no restating other files — link with the repo path (`roles/backend/database-migrations.md`).
4. **Add frontmatter** with a specific `when:` trigger.
5. **Run checks** (below) and commit `INDEX.md` with your change.
6. **PR** with a Conventional Commit title, e.g. `docs(backend): add caching rules`.

New role or template folder: also add it to the tables in this README.

### Example rule file

A complete task file as it should look when committed (for example `roles/backend/outbound-calls.md`):

````markdown
---
scope: task
when: Retries, timeouts, outbound HTTP calls
owner: Eren
status: draft
---
# Outbound Calls: Timeouts and Retries

## Timeouts
- Every outbound call sets a connect and a read timeout. No library defaults.
- Defaults: connect 2 s, read 5 s. Longer only with a comment naming the dependency's measured p99.

## Retries
- Retry only idempotent calls (GET, PUT, DELETE, or POST with an idempotency key). See `roles/backend/idempotency-and-queues.md`.
- Max 3 attempts, exponential backoff with jitter (200 ms, 400 ms, 800 ms ± 20%).
- Retry on connect errors, 429, 502, 503, 504. Never on other 4xx.
- Honor `Retry-After` when present.

## Failure handling
- Circuit breaker around every third-party dependency; open after 5 consecutive failures, half-open after 30 s.
- Log the final failure once with the trace id. See `roles/backend/errors-and-logging.md`.
- Return a degraded response only when the product owner has approved one; otherwise fail with 503.
````

Why it passes `scripts/check.py`: the frontmatter has `scope`, `owner` and `status`; a task file has a `when:` line of 60 characters or fewer; the body stays under 600 tokens (about 2400 characters); and every repo path it links (`roles/backend/...`) exists. After adding a file, run `python3 scripts/check.py` and commit the regenerated `INDEX.md`.

## Checks and CI

```bash
python3 scripts/check.py            # validate and regenerate INDEX.md
python3 scripts/check.py --no-write # validate only (used in CI)
```

Validates:
- Required frontmatter (`scope`, `owner`, `status`; `when` for task files; `name`/`description` for skills, `name` = folder)
- Every repo path linked in a file exists (`company/`, `templates/`, `roles/`, `examples/`, `skills/`)
- Token budgets per file and for `always` files in total, plus ArkeLab's character limits

GitHub Actions runs the check on every push and pull request (`.github/workflows/check.yml`).

## Feedback loop

Agents end their output with `Playbook gap: <file> — <problem> — <fix>` when a rule is missing or wrong. Collect these after each project and fix the files in one PR. Known limits until real use:
- Token sizes are estimates (chars ÷ 4).
- Default numbers (latency, PR size, rollout steps) are industry defaults; tune per project via overrides.
- All files are `draft` until the owner reviews them.

## ArkeLab

ArkeLab imports this repo as the content layer of its *Team and Templates* model (company / template / role / skill records). Mapping, decisions and open items: `docs/arkelab-integration.md`.

- `check.py` also enforces ArkeLab limits: `always` file ≤ 1200 chars, `when` ≤ 200, `owner` ≤ 80.
- Renaming or moving a file changes its identity in ArkeLab — list it in the PR.
- ArkeLab-specific workflow rules (task gates, publishing, Jira states) live in ArkeLab, not here.

## Conventions

- **Language:** English for all files.
- **Single source:** security → `company/security-basics.md`; ADR format → `templates/software/architecture-decision-record.md`; incidents → `company/incidents-and-rollback.md`; migrations → `roles/backend/database-migrations.md`.
- **Production-first:** backward compatibility, small reversible changes, feature flags for risk, explicit breaking-change labels.
- **Commits:** Conventional Commits; PRs only, squash merge into `main` (see `CONTRIBUTING.md`).

---

## License

Copyright (c) 2026 Eren Yılmaz. All rights reserved. The source is publicly visible for evaluation only; see [`LICENSE`](LICENSE). To request permission to use any part of it, contact eerenyilmazz1@gmail.com.

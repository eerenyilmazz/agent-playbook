# agent-playbook ↔ ArkeLab integration note

Date: 2026-11-04
Source repo: https://github.com/eerenyilmazz/agent-playbook (developer: Eren)
Status: draft. The repo was read through GitHub only; it was not cloned and the scripts were not run.

## 1. Purpose

agent-playbook will serve as the content layer of ArkeLab's "Team and Templates" model: company rules, template and role knowledge are written as Markdown in the playbook, and ArkeLab imports them into its own records (company / template / role / skill). It is part of the main development, not a plugin.

## 2. Repo summary

- 132 files. Python scripts: `scripts/load.py`, `scripts/check.py`. CI: `.github/workflows/check.yml`.
- `company/` (5 files, always loaded), `templates/<type>/` (8 types, 28 files), `roles/<role>/` (14 roles, 28 files), `skills/<name>/SKILL.md` (12 skills), `examples/` (5), `docs/` (human-only), `AGENTS.md`, `INDEX.md` (generated routing table).
- File header: `scope: always|task`, `when`, `owner`, `status: draft`; sensitive files carry `review: expert-required`.
- Budget: prompt limit is 5000 tokens (chars ÷ 4). 400 per `always` file and 2500 in total; 600 per `task` file.
- Load order: company → skill → role files → at most 5 template files ranked by `when` match.
- Precedence: user > project README > company > template > role > skill.
- Gap report: `Playbook gap: <file/topic> — <what is missing> — <suggestion>`.

## 3. Concept mapping

| Playbook | ArkeLab |
|---|---|
| `company/*.md` | Company document, tier `always` |
| `templates/<type>/*.md` | Template document |
| `roles/<role>/*.md` | Role document (`roles[]` filter) |
| `scope: always` / `task` | `tier: always` / `task` |
| `examples/*.md` | `tier: reference` |
| `docs/*.md` | Not imported (human-only) |
| `when:` | `when` (max 200 characters) |
| `owner:` | `owner` (max 80 characters) |
| `status: draft` | `reviewedAt` empty |
| `review: expert-required` | No equivalent (see §5) |
| `skills/<name>/SKILL.md` | Skill record in ArkeLab's AI tools area (written to all providers) |
| `Playbook gap:` line | Gaps in `company_report` / task comments / PM `company_review` |

## 4. Name mapping

Roles:
- Same: `qa-security`, `code-reviewer`, `decision-maker`, `security-reviewer`, `devops-cloud`
- Different: `backend` → `backend-developer`, `frontend` → `frontend-developer`, `pm` → `project-manager`
- No ArkeLab record: `data-engineer`, `game-developer`, `mobile-developer`, `release-manager`, `technical-writer`, `ux-designer`

Templates:
- Same: `software`, `web`, `web-panel`, `web-commerce`, `mobile`, `game`
- Different: `desktop` → `desktop-product`, `idle-game` → `game-idle`

Note: These mapping tables rely on recalled IDs from the ArkeLab catalog; verify them against the code before implementing. (§8b contains the corrected mapping.)

## 5. Mismatches and resolutions

1. **`always` file size.** The playbook allows 400 tokens (~1600 characters); ArkeLab truncates `always` documents to 1200 characters, so content would be cut silently. Resolve first: raise the limit or shorten the files.
2. **Unit ambiguity.** The playbook limit is 5000 *tokens*. I recall ArkeLab's `PROMPT_LIMIT=5000` as characters. Needs verification; if it is characters, the budget is roughly 4× tighter.
3. **Status field.** ArkeLab has no field for `expert-required`. Options: add a new `review` field, or skip importing `expert-required` files and only list them. Recommendation: a new field, so that nothing counts as `approved` without expert sign-off.
4. **Python.** `load.py` / `check.py` are not used inside the app. Loading stays in ArkeLab's own loader; `check.py` runs only in the playbook's CI.
5. **Ordering.** The playbook ranks template files by `when`; ArkeLab has no such ranking (it has a role filter). Not required for the first version.
6. **Precedence rule.** ArkeLab only has `hides` and conflict reporting. The playbook's precedence order is written into the company Markdown.
7. **ArkeLab-specific rules.** Task gates, `branch.publish`, owner-only main and Jira states are not in the playbook and should not be. They are kept on the ArkeLab side as a separate "ArkeLab working rules" document.
8. **Missing role records.** For roles, the playbook provides only Markdown; the `does / doesNot / handoff / evals` fields must be written separately in ArkeLab.
9. **Language.** The playbook is in English; the ArkeLab UI and its existing Markdown are in Turkish. A decision is needed (§8).
10. **Duplicate content.** The starter Markdown in `electron/company-starter-docs.cjs` overlaps with the playbook. The playbook becomes the single source and the old files are removed.

## 6. Design

The importer uses ArkeLab's existing plan → preview → approve flow (`apply`, hash, 15 min); it does not write data directly.

1. Read the playbook version (commit/tag) and fetch the tree.
2. Build its own table from file headers instead of `INDEX.md` (parsing: `key: value` lines and `---` blocks).
3. Convert each file into a company / template / role document using the mapping tables; skip `docs/` and the scripts.
4. Pass skills to the AI tools flow with `name` + `description` validation (name equals the folder name).
5. Show the resulting plan as a preview: files to add, change and delete; size and budget warnings; name conflicts.
6. After approval, `apply`; records arrive as `draft`; the source commit is written to the history.
7. For later versions, produce only a diff plan (never overwrite a user's local edits: ask on conflict).

## 7. Phases

1. **Preparation:** resolve §5-1 and §5-2 (limit and unit).
2. **Importer** + mapping tables + tests (using a sample playbook tree).
3. **Skills** (12) and **company/template Markdown**.
4. **The 6 missing role records** (`does/doesNot/handoff/evals`).
5. **Update flow** (diff plan) and linking `Playbook gap` to reports.
6. **Playbook CI:** check ArkeLab limits (size, names) with `check.py`.

## 8. Decisions (Eren, 2026-11-04)

- **Language:** Stays English. The ArkeLab UI may remain Turkish; Markdown bodies are not translated.
- **`expert-required`:** A new `review` field is added to ArkeLab. A document carrying it does not count as `approved` without expert sign-off (name + date). The files are imported.
- **Updates:** PR flow. Everyone opens a PR, Eren (`@eerenyilmazz`, CODEOWNERS) approves; no merge until `check.py` passes in CI. Details: `CONTRIBUTING.md`.
- **Starter Markdown:** The starter Markdown in `electron/company-starter-docs.cjs` is deleted entirely; the playbook is the single source.

## 8a. Done on the playbook side (2026-11-04)

- `company/` files are under ArkeLab's 1200-character `always` limit (largest: 1188).
- `check.py` also enforces ArkeLab limits: `always` ≤ 1200 characters, `when` ≤ 200, `owner` ≤ 80.
- The committed `__pycache__` was removed and a `.gitignore` added.

## 8b. Verified against ArkeLab code (2026-11-04, Arkhelab-main zip)

- **§5-2 unit: characters.** `electron/company-system.cjs`: `PROMPT_LIMIT = 5000` characters, applied to the whole prompt (company + templates + roles + document lists), with a 300-character reserve; sections that do not fit are dropped and a warning is added. `always` documents are embedded as content and truncated at 1200 characters; `task` documents are listed by name + `when` only; `reference` documents by name only.
- **Decision (Eren): 2 always + 4 task.** `engineering-principles` and `security-basics` are `always` and shortened to summaries (~1300 characters in total); details live in `security-details` (task) and `git-and-versioning` (PR rules). `git-and-versioning`, `incidents-and-rollback`, `documentation-standard` and `security-details` are `task`. The precedence order is in `engineering-principles`. `check.py`: total of `always` bodies ≤ 2400 characters, `when` ≤ 60 characters.
- **Measurement (with the importer, ArkeLab `brief`):** web-commerce + 3 roles → 3996; web-panel + web-commerce + 5 roles → 4601; mobile + web-panel + 5 roles → 4602 characters (limit 4700). With 2 templates + 7 roles the role section is dropped (ArkeLab warns). For larger teams the owner must decide: raise `PROMPT_LIMIT` or change the order of the role section.
- **§4 name mapping (corrected):**
  - Same roles: `decision-maker`, `qa-security`, `code-reviewer`, `security-reviewer`, `devops-cloud`, `technical-writer`, `data-engineer`.
  - Different roles: `pm` → `project-manager`, `frontend` → `frontend-developer`, `backend` → `backend-developer`, `ux-designer` → `ui-ux-engineer`.
  - Not in ArkeLab: `game-developer`, `mobile-developer`, `release-manager`. In ArkeLab but not in the playbook: `researcher`.
  - Different templates: `idle-game` → `game-idle`, `desktop` → `desktop-product`. In ArkeLab but not in the playbook: `web-presentation`, `game-mobile`, `game-pc`, `game-hyper-casual`.
- **Record limits:** at most 30 documents per record; names must end in `.md` and be unique; content ≤ 20000; `when` ≤ 200; `owner` ≤ 80; `roles` ≤ 40 IDs.
- **Merging to main:** In ArkeLab only the owner `burak` (Burakka1) can merge. Eren's changes arrive from a personal branch.

## 8c. Still open

- §10 rule conflict: `git-and-versioning` (squash, protected main) versus ArkeLab's publishing rules (`branch.publish`, owner-only main). ArkeLab-specific rules stay on the ArkeLab side; the playbook does not conflict as a general rule, but for agent precedence ArkeLab's company rules must rank above the playbook's.
- License: none in the playbook.

## 9. Acceptance criteria

- Importing the sample playbook produces 8 templates, 14 roles, 12 skills and 5 company files; none arrive as `approved`.
- If the `always` total exceeds the prompt limit, the preview warns; no silent truncation.
- Importing the same version twice yields an empty diff.
- A locally edited document is not overwritten by a version update.
- `npm run test` and `npm run build` pass.

## 10. Risks

- Content is still draft; payment, tax and store-policy files must not be trusted without expert sign-off.
- `git-and-versioning.md` and `engineering-principles.md` may conflict with ArkeLab rules (merging to main, Ponytail); their bodies were not read.
- The repo had `scripts/__pycache__/*.pyc` committed; a `.gitignore` is needed (done, see §8a). No license was seen.

## 11. Not verified

Most file bodies were not read; `load.py` and `check.py` were not run; CI results were not checked; ArkeLab's limit unit and catalog IDs were not confirmed from code (the unit and IDs were later confirmed; see §8b).

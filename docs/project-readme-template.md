# <Project name>

<!-- Copy into each project's README. The "Playbook" section is read by agents. -->

<What it does, 2–3 sentences.>

## Run
- Local: `<command>`
- Tests: `<command>`
- Env vars: `<NAME>`, `<NAME>` (values in secret manager)

## Owner
<name>

## Playbook
- Templates: software, <web | web-panel | web-commerce | mobile | game | idle-game | desktop>
- Roles: <backend, frontend, qa-security, code-reviewer, …>
- Stack: <e.g. Java 21 / Spring Boot 3, Angular 18, PostgreSQL 16>

### Overrides
Only list values that differ from the playbook defaults.

| Rule | Default | This project | Reason |
|---|---|---|---|
| API p95 read latency | 300 ms | | |
| API p95 write latency | 800 ms | | |
| Max PR size | 400 lines | | |
| Browser matrix | latest 2 majors | | |
| Min iOS / Android | current + previous / market data | | |
| Sprint length | 1–2 weeks | | |
| Release watch window | 60 min | | |
| Severity response times | Sev1 now / Sev2 1 h / Sev3 next day | | |

### Out of scope
<What this project deliberately doesn't do.>

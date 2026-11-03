---
scope: task
when: Security review of a feature's design or code
owner: Eren
status: draft
---
# Abuse Cases

Boundary: **security-reviewer reviews code and design**; QA tests. Rules: company/security-basics.md.

Ask "how would someone misuse this?" for each feature:

- **Accounts:** enumeration via login/sign-up/reset messages · credential stuffing · weak/reusable/non-expiring reset tokens · OTP brute force.
- **Business logic:** negative/huge quantities or prices · coupon/referral reuse · skipping steps (confirm without pay) · race conditions on balances/stock.
- **Data access:** IDOR · mass assignment (`role`, `price`, `tenantId` in body) · over-fetching in API responses.
- **Resources:** huge uploads/payloads · expensive searches · unbounded exports · spam via forms, invites, notifications.
- **Integrations:** forged webhooks · SSRF via user-supplied URLs · open redirects.

Output: each relevant case → code mitigation + QA test case.

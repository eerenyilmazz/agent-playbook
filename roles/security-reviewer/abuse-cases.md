---
scope: task
role: security-reviewer
owner: Eren
status: draft
---
# Abuse Cases

The security-reviewer reviews code and design (QA tests; see roles/qa-security). Base rules: company/security-basics.md.

For every feature, ask "how would someone misuse this?" Common abuse cases:

## Accounts
- Account enumeration through login, sign-up or password-reset messages.
- Credential stuffing and brute force; missing rate limits.
- Password reset tokens that are guessable, reusable or don't expire.

## Business logic
- Negative or huge quantities, prices or discounts.
- Reusing a coupon, referral or reward many times.
- Skipping steps (e.g. calling "confirm order" without paying).
- Race conditions: two parallel requests spending the same balance.

## Data access
- Changing ids to read or edit others' records (IDOR).
- Mass assignment: sending extra fields like `role` or `price` that the server accepts.

## Resources
- Large uploads, huge payloads or expensive searches used to exhaust the system.
- Spam through contact forms, invitations or notifications.

## Output
Each relevant abuse case becomes a mitigation in code and a test case for QA.

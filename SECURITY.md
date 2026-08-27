# Security Policy

## Supported versions

| Version | Supported |
| ------- | --------- |
| 1.x     | Yes       |

## What counts as a security issue here

This repository ships prompt-layer software: an agent identity, skills, and
configuration that are installed into Hermes environments. Reports we want:

- **Prompt-injection weaknesses** — any way content processed by the agent
  (webpages, uploads, emails, competitor material, research results) can steer
  it into taking actions, exfiltrating data, or ignoring its approval rules.
- **Approval bypasses** — any path where the agent publishes, sends,
  schedules, spends, or changes an external system without fresh explicit
  approval.
- **Data-handling flaws** — anything that causes credentials, customer data,
  or private context to be written into distributed files, memory it should
  not touch, or deliverables.
- **Distribution integrity** — install or update behavior that overwrites
  user-owned files (`.env`, memory, sessions, `local/`, user-created skills)
  or copies files outside the declared runtime contract.
- Secrets or personal data accidentally committed to this repository.

## Reporting

Report vulnerabilities privately through GitHub:
**Security → Report a vulnerability** on this repository
(GitHub private vulnerability reporting). Please do not open public issues
for security reports.

Include: the Hermes version, the profile version (`hermes profile info`),
reproduction steps or the injected content, observed behavior, and expected
behavior.

Expected response: acknowledgment within 7 days. Fixes ship as a new
distribution version with the issue noted in `CHANGELOG.md` once users can
update safely.

## A note on trust

Hermes profile distributions are unsigned, and installs track the
repository's default branch (Hermes does not yet support git ref pinning).
Review the contents of this repository before installing, prefer the
confirmation-enabled install command, and treat `--yes` as appropriate only
for automation whose operators have already reviewed the repository state
they are installing.

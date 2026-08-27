# Architecture

This repository is a native **Hermes Profile Distribution**. Installing it
creates (or updates) a persistent Hermes profile named `marketing` — a named
agent with its own isolated configuration, memory, sessions, skills, and
credentials. It is not an ephemeral `delegate_task` child: it survives across
sessions, learns with approval, and can be addressed directly or through
Kanban.

## Layers

| Layer | Files | Job |
| ----- | ----- | --- |
| Distribution manifest | `distribution.yaml` | Identity, version, license, requirements, and the exact list of runtime files the distribution owns. |
| Routing metadata | `profile.yaml` | Display name and the routing description the Chief of Staff / Kanban orchestrator uses to decide what to assign here. |
| Identity | `SOUL.md` | Who the agent is, its working loop, evidence standards, approval rules, and completion standard. |
| Configuration | `config.yaml` | Provider-neutral behavior settings. No models, credentials, paths, or services hardcoded. |
| Skills | `skills/marketing-core/` | 17 focused capabilities, one directory per skill, each with its own trigger, procedure, output contract, verification checklist, and a skill-local `templates/` directory holding its deliverable format (Hermes resolves a skill's template references against the skill's own directory, so these paths survive any install location). |
| Shared templates | `templates/` | The four cross-skill shapes — task brief, result handoff, approval request, business profile — installed at the profile root and referenced from `SOUL.md`. |

Everything else in the repository — README, docs, tests, evals, scripts, CI,
contributor files — exists for maintainers and never ships into an installed
profile.

## Distribution-owned vs user-owned

The manifest declares a narrow allowlist of runtime files the distribution
owns. On `hermes profile update`, only those files are replaced. Everything
the owner creates stays theirs:

- `.env`, credentials, and connected accounts
- Memory and sessions
- `local/` — including `local/business-profile.md`, the full marketing
  context built during onboarding
- Configuration overrides
- Any skill the owner creates outside `skills/marketing-core/`

This split is what makes the agent safe to update: identity and capabilities
version forward; the owner's business context and history never get
clobbered.

## Why one profile, many skills

A single mega-prompt degrades: instructions compete, triggers blur, and every
task pays the context cost of every capability. Separate skills keep each
capability's trigger, inputs, procedure, and output contract crisp, and let
the agent load only what the task needs. The identity layer (`SOUL.md`)
holds what must be true everywhere — evidence standards, approval rules, the
working loop — so skills don't repeat it and can't drift from it.

## Control flow

```
Owner ──direct chat──▶ marketing profile
Owner ──assigns──▶ Chief of Staff ──Kanban task──▶ marketing profile
                                        ▲                 │
                                        └──result / one ──┘
                                           blocking question
```

1. Work arrives as a Kanban task (with a brief) or a direct chat message.
2. `marketing-intake-and-routing` validates the brief, locates context, and
   picks the smallest skill set.
3. The selected skill runs its procedure and verification checklist.
4. The result returns as the structured handoff
   (`templates/handoff-result.md`): status, deliverables, sources, facts vs
   assumptions vs unknowns, checks performed, approvals still required, and
   the proposed next action.
5. External actions never execute inside this flow — they end at an
   approval request.

## Data boundaries

- Business context lives in user-owned memory (compact preferences) and
  `local/` (full marketing profile). Distribution updates preserve both.
- Deliverables are written as local artifacts the owner can open; the agent
  never claims they were published or sent anywhere.
- Credentials live wherever Hermes keeps them for the profile — never in
  this repository, never in deliverables, never in memory.
- Third-party content the agent researches is treated as untrusted data;
  instructions found inside it are ignored and reported.

## Versioning

The distribution uses semantic versioning, tracked in `CHANGELOG.md`.
Identity or contract changes are major, new capabilities minor, fixes patch.
Behavior changes ship only through versioned updates the owner installs —
the agent never edits its own distributed files.

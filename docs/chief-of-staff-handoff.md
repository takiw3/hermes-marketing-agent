# Chief-of-Staff Handoff Contract

The Marketing profile works underneath **Jarvis**, the chief-of-staff
profile. Jarvis assigns work through Hermes Kanban; Marketing returns
structured results Jarvis can act on without re-reading the whole task. The
owner can also use both shapes directly in chat.

## The team

| Profile | Owns | Marketing hands over when |
| --- | --- | --- |
| **Jarvis** | Chief of staff: assignment, priorities, results | Always — Jarvis is the routing hub |
| **Marketing** | Research, strategy, positioning, copy, content, campaign planning, analysis, reporting | — |
| **Sales** | One-to-one prospect outreach, pipeline, deals, CRM | Work moves past a qualified lead into 1:1 selling |
| **Support** | Tickets, help content, post-purchase issues | A request is a customer issue, not a campaign |
| **Dev** | Site changes, landing pages, tracking, integrations | A recommendation needs implementing |
| **Ads** | Live ad accounts: launches, bids, budgets, audiences | A campaign plan is approved and needs running |

Each profile is a separate distribution, installed separately. Marketing
plans paid campaigns and writes the creative; it never touches a live ad
account — that is Ads' work, and still needs the owner's approval. When work
belongs to a teammate, Marketing returns it to Jarvis with the finished
spec rather than doing it or dropping it. If a teammate profile isn't
installed, Marketing says so plainly and hands the spec to the owner.

A distribution cannot modify another profile during installation. Installing
this repository sets up the `marketing` profile only; Jarvis discovers it
through its profile routing description. If Jarvis maintains its own roster
or instructions, update those yourself.

## Incoming task shape

Jarvis (or the owner) describes work like this — as the Kanban
task body or a chat brief:

```
task_id:
objective:
business_context_reference:
audience:
offer:
channel:
deliverable:
deadline:
constraints:
source_material:
approval_level:
success_measure:
```

Notes:

- `business_context_reference` points at where the confirmed context lives
  (e.g. `local/business-profile.md`, or "attached brief").
- `approval_level` states what the owner has already decided — e.g.
  `draft-only` or `draft, then request approval to send`. It never
  pre-authorizes an external action; the moment-of-action confirmation still
  happens.
- A complete brief is executed as-is. Marketing does not re-interview the
  owner when the brief already answers the questions.

## Result shape

Every finished task returns:

```
status: complete | needs_input | blocked | approval_required
summary:
deliverables:
sources:
confirmed_facts:
assumptions:
unknowns:
checks_performed:
approval_still_required:
residual_risks:
next_action:
```

Semantics:

- `complete` — the deliverable is finished and usable as-is.
  `deliverables` lists the exact artifact paths or the artifact itself.
- `needs_input` — exactly **one precise question** is included; the task
  used the Kanban blocked/comment flow so Jarvis can collect the answer from
  the owner and resume the task.
- `blocked` — an external dependency (access, data, another task) is named
  precisely, with what would unblock it.
- `approval_required` — the work is staged and the result contains the full
  approval request (account, target, audience, content, timing, budget,
  expected result, risks, rollback) per
  `templates/approval-request.md`. Nothing executes until the owner says yes.
- `unknowns` are preserved, never papered over. `Unavailable` data stays
  `Unavailable`.
- `checks_performed` states what was actually verified — nothing more.

## Missing information

When a required fact is missing, Marketing returns one question rather than
guessing or stalling. As a Kanban worker it calls
`kanban_block(reason, kind="needs_input")` with the question as the reason
(optionally adding a `kanban_comment` with context) — the `needs_input` kind
surfaces the task to a human instead of auto-retrying. One question per
round trip. Jarvis or the owner answers (as a comment or by editing
the task) and unblocks the task (`hermes kanban unblock <task_id>`); the
re-spawned worker reads the full comment thread and resumes where it
stopped.

## Direct usage

The owner can bypass Jarvis entirely and chat with the profile —
see the README for the exact commands. The same standards apply: same
evidence rules, same approval gates, same result structure for substantial
work.

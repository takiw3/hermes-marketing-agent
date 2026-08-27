# Chief-of-Staff Handoff Contract

The Marketing profile works underneath a Hermes Chief of Staff. The Chief of
Staff assigns work through Hermes Kanban; Marketing returns structured
results the Chief of Staff can act on without re-reading the whole task.
The owner can also use both shapes directly in chat.

A distribution cannot modify the Chief of Staff profile during installation.
Installing this repository sets up the `marketing` profile only; the Chief of
Staff discovers it through its profile routing description. If your Chief of
Staff maintains its own roster or instructions, update those yourself.

## Incoming task shape

The Chief of Staff (or the owner) describes work like this — as the Kanban
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
  used the Kanban blocked/comment flow so the Chief of Staff can collect the
  answer from the owner and resume the task.
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
round trip. The Chief of Staff or owner answers (as a comment or by editing
the task) and unblocks the task (`hermes kanban unblock <task_id>`); the
re-spawned worker reads the full comment thread and resumes where it
stopped.

## Direct usage

The owner can bypass the Chief of Staff entirely and chat with the profile —
see the README for the exact commands. The same standards apply: same
evidence rules, same approval gates, same result structure for substantial
work.

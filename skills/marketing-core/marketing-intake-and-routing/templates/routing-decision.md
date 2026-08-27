# Template: Routing Decision

The output of marketing-intake-and-routing: what was validated, what
context exists, and the smallest skill set that completes the work — or the
one question that unblocks it.

```
task_id: <id from the brief, or "direct-chat">
request: <the incoming ask, one line, in the owner's words>
brief_status: complete | gaps: <each material gap found, and how it was
  closed — onboarding, one question, or still open>
context_status: <profile complete | in progress — next open item: X | none>
onboarding: <not needed | run — N questions asked | resumed at: X |
  paused at: X>
confirmed_context_used:
  - <each fact the routing relied on, with its classification tag>
route:
  - order: 1 — skill: <skill-name> — deliverable: <the exact artifact this
    skill alone produces> — inputs_forwarded: <brief fields and profile
    sections that skill needs, prices exact>
excluded:
  - <skill considered — why it adds no required artifact for this task>
escalations: <compliance or refusal flags the executing skill must carry
  forward, or none>
open_question: <exactly one question when status is needs_input, else none>
status: routed | needs_input
```

Rules:

- One deliverable, one skill is the normal case. Every routed skill must
  name the artifact only it produces; a skill that can't is excluded.
- `open_question` is one sentence, answerable in one sentence, and never
  something the brief or `local/business-profile.md` already answers.
- Exact prices pass through `inputs_forwarded` digit for digit as the owner
  stated them.
- This document routes work; it never contains the marketing deliverable
  itself.
- `escalations` travels with the work — an executing skill reading this
  decision must see every flag intake saw.

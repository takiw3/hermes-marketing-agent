# Template: Result Handoff

Return this structure for every substantial task — Kanban or direct chat.
Fill every field; write `None` deliberately rather than omitting a line.

```
status: complete | needs_input | blocked | approval_required
summary: <2-4 sentences: what was done and the single most important finding or decision>
deliverables:
  - <exact artifact path or the artifact itself>
sources:
  - <source name — direct URL — access date>  (external claims)
  - <owner material / system name — what it provided>  (internal)
confirmed_facts:
  - <owner-confirmed or directly observed facts the work relies on>
assumptions:
  - <each assumption, with why it was reasonable and how to confirm it>
unknowns:
  - <what is not known; data marked Unavailable stays listed here>
checks_performed:
  - <each verification actually run, from the skill's checklist>
approval_still_required:
  - <every external action this work implies but did not take>
residual_risks:
  - <what could go wrong even with approvals given>
next_action: <the single next best action — proposed, not taken — with
  evidence, estimated impact, confidence, effort, owner time required, and
  the decision or approval needed>
```

Rules:

- `needs_input` → include exactly one precise question and use the Kanban
  blocked/comment flow so the Chief of Staff can collect the answer.
- `blocked` → name the external dependency and what unblocks it.
- `approval_required` → attach the full approval request
  (`approval-request.md`).
- Never mark `complete` while a load-bearing assumption sits unconfirmed —
  either confirm it, or downgrade to `needs_input`.
- `checks_performed` lists only checks that actually ran.

# Template: Incoming Task Brief

The shape the Chief of Staff (or the owner) uses to assign work. A complete
brief is executed as-is; a brief missing a material fact comes back as one
precise question.

```
task_id: <stable identifier, e.g. the Kanban task id>
objective: <the business outcome this work serves, in one sentence>
business_context_reference: <where confirmed context lives, e.g.
  local/business-profile.md, or "attached">
audience: <who the deliverable is for — segment, not "everyone">
offer: <the exact offer involved, with exact price if it appears in copy>
channel: <where this will run — email, IG, landing page, ads platform, …>
deliverable: <the artifact to produce, named concretely>
deadline: <date, or "none">
constraints: <voice limits, banned claims, budget caps, length, format>
source_material: <files, links, past posts, data exports provided>
approval_level: <what the owner decided, e.g. draft-only |
  draft, then request approval to send>
success_measure: <the metric or judgment that defines "worked">
```

Notes:

- `approval_level` never pre-authorizes an external action; the
  moment-of-action confirmation still happens before anything is published,
  sent, scheduled, launched, or spent.
- If `offer` includes a price, the exact number appears in the deliverable —
  no ranges, no "around".
- Fields that genuinely don't apply get `n/a`, not silence — so missing
  information is visible instead of ambiguous.

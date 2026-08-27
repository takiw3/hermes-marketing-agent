# Template: Copy Brief

The deliverable for `conversion-copywriting`: the completed brief and the finished copy in one artifact, so the owner can see what was targeted and approve what was written in a single read.

```
copy_brief:
  audience: <who this is for, one line>
  offer: <name, contents, exact price>
  pain: <the problem this copy speaks to, in the customer's words where possible>
  desired_action: <the one action>
  channel_format: <where it runs, length constraints>
  voice_source: <voice guide or samples used>
  success_measure: <what the owner counts>
  constraints: <claims not to make, regulated terms, or None>
  proof_used: <owner-approved proof included, or None>
copy:
  headline: <the recommended headline>
  headline_variants:
    - <variant — when to prefer it>
  body: <the finished copy in full>
  cta: <the action plus what happens next>
  cta_variants:
    - <variant — when to prefer it>
reasoning:
  - <major choice — why, one or two sentences>
sources:
  - <source — URL and access date for external claims; owner material named for internal facts>
unknowns:
  - <what is not known, or None>
```

Rules:

- One audience, one offer, one action per brief. A second action means a second brief.
- Prices are exact owner-provided numbers. No ranges, no rounding.
- `proof_used: None` means the copy makes no proof claims. Never imply proof that is not listed.
- Variants appear only where a choice is genuinely contested, each with a when-to-prefer note.
- Fill every field; write `None` deliberately rather than leaving a field out.

# Template: Email Sequence

The deliverable for `email-sequences`: every email in full, its operating rules, the tracking plan, and the compliance checkpoints — one artifact the owner can approve and load. Nothing in this artifact sends anything.

```
sequence:
  name: <sequence name>
  goal: <what this flow exists to cause>
  success_measure: <what the owner counts, and over what window>
  audience: <who enters>
  entry_trigger: <the exact event that starts the flow>
  exit_rules:
    - <condition that removes a recipient, including goal completion>
  re_entry: <suppression window or rule, or None>
emails:
  - id: <number and job, e.g. "1 — recover the cart">
    trigger: <what causes this email relative to entry or the prior email>
    timing: <delay, with day/time constraints if any>
    segmentation: <rule for who gets this version, or "all entrants">
    subject: <the subject line>
    preheader: <the preheader>
    body: <the full body copy>
    cta: <the action plus destination>
    exit_check: <conditions verified before this email sends>
tracking_plan:
  per_email: <what is measured for each send>
  sequence_level: <goal completions, attribution window, and its stated limits>
  caveats: <open-rate reliability, attribution-is-a-model note>
compliance_checkpoints:
  consent_basis: <how recipients opted in, as stated by the owner>
  unsubscribe: <mechanism present in every email, and honoring process>
  sender_identity: <from-name, reply-to, business mailing address>
  verify_current: <jurisdiction requirements to confirm, with official source URL and access date>
sources:
  - <owner material and external sources with URLs and access dates>
unknowns:
  - <what is not known, or None>
```

Rules:

- Every email carries all four copy fields (subject, preheader, body, CTA) and all four operating fields (trigger, timing, segmentation, exit_check). No stubs.
- Exit rules always include goal completion.
- Prices are exact owner-provided numbers. No invented deadlines, stock levels, or proof.
- `consent_basis` is the owner's statement, not an inference.
- Compliance items are checkpoints to verify against official sources at execution time, not legal conclusions.
- This artifact is a draft for approval. Loading, scheduling, or sending requires a separate approval request.

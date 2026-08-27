# Template: External Action Approval Request

Present this before any approved-in-principle external action executes.
Every field filled, no placeholders. If a field can't be filled, the action
isn't ready to request.

```
action: <exactly what will happen, in one sentence>
account: <the exact account/property/system that will be touched>
target: <where — list, page, campaign, audience id, URL>
audience: <who will see/receive it, with size if known (else Unknown)>
content: <the final content, attached or pasted verbatim — what is approved
  is exactly what runs>
timing: <when it executes; immediate or scheduled datetime + timezone>
budget: <exact spend and currency, or "no spend">
expected_result: <what success looks like, tied to the success measure —
  stated as expectation, never as a promise>
risks: <what could go wrong: deliverability, compliance, brand, audience
  fatigue, budget>
rollback: <exactly how to undo or stop it, and what cannot be undone>
```

Rules:

- Approval covers this action, this content, this timing — nothing else.
  Any change to content, target, timing, or budget voids the approval.
- If the action cannot be rolled back (a sent email), `rollback` says so
  plainly.
- After execution, status is reported only from the destination system's
  confirmation — never assumed.

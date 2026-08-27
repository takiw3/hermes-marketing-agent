# Template: Content Calendar

The deliverable for `social-content-calendar`: a defined window of publish-ready slot briefs. Anyone picking up a slot can produce it without a second planning pass.

```
calendar:
  window: <start date — end date>
  channels: <accounts this calendar feeds>
  goals: <what this period's content must cause, with the measure per goal>
  cadence: <slots per week per channel, and the capacity reasoning>
slots:
  - slot: <number>
    channel: <account/platform>
    date: <publish date, with time if the owner sets one>
    format: <reel, carousel, story, text post, email, live>
    hook: <the actual opening line or on-screen text, written out>
    audience: <who this slot is for>
    goal: <the one goal this slot serves>
    cta: <what the viewer is asked to do>
    asset_needs: <exactly what must exist to produce this slot>
    owner: <who produces it>
    status: <draft | assets-needed | ready | approved>
    measurement: <what is counted for this slot>
production_handoffs:
  - <slot number → skill that produces it>
assumptions:
  - <each planning assumption and how to confirm it>
sources:
  - <owner material; analyses cited with dates; external sources with URLs and access dates>
unknowns:
  - <what is not known; data marked Unavailable stays listed here>
```

Rules:

- Every slot fills all eleven fields. A hook is the actual line, never a topic description.
- Slot count stays within stated production capacity.
- Status never starts at `published` or `scheduled`; those states come only from confirmed external action, which needs its own approval.
- Prices are exact owner-provided numbers.
- Platform constraints are labeled "verify current specs against the platform's official documentation (cite URL + access date)".
- Data-backed choices cite the analysis and numbers; everything else lands in assumptions.

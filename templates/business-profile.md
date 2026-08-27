# Template: Business Profile (`local/business-profile.md`)

The full marketing context built during onboarding. Lives in the profile's
user-owned `local/` directory, which distribution updates preserve. Every
entry carries a classification tag so later work knows what it can rely on:

`[confirmed]` owner-confirmed · `[observed]` directly observed ·
`[sourced]` external source (URL + access date) · `[calc]` calculation ·
`[inferred]` inference · `[unknown]` not yet known

```markdown
# Business Profile — <Business Name>
Last updated: <date> · Status: <complete | in progress — next open item: X>

## Business
- Name: … [confirmed]
- Website: … [confirmed]
- Market / location: … [confirmed]
- Business model: … [confirmed]
- Industry & jurisdiction: … [confirmed]

## Offers & economics
- Offer 1: <name> — exact price: <$X> [confirmed]
- Margins / economic constraints (when relevant): … [confirmed | unknown]

## Buyer
- Ideal buyer: … [confirmed | inferred]
- Pains: … [confirmed | sourced | inferred]
- Desired results: …
- Objections: …
- Buying triggers: …

## Sales process & funnel
- Stages, handoffs, current conversion data (or [unknown]): …

## Positioning & proof
- Differentiation: … [confirmed]
- Approved proof & claims: … [confirmed]
- Claims the business must NOT make: … [confirmed]

## Voice
- Brand voice samples (links/files): … [observed]
- Voice rules (from brand-voice-analysis, if run): …

## Channels & performance
- Current channels: … [confirmed]
- Available performance data & where it lives: … [confirmed | unknown]

## Goals & capacity
- Marketing goals, source metrics, time window: … [confirmed]
- Budget: … [confirmed | unknown]
- Production capacity: … [confirmed]

## Competitors
- <name — URL — what's known — accessed date> [sourced]

## Constraints
- Legal / privacy / consent / endorsement / disclosure: … [confirmed | unknown]

## Approval boundaries
- Agent MAY draft/stage: … [confirmed]
- Agent may EXECUTE only with fresh approval: everything external (fixed)
- Required human approval points: … [confirmed]

## Open items
- <the next onboarding question not yet asked or answered>
```

Never stored here: credentials, payment information, private contact lists,
raw customer records, health information, or personal data the work doesn't
need.

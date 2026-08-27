# Template: Ad Campaign Plan

The complete paid campaign plan: everything needed to approve and launch, with every external action stopped at a named gate. This document plans; it never executes.

```
# Ad campaign plan: <offer> — <platform>

## Plan metadata
platform: <ad platform>
account_status: <exists / access state, or none yet>
objective: <what the campaign must cause>
success_measure: <the number that proves it, and where it is read>
landing_destination: <URL the ads point at>
budget_ceiling: <owner-confirmed monthly maximum — note where the owner confirmed it>

## Strategy
<campaign structure, funnel stage per campaign, geography, objective split,
and the reasoning for each choice — short paragraphs, not slogans>

## Targeting
| parameter | value | tag: owner-confirmed / assumption | basis | how to confirm |
| --- | --- | --- | --- | --- |
| <audience / keyword set / placement / exclusion> | <value> | <tag> | <why this is reasonable> | <what confirms or kills it> |

## Creative matrix
| angle | format | audience | reasoning | what proves it wrong |
| --- | --- | --- | --- | --- |
| <angle> | <format> | <audience> | <why this angle> | <disproof signal> |

## Ad copy
### <matrix cell: angle / format / audience>
headline: <verbatim, within verified limits>
description: <verbatim, within verified limits>
cta: <verbatim>
<repeat per matrix cell; exact owner prices wherever price is named>

## Budget math
<one line per step: allocation, spend → clicks → conversions → sales →
revenue. Every number tagged (owner-confirmed) or (assumption — basis).
Totals re-added. All outputs labeled scenario math, never promised.>

## Tracking requirements
- <conversion events the destination can actually fire>
- <naming conventions and UTM scheme>
- <what must exist and be verified before launch is even proposed>

## Test design
comparison: <what is being tested against what>
primary_measure: <the one number that decides>
minimum_evidence: <spend or time before judging — no early calls>
decision_rule: <if X then Y, written before launch>

## Stop conditions
- <metric> <threshold> over <window> → <action>
<each one executable without debate; always include the hard stop at the
budget ceiling>

## Approval gates
- <every external action this plan implies — launch, budget entry, audience
  upload, tracking change — each gated on a fresh approval request; none taken>

## Specs and policy checks
- <spec or policy item>: <requirement per official docs> — <this plan> — <pass | fail> — <official doc URL — access date>

## Sources and assumptions
sources:
  - <owner material or URL — access date>
assumptions:
  - <every assumption used anywhere above, gathered in one list>
```

Rules:

- This document never records an executed action. A filled plan ends at the approval gates; the handoff status is `approval_required` when launch is the next step.
- Every number in the budget math carries a tag. An untagged number is a defect.
- The budget ceiling is owner-confirmed, appears once as a fact, and no scenario exceeds it.
- Prices in ad copy are exact owner-provided numbers. Proof, reviews, and results are never invented.
- Specs and policies are verified at execution time from the platform's official documentation with URL and access date. Never from memory.
- Projections are scenario math stated as expectations. Missing data is `Unavailable`, never zero.

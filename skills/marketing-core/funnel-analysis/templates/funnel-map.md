# Template: Funnel Map

The funnel analysis deliverable: stages with sourced metrics, drop-off math shown, tracking gaps, labeled hypotheses, and ranked experiments.

```
# Funnel map: <business> — <funnel end event>

## Funnel metadata
business: <business name>
end_event: <the conversion event that counts as the funnel's end>
date_range: <window under analysis>
baseline: <comparison window, or None>
data_sources:
  - <system — report or export name — metric coverage — access date>

## Stage map
| stage | definition | source metric (system / report / metric) | value | window | notes |
| --- | --- | --- | --- | --- | --- |
| <stage name> | <what counts as entering this stage> | <where the number comes from> | <count or Unavailable> | <dates> | <caveats> |

## Drop-off math
| from → to | math | rate | absolute loss | baseline | change |
| --- | --- | --- | --- | --- | --- |
| <stage A → stage B> | <B count ÷ A count, shown> | <rate> | <A minus B> | <baseline rate or Unavailable> | <delta> |
overall: <end count ÷ entry count, shown> = <rate> (baseline <rate or Unavailable>)

## Tracking gaps
- <gap — why it matters — how to close it>

## Friction hypotheses
- HYPOTHESIS — <stage>: <the suspected friction, tied to the numbers that
  prompted it> — confirming evidence needed: <what would confirm or kill it>

## Opportunity sizing (scenario math)
<what a stated relative improvement at the leaking stage is worth in end
conversions and revenue at the owner's exact price or AOV — labeled scenario
math, never a promise>

## Prioritized experiments
| # | hypothesis | change | primary measure | impact | confidence | effort | first step |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | <hypothesis tested> | <what changes> | <the one deciding number> | <high/med/low> | <high/med/low> | <high/med/low> | <the next concrete step> |
```

Rules:

- Every stage value traces to a named source, or reads `Unavailable`. Zero is a measured value, never a stand-in for missing data.
- The `math` column shows the division; a rate without its counts is a defect.
- Hypotheses always carry the HYPOTHESIS label and their confirming evidence. None is written as a finding.
- Where two sources disagree on a count, both values appear and the conflict is marked unresolved — never averaged away.
- Opportunity sizing uses the exact owner-provided price or AOV and stays labeled scenario math.
- A change that coincides with a drop is recorded as coinciding. Correlation is not causation.

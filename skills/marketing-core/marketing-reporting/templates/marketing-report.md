# Template: Marketing Report

The full output format for `marketing-reporting`. Every number has a source
and window; every gap stays `Unavailable`; explanations are correlations
unless a mechanism was tested.

```
# Marketing report: <business> — <report window>

business: <owner / business name>
report_window: <start date – end date, timezone>
comparison_window: <start date – end date>
prepared_on: <date of this run>

## Data sources

| source | what it provides | window pulled | pulled on | coverage notes |
|--------|------------------|---------------|-----------|----------------|
| …      | …                | …             | …         | full / partial / Unavailable — why |

## Results by channel

### <channel>
| metric | current | prior | change |
|--------|---------|-------|--------|
| …      | …       | …     | …      |
<Unavailable stays in the cell — never 0, never blank, never estimated>

## What changed and plausible why
- <movement, with numbers> — coincided with <dated plausible drivers> —
  correlation, not causation, unless a tested mechanism is cited.

## Experiments concluded this period
- <experiment — result vs baseline — decision taken — learning record path>

## Decisions this report surfaces
- <owner-level choice — the finding behind it — cost of not deciding>

## Proposed next operating actions
- <action (proposed, not taken) — the finding it answers — effort — expected
  direction, never a promised result>

## Data gaps and fixes
- <each Unavailable — why it is missing — the concrete fix and who does it>
```

Rules:

- A number with no named source and window does not enter the report.
- `Unavailable` is preserved in place through every table and repeated in
  the gaps section with a fix. It never becomes zero.
- Causal language only where a test established the mechanism; everything
  else is "coincided with" plus labeled plausible drivers.
- Prices and revenue are exact owner-confirmed or platform-exported values,
  labeled as such; nothing missing is invented.
- Actions are proposed, not taken; sending or publishing the report itself
  requires fresh approval.

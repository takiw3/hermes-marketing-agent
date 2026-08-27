# Template: CRO Audit

The full output format for `website-cro-analysis`. Observed issues carry
evidence; hypotheses are labeled; nothing promises a conversion increase.

```
# CRO audit: <site or page set>

prepared_for: <owner / business name>
prepared_on: <date of this run>
pages_audited:
  - <URL — access date — viewports checked (e.g. desktop 1440px, mobile 390px)
    — conversion action for this page>
data_sources:
  - <system name — what it provided — time window — pulled on>
  - <missing source — Unavailable — what it would have added>

## Observed issues (evidence-backed)

### OI-<n>: <short issue name>
- page: <URL>
- location: <where on the page>
- observed: <exactly what was seen>
- evidence: <screenshot filename, or the exact element and its state>
- why it likely hurts conversion: <reasoning tied to the observation and any
  measured stage — directional, never a promised number>
- severity: <high | medium | low>
- effort: <high | medium | low>

## Test hypotheses (not observations)

### TH-<n>: <short hypothesis name>
- hypothesis: If we <change X> on <page>, we expect <measure Y> to <move>,
  because <reasoning or evidence Z>.
- primary measure: <the one number the test reads>
- next step: design via measurement-and-experimentation before any change is
  called an improvement.

## Prioritized list

| rank | id | type (observed issue / hypothesis) | expected effect (directional) | confidence | effort | depends on |
|------|----|------------------------------------|-------------------------------|------------|--------|------------|
| 1    | …  | …                                  | …                             | …          | …      | …          |

<one-sentence justification for each of the top three ranks>

## What was not reviewed
- <page, device, or data left out — and why>
```

Rules:

- Every observed issue cites a screenshot filename or an exact page element,
  with page URL and access date. No evidence, no entry.
- Hypotheses never appear in the observed-issues section, and observations
  never appear as hypotheses.
- Expected effect is directional only. No promised or projected conversion
  increase anywhere in the audit.
- Analytics values come from named owner systems with time windows; missing
  data stays `Unavailable`, never zero.
- Page prices are checked against the owner's exact confirmed prices;
  mismatches are logged as observed issues.

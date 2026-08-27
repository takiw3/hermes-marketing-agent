# Template: Experiment Design

The full output format for `measurement-and-experimentation`. One hypothesis,
one primary measure, real baselines, honest sample math, and a decision rule
written before launch.

```
# Experiment design: <experiment name>

business: <owner / business name>
prepared_on: <date of this run>
status: draft
change_under_test: <exactly what varies, and on which page, email, campaign,
  or asset>
audience: <who is exposed — segment, channel, device where relevant>

## Hypothesis
If <change> for <audience>, then <primary measure> will <direction>, because
<evidence-based reason>.

## Baseline
- <measure — source system — exact time window — value — pull date>
- <missing measure — Unavailable — how and when it will be collected>

## Event tracking spec

| event name | fires when | properties | destination | exists today |
|------------|-----------|------------|-------------|--------------|
| …          | …         | …          | …           | yes / no — add |

<platform naming or limit checks: official documentation URL — access date>

## Measures
- primary: <one measure, as close to money or committed action as the data
  allows>
- guardrails:
  - <measure that must not degrade — tolerance>

## Sample constraints
- volume: <sessions/sends/impressions per week, with source and window>
- smallest effect worth acting on: <owner-confirmed or proposed default>
- estimated sample and runtime: <shown math, labeled estimate>
- what this test cannot detect: <stated plainly; an underpowered test is
  called underpowered, with the real options listed>

## Decision rule
- read date: <date>
- ship if: <condition on primary measure with guardrails intact>
- kill if: <condition>
- extend if: <condition and the new read date>

## Learning record (filled at conclusion)
- result vs baseline: <numbers>
- decision taken: <ship / kill / extend, and by whom>
- what was learned: <one paragraph>
- stored at: <local/ path>
```

Rules:

- One hypothesis and one primary measure per design; more questions means
  more designs.
- Baselines come from named owner systems with time windows and pull dates;
  missing values stay `Unavailable` and are never backfilled from benchmarks.
- The decision rule is written before launch and does not move afterward.
- Sample math uses real traffic, is labeled an estimate, and never shrinks
  to make a test look runnable.
- The design promises detection capability, never an outcome. Launch and
  tracking changes end at an approval request.

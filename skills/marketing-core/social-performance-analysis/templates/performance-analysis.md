# Template: Performance Analysis

The deliverable for `social-performance-analysis`: what the data covers, what it shows, what remains a hypothesis, and what test settles it. Observation and explanation never share a section.

```
analysis:
  question: <the decision this analysis serves>
  source: <each data source — export/surface name, export or access date>
  date_range: <the window actually covered by the data>
  coverage: <metrics present; posts included; known gaps>
  unavailable:
    - <each missing metric or segment, marked Unavailable, with why if known>
patterns:
  - finding: <what the numbers show, stated as observation>
    numbers: <the actual figures behind it — group sizes, averages/medians, comparisons>
    confounds: <overlapping variables or outliers that could explain it, or None found>
hypotheses:
  - hypothesis: <a plausible why, labeled as hypothesis>
    supports: <which pattern it would explain>
    would_be_wrong_if: <what evidence would kill it>
next_tests:
  - test: <the smallest test that separates the variables>
    measures: <what gets counted>
    size: <posts or weeks needed, stated as a rough requirement>
owner_reported:
  - <outcomes the owner stated, kept separate from platform-measured data, or None>
sources:
  - <every source with URL where applicable and access date>
unknowns:
  - <open questions the data cannot answer>
```

Rules:

- Missing data is `Unavailable` — never zero, never an estimate.
- Patterns contain observations only; anything causal-sounding belongs in hypotheses, labeled.
- Every pattern shows its numbers and group sizes; small samples are flagged.
- Every hypothesis carries a `would_be_wrong_if`.
- Correlation is never presented as causation; coincidence in time is reported as exactly that.
- No promised lifts. Tests propose learning, never guaranteed results.

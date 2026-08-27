# Behavior eval fixtures

These 18 YAML files are synthetic behavior evaluations for the marketing
profile. Every business, person, URL, and number in them is fictional. The
format, the universal pass conditions, and the full suite table live in
`docs/evals.md`; run and validate the suite with `scripts/run_evals.py`
(add `--live` for a model-backed run against an installed profile). One rule
above all when reporting results: an eval that was not run is never reported
as passed.

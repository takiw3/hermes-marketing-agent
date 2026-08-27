# Changelog

All notable changes to this distribution are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-08-26

### Added

- Initial release of the `marketing` Hermes Profile Distribution.
- Agent identity (`SOUL.md`): senior marketing operator for business owners,
  working under a Hermes Chief of Staff or directly with the owner.
- 17 marketing skills under `skills/marketing-core/`: intake and routing,
  strategy, brand voice analysis, customer and offer research, conversion
  copywriting, email sequences, social content calendar, social performance
  analysis, carousel creation, script creation, paid ad campaigns, funnel
  analysis, competitor intelligence, website CRO analysis, measurement and
  experimentation, marketing reporting, and weekly marketing review.
- Deliverable templates in `templates/`.
- Business-owner onboarding flow (one question at a time, consent-gated
  research, user-owned storage in memory and `local/`).
- Permission model: research, analyze, draft, and recommend by default;
  fresh explicit approval required for every external action.
- Chief-of-Staff handoff contract (incoming task shape and result shape)
  with Hermes Kanban routing.
- Synthetic behavior evaluations in `evals/` and validation tooling in
  `scripts/`.
- CI validation workflow, contributor documentation, and security policy.

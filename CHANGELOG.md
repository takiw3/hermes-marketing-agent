# Changelog

All notable changes to this distribution are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-08-27

### Added

- Team composition. `SOUL.md`, the README, and the handoff doc now name the
  full profile team — **Jarvis** (chief of staff), **Marketing**, **Sales**,
  **Support**, **Dev**, **Ads** — with the seams between them: Marketing
  plans paid campaigns but never touches a live ad account (Ads), owns
  demand generation up to a qualified lead (Sales), takes voice-of-customer
  evidence from tickets without answering them (Support), and specifies
  site and tracking changes without implementing them (Dev). Work belonging
  to a teammate goes back to Jarvis with a finished spec rather than being
  done or dropped; a missing teammate profile is stated plainly.

### Changed

- Lowered `hermes_requires` from `>=0.20.5` to `>=0.20.0`, widening support
  to six releases (0.20.0 through 0.20.5) plus 0.20.6. The full install
  suite was run against every one of them — 55 checks each, all passing.
  0.20.0 is the floor because the path-aware `distribution_owned` allowlist
  landed in that release (v2026.8.3); below it the installer copies every
  top-level repository file into the profile and `profile update` replaces
  `skills/` wholesale, destroying user-created skills. Refusal below the
  floor was verified on 0.19.1: a clear version error, nothing written.
- `scripts/test_install.sh` reads the version from `distribution.yaml`
  instead of hardcoding it.

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

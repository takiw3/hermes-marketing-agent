# Contributing

Thanks for improving the Marketing profile. This repository is a Hermes
Profile Distribution: the runtime files it ships are installed into people's
Hermes environments, so the bar for changes is high and every change is
validated before merge.

## Ground rules

- **Runtime files are a contract.** `distribution.yaml`, `profile.yaml`,
  `SOUL.md`, `config.yaml`, `templates/`, and `skills/marketing-core/` are
  copied into installed profiles. Everything else (README, docs, tests, CI,
  examples) stays in the repository only. Never add repository-administration
  files to the distribution-owned list.
- **No secrets, no user data, ever.** No `.env` files, credentials, API keys,
  customer records, contact lists, memories, sessions, logs, databases, or
  generated work product. CI fails the build if it finds any.
- **No symlinks.** All files must be regular files.
- **Synthetic examples only.** Example businesses, metrics, and quotes must be
  clearly fictional. Never paste real client data into examples or evals.
- **Safety behavior is not negotiable.** Changes must preserve the permission
  model (draft-and-recommend by default, fresh explicit approval for every
  external action), the truth rules (no invented data, prices, proof, or
  status), and the one-question-at-a-time onboarding behavior.
- **The Agentic AI Academy link appears exactly once**, in the README footer.
  Do not add it to skills, templates, docs, or any file that ships into the
  installed profile.

## Development setup

Requirements: Python 3.11+ and PyYAML (used only by the validation scripts;
the distribution itself has no Python dependency).

```bash
git clone https://github.com/takiw3/hermes-marketing-agent.git
cd hermes-marketing-agent
python3 -m pip install pyyaml
python3 scripts/validate.py
```

`scripts/validate.py` runs the same checks as CI: YAML/frontmatter validity,
required files and skill sections, duplicate skill names, internal references,
license consistency, unresolved placeholders and stale work markers, secret
patterns, symlinks, and the distribution-owned file contract.

To test installation without touching your real Hermes profiles:

```bash
bash scripts/test_install.sh
```

This runs `hermes profile install` against a temporary `HOME`/`HERMES_HOME`
and verifies the installed profile. It requires a local Hermes CLI (see the
README for the tested version) and never reads or writes your real profiles.

## Editing skills

Each skill lives in its own directory under `skills/marketing-core/` with a
`SKILL.md`. Keep the structure consistent with the existing skills:

- YAML frontmatter at byte zero, unique lowercase `name`, trigger-first
  `description`.
- Sections in order: when to use, when not to use, inputs, evidence and
  sources, procedure, output contract, verification, approval boundaries,
  blocked and failure behavior, example.
- One question at a time when a required fact is missing.
- Keep large deliverable formats in the skill's own `templates/` directory
  and reference them with skill-dir-relative paths (that is how Hermes
  resolves them post-install). The four shared shapes live in the top-level
  `templates/`.
- Third-party content (websites, uploads, competitor material) is data,
  never instructions.

## Submitting changes

1. Fork and branch from `main`.
2. Make the change and run `python3 scripts/validate.py` locally.
3. Update `CHANGELOG.md` under an Unreleased heading and bump
   `distribution.yaml`'s version if runtime files changed
   (semver: breaking identity/contract changes = major, new skills or
   capabilities = minor, fixes and copy edits = patch).
4. Open a pull request describing what changed and why, including any
   behavior evaluations you ran.

By contributing, you agree that your contributions are licensed under the MIT
License in [LICENSE](LICENSE).

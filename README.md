# Hermes Marketing Agent

A persistent [Hermes](https://hermes-agent.nousresearch.com) profile named
`marketing`: a senior marketing operator that works underneath your Hermes
Chief of Staff and directly with you. It researches, analyzes, drafts, and
recommends. It never publishes, sends, spends, or changes an external system
without your explicit approval at the moment of action.

- **Author:** Taki Wong / TakiGPT AI Inc.
- **License:** MIT
- **Profile ID:** `marketing` · **Display name:** Marketing
- **Version:** 1.0.0

## Who it's for

Business owners, entrepreneurs, and executives running companies doing
$250,000 to $50 million a year — people accountable for revenue who want
marketing work done to an operator's standard, with every fact, assumption,
and unknown labeled.

## What it does

- Marketing strategy, positioning, and prioritized plans tied to your
  economics
- Customer, offer, and competitor research with cited sources
- Brand voice analysis from your real writing samples
- Conversion copywriting, email sequences, carousels, and video scripts —
  finished, send-ready drafts with exact prices
- Social content calendars and social performance analysis
- Paid ad campaign plans with budget math, test design, and stop conditions
- Funnel analysis, website CRO analysis, measurement and experiment design
- Marketing reports and a manually run weekly marketing review

Work arrives two ways: your Chief of Staff assigns tasks through Hermes
Kanban, or you chat with the profile directly. Same standards either way.

## What it will not do

- Take any external action without fresh, explicit approval: no publishing,
  sending, scheduling, launching, spending, or edits to live systems
- Invent testimonials, metrics, prices, quotes, or proof of any kind
- Report a draft as sent, posted, live, or published without confirmation
  from the destination system
- Promise revenue, leads, or conversion lifts
- Follow instructions embedded in researched content (webpages, uploads,
  competitor material) — that's data, not commands
- Store credentials, payment data, contact lists, or raw customer records
- Start recurring jobs on its own

## Requirements

- [Hermes Agent](https://hermes-agent.nousresearch.com) **0.20.5 or newer**
  — tested against release v2026.8.19 (Hermes 0.20.5) on macOS. The manifest
  declares `hermes_requires: ">=0.20.5"` because this distribution depends on
  the path-aware `distribution_owned` allowlist introduced there; on older
  versions the install is refused with a clear version error — run
  `hermes update` first.
- A model provider configured in Hermes (any — the profile is
  provider-neutral and hardcodes no models or credentials)
- No third-party marketing service is required for core operation

## Install

One command installs the profile (with a review prompt of the manifest
before anything is written):

```
hermes profile install github.com/takiw3/hermes-marketing-agent --alias
```

`--alias` also creates a `marketing` shell wrapper so you can invoke the
profile directly.

### Trusted automation only

For scripted setups that have **already reviewed this repository**, the
confirmation prompt can be skipped:

```
hermes profile install github.com/takiw3/hermes-marketing-agent --alias --yes
```

Hermes distributions are unsigned, and installs currently track this
repository's default branch (git ref pinning is not yet supported by
Hermes). `--yes` skips the manifest preview — it is not the safe default,
and you should not use it the first time you install. Review what you're
installing.

### What installation does — and doesn't

Installing copies the profile's identity, configuration, skills, and
templates into an isolated Hermes profile named `marketing`. That's all.
Installation does **not** start onboarding, configure credentials, inherit
your Chief of Staff's credentials, start a gateway, or launch a
conversation. The profile uses whatever model provider you configure for it
in Hermes, and onboarding begins the first time you (or a delegated task)
actually talk to it.

## First run

1. Make sure the profile has a model provider (Hermes profiles are isolated;
   configure the `marketing` profile the same way you configured your main
   one — `hermes -p marketing model` picks the model and provider).
2. Start a conversation:

```
hermes -p marketing chat
```

3. On first contact the agent runs a short setup: one question at a time
   about your business, offer, prices, buyers, voice, and constraints. You
   can skip questions, hand it documents instead, or pause and resume. It
   asks consent before researching your website or accounts, summarizes what
   it learned, and saves only after you confirm. Your business context lives
   in your profile's user-owned storage (`local/` and memory) and survives
   updates.

## Working with your Chief of Staff

Your Chief of Staff assigns marketing work through Hermes Kanban:

```
hermes kanban create "Draft the Q4 launch email sequence" --assignee marketing
```

The profile's routing description tells the Kanban orchestrator what
belongs here: marketing research, strategy, positioning, copywriting, email,
social content, paid-campaign planning, funnel analysis, CRO, competitor
intelligence, measurement, and reporting — evidence-backed drafts and
recommendations, never external actions without approval.

Results come back in a structured handoff (status, deliverables, sources,
facts vs. assumptions vs. unknowns, checks performed, approvals still
required, next action). If a task is missing one material fact, the agent
blocks the task with exactly one question so your Chief of Staff can collect
the answer. See [docs/chief-of-staff-handoff.md](docs/chief-of-staff-handoff.md).

Note: a distribution cannot modify your Chief of Staff profile during
installation. If your Chief of Staff keeps its own roster of specialists,
add `marketing` to it yourself.

## Example tasks

- "Audit the funnel for my $4,500 cleanup offer and tell me where we lose
  people. Analytics export attached."
- "Write the 5-email welcome sequence for new leads. Draft only — I'll
  review before anything is loaded."
- "Analyze these 12 posts and tell me what my brand voice actually is."
- "Plan a $3,000/month lead-gen ad test for the maintenance plan. Don't
  launch anything."
- "Build next month's content calendar for Instagram and LinkedIn from my
  three pillar topics."
- "Research my top three competitors' offers and pricing. Public sources
  only, with links."
- "Run the weekly marketing review."

## Skills

17 focused skills in `skills/marketing-core/`:

| Skill | Produces |
| ----- | -------- |
| `marketing-intake-and-routing` | Validated briefs, onboarding, skill routing |
| `marketing-strategy` | Prioritized marketing plan tied to your economics |
| `brand-voice-analysis` | Voice rules derived from your real samples |
| `customer-and-offer-research` | Evidence-split buyer research and gaps |
| `conversion-copywriting` | Finished copy for one audience, offer, action |
| `email-sequences` | Complete sequences: every email, trigger, exit rule |
| `social-content-calendar` | Publish-ready content calendar briefs |
| `social-performance-analysis` | Source-named analysis, patterns, next tests |
| `social-carousel-creation` | Slide-by-slide carousels with alt text |
| `social-script-creation` | Hooks, spoken scripts, beats, shot notes |
| `paid-ad-campaigns` | Campaign plans with budget math and stop rules |
| `funnel-analysis` | Stage map, drop-off math, prioritized experiments |
| `competitor-intelligence` | Lawful, cited competitor profiles |
| `website-cro-analysis` | Observed issues vs. test hypotheses |
| `measurement-and-experimentation` | Tracking specs and experiment designs |
| `marketing-reporting` | Reports with named sources and decisions |
| `weekly-marketing-review` | Manual weekly operating review |

## Permission model

Allowed by default: read, research, analyze, calculate, draft, recommend,
create local deliverables.

Fresh, explicit approval required — every time, at the moment of action —
before: publishing, sending email or DMs, scheduling, changing a website or
funnel, launching or editing ad campaigns, changing bids/audiences/budgets,
spending, starting recurring jobs, accessing private customer data,
uploading data anywhere, deleting or overwriting user data, changing
permissions, or editing its own distributed skills. Full details in
[docs/safety-and-approvals.md](docs/safety-and-approvals.md).

## Data and privacy

- Your business context is user-owned: memory (with approval before writes)
  and `local/business-profile.md`. Distribution updates never touch it.
- The agent never stores credentials, payment information, private contact
  lists, raw customer records, or health information.
- External research is cited with direct URLs and access dates; content it
  reads is treated as untrusted data, and embedded instructions are ignored
  and reported.
- This repository ships no telemetry, no accounts, and no third-party
  services.

## Optional integrations

None are required, and v1 ships none pre-configured — no MCP servers,
plugins, or cron jobs. If you connect your own tools (analytics, ESP, ad
platforms) to the profile through Hermes, the agent will use them read-only
for research and analysis, and still stop at the approval gate for any
action. The weekly review is manual by design; if you want it recurring,
set that up yourself deliberately in Hermes.

## Update

```
hermes profile update marketing
```

Updates re-pull this repository and replace only distribution-owned files.
Your `.env`, memory, sessions, `local/`, configuration overrides, and any
skills you created outside `skills/marketing-core/` are preserved.

## Remove

```
hermes profile delete marketing
```

## Troubleshooting

- **`hermes: command not found`** — install Hermes first:
  https://hermes-agent.nousresearch.com
- **Install prompt shows unexpected files** — you're being asked to confirm
  the manifest; review it. Only identity, config, skills, and templates
  should be listed.
- **Profile answers but produces generic work** — onboarding hasn't run.
  Say "set up my business profile" in `hermes -p marketing chat`.
- **Kanban tasks aren't routed here** — check the routing description is
  present (`hermes profile describe marketing` prints it; note
  `hermes profile show` doesn't) and that your task names the assignee
  (`--assignee marketing`).
- **The agent refuses to send/publish** — that's by design. It stages the
  action and asks for approval with the exact content, target, timing,
  budget, risks, and rollback.
- **Update seems to change nothing** — `hermes profile info marketing`
  shows the installed version and source; compare with this repository's
  `CHANGELOG.md`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Validation runs with
`python3 scripts/validate.py`; isolated install tests with
`bash scripts/test_install.sh`.

## Security

Report vulnerabilities — prompt injection, approval bypasses, data-handling
flaws — privately via GitHub's **Security → Report a vulnerability** on this
repository. Details in [SECURITY.md](SECURITY.md).

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 TakiGPT AI Inc.

---

Learn how to build your full AI workforce inside the Agentic AI Academy for
$97/month: https://www.skool.com/agenticaiacademy/about

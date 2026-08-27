# Template: Weekly Review

The full output format for `weekly-marketing-review`. A manual,
owner-initiated review: work in motion, results, blockers, experiments, and
the decisions only the owner can make. It schedules nothing.

```
# Weekly marketing review: <business> — week of <start date>

business: <owner / business name>
week_reviewed: <start date – end date>
prepared_on: <date of this run>
run_trigger: <owner request | owner-configured recurrence in Hermes — named;
  never self-scheduled>

## Current work

| item | skill / task | status | status source | in state since |
|------|--------------|--------|---------------|----------------|
| …    | …            | …      | …             | …              |

## Results this week
- <measure — value — source — window>  (Unavailable preserved, never zero)

## Blocked items

| item | blocked on | who unblocks | age | the one unblocking action |
|------|-----------|--------------|-----|---------------------------|
| …    | …         | …            | …   | …                         |

## Experiments
- running: <experiment — week n of m — read date per decision rule — not
  read early>
- concluded: <experiment — result vs baseline — decision taken>

## Owner decisions needed
1. <decision — one line of context — options — recommendation with
   reasoning — cost of another week without a decision>

## Next week's plan (proposed)
- continues: <…>
- starts: <…>
- stops: <…>
```

Rules:

- The run trigger is always stated. This review is owner-initiated;
  recurring runs exist only when the owner deliberately sets them up in
  Hermes. The skill never schedules itself.
- Statuses name their source; nothing is reported done, sent, or live
  without confirmation from the destination system or the owner.
- Results carry source and window; missing numbers stay `Unavailable`.
- Running experiments are read only on their read dates against their
  written decision rules.
- Every plan item is a proposal. The review takes no action and creates no
  standing jobs.

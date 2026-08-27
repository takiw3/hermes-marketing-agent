# Template: Carousel

The finished carousel deliverable: everything the owner or a designer needs to build and publish the post without writing another word.

```
# Carousel: <topic> — <platform> / <account>

## Post metadata
platform: <platform>
account: <account or handle>
audience: <the segment this post targets>
goal: <the action this post must cause — saves, DMs, clicks, profile visits>
success_measure: <the number that says it worked, and where it is read>
voice_source: <voice guide or confirmed voice notes applied>

## Slides
### Slide <n> — <role: hook | build | proof | payoff | cta>
copy: |
  <exact on-slide text, verbatim — what is approved is what is published>
visual: <what the slide shows — layout, imagery, emphasis, brand constraints applied>
alt_text: <plain description of the visual and the on-slide text, for screen readers>

<repeat the Slide block for every slide>

## Caption
<full caption, verbatim — exact owner-provided prices wherever the post sells>

## CTA
<the single action asked of the viewer, matching the goal>

## Platform checks
- <spec item>: required <value per official docs> — this post <value> — <pass | fail> — <official doc URL — access date>

## Sources and assumptions
sources:
  - <owner material or URL — access date>
assumptions:
  - <each labeled assumption, or None>
hook_alternates:
  - <hook candidates not chosen, kept for testing>
```

Rules:

- `copy`, `caption`, and `alt_text` are verbatim publish text, not summaries.
- Every slide carries all three of `copy`, `visual`, `alt_text` — no exceptions.
- Platform checks are verified at execution time from the platform's official documentation, with URL and access date. Never filled from memory.
- Prices are exact owner-provided numbers. A missing price blocks the deliverable; it is never estimated.
- Missing data anywhere is written `Unavailable`, never zero.

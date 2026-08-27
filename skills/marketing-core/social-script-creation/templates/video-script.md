# Template: Video Script

The finished short-form video script deliverable: everything the speaker needs to record the video as-is, and everything an editor needs to cut it.

```
# Video script: <topic> — <platform> / <format>

## Metadata
platform: <platform>
format: <talking head | voiceover | b-roll with captions | mixed>
target_length: <seconds>
speaker: <who is on camera or on mic>
audience: <the segment this video targets>
goal: <the action this video must cause>
success_measure: <the number that says it worked, and where it is read>
voice_source: <voice guide or confirmed voice notes applied>

## Hook options
1. <spoken first line> — visual: <what plays under it>  (LEAD)
2. <spoken first line> — visual: <what plays under it>
3. <spoken first line> — visual: <what plays under it>

## Script
### Segment <n> — <time window, e.g. 0:00-0:04>
spoken: |
  <exact words, verbatim, written for the ear>
visual: <the beat — what the viewer sees during this segment>
on_screen_text: <text overlay, verbatim, or none>
shot_note: <framing, location, prop, or b-roll instruction>

<repeat the Segment block; time windows must sum to target_length>

## CTA
<the single ask — as spoken, and as mirrored on screen>

## Read-through check
read_aloud_pass: <done — what the aloud reading cut or rewrote>
length_check: <segment windows summed vs target_length>
voice_check: <voice rules applied; banned words absent>

## Platform checks
- <spec item>: required <value per official docs> — this script <value> — <pass | fail> — <official doc URL — access date>

## Sources and assumptions
sources:
  - <owner material or URL — access date>
assumptions:
  - <each labeled assumption, or None>
```

Rules:

- `spoken` and `on_screen_text` are verbatim record-and-publish text, written for the ear, not the page.
- Every segment carries all four of `spoken`, `visual`, `on_screen_text`, `shot_note`. "None" is a deliberate value, not an omission.
- Segment time windows sum exactly to `target_length`.
- The read-through check records what actually happened in the aloud pass; it is not a formality box.
- Platform checks are verified at execution time from the platform's official documentation, with URL and access date. Never filled from memory.
- Prices are exact owner-provided numbers. Unsourced claims are removed, not softened. Missing data is `Unavailable`, never zero.

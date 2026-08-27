# Example: completed result handoff

The result returned for task KC-2026-041 (see `kanban-task.md`), following
`templates/handoff-result.md`. In a live run the deliverable path would sit
under the profile's working directory; here it points at the example file in
this repository, `examples/deliverable-email-sequence.md`.

Synthetic example. All businesses, URLs, and numbers are fictional.

```
status: complete
summary: Wrote the full 3-email post-purchase sequence for first-time
  buyers: care-guide primer at day 1, first-cook recipes at day 8, dutch
  oven cross-sell at day 21 with owners excluded. All product claims were
  checked against the store's own pages. The sequence is ready for owner
  review; nothing is loaded into the ESP.
deliverables:
  - examples/deliverable-email-sequence.md (subject, preheader, body, CTA,
    send timing, and exit rule for each of the 3 emails)
sources:
  - Kettle & Crate product page — https://kettleandcrate.example/products/enameled-dutch-oven — accessed 2026-08-26  (price $139, cast iron with enamel coat, lifetime warranty)
  - Kettle & Crate care guide — https://kettleandcrate.example/pages/care-guide — accessed 2026-08-26  (care instructions referenced in email 1)
  - Task brief KC-2026-041 — objective, audience, offer, AOV $85, constraints, approval level
  - local/business-profile.md — voice (warm, plain, practical, no hype), channel setup
confirmed_facts:
  - Dutch oven price is $139 (product page, accessed 2026-08-26; matches the brief)
  - Store AOV is $85 (owner-confirmed in the brief)
  - Sequence trigger is first completed order, US list (brief)
  - No discount codes allowed in this sequence (brief constraint)
assumptions:
  - The ESP can branch email 3 on "order or later purchase included the
    dutch oven." Reasonable because the brief names a Klaviyo-style flow
    tool, where product-based flow filters are standard. Confirm during ESP
    load, before activation.
  - The first-run recipes page exists at the blog URL used in email 2.
    Reasonable because the owner's blog hosts recipe content; confirm the
    exact URL during ESP load and fix the link if it differs.
unknowns:
  - Pre-launch 45-day repeat purchase baseline: Unavailable until Sam pulls
    it from the ESP, per the brief. The success target cannot be set before
    then.
  - Current deliverability baseline (sender reputation, recent spam-rate
    data): Unavailable; no ESP reporting access was provided for this task.
  - Size of the first-time-buyer segment entering the flow: Unavailable.
checks_performed:
  - Price check: $139 appears wherever the dutch oven offer appears, and
    nowhere as a range or rounded figure
  - Claim check: every product claim in the copy traced to the product page
    or care guide; no review counts, ratings, or performance stats used
  - Constraint check: one CTA per email, no discount codes, voice matches
    the profile
  - Exit-rule check: each email has an explicit exit rule; email 3 excludes
    dutch oven owners
  - Link check: every URL in the copy is on the kettleandcrate.example
    domain
approval_still_required:
  - Loading the sequence into the ESP as an inactive flow
  - Activating the flow / sending to live customers (separate
    moment-of-action approval with the full approval-request shape)
residual_risks:
  - Email 3's cross-sell timing (day 21) is a judgment call with no account
    data behind it; if second orders cluster earlier, the pitch may arrive
    late
  - Unknown deliverability baseline means early sends need monitoring
    before the flow is judged
  - If the ESP cannot branch on dutch oven ownership, email 3 would reach
    owners and read as tone-deaf; the load step must verify the filter
next_action: Request approval to load the sequence into the ESP as an
  inactive flow, verifying the email 3 ownership filter and the recipe URL
  during the load. Evidence: sequence is finished and checked; activation
  is a separate approval. Estimated impact: unblocks baseline pull and
  target-setting. Confidence: high that the load is low-risk since the flow
  stays inactive. Effort: about an hour. Owner time: 10 minutes to review
  the loaded flow. Decision needed: approval to load (not activate).
```

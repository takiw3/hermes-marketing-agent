# Example: incoming Kanban task brief

A complete brief as the Chief of Staff assigns it, following
`templates/task-brief.md`. Because every field is answered, the marketing
profile executes it as-is with no questions back to the owner.

Synthetic example. Kettle & Crate, Sam Okafor, and all URLs and numbers are
fictional.

```
task_id: KC-2026-041
objective: Raise the 45-day repeat purchase rate of first-time buyers by
  putting a post-purchase email sequence behind every first order
business_context_reference: local/business-profile.md
audience: first-time purchasers of any product, US email list, entering the
  flow on order confirmation
offer: the sequence sells nothing in emails 1 and 2; email 3 cross-sells the
  enameled dutch oven at $139 to buyers who don't own it. Store AOV is $85,
  so the dutch oven is the step-up purchase.
channel: email, ESP automation flow (Klaviyo-style)
deliverable: 3-email post-purchase sequence, full copy - subject, preheader,
  body, CTA, send timing, and exit rule for each email
deadline: 2026-09-05
constraints: voice per profile (warm, plain, practical, no hype); no discount
  codes in this sequence; no invented reviews, ratings, or stats; one CTA per
  email; exact price where the offer appears
source_material: https://kettleandcrate.example/products/enameled-dutch-oven;
  https://kettleandcrate.example/pages/care-guide; local/business-profile.md
approval_level: draft, then request approval to load into ESP
success_measure: 45-day repeat purchase rate of sequence recipients vs the
  pre-launch baseline; Sam pulls the baseline from the ESP before activation
  and sets the target from it
```

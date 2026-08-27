# Onboarding

Installation does not start onboarding. Onboarding begins on the first direct
conversation with the owner, or on the first delegated task that arrives
without enough context to execute. If the Chief of Staff supplies a complete
brief, the agent executes it — it never forces the owner through a redundant
interview.

## Flow

1. **Check what already exists.** Approved context in user-owned memory and
   `local/business-profile.md` is used first. Answered questions are never
   asked again.
2. **Explain the setup.** One or two sentences: what will be asked, why, and
   that the owner can skip, pause, or hand over documents instead.
3. **Ask one question at a time.** Never a form, never a battery. The owner
   can skip any question, correct earlier answers, pause and resume later,
   or point at an existing document that answers it.
4. **Ask consent before researching.** Looking at the owner's website,
   accounts, connected apps, or private documents happens only after a yes.
5. **Summarize and confirm.** The finished profile is played back to the
   owner and saved only after confirmation.
6. **Store in the right place.** Compact preferences go to the supported
   memory system (with approval before writes). The full marketing context
   goes to `local/business-profile.md` (see
   `templates/business-profile.md`), which distribution updates preserve.

## What gets collected

Only what current or future marketing work needs:

- Business name, website, market, location, and business model
- Offers and exact prices
- Margins or economic constraints when relevant
- Ideal buyer
- Buyer pain, desired result, objections, and buying triggers
- Sales process and funnel
- Differentiation
- Approved proof and claims
- Claims the business must not make
- Brand voice samples
- Current channels and available performance data
- Marketing goals, source metrics, and time window
- Budget and production capacity
- Competitors
- Industry and jurisdiction
- Legal, privacy, consent, endorsement, and disclosure constraints
- Actions the agent may draft, stage, or execute
- Required human approval points

## What never gets collected or stored

Credentials, payment information, private contact lists, raw customer
records, health information, or personal data the work doesn't need. If the
owner pastes any of these, the agent uses what the task requires in the
moment and does not persist it.

## Fact discipline

Everything collected is classified as one of: owner-confirmed facts, directly
observed facts, sourced facts, calculations, inferences, unknowns, or
approval boundaries. The business profile records the classification so later
work knows what it can rely on and what it must still verify. Unknowns stay
unknowns until confirmed — the agent never promotes a guess to a fact.

## Partial onboarding

Onboarding is resumable. The business profile tracks which sections are
confirmed and which are open; the next session picks up at the first open
item without repeating anything. A task that needs only one missing fact asks
for that one fact — it does not restart the interview.

# Deliverable: Kettle & Crate post-purchase sequence (3 emails)

Task KC-2026-041. Draft for owner review; nothing here is loaded into the
ESP or sent. Trigger: first completed order, US list. All three emails leave
the flow immediately if the order is cancelled or refunded, or the contact
unsubscribes.

Synthetic example. Kettle & Crate and every URL in this file are fictional.

---

## Email 1 — the head start

**Send timing:** 1 day after order confirmation
**Exit rule:** skip if the order was cancelled before send time
**Subject:** Your Kettle & Crate order is on the way
**Preheader:** Two minutes of prep now saves your first cook later.

Hi {{first_name}},

Your order is packed and moving. While it travels, here's the head start
most people skip.

Unbox everything the day it arrives. Wash with warm water and a soft
sponge, dry completely, and put it where you'll actually reach for it.
Cookware that lives in the cupboard behind the blender gets used twice a
year. Cookware on the stove gets used twice a week.

Our care guide covers the rest: first wash, heat settings, what never goes
in the dishwasher, and how to fix the small stuff before it becomes big
stuff.

**CTA button:** Read the care guide
Link: https://kettleandcrate.example/pages/care-guide

Cook well,
Sam and the Kettle & Crate team

---

## Email 2 — the first real cook

**Send timing:** 8 days after order confirmation
**Exit rule:** skip if the contact placed a second order since email 1
(they move to the repeat-buyer flow instead)
**Subject:** The first meal decides everything
**Preheader:** Three recipes that make new cookware earn its spot.

Hi {{first_name}},

New cookware has one dangerous week: the one where it sits unused and
becomes furniture. The fix is a first meal that goes well.

We keep three first-run recipes for exactly this: a weeknight sear, a
one-pot pasta, and a Sunday braise. Each one is written for the piece you
just bought, with heat settings and timing included, so the first cook
feels like the tenth.

Pick one and make it this week. If something goes sideways at the stove,
reply to this email and tell us what happened. A real person reads these
and answers.

**CTA button:** See the three first-run recipes
Link: https://kettleandcrate.example/blogs/kitchen-notes/first-run-recipes

Cook well,
Sam and the Kettle & Crate team

---

## Email 3 — the step-up piece

**Send timing:** 21 days after order confirmation
**Exit rule:** skip if the first order included the enameled dutch oven, or
if one was purchased since; those contacts exit the flow here
**Subject:** The pot that ends up in the will
**Preheader:** One piece does the braises, the breads, and the soups.

Hi {{first_name}},

Three weeks in, you know how we build things. So here's the piece our
customers buy second most often, once they've decided the first one earned
their trust.

The enameled dutch oven is $139. It holds heat like cast iron because it
is cast iron, wears an enamel coat so there's no seasoning routine, and
moves from stovetop to oven to table. Braises, no-knead bread, chili for
a crowd, soup all winter. It's the pot that gets handed down, which is why
we put a lifetime warranty on it.

No discount, no countdown. Just the next piece, when you're ready for it.

**CTA button:** See the dutch oven ($139)
Link: https://kettleandcrate.example/products/enameled-dutch-oven

Cook well,
Sam and the Kettle & Crate team

---

## Sequence notes

- One CTA per email, per the brief. Reply-to in email 2 is a conversation
  channel, not a second CTA.
- No discount codes anywhere in the sequence, per the brief.
- No review counts, ratings, or performance stats appear in the copy;
  none have been collected or verified.
- The two product claims in email 3 (cast iron with enamel coat, lifetime
  warranty) were checked against the product page on 2026-08-26; both are
  stated there.

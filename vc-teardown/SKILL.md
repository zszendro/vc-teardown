---
name: vc-teardown
description: Stress-test a business idea as a skeptical VC, then rebuild it into a business plan with a defensible moat, business model, GTM, unit economics and kill criteria. Use this whenever the user describes a startup idea, product concept, app idea, side business, marketplace, portal, platform or "I'm thinking of building X" — however briefly or vaguely they describe it — and especially when they ask to validate it, poke holes in it, challenge assumptions, act as a VC or investor, find the moat, or write a business plan, MVP scope, or go-to-market. Also use when the user wants a second opinion on whether an idea is worth building, or asks what the competition looks like.
license: MIT
metadata:
  version: "1.1.0"
---

# VC Teardown → Moat → Plan

Turn a business idea — described in one line or ten pages — into a plan that survives contact with an investor and with the market.

The core belief: **most ideas fail not because they are bad but because the obvious version of them is already built.** The job is not to validate the user's framing. It is to find what is already true about the market, kill the parts of the idea that lose, and locate the wedge the incumbent structurally will not take.

An honest teardown that saves someone six months is worth more than an enthusiastic plan. But a teardown that only criticises is worthless — **every challenge must produce a change to the plan.**

## Workflow

1. **Intake** — take what they gave you
2. **Research** — find who already built this (non-negotiable)
3. **Teardown** — 8–12 numbered challenges, each with a verdict and a plan change
4. **Find the moat** — the reframe
5. **Build the plan** — model, MVP, GTM, economics, risks, kill criteria
6. **Deliver** — file, with the honest scale verdict stated plainly

---

## 1. Intake

Work with whatever detail level you're given. A one-liner is enough to start; do not stall the user with a questionnaire.

Ask at most **three** questions, and only ones that change the analysis:
- Geography and beachhead (a national plan and a one-city plan are different businesses)
- Ambition frame — bootstrap, or venture-scale? This changes what counts as a good answer.
- Anything the user is already committed to (an existing asset, audience, skill, or partner)

Do **not** ask for detail they can't have yet — TAM estimates, pricing, feature lists. You are going to supply those.

If the idea is genuinely ambiguous about what it does, ask one clarifying question and proceed on a stated assumption rather than waiting.

## 2. Research — do this before writing a single critique

Skipping research produces generic startup advice, which is worthless. Search before you judge. Look for:

- **Direct incumbents.** Name them, their funding, traffic/scale, and any distribution advantage (app store rank, official endorsement, partnership with a governing body or platform).
- **Free substitutes.** Google, spreadsheets, WhatsApp groups, a paper form. Most consumer ideas die here, not against a startup.
- **Adjacent software the buyer already pays for** — the thing that will absorb this as a feature.
- **Evidence the pain is real.** Local news, forum complaints, municipal minutes, review sites, subreddit threads, app-store one-star reviews. Direct evidence of people improvising a workaround is the single strongest signal available — it proves demand *and* proves nobody has served it.
- **Willingness-to-pay evidence.** Reviews of competitors' paid tiers are unusually revealing.

Cite what you find. A teardown grounded in named competitors and quoted complaints is persuasive; one grounded in your priors is not.

## 3. The teardown

Adopt a skeptical VC persona: someone who wants the deal to work but has seen this pattern fail. Direct, specific, unsentimental — not contrarian for sport, and never condescending. Assume the user is capable and wants the truth.

Write **8–12 numbered challenges**. Each one:

```
**C4. [One-sentence claim of what's wrong.]**
[2–4 sentences of specific evidence — named competitor, real number, quoted complaint.]
→ **Change:** [the concrete revision to the plan]
```

The `→ Change` line is what separates this from criticism. If a challenge produces no change, it isn't a real challenge.

Read `references/challenge-library.md` for the standard attack surfaces to work through — competition, monetization, cold start, distribution, buyer incentive, sales cycle, regulatory/liability, founder-market fit, capital efficiency, defensibility, timing, platform dependency, AI-native risk, and capital intensity. Work through them rather than inventing challenges ad hoc; the library exists so nothing structural gets missed.

Close the teardown with a one-line surviving thesis: *"[Original framing] is dead on arrival; [reframed wedge] is a real business because [reason]."*

Two calibration rules:
- **Do not soften a fatal flaw.** If the idea is a feature and not a company, say so in those words.
- **Do not kill a good idea for sport.** If a challenge has a genuinely good answer, say so and move on. Manufactured objections cost you credibility on the real ones.

## 4. Find the moat

This is the highest-value part of the skill and the hardest. Read `references/moat-patterns.md` for the full set of reframes. The recurring moves:

- **Demote the commodity.** The feature that's already free becomes an acquisition asset, never the value proposition.
- **Create the data instead of aggregating it.** If the information the product needs doesn't exist anywhere, that's not a blocker — that's the moat. Whoever generates it owns it.
- **Sell to operational pain, not marketing motive.** "Claim your listing" needs traffic you don't have. "Stop your staff refereeing arguments" needs nothing.
- **Find the incumbent's metric mismatch.** A company optimizing national MAU will not build a low-ARPU, high-touch, per-venue operations tool. That refusal is structural, not an oversight — and it's durable.
- **Prefer granted distribution to won distribution.** An institution telling its users to adopt something beats an SEO race.
- **Hunt for the unserved 80%.** Software usually serves the professionalized minority of a market. The informal majority is bigger, ignored, and reachable.
- **Own the eval set, not the model.** For anything AI, the base model is available to everyone. Knowing exactly what "correct" means in the domain — and holding the labelled corpus of hard cases that proves it — is what competitors can't copy in an afternoon.

State the reframed positioning in one sentence the user could say out loud, then explain in three or four bullets why it's defensible.

## 5. Build the plan

Use the structure in `references/plan-template.md`. It covers: market reality, the teardown, the reframed strategy, stakeholder use cases tiered MVP/v1.1/v2, business model with revenue lines in the order they turn on, unit economics, MVP scope and stack, GTM, metrics, risk register, kill criteria, and open questions.

**Write the full plan: 2,500–4,000 words.** Every section carries its own weight — a plan that lands under 2,000 words has almost certainly dropped the unit economics arithmetic, the risk register, or the build sequence, which are the parts that make it useful. Depth per section matters more than breadth: four sections written properly beat nine sections listed.

`references/example-teardown.md` is a complete pass over one idea — read it when you want the shape and density of the output rather than the rules for producing it. Two cautions. Its market facts are researched and cited, which is the standard to match, but they were current in August 2026 and will age. And **its plan sections are deliberately compressed to about a quarter length** — only section 5 is reproduced fully. Match the density of that section, not the length of the file.

Non-negotiable elements, because they're the ones people leave out:

**Unit economics with real arithmetic.** Show the calculation. If one beachhead produces $18k of revenue, write that number even though it's unimpressive — especially then.

**The honest scale verdict.** State plainly whether this is a lifestyle business, a bootstrap SaaS, or venture-scale. Dressing an SMB SaaS as a venture marketplace fails diligence and wastes the founder's year. Say which one it is and what would have to be true to change it.

**Kill criteria.** Two or three falsifiable conditions with dates, agreed before any money is spent. "No customer will pay anything by month 9 → this is a feature, not a company. Stop."

**The cheapest possible test.** Identify the one experiment that de-risks the biggest assumption, and note that it almost always costs time rather than money. Say explicitly what should *not* be built until it passes.

Tier every use case MVP / v1.1 / v2. An untiered feature list is a wish, not a scope.

## 6. Deliver

Default to a markdown file for plans over ~1,000 words. Keep the conversational reply short and readable — lead with what changed about their idea and why, not a summary of the document. Talk to them like a person who has just spent an afternoon on their problem, not like a report generator handing over output.

If the plan required a pivot, say so in the first two sentences of the reply. Users need to know their framing changed before they open a file that assumes it.

Then flag the one or two things you are least sure about. Naming where the analysis is thin is more useful than projecting confidence across all of it, and it tells them where their own knowledge should override yours.

### Close by offering what comes next

The plan is a starting point, and the user usually wants something built on it. End the reply by offering **three or four specific things**, chosen from what this particular analysis actually surfaced:

- **Go deeper on a specific challenge.** Name the one worth expanding — usually the challenge with the weakest evidence or the biggest consequence.
- **A PDF of the plan**, if it's going to a partner, co-founder or investor.
- **A one-page executive summary** — the verdict, the wedge, the ask, the kill criteria.
- **A pitch-deck outline** built from the reframed positioning.
- **Re-run the unit economics** under different assumptions: their pricing, their penetration estimate, a different beachhead.
- **A teardown of the reframe itself**, attacked as hard as the original idea. Worth offering when the reframe is doing a lot of load-bearing work.
- **The cheapest test, specified properly** — who to call, what to ask, what result would kill it.

Two rules for the close:

**Be specific, not generic.** "Let me know if you want anything else" is worthless. "Want me to expand C7 — the willingness-to-pay problem is the weakest part of this and probably decides it" gives them something to say yes to.

**Deliver first, always.** Offers come after the plan exists, never instead of it. Never end a teardown with a question in place of the work, and never withhold a section pending an answer. If something genuinely needs their input, state the assumption you used, deliver on it, and note that the answer would change it.

## Tone

The user brought you an idea they may have been thinking about for months. Respect that by being useful rather than gentle — but the goal is a better business, not a demonstration of your skepticism. Praise what genuinely works. Be specific about what doesn't. Always leave them with something to build.

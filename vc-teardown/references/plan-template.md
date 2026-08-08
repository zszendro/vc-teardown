# Plan Template

Structure for the deliverable. Adapt section depth to the idea; keep the order — it walks the reader from "what's true" through "why the obvious version fails" to "what to build."

Aim for 2,500–4,000 words. Longer stops being read; shorter can't carry unit economics and a risk register.

Treat that range as a sanity check, not a target to iterate against. Write each section at the depth it needs and let the total land where it lands. **Do not rewrite a finished plan to bring it inside the range** — compression passes cost the reader nothing and cost you time, and the first thing they strip is usually the arithmetic. Running long is much better than running thin.

Note that `example-teardown.md` compresses its plan sections to roughly a quarter length to keep the file small — only its section 5 shows full depth. Match that section's density across all of these, not the example's overall length.

---

## 0. Executive summary and verdict

Open with the verdict, not a description of the idea. If the original framing doesn't survive, say so in the first two sentences, then immediately give the reframe so the reader isn't left with only a demolition.

Include the single most important next action and — where one exists — the one-sentence kill criterion.

## 1. Market reality

Size, with a source and a date. Growth direction, not just magnitude.

**Where the activity actually happens** — a segmentation table is usually the most valuable thing in this section, because the asymmetry between where the money is and where the pain is often *is* the strategy.

**The competitive map.** Name incumbents with funding, scale, and distribution advantages. Include free substitutes. Include adjacent software the buyer already pays for. State plainly which competitors are beatable, in which segment, and which are not.

**Evidence the pain is real** — quoted complaints, documented workarounds, municipal or industry records.

## 2. Teardown

8–12 numbered challenges. Format:

```
**C1. [Claim of what's wrong.]**
[Specific evidence — named competitor, real number, quoted complaint.]
→ **Change:** [concrete revision to the plan]
```

Close with the surviving thesis in one line.

## 3. Revised strategy — the wedge

**Positioning:** one sentence the user could say out loud.

**The product in layers** — typically a wedge layer (the paid thing that solves the operational pain), a retention layer (free, sticky, generates the data), and an acquisition layer (free, SEO, commodity). Say which is which and why.

**Why it's defensible** — three or four bullets, each naming a specific mechanism, sequenced by when it starts holding.

**International or adjacent extension** — what to design for now versus build later. Schema decisions made cheaply at the start; features deferred.

## 4. Stakeholders and use cases

One subsection per stakeholder. Tier every item **[MVP] / [v1.1] / [v2]**.

An untiered list is a wish list. Tiering forces the scope argument to happen on paper instead of in month four.

Include the platform/admin stakeholder — moderation, verification and dispute handling are always underestimated.

## 5. Business model

Revenue lines in a table, ordered by **when they turn on**, not by size:

| # | Line | Who pays | Price | When |

State explicitly which lines are *not* launch revenue and why.

**Unit economics** — show the arithmetic:
- Beachhead penetration assumptions, stated as assumptions
- Revenue per beachhead at maturity
- CAC and how it falls with density
- LTV, retention assumption, gross margin
- The honest read: what kind of business this is

**The honest scale verdict**, in plain words. Lifestyle, bootstrap SaaS, or venture-scale — and what would have to be true to move up a category.

**What we are explicitly not doing.** A short list. Prevents scope creep and shows the abandoned ideas were considered rather than overlooked.

## 6. MVP scope and technical plan

**In scope** — numbered, narrow, and defensible as the minimum that tests the core assumption.

**Out of scope** — equally explicit, with one-line reasons.

**Stack** — concrete choices with brief rationale, favouring what the user already knows. Flag the one or two technical decisions that are genuinely hard to reverse (usually the data model and anything geo, realtime, or multi-tenant).

**Core data model** — abbreviated schema. Call out the design decisions that make later extension additive rather than a migration.

**Build sequence** — a week-by-week table. Put the riskiest thing early enough to fail cheaply, and start anything with a long lead time (SEO indexing, app review, compliance) in week one.

## 7. Go to market

**Beachhead selection** — weighted criteria, then the honest note that the criterion about who the user actually knows there usually outranks the analytical ones.

**The core motion** — numbered steps, concretely. This is the section founders skip and then fail on.

**Acquisition channels ranked by honest expected value.** Include the ones that won't work, and say why, so they don't get retried.

**Retention mechanics** — the weekly reason to come back.

**A phase table** for the first 12–18 months with a success metric per phase.

## 8. Metrics, risks, kill criteria

**North star** — one metric, and it should be an activity metric rather than a signup metric.

**Supporting metrics** — five or six.

**Risk register** — table of risk, severity, mitigation. Include founder bandwidth and liability; both are consistently underestimated.

**Kill criteria** — two or three, falsifiable, with dates, framed as agreed before spending starts.

## 9. Open questions

Five or six genuine ones, ordered by how much they change the plan. These are for the user to answer, not rhetorical. Good ones surface unstated assumptions: who's the operator, what's the ambition frame, how much time exists alongside everything else.

## Appendix — original idea, mapped

A table: each element of the user's original framing, the verdict on it, and where it landed in the new plan.

This matters more than it looks. It shows every part of their thinking was considered, makes the pivot legible rather than arbitrary, and gives them a way to argue back on any specific item rather than rejecting the whole plan.

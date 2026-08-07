# Worked Example

A complete pass over one idea, to show the shape of the output. The teardown is
reproduced in full because that section is the distinctive one; the plan sections are
abridged to their skeleton — see `plan-template.md` for what each expands to at full
length.

> **The competitor names, funding figures and quoted complaints below are illustrative,
> invented to demonstrate the format.** A real run must replace every one of them with
> researched facts. An example that taught you to fabricate a `$4M Series A` would be
> worse than no example at all — the entire value of a teardown is that its numbers are
> real. Read this for structure and tone, never for market data.

**The brief:** *"An AI tool that drafts municipal permit applications. I'm a contractor,
I've filed hundreds of these, they're miserable. Bootstrapping, based in Denver."*

---

## 1. Market reality — abridged

Residential construction permits in the US run into the millions annually, filed across
roughly 20,000 separate jurisdictions, each with its own forms, codes and submission
portal. That fragmentation is the whole story: it's why no dominant tool exists, and it's
why building one is hard.

**Where the activity is.** The market splits three ways, and they are different
businesses. Large general contractors have permit expediters on staff or on retainer.
Mid-size firms — 10 to 50 employees — have an office manager doing it badly between other
duties. Solo contractors and small crews do it themselves at night. The pain is worst at
the bottom, the budget is at the top, and the middle is where those two curves cross.

**Competitive map.** *[Illustrative]* Two funded startups sell permit-management software
to enterprise builders and municipalities. Neither drafts applications; both are workflow
and status-tracking layers. Several regional expediter firms do this as a service at
$300–800 per permit. The real substitute is the incumbent behaviour: a folder of last
year's applications, copy-pasted and edited.

**Evidence the pain is real.** Contractor forums are full of rejection-and-resubmit
complaints, and the recurring theme is not that the form is hard but that the *rejection
reason* is opaque and the resubmission clock is expensive. That distinction turns out to
be the whole strategy.

---

## 2. Teardown

**C1. "Drafting the form" is the cheap part of the problem.**
The forms are mostly transcription — address, scope, valuation, contractor licence
number. An experienced contractor fills one in twenty minutes. The expensive part is the
rejection: two weeks lost, a resubmission, and a crew standing idle. A tool that saves
twenty minutes of typing is selling into the wrong cost.
→ **Change:** reposition from drafting to rejection avoidance. The unit of value is a
permit approved first time, not a form filled faster.

**C2. The base model will absorb generic form-filling within the plan's timeline.**
Challenge 19. "Upload a PDF, extract fields, generate a draft" is a general capability
that improves for free and gets cheaper every quarter. Any product whose value claim is
that sentence has nothing left when the buyer's existing software ships it.
→ **Change:** move the value claim to what surrounds the generation — the
jurisdiction-specific rules, the rejection history, the accountability for being wrong.
Assume the drafting itself is free by year two and make sure the plan survives that.

**C3. The data required does not exist in any aggregated form.**
Twenty thousand jurisdictions, no standard schema, no API for most, and code amendments
that land locally with no central feed. There is no dataset to license.
→ **Change:** this reads fatal and is the best news in the analysis — see the reframe.
Stop planning to aggregate; plan to generate.

**C4. Nationwide coverage is a cold-start trap.**
Challenge 5. Coverage is the buying criterion — a contractor whose city is missing churns
permanently and won't return. Launching thin across fifty metros means every user's first
experience is a gap.
→ **Change:** Denver metro only, roughly a dozen jurisdictions, to genuine depth. Do not
open signups outside it until first-time approval rate is provably better than baseline.

**C5. Solo contractors are the wrong first customer.**
They feel the most pain and have the least budget, no purchasing habit for software, and
they churn seasonally with the build cycle. Consumer-grade price points can't fund
jurisdiction research.
→ **Change:** sell to the 10–50 employee firms where an office manager files 5–20 permits
a month. Real budget, an existing line item for expediter fees to displace, and a
comparison that flatters the product.

**C6. The expediters are the actual incumbent, and they're a benchmark not a rival.**
At $300–800 per permit, an outside service already solves this for anyone willing to pay.
That's the price anchor — and it's high enough that a software product looks cheap
against it.
→ **Change:** price against the expediter invoice, not against SaaS seat comparables.
Explicitly target the firms for whom expediters are too expensive per-permit but the
office manager is too slow.

**C7. Liability is unpriced in the plan.**
Challenge 10. If the tool asserts a filing is compliant and it isn't, the contractor eats
the delay and possibly a failed inspection. "Our AI said so" is not a defence a small firm
can absorb, and it's the first question a serious buyer asks.
→ **Change:** the product advises, never certifies. Every output carries its source
citation to the specific code section. Terms cap liability, and the roadmap includes a
reviewed tier where a human licensed reviewer signs off for a fee — which is a revenue
line, not just a disclaimer.

**C8. Municipal relationships are slow and can't be on the critical path.**
Challenge 8. Selling to cities means procurement, 6–18 month cycles and RFPs. A
bootstrapped plan dies waiting.
→ **Change:** cities are not a customer in the first two years. Any municipal
relationship is opportunistic and free. Revenue comes from contractors only.

**C9. Founder-market fit is real on domain, absent on distribution.**
Challenge 11. Having filed hundreds of permits is genuine credibility and the reason to
believe the rejection insight. But knowing the work is not the same as reaching 200 firms
in Denver, and there's no stated distribution asset.
→ **Change:** make the go-to-market a named, sequenced motion built on the founder's
actual network — the supply houses, the trade associations, the inspectors — rather than
an assumed one. If that network doesn't exist, recruiting someone who has it is a
precondition, not a nice-to-have.

**C10. Retention is weak if permits are episodic.**
Challenge 15. A contractor filing four permits a year has no reason to keep a
subscription open between them.
→ **Change:** target the segment with monthly filing volume, and build the retention
layer around what happens *between* permits — inspection scheduling, code-change alerts
for their jurisdictions, and the archive of their own filing history.

**C11. Honest scale check.**
Challenge 16. Assume 200 target firms in Denver metro, 25% penetration at maturity,
$250/month. That is 50 customers and $150k of annual revenue from a fully-penetrated
beachhead. Ten metros at the same penetration is $1.5M.
→ **Change:** this is a bootstrap SaaS, not a venture business, and the plan should say so
in those words. What would change it: the data asset in the reframe below becoming
sellable to insurers or code-publishers, which is a year-three question and not
underwritable now.

**Surviving thesis:** *An AI permit drafter is dead on arrival — the drafting is
commoditising and the pain isn't there. A jurisdiction-specific first-time-approval
engine, owned by whoever accumulates the rejection corpus, is a real business, because
that corpus exists nowhere and can only be built by watching outcomes.*

---

## 3. The reframe

**Positioning:** *"We get your permit approved the first time, in the jurisdictions you
actually build in."*

**The product in layers.**
- **Wedge (paid):** pre-submission review against the specific jurisdiction's rules and
  the known rejection patterns. This is what firms pay for.
- **Retention (free, generates the data):** filing archive, submission tracking,
  inspection scheduling and code-change alerts. Cheap to run, and it captures outcomes.
- **Acquisition (free, SEO):** per-jurisdiction requirement pages. Commodity content, and
  the thing every contractor searches for at 11pm.

**Why it's defensible.** Pattern 2 does the heavy lifting: nobody holds a corpus of
*what got rejected and why*, because it exists only in scattered emails between
contractors and plan reviewers. The product that sits in the submission path sees those
outcomes and nobody else does. Pattern 10 compounds it — every rejection becomes a
labelled hard case, and the eval set of "would this have been approved?" is what makes
the advice trustworthy and safe to improve. Pattern 4 explains why the funded incumbents
won't follow: both sell seats to enterprise builders and municipalities, and a
per-jurisdiction, high-touch, low-ARPU product is beneath their metric.

**What we are explicitly not doing:** national coverage, selling to cities, drafting as
the headline feature, or anything touching plan review or structural calculations.

---

## 4–8. Plan skeleton — abridged

**Stakeholders and use cases.** Office manager `[MVP]` — pre-submission check, filing
archive. Owner `[MVP]` — approval-rate dashboard. Field crew `[v1.1]` — inspection
status. Licensed reviewer `[v2]` — the human sign-off tier. Platform/admin `[MVP]` —
jurisdiction rule maintenance, which is the real operating cost and is consistently
underestimated.

**Business model.** Ordered by when each turns on:

| # | Line | Who pays | Price | When |
|---|---|---|---|---|
| 1 | Firm subscription | 10–50 employee contractors | $250/mo | Launch |
| 2 | Reviewed filings | Same, per permit | $75 | Month 9 |
| 3 | Rejection-pattern data | Insurers, code publishers | TBD | Year 3+, not underwritten |

**Unit economics.** 50 customers × $250 × 12 = $150k per mature beachhead. CAC is high
initially — this is a walked-in, trade-association sale — and falls with local density and
word of mouth, which is the argument for depth over breadth. Gross margin is good but not
software-good: jurisdiction rule maintenance is ongoing human work.

**Honest scale verdict: bootstrap SaaS.** A good one, and a bad venture pitch.

**MVP scope.** In: three Denver-area jurisdictions, pre-submission check against a
hand-built rule set, citation to code section, filing archive. Out: drafting from scratch,
e-filing integration, mobile, anything outside the three jurisdictions. **The riskiest
assumption** — that a rule set plus rejection history measurably improves first-time
approval — should be tested manually, by hand, on real applications, before any product
is built.

**Go to market.** Denver metro. The motion is: 20 firms hand-recruited through supply
houses and the local builders' association, run their next filings manually, publish the
approval-rate delta, then sell that number. Channels ranked honestly — trade association
and word of mouth first, SEO a year-two asset, paid acquisition never at this ACV.

**Metrics and kill criteria.** North star: permits submitted through the product per week.
Kill criteria, agreed before spending: *no measurable first-time-approval improvement
across 30 manual filings by month 6 → the rejection thesis is wrong, stop.* And: *fewer
than 10 paying firms by month 12 → the segment won't buy software for this, stop.*

---

## Appendix — original idea, mapped

| Original element | Verdict | Where it landed |
|---|---|---|
| AI drafts the application | Cut as headline | Demoted to a supporting feature; commoditising per C2 |
| Municipal permits | Kept | Narrowed to residential construction, Denver metro |
| Contractor as user | Kept, resegmented | Moved from solo to 10–50 employee firms per C5 |
| Nationwide | Cut | One metro until approval-rate lift is proven per C4 |
| Bootstrapping | Kept, and it drove the plan | Ruled out municipal sales and paid acquisition |
| Founder's filing experience | Kept as the core asset | Source of the rejection insight; distribution gap flagged per C9 |

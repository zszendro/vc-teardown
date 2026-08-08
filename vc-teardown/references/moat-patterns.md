# Moat Patterns

The teardown clears ground. This is what gets built on it.

The reframe is the hardest and most valuable move in the whole process, because it has to preserve what the user actually cares about while discarding the version of it that loses. Most of the time the user's instinct about the *market* is right and their instinct about the *product* is wrong.

---

## Pattern 1 — Demote the commodity

**When:** the headline feature is already free, funded, and everywhere.

Don't abandon it. Demote it. The commodity layer becomes an acquisition and SEO asset — worth building, never worth pitching. The value proposition moves to something adjacent that nobody serves.

*Example:* a court directory competing with a million-visitor incumbent becomes an SEO surface underneath a court queue product that no one has built.

**Test:** if the user's one-line pitch still names the commodity feature, the reframe hasn't landed.

---

## Pattern 2 — Generate the data, don't aggregate it

**When:** research shows the data the product needs doesn't exist anywhere.

This reads as a fatal blocker and is usually the best news in the analysis. Aggregated data is commodity — anyone can scrape it, and the source can cut you off. Data that exists only because your product created it cannot be scraped, licensed, or bought.

The product stops being a window onto information and becomes the instrument that produces it. Everything downstream — discovery, benchmarking, reporting, pricing intelligence — then runs on inputs no competitor can obtain.

*Example:* real-time court availability doesn't exist for public courts. Aggregating it is impossible; creating it via an on-court queue makes you the only holder of wait-time and utilization data anywhere.

**Test:** could a well-funded competitor obtain this data next quarter by any means other than replicating your ground operation?

---

## Pattern 3 — Sell operational relief, not marketing exposure

**When:** the supply-side hook is "claim your listing" or "get discovered."

Exposure-based pitches require traffic the product doesn't yet have — a chicken-and-egg that stalls every early supply conversation. Operational pitches require nothing but the pain already present.

Ask what this person does manually today, badly, that annoys them. Sell the removal of that. Marketing value becomes a later upsell once traffic exists.

*Example:* "claim your venue listing" (no traffic, no interest) → "stop your staff refereeing court arguments" (immediate, concrete, already painful).

---

## Pattern 4 — The incumbent's metric mismatch

**When:** a larger competitor could technically build what you're building.

The durable question isn't whether they *can* but whether their business model *lets* them. Look for structural refusals:

- A company optimizing national MAU won't build a low-ARPU, high-touch, per-account operations product — it's beneath their metric
- A company monetizing ads won't build the thing that reduces sessions
- A company selling to enterprise won't serve the informal long tail — the support cost destroys their margin structure
- A platform won't cannibalize its own take rate

These refusals are durable in a way that feature gaps are not. A feature gap closes in a quarter; a business-model conflict lasts years.

**Test:** name the specific internal metric or margin structure that makes this unattractive to them. If you can't, this isn't a moat.

---

## Pattern 5 — Granted distribution beats won distribution

**When:** the plan depends on SEO, ads, or viral growth against an entrenched player.

Find the institution that already has authority over the target users — an employer, venue, school, association, HOA, franchise, professional body, or platform. When they tell their users to adopt something, adoption is near-total and costs nothing.

This usually inverts the go-to-market: sell to the institution, acquire users free as a consequence. It also tends to fix monetization, since institutions have budgets and consumers don't.

---

## Pattern 6 — The unserved 80%

**When:** existing software serves the professionalized top of a market.

Most categories have well-built tools for the staffed, formal, high-revenue minority, and nothing at all for the informal majority — which is larger, less competitive, and often reachable at lower cost.

Serving them usually requires a genuinely different product (self-serve, no admin, no training, no procurement), which is exactly why the incumbent hasn't done it.

*Example:* club-management software exists for staffed private clubs; the parks, community centres and HOAs where most play happens have nothing, and no vendor will sell to a four-court park with no staff.

---

## Pattern 7 — Institutional switching cost

**When:** you need retention in a market with low individual switching cost.

Individual users churn freely. Communities and organizations do not. Once a group's rules, schedule, history and social norms live in a system, switching stops being a download decision and becomes a political event nobody wants to initiate.

Design for this deliberately: make the product hold shared state — rules, rosters, history, standings — rather than individual preferences.

---

## Pattern 8 — Vertical depth over horizontal reach

**When:** the idea is a general-purpose tool in a category with big horizontal players.

Go narrow enough that the workflow, vocabulary, integrations and compliance are specific to one trade. Horizontal players can't follow without breaking their generality, and the vertical version wins on fit even at a higher price.

---

## Pattern 9 — Embedded distribution

**When:** the plan requires people to adopt a new destination — another tab, another login, another tool to remember.

Every new destination competes with the user's existing habit and loses most of the time. The alternative is to put the product inside the surface where the work already happens: the spreadsheet, the inbox, the CRM, the IDE, the messaging tool, the system of record the team already opens every morning.

This trades reach for retention, deliberately. You inherit the host's usage frequency instead of manufacturing your own, and the product stops being something people have to remember to use. It also inverts the churn question — leaving means removing something from a workflow rather than declining to open an app.

*Example:* a reporting tool nobody logs into becomes a scheduled digest in the channel where the team already argues about the numbers.

**Test:** if the host surface vanished tomorrow, would users seek this out directly? If yes, this is genuine embedded distribution. If no, re-read challenge 18 — you've bought retention with dependency, and the plan needs to say how it earns a direct relationship later.

---

## Pattern 10 — Proprietary model or eval set

**When:** the product is AI and the base model is one your competitor can call with the same API key.

The weights are not the moat. The two things that can be owned are a fine-tune or retrieval corpus built on data nobody else holds — which is Pattern 2 wearing different clothes — and, more overlooked, **the eval set.**

Knowing precisely what "correct" means in a domain, with a labelled corpus of the hard and ambiguous cases, is what lets a team ship model changes without breaking customers. It compounds: every production failure becomes a test case, and the set gets harder to replicate the longer the product runs. Competitors can copy the prompt in an afternoon; they cannot copy three years of knowing which outputs were wrong and why.

This is also the honest answer to accuracy economics. A team that can measure quality can safely automate the review step; one that can't must keep a human on every output, and that shows up in the margin.

**Test:** could a competent team match your output quality next quarter using the same base model and a week of prompt iteration? If yes, name whether the data or the evals is the moat — and if neither, there isn't one.

---

## Pattern 11 — Regulatory or license position

**When:** the category has a gate — a licence, certification, accreditation, audit, or approval that takes real time to clear.

Founders treat the gate as a cost. It is also the wall. Anything that takes eighteen months, a lawyer, and an audit to obtain is by definition something a fast follower cannot obtain quickly, and unlike a feature gap it does not close with engineering effort.

The move is to clear the gate early and deliberately, then make it part of the product's value rather than a compliance line item — the buyer who needs the certification can only buy from the small set who hold it. In regulated buying, "we're the ones who can actually sign this" often beats a better product.

The caution: this is only a moat if the gate is genuinely hard and genuinely required. A voluntary badge anyone can buy is not a wall, and a gate that a well-funded competitor clears in a quarter just delays them.

*Example:* the SOC 2 report, the state licence, or the payer contract that turns an eighteen-month enterprise sales cycle into a shortlist of three vendors.

**Test:** name the specific credential, the time and cost to obtain it, and who is disqualified without it. If you can't name who it excludes, it isn't a moat.

---

## Pattern 12 — Sequence the moat

Moats are rarely present at launch; they accrue. State explicitly which mechanism holds at each stage:

- **Launch:** speed, founder attention, hand-built relationships — real but temporary
- **Year 1:** local density and switching cost
- **Year 2:** proprietary data compounding into product advantage
- **Year 3:** brand, distribution partnerships, category default

A plan claiming a year-three moat at launch is not credible. A plan with no path from stage one to stage three isn't either.

---

## Writing the reframe

Deliver it as one sentence the user could say to a stranger, then three or four bullets on why it holds.

> **The operating layer for crowded courts.** Venues run fair, level-appropriate play with zero staff overhead; players know when they'll get on court and who they're playing.

What makes that sentence work: it names the buyer, the pain, and the outcome, and it contains no feature that anyone else already gives away free.

Then say what the plan is *not* doing — explicitly listing the abandoned ideas prevents them creeping back into scope, and it shows the user their original thinking was heard rather than ignored.

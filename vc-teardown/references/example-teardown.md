# Worked Example

A real pass over one idea, to show the shape of the output. The teardown is reproduced in
full because that section is the distinctive one; the plan sections are abridged to their
skeleton — see `plan-template.md` for what each expands to at full length.

> **The market facts below are researched and sourced, not illustrative.** They were
> current as of August 2026 and will age — funding rounds, review times and competitive
> positions all move. Re-verify before relying on any of them. What should generalise is
> the method: every challenge names a real company, a real number, or a real quoted
> complaint, and every challenge ends in a change. Where the plan needs a figure that
> can't be sourced, it is labelled an assumption rather than dressed up as a finding.

**The brief:** *"An AI tool that drafts municipal building permit applications. I'm a
contractor, I've filed hundreds of these, they're miserable. Bootstrapping, based in
Denver."*

---

## 1. Market reality — abridged

Permitting is fragmented across roughly **20,000 jurisdictions** nationwide, each with its
own forms, codes and portal.[^shovels] That fragmentation is why no single tool dominates
the contractor side — and why building one is expensive.

**The competitive map is not empty. It is well funded.**

| Company | Raised | Position |
|---|---|---|
| PermitFlow | $31M Series A (Kleiner Perkins, 2024) + $54M Series B (Accel, 2025)[^pf-a][^pf-b] | Prepares, files and tracks permit applications. TechCrunch called it *"the TurboTax for construction permitting."*[^tc] |
| GreenLite | $28.5M Series A (Craft Ventures, 2024) + $49.5M Series B (Insight Partners, 2025)[^gl-a][^gl-b] | Privatised plan review, selling to authorities having jurisdiction |
| Pulley | $4.4M seed (Susa Ventures, 2022)[^pulley] | Permitting workflow; angels include Procore's CEO |
| Shovels.ai | $6.5M total (Base10 seed, 2025)[^shovels] | 170M+ permit records aggregated from 1,800+ jurisdictions |

On the government side, **Accela** (~2,200 agencies, averaging $382K per permitting
deal), **Tyler Technologies** and **OpenGov** together serve 5,000+ agencies in a market
valued at $2.2B in 2025.[^mkt] Austin, Phoenix and Denver have all awarded multi-year
digitisation contracts to these vendors.[^mkt]

**Evidence the pain is real — and that it is receding in the beachhead.** Denver's
Auditor published a 62-page audit in January 2024 finding that reviewers **missed on-time
completion 76% of the time in 2022, rising to 81% by April 2023**.[^audit] More than half
of surveyed homeowners and contractors said long review times made the process
harder.[^audit] But by 2024 residential plan review for single-family and duplex projects
was averaging **2–4 weeks, down from 12–15 weeks in autumn 2022**.[^sdb]

The most useful finding in the audit is not the delay. It is the **inconsistency**: 11 of
55 respondents complained about contradictory review comments, one saying approval
*"depended more on the reviewer they were assigned than on the project itself."*[^audit]

---

## 2. Teardown

**C1. The idea as stated is PermitFlow's core product, and PermitFlow has ~$85M.**
Challenge 1. "AI drafts permit applications" is not an unserved gap — it is a funded
category with a press narrative already attached. PermitFlow raised $31M in 2024 and $54M
in 2025.[^pf-a][^pf-b] Head-on, at the same feature, against that balance sheet, with no
capital, is not a plan.
→ **Change:** stop competing on drafting. The only viable entry is a segment or a data
asset these companies structurally won't pursue. Everything below is the search for one.

**C2. "Why now?" has a bad answer in Denver specifically.**
Challenge 17. The founder's pain is real but it is dated. Denver residential review has
gone from 12–15 weeks to 2–4 weeks.[^sdb] The crisis that motivated the idea has largely
been fixed by the city itself, and a plan whose value proposition is "permits take
forever" is selling against a problem the beachhead just solved.
→ **Change:** re-anchor the value proposition on what did *not* improve — the
inconsistency and the resubmission cycle, which the audit documents directly[^audit] —
and stop pitching speed.

**C3. Drafting is the cheap part; the correction letter is the expensive part.**
Industry sources are consistent that the most common cause of rejection is missing or
incomplete documentation rather than a design flaw.[^reject] The costly event is the
**correction letter** and the resubmission it triggers. One Denver project accrued over
$24,000 in extra rent and mortgage carrying costs from delay.[^audit]
→ **Change:** reposition from drafting to first-time approval. The unit of value is a
permit that clears review without a correction letter.

**C4. The base model absorbs generic form-filling within the plan's horizon.**
Challenge 19. "Extract fields from a PDF and generate a draft" is a general capability
that improves for free and gets cheaper each quarter. Any product whose value claim is
that sentence has nothing left when the buyer's existing software ships it.
→ **Change:** assume drafting is free by year two. Move the value to the
jurisdiction-specific rules, the correction history, and accountability for being wrong.

**C5. Procore distribution is already taken.**
Challenge 18. PermitFlow has shipped an embedded app on Procore's marketplace since
2022.[^pf-procore] The obvious integration path into the contractor's existing system of
record is occupied by the best-funded competitor, and Pulley's angel list includes
Procore's CEO.[^pulley]
→ **Change:** do not plan on Procore. That also implies not targeting the enterprise
builders who live in Procore — which points the same direction as C6.

**C6. The funded players sell to developers and agencies, not to small contractors.**
Challenge 13 and moat pattern 4. GreenLite sells privatised review to
jurisdictions;[^gl-a] PermitFlow's enterprise motion runs through Procore.[^pf-procore]
Neither can profitably serve a three-person remodelling crew: the support cost per dollar
of revenue is wrong for their margin structure. This is the first genuine opening in the
analysis, and it is a real one.
→ **Change:** target small residential contractors and remodellers — the unserved
majority — explicitly, and design for zero onboarding, no training and no procurement.

**C7. Willingness to pay has a real anchor, and it is lower than it looks.**
Challenge 4. Expediters charge roughly **$500–$2,500** for residential work, with minor
permits at $200–$400 and major remodels at $500–$1,000; hourly rates run
$75–$200.[^exp] That sets a credible ceiling. But the honest read is that most small
contractors *don't* hire expediters — they self-file at night, which means the real
competitor is unpaid founder labour, not an invoice.
→ **Change:** price against the resubmission cost, not the expediter invoice, and expect
the first objection to be "I already do this myself for free."

**C8. The data moat as originally imagined does not exist. A narrower one might.**
Challenge 9. "Nobody has the data" is false: Shovels.ai has aggregated **170M+ permit
records from 1,800+ jurisdictions**.[^shovels] Issued-permit records are public and
already commoditised. What does *not* appear to be aggregated anywhere is the **correction
letter** — the reviewer's comment list, which is correspondence rather than public record.
Some cities publish review datasets (Kansas City does[^kc]), so this must be verified
jurisdiction by jurisdiction rather than assumed.
→ **Change:** the asset is the corpus of correction letters and their resolutions, not
permit records. Instrument for capturing them from day one, and verify the assumption in
Denver before building anything.

**C9. Liability is unpriced.**
Challenge 10. If the tool asserts a submission is compliant and it isn't, the contractor
absorbs the delay and possibly a failed inspection. "The AI said so" is not a defence a
small firm can carry, and it is the first question a serious buyer asks.
→ **Change:** advise, never certify. Cite the specific code section behind every flag.
Cap liability in terms, and treat a human-reviewed tier as a later revenue line rather
than a disclaimer.

**C10. Selling to Denver the city cannot be on the critical path.**
Challenge 8. Municipal procurement runs in quarters, and Accela-class deals average
$382K[^mkt] — a scale and cycle a bootstrapper cannot wait out. GreenLite raised $78M
specifically to play that game.[^gl-a][^gl-b]
→ **Change:** the city is not a customer in the first two years. Any municipal
relationship is opportunistic and free.

**C11. Founder-market fit is strong on domain and absent on distribution.**
Challenge 11. Having filed hundreds of permits is genuine credibility and the reason to
believe the correction-letter thesis. It is not a channel to 200 firms in Denver, and no
distribution asset was stated.
→ **Change:** name the specific route — supply houses, the local builders' association,
inspectors — or make recruiting someone who has it an explicit precondition.

**C12. Honest scale, with the arithmetic.**
Challenge 16. *Assumption, not a finding:* ~200 addressable small residential firms in
Denver metro, 25% penetration at maturity, $250/month. That is 50 customers and
**$150,000 of annual revenue** from a fully-penetrated beachhead. Ten comparable metros at
the same penetration is $1.5M.
→ **Change:** state plainly that this is a bootstrap SaaS, not a venture business, and
that the funded competitors are playing a different game rather than the same one badly.

**Surviving thesis:** *An AI permit drafter is dead on arrival — PermitFlow has $85M and
Procore distribution for exactly that, drafting is commoditising, and Denver just fixed
the delay that motivated the idea. What survives is narrower: a first-time-approval tool
for the small residential contractors nobody funded can afford to serve, owned by whoever
accumulates the correction-letter corpus — which is correspondence, not public record, and
is the one asset Shovels' 170M permits don't contain.*

---

## 3. The reframe

**Positioning:** *"We get your permit through review without a correction letter, in the
handful of jurisdictions you actually build in."*

**The product in layers.**
- **Wedge (paid):** pre-submission check against the jurisdiction's rules and its known
  correction patterns, citing the code section behind each flag.
- **Retention (free, generates the data):** submission tracking and the contractor's own
  correction-letter archive — cheap to run, and it captures the outcomes.
- **Acquisition (free, SEO):** per-jurisdiction requirement pages.

**Why it's defensible.** Pattern 6 carries the near term: PermitFlow and GreenLite have
raised $85M and $78M against developers and agencies respectively, and the support economics
of a three-person crew are wrong for both. Pattern 2 and pattern 10 carry the long term —
correction letters are correspondence, not public record, so they sit outside what Shovels
aggregates, and each one is a labelled hard case for an eval set of *"would this have
cleared review?"* Pattern 9 is honest about sequencing: at launch the moat is founder
credibility only, which is real but temporary.

**What we are explicitly not doing:** national coverage, selling to the city, drafting as
the headline, Procore integration, or anything touching structural calculations.

---

## 4–8. Plan skeleton — abridged

**Stakeholders.** Owner-operator `[MVP]` — pre-submission check, correction archive.
Office manager `[MVP]` — submission tracking. Field crew `[v1.1]` — inspection status.
Licensed reviewer `[v2]` — human-signoff tier. Platform/admin `[MVP]` — per-jurisdiction
rule maintenance, which is the real recurring cost and is always underestimated.

**Business model.** Ordered by when each line turns on:

| # | Line | Who pays | Price | When |
|---|---|---|---|---|
| 1 | Firm subscription | Small residential contractors | $250/mo | Launch |
| 2 | Reviewed submissions | Same, per permit | $150 | Month 9 |
| 3 | Correction-pattern data | Insurers, design firms, jurisdictions | TBD | Year 3+, not underwritten |

**Unit economics.** 50 × $250 × 12 = **$150k** per mature beachhead (penetration assumed,
not measured). CAC is high and human early — this is a walked-in, association-and-supply-house
sale — and falls with local density. Gross margin is good but not software-good, because
rule maintenance is ongoing human work.

**Honest scale verdict: bootstrap SaaS.** A decent one. A bad venture pitch, and a worse
one to make in a category where the funded players raised nine figures between them.

**MVP scope.** In: three Denver-area jurisdictions, pre-submission check against a
hand-built rule set, code-section citations, correction archive. Out: drafting from
scratch, e-filing, mobile, anything beyond those three jurisdictions.

**The cheapest test, and it costs time not money:** collect 30 real correction letters from
Denver contractors and check by hand whether a rule set plus prior corrections would have
predicted them. **Build nothing until that passes.** This also settles C8 — if the letters
turn out to be routinely published, the moat is gone and the plan should stop.

**Go to market.** Denver metro. Hand-recruit 20 firms through supply houses and the local
builders' association, run their next filings manually, publish the first-time-approval
delta, sell that number. SEO is a year-two asset; paid acquisition never works at this ACV.

**Metrics and kill criteria.** North star: submissions checked per week. Kill criteria,
agreed before spending: *no measurable first-time-approval improvement across 30 manual
filings by month 6 → the correction thesis is wrong, stop.* And: *fewer than 10 paying
firms by month 12 → this segment won't buy software, stop.*

---

## Appendix — original idea, mapped

| Original element | Verdict | Where it landed |
|---|---|---|
| AI drafts the application | **Cut as headline** | PermitFlow owns it with $85M; commoditising anyway per C4 |
| Municipal permits | Kept | Narrowed to small residential work in Denver metro |
| Contractor as customer | Kept, resegmented | Small firms specifically — the segment the funded players can't serve per C6 |
| "Permits take forever" | **Cut** | Denver fixed it: 2–4 weeks, down from 12–15 per C2 |
| Nationwide | Cut | Three jurisdictions until the approval delta is proven |
| Bootstrapping | Kept, and it drove the plan | Ruled out municipal sales, Procore, and paid acquisition |
| Founder's filing experience | Kept as the core asset | Source of the correction-letter thesis; distribution gap flagged per C11 |

---

## Sources

[^pf-a]: [PermitFlow Raises $31 Million in Series A](https://www.thesaasnews.com/news/permitflow-raises-31-million-in-series-a) — led by Kleiner Perkins, 2024.
[^pf-b]: [PermitFlow Raises $54 Million Series B](https://www.permitflow.com/blog/permitflow-series-b) — led by Accel, 2025.
[^tc]: [This YC alum just raised $31M to build the 'TurboTax for construction permitting'](https://techcrunch.com/2024/02/21/this-yc-alum-just-raised-31m-to-build-the-turbotax-for-construction-permitting/), TechCrunch.
[^pf-procore]: [PermitFlow Announces their Construction Permit Software Integration on Procore's Marketplace](https://markets.financialcontent.com/stocks/article/bizwire-2022-10-20-permitflow-announces-their-construction-permit-software-integration-on-procores-marketplace), 2022.
[^gl-a]: [GreenLite Raises $28.5M to Privatize Permitting for Developers and Regulatory Authorities](https://www.prnewswire.com/news-releases/greenlite-raises-28-5m-to-privatize-permitting-for-developers-and-regulatory-authorities-302250308.html) — led by Craft Ventures, 2024.
[^gl-b]: [GreenLite Raises $49.5M Series B](https://www.prnewswire.com/news-releases/greenlite-raises-49-5m-series-b-to-advance-the-privatization-of-construction-permitting-with-ai-powered-solutions-302555315.html) — led by Insight Partners, 2025.
[^pulley]: [Pulley raises $4.4M seed to shorten the construction permitting process 'from months to days'](https://techcrunch.com/2022/06/02/pulley-raises-4-4m-seed-to-shorten-the-construction-permitting-process-from-months-to-days-with-its-software), TechCrunch, 2022.
[^shovels]: [Shovels Raises $5M Seed Round to Scale AI-Powered Building Permit Platform](https://www.shovels.ai/blog/shovels-raises-5m-seed-round-to-scale-ai-powered-building-permit-platform/) and [Shovels API](https://www.shovels.ai/api) — 170M+ permits, 1,800+ jurisdictions, ~20,000 nationwide.
[^mkt]: [Citizenserve vs Accela vs Tyler vs OpenGov – A Real Comparison](https://www.citizenserve.com/citizenserve-vs-accela-vs-tyler-vs-opengov-a-real-comparison-2026/) and [Enterprise Permitting Software Market Report](https://dataintelo.com/report/enterprise-permitting-software-market) — agency counts, $382K average deal, $2.2B market (2025).
[^audit]: Denver Auditor Timothy O'Brien, residential permitting audit, January 2024 — 62 pages. Reported by [Denver Gazette](https://www.denvergazette.com/2024/01/19/delayed-permit-approvals-increases-home-building-costs-denver-auditors-say-5fe29a3c-b64a-11ee-85a9-bfb05acf0099/), [Denverite](https://denverite.com/2024/01/22/denver-slow-permitting-times-city-audit/) and [CBS Colorado](https://www.cbsnews.com/colorado/news/denvers-city-auditor-slow-permitting-process-costs-homeowners/).
[^sdb]: [Are Denver Permit Times Finally Turning Around?](https://sdb-denver.com/2023/interior-design/are-denver-permit-times-finally-turning-around/) and [Denver's Average Plan Review Time Almost Reaches 400 Days](https://sdb-denver.com/2024/the-construction-industry/denvers-average-plan-review-time-almost-reached-400-days-in-march/) — trade coverage; figures vary by permit category, so verify against the city's current dashboard.
[^exp]: [How Much Does a Permit Expediter Cost?](https://permitplace.com/permit-expediter-cost-guide/) and [What's a Permit Expediter? Overview, Costs, Alternatives](https://www.permitflow.com/blog/permit-expediter).
[^reject]: [Top Building Permit Rejection Reasons and How to Avoid Them](https://jdj-consulting.com/common-building-permit-rejection-reasons-and-how-to-avoid-them/) and [Why Building Permits Get Rejected](https://www.cadtri.com/blog/why-building-permits-get-rejected-and-how-to-pass-plan-check-the-first-time).
[^kc]: [Permit and Plan Review Data, City of Kansas City](https://www.kcmo.gov/city-hall/departments/city-planning-development/permits/permits-dashboard-2023).

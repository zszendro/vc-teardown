# vc-teardown

**A Claude Skill that stress-tests your startup idea as a skeptical VC — then rebuilds it into a plan with a defensible moat.**

Describe a business idea in one line or ten pages. The skill researches who already built it, attacks it with the objections a real investor would raise, finds the wedge the incumbent structurally won't take, and writes the business plan, MVP scope, go-to-market and kill criteria.

Most ideas fail not because they're bad, but because the obvious version is already built. This skill is designed to find that out in an afternoon instead of six months.

---

## What it does

**1. Intake** — takes whatever detail you have. No questionnaire; at most three questions, and only ones that change the analysis.

**2. Research** — searches for direct incumbents, free substitutes, adjacent software your buyer already pays for, and evidence the pain is real. This step is non-negotiable: skipping it produces generic startup advice.

**3. Teardown** — 8–12 numbered challenges drawn from a library of 20 attack surfaces. Every challenge ends in a concrete revision. Criticism that doesn't change the plan doesn't count.

**4. Moat** — the reframe. Twelve patterns for finding defensibility, including the two that do most of the work: *generate the data instead of aggregating it*, and *find the incumbent's metric mismatch*.

**5. Plan** — market reality, tiered use cases, revenue lines ordered by when they turn on, unit economics with the actual arithmetic, MVP scope and stack, GTM, risk register, and falsifiable kill criteria.

**6. Delivery** — a written plan, plus an appendix mapping every element of your original idea to where it landed.

---

## How it differs from other VC skills

There are several Claude skills in this space. Most of them **score** something you've already built — a pitch deck, a fundraising narrative, a named company you're evaluating. Some simulate specific investors' philosophies to grade your existing story.

This one starts earlier and ends differently. It takes a raw idea, establishes what's already been built in that market, kills the version that loses, and **rebuilds the idea around a different moat**. The teardown isn't the deliverable — the reframe is.

If you have a deck and want it graded, use one of the others. If you have an idea and want to know whether the obvious version of it is already dead, use this.

---

## Why it's not a yes-man

Three constraints do the work:

- **It runs the numbers.** If one fully-penetrated beachhead produces $18k of revenue, it writes that number. Especially then.
- **It states the honest scale verdict.** Lifestyle business, bootstrap SaaS, or venture-scale — in plain words. Dressing an SMB SaaS as a venture marketplace fails diligence and wastes a year.
- **It names the cheapest test.** The experiment that de-risks the biggest assumption usually costs time, not money — and it says explicitly what shouldn't be built until that test passes.

It's also calibrated not to be contrarian for sport. If a challenge has a good answer, it says so and moves on. Manufactured objections cost credibility on the real ones.

---

## Install

**Claude apps** — download `vc-teardown.skill` from [Releases](../../releases) and click **Save skill** on the file card in a conversation.

**Claude Code** — clone anywhere, then symlink the skill folder into your skills directory:

```bash
git clone https://github.com/zszendro/vc-teardown.git ~/src/vc-teardown
ln -s ~/src/vc-teardown/vc-teardown ~/.claude/skills/vc-teardown
```

Claude Code follows the symlink and reads `SKILL.md` from the target, so `git pull` updates the skill in place.

Cloning straight into `~/.claude/skills/vc-teardown` does **not** work: this repo's root holds the README and LICENSE, so `SKILL.md` would land at `~/.claude/skills/vc-teardown/vc-teardown/SKILL.md` — one level deeper than skill discovery looks.

**Manual** — copy the inner `vc-teardown/` folder (not the repo root) into wherever your setup loads skills from.

---

## Use it

Just describe the idea. The skill triggers on its own:

> I'm thinking about building a marketplace for freelance CAD designers.

> Poke holes in this: a subscription box for aquarium hobbyists.

> Here's my pitch deck outline — act as a VC and tell me what's wrong with it.

> Is there a moat in an AI tool that drafts municipal permit applications?

It also triggers on "validate this idea," "what does the competition look like," "find the moat," and "write me a business plan."

Two things worth telling it up front, since they change the analysis: **where you'd launch**, and whether you're **bootstrapping or raising**.

---

## Structure

```
vc-teardown/
├── SKILL.md                        # workflow + tone calibration
└── references/
    ├── challenge-library.md        # 20 attack surfaces
    ├── moat-patterns.md            # 12 reframes
    ├── plan-template.md            # output structure
    └── example-teardown.md         # one idea, worked end to end
```

Reference files load only when needed, so the skill stays cheap in context until it's actually working.

### The 20 challenges

Competition · Free substitutes · Monetization · Willingness to pay · Cold start · Distribution · Buyer incentive · Sales cycle · Data availability · Regulatory & liability · Founder-market fit · Capital efficiency · Defensibility · Feature-not-a-company · Retention · Scale honesty · Timing · Platform dependency · AI-native risk · Atoms and capital intensity

### The 12 moat patterns

Demote the commodity · Generate the data, don't aggregate it · Sell operational relief, not marketing exposure · The incumbent's metric mismatch · Granted distribution beats won distribution · The unserved 80% · Institutional switching cost · Vertical depth over horizontal reach · Embedded distribution · Proprietary model or eval set · Regulatory or license position · Sequence the moat

---

## What it isn't

Not investment advice, not a substitute for talking to customers, and not a replacement for an operator who knows your market. It's a structured second opinion that arrives before you write code — good at finding what's already built and where the obvious plan breaks, and useless as a source of conviction.

The output is a hypothesis with kill criteria attached. The point is to go test it.

---

## Contributing

The reference files are the interesting part. New attack surfaces, new moat patterns, and worked examples from real teardowns are all welcome — especially from categories the current library handles badly (hardware, biotech, regulated finance, deep tech).

## License

MIT

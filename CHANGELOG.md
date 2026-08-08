# Changelog

All notable changes to this skill are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] — 2026-08-07

### Added

- **Four challenge surfaces**, taking the library from 16 to 20: timing ("why now?" and
  the prior-attempts graveyard), platform dependency (price risk vs. existence risk),
  AI-native risk (whether a product rides model improvement or gets absorbed by it), and
  atoms and capital intensity (hardware, inventory, long R&D).
- **Three moat patterns**, taking the set from 9 to 12: embedded distribution,
  proprietary model or eval set, and regulatory or license position. "Sequence the moat"
  renumbers from 9 to 12 to stay last as the capstone.
- **`references/example-teardown.md`** — one idea worked end to end, so the output shape
  is visible without installing the skill. Produced by running the skill on itself, with
  researched and footnoted market facts — named competitors and their actual funding, a
  city audit, real price anchors — rather than illustrative ones. Figures carry a date and
  a re-verify warning. Where the plan needs a number that can't be sourced, it's labelled
  an assumption instead.
- **`CHANGELOG.md`** and `metadata.version` in `SKILL.md`, so an installed copy carries a
  version string.
- **`scripts/validate.py` and `scripts/package.sh`** — the `.skill` bundle is now built
  reproducibly, with validation that fails the build rather than the upload.
- **`.github/workflows/validate.yml`** — runs both on every push and pull request.

### Fixed

- **The Claude Code install instruction.** Cloning into `~/.claude/skills/vc-teardown`
  put `SKILL.md` one directory deeper than skill discovery looks, so the skill silently
  never loaded, with no error explaining why. The README now documents the supported
  symlink route, which also makes `git pull` the update path.
- **The Claude apps install instruction**, which described a flow that doesn't exist. It
  now gives the real path — Customize → Skills → Add → Upload a skill.

- **A conversational close.** `SKILL.md` section 6 now ends the delivery by naming the one
  or two things the analysis is least sure about, then offering three or four specific next
  steps — expanding a named challenge, a PDF, a one-page executive summary, a deck outline,
  re-running the economics on the user's own numbers, or a teardown of the reframe itself.
  Guarded so offers follow the deliverable and never replace it.

### Changed

- **Guards against the worked example shortening output.** An in-context example anchors
  harder than an instruction, and a compressed one risked producing thinner plans than
  1.0.1 did. Section 5 of the example is now reproduced at full depth as the density
  reference, every other section carries an explicit `[full length: ~N words]` marker, and
  the 2,500–4,000 word target is now stated in `SKILL.md` itself rather than only in
  `plan-template.md`. Verified by running the skill end to end on an unrelated idea: 5,933
  words, all sections present, from a run given no hint that length was being measured.
- **The word range is explicitly not a target to iterate against.** That same test run
  spent about ten minutes in "compression passes to hit the binding word range" without
  converging — a stall is a worse outcome than a plan that runs long. Both `SKILL.md` and
  `plan-template.md` now say to write once at the depth each section needs and skip the
  compression pass, noting that re-editing strips arithmetic before it strips padding.
- **Install section rewritten.** It now states that the two routes are different
  mechanisms and do not sync, that the app route is a cloud upload storing the skill
  against your account rather than on disk, that it needs a Pro/Max/Team/Enterprise plan
  with code execution enabled, and that cloud and Cowork sessions read the account's
  skills rather than `~/.claude/skills/`.
- **Dropped the "Manual" install option.** It described copying the folder "wherever your
  setup loads skills from", which was vague enough to reproduce the path bug above and
  covered no surface the two documented routes don't.
- `SKILL.md` declares `license: MIT`, and its section 3 and 4 summaries list the new
  surfaces and the eval-set move.
- `scripts/validate.py` caps `description` at 1024 rather than 1536 — the API and upload
  path enforce 1024, so that's the binding limit.

## [1.0.1] — 2026-08-02

First public release of the vc-teardown Claude Skill.

### Added

- `SKILL.md` — the six-stage workflow: intake, research, teardown, moat, plan, deliver.
- `references/challenge-library.md` — 16 attack surfaces, each with the evidence to look
  for and the plan change it typically forces.
- `references/moat-patterns.md` — 9 reframe patterns in When / Example / Test form.
- `references/plan-template.md` — the output document structure, sections 0–9 plus the
  original-idea appendix.

[1.1.0]: https://github.com/zszendro/vc-teardown/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/zszendro/vc-teardown/releases/tag/v1.0.1

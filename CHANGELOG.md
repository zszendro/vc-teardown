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
  is visible without installing the skill. Its market facts are invented for
  illustration and the file says so.
- **`CHANGELOG.md`** and `metadata.version` in `SKILL.md`, so an installed copy carries a
  version string.
- **`scripts/validate.py` and `scripts/package.sh`** — the `.skill` bundle is now built
  reproducibly, with validation that fails the build rather than the upload.
- **`.github/workflows/validate.yml`** — runs both on every push and pull request.

### Fixed

- **The Claude Code install instruction.** Cloning into `~/.claude/skills/vc-teardown`
  put `SKILL.md` one directory deeper than skill discovery looks, so the skill silently
  never loaded. The README now documents the supported symlink route, which also makes
  `git pull` the update path.

### Changed

- `SKILL.md` declares `license: MIT`, and its section 3 and 4 summaries list the new
  surfaces and the eval-set move.

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

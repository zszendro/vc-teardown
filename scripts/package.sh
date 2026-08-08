#!/usr/bin/env bash
# Build vc-teardown.skill for attaching to a GitHub Release.
#
# The bundle contains the skill directory and nothing else — README, LICENSE,
# CHANGELOG and scripts/ stay in the repo and out of the artifact. Validation
# runs first and is not optional: an invalid frontmatter key packages fine here
# but fails on upload to claude.ai, which is the install path most users take.
#
# Usage: bash scripts/package.sh

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

skill_dir="vc-teardown"
bundle="vc-teardown.skill"
alias_bundle="vc-teardown.zip"

python3 scripts/validate.py "$skill_dir"

rm -f "$bundle" "$alias_bundle"
zip -r -q "$bundle" "$skill_dir" \
  -x '*.DS_Store' -x '__MACOSX/*' -x '*/__pycache__/*'

# Same archive under both names. The .skill extension is what the README and
# past releases use and the upload dialog accepts it, but the documented format
# is a plain zip — shipping both means no one is blocked by a strict file picker.
cp "$bundle" "$alias_bundle"

echo "built $bundle and $alias_bundle ($(du -h "$bundle" | cut -f1) each)"
unzip -l "$bundle"

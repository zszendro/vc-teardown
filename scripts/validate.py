#!/usr/bin/env python3
"""Validate the vc-teardown skill before packaging or release.

The important check is the frontmatter key set. Claude Code accepts a wide range
of frontmatter fields, but `.skill` packaging and claude.ai upload validate
against the six-field Agent Skills spec and fail with a hard error on anything
else. Since a downloadable `.skill` bundle is this project's primary install
path, a Claude Code-only field (`version:`, `when_to_use:`, `argument-hint:` …)
would silently pass local use and then break the release. Fail here instead.

Usage: python3 scripts/validate.py [skill_dir]   (default: vc-teardown)
"""

import re
import sys
from pathlib import Path

import yaml

# https://agentskills.io — the only fields `.skill` packaging and claude.ai upload accept.
SPEC_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}

# description + when_to_use are truncated past this in the skill listing.
DESCRIPTION_LIMIT = 1536

errors: list[str] = []
warnings: list[str] = []


def main() -> int:
    skill_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "vc-teardown")
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.is_file():
        print(f"FAIL: {skill_md} not found", file=sys.stderr)
        return 1

    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        print(f"FAIL: {skill_md} has no YAML frontmatter", file=sys.stderr)
        return 1

    _, raw_fm, body = text.split("---\n", 2)

    try:
        fm = yaml.safe_load(raw_fm)
    except yaml.YAMLError as exc:
        print(f"FAIL: frontmatter is not valid YAML: {exc}", file=sys.stderr)
        return 1

    if not isinstance(fm, dict):
        print("FAIL: frontmatter did not parse to a mapping", file=sys.stderr)
        return 1

    check_frontmatter(fm)
    check_references(skill_dir, body)

    for warning in warnings:
        print(f"warn: {warning}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    version = (fm.get("metadata") or {}).get("version", "unset")
    print(f"ok: {fm.get('name')} v{version} — frontmatter and references valid")
    return 0


def check_frontmatter(fm: dict) -> None:
    unexpected = set(fm) - SPEC_FIELDS
    if unexpected:
        errors.append(
            f"unexpected frontmatter key(s): {', '.join(sorted(unexpected))}. "
            f"Packaging and claude.ai upload allow only: {', '.join(sorted(SPEC_FIELDS))}. "
            "Version belongs under `metadata:`, not at the top level."
        )

    description = fm.get("description")
    if not description:
        errors.append("`description` is missing — Claude uses it to decide when to load the skill")
    elif len(description) > DESCRIPTION_LIMIT:
        errors.append(f"description is {len(description)} chars, over the {DESCRIPTION_LIMIT} limit")

    metadata = fm.get("metadata")
    if metadata is None:
        warnings.append("no `metadata.version` — the bundle will carry no version string")
    elif not isinstance(metadata, dict):
        errors.append("`metadata` must be a map; Claude Code drops a value that isn't one")
    elif "version" not in metadata:
        warnings.append("`metadata` has no `version` key")


def check_references(skill_dir: Path, body: str) -> None:
    """Every references/*.md named in the body must exist, and vice versa."""
    named = set(re.findall(r"references/[\w.-]+\.md", body))
    for rel in sorted(named):
        if not (skill_dir / rel).is_file():
            errors.append(f"SKILL.md points at {rel}, which does not exist")

    refs_dir = skill_dir / "references"
    if refs_dir.is_dir():
        for path in sorted(refs_dir.glob("*.md")):
            if f"references/{path.name}" not in named:
                warnings.append(f"{path.name} exists but SKILL.md never points at it")


if __name__ == "__main__":
    sys.exit(main())

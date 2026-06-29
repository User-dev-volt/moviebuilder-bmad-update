#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""check_character — deterministic structural check for a CPM character state file.

Validate-mode plumbing for cpm-character-create. It confirms only what a machine can
judge without reading meaning: the load-bearing header (the `# Character:` H1 and the
bold Asset ID / Status fields) and required sections are present, the AUTHORED immutable
Visual Identity content pins BOTH LEFT and RIGHT (the continuity anchor an AI video model
needs) with no template guidance left unfilled, and a roster row exists for the character
in the Characters index. Template scaffolding (the section intro and underscore-italic
placeholder spans) is stripped before the laterality check, so boilerplate that names
both sides can never satisfy the gate. Whether the captured detail is GOOD continuity
stays with the prompt — this script reports structure, not substance.

Output: one JSON object on stdout.
Exit codes: 0 = pass; 1 = hold (structure incomplete); 2 = usage/precondition error
            (the message names the fix).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Required header + sections/fields — kept in sync with references/character-contract.md.
# The H1 title is checked separately via NAME_RE (its value is the variable {Name}, so it
# cannot be a literal substring); the contract names the H1 as load-bearing header.
H1_REQUIREMENT = "# Character: {Name}"
REQUIRED_FIELDS = [
    "**Asset ID:**",
    "**Status:**",
    "## Visual Identity (Immutable",
    "### Face",
    "### Body",
    "## Current Outfit",
    "## Inventory",
    "## Physical State",
    "## Behavioral Profile",
    "## Arc Position",
    "## Version History",
]

IMMUTABLE_HEADER = "## Visual Identity (Immutable"
NAME_RE = re.compile(r"^#\s+Character:\s*(.+?)\s*$", re.MULTILINE)
# Laterality is written uppercase by convention (LEFT eyebrow, RIGHT jawline), so a
# case-sensitive word-boundary match avoids false hits on words like "left" or "right".
LEFT_RE = re.compile(r"\bLEFT\b")
RIGHT_RE = re.compile(r"\bRIGHT\b")
# Template guidance is written as underscore-italic placeholder spans (_..._); authored
# emphasis in real character files uses *...* (see the proven instances), so stripping
# only _..._ removes scaffolding without touching authored content.
ITALIC_PLACEHOLDER_RE = re.compile(r"_[^_\n]+_")
# A bullet whose value is wholly an italic placeholder is an unfilled template slot —
# retained guidance, not authored continuity. Such a file is not continuity-ready.
UNFILLED_BULLET_RE = re.compile(r"(?m)^\s*[-*]\s+\*\*[^\n]+?:\*\*\s*_[^\n]+_\s*$")


def err(message: str) -> dict:
    """A usage/precondition error result. The message names the fix."""
    return {"ok": False, "status": "error", "error": message}


def immutable_section(text: str) -> str:
    """Return the text of the immutable Visual Identity section (its header to the next H2)."""
    start = text.find(IMMUTABLE_HEADER)
    if start == -1:
        return ""
    rest = text[start + len(IMMUTABLE_HEADER):]
    end = rest.find("\n## ")  # next H2 ends the section; H3 subsections stay inside it
    return rest if end == -1 else rest[:end]


def authored_laterality_text(section: str) -> str:
    """The authored content of the immutable section, with template scaffolding removed.

    Drops the descriptive intro (everything before the first ### subsection) and all
    underscore-italic placeholder spans, so boilerplate guidance can never satisfy the
    LEFT/RIGHT gate — only what the filmmaker actually anchored counts. Without this, an
    untouched template (whose guidance names both sides) would pass a non-anchored file.
    """
    first_sub = section.find("\n### ")
    body = section[first_sub:] if first_sub != -1 else ""
    return ITALIC_PLACEHOLDER_RE.sub(" ", body)


def character_name(text: str, fallback: str) -> str:
    m = NAME_RE.search(text)
    return m.group(1).strip() if m else fallback


def check(character: Path, index: Path | None) -> tuple[dict, int]:
    if not character.is_file():
        return err(f"character file not found: {character} — pass --character with the path "
                   f"to the character's .md file"), 2

    text = character.read_text(encoding="utf-8")
    header_present = NAME_RE.search(text) is not None
    name = character_name(text, character.stem)

    missing_fields = [f for f in REQUIRED_FIELDS if f not in text]

    section = immutable_section(text)
    if not section:
        # No immutable section at all — both sides are unanchored by definition.
        missing_sides = ["LEFT", "RIGHT"]
        unfilled = 0
    else:
        authored = authored_laterality_text(section)
        missing_sides = []
        if not LEFT_RE.search(authored):
            missing_sides.append("LEFT")
        if not RIGHT_RE.search(authored):
            missing_sides.append("RIGHT")
        # Retained template guidance (a bullet still wholly italic) is not authored.
        unfilled = len(UNFILLED_BULLET_RE.findall(section))

    # Roster: exactly one row for this character must exist in the index.
    if index is None:
        index = character.parent / "_index.md"
    roster_row_present = False
    roster_issue = ""
    if index.is_file():
        roster_row_present = f"**{name}**" in index.read_text(encoding="utf-8")
        if not roster_row_present:
            roster_issue = f"no roster row for **{name}** in {index}"
    else:
        roster_issue = f"roster index not found: {index}"

    issues = []
    if not header_present:
        issues.append(f"missing required header: {H1_REQUIREMENT}")
    if missing_fields:
        issues.append(f"missing required fields: {', '.join(missing_fields)}")
    if missing_sides:
        issues.append(f"immutable Visual Identity does not pin {', '.join(missing_sides)} "
                      f"(both sides required for AI continuity)")
    if unfilled:
        issues.append(f"immutable Visual Identity still holds {unfilled} unfilled template "
                      f"placeholder(s) — author each bullet before handoff")
    if roster_issue:
        issues.append(roster_issue)

    intact = not issues
    return {
        "ok": True,
        "status": "pass" if intact else "hold",
        "character_path": str(character),
        "character_name": name,
        "header_present": header_present,
        "index_path": str(index),
        "missing_fields": missing_fields,
        "missing_sides": missing_sides,
        "unfilled_immutable_placeholders": unfilled,
        "roster_row_present": roster_row_present,
        "issues": issues,
    }, 0 if intact else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Deterministic structural check for a CPM character state file")
    p.add_argument("--character", required=True, type=Path, help="path to the character .md file")
    p.add_argument("--index", type=Path, help="path to Bible/Characters/_index.md "
                                              "(default: _index.md beside the character file)")
    args = p.parse_args(argv)

    result, code = check(args.character, args.index)
    print(json.dumps(result, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())

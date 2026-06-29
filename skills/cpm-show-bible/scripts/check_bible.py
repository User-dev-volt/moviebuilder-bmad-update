#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""check_bible — deterministic structural check for a CPM Show Bible.

The Show Bible is the narrative DNA a production runs on; the Showrunner cannot
guard a Bible with a missing or hollow section. This script does only the
mechanical, deterministic half of validation: confirm every required section is
present and carries real content. It makes no judgment about whether a section
is GOOD — that substance call (is the logline sharp? do the pillars actually
constrain a beat?) stays in the prompt that calls this. Structure here, judgment
there; neither leaks into the other.

"Real content" is any non-blank line that is not a heading and not a bare
`{placeholder}` token left unfilled from the template. HTML comments are stripped
before the scan, so a section that is only template guidance counts as empty.

Output: one JSON object on stdout.
Exit codes: 0 = pass; 1 = hold (sections missing or empty); 2 = usage or
            precondition error (the message names the fix).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# The required sections, in canonical display form. Kept in sync with
# references/show-bible-contract.md and assets/show-bible-template.md.
REQUIRED_SECTIONS = [
    "Logline",
    "Genre & Tone",
    "Thematic Pillars",
    "World Rules",
    "Story Arc",
    "Recurring Motifs",
]

COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
BARE_PLACEHOLDER_RE = re.compile(r"^\{[^{}]*\}$")


def err(message: str) -> dict:
    """A usage/precondition error result. The message names the fix."""
    return {"ok": False, "status": "error", "error": message}


def normalize(heading: str) -> str:
    """Fold a heading to a comparable key: lowercased, whitespace-collapsed,
    'and' treated as '&' so 'Genre and Tone' matches 'Genre & Tone'."""
    text = " ".join(heading.strip().lower().split())
    return text.replace(" and ", " & ")


def split_sections(text: str) -> dict[str, list[str]]:
    """Map each H2 heading's normalized text to the body lines beneath it,
    up to the next H2 (or end of file). Comments are already stripped."""
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in text.splitlines():
        if line.startswith("## "):  # H2 only; '### ' does not match
            current = normalize(line[3:])
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    return sections


def has_real_content(body: list[str]) -> bool:
    """True if any line is genuine content — non-blank, not a heading, and not a
    lone unfilled {placeholder}. List items, table rows, and prose all count."""
    for line in body:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if BARE_PLACEHOLDER_RE.match(stripped):
            continue
        return True
    return False


def check(bible_path: Path) -> tuple[dict, int]:
    raw = bible_path.read_text(encoding="utf-8")
    text = COMMENT_RE.sub("", raw)
    sections = split_sections(text)

    missing: list[str] = []
    empty: list[str] = []
    for name in REQUIRED_SECTIONS:
        key = normalize(name)
        if key not in sections:
            missing.append(name)
        elif not has_real_content(sections[key]):
            empty.append(name)

    intact = not (missing or empty)
    return {
        "ok": True,
        "status": "pass" if intact else "hold",
        "bible_path": str(bible_path),
        "missing_sections": missing,
        "empty_sections": empty,
    }, 0 if intact else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Deterministic structural check for a CPM Show Bible"
    )
    p.add_argument("--bible", required=True,
                   help="path to the Show Bible markdown file (Bible/Show_Bible.md)")
    args = p.parse_args(argv)

    bible_path = Path(args.bible)
    if not bible_path.is_file():
        result, code = err(
            f"Show Bible not found: {bible_path} — run the Show Bible workflow in create "
            f"mode to author one, or pass the correct --bible path"
        ), 2
    else:
        result, code = check(bible_path)

    print(json.dumps(result, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())

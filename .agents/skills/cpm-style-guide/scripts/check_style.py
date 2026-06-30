#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""check_style — deterministic structural check for a CPM Style Guide.

Grades the four files a production's visual law lives in, under the project's
Architecture/ folder: Style_Guide.md, Palette.md, Lens_Language.md, Vocabulary.md.
It checks only what a structure check can know for certain — each file present,
each required section present, the palette carrying exact hex codes (not vague color
names), and the vocabulary carrying BOTH a banned list and a required list. A list
whose only rows are raw {placeholder} template tokens counts as empty, so an untouched
template never satisfies the gate. Hex codes and the banned list are graded at the same
hardness: either one missing is a hold. All substance judgment — every color carrying a hex, every banned word
justified, choices tracing to the Show Bible — stays in the prompt that calls this.

Read-only: writes nothing. Output is one JSON object on stdout.
Exit codes: 0 = pass; 1 = hold (gaps found); 2 = usage/precondition error (the
message names the fix).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# --- The contract (kept in sync with references/style-guide-contract.md) ---

# Each required section is matched by a keyword appearing in a markdown heading line.
REQUIRED_SECTIONS = {
    "Style_Guide.md": ["Visual Identity", "Lighting Protocol", "Color Palette",
                       "Camera Language", "Spatial Rules"],
    "Palette.md": ["Allowed Colors", "Forbidden Colors", "Color Meanings"],
    "Lens_Language.md": ["Lens Vocabulary", "Shot Progressions", "Camera Movement Rules"],
    "Vocabulary.md": ["Required Substitutions", "Banned Words"],
}
REQUIRED_FILES = list(REQUIRED_SECTIONS)

HEX_RE = re.compile(r"#[0-9A-Fa-f]{6}")
# A markdown table separator row: only pipes, dashes, colons, spaces.
SEPARATOR_RE = re.compile(r"^\s*\|[\s|:-]+\|?\s*$")
# A cell that is wholly a {placeholder} token is raw template scaffolding, not an
# authored value; a bullet whose value (after an optional bold label) is such a token
# is an unfilled slot. A list whose only entries are these counts as empty.
PLACEHOLDER_CELL_RE = re.compile(r"^\{.*\}$")
PLACEHOLDER_BULLET_RE = re.compile(r"^\s*[-*]\s+(?:\*\*[^\n]+?:\*\*\s*)?\{[^\n]*\}\s*$")


def err(message: str) -> dict:
    """A usage/precondition error result. The message names the fix."""
    return {"ok": False, "status": "error", "error": message}


def section_body(text: str, keyword: str) -> str | None:
    """Return the body of the section whose heading contains keyword, or None if absent.

    The body runs from the line after the matched heading to the next markdown heading.
    """
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.lstrip().startswith("#") and keyword.lower() in line.lower():
            start = i + 1
            break
    if start is None:
        return None
    end = start
    while end < len(lines) and not lines[end].lstrip().startswith("#"):
        end += 1
    return "\n".join(lines[start:end])


def _placeholder_row(line: str) -> bool:
    """True when a table row's every non-empty cell is a bare {placeholder} token — a raw
    template row (| {banned word} | {what it drifts to} | {...} |), not an authored entry."""
    cells = [c.strip() for c in line.split("|")]
    cells = [c for c in cells if c]
    return bool(cells) and all(PLACEHOLDER_CELL_RE.match(c) for c in cells)


def has_entries(body: str) -> bool:
    """True when a section body carries at least one real, authored entry — a table data
    row or a list bullet. Rows and bullets that are only {placeholder} tokens are raw
    template scaffolding and are skipped, so an untouched template never satisfies a list
    gate (mirrors the placeholder rigor in check_character.py)."""
    pipe_rows = [ln for ln in body.splitlines()
                 if ln.lstrip().startswith("|")
                 and not SEPARATOR_RE.match(ln)
                 and not _placeholder_row(ln)]
    if len(pipe_rows) >= 2:  # a header row plus at least one authored data row
        return True
    return any(re.match(r"^\s*[-*] ", ln) and not PLACEHOLDER_BULLET_RE.match(ln)
               for ln in body.splitlines())


def check(project_path: Path) -> tuple[dict, int]:
    arch = project_path / "Architecture"
    if not project_path.exists():
        return err(f"{project_path} does not exist — pass --project-path the production "
                   f"project's root folder"), 2
    if not arch.is_dir():
        return err(f"no Architecture/ folder in {project_path} — the Style Guide has not "
                   f"been created yet; run the Style Guide workflow's create mode first"), 2

    missing_files: list[str] = []
    present: dict[str, str] = {}
    for name in REQUIRED_FILES:
        path = arch / name
        if path.is_file():
            present[name] = path.read_text(encoding="utf-8")
        else:
            missing_files.append(name)

    missing_sections: dict[str, list[str]] = {}
    for name, text in present.items():
        absent = [s for s in REQUIRED_SECTIONS[name] if section_body(text, s) is None]
        if absent:
            missing_sections[name] = absent

    issues: list[str] = []
    for name in missing_files:
        issues.append(f"{name} is missing from Architecture/")
    for name, absent in missing_sections.items():
        issues.append(f"{name}: missing section(s): {', '.join(absent)}")

    # Exact hex codes in the palette — vague color names instead of hex are a HOLD.
    palette_hex_ok = False
    if "Palette.md" in present:
        allowed = section_body(present["Palette.md"], "Allowed Colors")
        palette_hex_ok = bool(allowed and HEX_RE.search(allowed))
        if not palette_hex_ok:
            issues.append("Palette.md: no exact hex code found in Allowed Colors — vague "
                          "color names are a HOLD; specify every allowed color as a hex code")

    # Vocabulary must carry BOTH lists, each non-empty — graded as hard as the hex check.
    banned_ok = False
    required_ok = False
    if "Vocabulary.md" in present:
        banned = section_body(present["Vocabulary.md"], "Banned Words")
        required = section_body(present["Vocabulary.md"], "Required Substitutions")
        banned_ok = bool(banned and has_entries(banned))
        required_ok = bool(required and has_entries(required))
        if not banned_ok:
            issues.append("Vocabulary.md: the Banned Words list is missing or empty — a HOLD")
        if not required_ok:
            issues.append("Vocabulary.md: the Required Substitutions list is missing or empty — a HOLD")

    ready = not issues
    return {
        "ok": True,
        "status": "pass" if ready else "hold",
        "project_path": str(project_path),
        "architecture_dir": str(arch),
        "missing_files": missing_files,
        "missing_sections": missing_sections,
        "palette_hex_ok": palette_hex_ok,
        "vocabulary_banned_list_ok": banned_ok,
        "vocabulary_required_list_ok": required_ok,
        "issues": issues,
    }, 0 if ready else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Deterministic structural check for a CPM Style Guide's four Architecture files")
    p.add_argument("--project-path", required=True,
                   help="the production project's root folder (the check reads its Architecture/ folder)")
    args = p.parse_args(argv)

    result, code = check(Path(args.project_path))
    print(json.dumps(result, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())

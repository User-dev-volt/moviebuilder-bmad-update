#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""validate_inception — deterministic readiness check for a CPM draft foundation.

Inception produces a draft foundation in one pass: a scaffolded project plus a draft
Show Bible, a draft Style Guide (four Architecture files), and at least one draft
character sketch. This script grades only what a structure check can know for certain:
each foundation artifact is PRESENT at its project-relative path, the scaffold is in
place, and each draft carries an HONEST draft marker. It deliberately does NOT re-judge
section depth, hex correctness, or LEFT/RIGHT laterality — those are the foundation
checks (check_bible / check_style / check_character) and the reviewer's job. Presence,
markers, and scaffold here; substance there.

A draft marker is accepted in either native form, since the artifacts mark themselves
differently by convention: a frontmatter `status: draft` (Bible, Style_Guide) or a bold
`**Status:** DRAFT` (character). Either satisfies the marker check.

Read-only: writes nothing. Output is one JSON object on stdout.
Exit codes: 0 = pass (foundation ready); 1 = hold (a foundation missing or unmarked);
            2 = error (no CPM project at that path — the message names the fix).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Project-relative paths of the foundation artifacts.
SCAFFOLD_FILES = [".cpm/config.yaml", ".cpm/manifest.md"]
SHOW_BIBLE = "Bible/Show_Bible.md"
STYLE_FILES = [
    "Architecture/Style_Guide.md",
    "Architecture/Palette.md",
    "Architecture/Lens_Language.md",
    "Architecture/Vocabulary.md",
]
STYLE_MASTER = "Architecture/Style_Guide.md"
CHARACTERS_DIR = "Bible/Characters"
CHARACTER_INDEX = "Bible/Characters/_index.md"

# A draft marker in either native form: frontmatter `status: draft` or bold `**Status:** DRAFT`.
FRONTMATTER_MARKER_RE = re.compile(r"(?im)^\s*status:\s*['\"]?draft\b")
BOLD_MARKER_RE = re.compile(r"(?i)\*\*status:\*\*\s*draft\b")


def err(message: str) -> dict:
    """A usage/precondition error result. The message names the fix."""
    return {"ok": False, "status": "error", "error": message}


def has_draft_marker(path: Path) -> bool:
    """True when the file carries an honest draft marker in either native form."""
    text = path.read_text(encoding="utf-8")
    return bool(FRONTMATTER_MARKER_RE.search(text) or BOLD_MARKER_RE.search(text))


def character_files(project: Path) -> list[Path]:
    """The authored (non-index) character sketches under Bible/Characters/."""
    chars = project / CHARACTERS_DIR
    if not chars.is_dir():
        return []
    return sorted(p for p in chars.glob("*.md") if not p.name.startswith("_"))


def check(project: Path) -> tuple[dict, int]:
    if not project.exists():
        return err(f"{project} does not exist — there is no project to validate at this "
                   f"path; run inception in create mode to onboard one"), 2
    if not (project / ".cpm").is_dir():
        return err(f"no CPM project at {project} — there is no .cpm/ scaffold; run "
                   f"inception in create mode to onboard one"), 2

    missing_files: list[str] = []
    missing_markers: list[str] = []
    issues: list[str] = []

    # --- Scaffold: config + manifest present. ---
    scaffold_missing = [rel for rel in SCAFFOLD_FILES if not (project / rel).is_file()]
    missing_files.extend(scaffold_missing)
    scaffold_ok = not scaffold_missing
    if not scaffold_ok:
        issues.append(f"scaffold incomplete — missing: {', '.join(scaffold_missing)}")

    # --- Show Bible: present + draft marker. ---
    bible_path = project / SHOW_BIBLE
    bible_present = bible_path.is_file()
    bible_marked = bible_present and has_draft_marker(bible_path)
    if not bible_present:
        missing_files.append(SHOW_BIBLE)
        issues.append(f"draft Show Bible missing: {SHOW_BIBLE}")
    elif not bible_marked:
        missing_markers.append(SHOW_BIBLE)
        issues.append(f"{SHOW_BIBLE} present but carries no draft marker (status: draft)")
    show_bible_ok = bible_present and bible_marked

    # --- Style Guide: four files present + master carries the draft marker. ---
    style_missing = [rel for rel in STYLE_FILES if not (project / rel).is_file()]
    missing_files.extend(style_missing)
    master_path = project / STYLE_MASTER
    master_marked = master_path.is_file() and has_draft_marker(master_path)
    if style_missing:
        issues.append(f"draft Style Guide incomplete — missing: {', '.join(style_missing)}")
    if master_path.is_file() and not master_marked:
        missing_markers.append(STYLE_MASTER)
        issues.append(f"{STYLE_MASTER} present but carries no draft marker (status: draft)")
    style_guide_ok = not style_missing and master_marked

    # --- Characters: index + >=1 sketch present, each marked. ---
    chars = character_files(project)
    characters_found = [p.stem for p in chars]
    index_present = (project / CHARACTER_INDEX).is_file()
    if not index_present:
        missing_files.append(CHARACTER_INDEX)
        issues.append(f"character roster missing: {CHARACTER_INDEX}")
    if not chars:
        issues.append(f"no draft character sketch under {CHARACTERS_DIR}/ "
                      f"(at least the protagonist is required)")
    unmarked_chars = [p.name for p in chars if not has_draft_marker(p)]
    for name in unmarked_chars:
        rel = f"{CHARACTERS_DIR}/{name}"
        missing_markers.append(rel)
        issues.append(f"{rel} present but carries no draft marker (**Status:** DRAFT)")
    characters_ok = index_present and bool(chars) and not unmarked_chars

    ready = scaffold_ok and show_bible_ok and style_guide_ok and characters_ok
    result = {
        "ok": True,
        "status": "pass" if ready else "hold",
        "project_path": str(project),
        "scaffold_present": scaffold_ok,
        "foundations": {
            "scaffold": "pass" if scaffold_ok else "hold",
            "show_bible": "pass" if show_bible_ok else "hold",
            "style_guide": "pass" if style_guide_ok else "hold",
            "characters": "pass" if characters_ok else "hold",
        },
        "characters_found": characters_found,
        "missing_files": missing_files,
        "missing_markers": missing_markers,
        "issues": issues,
    }
    return result, 0 if ready else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Deterministic readiness check for a CPM draft foundation "
                    "(presence + draft markers + scaffold; never section depth)")
    p.add_argument("--project", required=True, type=Path,
                   help="the CPM production project's root folder (holds .cpm/, Bible/, Architecture/)")
    args = p.parse_args(argv)

    result, code = check(args.project)
    print(json.dumps(result, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())

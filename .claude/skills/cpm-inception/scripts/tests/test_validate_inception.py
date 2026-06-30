#!/usr/bin/env python3
"""Unit tests for validate_inception.py — exercises the readiness-check contract.

Runs the real script via subprocess against throwaway draft foundations in a temp project
skeleton. One test per script-owned outcome: the full pass, each missing/unmarked HOLD mode,
both native draft-marker forms, and the no-project ERROR.
Run with: python test_validate_inception.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = SKILL_ROOT / "scripts" / "validate_inception.py"

BIBLE_DRAFT = """\
---
title: 'Show Bible (Draft): Test'
status: draft
---

# Show Bible: Test

## Logline
A clinical collector must choose his code or a widow's hope.

## Genre & Tone
- **Primary Genre:** Moral drama
"""

STYLE_MASTER_DRAFT = """\
---
project_name: 'Test'
status: draft
---

# Cinematic Style Guide (Draft) — Test

## Visual Identity
The thermal divide from cold to warm.
"""

PALETTE_DRAFT = "# Color Palette (Draft) — Test\n\n## Allowed Colors\n\n| Name | Hex | Usage |\n|--|--|--|\n| Slate Blue | `#2C3E50` | armor |\n"
LENS_DRAFT = "# Lens Language (Draft) — Test\n\n## Lens Vocabulary\n\n| Shot | Lens | Effect |\n|--|--|--|\n| CU | 85mm | clinical |\n"
VOCAB_DRAFT = "# Prompt Vocabulary (Draft) — Test\n\n## Banned Words\n\n| Word | Reason | Alt |\n|--|--|--|\n| cinematic | drifts | naturalistic |\n"

INDEX = "# Characters Index\n\n## Characters\n\n| Character | Description | Asset ID | Status |\n|--|--|--|--|\n| **Elias** | crease above LEFT eyebrow | ELIAS_V1 | DRAFT |\n"

CHAR_DRAFT_BOLD = """\
---
characterName: 'Elias'
assetID: 'ELIAS_V1'
status: 'DRAFT'
---

# Character: Elias

**Asset ID:** ELIAS_V1
**Status:** DRAFT

## Visual Identity (Immutable Unless Story Changes)

### Face
- **Distinguishing Features:** crease above LEFT eyebrow; scar on RIGHT jawline
"""

CHAR_UNMARKED = CHAR_DRAFT_BOLD.replace("**Status:** DRAFT", "**Status:** ACTIVE").replace(
    "status: 'DRAFT'", "status: 'ACTIVE'")


def run(*extra) -> tuple[int, dict]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), *extra],
        capture_output=True, text=True,
    )
    payload = json.loads(proc.stdout) if proc.stdout.strip() else {}
    return proc.returncode, payload


def build_foundation(tmp, *, make_cpm: bool = True, config: bool = True, manifest: bool = True,
                     bible: str | None = BIBLE_DRAFT, style: bool = True,
                     style_master: str = STYLE_MASTER_DRAFT, omit_style: str | None = None,
                     index: bool = True, character: str | None = CHAR_DRAFT_BOLD,
                     char_name: str = "Elias"):
    """Lay down a tiny CPM draft foundation and return the project root."""
    root = Path(tmp) / "Project"
    if make_cpm:
        (root / ".cpm").mkdir(parents=True, exist_ok=True)
        if config:
            (root / ".cpm" / "config.yaml").write_text("project_name: Test\n", encoding="utf-8")
        if manifest:
            (root / ".cpm" / "manifest.md").write_text("# Manifest\n", encoding="utf-8")
    else:
        root.mkdir(parents=True, exist_ok=True)

    if bible is not None:
        (root / "Bible").mkdir(parents=True, exist_ok=True)
        (root / "Bible" / "Show_Bible.md").write_text(bible, encoding="utf-8")

    if style:
        arch = root / "Architecture"
        arch.mkdir(parents=True, exist_ok=True)
        files = {
            "Style_Guide.md": style_master,
            "Palette.md": PALETTE_DRAFT,
            "Lens_Language.md": LENS_DRAFT,
            "Vocabulary.md": VOCAB_DRAFT,
        }
        for name, text in files.items():
            if name == omit_style:
                continue
            (arch / name).write_text(text, encoding="utf-8")

    chars = root / "Bible" / "Characters"
    chars.mkdir(parents=True, exist_ok=True)
    if index:
        (chars / "_index.md").write_text(INDEX, encoding="utf-8")
    if character is not None:
        (chars / f"{char_name}.md").write_text(character, encoding="utf-8")
    return root


class ValidateInceptionTests(unittest.TestCase):
    def test_full_foundation_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build_foundation(tmp)
            code, out = run("--project", str(root))
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertEqual(out["issues"], [])
            self.assertTrue(out["scaffold_present"])
            self.assertEqual(out["foundations"], {
                "scaffold": "pass", "show_bible": "pass",
                "style_guide": "pass", "characters": "pass"})
            self.assertEqual(out["characters_found"], ["Elias"])

    def test_missing_show_bible_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build_foundation(tmp, bible=None)
            code, out = run("--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertIn("Bible/Show_Bible.md", out["missing_files"])
            self.assertEqual(out["foundations"]["show_bible"], "hold")

    def test_unmarked_bible_holds(self):
        bible = BIBLE_DRAFT.replace("status: draft", "status: final")
        with tempfile.TemporaryDirectory() as tmp:
            root = build_foundation(tmp, bible=bible)
            code, out = run("--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertIn("Bible/Show_Bible.md", out["missing_markers"])
            self.assertEqual(out["foundations"]["show_bible"], "hold")

    def test_missing_style_file_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build_foundation(tmp, omit_style="Palette.md")
            code, out = run("--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertIn("Architecture/Palette.md", out["missing_files"])
            self.assertEqual(out["foundations"]["style_guide"], "hold")

    def test_unmarked_style_master_holds(self):
        master = STYLE_MASTER_DRAFT.replace("status: draft", "status: final")
        with tempfile.TemporaryDirectory() as tmp:
            root = build_foundation(tmp, style_master=master)
            code, out = run("--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertIn("Architecture/Style_Guide.md", out["missing_markers"])
            self.assertEqual(out["foundations"]["style_guide"], "hold")

    def test_missing_character_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build_foundation(tmp, character=None)
            code, out = run("--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertEqual(out["characters_found"], [])
            self.assertEqual(out["foundations"]["characters"], "hold")

    def test_unmarked_character_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build_foundation(tmp, character=CHAR_UNMARKED)
            code, out = run("--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertIn("Bible/Characters/Elias.md", out["missing_markers"])
            self.assertEqual(out["foundations"]["characters"], "hold")

    def test_missing_index_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build_foundation(tmp, index=False)
            code, out = run("--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertIn("Bible/Characters/_index.md", out["missing_files"])
            self.assertEqual(out["foundations"]["characters"], "hold")

    def test_missing_scaffold_config_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build_foundation(tmp, config=False)
            code, out = run("--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertIn(".cpm/config.yaml", out["missing_files"])
            self.assertEqual(out["foundations"]["scaffold"], "hold")

    def test_missing_scaffold_manifest_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build_foundation(tmp, manifest=False)
            code, out = run("--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertIn(".cpm/manifest.md", out["missing_files"])
            self.assertEqual(out["foundations"]["scaffold"], "hold")

    def test_missing_style_master_file_holds(self):
        # The master file itself absent (vs. an extract) is a missing FILE, not a missing
        # marker, and holds the style foundation.
        with tempfile.TemporaryDirectory() as tmp:
            root = build_foundation(tmp, omit_style="Style_Guide.md")
            code, out = run("--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertIn("Architecture/Style_Guide.md", out["missing_files"])
            self.assertNotIn("Architecture/Style_Guide.md", out["missing_markers"])
            self.assertEqual(out["foundations"]["style_guide"], "hold")

    def test_character_bold_marker_accepted(self):
        # A character marked ONLY with the bold form (frontmatter status stripped) still passes.
        bold_only = CHAR_DRAFT_BOLD.replace("status: 'DRAFT'\n", "")
        with tempfile.TemporaryDirectory() as tmp:
            root = build_foundation(tmp, character=bold_only)
            code, out = run("--project", str(root))
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")

    def test_no_cpm_project_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build_foundation(tmp, make_cpm=False)
            code, out = run("--project", str(root))
            self.assertEqual(code, 2, out)
            self.assertEqual(out["status"], "error")
            self.assertIn("no .cpm/", out["error"])

    def test_nonexistent_path_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "nope"
            code, out = run("--project", str(missing))
            self.assertEqual(code, 2, out)
            self.assertEqual(out["status"], "error")
            self.assertIn("does not exist", out["error"])


if __name__ == "__main__":
    unittest.main()

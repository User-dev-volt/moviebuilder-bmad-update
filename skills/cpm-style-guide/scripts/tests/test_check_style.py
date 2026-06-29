#!/usr/bin/env python3
"""Unit tests for check_style.py — exercises the structural-check CLI contract.

Builds synthetic Style Guides (a complete one, and ones with specific gaps) in a
throwaway temp directory and runs the real script against them. Run with:
python test_check_style.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = SKILL_ROOT / "scripts" / "check_style.py"

STYLE_GUIDE = """# Cinematic Style Guide — Test

## Visual Identity
A test look organized by one idea.

## Lighting Protocol
ALWAYS motivated sources.

## Color Palette
| Name | Hex | Usage Context |
|---|---|---|
| Ink | `#0B101A` | shadows |

## Camera Language
| Shot | Lens | Effect |
|---|---|---|
| Wide | 35mm | the room |

## Spatial Rules
Cold world stays screen-left.
"""

PALETTE = """# Color Palette — Test

## Allowed Colors
| Name | Hex | Usage Context |
|------|-----|---------------|
| Ink | `#0B101A` | shadows |

## Forbidden Colors
| Color | Reason |
|-------|--------|
| Pure Black (`#000000`) | too mysterious |

## Color Meanings
- **`#0B101A` Ink:** the void at rest
"""

LENS = """# Lens Language — Test

## Lens Vocabulary
| Shot Type | Lens | Emotional Effect |
|-----------|------|------------------|
| Wide | 35mm | the room |

## Shot Progressions
- **The Arc** — across the film: 85mm -> 50mm

## Camera Movement Rules
- **Default:** heavy dolly only
"""

VOCABULARY = """# Prompt Vocabulary — Test

## Required Substitutions
| Instead of... | Use... |
|---------------|--------|
| "cinematic" | "naturalistic, 35mm deep focus" |

## Banned Words
| Word | Reason | Alternative |
|------|--------|-------------|
| "cinematic" | orange/teal grade | "naturalistic" |
"""

COMPLETE = {
    "Style_Guide.md": STYLE_GUIDE,
    "Palette.md": PALETTE,
    "Lens_Language.md": LENS,
    "Vocabulary.md": VOCABULARY,
}


def run(project: Path) -> tuple[int, dict]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--project-path", str(project)],
        capture_output=True, text=True,
    )
    payload = json.loads(proc.stdout) if proc.stdout.strip() else {}
    return proc.returncode, payload


def write_guide(project: Path, files: dict[str, str]) -> None:
    arch = project / "Architecture"
    arch.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        (arch / name).write_text(content, encoding="utf-8")


class CheckStyleTests(unittest.TestCase):
    def test_complete_guide_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "proj"
            write_guide(project, COMPLETE)
            code, out = run(project)
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertEqual(out["issues"], [])
            self.assertTrue(out["palette_hex_ok"])
            self.assertTrue(out["vocabulary_banned_list_ok"])
            self.assertTrue(out["vocabulary_required_list_ok"])

    def test_missing_file_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "proj"
            files = dict(COMPLETE)
            del files["Lens_Language.md"]
            write_guide(project, files)
            code, out = run(project)
            self.assertEqual(code, 1)
            self.assertEqual(out["status"], "hold")
            self.assertIn("Lens_Language.md", out["missing_files"])

    def test_missing_section_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "proj"
            files = dict(COMPLETE)
            files["Style_Guide.md"] = STYLE_GUIDE.replace("## Spatial Rules\nCold world stays screen-left.\n", "")
            write_guide(project, files)
            code, out = run(project)
            self.assertEqual(code, 1)
            self.assertEqual(out["status"], "hold")
            self.assertIn("Spatial Rules", out["missing_sections"]["Style_Guide.md"])

    def test_vague_palette_holds(self):
        # Exact-hex enforcement: an allowed palette with vague names and no hex is a HOLD.
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "proj"
            files = dict(COMPLETE)
            files["Palette.md"] = """# Color Palette — Test

## Allowed Colors
| Name | Hex | Usage Context |
|------|-----|---------------|
| warm gold | golden | sunlight |

## Forbidden Colors
| Color | Reason |
|-------|--------|
| neon | too loud |

## Color Meanings
- **warm gold:** the soul
"""
            write_guide(project, files)
            code, out = run(project)
            self.assertEqual(code, 1)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["palette_hex_ok"])

    def test_missing_banned_list_holds(self):
        # Symmetric with the hex check: a missing banned list is just as hard a HOLD.
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "proj"
            files = dict(COMPLETE)
            files["Vocabulary.md"] = """# Prompt Vocabulary — Test

## Required Substitutions
| Instead of... | Use... |
|---------------|--------|
| "cinematic" | "naturalistic, 35mm deep focus" |
"""
            write_guide(project, files)
            code, out = run(project)
            self.assertEqual(code, 1)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["vocabulary_banned_list_ok"])

    def test_empty_banned_list_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "proj"
            files = dict(COMPLETE)
            files["Vocabulary.md"] = """# Prompt Vocabulary — Test

## Required Substitutions
| Instead of... | Use... |
|---------------|--------|
| "cinematic" | "naturalistic" |

## Banned Words
| Word | Reason | Alternative |
|------|--------|-------------|
"""
            write_guide(project, files)
            code, out = run(project)
            self.assertEqual(code, 1)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["vocabulary_banned_list_ok"])

    def test_symmetric_hardness_required_list(self):
        # The required list is held to the same bar as the banned list and the hex codes.
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "proj"
            files = dict(COMPLETE)
            files["Vocabulary.md"] = """# Prompt Vocabulary — Test

## Required Substitutions

## Banned Words
| Word | Reason | Alternative |
|------|--------|-------------|
| "cinematic" | orange/teal grade | "naturalistic" |
"""
            write_guide(project, files)
            code, out = run(project)
            self.assertEqual(code, 1)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["vocabulary_required_list_ok"])
            self.assertTrue(out["vocabulary_banned_list_ok"])

    def test_no_architecture_dir_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "proj"
            project.mkdir()
            code, out = run(project)
            self.assertEqual(code, 2)
            self.assertEqual(out["status"], "error")
            self.assertIn("Architecture", out["error"])


if __name__ == "__main__":
    unittest.main()

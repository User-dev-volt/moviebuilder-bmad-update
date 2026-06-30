#!/usr/bin/env python3
"""Unit tests for check_character.py — exercises the validate structural-check contract.

Runs the real script against throwaway character files in a temp directory.
Run with: python test_check_character.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = SKILL_ROOT / "scripts" / "check_character.py"
TEMPLATE = SKILL_ROOT / "assets" / "character-template.md"

VALID_CHARACTER = """\
---
characterName: 'Tester'
assetID: 'TESTER_V1'
status: 'ACTIVE'
---

# Character: Tester

**Asset ID:** TESTER_V1
**Status:** ACTIVE

## Visual Identity (Immutable Unless Story Changes)

### Face
- **Distinguishing Features:** scar on the RIGHT jawline; mathematically precise part on the LEFT
- **Expression Default:** neutral void
- **Age Appearance:** appears 40

### Body
- **Build:** tall, lean
- **Posture:** locked upright
- **Movement Style:** brisk, straight lines

## Current Outfit (Mutable - Update Per Scene)
- **Base:** structured charcoal suit

## Inventory (Mutable)

| Item | Status | Acquired | Notes |
|------|--------|----------|-------|
| pen | POCKET (Right) | Scene 1 | sterile instrument |

## Physical State (Mutable)

| Condition | Location | Severity | Since |
|-----------|----------|----------|-------|
| ACUTE_JAW_TENSION | jaw | active | Scene 1 |

## Behavioral Profile (For Prompt Engineer)
- **Speech Pattern:** clipped, final

## Arc Position
- **Current Emotional State:** brittle
- **Arc Progress:** 0%

## Version History

| Version | Scene | Changes |
|---------|-------|---------|
| V1 | Scene 1 | Initial state |
"""

VALID_INDEX = """\
# Characters Index

## Characters

| Character | Description | Asset ID | Status |
|-----------|-------------|----------|--------|
| **Tester** | tall lean, scar RIGHT jaw, part LEFT | TESTER_V1 | ACTIVE |
"""


def run(*extra) -> tuple[int, dict]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), *extra],
        capture_output=True, text=True,
    )
    payload = json.loads(proc.stdout) if proc.stdout.strip() else {}
    return proc.returncode, payload


class CheckCharacterTests(unittest.TestCase):
    def _write(self, tmp: str, character: str = VALID_CHARACTER, index: str | None = VALID_INDEX):
        char_path = Path(tmp) / "Tester.md"
        char_path.write_text(character, encoding="utf-8")
        idx_path = Path(tmp) / "_index.md"
        if index is not None:
            idx_path.write_text(index, encoding="utf-8")
        return char_path, idx_path

    def test_valid_character_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            char_path, idx_path = self._write(tmp)
            code, out = run("--character", str(char_path), "--index", str(idx_path))
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertEqual(out["missing_fields"], [])
            self.assertEqual(out["missing_sides"], [])
            self.assertTrue(out["roster_row_present"])
            self.assertEqual(out["character_name"], "Tester")

    def test_default_index_beside_character(self):
        with tempfile.TemporaryDirectory() as tmp:
            char_path, _ = self._write(tmp)
            code, out = run("--character", str(char_path))  # no --index
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")

    def test_right_missing_immutable_holds(self):
        # Only LEFT is anchored — RIGHT side absent must force a hold at equal hardness.
        left_only = VALID_CHARACTER.replace("scar on the RIGHT jawline; ", "")
        with tempfile.TemporaryDirectory() as tmp:
            char_path, idx_path = self._write(tmp, character=left_only)
            code, out = run("--character", str(char_path), "--index", str(idx_path))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertEqual(out["missing_sides"], ["RIGHT"])

    def test_left_missing_immutable_holds(self):
        # Mirror of the above — only RIGHT anchored — proving BOTH sides gate at equal hardness.
        right_only = VALID_CHARACTER.replace("; mathematically precise part on the LEFT", "")
        with tempfile.TemporaryDirectory() as tmp:
            char_path, idx_path = self._write(tmp, character=right_only)
            code, out = run("--character", str(char_path), "--index", str(idx_path))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertEqual(out["missing_sides"], ["LEFT"])

    def test_untouched_template_holds(self):
        # The shipped template, name filled in but every bullet left as italic guidance,
        # must HOLD — boilerplate that names sides cannot satisfy the laterality gate.
        filled = (TEMPLATE.read_text(encoding="utf-8")
                  .replace("{Name}", "Lazy").replace("{NAME}", "LAZY")
                  .replace("{date}", "2026-01-01").replace("{scene}", "Scene 1"))
        index = ("# Characters Index\n\n## Characters\n\n"
                 "| Character | Description | Asset ID | Status |\n|---|---|---|---|\n"
                 "| **Lazy** | placeholder | LAZY_V1 | ACTIVE |\n")
        with tempfile.TemporaryDirectory() as tmp:
            char_path, idx_path = self._write(tmp, character=filled, index=index)
            code, out = run("--character", str(char_path), "--index", str(idx_path))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertEqual(out["missing_sides"], ["LEFT", "RIGHT"])
            self.assertGreater(out["unfilled_immutable_placeholders"], 0)

    def test_missing_h1_header_holds(self):
        no_h1 = VALID_CHARACTER.replace("# Character: Tester\n\n", "")
        with tempfile.TemporaryDirectory() as tmp:
            char_path, idx_path = self._write(tmp, character=no_h1)
            code, out = run("--character", str(char_path), "--index", str(idx_path))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["header_present"])
            self.assertTrue(any("missing required header" in i for i in out["issues"]))

    def test_missing_required_field_holds(self):
        no_arc = VALID_CHARACTER.replace("## Arc Position", "## Backstory")
        with tempfile.TemporaryDirectory() as tmp:
            char_path, idx_path = self._write(tmp, character=no_arc)
            code, out = run("--character", str(char_path), "--index", str(idx_path))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertIn("## Arc Position", out["missing_fields"])

    def test_missing_roster_row_holds(self):
        empty_index = "# Characters Index\n\n## Characters\n\n| Character | Description | Asset ID | Status |\n|---|---|---|---|\n"
        with tempfile.TemporaryDirectory() as tmp:
            char_path, idx_path = self._write(tmp, index=empty_index)
            code, out = run("--character", str(char_path), "--index", str(idx_path))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["roster_row_present"])

    def test_missing_index_file_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            char_path, _ = self._write(tmp, index=None)
            missing = Path(tmp) / "_index.md"
            code, out = run("--character", str(char_path), "--index", str(missing))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertTrue(any("roster index not found" in i for i in out["issues"]))

    def test_missing_character_file_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "Nobody.md"
            code, out = run("--character", str(missing))
            self.assertEqual(code, 2)
            self.assertEqual(out["status"], "error")
            self.assertIn("character file not found", out["error"])


if __name__ == "__main__":
    unittest.main()

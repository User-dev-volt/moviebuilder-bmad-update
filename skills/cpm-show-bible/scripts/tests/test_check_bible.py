#!/usr/bin/env python3
"""Unit tests for check_bible.py — exercises the deterministic structural contract.

Runs the real script against throwaway Bible files in a temp directory, and (when
present) against the proven production Bible as a known-good lock.
Run with: python test_check_bible.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = SKILL_ROOT / "scripts" / "check_bible.py"
PROVEN = (SKILL_ROOT.parents[1] / "_bmad-output" / "cpm-projects"
          / "The Second Receipt" / "Bible" / "Show_Bible.md")

FULL_BIBLE = """\
---
title: 'Show Bible: The Test Reel'
---

# Show Bible: The Test Reel

## Logline

A weary archivist must choose between burning the last record or living inside it.

## Genre & Tone

- **Primary Genre:** Speculative drama
- **Tone:** Cold dread thawing into grief. Begins clinical, ends elegiac.
- **Comparable Works:** *Solaris* meets *Arrival*.

## Thematic Pillars

1. **Memory as debt:** what do we owe the people we choose to forget?
2. **The cost of preservation:** does keeping a thing alive keep it true?

## World Rules

### Physics
- A record can be read only once before it decays — every viewing is a theft.

### Society
- The Archive owns all memory; an unfiled memory legally never happened.

## Story Arc

### Act I: The Filing *(approx 1-3)*
The archivist wants order and is handed a record that refuses to be filed.

### Act III: The Burning *(approx 7-10)*
She needs to be remembered, not to remember; she burns the record and is freed.

## Recurring Motifs

### Visual Motifs
- **Ash on glass:** opening, midpoint, and finale — tracks what cannot be re-read.

### Color Motifs
- **Archive grey:** the color of things the world has agreed to stop feeling.
"""


def run(*extra) -> tuple[int, dict]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), *extra],
        capture_output=True, text=True,
    )
    payload = json.loads(proc.stdout) if proc.stdout.strip() else {}
    return proc.returncode, payload


def write_bible(tmp: str, text: str) -> Path:
    path = Path(tmp) / "Show_Bible.md"
    path.write_text(text, encoding="utf-8")
    return path


class CheckBibleTests(unittest.TestCase):
    def test_full_bible_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = write_bible(tmp, FULL_BIBLE)
            code, out = run("--bible", str(path))
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertEqual(out["missing_sections"], [])
            self.assertEqual(out["empty_sections"], [])

    def test_missing_section_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            text = FULL_BIBLE.replace("## Recurring Motifs", "## Epilogue")
            path = write_bible(tmp, text)
            code, out = run("--bible", str(path))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertIn("Recurring Motifs", out["missing_sections"])

    def test_empty_section_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            # Logline heading remains, but its only line is replaced by an HTML
            # comment — which the scan strips, leaving the section truly empty.
            text = FULL_BIBLE.replace(
                "A weary archivist must choose between burning the last record or living inside it.",
                "<!-- still to write -->",
            )
            path = write_bible(tmp, text)
            code, out = run("--bible", str(path))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertIn("Logline", out["empty_sections"])

    def test_bare_placeholder_counts_as_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            text = FULL_BIBLE.replace(
                "A weary archivist must choose between burning the last record or living inside it.",
                "{logline — who the story is about and what they must decide}",
            )
            path = write_bible(tmp, text)
            code, out = run("--bible", str(path))
            self.assertEqual(code, 1, out)
            self.assertIn("Logline", out["empty_sections"])

    def test_and_matches_ampersand(self):
        with tempfile.TemporaryDirectory() as tmp:
            text = FULL_BIBLE.replace("## Genre & Tone", "## Genre and Tone")
            path = write_bible(tmp, text)
            code, out = run("--bible", str(path))
            self.assertEqual(code, 0, out)
            self.assertNotIn("Genre & Tone", out["missing_sections"])

    def test_missing_file_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "nope.md"
            code, out = run("--bible", str(path))
            self.assertEqual(code, 2, out)
            self.assertEqual(out["status"], "error")
            self.assertIn("not found", out["error"])

    @unittest.skipUnless(PROVEN.is_file(), "proven production Bible not present")
    def test_proven_instance_passes(self):
        code, out = run("--bible", str(PROVEN))
        self.assertEqual(code, 0, out)
        self.assertEqual(out["status"], "pass")
        self.assertEqual(out["missing_sections"], [])
        self.assertEqual(out["empty_sections"], [])


if __name__ == "__main__":
    unittest.main()

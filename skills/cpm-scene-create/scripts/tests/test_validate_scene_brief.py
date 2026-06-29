#!/usr/bin/env python3
"""Unit tests for validate_scene_brief.py — exercises the validate structural-check contract.

Runs the real script via subprocess against throwaway scene briefs in a temp project skeleton
(Bible/Characters stubs, a manifest carrying the scene block, a Slate carrying the scene row), so
checks 6 and 9 are exercised end-to-end. One test per script-owned failure mode.
Run with: python test_validate_scene_brief.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = SKILL_ROOT / "scripts" / "validate_scene_brief.py"

# A canonical, valid 6-beat brief. ASCII only (the script does not care about the dash style).
VALID_BRIEF = """\
---
scene_number: '01'
scene_id: 'SCENE_01'
scene_title: 'The Functional Ghost'
status: 'ready'
shard_count: 6
default_shard_duration: 5
on_camera_characters:
  - Elias
arc_position: 'Act I - opening scene'
created: '2026-02-21'
lastModified: '2026-02-21'
---

# Scene 01: The Functional Ghost

## Setting

- **Location:** Sedan transitioning to apartment hallway
- **Time of Day:** Late afternoon
- **Atmosphere:** Synthetic cold

## Narrative Purpose

Establish the full weight of the Cold.

**Serves theme:** The Good Soldier Complex

## Emotional Arc

- **Opens at:** Sterile isolation
- **Closes at:** Coiled spring

## Beats

### Beat Table

| Beat | Duration | Focus | Primary Requirement |
|------|----------|-------|---------------------|
| 1 | 5s | Elias - face, 85mm CU | Functional Ghost expression; Tablet Blue #5B8DD9 uplight; single RIGHT-hand swipe |
| 2 | 5s | Elias - LEFT wrist, 100mm ECU | Smartwatch countdown on LEFT wrist; RIGHT gloved index taps glass once |
| 3 | 5s | Elias - hands + paper, 85mm MCU | Repossession paper #F0F4F8 squared to 90 degrees with RIGHT index |
| 4 | 5s | Elias - full body, 35mm tracking | Plunge into System Green #8FBCAA; RIGHT thumb traces LEFT glove seam |
| 5 | 5s | Elias - full figure, 24mm wide | Metronomic march; Slate Blue #2C3E50 silhouette boxed by receding lines |
| 6 | 5s | Elias - LEFT fist + door, 85mm CU | LEFT glove curls to a fist; strikes wood exactly 3 times; zero drift |

### Beat Details

#### Beat 1 - The Asset Scan
- **Action:** Elias stares into harsh Tablet Blue light and swipes once with his RIGHT hand. He does not blink.
- **Emotional Note:** Absolute Zero.
- **Shot:** 85mm clinical close-up.
- **Continuity In:** carry-in per state/entry_contract.md.
- **State Change:** none - arc holds at 0%.

#### Beat 2 - The Metronome
- **Action:** Elias's LEFT wrist rotates up; his RIGHT gloved index finger taps the glass once.
- **Emotional Note:** Dominance without anger.
- **Shot:** 100mm extreme close-up.

#### Beat 3 - The Geometric Imposition
- **Action:** Elias squares the repossession paper to a perfect 90 degrees with his RIGHT index finger.
- **Emotional Note:** Ritual order.
- **Shot:** 85mm medium close-up.

#### Beat 4 - The Boundary Check
- **Action:** Elias steps out of the car; his RIGHT thumb traces the seam of his LEFT glove.
- **Emotional Note:** The armoring ritual.
- **Shot:** 35mm tracking, exterior to hallway.

#### Beat 5 - The March
- **Action:** Camera tracks backward as Elias marches dead-center down the hallway.
- **Emotional Note:** Geometric, inevitable, suffocating.
- **Shot:** 24mm wide, system dolly.

#### Beat 6 - The Apex of the System
- **Action:** Elias stops with zero drift and strikes the door three times with his LEFT fist.
- **Emotional Note:** The Apex.
- **Shot:** 85mm clinical close-up.
"""

CHAR_STUB = "# Character: Elias\n\n**Asset ID:** ELIAS_V1\n**Status:** ACTIVE\n"

ENTRY_CONTRACT = """\
---
scene_id: 'SCENE_01'
applies_to_shard: 1
derived_from: 'character-initial-state'
created: '2026-02-21'
---

# Entry Contract - Scene 01, Shard 1

## On-Camera Characters (carry-in)
### Elias - Bible/Characters/Elias.md (assetID ELIAS_V1)
- **Conditions (carry-in):** ACUTE_JAW_TENSION (active)
"""

# A later-scene gap stub: carries the marker phrase the script greps for.
ENTRY_CONTRACT_GAP = """\
---
scene_id: 'SCENE_01'
applies_to_shard: 1
derived_from: 'Scene_00/state/shard_last_exit_state.md'
created: '2026-02-21'
---

# Entry Contract - Scene 01, Shard 1

## On-Camera Characters (carry-in)
> unresolved - Script Supervisor fills before Shard 1
"""

MANIFEST = """\
# Project Manifest
## Test Project

### Project Status

- [x] Scenes defined

### Scenes

<!-- scene-create updates this section automatically -->

## Scene 01
- **Title:** The Functional Ghost
- **Status:** ready
- **On-Camera Characters:** Elias
- **Shard Count:** 6
- **Brief:** `Production/Scenes/Scene_01/scene-brief.md`
"""

MANIFEST_NO_SCENE = """\
# Project Manifest
## Test Project

### Scenes

<!-- scene-create updates this section automatically -->
"""

SLATE = """\
# Production Slate
## Test Project

## Scenes
| Scene | Title | Status | Shards | Brief |
|-------|-------|--------|--------|-------|
| 01 | The Functional Ghost | ready | 6 | Production/Scenes/Scene_01/scene-brief.md |

## Production Log
- 2026-02-21 - Scene 01 brief created (6 beats); status: ready.
"""

SLATE_NO_SCENE = """\
# Production Slate
## Test Project

## Scenes
| Scene | Title | Status | Shards | Brief |
|-------|-------|--------|--------|-------|

## Production Log
"""


def run(*extra) -> tuple[int, dict]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), *extra],
        capture_output=True, text=True,
    )
    payload = json.loads(proc.stdout) if proc.stdout.strip() else {}
    return proc.returncode, payload


def build_project(tmp, brief: str = VALID_BRIEF, *, write_char: bool = True,
                  write_entry: bool = True, entry_text: str = ENTRY_CONTRACT,
                  manifest: str | None = MANIFEST, slate: str | None = SLATE):
    """Lay down a tiny CPM project skeleton and return (project_root, brief_path)."""
    root = Path(tmp) / "Project"
    scene_dir = root / "Production" / "Scenes" / "Scene_01"
    (scene_dir / "state").mkdir(parents=True, exist_ok=True)
    brief_path = scene_dir / "scene-brief.md"
    brief_path.write_text(brief, encoding="utf-8")
    if write_entry:
        (scene_dir / "state" / "entry_contract.md").write_text(entry_text, encoding="utf-8")
    (root / "Bible" / "Characters").mkdir(parents=True, exist_ok=True)
    if write_char:
        (root / "Bible" / "Characters" / "Elias.md").write_text(CHAR_STUB, encoding="utf-8")
    (root / ".cpm").mkdir(parents=True, exist_ok=True)
    if manifest is not None:
        (root / ".cpm" / "manifest.md").write_text(manifest, encoding="utf-8")
    if slate is not None:
        (root / "Production" / "Slate.md").write_text(slate, encoding="utf-8")
    return root, brief_path


class ValidateSceneBriefTests(unittest.TestCase):
    def test_valid_brief_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, brief = build_project(tmp)
            code, out = run("--brief", str(brief), "--project", str(root))
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertEqual(out["issues"], [])
            self.assertTrue(out["four_way_equality"])
            self.assertTrue(out["contiguous"])
            self.assertTrue(out["columns_ok"])
            self.assertTrue(out["table_detail_match"])
            self.assertEqual(out["shard_count"], 6)
            self.assertEqual(out["beat_column"], [1, 2, 3, 4, 5, 6])
            self.assertEqual(out["missing_character_files"], [])
            self.assertTrue(out["entry_contract_present"])
            self.assertTrue(out["manifest_has_scene"])
            self.assertTrue(out["slate_has_scene"])

    def test_project_root_inferred_when_omitted(self):
        # No --project supplied: the project root is inferred from the brief path.
        with tempfile.TemporaryDirectory() as tmp:
            _root, brief = build_project(tmp)
            code, out = run("--brief", str(brief))  # no --project
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")

    def test_noncontiguous_beats_holds(self):
        # Beat 6 renamed to 7 in both table and detail -> column is {1,2,3,4,5,7}, not contiguous.
        brief = VALID_BRIEF.replace("| 6 | 5s |", "| 7 | 5s |").replace("#### Beat 6 -", "#### Beat 7 -")
        with tempfile.TemporaryDirectory() as tmp:
            root, brief_path = build_project(tmp, brief=brief)
            code, out = run("--brief", str(brief_path), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["contiguous"])

    def test_table_detail_mismatch_holds(self):
        # Drop the Beat 6 detail block; the table row stays -> 6 rows, 5 detail blocks.
        brief = VALID_BRIEF.split("#### Beat 6")[0]
        with tempfile.TemporaryDirectory() as tmp:
            root, brief_path = build_project(tmp, brief=brief)
            code, out = run("--brief", str(brief_path), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["table_detail_match"])
            self.assertEqual(out["beat_table_rows"], 6)
            self.assertEqual(out["beat_detail_blocks"], 5)

    def test_shard_count_drift_holds(self):
        brief = VALID_BRIEF.replace("shard_count: 6", "shard_count: 5")
        with tempfile.TemporaryDirectory() as tmp:
            root, brief_path = build_project(tmp, brief=brief)
            code, out = run("--brief", str(brief_path), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["four_way_equality"])
            self.assertTrue(any("four-way" in i for i in out["issues"]))

    def test_wrong_columns_holds(self):
        brief = VALID_BRIEF.replace(
            "| Beat | Duration | Focus | Primary Requirement |",
            "| Beat | Duration | Focus | Requirement |")
        with tempfile.TemporaryDirectory() as tmp:
            root, brief_path = build_project(tmp, brief=brief)
            code, out = run("--brief", str(brief_path), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["columns_ok"])

    def test_scene_id_mismatch_holds(self):
        brief = VALID_BRIEF.replace("scene_id: 'SCENE_01'", "scene_id: 'SCENE_02'")
        with tempfile.TemporaryDirectory() as tmp:
            root, brief_path = build_project(tmp, brief=brief)
            code, out = run("--brief", str(brief_path), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertTrue(any("scene_id" in i for i in out["issues"]))

    def test_bad_scene_number_padding_holds(self):
        # Keep scene_id consistent so only the padding rule fires.
        brief = (VALID_BRIEF
                 .replace("scene_number: '01'", "scene_number: '1'")
                 .replace("scene_id: 'SCENE_01'", "scene_id: 'SCENE_1'"))
        with tempfile.TemporaryDirectory() as tmp:
            root, brief_path = build_project(tmp, brief=brief)
            code, out = run("--brief", str(brief_path), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertTrue(any("zero-padded" in i or "scene_number" in i for i in out["issues"]))

    def test_missing_canonical_field_holds(self):
        # Drop a canonical frontmatter field (status): the brief is no longer well-formed -> hold.
        brief = VALID_BRIEF.replace("status: 'ready'\n", "")
        with tempfile.TemporaryDirectory() as tmp:
            root, brief_path = build_project(tmp, brief=brief)
            code, out = run("--brief", str(brief_path), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertTrue(any("status" in i for i in out["issues"]))

    def test_bad_duration_holds(self):
        brief = VALID_BRIEF.replace("| 5s |", "| 7s |", 1)  # Beat 1 only
        with tempfile.TemporaryDirectory() as tmp:
            root, brief_path = build_project(tmp, brief=brief)
            code, out = run("--brief", str(brief_path), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertTrue(any("Duration" in i for i in out["issues"]))

    def test_missing_character_file_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, brief = build_project(tmp, write_char=False)
            code, out = run("--brief", str(brief), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertIn("Elias", out["missing_character_files"])

    def test_inline_list_characters_resolve(self):
        # on_camera_characters as an inline list [Elias, Mara]: Elias resolves, Mara is absent.
        # Exercises the inline-list parse branch (block-list form is covered everywhere else).
        brief = VALID_BRIEF.replace("on_camera_characters:\n  - Elias",
                                    "on_camera_characters: [Elias, Mara]")
        with tempfile.TemporaryDirectory() as tmp:
            root, brief_path = build_project(tmp, brief=brief)  # writes Elias.md, not Mara.md
            code, out = run("--brief", str(brief_path), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertEqual(out["missing_character_files"], ["Mara"])

    def test_missing_entry_contract_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, brief = build_project(tmp, write_entry=False)
            code, out = run("--brief", str(brief), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["entry_contract_present"])

    def test_missing_manifest_scene_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, brief = build_project(tmp, manifest=MANIFEST_NO_SCENE)
            code, out = run("--brief", str(brief), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["manifest_has_scene"])

    def test_missing_slate_scene_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, brief = build_project(tmp, slate=SLATE_NO_SCENE)
            code, out = run("--brief", str(brief), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["slate_has_scene"])

    def test_entry_contract_gap_warns_not_holds(self):
        # The later-scene gap stub is non-blocking: PASS with a warning, never a hold.
        with tempfile.TemporaryDirectory() as tmp:
            root, brief = build_project(tmp, entry_text=ENTRY_CONTRACT_GAP)
            code, out = run("--brief", str(brief), "--project", str(root))
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertEqual(out["issues"], [])
            self.assertTrue(out["warnings"])
            self.assertTrue(any("gap stub" in w for w in out["warnings"]))

    def test_missing_brief_file_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "nope.md"
            code, out = run("--brief", str(missing))
            self.assertEqual(code, 2)
            self.assertEqual(out["status"], "error")
            self.assertIn("scene brief not found", out["error"])


if __name__ == "__main__":
    unittest.main()

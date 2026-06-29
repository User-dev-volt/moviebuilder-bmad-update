#!/usr/bin/env python3
"""Unit tests for validate_shard.py — exercises the structural-check contract for a shard.

Three kinds of coverage:
  * a read-only positive run against the PROVEN Scene_01_Shard_1 prompt + exit state (skipped
    if that project is not present), confirming the structure round-trips;
  * a positive run against a clean, self-contained project laid down in a temp dir, whose
    scene-brief is the authored fixtures/scene-brief.md — this exercises the Beat Table
    cross-checks on the PASS path;
  * one negative case per script-owned failure mode and per exit code, each built from a mutated
    copy in a throwaway temp dir so the proven project is never touched.

Run with: python test_validate_shard.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = SKILL_ROOT / "scripts" / "validate_shard.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"
REPO_ROOT = SKILL_ROOT.parents[1]
PROVEN = REPO_ROOT / "_bmad-output" / "cpm-projects" / "The Second Receipt"
PROVEN_PROMPT = PROVEN / "Output" / "Prompts" / "Scene_01_Shard_1_prompt.md"

# The authored scene brief that carries a machine-readable Beat Table, so it drives the
# cross-checks on the PASS path. Beat 1 is 5s, beat 4 is 15s, beat 5 is 30s — the full {5,15,30} range.
BRIEF_WITH_TABLE = (FIXTURES / "scene-brief.md").read_text(encoding="utf-8")

# An older brief shape: real frontmatter (with shard_count) but no Beat Table. The cross-checks
# must degrade around it with a warning, never a hold.
BRIEF_NO_TABLE = """\
---
scene_number: '01'
scene_id: 'SCENE_01'
status: not-started
shard_count: 6
on_camera_characters:
  - Elias
---

# Scene 01: The Functional Ghost

## Beats

### Shard 1 - The Asset Scan
- **Action:** Elias stares into harsh Tablet Blue light and swipes once with his RIGHT hand.
- **Character Focus:** Elias - 85mm clinical close-up on face.
- **Emotional Note:** Absolute Zero.
"""

# Distinctive, short action/environment lines so the out-of-order test can swap them exactly.
ACTION_BLOCK = ("[Action/State]:\n"
                "Subject performs a single precise RIGHT-hand swipe below frame.")
ENV_BLOCK = ("[Environment/Lighting]:\n"
             "Primary harsh #5B8DD9 uplight from below; #0B101A void on the dark half.")

PROMPT = f"""\
---
sceneNumber: '01'
shardNumber: '1'
beatName: 'THE_ASSET_SCAN'
generatedDate: '2026-02-21'
agentInputs:
  showrunner: true
  cinematographer: true
  scriptSupervisor: true
  promptEngineer: true
stateDiffPassed: true
---

[ID: SCENE_01.1_THE_ASSET_SCAN]

[Technical Header]:
85mm clinical close-up, 24fps, harsh #5B8DD9 digital tablet uplight from below.

[Subject/Asset]:
[ANCHOR POINT] Faint white crescent scar on RIGHT lower jawline. [CRITICAL] Functional Ghost expression.

{ACTION_BLOCK}

{ENV_BLOCK}

[Temporal Constraint]:
5 seconds. Heavy rails dolly, zero breath. Shot ends with the face dead-center, expression intact.

---

**Build Notes:**
- Anchor Points: RIGHT jawline scar, Functional Ghost expression [CRITICAL]
- Vocabulary Compliance: "cold lighting" -> "harsh #5B8DD9 digital tablet uplight"
- Exit Hook: face dead-center, gaze toward #5B8DD9 source, positioned for Shard 2
- Injections Applied: RIGHT jawline scar; unblinking mandate
- Source Agents: Showrunner -> Cinematographer -> Script Supervisor -> Prompt Engineer
"""

EXIT_STATE = """\
---
sceneNumber: '01'
shardNumber: '1'
generatedDate: '2026-02-21'
generatedBy: 'shard-generation-ritual'
---

# Exit State: Scene 01, Shard 1

## Character States

### Elias

- **Position:** Dead-center frame, 85mm clinical close-up
- **Facing:** Slight downward gaze toward off-screen #5B8DD9 source
- **Expression:** Functional Ghost - jaw clenched, mouth a firm horizontal line
- **Action:** Returns to absolute stillness; RIGHT gloved hand off-screen
- **Holding:** Tablet (LEFT hand, off-screen below frame)
- **Physical Condition:** ACUTE_JAW_TENSION active. Arc progress: 0%.

## Environment State

- **Lighting Position:** #5B8DD9 uplight, single source from below, steady mid-intensity
- **Time Progression:** Late afternoon; interior sedan, no ambient change this shard
- **Active Environmental Elements:** Sealed sedan cab; #0B101A void background

## Entry Contract for Next Shard

### MUST Start With:
- Same sealed sedan interior; same #5B8DD9 uplight position below frame
- Elias dead-center, Functional Ghost expression intact from previous shard

### MUST NOT Show:
- Elias blinking - any single blink breaks The Metronome beat
- Any warm light source entering the sedan

## State Changes This Shard

| Element | Previous Value | New Value | Reason |
|---------|---------------|-----------|--------|
| Arc progress | 0% | 0% | No thaw initiated; Absolute Zero baseline established |

## Active Contracts

| Contract ID | Status | Notes |
|-------------|--------|-------|
| (none) | - | Shard 1 is pre-contract ground. |
"""

# A final-shard exit state: no next-shard contract owed, so the Entry Contract section is absent.
EXIT_FINAL = """\
---
sceneNumber: '01'
shardNumber: '6'
generatedDate: '2026-02-21'
generatedBy: 'shard-generation-ritual'
---

# Exit State: Scene 01, Shard 6

## Character States

### Elias

- **Position:** Squared to the numbered door, LEFT fist raised
- **Facing:** Forward, into the door
- **Expression:** The Apex - armor fully locked
- **Action:** LEFT fist has struck the door three times; arm returning
- **Holding:** Repossession order (RIGHT hand, off-screen)
- **Physical Condition:** THERMAL_RIGIDITY active. Arc progress: 0%.

## Environment State

- **Lighting Position:** System Green #8FBCAA hallway fluorescent, overhead, high intensity
- **Time Progression:** Late afternoon; hallway
- **Active Environmental Elements:** Cinderblock hallway; numbered door at the vanishing point

## State Changes This Shard

| Element | Previous Value | New Value | Reason |
|---------|---------------|-----------|--------|
| Door | Untouched | Struck three times | Elias knocks to open the repossession |

## Active Contracts

| Contract ID | Status | Notes |
|-------------|--------|-------|
| (none) | - | The scene closes on the knock. |
"""


def run(*extra) -> tuple[int, dict]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), *extra],
        capture_output=True, text=True,
    )
    payload = json.loads(proc.stdout) if proc.stdout.strip() else {}
    return proc.returncode, payload


def build_project(tmp, *, prompt: str = PROMPT, exit_state: str | None = EXIT_STATE,
                  brief: str | None = BRIEF_WITH_TABLE, shard: int = 1):
    """Lay down a tiny CPM project skeleton and return (project_root, prompt_path)."""
    root = Path(tmp) / "Project"
    scene = root / "Production" / "Scenes" / "Scene_01"
    (scene / "state").mkdir(parents=True, exist_ok=True)
    (root / "Output" / "Prompts").mkdir(parents=True, exist_ok=True)
    prompt_path = root / "Output" / "Prompts" / f"Scene_01_Shard_{shard}_prompt.md"
    prompt_path.write_text(prompt, encoding="utf-8")
    if exit_state is not None:
        (scene / "state" / f"shard_{shard}_exit_state.md").write_text(exit_state, encoding="utf-8")
    if brief is not None:
        (scene / "scene-brief.md").write_text(brief, encoding="utf-8")
    return root, prompt_path


class ValidateShardTests(unittest.TestCase):
    # ---- positive: the proven artifact (read-only) ----
    def test_proven_prompt_passes(self):
        if not PROVEN_PROMPT.is_file():
            self.skipTest(f"proven prompt not present at {PROVEN_PROMPT}")
        code, out = run("--prompt", str(PROVEN_PROMPT), "--project", str(PROVEN))
        self.assertEqual(code, 0, out)
        self.assertEqual(out["status"], "pass")
        self.assertEqual(out["issues"], [])
        self.assertTrue(out["state_diff_passed"])
        self.assertTrue(out["agent_inputs_ok"])
        self.assertTrue(out["prompt_sections_ok"])
        self.assertEqual(out["temporal_duration"], 5)
        self.assertTrue(out["exit_state_present"])
        self.assertTrue(out["exit_state_identity_match"])
        self.assertTrue(out["exit_state_sections_ok"])
        # The proven project carries an older brief shape (no Beat Table): degrade with a warning.
        self.assertFalse(out["scene_brief_checked"])
        self.assertTrue(out["warnings"])

    # ---- positive: a clean brief-with-Beat-Table project exercises the cross-checks ----
    def test_beat_table_crosschecks_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, prompt = build_project(tmp)
            code, out = run("--prompt", str(prompt), "--project", str(root))
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertEqual(out["issues"], [])
            self.assertEqual(out["warnings"], [])
            self.assertTrue(out["scene_brief_checked"])
            self.assertEqual(out["shard_count"], 6)
            self.assertTrue(out["shard_in_range"])
            self.assertTrue(out["beat_in_table"])
            self.assertEqual(out["beat_duration"], 5)
            self.assertTrue(out["duration_matches_beat"])

    def test_project_inferred_when_omitted(self):
        with tempfile.TemporaryDirectory() as tmp:
            _root, prompt = build_project(tmp)
            code, out = run("--prompt", str(prompt))  # no --project
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertTrue(out["scene_brief_checked"])

    # ---- check 1: prompt frontmatter completeness ----
    def test_missing_frontmatter_field_holds(self):
        prompt = PROMPT.replace("beatName: 'THE_ASSET_SCAN'\n", "")
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, prompt=prompt)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertTrue(any("beatName" in i for i in out["issues"]))

    # ---- check 2: stateDiffPassed must be true ----
    def test_state_diff_false_holds(self):
        prompt = PROMPT.replace("stateDiffPassed: true", "stateDiffPassed: false")
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, prompt=prompt)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["state_diff_passed"])
            self.assertTrue(any("stateDiffPassed" in i for i in out["issues"]))

    # ---- check 3: all four agent inputs true ----
    def test_agent_input_false_holds(self):
        prompt = PROMPT.replace("promptEngineer: true", "promptEngineer: false")
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, prompt=prompt)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["agent_inputs_ok"])
            self.assertTrue(any("promptEngineer" in i for i in out["issues"]))

    # ---- check 4: the six bracketed sections present ----
    def test_missing_section_holds(self):
        prompt = PROMPT.replace("[Action/State]:", "[Removed]:")
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, prompt=prompt)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["prompt_sections_ok"])
            self.assertTrue(any("Action/State" in i for i in out["issues"]))

    # ---- check 4: the six bracketed sections in order ----
    def test_sections_out_of_order_holds(self):
        prompt = PROMPT.replace(f"{ACTION_BLOCK}\n\n{ENV_BLOCK}",
                                f"{ENV_BLOCK}\n\n{ACTION_BLOCK}")
        self.assertNotEqual(prompt, PROMPT)  # the swap actually happened
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, prompt=prompt)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["prompt_sections_ok"])
            self.assertTrue(any("out of order" in i for i in out["issues"]))

    # ---- check 5: temporal duration in {5, 15, 30} ----
    def test_bad_temporal_duration_holds(self):
        prompt = PROMPT.replace("5 seconds.", "7 seconds.")
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, prompt=prompt)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertEqual(out["temporal_duration"], 7)
            self.assertFalse(out["temporal_duration_ok"])

    # ---- check 6: sibling exit state must exist ----
    def test_missing_exit_state_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, exit_state=None)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["exit_state_present"])

    # ---- check 6: exit-state identity must match the prompt ----
    def test_exit_identity_mismatch_holds(self):
        exit_state = EXIT_STATE.replace("shardNumber: '1'", "shardNumber: '2'")
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, exit_state=exit_state)  # file still shard_1
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["exit_state_identity_match"])

    # ---- check 7: exit-state core sections required ----
    def test_exit_missing_core_section_holds(self):
        exit_state = EXIT_STATE.split("## Active Contracts")[0]
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, exit_state=exit_state)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["exit_state_sections_ok"])
            self.assertTrue(any("Active Contracts" in i for i in out["issues"]))

    # ---- check 7/9: a non-final shard needs a non-empty entry contract ----
    def test_nonfinal_empty_entry_contract_holds(self):
        exit_state = EXIT_STATE.replace(
            "### MUST Start With:\n"
            "- Same sealed sedan interior; same #5B8DD9 uplight position below frame\n"
            "- Elias dead-center, Functional Ghost expression intact from previous shard\n",
            "### MUST Start With:\n")
        self.assertNotEqual(exit_state, EXIT_STATE)
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, exit_state=exit_state)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertTrue(out["entry_contract_required"])
            self.assertFalse(out["entry_contract_ok"])
            self.assertTrue(any("MUST Start With" in i for i in out["issues"]))

    # ---- finality: the last shard owes no entry contract ----
    def test_final_shard_without_entry_contract_passes(self):
        prompt = PROMPT.replace("shardNumber: '1'", "shardNumber: '6'")
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, prompt=prompt, exit_state=EXIT_FINAL, shard=6)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertFalse(out["entry_contract_required"])
            self.assertTrue(out["entry_contract_ok"])
            self.assertTrue(out["scene_brief_checked"])

    # ---- check 8: shard number outside the Beat Table range ----
    def test_shard_out_of_range_holds(self):
        prompt = PROMPT.replace("shardNumber: '1'", "shardNumber: '9'")
        exit_state = EXIT_STATE.replace("shardNumber: '1'", "shardNumber: '9'")
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, prompt=prompt, exit_state=exit_state, shard=9)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertTrue(out["scene_brief_checked"])
            self.assertFalse(out["shard_in_range"])
            self.assertFalse(out["beat_in_table"])

    # ---- check 8: prompt duration must match the beat's Duration ----
    def test_duration_mismatch_with_beat_holds(self):
        prompt = PROMPT.replace("5 seconds.", "15 seconds.")  # beat 1 is 5s in the brief
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, prompt=prompt)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertEqual(out["temporal_duration"], 15)
            self.assertEqual(out["beat_duration"], 5)
            self.assertFalse(out["duration_matches_beat"])

    # ---- variable intervals: positive 15s round-trip (beat 4) ----
    def test_beat_15s_positive_roundtrip(self):
        prompt = (PROMPT
                  .replace("shardNumber: '1'", "shardNumber: '4'")
                  .replace("beatName: 'THE_ASSET_SCAN'", "beatName: 'THE_BOUNDARY_CHECK'")
                  .replace("[ID: SCENE_01.1_THE_ASSET_SCAN]", "[ID: SCENE_01.4_THE_BOUNDARY_CHECK]")
                  .replace("5 seconds.", "15 seconds."))
        exit_state = (EXIT_STATE
                      .replace("shardNumber: '1'", "shardNumber: '4'")
                      .replace("Scene 01, Shard 1", "Scene 01, Shard 4"))
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, prompt=prompt, exit_state=exit_state, shard=4)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertEqual(out["issues"], [])
            self.assertTrue(out["scene_brief_checked"])
            self.assertEqual(out["temporal_duration"], 15)
            self.assertEqual(out["beat_duration"], 15)
            self.assertTrue(out["duration_matches_beat"])

    # ---- variable intervals: positive 30s round-trip (beat 5) ----
    def test_beat_30s_positive_roundtrip(self):
        prompt = (PROMPT
                  .replace("shardNumber: '1'", "shardNumber: '5'")
                  .replace("beatName: 'THE_ASSET_SCAN'", "beatName: 'THE_MARCH'")
                  .replace("[ID: SCENE_01.1_THE_ASSET_SCAN]", "[ID: SCENE_01.5_THE_MARCH]")
                  .replace("5 seconds.", "30 seconds."))
        exit_state = (EXIT_STATE
                      .replace("shardNumber: '1'", "shardNumber: '5'")
                      .replace("Scene 01, Shard 1", "Scene 01, Shard 5"))
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, prompt=prompt, exit_state=exit_state, shard=5)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertEqual(out["issues"], [])
            self.assertTrue(out["scene_brief_checked"])
            self.assertEqual(out["temporal_duration"], 30)
            self.assertEqual(out["beat_duration"], 30)
            self.assertTrue(out["duration_matches_beat"])

    # ---- check 8: graceful degradation around an older brief shape ----
    def test_degraded_brief_warns_not_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, brief=BRIEF_NO_TABLE)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertEqual(out["issues"], [])
            self.assertFalse(out["scene_brief_checked"])
            self.assertIsNone(out["shard_in_range"])
            self.assertTrue(out["warnings"])

    def test_missing_brief_warns_not_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, p = build_project(tmp, brief=None)
            code, out = run("--prompt", str(p), "--project", str(root))
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertFalse(out["scene_brief_checked"])
            self.assertTrue(out["warnings"])

    # ---- exit code 2: the prompt file must exist ----
    def test_missing_prompt_file_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "nope.md"
            code, out = run("--prompt", str(missing))
            self.assertEqual(code, 2)
            self.assertEqual(out["status"], "error")
            self.assertIn("compiled prompt not found", out["error"])


if __name__ == "__main__":
    unittest.main()

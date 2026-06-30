#!/usr/bin/env python3
"""Unit tests for validate_handshake.py — the structural floor for one continuity boundary.

Three kinds of coverage:
  * a positive run against the AUTHORED adjacent pair (shard 1 -> shard 2 of Scene 07), laid down
    in a temp project, confirming the PASS path round-trips and every token survives into B;
  * one negative case per script-owned failure mode (drop the object, flip the hand, drop the
    feature's LEFT/RIGHT specificity, wrong framing, wrong/absent signature hex, a MUST-NOT-Show
    token present, identity mismatch, non-adjacent shards, an empty entry contract, B not yet
    generated), each built by mutating an in-memory COPY so the fixtures are never touched;
  * the graceful paths — a final shard reported as NO-BOUNDARY, a degraded (brief-less) finality
    fallback that warns rather than holds — and the usage-error exit code (missing file => 2).

A read-only run against the proven project is included too: it has only one shard, so its single
boundary correctly HOLDS with "shard B ... not found" — exactly the one-shard reality.

Run with: python test_validate_handshake.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = SKILL_ROOT / "scripts" / "validate_handshake.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"
REPO_ROOT = SKILL_ROOT.parents[1]
PROVEN = REPO_ROOT / "_bmad-output" / "cpm-projects" / "The Second Receipt"

# The authored adjacent pair — the single source of truth. Every mutation below works on a COPY
# of these strings, written into a throwaway temp project, so the fixture files stay pristine.
A_EXIT = (FIXTURES / "shard_1_exit_state.md").read_text(encoding="utf-8")
A_PROMPT = (FIXTURES / "Scene_07_Shard_1_prompt.md").read_text(encoding="utf-8")
B_EXIT = (FIXTURES / "shard_2_exit_state.md").read_text(encoding="utf-8")
B_PROMPT = (FIXTURES / "Scene_07_Shard_2_prompt.md").read_text(encoding="utf-8")
BRIEF = (FIXTURES / "scene-brief.md").read_text(encoding="utf-8")

# The exact MUST Start With bullet block, so the empty-contract negative can excise it precisely.
START_BLOCK = (
    "### MUST Start With:\n"
    "- Hero still holding the [Asset: Brass_Key] in his RIGHT hand, raised to chest height\n"
    "- The pale crescent scar along Hero's LEFT jaw, unchanged from the previous shard\n"
    "- 85mm framing with Hero held at frame-left, squared to the door\n"
)


def run(*extra) -> tuple[int, dict]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), *extra],
        capture_output=True, text=True,
    )
    payload = json.loads(proc.stdout) if proc.stdout.strip() else {}
    return proc.returncode, payload


def build_project(tmp, *, exit_a: str | None = A_EXIT, prompt_b: str | None = B_PROMPT,
                  exit_b: str | None = B_EXIT, prompt_a: str | None = A_PROMPT,
                  brief: str | None = BRIEF, scene: str = "07"):
    """Lay the authored pair into a tiny CPM project skeleton; return the project root."""
    root = Path(tmp) / "Project"
    scene_dir = root / "Production" / "Scenes" / f"Scene_{scene}"
    (scene_dir / "state").mkdir(parents=True, exist_ok=True)
    (root / "Output" / "Prompts").mkdir(parents=True, exist_ok=True)
    if exit_a is not None:
        (scene_dir / "state" / "shard_1_exit_state.md").write_text(exit_a, encoding="utf-8")
    if exit_b is not None:
        (scene_dir / "state" / "shard_2_exit_state.md").write_text(exit_b, encoding="utf-8")
    if prompt_a is not None:
        (root / "Output" / "Prompts" / f"Scene_{scene}_Shard_1_prompt.md").write_text(
            prompt_a, encoding="utf-8")
    if prompt_b is not None:
        (root / "Output" / "Prompts" / f"Scene_{scene}_Shard_2_prompt.md").write_text(
            prompt_b, encoding="utf-8")
    if brief is not None:
        (scene_dir / "scene-brief.md").write_text(brief, encoding="utf-8")
    return root


class ValidateHandshakeTests(unittest.TestCase):
    # ---- positive: the authored adjacent pair passes every floor check ----
    def test_authored_pair_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build_project(tmp)
            code, out = run("--project", str(root), "--scene", "07", "--shard-a", "1")
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertEqual(out["issues"], [])
            self.assertEqual(out["warnings"], [])
            self.assertTrue(out["boundary_testable"])
            self.assertFalse(out["a_is_final"])
            self.assertEqual(out["finality_source"], "scene_brief")
            self.assertTrue(out["entry_contract_nonempty"])
            self.assertTrue(out["scene_match"])
            self.assertTrue(out["adjacent"])
            self.assertEqual(out["must_start_missing"], [])
            self.assertEqual(out["must_not_violations"], [])
            self.assertEqual(out["signature_hex"], "#3FA7D6")
            self.assertTrue(out["signature_hex_in_b_lighting"])
            for tok in ("asset:Brass_Key", "hand:RIGHT", "hand:LEFT", "lens:85mm"):
                self.assertIn(tok, out["must_start_with_tokens"])
                self.assertIn(tok, out["must_start_present"])

    # ---- override flags wire to the same result ----
    def test_explicit_path_overrides_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build_project(tmp)
            exit_a = root / "Production" / "Scenes" / "Scene_07" / "state" / "shard_1_exit_state.md"
            prompt_b = root / "Output" / "Prompts" / "Scene_07_Shard_2_prompt.md"
            brief = root / "Production" / "Scenes" / "Scene_07" / "scene-brief.md"
            code, out = run("--project", str(root), "--scene", "07", "--shard-a", "1",
                            "--exit-a", str(exit_a), "--prompt-b", str(prompt_b),
                            "--brief", str(brief))
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertEqual(out["issues"], [])

    # ---- finality: the scene's final shard owes no contract => not a testable boundary ----
    def test_final_shard_reports_no_boundary(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build_project(tmp)
            code, out = run("--project", str(root), "--scene", "07", "--shard-a", "2")
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "no_boundary")
            self.assertFalse(out["boundary_testable"])
            self.assertTrue(out["a_is_final"])
            self.assertEqual(out["finality_source"], "scene_brief")
            self.assertEqual(out["issues"], [])

    # ---- criterion 1: carried object dropped from B ----
    def test_drop_object_holds(self):
        prompt_b = B_PROMPT.replace("[Asset: Brass_Key]", "the small key")
        self.assertNotEqual(prompt_b, B_PROMPT)
        with tempfile.TemporaryDirectory() as tmp:
            root = build_project(tmp, prompt_b=prompt_b)
            code, out = run("--project", str(root), "--scene", "07", "--shard-a", "1")
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertTrue(any("Brass_Key" in t for t in out["must_start_missing"]))

    # ---- criterion 1: object present but in the wrong hand (RIGHT -> LEFT) ----
    def test_flip_hand_holds(self):
        prompt_b = B_PROMPT.replace("RIGHT", "LEFT")
        self.assertNotEqual(prompt_b, B_PROMPT)
        with tempfile.TemporaryDirectory() as tmp:
            root = build_project(tmp, prompt_b=prompt_b)
            code, out = run("--project", str(root), "--scene", "07", "--shard-a", "1")
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertTrue(any("RIGHT" in t for t in out["must_start_missing"]))

    # ---- criterion 2: distinctive-feature LEFT/RIGHT specificity dropped from B ----
    def test_drop_feature_holds(self):
        prompt_b = B_PROMPT.replace("LEFT", "left")  # the only uppercase LEFT carries the scar side
        self.assertNotEqual(prompt_b, B_PROMPT)
        with tempfile.TemporaryDirectory() as tmp:
            root = build_project(tmp, prompt_b=prompt_b)
            code, out = run("--project", str(root), "--scene", "07", "--shard-a", "1")
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertTrue(any("LEFT" in t for t in out["must_start_missing"]))

    # ---- criterion 4: spatial framing dropped from B ----
    def test_wrong_position_holds(self):
        prompt_b = B_PROMPT.replace("85mm", "35mm")
        self.assertNotEqual(prompt_b, B_PROMPT)
        with tempfile.TemporaryDirectory() as tmp:
            root = build_project(tmp, prompt_b=prompt_b)
            code, out = run("--project", str(root), "--scene", "07", "--shard-a", "1")
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertTrue(any("85mm" in t for t in out["must_start_missing"]))

    # ---- criterion 3: signature lighting hex absent from B's [Environment/Lighting] ----
    def test_wrong_signature_hex_holds(self):
        prompt_b = B_PROMPT.replace("#3FA7D6", "#999999")
        self.assertNotEqual(prompt_b, B_PROMPT)
        with tempfile.TemporaryDirectory() as tmp:
            root = build_project(tmp, prompt_b=prompt_b)
            code, out = run("--project", str(root), "--scene", "07", "--shard-a", "1")
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["signature_hex_in_b_lighting"])
            self.assertTrue(any("#3FA7D6" in i for i in out["issues"]))

    # ---- the MUST-NOT-Show floor: a forbidden token appears in B ----
    def test_forbidden_token_present_holds(self):
        prompt_b = B_PROMPT.replace("flat #0B0E14 void",
                                    "flat #0B0E14 void, with a stray #FFB000 warm spill")
        self.assertNotEqual(prompt_b, B_PROMPT)
        with tempfile.TemporaryDirectory() as tmp:
            root = build_project(tmp, prompt_b=prompt_b)
            code, out = run("--project", str(root), "--scene", "07", "--shard-a", "1")
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertTrue(any("#FFB000" in t for t in out["must_not_violations"]))

    # ---- identity: B names a different scene ----
    def test_identity_mismatch_holds(self):
        prompt_b = B_PROMPT.replace("sceneNumber: '07'", "sceneNumber: '02'")
        self.assertNotEqual(prompt_b, B_PROMPT)
        with tempfile.TemporaryDirectory() as tmp:
            root = build_project(tmp, prompt_b=prompt_b)
            code, out = run("--project", str(root), "--scene", "07", "--shard-a", "1")
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["scene_match"])
            self.assertTrue(any("identity mismatch" in i for i in out["issues"]))

    # ---- adjacency: B is not shard N+1 ----
    def test_non_adjacent_holds(self):
        prompt_b = B_PROMPT.replace("shardNumber: '2'", "shardNumber: '5'")
        self.assertNotEqual(prompt_b, B_PROMPT)
        with tempfile.TemporaryDirectory() as tmp:
            root = build_project(tmp, prompt_b=prompt_b)
            code, out = run("--project", str(root), "--scene", "07", "--shard-a", "1")
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["adjacent"])
            self.assertTrue(any("not adjacent" in i for i in out["issues"]))

    # ---- a non-final shard that handed an empty contract has nothing to handshake ----
    def test_empty_entry_contract_holds(self):
        exit_a = A_EXIT.replace(START_BLOCK, "### MUST Start With:\n")
        self.assertNotEqual(exit_a, A_EXIT)
        with tempfile.TemporaryDirectory() as tmp:
            root = build_project(tmp, exit_a=exit_a)
            code, out = run("--project", str(root), "--scene", "07", "--shard-a", "1")
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["entry_contract_nonempty"])
            self.assertTrue(any("Entry Contract" in i for i in out["issues"]))

    # ---- B prompt not yet generated: a hold, with the fix named ----
    def test_b_prompt_missing_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build_project(tmp, prompt_b=None)
            code, out = run("--project", str(root), "--scene", "07", "--shard-a", "1")
            self.assertEqual(code, 1, out)
            self.assertEqual(out["status"], "hold")
            self.assertFalse(out["b_present"])
            self.assertTrue(any("not found" in i for i in out["issues"]))

    # ---- graceful degradation: no machine-readable brief => finality falls back, warns ----
    def test_degraded_brief_warns_not_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build_project(tmp, brief=None)
            code, out = run("--project", str(root), "--scene", "07", "--shard-a", "1")
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertEqual(out["issues"], [])
            self.assertEqual(out["finality_source"], "entry_contract_presence")
            self.assertTrue(out["warnings"])

    # ---- read-only: the proven project has one shard, so its boundary holds (B never generated) ----
    def test_proven_boundary_holds_b_not_generated(self):
        proven_exit = PROVEN / "Production" / "Scenes" / "Scene_01" / "state" / "shard_1_exit_state.md"
        if not proven_exit.is_file():
            self.skipTest(f"proven project not present at {PROVEN}")
        code, out = run("--project", str(PROVEN), "--scene", "01", "--shard-a", "1")
        self.assertEqual(code, 1, out)
        self.assertEqual(out["status"], "hold")
        self.assertTrue(out["entry_contract_nonempty"])
        self.assertFalse(out["b_present"])
        self.assertTrue(any("not found" in i for i in out["issues"]))

    # ---- exit code 2: shard A's exit state must exist ----
    def test_missing_a_exit_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build_project(tmp)
            code, out = run("--project", str(root), "--scene", "07", "--shard-a", "3")
            self.assertEqual(code, 2)
            self.assertEqual(out["status"], "error")
            self.assertIn("shard A exit state not found", out["error"])


if __name__ == "__main__":
    unittest.main()

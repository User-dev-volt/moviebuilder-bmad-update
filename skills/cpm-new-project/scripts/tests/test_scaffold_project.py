#!/usr/bin/env python3
"""Unit tests for scaffold_project.py — exercises the create/update/validate CLI contract.

Runs the real script against the real templates and methodology asset bundled in the
skill, into a throwaway temp directory. Run with: python test_scaffold_project.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = SKILL_ROOT / "scripts" / "scaffold_project.py"
ASSETS = SKILL_ROOT / "assets"

CONFIG_TEMPLATE = ASSETS / "config-template.yaml"
MANIFEST_TEMPLATE = ASSETS / "manifest-template.md"
SLATE_TEMPLATE = ASSETS / "slate-template.md"
METHODOLOGY = ASSETS / "cpm-methodology.excalidraw"

REQUIRED_DIRS = [
    ".cpm", ".cpm/agents",
    "Bible", "Bible/Characters", "Bible/World",
    "Architecture",
    "Production", "Production/Scenes", "Production/Contracts",
    "Output", "Output/Prompts", "Output/Renders",
    "Diagrams",
]
REQUIRED_FILES = [
    ".cpm/config.yaml", ".cpm/manifest.md",
    "Production/Slate.md", "Diagrams/cpm-methodology.excalidraw",
]


def run(*extra) -> tuple[int, dict]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), *extra],
        capture_output=True, text=True,
    )
    payload = json.loads(proc.stdout) if proc.stdout.strip() else {}
    return proc.returncode, payload


def create_args(project: Path) -> list[str]:
    return [
        "--mode", "create", "--project-path", str(project),
        "--project-name", "The Test Reel", "--model-target", "sora",
        "--shard-duration", "5", "--max-shard-duration", "30",
        "--config-template", str(CONFIG_TEMPLATE),
        "--manifest-template", str(MANIFEST_TEMPLATE),
        "--slate-template", str(SLATE_TEMPLATE),
        "--methodology-src", str(METHODOLOGY),
    ]


class ScaffoldProjectTests(unittest.TestCase):
    def test_create_then_validate_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "The Test Reel"
            code, out = run(*create_args(project))
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "created")
            for d in REQUIRED_DIRS:
                self.assertTrue((project / d).is_dir(), f"missing dir {d}")
            for f in REQUIRED_FILES:
                self.assertTrue((project / f).is_file(), f"missing file {f}")

            # Empty leaf dirs carry a .gitkeep so the skeleton survives version control.
            for d in [".cpm/agents", "Bible/Characters", "Bible/World", "Architecture",
                      "Production/Scenes", "Production/Contracts", "Output/Prompts", "Output/Renders"]:
                self.assertTrue((project / d / ".gitkeep").is_file(), f"missing .gitkeep in {d}")

            config = (project / ".cpm" / "config.yaml").read_text(encoding="utf-8")
            self.assertIn('project_name: "The Test Reel"', config)
            self.assertIn('target: "sora"', config)
            self.assertIn("default_shard_duration: 5", config)
            self.assertIn("max_shard_duration: 30", config)
            self.assertIn("require_state_diff_check: true", config)

            manifest = (project / ".cpm" / "manifest.md").read_text(encoding="utf-8")
            self.assertIn("<!-- scene-create updates this section automatically -->", manifest)
            self.assertIn("### Scenes", manifest)
            self.assertIn("- [ ] Show Bible created", manifest)
            self.assertNotIn("## Scene 01", manifest)
            self.assertNotIn("/cpm-", manifest)

            code, out = run("--mode", "validate", "--project-path", str(project))
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "pass")
            self.assertEqual(out["missing_dirs"], [])
            self.assertEqual(out["missing_files"], [])
            self.assertEqual(out["missing_config_keys"], [])
            self.assertEqual(out["manifest_issues"], [])

    def test_create_refuses_existing_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "proj"
            run(*create_args(project))
            code, out = run(*create_args(project))
            self.assertEqual(code, 2)
            self.assertEqual(out["status"], "error")
            self.assertIn("already initialized", out["error"])

    def test_update_is_idempotent_and_preserves_creative_work(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "proj"
            run(*create_args(project))
            sentinel = project / "Bible" / "Show_Bible.md"
            sentinel.write_text("USER CONTENT — do not clobber", encoding="utf-8")

            code, out = run(
                "--mode", "update", "--project-path", str(project),
                "--config-template", str(CONFIG_TEMPLATE),
                "--manifest-template", str(MANIFEST_TEMPLATE),
                "--slate-template", str(SLATE_TEMPLATE),
                "--methodology-src", str(METHODOLOGY),
            )
            self.assertEqual(code, 0, out)
            self.assertEqual(out["status"], "updated")
            self.assertEqual(out["created"], [])
            self.assertEqual(out["overwritten"], [])
            self.assertEqual(len(out["skipped_existing"]), 4)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "USER CONTENT — do not clobber")

    def test_update_repairs_missing_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "proj"
            run(*create_args(project))
            import shutil
            shutil.rmtree(project / "Output" / "Renders")
            code, out = run(
                "--mode", "update", "--project-path", str(project),
                "--config-template", str(CONFIG_TEMPLATE),
                "--manifest-template", str(MANIFEST_TEMPLATE),
                "--slate-template", str(SLATE_TEMPLATE),
                "--methodology-src", str(METHODOLOGY),
            )
            self.assertEqual(code, 0, out)
            self.assertTrue((project / "Output" / "Renders").is_dir())
            self.assertTrue(any("Renders" in c for c in out["created"]))

    def test_update_overwrite_config_only_when_named(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "proj"
            run(*create_args(project))
            config_path = project / ".cpm" / "config.yaml"
            config_path.write_text("hand-edited junk", encoding="utf-8")
            code, out = run(
                "--mode", "update", "--project-path", str(project), "--overwrite", "config",
                "--project-name", "The Test Reel", "--model-target", "kling",
                "--config-template", str(CONFIG_TEMPLATE),
                "--manifest-template", str(MANIFEST_TEMPLATE),
                "--slate-template", str(SLATE_TEMPLATE),
                "--methodology-src", str(METHODOLOGY),
            )
            self.assertEqual(code, 0, out)
            self.assertTrue(any("config.yaml" in o for o in out["overwritten"]))
            self.assertIn('target: "kling"', config_path.read_text(encoding="utf-8"))

    def test_validate_hold_on_empty_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "empty"
            project.mkdir()
            code, out = run("--mode", "validate", "--project-path", str(project))
            self.assertEqual(code, 1)
            self.assertEqual(out["status"], "hold")
            self.assertTrue(out["missing_dirs"])
            self.assertTrue(out["missing_files"])
            self.assertTrue(out["missing_config_keys"])

    def test_create_missing_template_is_clean_precondition_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "proj"
            code, out = run(
                "--mode", "create", "--project-path", str(project),
                "--project-name", "X", "--model-target", "sora",
                "--config-template", str(ASSETS / "does-not-exist.yaml"),
                "--manifest-template", str(MANIFEST_TEMPLATE),
                "--slate-template", str(SLATE_TEMPLATE),
                "--methodology-src", str(METHODOLOGY),
            )
            self.assertEqual(code, 2)
            self.assertEqual(out["status"], "error")
            self.assertFalse(project.exists(), "no partial project may be left behind")


if __name__ == "__main__":
    unittest.main()

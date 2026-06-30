#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""scaffold_project — deterministic plumbing for a CPM production project.

The external state machine a CPM production runs on: the directory tree, the
.cpm/config.yaml, the .cpm/manifest.md skeleton, Production/Slate.md, and the
static methodology diagram. This script does only the mechanical work — make the
tree, render the templates with the user's answers, copy the diagram, or report
exactly what an existing project is missing. All judgment (gathering inputs,
resolving conflicts, grading) stays in the prompt that calls this.

Three modes:
  create   — write a brand-new project in full. Refuses if one already exists and,
             on any failure, removes whatever this run wrote so no partial project
             is ever left behind.
  update   — repair an existing project: make missing directories and missing
             scaffolding files only. Never overwrites a file unless it is named in
             --overwrite, so creative work (Bible, Architecture, scenes) is safe.
  validate — read-only. Report missing directories, missing files, missing config
             keys, and manifest skeleton problems. Writes nothing.

Output: one JSON object on stdout describing the result.
Exit codes: 0 = created / updated / validate-pass; 1 = validate-hold / create-failed;
            2 = usage or precondition error (message names the fix).
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import date
from pathlib import Path
from string import Template

# --- The structure contract (kept in sync with references/project-structure.md) ---

REQUIRED_DIRS = [
    ".cpm", ".cpm/agents",
    "Bible", "Bible/Characters", "Bible/World",
    "Architecture",
    "Production", "Production/Scenes", "Production/Contracts", "Production/Validation",
    "Output", "Output/Prompts", "Output/Renders",
    "Diagrams",
]

# logical name -> (relative output path, --<name>-template arg attribute)
SCAFFOLD_FILES = {
    "config": (".cpm/config.yaml", "config_template"),
    "manifest": (".cpm/manifest.md", "manifest_template"),
    "slate": ("Production/Slate.md", "slate_template"),
}

METHODOLOGY_DEST = "Diagrams/cpm-methodology.excalidraw"

# Presence check only (stdlib, no YAML parse): each key token must appear at least
# once in the rendered config. The scaffold writes this file, so this guards against a
# wholesale missing section, not against hand-editing a single agent block's sub-keys.
REQUIRED_CONFIG_KEYS = [
    "project_name:", "version:", "created:",
    "temporal:", "default_shard_duration:", "max_shard_duration:",
    "model:", "target:",
    "agents:", "showrunner:", "cinematographer:", "script_supervisor:", "prompt_engineer:",
    "enabled:", "prompt_file:",
    "validation:", "require_state_diff_check:", "require_style_compliance:", "banned_words_enforcement:",
]

MANIFEST_SECTIONS = [
    "### Active Scene Context",
    "### Required Files for Current Context",
    "### Project Status",
    "### Scenes",
]
MANIFEST_SCENE_MARKER = "<!-- scene-create updates this section automatically -->"


def err(message: str) -> dict:
    """A usage/precondition error result. The message names the fix."""
    return {"ok": False, "status": "error", "error": message}


def subs_from(args) -> dict:
    return {
        "project_name": args.project_name or "",
        "version": args.version,
        "created": args.created,
        "model_target": args.model_target or "",
        "default_shard_duration": args.shard_duration,
        "max_shard_duration": args.max_shard_duration,
    }


def render_template(template_path: Path, subs: dict) -> str:
    """Render a ${token} template with strict substitution (missing token fails loudly)."""
    text = template_path.read_text(encoding="utf-8")
    try:
        return Template(text).substitute(subs)
    except KeyError as e:
        raise KeyError(
            f"template {template_path} references unknown token {e}; "
            f"known tokens: {', '.join(sorted(subs))}"
        ) from e


def template_path_for(name: str, args) -> Path:
    _, attr = SCAFFOLD_FILES[name]
    return Path(getattr(args, attr))


def missing_template_paths(names, args) -> list[str]:
    out = []
    for name in names:
        p = template_path_for(name, args)
        if not p.is_file():
            out.append(f"{name} template not found: {p} — restore it under the skill's assets/ "
                       f"or pass the correct --{name}-template path")
    return out


def do_create(args) -> tuple[dict, int]:
    project = Path(args.project_path)

    # Preconditions — fail BEFORE writing anything, so create is all-or-nothing.
    problems = missing_template_paths(SCAFFOLD_FILES.keys(), args)
    methodology_src = Path(args.methodology_src)
    if not methodology_src.is_file():
        problems.append(f"methodology diagram not found: {methodology_src} — restore "
                        f"assets/cpm-methodology.excalidraw or pass --methodology-src")
    if not args.project_name:
        problems.append("--project-name is required for create")
    if not args.model_target:
        problems.append("--model-target is required for create")
    if (project / ".cpm" / "config.yaml").exists():
        problems.append(f"{project / '.cpm' / 'config.yaml'} already exists — this project is "
                        f"already initialized; run with --mode update to repair or change config")
    if problems:
        return err("; ".join(problems)), 2

    subs = subs_from(args)
    created: list[str] = []
    project_made_by_us = not project.exists()

    try:
        project.mkdir(parents=True, exist_ok=True)
        if project_made_by_us:
            created.append(str(project))
        for d in REQUIRED_DIRS:
            target = project / d
            if not target.exists():
                target.mkdir(parents=True, exist_ok=True)
                created.append(str(target))
        for name, (rel, _attr) in SCAFFOLD_FILES.items():
            out_path = project / rel
            out_path.write_text(render_template(template_path_for(name, args), subs), encoding="utf-8")
            created.append(str(out_path))
        diagram_dest = project / METHODOLOGY_DEST
        shutil.copy2(methodology_src, diagram_dest)
        created.append(str(diagram_dest))
        _write_gitkeeps(project, created)
    except Exception as e:  # noqa: BLE001 — any failure must leave NO partial project
        _rollback(project, project_made_by_us, created)
        return {
            "ok": False,
            "status": "failed",
            "error": f"scaffold failed and was rolled back ({e}); no partial project remains",
            "project_path": str(project),
        }, 1

    return {
        "ok": True,
        "status": "created",
        "project_path": str(project),
        "created": created,
    }, 0


def _rollback(project: Path, project_made_by_us: bool, created: list[str]) -> None:
    """Undo this run's writes so a failed create never leaves a partial project."""
    if project_made_by_us and project.exists():
        shutil.rmtree(project, ignore_errors=True)
        return
    for path_str in reversed(created):
        p = Path(path_str)
        try:
            if p.is_file():
                p.unlink()
            elif p.is_dir():
                p.rmdir()  # only removes if empty — leaves any pre-existing content intact
        except OSError:
            pass


def _write_gitkeeps(project: Path, created: list[str]) -> None:
    """Drop a .gitkeep into every required directory left empty after scaffolding.
    Git does not track empty directories, so without these the skeleton would not
    survive version control — and the skill's own validate would then report the
    vanished dirs as missing. Deterministic: only ever adds a marker to an empty dir."""
    for d in REQUIRED_DIRS:
        target = project / d
        if target.is_dir() and not any(target.iterdir()):
            keep = target / ".gitkeep"
            keep.write_text("", encoding="utf-8")
            created.append(str(keep))


def do_update(args) -> tuple[dict, int]:
    project = Path(args.project_path)
    if not project.exists():
        return err(f"{project} does not exist — run --mode create to scaffold a new project"), 2

    overwrite = {x.strip() for x in (args.overwrite or "").split(",") if x.strip()}
    unknown = overwrite - (set(SCAFFOLD_FILES) | {"methodology"})
    if unknown:
        return err(f"--overwrite names unknown targets: {', '.join(sorted(unknown))}; "
                   f"valid: {', '.join(sorted(set(SCAFFOLD_FILES) | {'methodology'}))}"), 2

    subs = subs_from(args)
    created: list[str] = []
    overwritten: list[str] = []
    skipped_existing: list[str] = []

    # Directories are always safe to create when missing.
    for d in REQUIRED_DIRS:
        target = project / d
        if not target.exists():
            target.mkdir(parents=True, exist_ok=True)
            created.append(str(target))

    # Files: write only when missing, or when explicitly named in --overwrite.
    to_write = [n for n, (rel, _a) in SCAFFOLD_FILES.items()
                if not (project / rel).exists() or n in overwrite]
    problems = missing_template_paths(to_write, args)
    if problems:
        return err("; ".join(problems)), 2
    for name, (rel, _attr) in SCAFFOLD_FILES.items():
        out_path = project / rel
        if not out_path.exists():
            out_path.write_text(render_template(template_path_for(name, args), subs), encoding="utf-8")
            created.append(str(out_path))
        elif name in overwrite:
            out_path.write_text(render_template(template_path_for(name, args), subs), encoding="utf-8")
            overwritten.append(str(out_path))
        else:
            skipped_existing.append(str(out_path))

    # Methodology diagram: place when missing, or replace when named in --overwrite.
    diagram_dest = project / METHODOLOGY_DEST
    if not diagram_dest.exists() or "methodology" in overwrite:
        methodology_src = Path(args.methodology_src)
        if not methodology_src.is_file():
            return err(f"methodology diagram not found: {methodology_src} — restore "
                       f"assets/cpm-methodology.excalidraw or pass --methodology-src"), 2
        existed = diagram_dest.exists()
        shutil.copy2(methodology_src, diagram_dest)
        (overwritten if existed else created).append(str(diagram_dest))
    else:
        skipped_existing.append(str(diagram_dest))

    # Keep the skeleton durable under version control for any dir still empty.
    _write_gitkeeps(project, created)

    return {
        "ok": True,
        "status": "updated",
        "project_path": str(project),
        "created": created,
        "overwritten": overwritten,
        "skipped_existing": skipped_existing,
    }, 0


def do_validate(args) -> tuple[dict, int]:
    project = Path(args.project_path)
    if not project.exists():
        return err(f"{project} does not exist — there is no project to validate at this path"), 2

    missing_dirs = [d for d in REQUIRED_DIRS if not (project / d).is_dir()]

    missing_files = []
    for _name, (rel, _attr) in SCAFFOLD_FILES.items():
        if not (project / rel).is_file():
            missing_files.append(rel)
    if not (project / METHODOLOGY_DEST).is_file():
        missing_files.append(METHODOLOGY_DEST)

    config_path = project / ".cpm" / "config.yaml"
    if config_path.is_file():
        config_text = config_path.read_text(encoding="utf-8")
        missing_config_keys = [k.rstrip(":") for k in REQUIRED_CONFIG_KEYS if k not in config_text]
    else:
        missing_config_keys = [k.rstrip(":") for k in REQUIRED_CONFIG_KEYS]

    manifest_path = project / ".cpm" / "manifest.md"
    manifest_issues = []
    if manifest_path.is_file():
        manifest_text = manifest_path.read_text(encoding="utf-8")
        for section in MANIFEST_SECTIONS:
            if section not in manifest_text:
                manifest_issues.append(f"missing section: {section}")
        if MANIFEST_SCENE_MARKER not in manifest_text:
            manifest_issues.append("missing scene-registry marker in Scenes section")
    else:
        manifest_issues.append("manifest file absent")

    intact = not (missing_dirs or missing_files or missing_config_keys or manifest_issues)
    return {
        "ok": True,
        "status": "pass" if intact else "hold",
        "project_path": str(project),
        "missing_dirs": missing_dirs,
        "missing_files": missing_files,
        "missing_config_keys": missing_config_keys,
        "manifest_issues": manifest_issues,
    }, 0 if intact else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Deterministic scaffolder for a CPM production project")
    p.add_argument("--mode", required=True, choices=["create", "update", "validate"])
    p.add_argument("--project-path", required=True, help="destination folder for the production project")
    p.add_argument("--project-name", help="display name written into config, manifest, and slate")
    p.add_argument("--model-target", help="AI video model id (e.g. sora, kling, runway, pika, or other)")
    p.add_argument("--shard-duration", default="5", help="default shard duration in seconds (default 5)")
    p.add_argument("--max-shard-duration", default="30", help="max shard duration in seconds (default 30)")
    p.add_argument("--version", default="1.0", help="project schema version written to config (default 1.0)")
    p.add_argument("--created", default=date.today().isoformat(), help="creation date (default today, ISO)")
    p.add_argument("--config-template", help="path to the config.yaml template")
    p.add_argument("--manifest-template", help="path to the manifest.md template")
    p.add_argument("--slate-template", help="path to the Slate.md template")
    p.add_argument("--methodology-src", help="path to the methodology .excalidraw asset to place in Diagrams/")
    p.add_argument("--overwrite", default="", help="update mode only: comma list of files to overwrite "
                                                   "(config,manifest,slate,methodology)")
    args = p.parse_args(argv)

    if args.mode == "create":
        result, code = do_create(args)
    elif args.mode == "update":
        result, code = do_update(args)
    else:
        result, code = do_validate(args)

    print(json.dumps(result, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())

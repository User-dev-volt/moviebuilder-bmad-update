#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""validate_scene_brief — deterministic structural check for a CPM scene brief.

Validate-mode plumbing for cpm-scene-create. It confirms only what a machine can judge
without reading meaning:

  1. Frontmatter is well-formed and carries the full canonical field set; scene_id ==
     "SCENE_" + scene_number; scene_number is a zero-padded two-digit string.
  2. The four-way equality that makes {currentBeat} a pure integer lookup —
     shard_count == Beat-Table rows == Beat-Detail blocks == max(Beat).
  3. A contiguous integer Beat column: 1..shard_count, exactly one row each.
  4. The Beat Table columns are exactly: Beat | Duration | Focus | Primary Requirement.
  5. Every Beat Table row has a matching '#### Beat {N}' detail block and vice versa (by integer).
  6. Every on-camera character resolves to a Bible/Characters/{Name}.md file.
  9. The side artifacts were written: entry_contract.md beside the brief, a Scenes entry in the
     manifest, and a Scenes row in the Slate.

It also checks the deterministic halves of per-beat quality: Duration in {5, 15, 30}, Focus
non-empty, and an **Action:** field present in each detail block. Whether a Primary Requirement
is CONCRETE enough, and whether the Narrative Purpose names a theme or the Emotional Arc opens
and closes, stays with the prompt — this script reports structure, not substance.

A later-scene entry_contract that is an explicit gap stub (the prior shard's exit state does not
exist yet) is surfaced as a non-blocking warning, never a hold — the handoff is marked, not
silently hollow.

Output: one JSON object on stdout.
Exit codes: 0 = pass (warnings allowed); 1 = hold (structure incomplete); 2 = usage/precondition
            error (the message names the fix).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# The full canonical frontmatter field set, in schema order — kept in sync with
# references/scene-brief-contract.md and assets/scene-brief.template.md.
REQUIRED_FRONTMATTER = [
    "scene_number", "scene_id", "scene_title", "status", "shard_count",
    "default_shard_duration", "on_camera_characters", "arc_position",
    "created", "lastModified",
]
BEAT_COLUMNS = ["Beat", "Duration", "Focus", "Primary Requirement"]
VALID_DURATIONS = {5, 15, 30}
# A later-scene entry_contract whose prior exit state does not yet exist is written as an
# explicit gap stub carrying this phrase. Detecting it lets Validate surface a non-blocking
# warning instead of passing off a silent hollow handoff. (No em-dash in the marker so the
# match stays portable across encodings.)
ENTRY_GAP_MARKER = "Script Supervisor fills before Shard 1"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)
SCALAR_RE = re.compile(r"^([A-Za-z0-9_]+):\s*(.*)$")
LIST_ITEM_RE = re.compile(r"^\s+-\s+(.*)$")
BEAT_DETAIL_RE = re.compile(r"(?m)^####\s+Beat\s+(\d+)\b")
PADDED_RE = re.compile(r"^\d{2}$")
SEPARATOR_CELL_RE = re.compile(r"^:?-+:?$")


def err(message: str) -> dict:
    """A usage/precondition error result. The message names the fix."""
    return {"ok": False, "status": "error", "error": message}


def _unquote(value: str) -> str:
    """Strip surrounding quotes; otherwise drop a trailing ` # comment` from a bare scalar."""
    value = value.strip()
    if value.startswith("'") and "'" in value[1:]:
        return value[1:value.index("'", 1)]
    if value.startswith('"') and '"' in value[1:]:
        return value[1:value.index('"', 1)]
    if " #" in value:
        value = value.split(" #", 1)[0].strip()
    return value


def parse_frontmatter(text: str):
    """Parse the leading YAML frontmatter block into a dict.

    Handles the scalar keys plus on_camera_characters as either a block list (one `  - name`
    per line) or an inline list (`[a, b]`). Stdlib only — no third-party YAML dependency, so
    this stays in lockstep with check_character.py's no-dependency discipline.
    """
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    data: dict = {}
    lines = m.group(1).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue
        sm = SCALAR_RE.match(line)
        if not sm:
            i += 1
            continue
        key, raw = sm.group(1), sm.group(2).strip()
        if raw == "":
            items = []
            j = i + 1
            while j < len(lines):
                im = LIST_ITEM_RE.match(lines[j])
                if not im:
                    break
                items.append(_unquote(im.group(1)))
                j += 1
            if items:
                data[key] = items
                i = j
                continue
            data[key] = ""
        elif raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            data[key] = [_unquote(x) for x in inner.split(",") if x.strip()]
        else:
            data[key] = _unquote(raw)
        i += 1
    return data


def _is_separator_row(cells) -> bool:
    return bool(cells) and all(SEPARATOR_CELL_RE.match(c.strip()) for c in cells)


def parse_beat_table(text: str):
    """Return (header_cells, data_rows) for the table under '### Beat Table'.

    header_cells is None when no table is found. The Markdown separator row (`|---|`) is
    dropped from data_rows.
    """
    idx = text.find("### Beat Table")
    if idx == -1:
        return None, []
    rows = []
    for line in text[idx:].splitlines()[1:]:
        s = line.strip()
        if s.startswith("|"):
            rows.append([c.strip() for c in s.strip("|").split("|")])
        elif rows:
            break
        elif s.startswith("#"):
            break
    if not rows:
        return None, []
    header = rows[0]
    data = [r for r in rows[1:] if not _is_separator_row(r)]
    return header, data


def check(brief: Path, project: Path | None) -> tuple[dict, int]:
    if not brief.is_file():
        return err(f"scene brief not found: {brief} — pass --brief with the path to the "
                   f"scene-brief.md file"), 2

    brief = brief.resolve()
    if project is None:
        parents = brief.parents
        # {project}/Production/Scenes/Scene_XX/scene-brief.md -> parents[3] == {project}
        project = parents[3] if len(parents) > 3 else brief.parent
    project = Path(project)

    text = brief.read_text(encoding="utf-8")
    issues: list[str] = []
    warnings: list[str] = []

    # ---- check 1: frontmatter identity ----
    fm = parse_frontmatter(text)
    scene_number = scene_id = None
    shard_count = None
    characters: list[str] = []
    if fm is None:
        issues.append("frontmatter missing or malformed (no leading '--- ... ---' block)")
    else:
        missing_keys = [k for k in REQUIRED_FRONTMATTER if k not in fm]
        if missing_keys:
            issues.append(f"frontmatter missing required field(s): {', '.join(missing_keys)}")
        scene_number = fm.get("scene_number")
        scene_id = fm.get("scene_id")
        chars = fm.get("on_camera_characters") or []
        characters = [chars] if isinstance(chars, str) and chars else (chars if isinstance(chars, list) else [])
        if scene_number is not None and not PADDED_RE.match(str(scene_number)):
            issues.append(f"scene_number '{scene_number}' is not a zero-padded two-digit string "
                          f"(e.g. '01')")
        if scene_number is not None and scene_id is not None:
            expected = f"SCENE_{scene_number}"
            if scene_id != expected:
                issues.append(f"scene_id '{scene_id}' must equal '{expected}' "
                              f"(\"SCENE_\" + scene_number)")
        raw_count = fm.get("shard_count")
        try:
            shard_count = int(str(raw_count))
        except (TypeError, ValueError):
            issues.append(f"shard_count is missing or not an integer: {raw_count!r}")

    # ---- parse the two Beat layers ----
    header, data_rows = parse_beat_table(text)
    columns_ok = header == BEAT_COLUMNS
    if header is None:
        issues.append("no '### Beat Table' section found")
    elif not columns_ok:
        issues.append(f"Beat Table columns must be exactly '{' | '.join(BEAT_COLUMNS)}'; "
                      f"found '{' | '.join(header)}'")

    table_beats: list[int] = []
    for r in data_rows:
        if not r or not r[0]:
            continue
        try:
            table_beats.append(int(r[0]))
        except ValueError:
            issues.append(f"Beat Table row has a non-integer Beat value: {r[0]!r}")

    detail_beats = [int(n) for n in BEAT_DETAIL_RE.findall(text)]

    beat_table_rows = len(table_beats)
    beat_detail_blocks = len(detail_beats)
    max_beat = max(table_beats) if table_beats else 0

    # ---- check 2: the four-way equality (the determinism precondition) ----
    four_way = shard_count is not None and \
        shard_count == beat_table_rows == beat_detail_blocks == max_beat
    if shard_count is not None and not four_way:
        issues.append(
            f"four-way equality broken: shard_count={shard_count}, Beat-Table rows="
            f"{beat_table_rows}, Beat-Detail blocks={beat_detail_blocks}, max(Beat)={max_beat} "
            f"— all four must be equal")

    # ---- check 3: contiguous integer Beat column ----
    contiguous = bool(table_beats) and sorted(table_beats) == list(range(1, beat_table_rows + 1))
    if table_beats and not contiguous:
        issues.append(f"Beat column must be contiguous integers 1..{beat_table_rows}, exactly one "
                      f"row each; found {sorted(table_beats)}")

    # ---- check 5: Beat Table <-> Beat Details are 1:1 by integer ----
    table_detail_match = (
        sorted(set(table_beats)) == sorted(set(detail_beats))
        and len(table_beats) == len(set(table_beats))
        and len(detail_beats) == len(set(detail_beats))
    )
    if not table_detail_match:
        only_table = sorted(set(table_beats) - set(detail_beats))
        only_detail = sorted(set(detail_beats) - set(table_beats))
        bits = []
        if only_table:
            bits.append(f"table rows with no detail block: {only_table}")
        if only_detail:
            bits.append(f"detail blocks with no table row: {only_detail}")
        if not bits:
            bits.append("duplicate Beat integers in the table or the details")
        issues.append("Beat Table and Beat Details are not 1:1 — " + "; ".join(bits))

    # ---- cheap deterministic halves of per-beat quality (Duration / Focus / Action) ----
    # The specificity judgment (is the Primary Requirement concrete?) stays with the prompt.
    if columns_ok:
        for r in data_rows:
            if len(r) < 4:
                continue
            beat_label, duration_raw, focus = r[0], r[1], r[2]
            digits = re.sub(r"[^\d]", "", duration_raw)
            if not digits or int(digits) not in VALID_DURATIONS:
                issues.append(f"Beat {beat_label}: Duration '{duration_raw}' must be one of "
                              f"5s, 15s, 30s")
            if not focus:
                issues.append(f"Beat {beat_label}: Focus is empty")
    detail_iter = list(BEAT_DETAIL_RE.finditer(text))
    for k, mobj in enumerate(detail_iter):
        start = mobj.start()
        end = detail_iter[k + 1].start() if k + 1 < len(detail_iter) else len(text)
        if "**Action:**" not in text[start:end]:
            issues.append(f"Beat {mobj.group(1)} detail block is missing the **Action:** field")

    # ---- check 6: each on-camera character resolves to a Bible/Characters file ----
    missing_characters = []
    for name in characters:
        name = str(name).strip()
        if not name:
            continue
        if not (project / "Bible" / "Characters" / f"{name}.md").is_file():
            missing_characters.append(name)
    if missing_characters:
        issues.append("on_camera_characters with no Bible/Characters/<name>.md file: "
                      + ", ".join(missing_characters))

    # ---- check 9: the side artifacts were written ----
    entry_contract = brief.parent / "state" / "entry_contract.md"
    entry_contract_present = entry_contract.is_file()
    if not entry_contract_present:
        issues.append(f"entry contract not found: {entry_contract} — finalize must seed "
                      f"state/entry_contract.md")
    elif ENTRY_GAP_MARKER in entry_contract.read_text(encoding="utf-8"):
        warnings.append(f"entry_contract.md is an unresolved gap stub ('{ENTRY_GAP_MARKER}') — "
                        f"the Script Supervisor must fill it before Shard 1")

    manifest = project / ".cpm" / "manifest.md"
    manifest_has_scene = False
    if not manifest.is_file():
        issues.append(f"manifest not found: {manifest} — finalize must register the scene")
    elif scene_number is not None:
        manifest_has_scene = f"## Scene {scene_number}" in manifest.read_text(encoding="utf-8")
        if not manifest_has_scene:
            issues.append(f"manifest has no '## Scene {scene_number}' entry in its Scenes registry")

    slate = project / "Production" / "Slate.md"
    slate_has_scene = False
    if not slate.is_file():
        issues.append(f"Slate not found: {slate} — finalize must add the scene to the Slate")
    elif scene_number is not None:
        brief_rel = f"Production/Scenes/Scene_{scene_number}/scene-brief.md"
        slate_has_scene = brief_rel in slate.read_text(encoding="utf-8")
        if not slate_has_scene:
            issues.append(f"Slate has no row for Scene {scene_number} "
                          f"(expected the brief path '{brief_rel}')")

    intact = not issues
    return {
        "ok": True,
        "status": "pass" if intact else "hold",
        "brief_path": str(brief),
        "project_root": str(project),
        "scene_id": scene_id,
        "scene_number": scene_number,
        "shard_count": shard_count,
        "beat_table_rows": beat_table_rows,
        "beat_detail_blocks": beat_detail_blocks,
        "max_beat": max_beat,
        "beat_column": sorted(table_beats),
        "columns_ok": columns_ok,
        "four_way_equality": four_way,
        "contiguous": contiguous,
        "table_detail_match": table_detail_match,
        "missing_character_files": missing_characters,
        "entry_contract_present": entry_contract_present,
        "manifest_has_scene": manifest_has_scene,
        "slate_has_scene": slate_has_scene,
        "warnings": warnings,
        "issues": issues,
    }, 0 if intact else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Deterministic structural check for a CPM scene brief")
    p.add_argument("--brief", required=True, type=Path, help="path to the scene-brief.md file")
    p.add_argument("--project", type=Path,
                   help="path to the CPM project root (the folder holding .cpm/, Bible/, "
                        "Production/). Default: inferred from the brief path "
                        "(project/Production/Scenes/Scene_XX/scene-brief.md).")
    args = p.parse_args(argv)

    result, code = check(args.brief, args.project)
    print(json.dumps(result, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())

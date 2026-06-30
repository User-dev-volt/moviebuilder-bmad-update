#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""validate_shard — deterministic structural check for a compiled CPM shard.

Validate-mode plumbing for cpm-shard-generation. It confirms only what a machine can judge
without reading meaning — the prompt and its sibling exit state are structurally whole and
agree with each other and (when available) with the scene brief's Beat Table:

  1. The prompt frontmatter is well-formed and carries the full field set: sceneNumber,
     shardNumber, beatName, generatedDate, agentInputs, stateDiffPassed.
  2. stateDiffPassed is true. A prompt may never be written while the State-Diff Gate reads
     false — that is a structural contradiction, not a warning.
  3. All four agentInputs (showrunner, cinematographer, scriptSupervisor, promptEngineer) are
     true — every seat at the Four-Agent Ritual is accounted for.
  4. The prompt body carries the six bracketed sections in order: [ID: ...], [Technical Header],
     [Subject/Asset], [Action/State], [Environment/Lighting], [Temporal Constraint].
  5. [Temporal Constraint] opens with a shard duration of 5, 15, or 30 seconds.
  6. The sibling exit state exists and its sceneNumber / shardNumber match the prompt.
  7. The exit state carries its required sections (Character States, Environment State, State
     Changes This Shard, Active Contracts); a non-final shard also carries a non-empty Entry
     Contract for the next shard (MUST Start With / MUST NOT Show).

The Beat Table cross-checks DEGRADE GRACEFULLY. When the scene brief is absent, or carries no
machine-readable Beat Table (a production may carry only an older brief shape), the cross-checks
are skipped with a single warning — never a hold. When a Beat Table is present they hold at full
hardness: shardNumber is 1..shard_count, the beat exists in the table, and the prompt's
[Temporal Constraint] duration equals that beat's Duration.

Substance — continuity-safe against the entry contract, anchors inside the first 25%, banned
words, the exit hook — is judged by the workflow's Validate mode, not here. This script reports
structure, not meaning.

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

# The prompt's canonical frontmatter field set, in schema order — kept in sync with
# references/shard-ritual-contract.md and assets/shard-prompt.template.md.
REQUIRED_PROMPT_FRONTMATTER = [
    "sceneNumber", "shardNumber", "beatName", "generatedDate", "agentInputs", "stateDiffPassed",
]
# The four seats of the Four-Agent Ritual; every input must read true in a shipped prompt.
AGENT_INPUTS = ["showrunner", "cinematographer", "scriptSupervisor", "promptEngineer"]
# The six bracketed body sections, in the order the compiled prompt must present them.
PROMPT_SECTIONS = [
    "[ID:", "[Technical Header]", "[Subject/Asset]", "[Action/State]",
    "[Environment/Lighting]", "[Temporal Constraint]",
]
# Exit-state sections that every shard carries, regardless of position in the scene.
EXIT_CORE_SECTIONS = [
    "## Character States", "## Environment State",
    "## State Changes This Shard", "## Active Contracts",
]
# The next-shard handshake; required and non-empty on every shard but the scene's last.
EXIT_ENTRY_HEADING = "## Entry Contract for Next Shard"
EXIT_MUST_START = "### MUST Start With:"
EXIT_MUST_NOT = "### MUST NOT Show:"
# The Beat Table columns the cross-checks read; their absence means an older brief shape that
# the cross-checks degrade around rather than hold on.
BEAT_COLUMNS = ["Beat", "Duration", "Focus", "Primary Requirement"]
VALID_DURATIONS = {5, 15, 30}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)
SCALAR_RE = re.compile(r"^([A-Za-z0-9_]+):\s*(.*)$")
LIST_ITEM_RE = re.compile(r"^\s+-\s+(.*)$")
NESTED_ITEM_RE = re.compile(r"^\s+([A-Za-z0-9_]+):\s*(.*)$")
SEPARATOR_CELL_RE = re.compile(r"^:?-+:?$")
# The block opens just past the `[Temporal Constraint]:` marker, so skip a leading colon and
# whitespace before the duration count.
DURATION_OPEN_RE = re.compile(r"^[:\s]*(\d+)\s*seconds?\b", re.IGNORECASE)


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


def _truthy(value) -> bool:
    """A YAML-ish boolean: a real bool, or a scalar string that reads 'true'."""
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() == "true"


def parse_frontmatter(text: str):
    """Parse the leading YAML frontmatter block into a dict.

    Handles scalar keys, a nested one-level mapping (agentInputs: with indented `  key: value`
    children), and block lists (`  - item`). Stdlib only — no third-party YAML dependency, so
    this stays in lockstep with validate_scene_brief.py's no-dependency discipline.
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
            # An empty value opens either a block list, a nested mapping, or nothing.
            j = i + 1
            list_items = []
            while j < len(lines) and LIST_ITEM_RE.match(lines[j]):
                list_items.append(_unquote(LIST_ITEM_RE.match(lines[j]).group(1)))
                j += 1
            if list_items:
                data[key] = list_items
                i = j
                continue
            nested: dict = {}
            while j < len(lines) and NESTED_ITEM_RE.match(lines[j]) \
                    and not LIST_ITEM_RE.match(lines[j]):
                nm = NESTED_ITEM_RE.match(lines[j])
                nested[nm.group(1)] = _unquote(nm.group(2))
                j += 1
            if nested:
                data[key] = nested
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


def body_after_frontmatter(text: str) -> str:
    """Return the document body with any leading frontmatter block removed."""
    m = FRONTMATTER_RE.match(text)
    return text[m.end():] if m else text


def section_block(text: str, marker: str, stops) -> str:
    """Return the text from `marker` up to the next stop marker (or end of text)."""
    start = text.find(marker)
    if start == -1:
        return ""
    after = start + len(marker)
    end = len(text)
    for stop in stops:
        pos = text.find(stop, after)
        if pos != -1:
            end = min(end, pos)
    return text[after:end]


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


def _duration_int(raw: str):
    """Pull the integer second-count out of a Duration cell ('5s' -> 5); None if absent."""
    digits = re.sub(r"[^\d]", "", raw or "")
    return int(digits) if digits else None


def check(prompt: Path, project: Path | None) -> tuple[dict, int]:
    if not prompt.is_file():
        return err(f"compiled prompt not found: {prompt} — pass --prompt with the path to the "
                   f"Scene_XX_Shard_Y_prompt.md file"), 2

    prompt = prompt.resolve()
    if project is None:
        parents = prompt.parents
        # {project}/Output/Prompts/Scene_XX_Shard_Y_prompt.md -> parents[2] == {project}
        project = parents[2] if len(parents) > 2 else prompt.parent
    project = Path(project)

    text = prompt.read_text(encoding="utf-8")
    body = body_after_frontmatter(text)
    issues: list[str] = []
    warnings: list[str] = []

    # ---- check 1: prompt frontmatter identity ----
    fm = parse_frontmatter(text)
    scene_number = shard_number = beat_name = None
    agent_inputs: dict = {}
    state_diff_passed = False
    if fm is None:
        issues.append("prompt frontmatter missing or malformed (no leading '--- ... ---' block)")
    else:
        missing_keys = [k for k in REQUIRED_PROMPT_FRONTMATTER if k not in fm]
        if missing_keys:
            issues.append("prompt frontmatter missing required field(s): "
                          + ", ".join(missing_keys))
        scene_number = fm.get("sceneNumber")
        shard_number = fm.get("shardNumber")
        beat_name = fm.get("beatName")
        raw_inputs = fm.get("agentInputs")
        if isinstance(raw_inputs, dict):
            agent_inputs = {k: _truthy(v) for k, v in raw_inputs.items()}
        state_diff_passed = _truthy(fm.get("stateDiffPassed"))

    # ---- check 2: stateDiffPassed is true (a false gate may never ship a prompt) ----
    if fm is not None and not state_diff_passed:
        issues.append("stateDiffPassed is not true — the State-Diff Gate must read PASSED before "
                      "a prompt is written; a prompt with a failed gate is a structural break")

    # ---- check 3: all four agent inputs are true ----
    missing_inputs = [a for a in AGENT_INPUTS if not agent_inputs.get(a)]
    agent_inputs_ok = fm is not None and not missing_inputs
    if fm is not None and missing_inputs:
        issues.append("agentInputs not all true (missing or false): " + ", ".join(missing_inputs))

    # ---- check 4: the six bracketed sections, present and in order ----
    positions = []
    sections_present = []
    last = -1
    sections_ok = True
    for marker in PROMPT_SECTIONS:
        pos = body.find(marker)
        if pos == -1:
            issues.append(f"prompt body missing the {marker.rstrip(':')} section")
            sections_ok = False
            continue
        sections_present.append(marker)
        positions.append(pos)
        if pos < last:
            sections_ok = False
        last = pos
    if positions and positions != sorted(positions):
        if "prompt body sections are out of order" not in issues:
            issues.append("prompt body sections are out of order — expected: "
                          + " -> ".join(s.rstrip(":") for s in PROMPT_SECTIONS))
        sections_ok = False

    # ---- check 5: [Temporal Constraint] opens with a 5 / 15 / 30 second duration ----
    temporal_block = section_block(body, "[Temporal Constraint]",
                                   ["**Build Notes:**", "\n---"])
    temporal_duration = None
    dm = DURATION_OPEN_RE.match(temporal_block)
    if dm:
        temporal_duration = int(dm.group(1))
    temporal_ok = temporal_duration in VALID_DURATIONS
    if "[Temporal Constraint]" in body and not temporal_ok:
        issues.append("[Temporal Constraint] must open with a duration of 5, 15, or 30 seconds; "
                      f"found {temporal_duration if temporal_duration is not None else 'no number'}")

    # ---- locate the sibling exit state ----
    exit_path = None
    exit_present = False
    exit_identity_match = False
    exit_core_ok = False
    entry_contract_required = False
    entry_contract_ok = False
    if scene_number is not None and shard_number is not None:
        exit_path = (project / "Production" / "Scenes" / f"Scene_{scene_number}"
                     / "state" / f"shard_{shard_number}_exit_state.md")
        exit_present = exit_path.is_file()

    # ---- parse the scene brief's Beat Table (graceful degradation) ----
    scene_brief_checked = False
    shard_count = None
    shard_in_range = None
    beat_in_table = None
    beat_duration = None
    duration_matches_beat = None
    brief_path = None
    if scene_number is not None:
        brief_path = (project / "Production" / "Scenes" / f"Scene_{scene_number}"
                      / "scene-brief.md")
        brief_text = brief_path.read_text(encoding="utf-8") if brief_path.is_file() else None
        header, data_rows = parse_beat_table(brief_text) if brief_text else (None, [])
        bfm = parse_frontmatter(brief_text) if brief_text else None
        if bfm is not None:
            try:
                shard_count = int(str(bfm.get("shard_count")))
            except (TypeError, ValueError):
                shard_count = None
        beats: dict = {}
        if header == BEAT_COLUMNS:
            for r in data_rows:
                if len(r) >= 2 and r[0]:
                    try:
                        beats[int(r[0])] = _duration_int(r[1])
                    except ValueError:
                        continue
        # A brief is cross-checkable only when it carries an integer shard_count AND a Beat
        # Table in the expected column shape. Anything else is an older brief shape: degrade.
        if shard_count is not None and header == BEAT_COLUMNS and beats:
            scene_brief_checked = True
        else:
            warnings.append(
                "scene brief has no machine-readable Beat Table (or no shard_count) at "
                f"{brief_path} — Beat Table cross-checks skipped; structure of the prompt and "
                "exit state were still checked")

    # ---- shard number as an integer, for range and finality logic ----
    shard_num_int = None
    if shard_number is not None:
        try:
            shard_num_int = int(str(shard_number))
        except (TypeError, ValueError):
            shard_num_int = None

    # ---- check 8: Beat Table cross-checks (holds only when the brief is cross-checkable) ----
    if scene_brief_checked and shard_num_int is not None:
        shard_in_range = 1 <= shard_num_int <= shard_count
        if not shard_in_range:
            issues.append(f"shardNumber {shard_num_int} is outside 1..{shard_count} "
                          f"(shard_count from the scene brief)")
        beat_in_table = shard_num_int in beats
        if not beat_in_table:
            issues.append(f"beat {shard_num_int} has no row in the scene brief's Beat Table")
        elif temporal_duration is not None:
            beat_duration = beats[shard_num_int]
            duration_matches_beat = beat_duration == temporal_duration
            if not duration_matches_beat:
                issues.append(f"[Temporal Constraint] duration {temporal_duration}s does not match "
                              f"beat {shard_num_int}'s Duration of {beat_duration}s in the Beat Table")

    # ---- a shard is final only when we can prove it from a cross-checkable brief ----
    is_final = bool(scene_brief_checked and shard_count is not None
                    and shard_num_int is not None and shard_num_int == shard_count)
    entry_contract_required = not is_final

    # ---- check 6 / 7: the sibling exit state ----
    if exit_path is None:
        issues.append("cannot locate the exit state — prompt sceneNumber/shardNumber are missing")
    elif not exit_present:
        issues.append(f"sibling exit state not found: {exit_path} — every generated shard writes "
                      f"its shard_{shard_number}_exit_state.md")
    else:
        exit_text = exit_path.read_text(encoding="utf-8")
        efm = parse_frontmatter(exit_text)
        exit_scene = efm.get("sceneNumber") if efm else None
        exit_shard = efm.get("shardNumber") if efm else None
        exit_identity_match = (str(exit_scene) == str(scene_number)
                               and str(exit_shard) == str(shard_number))
        if not exit_identity_match:
            issues.append(f"exit state identity mismatch: prompt is Scene {scene_number} Shard "
                          f"{shard_number}; exit state reads Scene {exit_scene} Shard {exit_shard}")
        missing_sections = [s for s in EXIT_CORE_SECTIONS if s not in exit_text]
        exit_core_ok = not missing_sections
        if missing_sections:
            issues.append("exit state missing required section(s): " + ", ".join(missing_sections))
        # The next-shard handshake: required and non-empty on every shard but the scene's last.
        if entry_contract_required:
            if EXIT_ENTRY_HEADING not in exit_text:
                issues.append(f"exit state missing '{EXIT_ENTRY_HEADING}' — a non-final shard must "
                              f"hand the next shard an entry contract")
            else:
                start_block = section_block(exit_text, EXIT_MUST_START,
                                            [EXIT_MUST_NOT, "## ", "\n---"])
                not_block = section_block(exit_text, EXIT_MUST_NOT,
                                          ["## ", "\n---"])
                start_ok = EXIT_MUST_START in exit_text and start_block.strip() != ""
                not_ok = EXIT_MUST_NOT in exit_text and not_block.strip() != ""
                entry_contract_ok = start_ok and not_ok
                if not start_ok:
                    issues.append(f"exit state '{EXIT_MUST_START}' is missing or empty — the next "
                                  f"shard has nothing to handshake against")
                if not not_ok:
                    issues.append(f"exit state '{EXIT_MUST_NOT}' is missing or empty — the "
                                  f"forbidden-state half of the handshake is unset")
        else:
            entry_contract_ok = True  # final shard: no next-shard contract owed

    intact = not issues
    return {
        "ok": True,
        "status": "pass" if intact else "hold",
        "prompt_path": str(prompt),
        "project_root": str(project),
        "scene_number": scene_number,
        "shard_number": shard_number,
        "beat_name": beat_name,
        "state_diff_passed": state_diff_passed,
        "agent_inputs": agent_inputs,
        "agent_inputs_ok": agent_inputs_ok,
        "prompt_sections_present": [s.rstrip(":") for s in sections_present],
        "prompt_sections_ok": sections_ok,
        "temporal_duration": temporal_duration,
        "temporal_duration_ok": temporal_ok,
        "exit_state_path": str(exit_path) if exit_path else None,
        "exit_state_present": exit_present,
        "exit_state_identity_match": exit_identity_match,
        "exit_state_sections_ok": exit_core_ok,
        "entry_contract_required": entry_contract_required,
        "entry_contract_ok": entry_contract_ok,
        "scene_brief_path": str(brief_path) if brief_path else None,
        "scene_brief_checked": scene_brief_checked,
        "shard_count": shard_count,
        "shard_in_range": shard_in_range,
        "beat_in_table": beat_in_table,
        "beat_duration": beat_duration,
        "duration_matches_beat": duration_matches_beat,
        "warnings": warnings,
        "issues": issues,
    }, 0 if intact else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Deterministic structural check for a compiled CPM shard")
    p.add_argument("--prompt", required=True, type=Path,
                   help="path to the Scene_XX_Shard_Y_prompt.md file")
    p.add_argument("--project", type=Path,
                   help="path to the CPM project root (the folder holding .cpm/, Bible/, "
                        "Production/, Output/). Default: inferred from the prompt path "
                        "(project/Output/Prompts/Scene_XX_Shard_Y_prompt.md).")
    args = p.parse_args(argv)

    result, code = check(args.prompt, args.project)
    print(json.dumps(result, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())

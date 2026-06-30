#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""validate_handshake — deterministic structural floor for a single CPM continuity boundary.

Validate-mode plumbing for cpm-handshake-test. It judges one adjacent boundary — shard A (N) to
shard B (N+1) of the same scene — confirming only what a machine can judge WITHOUT reading
meaning: that the pair is locatable and identity-matched, that A handed a real entry contract,
and that the unambiguous continuity tokens that contract carries survive into B's compiled
prompt. It reads shard A's exit state and shard B's compiled prompt; it never reads or grades
substance the way a human does.

  1. Locate & identity-match the adjacent pair: shard A's exit state exists; shard B's compiled
     prompt exists; A and B name the SAME scene; B is shard A + 1 (a true N -> N+1 boundary).
  2. Entry-contract presence: A's exit state carries a non-empty "## Entry Contract for Next
     Shard" with non-empty "### MUST Start With:" and "### MUST NOT Show:" subsections. A final
     shard owes no next-shard contract, so a final A is reported as a NO-BOUNDARY (not an error,
     not a hold) — there is nothing to handshake.
  3. MUST-Start-With token presence: every machine-extractable continuity token in A's MUST Start
     With block (hex color, [Asset: ID], a RIGHT/LEFT hand marker, a lens spec) appears in B's
     prompt body. A missing token is the carried-object / feature / spatial break the test exists
     to catch.
  4. MUST-NOT-Show floor: NO token A forbids appears in B's prompt body. One forbidden token
     present fails the boundary at the same hardness as a missing required one.
  5. Signature-lighting continuity: the signature hex on A's exit-state "Lighting Position:" line
     appears in B's [Environment/Lighting] section.

Finality is read from the scene brief's shard_count when one is machine-readable; otherwise it
DEGRADES GRACEFULLY to the presence of A's entry contract (a shard that hands no contract is
treated as terminal) and a single warning is emitted — never a hold.

The five continuity CRITERIA themselves — carried-object, distinctive-feature, style/lighting,
spatial-position, and autonomy — are graded by the workflow's prose against the contract, at
equal hardness. This script is the structural floor beneath that grade: it reports which tokens
are present, missing, or forbidden, not whether the boundary "feels" continuous.

Output: one JSON object on stdout.
Exit codes: 0 = pass or no-boundary (warnings allowed); 1 = hold (a continuity break the floor
            caught); 2 = usage/precondition error (the message names the fix).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# The next-shard handshake headings, in lockstep with cpm-shard-generation's exit-state template
# and references/handshake-test-contract.md.
EXIT_ENTRY_HEADING = "## Entry Contract for Next Shard"
EXIT_MUST_START = "### MUST Start With:"
EXIT_MUST_NOT = "### MUST NOT Show:"
# The exit-state line that carries the scene's signature lighting baseline.
LIGHTING_POSITION_RE = re.compile(r"(?m)^\s*-\s*\*\*Lighting Position:\*\*(.*)$")

# The four unambiguous, machine-extractable continuity-token forms. Each is a carrier the
# production's own templates already use, so extracting them reads structure, not meaning:
#   hex   — a Palette color (#RRGGBB); the lighting / style signature.
#   asset — a [Asset: ID] reference; the canonical way a recurring object/inventory is named.
#   hand  — an uppercase RIGHT / LEFT marker; the LEFT/RIGHT specificity the module is built on.
#   lens  — a focal-length spec (e.g. 85mm); part of the spatial/framing handshake.
HEX_RE = re.compile(r"#[0-9A-Fa-f]{6}")
ASSET_RE = re.compile(r"\[Asset:\s*([^\]]+)\]")
HAND_RE = re.compile(r"\b(?:RIGHT|LEFT)\b")
LENS_RE = re.compile(r"\b\d{2,3}mm\b")

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)
SCALAR_RE = re.compile(r"^([A-Za-z0-9_]+):\s*(.*)$")
LIST_ITEM_RE = re.compile(r"^\s+-\s+(.*)$")


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

    Handles scalar keys, block lists (`  - item`), and inline lists (`[a, b]`). Stdlib only — no
    third-party YAML dependency, so this stays in lockstep with validate_shard.py's discipline.
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


def extract_tokens(block: str):
    """Return an ordered, de-duplicated list of (kind, value) continuity tokens in `block`."""
    seen = set()
    out = []

    def add(kind: str, value: str):
        value = value.strip()
        if not value:
            return
        key = (kind, value)
        if key not in seen:
            seen.add(key)
            out.append((kind, value))

    for v in HEX_RE.findall(block):
        add("hex", v)
    for v in ASSET_RE.findall(block):
        add("asset", v)
    for v in HAND_RE.findall(block):
        add("hand", v)
    for v in LENS_RE.findall(block):
        add("lens", v)
    return out


def token_in(text: str, kind: str, value: str) -> bool:
    """Is the token present in `text`? Hand/lens markers are whole-word; hex/asset are literal."""
    if kind in ("hand", "lens"):
        return re.search(r"\b" + re.escape(value) + r"\b", text) is not None
    return value in text


def _display(tokens) -> list:
    """Render (kind, value) token tuples as readable 'kind:value' strings."""
    return [f"{kind}:{value}" for kind, value in tokens]


def read_shard_count(brief_path: Path):
    """Read an integer shard_count from a scene brief's frontmatter, or None when not readable."""
    if not brief_path.is_file():
        return None
    fm = parse_frontmatter(brief_path.read_text(encoding="utf-8"))
    if not fm:
        return None
    try:
        return int(str(fm.get("shard_count")))
    except (TypeError, ValueError):
        return None


def check(project: Path, scene: str, shard_a: int,
          exit_a: Path | None, prompt_b: Path | None, brief: Path | None) -> tuple[dict, int]:
    project = Path(project)
    scene_str = scene.zfill(2) if str(scene).isdigit() else str(scene)
    shard_a_int = int(shard_a)
    shard_b_int = shard_a_int + 1

    if exit_a is None:
        exit_a = (project / "Production" / "Scenes" / f"Scene_{scene_str}"
                  / "state" / f"shard_{shard_a_int}_exit_state.md")
    if prompt_b is None:
        prompt_b = (project / "Output" / "Prompts"
                    / f"Scene_{scene_str}_Shard_{shard_b_int}_prompt.md")
    if brief is None:
        brief = (project / "Production" / "Scenes" / f"Scene_{scene_str}" / "scene-brief.md")
    exit_a, prompt_b, brief = Path(exit_a), Path(prompt_b), Path(brief)

    if not exit_a.is_file():
        return err(f"shard A exit state not found: {exit_a} — pass --shard-a with a generated "
                   f"shard (its shard_N_exit_state.md must exist), or override with --exit-a"), 2

    issues: list[str] = []
    warnings: list[str] = []

    # ---- read shard A's exit state ----
    a_text = exit_a.read_text(encoding="utf-8")
    a_fm = parse_frontmatter(a_text) or {}
    a_scene = a_fm.get("sceneNumber")
    a_shard = a_fm.get("shardNumber")

    entry_contract_present = EXIT_ENTRY_HEADING in a_text
    start_block = (section_block(a_text, EXIT_MUST_START, [EXIT_MUST_NOT, "## ", "\n---"])
                   if EXIT_MUST_START in a_text else "")
    not_block = (section_block(a_text, EXIT_MUST_NOT, ["## ", "\n---"])
                 if EXIT_MUST_NOT in a_text else "")
    entry_contract_nonempty = (entry_contract_present
                               and start_block.strip() != "" and not_block.strip() != "")

    # ---- signature lighting hex from A's "Lighting Position:" line ----
    signature_hex = None
    lm = LIGHTING_POSITION_RE.search(a_text)
    if lm:
        hm = HEX_RE.search(lm.group(1))
        signature_hex = hm.group(0) if hm else None

    # ---- finality: scene brief shard_count is authoritative; degrade to contract presence ----
    shard_count = read_shard_count(brief)
    if shard_count is not None:
        a_is_final = shard_a_int >= shard_count
        finality_source = "scene_brief"
    else:
        a_is_final = not entry_contract_nonempty
        finality_source = "entry_contract_presence"
        warnings.append(f"scene brief has no machine-readable shard_count at {brief} — finality "
                        f"inferred from shard A's Entry Contract presence")

    boundary_testable = not a_is_final
    b_present = None
    b_scene = b_shard = None
    scene_match = adjacent = None
    must_start_tokens: list = []
    must_start_present: list = []
    must_start_missing: list = []
    must_not_tokens: list = []
    must_not_violations: list = []
    signature_hex_in_b_lighting = None

    if a_is_final:
        # A final shard owes no next-shard contract: this is not a testable handshake boundary.
        if entry_contract_nonempty and finality_source == "scene_brief":
            warnings.append(f"shard {shard_a_int} is the scene's final shard "
                            f"(shard_count={shard_count}) yet still carries an Entry Contract — "
                            f"the final shard owes none; boundary treated as not testable")
        status = "no_boundary"
    else:
        # A non-final shard must hand a real contract for the next shard to honor.
        if not entry_contract_nonempty:
            issues.append("shard A is not the scene's final shard but its exit state carries no "
                          "non-empty Entry Contract (MUST Start With / MUST NOT Show) — there is "
                          "nothing for shard B to handshake against")

        b_present = prompt_b.is_file()
        if not b_present:
            issues.append(f"shard B compiled prompt not found: {prompt_b} — generate shard "
                          f"{shard_b_int} before testing this boundary, or override with --prompt-b")
        else:
            b_text = prompt_b.read_text(encoding="utf-8")
            b_body = body_after_frontmatter(b_text)
            b_fm = parse_frontmatter(b_text) or {}
            b_scene = b_fm.get("sceneNumber")
            b_shard = b_fm.get("shardNumber")

            # ---- identity & adjacency ----
            scene_match = str(a_scene) == str(b_scene)
            if not scene_match:
                issues.append(f"identity mismatch: shard A is Scene {a_scene}, shard B prompt is "
                              f"Scene {b_scene} — a handshake boundary lives within one scene")
            if a_shard is not None and str(a_shard) != str(shard_a_int):
                issues.append(f"shard A exit state shardNumber {a_shard} does not match the "
                              f"requested --shard-a {shard_a_int} — the pair is mislabeled")
            try:
                adjacent = int(str(b_shard)) == shard_a_int + 1
            except (TypeError, ValueError):
                adjacent = False
            if not adjacent:
                issues.append(f"shards are not adjacent: shard A is {shard_a_int}, shard B prompt "
                              f"is shard {b_shard} — a handshake tests N against N+1 (expected "
                              f"{shard_b_int})")

            # ---- token floor (only meaningful when A handed a real contract) ----
            if entry_contract_nonempty:
                start_tokens = extract_tokens(start_block)
                must_start_tokens = _display(start_tokens)
                present = [(k, v) for k, v in start_tokens if token_in(b_body, k, v)]
                missing = [(k, v) for k, v in start_tokens if not token_in(b_body, k, v)]
                must_start_present = _display(present)
                must_start_missing = _display(missing)
                if missing:
                    issues.append("MUST Start With continuity token(s) absent from shard B "
                                  "prompt: " + ", ".join(must_start_missing))

                not_tokens = extract_tokens(not_block)
                must_not_tokens = _display(not_tokens)
                violations = [(k, v) for k, v in not_tokens if token_in(b_body, k, v)]
                must_not_violations = _display(violations)
                if violations:
                    issues.append("MUST NOT Show token(s) present in shard B prompt: "
                                  + ", ".join(must_not_violations))

            # ---- signature-lighting continuity ----
            if signature_hex:
                b_light = section_block(b_body, "[Environment/Lighting]",
                                        ["[Temporal Constraint]", "**Build Notes:**", "\n---"])
                signature_hex_in_b_lighting = signature_hex in b_light
                if not signature_hex_in_b_lighting:
                    issues.append(f"signature lighting hex {signature_hex} from shard A's Lighting "
                                  f"Position does not appear in shard B's [Environment/Lighting]")
            else:
                warnings.append("shard A exit state has no hex on its Lighting Position line — the "
                                "signature-lighting continuity check was skipped")

        status = "hold" if issues else "pass"

    code = 0 if status in ("pass", "no_boundary") else 1
    return {
        "ok": True,
        "status": status,
        "project_root": str(project),
        "scene_number": scene_str,
        "shard_a": shard_a_int,
        "shard_b": shard_b_int,
        "exit_a_path": str(exit_a),
        "prompt_b_path": str(prompt_b),
        "scene_brief_path": str(brief),
        "boundary_testable": boundary_testable,
        "a_is_final": a_is_final,
        "finality_source": finality_source,
        "shard_count": shard_count,
        "a_scene_number": a_scene,
        "a_shard_number": a_shard,
        "b_scene_number": b_scene,
        "b_shard_number": b_shard,
        "b_present": b_present,
        "scene_match": scene_match,
        "adjacent": adjacent,
        "entry_contract_present": entry_contract_present,
        "entry_contract_nonempty": entry_contract_nonempty,
        "must_start_with_tokens": must_start_tokens,
        "must_start_present": must_start_present,
        "must_start_missing": must_start_missing,
        "must_not_show_tokens": must_not_tokens,
        "must_not_violations": must_not_violations,
        "signature_hex": signature_hex,
        "signature_hex_in_b_lighting": signature_hex_in_b_lighting,
        "warnings": warnings,
        "issues": issues,
    }, code


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Deterministic structural floor for one CPM continuity boundary (N -> N+1)")
    p.add_argument("--project", required=True, type=Path,
                   help="path to the CPM project root (the folder holding .cpm/, Bible/, "
                        "Production/, Output/)")
    p.add_argument("--scene", required=True,
                   help="scene number, zero-padded two digits (e.g. 07)")
    p.add_argument("--shard-a", required=True, type=int, dest="shard_a",
                   help="shard A's number (N); shard B is inferred as N+1")
    p.add_argument("--exit-a", type=Path, dest="exit_a",
                   help="override path to shard A's exit state "
                        "(default: Production/Scenes/Scene_XX/state/shard_N_exit_state.md)")
    p.add_argument("--prompt-b", type=Path, dest="prompt_b",
                   help="override path to shard B's compiled prompt "
                        "(default: Output/Prompts/Scene_XX_Shard_{N+1}_prompt.md)")
    p.add_argument("--brief", type=Path,
                   help="override path to the scene brief (default: "
                        "Production/Scenes/Scene_XX/scene-brief.md). Read only for shard_count.")
    args = p.parse_args(argv)

    result, code = check(args.project, args.scene, args.shard_a,
                         args.exit_a, args.prompt_b, args.brief)
    print(json.dumps(result, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())

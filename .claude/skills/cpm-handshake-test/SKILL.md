---
name: cpm-handshake-test
description: Proves CPM holds continuity across shard boundaries — grades one adjacent boundary or runs the full three-consecutive-pass validation suite for a scene, read-only, writing test reports. Use when the user says "handshake test", "test a boundary", "validate continuity", "run the validation suite", "is CPM validated", or "check the handshake".
---

# CPM Handshake Test

This workflow proves CPM holds continuity across a shard boundary — the seam where one shard's exit state hands the next shard its opening. Act as the continuity tester running the proof headlessly: the production is the subject under test, and the test reads it without ever changing it. It consumes two already-generated artifacts — shard A's exit state (its `## Entry Contract for Next Shard`) and shard B's compiled prompt — and writes a test report; it never edits a shard, an exit state, the manifest, or the Slate, because a test that mutates its subject proves nothing. What it proves is narrow and total: that everything shard B needed to stay continuous travelled to it through shard A's entry contract alone, with no human leaning in to remind the generator. Two capabilities sit on one engine: a **Handshake Test Run** grades a single adjacent boundary on the five continuity criteria and the MUST-NOT-Show floor; a **Validation Suite** chains that test across a scene and renders the binding verdict under the three-consecutive-pass law — three consecutive boundaries PASS and CPM is VALIDATED, any FAIL breaks the streak and it is NOT VALIDATED. The structural floor is `scripts/validate_handshake.py`, which judges only what a machine can without reading meaning; the five criteria themselves are graded by reading the artifacts against the contract. Grade every criterion and the floor at the same hardness: a boundary is PASS only when all five read PASS and nothing forbidden appears.

## Resolution rules

- Bare paths and `{skill-root}` (e.g. `references/handshake-test-contract.md`) resolve from this skill's installed directory.
- `{project-root}` → the BMad framework working directory (the repository root), distinct from the CPM production project below; the validate command runs from here.
- `{project}` → the located CPM production project root — the folder holding `.cpm/`, `Bible/`, `Production/`, and `Output/` — distinct from `{project-root}`.
- `{XX}` → the scene number as a zero-padded two-digit string (`01`, `07`).
- `{N}` → shard A's number as the bare integer (`1`, not `01`); `{N+1}` → shard B's number, the adjacent next shard.
- `cpm-handshake-test` → the skill directory's basename.

## On Activation

1. Load config from `{project-root}/_bmad/config.yaml` (and `config.user.yaml` if present; root and `cpm` section). Apply `{user_name}`, `{communication_language}`, `{document_output_language}` with sensible defaults; never block on missing config.
2. Resolve the `workflow` block: run `uv run {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`. If it fails, merge base → team → user yourself — `{skill-root}/customize.toml`, `{project-root}/_bmad/custom/cpm-handshake-test.toml`, `{project-root}/_bmad/custom/cpm-handshake-test.user.toml` (scalars override, arrays append). Reference resolved values as `{workflow.<name>}` below; never hardcode a path beside a declared scalar.
3. Bind `{project}` before any `{project}/...` path is read or written — use the production named in the conversation, or glob for a folder containing `.cpm/` under the productions base and confirm the match with the user; never guess when more than one exists. **If no `.cpm/` scaffold is found, degrade — do not error:** route the user to the new-project workflow, because there is no production to test a boundary in.
4. Route by capability from what the user said — a **Handshake Test Run** (grade one adjacent boundary; the default when a single shard or a specific boundary is named) or the **Validation Suite** (chain the test across a scene and render the CPM-VALIDATED verdict; the default when the user asks whether CPM is validated or names a whole scene). These are not interchangeable; if which one is unclear, ask the single question that settles it — one boundary, or the whole scene — before doing anything.

All replies use `{communication_language}`; generated file content uses `{document_output_language}`.

## Handshake Test Run

Read first, every time — you cannot grade what you have not read: `{workflow.handshake_test_contract}` (the five criteria, the MUST-NOT-Show floor, the by-hand method, and the same-hardness rule you hold the boundary to), the two cross-skill artifact shapes you consume — `skills/cpm-shard-generation/assets/exit-state.template.md` (shard A's exit state and its `## Entry Contract for Next Shard`) and `skills/cpm-shard-generation/assets/shard-prompt.template.md` (shard B's six bracketed sections) — the per-shard check this generalizes, `skills/cpm-script-supervisor/references/handshake-review.md` (the two-term contract, widened here to five criteria), and `{workflow.handshake_report_template}` (the report you will write). Keep `{project}/Architecture/Style_Guide.md` and `Palette.md` at hand for the substance of criterion 3, and read `{project}/.cpm/config.yaml` for the `validation.require_style_compliance` gate that governs that criterion's Style-Guide check — when it is on (its default if the key is absent), shard B's `[Environment/Lighting]` must honour the Style Guide's placement, not merely carry the bare signature hex.

**The precondition — both shards must exist.** Identify the boundary: scene `{XX}` and shard A `{N}` (shard B is `{N+1}`). A boundary can only be tested once shard A's exit state and shard B's prompt both exist; if the project has no generated shards yet, there is nothing to test — route the user to shard-generation. The structural floor names a missing artifact precisely, so let it run first.

**Run the structural floor.** From `{project-root}`, prefer `python`; fall back to `uv run` if the interpreter is unavailable:

```
python skills/cpm-handshake-test/scripts/validate_handshake.py --project "{project}" --scene {XX} --shard-a {N}
```

It writes nothing and returns one JSON object on stdout; the exit code is `0 = pass or no_boundary` (warnings allowed), `1 = hold` (a continuity break the floor caught), or `2 = usage/precondition error` (the message names the fix — most often shard A's exit state is absent at that path). `--project`, `--scene`, and `--shard-a` are required; `--exit-a`, `--prompt-b`, and `--brief` override the default paths when a production deviates from the standard tree. The floor owns the deterministic structure: it locates and identity-matches the adjacent pair (shard A is `{N}`, shard B is `{N+1}`, the same scene), confirms shard A handed a non-empty entry contract or is the scene's final shard, confirms each machine-extractable MUST Start With token (a hex code, an `[Asset: ID]`, a RIGHT/LEFT marker, a lens spec) survives into shard B, confirms no MUST NOT Show token appears in shard B, and confirms shard A's signature lighting hex appears in shard B's `[Environment/Lighting]`. If neither `python` nor `uv run` is available, grade the structural floor by hand against `{workflow.handshake_test_contract}` using the same checks.

**Branch on the floor's `status`:**

- **`status: error` (exit 2)** — a precondition failed; there is nothing to grade. Do not emit PASS or FAIL. Surface the error (it names the fix) and route to shard-generation to produce the missing shard:

  > **NO BOUNDARY TO TEST.** {the error the floor reported, which names the fix}. A handshake needs both shards present — shard A's exit state and shard B's compiled prompt. Generate the missing shard, then re-run the test.

- **`status: no_boundary` (exit 0)** — shard A is the scene's final shard; it owes no next-shard contract, so this is **not a testable handshake boundary**. This is graceful, not a failure: report it plainly, do not grade PASS or FAIL, and do not write a pass/fail report. If the Validation Suite called this, the chain ends here.

- **`status: hold` (exit 1)** — the floor caught a structural continuity break (`issues` is non-empty: a missing required token, a forbidden token present, a missing signature hex, an identity or adjacency mismatch, or an empty contract). This is a FAIL at the floor; carry every `issues` entry into the report's Blocking Continuity Breaks and grade the affected criteria FAIL.

- **`status: pass` (exit 0)** — the structural floor holds. Now grade the substance the floor cannot read.

**Grade the five continuity criteria — the reading judgment, at the same hardness.** With the floor's token report in hand (`must_start_present` / `must_start_missing`, `must_not_violations`, `signature_hex_in_b_lighting`), read shard A's exit state and shard B's prompt against `{workflow.handshake_test_contract}` and grade each criterion PASS or FAIL:

1. **Carried-object / inventory** — every object shard A is Holding, and every object in its MUST Start With, is present in shard B in the SAME hand. The floor confirms the `[Asset: ID]` and RIGHT/LEFT token survive; you confirm it is genuinely the same object in the same hand, not a coincidental marker.
2. **Distinctive-feature / identity** — every immutable LEFT/RIGHT-specific feature (the scar, the permanent crease) appears in shard B's `[Subject/Asset]` anchors on the same side. The floor sees only the side marker; you confirm the feature itself is named, not a stray hand reference.
3. **Style / lighting** — shard B's `[Environment/Lighting]` carries shard A's signature hex in the same placement and, when the project's `validation.require_style_compliance` gate is on (its default), honours the Style Guide. The floor confirms the hex is present; you confirm the placement and the visual language hold.
4. **Spatial-position** — shard B opens on the framing, screen placement, and facing shard A's MUST Start With mandates. The floor confirms the lens and framing tokens survive; you confirm they genuinely open the shard rather than trailing it.
5. **Autonomy — no human reminder** — every continuous element above traces to a line shard A actually wrote in its exit state or entry contract; nothing shard B got right needed an out-of-band human re-injection. No token can prove this — map each honoured element to its source line by reading. If shard B is continuous only because a human hand-fed the detail, this FAILS even when 1–4 read clean.

Then the **MUST-NOT-Show floor**: nothing on shard A's MUST NOT Show appears in shard B (`must_not_violations` empty). A single forbidden element present fails the boundary at the same hardness as a missing required one.

**Write the report.** Render `{workflow.handshake_report_template}` to `{project}/Production/Validation/Scene_{XX}_Shard_{N}_handshake.md` — fill the per-criterion table, list every FAIL in Blocking Continuity Breaks, and set the verdict. The verdict reads **PASS only when all five criteria read PASS and the floor holds** — the Blocking Continuity Breaks list is empty if and only if the verdict is PASS; any criterion FAIL or any forbidden element present forces FAIL. The new-project scaffold does not carve a dedicated validation folder, so reports live under `{project}/Production/Validation/` — create it if absent and name that gap in the finalize message. Then run the reviewer gate below and finalize.

## Validation Suite

Read first, every time — you cannot grade what you have not read: `{workflow.handshake_test_contract}` (especially the three-consecutive-pass law you apply here), the same two cross-skill artifact shapes — `skills/cpm-shard-generation/assets/exit-state.template.md` and `skills/cpm-shard-generation/assets/shard-prompt.template.md` — the per-shard check `skills/cpm-script-supervisor/references/handshake-review.md`, `{workflow.handshake_report_template}` (each boundary still gets its own single-boundary report), and `{workflow.validation_suite_report_template}` (the scene-wide report you will write). Keep `{project}/Architecture/Style_Guide.md` and `Palette.md` at hand for criterion 3, and read `{project}/.cpm/config.yaml`'s `validation.require_style_compliance` gate exactly as the Handshake Test Run procedure does.

**Enumerate the scene's boundaries.** Read `shard_count` (`S`) from the scene brief at `{project}/Production/Scenes/Scene_{XX}/scene-brief.md`; a scene of `S` shards offers `S-1` testable boundaries — one per adjacent pair: Shard 1 → Shard 2, Shard 2 → Shard 3, and so on, the final shard owing none. **If the brief carries no machine-readable `shard_count`, degrade — do not error:** count the generated `state/shard_{N}_exit_state.md` files, treat the highest as `S`, and name that degraded basis in the report.

**Run the single-boundary logic across consecutive boundaries.** For each boundary in order from Shard 1, run the **Handshake Test Run** procedure above — the structural floor (`validate_handshake.py --shard-a N`) followed by the five-criteria grade — producing each boundary's single-boundary verdict and its handshake report. A `no_boundary` result (the scene's final shard) ends the chain gracefully; it is neither PASS nor FAIL. An `error` status (a missing shard, an absent exit state or prompt — exit 2) is not a FAIL but a gap in the evidence: surface it and route to shard-generation to produce the missing artifact, and do not continue the chain, because a suite with an ungenerated boundary cannot be declared VALIDATED. Track the **consecutive-PASS streak**: a PASS extends it, a FAIL breaks it and restarts the count at zero.

**Apply the three-consecutive-pass law.** CPM is **VALIDATED** only when three CONSECUTIVE boundaries PASS, with no FAIL between them. Any FAIL breaks the streak and the verdict is **NOT VALIDATED**. A scene that cannot field three consecutive testable boundaries — fewer than three exist (`S-1 < 3`, i.e. fewer than four shards), or a `no_boundary` ended the chain early — **cannot be declared VALIDATED.** That is not a continuity FAIL but insufficient evidence: report NOT VALIDATED and name the gap — how many boundaries the scene offers and how many more shards continuity needs to prove out.

**Write the suite report.** Render `{workflow.validation_suite_report_template}` to `{project}/Production/Validation/Scene_{XX}_validation_suite.md` — fill the per-pass table (each boundary's result and the running streak), list every FAILED boundary in Blocking Failures, complete Evidence Sufficiency, and set the verdict. The verdict reads **VALIDATED only when the Blocking Failures list is empty, three consecutive boundaries PASSED, and the scene fielded enough boundaries to clear the bar**; otherwise NOT VALIDATED. Place it under `{project}/Production/Validation/` (create the folder if absent and name the gap). Then run the reviewer gate below and finalize.

## Reviewer gate and finalize

After a Handshake Test Run or a Validation Suite, confirm the result independently before declaring a verdict: re-run `validate_handshake.py` over the graded boundary (or each boundary in the suite) as a reviewer gate — delegate it to a subagent for fresh eyes when subagents are available, instructing it to run the command(s), judge the five criteria and the MUST-NOT-Show floor against `{workflow.handshake_test_contract}`, and return ONLY the verdict (PASS or FAIL per boundary; VALIDATED or NOT VALIDATED for the suite, with the failing criteria named). A FAIL or NOT VALIDATED becomes the blocking slot in the report and sends production back to shard-generation; only a clean reviewer pass clears the verdict.

Once confirmed, finalize for the filmmaker in `{communication_language}`: state the report path under `{project}/Production/Validation/` (noting that the project scaffold carries no dedicated validation folder, so the workflow created `Production/Validation/`), give the verdict plainly, and point to the next move — for a FAIL, the exact boundary to regenerate through shard-generation and why; for the suite, either that CPM is VALIDATED for this scene, or how many more clean consecutive boundaries the proof still needs.

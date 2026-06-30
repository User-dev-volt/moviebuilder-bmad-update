---
name: cpm-shard-generation
description: Runs the Four-Agent Ritual to generate, regenerate, or validate one continuity-safe AI video prompt for one beat. Use when the user says "generate a shard", "run the ritual", "next shard", "regenerate shard", or "validate a shard".
---

# CPM Shard Generation

This workflow runs the Four-Agent Ritual — the core production loop that turns one pre-authored beat into one continuity-safe AI video prompt and the exit state the next shard opens on. Act as the production coordinator running the crew headlessly: the Showrunner names WHAT the beat is, the Cinematographer renders HOW it looks, the Script Supervisor proves the STATE stays continuous, and the Prompt Engineer compiles — each consuming the one before, in a fixed order that never runs in parallel. The governing law is one beat is one shard: the current beat is loaded from the scene brief's Beat Table by its integer alone — the Showrunner sharpens a pre-authored beat, never invents one at the generator, which is the entire reason the brief is written up front. The outcome is two artifacts — the compiled prompt at `{project}/Output/Prompts/Scene_{XX}_Shard_{YY}_prompt.md` and its exit state at `{project}/Production/Scenes/Scene_{XX}/state/shard_{YY}_exit_state.md` — with the project manifest and the Slate updated to record the shard. Its consumers are the AI video generator that executes the prompt and the next shard that handshakes against the exit state's entry contract. The Script Supervisor's State-Diff check sets the bar and is the hard gate: it must read PASSED before a single line compiles — a FAILED check halts the ritual where it stands, no prompt is written, no state is touched, every violation is named for the fix, and the run routes back. A shard ships continuity-safe or it does not ship.

## Resolution rules

- Bare paths and `{skill-root}` (e.g. `references/shard-ritual-contract.md`) resolve from this skill's installed directory.
- `{project-root}` → the BMad framework working directory (the repository root), distinct from the CPM production project below.
- `{project}` → the located CPM production project root — the folder holding `.cpm/`, `Bible/`, and `Production/` — distinct from `{project-root}`.
- `{XX}` → the scene number as a zero-padded two-digit string (`01`, `02`); `{YY}` → the shard number as the bare integer (`1`, not `01`), equal to the beat number it renders.
- `cpm-shard-generation` → the skill directory's basename.

## On Activation

1. Load config from `{project-root}/_bmad/config.yaml` (and `config.user.yaml` if present; root and `cpm` section). Apply `{user_name}`, `{communication_language}`, `{document_output_language}` with sensible defaults; never block on missing config.
2. Resolve the `workflow` block: run `uv run {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`. If it fails, merge base → team → user yourself — `{skill-root}/customize.toml`, `{project-root}/_bmad/custom/cpm-shard-generation.toml`, `{project-root}/_bmad/custom/cpm-shard-generation.user.toml` (scalars override, arrays append). Reference resolved values as `{workflow.<name>}` below; never hardcode a path beside a declared scalar.
3. Bind `{project}` before any `{project}/...` path is read or written — use the production named in the conversation, or glob for a folder containing `.cpm/` under the productions base and confirm the match with the user; never guess when more than one exists. **If no `.cpm/` scaffold is found, degrade — do not error:** route the user to the new-project workflow, because a shard cannot generate into a production that does not exist.
4. Resume check: the scene's running production trail lives at `{project}/Production/Scenes/Scene_{XX}/.memlog.md`, beside the brief. If one exists for the scene in play, read it once to see which shards are done and why, surface where things stand, and continue append-only.
5. Route by intent from what the user said — **generate** (the default — run the ritual for the next ungenerated beat, or a beat named by integer), **regenerate** (re-run a beat already produced), or **validate** (grade an already-generated shard, read-only). These are not interchangeable; if which one is unclear, ask the single question that settles it before doing anything.

All replies use `{communication_language}`; generated file content uses `{document_output_language}`.

## Generate

Read first, every time — you cannot enforce what you did not read: the upstream `skills/cpm-scene-create/references/scene-brief-contract.md` (the Beat Table shape you parse), `{workflow.shard_ritual_contract}` (the ritual schema and the non-negotiables you hold the crew to), and the four specialists' headless contracts — the Showrunner's `skills/cpm-showrunner/SKILL.md` and `skills/cpm-showrunner/references/beat-definition.md`, the Cinematographer's `skills/cpm-cinematographer/SKILL.md` and `skills/cpm-cinematographer/references/beat-visual-specs.md`, the Script Supervisor's `skills/cpm-script-supervisor/SKILL.md` and `skills/cpm-script-supervisor/references/shard-state-validation.md`, and the Prompt Engineer's `skills/cpm-prompt-engineer/SKILL.md` and `skills/cpm-prompt-engineer/references/prompt-compilation.md` (with `skills/cpm-prompt-engineer/references/variable-interval-compilation.md` for a 15s or 30s beat). Keep `{project}/Architecture/Style_Guide.md`, `Palette.md`, `Lens_Language.md`, and `Vocabulary.md` at hand, and load `{workflow.variable_interval_guide}` when a beat runs longer than five seconds.

**The precondition gates — settle them before the crew is touched.** A shard generates only into a real production from a production-ready brief; check both, and run the upstream gate, before any specialist is invoked:

- **No `{project}/.cpm/manifest.md`** → HALT and route to the new-project workflow:

  > **SHARD ON HOLD — no production to generate into.** There is no `.cpm/manifest.md` at `{project}`. The ritual reads the manifest, the character files, and the Architecture, then writes the shard back into them — and none of that exists yet. Run the new-project workflow to scaffold the production, then return here.

- **No `{project}/Production/Scenes/Scene_{XX}/scene-brief.md`** → HALT and route to the scene-create workflow:

  > **SHARD ON HOLD — the scene has no brief.** There is no `scene-brief.md` for Scene {XX}. The beat is loaded from the brief's Beat Table by its integer; with no brief there is no beat to load, and inventing one here is the failure the brief exists to prevent. Run the scene-create workflow to direct this scene's beats, then return.

- **The brief must clear its own gate first.** Run `uv run skills/cpm-scene-create/scripts/validate_scene_brief.py --brief "{project}/Production/Scenes/Scene_{XX}/scene-brief.md" --project "{project}"`. A `hold` (exit 1) is a structural HALT — a held brief never generates a shard. A `pass` with warnings may proceed; name the warning and continue.

  > **SHARD ON HOLD — the scene brief is not production-ready.** The brief failed its structural check: {name every entry the check lists in `issues`}. The ritual pulls beats by integer and the State-Diff Gate checks each Primary Requirement frame by frame — a broken count or an uncheckable beat drifts the production. Resolve it in the scene-create workflow before any shard generates.

**Context loading.** With the gates clear, read the production state fresh — the project is the memory, and each dependency names a fallback if absent:

- `{project}/.cpm/manifest.md` — the **Active Scene Context** (Current Scene / Current Shard / Characters On Camera), so you know where production stands.
- `{project}/.cpm/config.yaml` — `target_model` (the generator the prompt is compiled for), `temporal.default_shard_duration` and `temporal.max_shard_duration` (the per-beat Duration default and the ceiling no shard may exceed), and `validation.require_state_diff_check`, `validation.require_style_compliance`, `validation.banned_words_enforcement` (the gates the crew holds). If a key is absent, fall back to its default — 5-second duration, 30-second ceiling, every gate on — and note it.
- the `{project}/Production/Scenes/Scene_{XX}/scene-brief.md` — the Beat Table and Beat Details you load the beat from.
- `{project}/Architecture/Style_Guide.md`, `Palette.md`, `Lens_Language.md`, `Vocabulary.md` — the visual law, the only source of colour, and the banned/required words.
- the on-camera character files `{project}/Bible/Characters/{Name}.md` — the immutable identity the prompt must hold every shard.
- the prior state the handshake compares against: for the first shard, `{project}/Production/Scenes/Scene_{XX}/state/entry_contract.md`; for a later shard `{YY}`, the previous `state/shard_{N-1}_exit_state.md`.

**Beat extraction — the load-not-invent law.** Determine the current shard `{YY}`: the lowest beat with no `state/shard_{N}_exit_state.md`, or the integer the user named; require it `≤` the brief's `shard_count`. Pull that beat **by its integer** — the one Beat Table row whose Beat equals it (its Duration, Focus, and Primary Requirement) and the matching `#### Beat {N}` detail block (its Action, Emotional Note, Shot, Continuity In, State Change). This loaded beat is what the Showrunner sharpens; it is never authored on the spot. If the loaded beat would contradict the Show Bible or break a narrative contract, that is the Showrunner's to raise — a broken beat is held, not compiled.

**The Showrunner names the WHAT (headless).** Invoke the Showrunner in its beat-definition mode with the loaded beat, the entry contract, and the theme context → the **Showrunner Notes**: the beat's narrative intent and emotional truth, its single Primary Requirement restated as the non-negotiable that rides the whole ritual, and any narrative contract this beat plants, maintains, or pays off.

**The Cinematographer renders the HOW (headless).** Invoke the Cinematographer in its beat-visual-specs mode with the Showrunner Notes against the Style Guide, Palette, Lens Language, and Vocabulary → the **Cinematographer Specs**: lens and fps, hex-coded lighting with placement, composition and negative space, camera move, atmosphere — every colour a hex code from the Palette, no banned word, the mandatory rim light present. The Cinematographer holds its own visual gate; specs that smuggle a vague colour name or a banned word come back HELD, not flagged.

**The State-Diff Gate — the Script Supervisor proves the STATE (headless, the hard gate).** Invoke the Script Supervisor in its shard-state-validation mode with the entry contract, the character files, the prior exit state, the Showrunner Notes, and the Cinematographer Specs → a Continuity Validation ending in a binding **Status**. This is the load-bearing refusal of the whole loop, and every violation class holds at the same hardness: a narrative-contract breach, a protected-object reveal, a broken inherited handshake, and a position-based lighting discontinuity each force FAILED — none is softened to a note that travels downstream with the prompt. **On FAILED the ritual halts here: no prompt compiles, no exit state is written, no manifest or Slate update happens.** Emit the structured hold, naming every blocking item and the exact change, and route it back to the agent who owns the gap:

> **SHARD ON HOLD — the State-Diff Gate FAILED.** This shard is NOT continuity-safe, and nothing downstream proceeds — no prompt, no exit state, no manifest or Slate write. Blocking: {enumerate every item the Script Supervisor flagged and the exact fix each needs}. The gate is the safety of the production loop; a failed check is a refusal, not a warning. Resolve each blocker with its owning specialist, then re-run the ritual.

Only a **VALIDATED** or **VALIDATED WITH INJECTIONS** Status clears the gate. An injection is the exact state text the Script Supervisor baked into the draft when a known detail was missing — never a flag left for someone else — and each one is recorded in the prompt's Build Notes.

**Compilation — the Prompt Engineer, on a cleared gate only (headless, variable intervals).** With the Status cleared, invoke the Prompt Engineer in its prompt-compilation mode — its variable-interval-compilation mode for a 15s or 30s beat — with all three upstream outputs plus `{project}/Architecture/Vocabulary.md`. It refuses if any of the three inputs is missing or the Status is FAILED; a missing input is a refusal, never a guess. The beat's Duration drives the `[Temporal Constraint]` and the choreography density, scaled per `{workflow.variable_interval_guide}` and never compiled longer than `temporal.max_shard_duration` — more seconds buy more choreography of the same beat, never a second beat. Whatever the duration, the critical anchors stay in the first 25%, every colour is a hex code, no banned word survives, and the shard ends on an exit hook the next shard can handshake against. The compiled prompt matches the shape `{workflow.shard_prompt_template}` lays down.

**State update — the bounded writes** (the Script Supervisor is the one specialist that writes project state). Only on a cleared gate and a compiled prompt, perform these explicit writes (you write them; the validate check only confirms they happened):

1. **Write the prompt** to `{project}/Output/Prompts/Scene_{XX}_Shard_{YY}_prompt.md` from `{workflow.shard_prompt_template}` — `sceneNumber` the two-digit `{XX}`, `shardNumber` the bare `{YY}`, `beatName` the UPPER_SNAKE of the beat title, every one of the four `agentInputs` true, `stateDiffPassed` true (a prompt is never written while the gate reads false), and the six bracketed sections in order with the critical anchors leading `[Subject/Asset]`.
2. **Write the exit state** to `{project}/Production/Scenes/Scene_{XX}/state/shard_{YY}_exit_state.md` from `{workflow.exit_state_template}` — the full state at the shard's end moment, never a position alone. Its `## Entry Contract for Next Shard` (`### MUST Start With:` and `### MUST NOT Show:`) is mandatory and non-empty unless this is the scene's final shard, which owes no next-shard contract.
3. **Update the manifest** at `{project}/.cpm/manifest.md` — set the **Active Scene Context** and refresh the `### Required Files for Current Context` block to the files this shard established. This Active Scene Context is the one block the scene-create workflow must never touch; it is owned here.

   ```markdown
   ### Active Scene Context

   - **Current Scene:** {XX}
   - **Current Shard:** {YY}
   - **Characters On Camera:** {comma-separated on-camera names}
   ```

   On the first shard generated for the production, flip the Project-Status checkbox `- [ ] First shard generated` to `- [x] First shard generated`.
4. **Update the Slate** at `{project}/Production/Slate.md` — bump this scene's row Status (`in-progress` with a shards-done count, or `complete` when `{YY}` equals the brief's `shard_count`) and append a `## Production Log` line:

   ```markdown
   ## Production Log
   - {date} — Scene {XX} Shard {YY} "{beat title}" generated; state-diff PASSED; status: in-progress ({YY}/{shard_count}).
   ```

Capture the run to the scene's memlog as it lands — the gate result and the shard's completion (`--type event`) — then run the reviewer gate below and finalize.

## Regenerate

Read first, every time: `{workflow.shard_ritual_contract}` (the bar the re-run must clear), the existing `{project}/Output/Prompts/Scene_{XX}_Shard_{YY}_prompt.md` and `state/shard_{YY}_exit_state.md` (what stands today), the `scene-brief.md` (the beat as it now reads — an edited beat is the usual reason to regenerate), and the scene's `.memlog.md` if present. Then run the same ritual as Generate for that beat — the same precondition gates, the same hard State-Diff Gate, the same bounded writes.

Regenerating overwrites a beat already produced, and it is never silent. A shard with an existing `shard_{YY}_exit_state.md` already sits in the project's continuity chain, so surface the conflict and require explicit confirmation before the crew is touched:

> **REGENERATION OVERWRITES A GENERATED SHARD.** Scene {XX} Shard {YY} already has a compiled prompt and an exit state, and any later shard handshook against that exit state. Re-running this beat rewrites its prompt and exit state, which **invalidates every later shard in the scene** — their entry contracts were built against the old exit state and must be regenerated in turn. Confirm you want to regenerate Shard {YY} and re-run the shards after it; on confirmation I run the ritual and rewrite the state.

Only after the filmmaker confirms does the ritual run. If the new State-Diff Gate FAILS, the existing shard is left exactly as it stands — a failed regeneration never half-replaces a good shard. On success, the manifest Active Scene Context and the Slate are updated as in Generate, and the finalize report names every downstream shard that now needs regenerating.

## Validate

Read first, every time — you cannot grade what you have not read: `{workflow.shard_ritual_contract}` (the contract), the target prompt `{project}/Output/Prompts/Scene_{XX}_Shard_{YY}_prompt.md` and its sibling `state/shard_{YY}_exit_state.md` (the artifacts), beat `{YY}` from the `scene-brief.md` and the prior shard's exit state (the continuity it inherits), `{project}/Architecture/Vocabulary.md` (the banned words), and the scene's `.memlog.md` if present. Then run the read-only structural check:

```
uv run scripts/validate_shard.py --prompt "{project}/Output/Prompts/Scene_{XX}_Shard_{YY}_prompt.md" --project "{project}"
```

It writes nothing and returns one JSON object on stdout; the exit code is `0 = pass` (warnings allowed), `1 = hold` (structure incomplete), or `2 = usage/precondition error` (the message names the fix — most often the prompt file is absent). `--prompt` is required; `--project` is optional and inferred from the prompt's path when omitted. The check owns the deterministic structure: the prompt frontmatter field set, `stateDiffPassed` true, all four `agentInputs` true, the six bracketed sections in order, the `[Temporal Constraint]` opening on a 5/15/30-second duration, the sibling exit state's existence and identity match, the exit-state sections (and a non-final shard's non-empty entry contract), and — when the brief carries a machine-readable Beat Table — that the shard number is in range, the beat exists, and the prompt's duration equals the beat's Duration. When the brief carries no Beat Table those cross-checks degrade to a single warning, never a hold (`scene_brief_checked` reads false). If `uv run` is unavailable, grade these by hand against the contract.

What the check cannot judge, you do — read the prompt and exit state against the contract and the inherited continuity:

- **Continuity-safe against the entry contract** — the prompt honours every `MUST Start With` of the prior exit state and shows nothing in its `MUST NOT Show`. A contradiction holds at the same hardness as a structural break.
- **The critical anchors genuinely lead the attention window** — the LEFT/RIGHT-specific scar, the permanent crease, the expression, any unblinking mandate sit in the first 25% of `[Subject/Asset]`; an anchor that trails it fails.
- **Zero banned words** — no term from `Vocabulary.md` survived, and every colour is a hex code, never a vague colour name.
- **A real exit hook** — the `[Temporal Constraint]` ends on a freeze the next shard can actually handshake against, and the exit state records that same end position.

Grade every clause at the same hardness. Emit a per-check table — one row per check, PASS or the specific failure — and an overall verdict:

- **PASS** — the check returns `pass` with no warnings and every substance clause holds. Report: **SHARD CLEARED.** The structure round-trips, the anchors lead, no banned word survives, and the exit hook is one the next shard can read.
- **PASS WITH WARNINGS** — structure and substance hold, but the check returned a `warnings` entry (most often a brief with no machine-readable Beat Table, so the cross-checks degraded). Name each warning; it is surfaced, not blocking.
- **HOLD** — any `issues` entry from the check, or any substance clause that fails. This is a structural block, not a warning:

  > **SHARD ON HOLD.** This shard is NOT continuity-safe and must not be handed to the generator or treated as the baseline for the next shard. Failing: {name every entry in `issues`, plus any substance clause you found wanting}. Regenerate the shard before production proceeds.

- **NO SHARD** — the check exits `2` (`status: error`) because no prompt exists at that path. There is nothing to grade: do not emit PASS or HOLD. Report that no shard was generated there and route the user to **generate**.

## Reviewer gate and finalize

After a generate or regenerate, confirm the result independently before declaring the shard ready: run the **Validate** check as a reviewer gate — delegate it to a subagent for fresh eyes when subagents are available, instructing it to run the validate command, judge the continuity / anchor / vocabulary / exit-hook clauses against `{workflow.shard_ritual_contract}`, and return ONLY the verdict (PASS, PASS WITH WARNINGS, or HOLD with the gaps named). Only a PASS — or a PASS WITH WARNINGS whose sole entry is a known degraded-brief warning — clears the shard; a HOLD becomes the blocking slot above and sends you back into regenerate.

Once cleared, distill the memlog so the scene's trail reflects this shard, and record completion beside the brief: `uv run {project-root}/_bmad/scripts/memlog.py append --path {project}/Production/Scenes/Scene_{XX}/.memlog.md --type event --text "scene {XX} shard {YY} generated"` (add the line by hand if `uv run` is unavailable — never block the shard on the logger). Then finalize for the filmmaker in `{communication_language}`: state the prompt and exit-state paths, note that the manifest Active Scene Context and the Slate now record the shard, and point to the next move — the next ungenerated beat, or, when `{YY}` equals the brief's `shard_count`, that the scene is complete and every beat has been produced.

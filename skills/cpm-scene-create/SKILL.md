---
name: cpm-scene-create
description: Creates, updates, and validates a CPM scene brief — the filmmaker-directed beats of a scene. Use when the user says "create a scene", "new scene brief", "break a scene into beats", "update a scene", or "validate a scene brief".
---

# CPM Scene Brief

This workflow produces a scene brief — the filmmaker's beat-by-beat direction for one scene, authored up front, before a single shard is generated. Act as the production coordinator and beat facilitator: the filmmaker directs each beat, and this workflow pins it down on the page so the scene is decided here rather than improvised later at the generator. The outcome is `{project}/Production/Scenes/Scene_{XX}/scene-brief.md`, its `state/entry_contract.md` companion, and the scene's registration in the project manifest and the Slate. Its consumers are the Showrunner, who reads the whole Beat Table to review the scene, and the shard-generation loop, which pulls one beat per shard by its integer number alone — so the Showrunner *loads* a pre-authored beat instead of inventing one on the spot, which is the whole reason this brief exists. That sets the bar: one beat is one shard, the four counts that prove it agree (`shard_count`, Beat Table rows, Beat Detail blocks, and the highest Beat number are all equal, the beats numbered contiguously from 1), and every beat's single Primary Requirement names something concrete a reviewer can check — or the scene is held, never handed to production.

## Resolution rules

- Bare paths and `{skill-root}` (e.g. `references/scene-brief-contract.md`) resolve from this skill's installed directory.
- `{project-root}` → the BMad framework working directory (the repository root), distinct from the CPM production project below.
- `{project}` → the located CPM production project root — the folder holding `.cpm/`, `Bible/`, and `Production/` — distinct from `{project-root}`.
- `{XX}` → the scene number as a zero-padded two-digit string (`01`, `02`); `Scene_{XX}` is the scene's folder under `{project}/Production/Scenes/`.
- `cpm-scene-create` → the skill directory's basename.

## On Activation

1. Load config from `{project-root}/_bmad/config.yaml` (and `config.user.yaml` if present; root and `cpm` section). Apply `{user_name}`, `{communication_language}`, `{document_output_language}` with sensible defaults; never block on missing config.
2. Resolve the `workflow` block: run `uv run {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`. If it fails, merge base → team → user yourself — `{skill-root}/customize.toml`, `{project-root}/_bmad/custom/cpm-scene-create.toml`, `{project-root}/_bmad/custom/cpm-scene-create.user.toml` (scalars override, arrays append). Reference resolved values as `{workflow.<name>}` below; never hardcode a path beside a declared scalar.
3. Bind `{project}` before any `{project}/...` path is read or written — use the production named in the conversation, or glob for a folder containing `.cpm/` under the productions base and confirm the match with the user; never guess when more than one exists. **If no `.cpm/` scaffold is found, degrade — do not error:** point the user to the new-project workflow to scaffold a production first, because a scene cannot be briefed into a project that does not exist.
4. Resume check: a scene's decision trail lives at `{project}/Production/Scenes/Scene_{XX}/.memlog.md`, beside the brief. If one exists for the scene in play, read it once to rebuild what was decided and why, surface where things stand, and continue append-only.
5. Route by intent from what the user said — **create** (author a new scene brief), **update** (revise an existing one), or **validate** (grade an existing one). These are not interchangeable; if which one is unclear, ask the single question that settles it before doing anything.

All replies use `{communication_language}`; generated file content uses `{document_output_language}`.

## Create

Read first, every time: `references/scene-brief-contract.md` (the schema and the non-negotiables you will enforce) and `{workflow.scene_brief_template}` (the shape you will write). Keep `{workflow.scene_structure_reference}` at hand for shaping the spine and `{workflow.beat_specificity_guide}` for the beats — the standard every Primary Requirement must clear.

**The init gate — settle new-vs-update before writing anything.** First, confirm there is a project to brief into: if there is no `{project}/.cpm/manifest.md`, HALT and route to the new-project workflow:

> **SCENE ON HOLD — no project to brief into.** There is no `.cpm/manifest.md` at `{project}`. A scene brief registers into a CPM production — its manifest, its Slate, its character files — and none of that exists yet. Run the new-project workflow to scaffold the production first, then return here.

Then determine the scene number with the filmmaker and look for `{project}/Production/Scenes/Scene_{XX}/scene-brief.md`:

- **Absent → a new scene.** Proceed.
- **Present → the scene already exists, and is never silently overwritten.** Offer the choice and default to the safe path: **[E]** edit the existing brief (→ Update, the default), **[V]** validate or view it (→ Validate), **[N]** a different, unused scene number (→ back to new), or **[O]** overwrite from scratch — destructive, and only after the filmmaker types the scene id (`SCENE_{XX}`) to confirm. If they asked to create but the scene exists, route to Update rather than clobber.

Load context, degrading gracefully if absent: the Show Bible at `{project}/Bible/Show_Bible.md` (theme and arc), and the Style Guide and Palette under `{project}/Architecture/` (so Focus and Primary Requirement are written in the production's hex codes and visual language). Read `{project}/.cpm/config.yaml` for `temporal.default_shard_duration` (the per-beat Duration default) and `temporal.max_shard_duration` (the ceiling). Then init this scene's decision trail: `uv run {project-root}/_bmad/scripts/memlog.py init --path {project}/Production/Scenes/Scene_{XX}/.memlog.md` (if a prior aborted run left one, append to it instead; if `uv run` is unavailable, create the file by hand and append entries directly — never block the scene on the logger).

Now facilitate — the filmmaker is the expert; you draw the scene out and press for specificity, you never invent it. Capture decisions to the memlog as they land (`--type decision --text "..."`). Work the sections in order:

- **`## Setting`** — Location, Time of Day, Atmosphere.
- **`## On-Camera Characters`** — the plain names on camera (recommended once two or more share the frame). **Verify each resolves to `{project}/Bible/Characters/{Name}.md`**; if any is missing, HALT and offer the character workflow, held at the same hardness as any other block:

  > **SCENE ON HOLD — a character on camera has no state file.** {name the missing character(s)} on camera in this scene have no `Bible/Characters/{Name}.md`. The Beat Table's Focus and Primary Requirement reference a character by name and rely on that file for the immutable identity the generator must hold every shard; without it the scene cannot be briefed honestly. Run the character workflow to create {the character(s)}, then we continue.

- **`## Narrative Purpose`** — what the scene accomplishes for the story, plus a **Serves theme:** line naming at least one theme checked against the Show Bible.
- **`## Emotional Arc`** — **Opens at:** and **Closes at:**; the two states must differ, because the scene exists to move something.
- **`## Beats`** — the creative core, authored one beat at a time until the filmmaker says the scene is complete. For each beat build **both** layers together: a row in the **`### Beat Table`** (columns are exactly `Beat | Duration | Focus | Primary Requirement`, in that order, nothing more) and a matching `#### Beat {N} — {Title}` block under **`### Beat Details`** (fields **Action:** and **Emotional Note:** required, **Shot:** recommended, **Continuity In:** required on Beat 1 as the carry-in and optional after, **State Change:** optional). Keep the two layers 1:1 by integer — the table owns Duration and Primary Requirement, the details own the prose, neither restates the other's fields. Set each beat's **Duration** from `temporal.default_shard_duration` unless the filmmaker overrides it, always one of 5s, 15s, or 30s and never above `temporal.max_shard_duration`. Reference each character by name; never restate the immutable identity that lives in their character file. Every **Primary Requirement** is the single non-negotiable that beat must deliver and must name at least one concrete checkable element — a hex code, a lens, a LEFT/RIGHT designation, a named prop, or a condition flag. Hold a vague requirement at the same hardness as a missing character file — never "flag it and proceed":

  > **BEAT ON HOLD — the Primary Requirement is not checkable.** Beat {N}'s requirement ({quote it}) names a feeling, not a fact. A beat the Script Supervisor cannot grade with a clean yes/no is not production-ready — name at least one concrete element (a hex code, a lens, a LEFT/RIGHT side, a named prop, or a condition flag), then we lock the beat.

- **polish** — review every beat for specificity, for an arc the State Changes actually earn, for a contiguous one-beat-one-shard mapping (`Beat` runs `1..shard_count`, one row each), and for honest durations. `## Continuity Carry-Out` is an optional scene-level note of what the next scene should assume.

**finalize** — when every beat is locked, perform these bounded, explicit writes (you write them; the validate script only checks they happened):

1. **Scaffold** `{project}/Production/Scenes/Scene_{XX}/state/`.
2. **Write the brief** to `{project}/Production/Scenes/Scene_{XX}/scene-brief.md` from `{workflow.scene_brief_template}` — `status: ready`, `scene_id` equal to `"SCENE_" + scene_number`, `on_camera_characters` as plain names, `shard_count` equal to the beat count, `created` and `lastModified` stamped. The brief carries only the contract's frontmatter; resume bookkeeping lives in the memlog, never in the shipped artifact.
3. **Seed the entry contract** at `state/entry_contract.md` from `{workflow.entry_contract_template}`. For Scene 01, derive the carry-in from the on-camera characters' initial state in their character files, capturing each asset ID (e.g. `ELIAS_V1`) here — not in the brief frontmatter. For a later scene, seed it from the prior scene's last `shard_{last}_exit_state.md` when that file exists; when it does not, write an explicit gap stub — keep the section shapes, mark the unknowns `> unresolved — Script Supervisor fills before Shard 1`, and point `derived_from` at the expected prior exit-state path. A stub is a marked handoff, never a silent hollow one; Validate surfaces it as a warning, not a hold.
4. **Register the scene in the manifest** at `{project}/.cpm/manifest.md` — a bounded write of two regions only; **never touch Active Scene Context** (`Current Scene` / `Current Shard` / `Characters On Camera`). Below the `<!-- scene-create updates this section automatically -->` marker in `### Scenes`, append this scene's block, or replace it if one already stands:

   ```markdown
   ## Scene {XX}
   - **Title:** {scene_title}
   - **Status:** ready
   - **On-Camera Characters:** {comma-separated plain names}
   - **Shard Count:** {shard_count}
   - **Brief:** `Production/Scenes/Scene_{XX}/scene-brief.md`
   ```

   Then flip the Project-Status checkbox `- [ ] Scenes defined …` to `- [x] Scenes defined …` now that a scene exists.
5. **Update the Slate** at `{project}/Production/Slate.md` — add (or update) this scene's row in the `## Scenes` status table and append a `## Production Log` line:

   ```markdown
   ## Scenes
   | Scene | Title | Status | Shards | Brief |
   |-------|-------|--------|--------|-------|
   | {XX} | {scene_title} | ready | {shard_count} | Production/Scenes/Scene_{XX}/scene-brief.md |

   ## Production Log
   - {date} — Scene {XX} "{scene_title}" brief created ({shard_count} beats); status: ready.
   ```

Then run the reviewer gate below and finalize.

## Update

Read first, every time: `references/scene-brief-contract.md` (the bar), the existing `{project}/Production/Scenes/Scene_{XX}/scene-brief.md` (what stands today), and `{project}/Production/Scenes/Scene_{XX}/.memlog.md` if present (why it stands that way; a brief authored outside this workflow may have none — then work from the file itself). Keep `{workflow.beat_specificity_guide}` at hand.

Present an edit menu — **setting / on-camera characters / narrative purpose / emotional arc / edit a beat / add a beat / remove a beat / reorder beats / change durations / carry-out** — and apply only what is asked, holding every untouched section as it stands. The two layers and the registrations must never drift:

- **Any change to the beat count** (add or remove) recomputes `shard_count`, re-numbers the beats so the `Beat` column stays contiguous `1..shard_count`, and re-syncs the Beat Table and Beat Details 1:1 — a renumbered beat is renumbered in both layers.
- **Editing or reordering beats** re-syncs the Beat Table against the Beat Details by integer; the table keeps Duration and Primary Requirement, the details keep the prose, neither restates the other.
- **Adding an on-camera character** runs the same existence check as Create — a name with no `Bible/Characters/{Name}.md` HALTS on that same blocking slot, never a softer note.

Before applying a removal or a reorder, check whether shards have already been generated (the Slate `status` and Production Log will say). If they have, surface the conflict first and get the filmmaker's confirmation before touching the brief:

> **SCENE CHANGE CONFLICTS WITH GENERATED SHARDS.** {which beats change, and which shards were generated against them}. Renumbering or removing them rewrites a beat the production loop already produced against. Confirm those downstream shards may be invalidated; on confirmation I apply the change and re-sync the Beat Table, Beat Details, manifest, and Slate.

On finalize, bump `lastModified`, re-run the bounded manifest write and the Slate update so both match the edited brief, then run the reviewer gate. Record each change to the memlog (`--type decision`); an override of a past call records the rejected reasoning too. If `uv run` is unavailable, edit by hand against the contract and append the memlog line by hand.

## Validate

Read first, every time — you cannot grade what you have not read: `references/scene-brief-contract.md` (the contract), the target `{project}/Production/Scenes/Scene_{XX}/scene-brief.md` (the artifact), `{workflow.beat_specificity_guide}` (the standard the Primary Requirements must clear), and `{project}/Production/Scenes/Scene_{XX}/.memlog.md` if present (to grade against the standards the filmmaker set, not only a generic rubric). Then run the read-only structural check:

```
uv run scripts/validate_scene_brief.py --brief "{project}/Production/Scenes/Scene_{XX}/scene-brief.md" --project "{project}"
```

It writes nothing and returns one JSON object on stdout; the exit code is `0 = pass` (warnings allowed), `1 = hold` (structure incomplete), or `2 = usage/precondition error` (the message names the fix). The script owns the deterministic structure: frontmatter identity (`scene_id == "SCENE_" + scene_number`, two-digit `scene_number`), the four-way equality, the contiguous `Beat` column, the exact four columns, the table-to-detail 1:1 mapping, character-file resolution, the side artifacts (entry contract, manifest Scenes entry, Slate row), and the cheap halves of beat quality (Duration ∈ {5, 15, 30}, Focus non-empty, an **Action:** field present). If `uv run` is unavailable, grade these by hand against the contract.

What the script cannot judge, you do — read every beat against the beat-specificity guide and the brief against the contract:

- **Each Primary Requirement names a genuinely concrete, checkable element** — a hex code, a lens, a LEFT/RIGHT side, a named prop, or a condition flag. A requirement the script counts as present but that names only a feeling ("cold and controlled") fails this at the same hardness as any structural break — there is no "flag it and pass."
- **`## Narrative Purpose` names at least one real theme** (checked against the Show Bible) and **`## Emotional Arc` opens and closes at states that differ** — the scene earns its change.

Grade every clause at the same hardness: a vague Primary Requirement holds exactly as hard as a missing character file. Emit a per-check table — one row per check, PASS or the specific failure — and an overall verdict:

- **PASS** — every structural check passes and every Primary Requirement is concrete. Report: **SCENE READY.** The four-way equality holds, every beat is checkable, and the scene is registered; the Showrunner can load its beats and shard-generation can extract each one by number.
- **PASS WITH WARNINGS** — structure and specificity hold, but the check returned a `warnings` entry (most often an `entry_contract.md` written as an explicit gap stub for a later scene whose prior exit state does not exist yet). Name each warning; it is surfaced, not blocking — the handoff is marked, and the Script Supervisor fills it before Shard 1.
- **HOLD** — any structural `issues` entry, or any Primary Requirement that is not concrete. This is a structural block, not a warning:

> **SCENE ON HOLD.** This brief is NOT production-ready and must not be handed to the Showrunner or shard-generation. Failing: {name every entry the check lists in `issues`, plus any vague Primary Requirement you found}. The production loop pulls beats by integer and the Script Supervisor checks each requirement frame by frame — a broken count or an uncheckable beat drifts the production. Resolve these in create or update before any shard generation.

- **NO BRIEF** — the check exits `2` (`status: error`) because no file exists at that path. There is nothing to grade: do not emit PASS or HOLD. Report that no scene brief exists there and route the user to **create** to author one.

## Reviewer gate and finalize

After a create or update, confirm the result independently before declaring the scene ready: run the **Validate** check as a reviewer gate — delegate it to a subagent for fresh eyes when subagents are available, instructing it to run the validate command, judge the specificity and theme checks against `references/scene-brief-contract.md` and `{workflow.beat_specificity_guide}`, and return ONLY the verdict (PASS, PASS WITH WARNINGS, or HOLD with the gaps named). Only a PASS — or a PASS WITH WARNINGS whose sole entry is a known entry-contract gap — clears the scene; a HOLD becomes the blocking slot above and sends you back into create or update.

Once cleared, distill the memlog — confirm every meaningful decision is reflected in the brief or consciously set aside as process noise — and record completion beside the brief: `uv run {project-root}/_bmad/scripts/memlog.py append --path {project}/Production/Scenes/Scene_{XX}/.memlog.md --type event --text "scene {XX} brief complete"` (a memlog carries no 'complete' flag; completion is simply its final entry; add the line by hand if `uv run` is unavailable — never block the scene on the logger). Then finalize for the filmmaker in `{communication_language}`: state the brief's path and its `state/entry_contract.md`, note that the manifest Scenes registry and the Slate now carry the scene, and point to the next move — another scene, or shard-generation to start producing this one beat by beat.

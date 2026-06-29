---
name: cpm-character-create
description: Creates, updates, and validates a CPM character state file. Use when the user says "create a character", "new character", "update character state", or "validate a character file".
---

# CPM Character State File

This workflow produces a character state file — the immutable visual identity an AI video model needs to render the same person in every shard. Act as the casting and continuity coordinator: the filmmaker holds the character; this workflow draws them out with the lateral specificity continuity demands, writes the file, and rosters it. The outcome is `{project}/Bible/Characters/{Name}.md` plus a row in the roster at `{project}/Bible/Characters/_index.md`. Its consumers are the Script Supervisor and the Prompt Engineer, who reload the immutable features every shard — a character whose asymmetric features are not pinned to a side breaks continuity downstream, because the model mirrors or drifts any side left unstated. The bar: every immutable feature anchored to LEFT or RIGHT with both sides accounted for; a character missing that specificity is held, never handed off.

## Resolution rules

- Bare paths and `{skill-root}` (e.g. `references/character-contract.md`) resolve from this skill's installed directory.
- `{project-root}` → the BMad framework working directory (the repository root), distinct from the CPM production project below.
- `{project}` → the CPM production project folder (where `Bible/`, `Architecture/`, `Production/` live).
- `cpm-character-create` → the skill directory's basename.

## On Activation

1. Load config from `{project-root}/_bmad/config.yaml` (and `config.user.yaml` if present; root and `cpm` section). Apply `{user_name}`, `{communication_language}`, `{document_output_language}` with sensible defaults; never block on missing config.
2. Resolve the `workflow` block: run `uv run {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`. If it fails, merge base → team → user yourself — `{skill-root}/customize.toml`, `{project-root}/_bmad/custom/cpm-character-create.toml`, `{project-root}/_bmad/custom/cpm-character-create.user.toml` (scalars override, arrays append). Reference resolved values as `{workflow.<name>}` below; never hardcode a path beside a declared scalar.
3. Bind `{project}` to a specific production before any `{project}/...` path is read or written — use the one named in the conversation, or glob for a folder containing `.cpm/` under the productions base (where the new-project workflow places productions) and confirm the match with the user; never guess when more than one exists. The production project is the folder holding `.cpm/` and `Bible/Characters/`. If `.cpm/` is absent the project is not scaffolded: point the user to the new-project workflow, or, if they want to proceed, write under the `Bible/Characters/` path they name. Never error on a missing scaffold.
4. Route by intent from what the user said — **create** (a brand-new character: a fresh, full visual-identity interview), **update** (a change to an existing character: mutable state, append a version-history row), or **validate** (grade an existing character file). These are not interchangeable; if which one is unclear, ask the single question that settles it before doing anything.

State survives across turns in a per-character decision trail beside each file — `{project}/Bible/Characters/.{Name}.memlog.md` — and in the character files themselves; scoping the log to one character keeps its init, distill, and completion operating on exactly the unit a run produces. Update and Validate recover context by reading them. All replies use `{communication_language}`.

## Create

Read first, every time: `references/character-contract.md` (the field and laterality contract) and `{workflow.character_template}` (the shape you will write).

Confirm this is a brand-new character, not a change to one already rostered — if the name already appears in `_index.md`, this is an Update; switch. Then init this character's decision trail: `uv run {project-root}/_bmad/scripts/memlog.py init --path {project}/Bible/Characters/.{Name}.memlog.md` (if a prior aborted run already left one, append to it instead of re-initializing; if `uv run` is unavailable, create that file by hand and append entries directly — never block the character on the logger).

Interview the filmmaker (they are the expert; you confirm, never invent), capturing every section of the contract: the immutable Visual Identity (Face, Body, Movement), the mutable Current Outfit, Inventory, and Physical State, the Behavioral Profile, and the Arc Position. Capture casting and continuity calls as they land — especially which features are immutable and why — one entry at a time: `uv run {project-root}/_bmad/scripts/memlog.py append --path {project}/Bible/Characters/.{Name}.memlog.md --type decision --text "..."` (if `uv run` is unavailable, add the line by hand).

The non-negotiable, enforced as you gather: every asymmetric immutable feature is pinned to LEFT or RIGHT, and BOTH sides are accounted for, held at equal hardness. If the filmmaker gives only one side, surface the gap and resolve it before writing:

> **CHARACTER ON HOLD — lateral specificity incomplete.** {the feature(s) missing a side}. An AI video model mirrors or drifts any side left unstated, so a one-sided character is not continuity-ready. Pin both sides, then we write.

When every section is captured and both sides are anchored, write `{project}/Bible/Characters/{Name}.md` from the template, then roster the character: if `_index.md` is absent, create it from `{workflow.index_template}`; append the row `| **{Name}** | {one-line visual signature} | {AssetID} | {Status} |`. Then run the reviewer gate below and finalize.

## Update

Read first, every time: `references/character-contract.md`, the existing `{project}/Bible/Characters/{Name}.md`, and `{project}/Bible/Characters/.{Name}.memlog.md` if present (read once to rebuild what was decided and why; a character authored outside this workflow may have none — then work from the file itself).

Update touches mutable state only — Current Outfit, Inventory, Physical State, and Arc Position — and appends a row to the Version History table for the change (next version label, the scene, what changed). Log each change to the memlog; an override of a past call also records the rejected reasoning.

Never silently overwrite an immutable feature. The Visual Identity section is "Immutable Unless Story Changes": if a request would alter a LEFT or RIGHT immutable feature — either side, same hardness — surface the conflict and get explicit confirmation that a story event justifies it before changing anything:

> **IMMUTABLE FEATURE CONFLICT.** {the immutable feature and its side}. Changing it rewrites the continuity anchor the Script Supervisor and Prompt Engineer rely on. Confirm a story event justifies this; on confirmation I change it, bump the Asset ID version, and log the override.

If the visual signature, Asset ID, or status changed, update the character's row in `_index.md`. If `uv run` is unavailable to append to the memlog, record the change in that file by hand. Then run the reviewer gate and finalize.

## Validate

Read first, every time — you cannot grade what you have not read: `references/character-contract.md` (the contract), the target `{project}/Bible/Characters/{Name}.md` (the artifact), `{project}/Bible/Characters/_index.md` (the roster), and `{project}/Bible/Characters/.{Name}.memlog.md` if present (to grade against the standards the filmmaker set, not only a generic rubric; a character authored outside this workflow has no memlog — grade it against the contract alone). Then run the read-only check:

```
uv run scripts/check_character.py --character "{project}/Bible/Characters/{Name}.md" --index "{project}/Bible/Characters/_index.md"
```

If `uv run` is unavailable, grade by hand against `references/character-contract.md`. Grade every clause at the same hardness: a missing required field, only one of LEFT/RIGHT specified in the immutable section, and a missing roster row are all blocking — none is a mere warning. The check writes nothing.

- **`status: pass`** — report: **CHARACTER CONTINUITY-READY.** Both immutable sides are anchored and the roster is in sync; safe to hand to the Script Supervisor and Prompt Engineer.
- **`status: hold`** — report the blocking slot, naming every entry the check lists in `issues` (a missing header, missing required fields, an unanchored LEFT or RIGHT, unfilled template placeholders, and a missing roster row are all blocking — none is a warning):

> **CHARACTER ON HOLD.** This file is NOT continuity-ready and must not be handed to the Script Supervisor or Prompt Engineer. Failing: {the check's `issues`}. The model will drift or mirror unanchored features. Run Update or Create to resolve before any shard generation.

## Reviewer gate and finalize

After a create or update, confirm the result independently before declaring the character ready: run the **Validate** check as a reviewer gate — delegate it to a subagent for fresh eyes when available, instructing it to run the check command and return ONLY the validate JSON. Only a `pass` clears the character; a `hold` becomes the blocking slot above, and you resolve it before any handoff.

Once cleared, finalize for the filmmaker in `{communication_language}`: distill this character's memlog so every meaningful entry is either reflected in `{Name}.md` or set aside as process noise, then record completion as the log's last entry — `uv run {project-root}/_bmad/scripts/memlog.py append --path {project}/Bible/Characters/.{Name}.memlog.md --type event --text "character {Name} complete"` (a memlog carries no 'complete' flag; completion is simply its final entry). If `uv run` is unavailable, add that entry by hand — never block the character on the logger. State the character's path and roster status, and point to the next move — another character, or the Scene workflow to place this one in a beat.

---
name: cpm-inception
description: Rapid-start onboarding for a new CPM production — one conversational vision interview that scaffolds the project and drafts the Show Bible, Style Guide, and character sketches in a single pass. Use when the user says "start a new film", "rapid start a production", "onboard a CPM project", "take my idea to a project foundation", "set everything up from my vision", or "inception".
---

# CPM Inception

This workflow is the rapid-start path: one conversational vision interview takes a filmmaker from nothing to a scaffolded project and a refine-in-place DRAFT foundation in a single pass. Act as the onboarding coordinator — the filmmaker holds the vision, this workflow draws it out, presses on the gaps, and lays down the foundation so production can begin. The outcome is a scaffolded project (the directory tree, `.cpm/config.yaml`, the manifest, the Slate, and the static methodology diagram) plus a DRAFT narrative foundation: a draft Show Bible, a draft Style Guide (all four `Architecture/` files), and a draft character sketch for each key character. Its consumers are the dedicated refine workflows — cpm-show-bible, cpm-style-guide, cpm-character-create — which deepen each draft in place, and cpm-scene-create, which starts authoring scenes against it. That sets the bar: every draft is structurally valid against its foundation contract (a draft Bible carries the Bible's required sections, a draft character pins LEFT/RIGHT, the draft palette is exact hex) so the dedicated workflow can refine rather than rebuild, and every draft is honestly marked as a draft. A draft is shallow on purpose, never broken — the laterality, exact-hex, and banned-word non-negotiables hold at full hardness even here.

## Resolution rules

- Bare paths and `{skill-root}` (e.g. `references/vision-interview.md`) resolve from this skill's installed directory.
- `{project-root}` → the BMad framework working directory (the repository root), distinct from the CPM production project below.
- `{project}` → the located or named CPM production project root — the folder holding `.cpm/`, `Bible/`, and `Architecture/` — distinct from `{project-root}`.
- `{Name}` → a character's display name; `{XX}` → a zero-padded two-digit number where one is needed.
- `{new-project-skill}` → the sibling cpm-new-project skill: resolve `{workflow.new_project_skill}` from `{skill-root}` (it names the sibling skill directory under the same skills root). If that directory is absent, glob the skills root — the parent of `{skill-root}` — for a `cpm-new-project/` folder and use it. This is the single source of the project structure; inception never reimplements it.
- `{show-bible-skill}`, `{style-guide-skill}`, `{character-skill}` → the sibling foundation skills, resolved the same way from `{workflow.show_bible_skill}`, `{workflow.style_guide_skill}`, `{workflow.character_skill}`, with the same glob-the-skills-root fallback. They are read only for their deterministic check scripts in Validate.
- `cpm-inception` → the skill directory's basename.

## On Activation

1. Load config from `{project-root}/_bmad/config.yaml` (and `config.user.yaml` if present; root and `cpm` section). Apply `{user_name}`, `{communication_language}`, `{document_output_language}` with sensible defaults; never block on missing config.
2. Resolve the `workflow` block: run `uv run {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`. If it fails, merge base → team → user yourself — `{skill-root}/customize.toml`, `{project-root}/_bmad/custom/cpm-inception.toml`, `{project-root}/_bmad/custom/cpm-inception.user.toml` (scalars override, arrays append). Reference resolved values as `{workflow.<name>}` below; never hardcode a path beside a declared scalar.
3. Bind `{project}` before any `{project}/...` path is read or written — use the production named in the conversation, or glob for a folder containing `.cpm/` under the productions base and confirm the match; never guess when more than one exists. For a brand-new run there is no project yet: treat `{workflow.default_project_path}` joined with the production name as the destination, and confirm it with the filmmaker before scaffolding.
4. Resume check: an inception decision trail lives at `{project}/.cpm/.inception.memlog.md`, beside the config. If one exists, read it once to rebuild the interview decisions and which phases completed, surface where things stand, and continue append-only. Before any scaffold exists there is no project-scoped trail yet — re-entry simply re-detects on-disk state through the situation map in Create.
5. Route by intent from what the user said — **create** (the full onboarding interview into a draft foundation), **update** (extend the draft or run a missed phase), or **validate** (grade foundation readiness). These are not interchangeable; if which one is unclear, ask the single question that settles it before doing anything.

All replies use `{communication_language}`; generated file content uses `{document_output_language}`.

## Create

Read first, every time — you cannot draft toward a floor you have not read: `references/inception-draft-contract.md` (the draft floor each foundation artifact must clear to be refine-in-place) and `references/vision-interview.md` (the question bank and the gates the interview holds at full hardness).

**Read the situation before writing anything.** Detect what already exists at `{project}` and route by it — the never-clobber rule means create only ever writes a missing artifact, and skips any phase whose artifact already stands:

- **no-project** — no `.cpm/` at the destination: the full run, scaffold plus all four draft phases.
- **partial-foundation** — `.cpm/` exists but some drafts are missing (e.g. a project scaffolded by cpm-new-project, or a half-finished inception): never re-create the scaffold over an existing `.cpm/`, skip every artifact already present, generate only the missing phases. If the `.cpm/` scaffold itself is incomplete (config, manifest, or Slate missing), repair it through the scaffolder's update mode — which fills only the missing files and never overwrites — never its create mode.
- **full-foundation** — `.cpm/` plus the Show Bible, the four Style files, and at least one character all present: there is nothing to create. Report that all foundations are present, never clobber, and route to Validate and to the dedicated refine workflows and cpm-scene-create.

**The vision interview.** Run it per `references/vision-interview.md`: one flowing, open conversation, not a form. Open the floor with the broad question, then mine the natural answer for the structured data each movement must extract, reflect back what you pulled, and press only on the gaps — the filmmaker talks, you structure. Work the six movements (the Pitch, the Meaning, the Shape, the Look, the Cast, the Setup), each grouped by the foundation it feeds so one pass gathers enough to draft all four. Hold the gates the interview names at full hardness as you gather: press every vague color to an exact hex and every "cinematic / dark / warm" to a concrete substitution, and pin every asymmetric character mark to LEFT or RIGHT with both sides accounted for — never soften one to a note. Capture each decision to the inception memlog as it lands.

**The graceful-resume draft pass.** Once the Setup answers are confirmed, lay down the foundation in four phases, skipping any phase whose artifact already exists and saying so. Initialize the memlog the moment the scaffold exists: `uv run {project-root}/_bmad/scripts/memlog.py init --path {project}/.cpm/.inception.memlog.md` (init refuses if the file already exists, so a resume never clobbers the trail; if `uv run` is unavailable, create the file by hand ONLY if it is absent — on a resume where it already exists, append to it, never recreate it — and append entries directly, never block on the logger), then append one typed entry per decision as the drafts firm up.

1. **Scaffold the project skeleton.** Branch on whether a `.cpm/` directory already stands at `{project}` — never run the scaffolder's create mode against a directory that already holds a `.cpm/`, because create writes config / manifest / Slate unconditionally and would clobber a hand-edited manifest or Slate:

   - **No `.cpm/` directory** — build it fresh with the scaffolder's **create** mode (the one deliberate cross-skill call, so the project structure has a single source).
   - **`.cpm/` present and complete** — `config.yaml`, `manifest.md`, and `Production/Slate.md` all there: report "project already scaffolded — skipping" and move to the draft phases.
   - **`.cpm/` present but the scaffold is incomplete** — any of config, manifest, or Slate missing: run the **same command with `--mode update`** to repair it. Update fills only the missing scaffold files and never overwrites an existing one, so it is safe against the partial scaffold a create would clobber.

   ```
   uv run {new-project-skill}/scripts/scaffold_project.py --mode create \
     --project-path "{location}" \
     --project-name "{name}" --model-target "{model}" --shard-duration {seconds} \
     --config-template "{new-project-skill}/assets/config-template.yaml" \
     --manifest-template "{new-project-skill}/assets/manifest-template.md" \
     --slate-template "{new-project-skill}/assets/slate-template.md" \
     --methodology-src "{new-project-skill}/assets/cpm-methodology.excalidraw"
   ```

   This writes the tree, renders config / manifest / slate with the Setup answers (the config carrying the correct nested keys — `temporal.default_shard_duration`, `temporal.max_shard_duration`, `model.target`, the `validation.*` flags), and places the methodology diagram in `Diagrams/`. Create is all-or-nothing. **On `status: created` or `status: updated`** — proceed to the draft phases. **On `status: failed` or `status: error`** — STOP on the blocking slot, present no foundation:

   > **FOUNDATION NOT CREATED.** {the error, which names the fix}. Nothing was written, and no partial project remains. Resolve the cause and re-run. Do not present a foundation or hand off to any production workflow.

   If `uv run` is unavailable, build the tree by hand from `{new-project-skill}/references/project-structure.md` and its config / manifest / slate templates, then copy `{new-project-skill}/assets/cpm-methodology.excalidraw` into `{project}/Diagrams/cpm-methodology.excalidraw` — writing only the files that are absent and never overwriting an existing config, manifest, or Slate, and reading the sibling's structure contract cross-skill so there is no second, drift-prone structure source inside inception.

2. **Draft the Show Bible.** Skip if `{project}/Bible/Show_Bible.md` already exists — report it and route deeper edits to cpm-show-bible. Otherwise write `{project}/Bible/Show_Bible.md` from `{workflow.bible_draft_template}`, filling all six required H2 sections (Logline, Genre & Tone, Thematic Pillars, World Rules, Story Arc, Recurring Motifs) from the Pitch / Meaning / Shape movements to the draft floor in the contract — frontmatter `status: draft` and the "refine with cpm-show-bible" pointer intact. The floor is real, not hollow: a Logline with protagonist, conflict, and stakes; two or more testable pillars; at least one enforceable world rule with a consequence; the act spine with the protagonist's want → need → change legible; at least one motif with where it recurs and what it means. Honestly shallow areas (secondary arcs, the full world-rule set, the traced tonal arc) are left for cpm-show-bible.

3. **Draft the Style Guide.** Skip the whole style phase if ANY of the four `Architecture/` files already exists — never half-overwrite a partial guide; route to cpm-style-guide. Otherwise read `{project}/.cpm/config.yaml`: `validation.require_style_compliance` and `validation.banned_words_enforcement` (both default true) hard-gate the Palette and Vocabulary at shard generation regardless of draft status, so this phase is structurally complete even when thematically thin. Write all four files — `Style_Guide.md` from `{workflow.style_guide_draft_template}` (all five sections, frontmatter `status: draft`), `Palette.md` from `{workflow.palette_draft_template}`, `Lens_Language.md` from `{workflow.lens_language_draft_template}`, `Vocabulary.md` from `{workflow.vocabulary_draft_template}` — from the Look movement. Every allowed color is an EXACT hex (a vague color name is a HOLD even in a draft, held exactly as hard as in cpm-style-guide), and the banned list is non-empty — an empty banned list is a HOLD even in a draft, held exactly as hard as the exact-hex gate — seeded with the universal AI-video offenders the draft template pre-loads, plus any story-specific bans pulled from the interview.

4. **Draft the character sketch(es).** Skip the auto-sketch if any non-index `{Name}.md` already exists under `{project}/Bible/Characters/` — offer to add another through the character phase rather than duplicating or overwriting. Otherwise, for each key character from the Cast movement (the protagonist is mandatory; one or two others if named), write `{project}/Bible/Characters/{Name}.md` from `{workflow.character_draft_template}` with `**Status:** DRAFT` and Asset ID `{NAME}_V1`, and append a roster row to `{project}/Bible/Characters/_index.md` (create it from `{workflow.character_index_template}` first if absent) — but only if no row for `{Name}` already stands in it, so a resume that finds the index already present never duplicates a roster entry. The laterality anchor is non-negotiable even in a draft: every asymmetric immutable feature is pinned LEFT or RIGHT with both sides accounted for in uppercase tokens, or the character is held on the same blocking slot cpm-character-create uses — never softened to a flag:

   > **CHARACTER SKETCH ON HOLD — lateral specificity incomplete.** {the feature(s) missing a side}. An AI video model mirrors or drifts any side left unstated, so a one-sided sketch is not continuity-ready even as a draft. Pin both sides, then we write.

When the present phases are written, run the reviewer gate below and finalize.

## Update

Read first, every time: `references/inception-draft-contract.md` (the floor a change must still clear), the existing foundation artifacts under `{project}`, and `{project}/.cpm/.inception.memlog.md` if present (why the drafts stand as they do).

Update continues the rapid start, and never clobbers creative content. Two moves:

- **Extend the existing draft from more conversation** — deepen a thin section the filmmaker wants firmer now, within the draft frame. Apply only what is asked, hold every untouched section as it stands, and keep the marker honest: update does not promote a draft to final — that is the dedicated workflow's job, the single owner of `final`. Even when a section is deepened in conversation, the `status: draft` / `**Status:** DRAFT` marker stays until the artifact passes its full foundation contract in its dedicated workflow.
- **Run a phase that was skipped or missed earlier** — add a second character sketch, fill a deferred world rule, draft a Style Guide onto a project that only has a Bible. This is the same graceful-resume detection as Create: write only what is missing, skip what is present, hold the same non-negotiables (laterality, exact hex, banned list) at the same hardness. The roster `_index.md` is only ever APPENDED to — never regenerated from the template when it already exists — so an added character's row joins the protagonist's rather than replacing it, and an existing row is never duplicated.

For deep, full-depth work on any single artifact — the kind that should pass the artifact's full contract — hand off to that artifact's dedicated workflow rather than re-doing it shallowly here: cpm-show-bible, cpm-style-guide, or cpm-character-create. Record each change to the memlog (an override of a past call records the rejected reasoning too), then run the reviewer gate and finalize. If `uv run` is unavailable, edit by hand against the contract and append the memlog line by hand.

## Validate

Read first, every time — you cannot grade what you have not read: `references/inception-draft-contract.md` (the draft floor and the foundation contracts it cites), the four foundation artifacts under `{project}`, and `{project}/.cpm/.inception.memlog.md` if present (to grade against the standards the filmmaker set, not only a generic rubric). Validate grades foundation READINESS only — each draft present, structurally valid against its foundation contract, and honestly marked — and deepens nothing. It grades the rapid-start *draft* foundation: an artifact a dedicated refine workflow has already promoted to final carries `status: final` rather than a draft marker, so `validate_inception` holds it — that is expected, not a defect, because a finalized artifact is past inception's readiness gate. Grade such an artifact with its own workflow's check (cpm-show-bible / cpm-style-guide / cpm-character-create), not here; do not route the filmmaker back into create or update to "re-draft" something a dedicated workflow has already finished.

First the deterministic, inception-specific check (always available, no sibling skills required):

```
uv run scripts/validate_inception.py --project "{project}"
```

It writes nothing and returns one JSON object on stdout; the exit code is `0 = pass`, `1 = hold` (a foundation missing or unmarked), or `2 = error` (no project at that path). It checks PRESENCE, the honest DRAFT MARKER on the Show Bible, the Style Guide master, and each character sketch (the Palette / Lens / Vocabulary extracts are presence-only by design — they carry no status field), and that the scaffold is in place — it never re-judges section depth, hex correctness, or laterality.

Then prove refine-readiness so the dedicated workflows can refine each draft in place — run the sibling foundation checks (preferred, cross-skill):

```
uv run {show-bible-skill}/scripts/check_bible.py --bible "{project}/Bible/Show_Bible.md"
uv run {style-guide-skill}/scripts/check_style.py --project-path "{project}"
uv run {character-skill}/scripts/check_character.py --character "{project}/Bible/Characters/{Name}.md" --index "{project}/Bible/Characters/_index.md"
```

If a sibling check script is unavailable, grade that artifact BY HAND against `references/inception-draft-contract.md` — which is exactly why inception carries its own draft contract: it stays self-contained, not coupled to the sibling scripts.

Grade every clause at one hardness (a missing world rule holds exactly as hard as an unanchored character side), and beyond the scripts judge what they cannot see: each draft is a genuine usable starting point rather than hollow, the honest-draft framing is accurate, the laterality / exact-hex / banned-list non-negotiables truly hold, and the draft coheres (the palette and lighting serve the Bible's themes; the roster matches the Bible). Emit a per-artifact PASS/HOLD table — one row per foundation — and an overall verdict:

- **FOUNDATION READY** — every draft present, structurally valid against its foundation contract, and honestly marked. Report: **FOUNDATION READY.** The scaffold is intact and every draft is a refine-in-place starting point; hand off to cpm-show-bible / cpm-style-guide / cpm-character-create to deepen, and to cpm-scene-create to start authoring scenes.
- **FOUNDATION ON HOLD** — any foundation missing, structurally invalid against its contract, or dishonestly marked. This is a structural block, not a warning:

  > **FOUNDATION ON HOLD.** This foundation is NOT ready to hand off. Failing: {name every gap — each missing or invalid foundation from the checks, plus any non-negotiable you found unmet}. A draft that cannot pass its foundation contract cannot be refined in place, and an unmarked draft lies about its depth. Resolve these in create or update before handing off to the refine workflows or to scene authoring.
- **NO PROJECT** — `validate_inception.py` exits `2` because there is no project at that path. There is nothing to grade: do not emit READY or ON HOLD. Report that no project exists there and route the user to **create** to onboard one.

## Reviewer gate and finalize

After a create or update, confirm the result independently before declaring the foundation ready: run the **Validate** layers as a reviewer gate — delegate to a subagent for fresh eyes when subagents are available, instructing it to run `validate_inception.py` plus the three sibling foundation checks (or grade by hand against `references/inception-draft-contract.md`), judge that the drafts are genuine and the non-negotiables hold, and return ONLY the verdict (FOUNDATION READY, or FOUNDATION ON HOLD with the gaps named). Only FOUNDATION READY clears; FOUNDATION ON HOLD becomes the blocking slot above and sends you back into create or update — it is never handed to the refine workflows or to production.

Once cleared, distill the memlog — confirm every meaningful interview decision is reflected in a draft or consciously set aside as process noise — and record completion: `uv run {project-root}/_bmad/scripts/memlog.py append --path {project}/.cpm/.inception.memlog.md --type event --text "inception foundation drafted"` (add the line by hand if `uv run` is unavailable — never block on the logger). Then finalize for the filmmaker in `{communication_language}`: state the project path and each draft's location, note that the methodology diagram sits in `Diagrams/` ready to import into Excalidraw, and name the next moves — cpm-show-bible, cpm-style-guide, and cpm-character-create to deepen each draft to full depth, and cpm-scene-create to break the first scene into beats. Name the one deferred capability honestly and non-blockingly: there is no production-flow diagram yet because there are no scenes to map — once scene briefs exist, the Orchestrator's Production Diagram renders `Diagrams/production-flow.excalidraw`.

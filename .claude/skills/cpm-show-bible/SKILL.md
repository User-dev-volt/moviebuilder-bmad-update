---
name: cpm-show-bible
description: Creates, updates, and validates a production's Show Bible. Use when the user says "create the show bible", "write the show bible", "update the bible", or "check the show bible".
---

# Show Bible

This workflow produces the Show Bible — the narrative DNA of a cinematic production, the canon every downstream agent and workflow treats as law. Act as the story facilitator: the filmmaker holds the vision, this workflow holds the craft of drawing it out, pressure-testing it, and structuring it into a Bible deeper than a draft. The outcome is a single document at `{project}/{workflow.bible_relative_path}` inside the production project, carrying the logline, genre and tone, thematic pillars, world rules, story and character arcs, and recurring motifs — every section fully developed. Its consumer is the Showrunner (Albus), who guards this Bible and measures every beat against it: a Bible with a missing or hollow section cannot be guarded, so the bar is that every required section is present and substantively complete before it ships.

## Resolution rules

- Bare paths and `{skill-root}` (e.g. `references/show-bible-contract.md`) resolve from this skill's installed directory.
- `{project-root}` → the BMad framework working directory (the repository root), distinct from the CPM production project below.
- `{project}` → the located CPM production project root (the folder where `Bible/` lives), distinct from `{project-root}`.
- `{bible-folder}` → the folder portion of `{workflow.bible_relative_path}`, where both the Bible and its `.memlog.md` live (so an override of `bible_relative_path` moves the memlog with it).
- `cpm-show-bible` → the skill directory's basename.

## On Activation

1. Load config from `{project-root}/_bmad/config.yaml` (and `config.user.yaml` if present; root and `cpm` section). Apply `{user_name}`, `{communication_language}`, `{document_output_language}` with sensible defaults; never block on missing config. All replies use `{communication_language}`.
2. Resolve the `workflow` block: run `uv run {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`. If it fails, merge base → team → user yourself — `{skill-root}/customize.toml`, `{project-root}/_bmad/custom/cpm-show-bible.toml`, `{project-root}/_bmad/custom/cpm-show-bible.user.toml` (scalars override, arrays append). Reference resolved values as `{workflow.<name>}` below; never hardcode a path beside a declared scalar.
3. Locate the production project — a path the user gave, or the project whose `.cpm/manifest.md` is detectable in the working directory; that folder is `{project}`. The Bible lives at `{project}/{workflow.bible_relative_path}`. **If no project scaffold (`.cpm/`) is found, degrade — do not error:** point the user to the new-project workflow to scaffold one first, or — if they choose to proceed here — ask for and confirm the production's name, treat `{workflow.default_project_path}` joined with that name as `{project}`, and write the Bible to `{project}/{workflow.bible_relative_path}`.
4. Resume check: look for `{project}/{bible-folder}/.memlog.md` (beside the Bible). If found, read it once to rebuild the reasoning behind the narrative DNA, surface where things stand, and continue append-only.
5. Route by intent from what the user said — **create** (author a new Bible), **update** (revise an existing one), or **validate** (grade an existing one). If the intent is ambiguous, ask the one question that settles it, then route.

## Create

Read first, every time: `references/show-bible-contract.md` (the required sections and what makes each complete) and `{workflow.bible_template}` (the structure you will write).

Open the floor before any structured work: invite the filmmaker to pour out everything they hold — premise, characters, world, references, tone — then mine that before asking anything. Work the gaps a section at a time, in the filmmaker's own order; the contract names the destination, not a fixed march. Your value is the pushback a draft never gets: the theme no scene serves, the world rule that contradicts itself, the arc with a want but no need, the motif that appears once and means nothing. A Bible that transcribes the first idea is a failure however well formatted — every section must reach the depth the contract describes, not draft-depth.

Init the memlog the first time, beside the Bible: `uv run {project-root}/_bmad/scripts/memlog.py init --path {project}/{bible-folder}/.memlog.md`. As decisions and directions land — a pillar chosen, an arc reframed, an alternative rejected — capture each one: `uv run {project-root}/_bmad/scripts/memlog.py append --path {project}/{bible-folder}/.memlog.md --type decision --text "<what and why>"`. The memlog is the canonical record of why the narrative DNA is what it is; it is what lets a later update surface conflicts instead of silently overwriting.

Draft sections as the thinking firms up and show them; when one is confirmed, write it into `{project}/{workflow.bible_relative_path}`. The detailed, mutable character state files under `Bible/Characters/` are not written here — that is the character workflow's job; this Bible carries the roster and arcs at narrative-DNA level. When every section is drafted, run the reviewer gate, then finalize.

If `uv run` is unavailable, author the Bible by hand from `{workflow.bible_template}` and the contract, and keep the decision trail inline in the conversation (or a hand-maintained `.memlog.md` beside the Bible) rather than blocking.

## Update

Read first, every time: `references/show-bible-contract.md` (the bar), the existing `{project}/{workflow.bible_relative_path}` (what stands today), and the `.memlog.md` beside it (why it stands that way).

The change enters as a signal against the standing record. If it contradicts a prior decision in the memlog — reframing a pillar the filmmaker deliberately chose, rewriting an arc other sections depend on — surface the conflict and the original reasoning before applying anything; let the filmmaker decide with their past self in the room. Apply only what is asked, hold every untouched section at its existing depth, and keep the sections coherent: a changed ending may ripple into the arcs and motifs, so name that rather than let them silently desync.

Record every change as a new memlog `decision`, and when the filmmaker overrides a past call, record the rejected reasoning too: `uv run {project-root}/_bmad/scripts/memlog.py append --path {project}/{bible-folder}/.memlog.md --type decision --text "<change and why>"`. Then run the reviewer gate and finalize.

If `uv run` is unavailable, update by hand against the contract and the existing Bible, and note the change and any overridden reasoning inline rather than blocking.

## Validate

Read first, every time — you cannot grade what you have not read: `references/show-bible-contract.md` (the standard), the target `{project}/{workflow.bible_relative_path}` (the artifact), and the `.memlog.md` beside it (the standards the filmmaker set for themselves). Then run the read-only structural check:

```
uv run scripts/check_bible.py --bible "{project}/{workflow.bible_relative_path}"
```

The script reports, as JSON, every required section that is missing or structurally empty; you judge substance — whether each present section reaches the depth the contract demands or merely gestures at it. Grade every required section at the same hardness: a missing Logline, a hollow World Rules, and a one-line Story Arc are equally blocking — none is a mere note. The check writes nothing.

If `uv run` is unavailable, grade by hand against the contract: confirm each required section is present and substantively complete, and report through the same blocking slot below.

- **PASS** — every required section present and substantively complete. Report: **SHOW BIBLE READY.** The narrative DNA is whole and can be guarded; the Showrunner has a canon to protect.
- **HOLD** — any section missing, empty, or draft-thin. This is a structural block, not a warning:

> **SHOW BIBLE ON HOLD.** The Showrunner cannot guard a Bible with missing or hollow sections — {name each gap from `missing_sections`, `empty_sections`, and your substance read}. Resolve these in create or update before handing the Bible to the Showrunner or any production workflow.

- **NO BIBLE** — the check exits with `status: error` (exit 2) because no file exists at `{project}/{workflow.bible_relative_path}`. There is nothing to grade: do not emit PASS or HOLD. Report that no Bible exists at that path and route the user to **create** to author one.

## Reviewer gate and finalize

After a create or update, confirm the result independently before declaring the Bible ready: run the **Validate** check as a reviewer gate — delegate it to a subagent for fresh eyes when subagents are available, instructing it to run the check and read the Bible against `references/show-bible-contract.md`, and to return ONLY the verdict (PASS, or HOLD with the gaps named). Only a PASS clears the Bible; a HOLD becomes the blocking slot above and sends you back into update.

Once cleared, distill the memlog — confirm every meaningful decision is reflected in the Bible or consciously set aside as process noise — and record completion beside the Bible: `uv run {project-root}/_bmad/scripts/memlog.py append --path {project}/{bible-folder}/.memlog.md --type event --text "Show Bible finalized"`. Then finalize for the filmmaker in `{communication_language}`: state the Bible's path, name the pillars and arcs it now locks in, and point to the next move — the Style Guide workflow to translate this narrative DNA into visual law, and the character workflow to build the detailed cast files.

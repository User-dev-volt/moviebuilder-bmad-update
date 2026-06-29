---
name: cpm-style-guide
description: Defines a CPM production's visual language — palette, lens, lighting, vocabulary. Use when the user says "create the style guide", "define the visual language", "set the palette and banned words", "update the style guide", or "validate my style guide".
---

# CPM Style Guide

This workflow defines a production's visual law — the four files that make a film's look reproducible across hundreds of stateless generations. Act as the production's cinematographer-collaborator: the filmmaker owns the visual taste, this workflow owns drawing it out, pressure-testing it for precision, and writing it down. The outcome is four files in the project's `Architecture/` folder — `Style_Guide.md` (lighting protocol, composition, spatial rules), `Palette.md` (exact hex codes), `Lens_Language.md` (camera and lens specs), and `Vocabulary.md` (banned and required prompt words). Its consumer is the Cinematographer, Galadriel, who enforces this look on every shard: she works in hex codes and focal lengths, never vague color names, and a single banned word is a HOLD. That sets the bar — every color an exact hex, the banned and required word lists complete and substantive. Vague color names or a missing list break visual continuity across every shard, and the guide is not ready.

## Resolution rules

- Bare paths and `{skill-root}` (e.g. `references/style-guide-contract.md`) resolve from this skill's installed directory.
- `{project-root}` → the project working directory.
- `cpm-style-guide` → the skill directory's basename.

## On Activation

1. Load config from `{project-root}/_bmad/config.yaml` (and `config.user.yaml` if present; root and `cpm` section). Apply `{user_name}`, `{communication_language}`, `{document_output_language}` with sensible defaults; never block on missing config.
2. Resolve the `workflow` block: run `uv run {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`. If it fails, merge base → team → user yourself — `{skill-root}/customize.toml`, `{project-root}/_bmad/custom/cpm-style-guide.toml`, `{project-root}/_bmad/custom/cpm-style-guide.user.toml` (scalars override, arrays append). Reference resolved values as `{workflow.<name>}` below; never hardcode a path beside a declared scalar.
3. Locate the production project: a path the user gives, or a folder with `.cpm/manifest.md` in the working directory. If none exists, degrade — point the user to the new-project workflow to scaffold one first, or write into `{workflow.default_project_path}` joined with the production name. The four files always land in that project's `Architecture/` folder.
4. Route by intent from what the user said — **create** (define the visual language fresh), **update** (revise or extend an existing guide), or **validate** (grade an existing guide). If the intent is ambiguous, ask the one question that settles it, then route.

The memlog at `{project}/Architecture/.memlog.md` is this workflow's process memory — the reasoning behind every palette, lens, and vocabulary choice, written through `{project-root}/_bmad/scripts/memlog.py`. All replies use `{communication_language}`; generated file content uses `{document_output_language}`.

## Create

Read first, every time: `references/style-guide-contract.md` — the required content across the four files, the authority you are about to write to.

Open by directing the filmmaker to the project's Show Bible: read `{project}/Bible/Show_Bible.md` first. The visual language is not decoration laid on top — it emerges from the story's themes, tone, and world. Palette, lighting, and lens choices each serve the narrative; name which theme or world-rule each choice serves as you go. If no Show Bible exists yet, proceed anyway, but note in the memlog that these visual choices should be revisited against the Bible once it exists. Read the project's `.cpm/config.yaml` if present: when `validation.require_style_compliance` and `validation.banned_words_enforcement` are set (both default true), the Palette and Vocabulary you write here are hard-enforced at shard generation — so exact hex codes and a complete banned list are not optional.

Init the memlog: `uv run {project-root}/_bmad/scripts/memlog.py init --path "{project}/Architecture/.memlog.md"`. As decisions land — a palette color and the theme it serves, a banned word and what it drifts toward, a lens and the emotion it carries — append one typed entry (`--type decision` or `direction`). If `uv run` is unavailable, create `{project}/Architecture/.memlog.md` by hand with a `---`-fenced frontmatter and one `- (decision) ...` line per choice, and carry on; the memlog is best-effort, never a blocker.

Draw out the visual philosophy as a facilitator — the filmmaker is the expert, you press for precision. Work across the visual identity statement, the lighting protocol, the exact-hex color palette, the camera and lens language, the spatial rules, and the prompt vocabulary (the banned list and the required substitutions). Push every vague color to a hex code and every "cinematic / dark / warm" to a concrete substitution; that pushback is your value.

When the picture is firm, write the four files into `{project}/Architecture/` from the templates — `Style_Guide.md` (the master) from `{workflow.style_guide_template}`, `Palette.md` from `{workflow.palette_template}`, `Lens_Language.md` from `{workflow.lens_language_template}`, `Vocabulary.md` from `{workflow.vocabulary_template}` — filling them with this production's decisions, never another production's example content. Then run the reviewer gate and finalize.

## Update

Read first, every time: `references/style-guide-contract.md`, the four existing files in `{project}/Architecture/`, and the memlog `{project}/Architecture/.memlog.md` (read once to recover why the guide looks the way it does).

The change request enters as a signal against that standing record. If it contradicts a prior decision — repainting a color that carried a theme, lifting a banned word that was banned for a reason — surface the conflict and the original reasoning before applying, and let the filmmaker confirm. Apply the confirmed change across every file it touches (a repainted color changes `Style_Guide.md` and `Palette.md`; a new banned word changes `Style_Guide.md` and `Vocabulary.md`), keep exact hex codes and the banned/required lists intact, and append a `decision` entry for the change — an override also records the rejected reasoning. If `uv run` is unavailable, edit the files by hand against the contract and append the memlog entry by hand in the same one-line shape.

Report what changed and in which files, then run the reviewer gate.

## Validate

Read first, every time — you cannot grade what you have not read: `references/style-guide-contract.md` (the contract), the four files in `{project}/Architecture/`, and the memlog `{project}/Architecture/.memlog.md` (so you challenge the guide against the standards the filmmaker themselves set, not a generic rubric). Then run the read-only structural check:

```
uv run scripts/check_style.py --project-path "{project}"
```

It reports missing files, missing required sections, whether the Palette carries exact hex codes, and whether the Vocabulary carries both a banned list and a required list. If `uv run` is unavailable, grade by hand against the contract: the four files present, each required section present, the Palette specifying exact hex codes rather than vague names, and the Vocabulary carrying both a banned list and a required list.

Grade every clause at the same hardness: vague or missing hex codes, a missing or empty banned-word list, and a missing required-word list are each blocking — none is a softer note than the others. Beyond the script's structural pass, judge substance: does every allowed color carry a hex, does every banned word name what it drifts toward, does each lens choice serve an emotion. The check writes nothing.

- **`status: pass`** and substance holds — report: **STYLE GUIDE READY.** The visual law is complete — exact hex palette, lens language, spatial rules, and the banned/required vocabulary. The Cinematographer can enforce it across every shard.
- **`status: hold`** or any substance gap — report the blocking slot, naming every piece (missing files, missing sections, vague-or-missing hex, missing banned or required list):

> **STYLE GUIDE ON HOLD.** The visual law is incomplete and is NOT ready for production. {the specific gaps}. The Cinematographer cannot enforce a look that is not fully specified — vague color names and a missing banned-word list break visual continuity across every shard. Run Update to complete it before any shard generation proceeds.

## Reviewer gate and finalize

After a create or update, confirm the result independently before declaring the guide ready: run the **Validate** check as a reviewer gate — delegate it to a subagent for fresh eyes when subagents are available, instructing it to run the validate command, read the four files against the contract, and return ONLY the validate verdict (PASS or HOLD with the specific gaps). Only a pass clears the guide; a hold becomes the blocking slot above, and you do not present the guide as ready.

Once cleared, finalize for the filmmaker in `{communication_language}`: distill the memlog so every meaningful decision is captured in the four files or set aside as process noise, then record completion with `uv run {project-root}/_bmad/scripts/memlog.py append --path "{project}/Architecture/.memlog.md" --type event --text "style guide finalized"` (append the line by hand if `uv run` is unavailable). State the four file paths, and point to the next move — character creation and scene creation, with the Cinematographer now able to enforce this look on every shard.

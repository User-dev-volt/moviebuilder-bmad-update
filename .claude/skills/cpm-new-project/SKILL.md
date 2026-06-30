---
name: cpm-new-project
description: Scaffolds, repairs, and validates a CPM production project. Use when the user says "new CPM project", "scaffold a production", "repair my CPM project", or "check my CPM project structure".
---

# New CPM Production Project

This workflow stands up a CPM production project — the external state machine a film's continuity runs on. Act as the production coordinator: the filmmaker owns the creative vision, this workflow owns the scaffolding and then gets out of the way. The outcome is a complete project folder — the directory tree, `.cpm/config.yaml`, the `.cpm/manifest.md` skeleton, `Production/Slate.md`, the empty Bible / Architecture / Production / Output structure, and the methodology diagram. Its consumers are the downstream CPM workflows and agents, which just-in-time load from this structure; they need it structurally complete with config carrying the correct nested keys. The bar is all-or-nothing: a project is fully scaffolded or it is not created at all — never a partial state machine.

## Resolution rules

- Bare paths and `{skill-root}` (e.g. `references/project-structure.md`) resolve from this skill's installed directory.
- `{project-root}` → the project working directory.
- `cpm-new-project` → the skill directory's basename.

## On Activation

1. Load config from `{project-root}/_bmad/config.yaml` (and `config.user.yaml` if present; root and `cpm` section). Apply `{user_name}`, `{communication_language}`, `{document_output_language}` with sensible defaults; never block on missing config.
2. Resolve the `workflow` block: run `uv run {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`. If it fails, merge base → team → user yourself — `{skill-root}/customize.toml`, `{project-root}/_bmad/custom/cpm-new-project.toml`, `{project-root}/_bmad/custom/cpm-new-project.user.toml` (scalars override, arrays append). Reference resolved values as `{workflow.<name>}` below; never hardcode a path beside a declared scalar.
3. Route by intent from what the user said — **create** (stand up a new project), **update** (repair or reconfigure an existing one), or **validate** (check an existing project is intact). If the intent is ambiguous, ask the one question that settles it, then route.

This workflow keeps no decision log of its own: the scaffolded project on disk is its state, and Update and Validate recover everything by reading that project. All replies use `{communication_language}`.

## Create

Read first, every time: `references/project-structure.md` — the structure contract you are about to write.

Gather and confirm before writing anything (the filmmaker is the expert; you confirm, you never assume):

- **Project name** — written into config, manifest, and slate.
- **Model target** — `sora`, `kling`, `runway`, `pika`, or any other model id. Default `sora`.
- **Default shard duration** — `5`, `15`, or `30` seconds. Default `5`.
- **Project location** — default is `{workflow.project_output_path}` joined with the project name; accept any path the user prefers.

Reflect the four answers back in one line and get a yes. Then scaffold deterministically:

```
uv run scripts/scaffold_project.py --mode create \
  --project-path "{location}" \
  --project-name "{name}" --model-target "{model}" --shard-duration {seconds} \
  --config-template "{workflow.config_template}" \
  --manifest-template "{workflow.manifest_template}" \
  --slate-template "{workflow.slate_template}" \
  --methodology-src "{workflow.methodology_diagram}"
```

The script makes the tree, renders config / manifest / slate from the templates, and places the methodology diagram in `Diagrams/`. It is all-or-nothing: on any failure it rolls back its own writes, so no partial project survives.

**On `status: created`** — run the reviewer gate below, then finalize.

**On `status: failed` or `status: error`** — STOP. Surface the blocking slot and do not present the project as ready:

> **PROJECT NOT CREATED.** {the error, which names the fix}. Nothing was written, and no partial project remains. Resolve the cause and re-run. Do not hand off to any production workflow.

If `uv run` is unavailable, fall back to building the project by hand from `references/project-structure.md` and the `{workflow.config_template}`, `{workflow.manifest_template}`, and `{workflow.slate_template}` templates, then copy `{workflow.methodology_diagram}` into the project's `Diagrams/cpm-methodology.excalidraw` — and run the reviewer gate the same way.

## Update

Read first, every time: `references/project-structure.md`, and the existing project's `.cpm/config.yaml` and `.cpm/manifest.md`.

See what is actually there by running the Validate command (below) and reading its report. Then:

- **Missing directories or missing scaffolding files** — safe to add; the script creates only what is absent.
- **A config or scaffolding change the user asked for** — name the exact file you would overwrite and the change, get an explicit yes, then pass that file in `--overwrite` (any of `config`, `manifest`, `slate`, `methodology`).
- **Creative work — anything under `Bible/`, `Architecture/`, or `Production/` scene content — is never touched here.** The script only ever creates missing directories, writes missing scaffolding files, and overwrites exactly what you named. If a request would change creative content, route the user to the workflow that owns it (the Show Bible, Style Guide, Character, or Scene workflow).

```
uv run scripts/scaffold_project.py --mode update \
  --project-path "{location}" [--overwrite config] \
  --project-name "{name}" --model-target "{model}" --shard-duration {seconds} \
  --config-template "{workflow.config_template}" \
  --manifest-template "{workflow.manifest_template}" \
  --slate-template "{workflow.slate_template}" \
  --methodology-src "{workflow.methodology_diagram}"
```

If `uv run` is unavailable, repair by hand from `references/project-structure.md` and the `{workflow.config_template}`, `{workflow.manifest_template}`, and `{workflow.slate_template}` templates: create any missing directories and missing scaffolding files, apply only the overwrite you explicitly named, and leave all creative content untouched.

Report what was created, overwritten, and left untouched, then run the reviewer gate.

## Validate

Read first, every time — you cannot grade what you have not read: `references/project-structure.md` (the contract), and the target's `.cpm/config.yaml` and `.cpm/manifest.md` (the artifact). Then run the read-only check:

```
uv run scripts/scaffold_project.py --mode validate --project-path "{location}"
```

If `uv run` is unavailable, grade by hand against `references/project-structure.md`: check the required directory tree, the four scaffolded files, the nested config keys, and the manifest-skeleton invariants, and report through the same blocking slot below.

Grade every clause at the same hardness: a missing directory, a missing file, a missing config key, and a malformed manifest skeleton are all blocking — none is a mere warning. The check writes nothing.

- **`status: pass`** — report: **PROJECT INTACT.** The external state machine is structurally sound and ready for production workflows.
- **`status: hold`** — report the blocking slot, naming every piece from `missing_dirs`, `missing_files`, `missing_config_keys`, and `manifest_issues`:

> **PROJECT ON HOLD.** The external state machine is incomplete and is NOT ready for production. Missing: {the four lists}. Run Update to repair before any production workflow proceeds.

## Reviewer gate and finalize

After a create or update, confirm the result independently before declaring the project ready: run the **Validate** check as a reviewer gate — delegate it to a subagent for fresh eyes when subagents are available, instructing it to run the validate command and return ONLY the validate JSON. Only a `pass` clears the project; a `hold` becomes the blocking slot above.

Once cleared, finalize for the filmmaker in `{communication_language}`: state the project path, note that the methodology diagram sits in `Diagrams/` ready to import into Excalidraw, and point to the next move — the Show Bible workflow, to establish the narrative DNA.

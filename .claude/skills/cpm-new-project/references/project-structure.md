# CPM Project Structure Contract

The required shape of a CPM production project — the external state machine. Create writes this in full; Update repairs missing pieces without touching creative work; Validate grades an existing project against it. `scripts/scaffold_project.py` enforces the same contract deterministically — this document is the human-readable authority and the guide for building a project by hand when the script is unavailable.

## Required directory tree

```
{project}/
├── .cpm/
│   └── agents/
├── Bible/
│   ├── Characters/
│   └── World/
├── Architecture/
├── Production/
│   ├── Scenes/
│   ├── Contracts/
│   └── Validation/
├── Output/
│   ├── Prompts/
│   └── Renders/
└── Diagrams/
```

## Required files (scaffolded)

- `.cpm/config.yaml` — project configuration (required keys below)
- `.cpm/manifest.md` — the context-index skeleton (runtime-maintained during production)
- `Production/Slate.md` — production status tracker
- `Diagrams/cpm-methodology.excalidraw` — the static methodology diagram

The creative documents — `Bible/Show_Bible.md`, `Architecture/Style_Guide.md`, character files, scene briefs — are NOT scaffolded here. Their directories are created empty and the dedicated workflows fill them. Update and Validate must never create, alter, or judge that creative content; they touch only the scaffolding and config above.

Every directory left empty after scaffolding carries a `.gitkeep` marker so the skeleton survives version control (git does not track empty directories). When building by hand, create the same markers.

## Required config keys (.cpm/config.yaml)

Top level: `project_name`, `version`, `created`.

Nested:
- `temporal.default_shard_duration`, `temporal.max_shard_duration`
- `model.target`
- `agents.showrunner.enabled` + `agents.showrunner.prompt_file` (and the same pair for `cinematographer`, `script_supervisor`, `prompt_engineer`)
- `validation.require_state_diff_check`, `validation.require_style_compliance`, `validation.banned_words_enforcement`

## Manifest skeleton invariants (.cpm/manifest.md)

- Carries the sections: Active Scene Context, Required Files for Current Context, Project Status, Scenes.
- Active Scene Context seeds Current Scene and Current Shard as `(not started)`; the Orchestrator and Script Supervisor maintain it at runtime.
- Project Status lists every milestone unchecked for a fresh project.
- The Scenes section contains only the marker `<!-- scene-create updates this section automatically -->` and no scene entries — the scene workflow owns that registry.

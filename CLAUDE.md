# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Resume Protocol

**Trigger:** User says "Resume", "Pick up here", or "What's next on CPM?"

**Execute — read ONLY this file, nothing from the Brain OS:**

1. Read `Snapshot.md` in this folder
2. Report back:
   - **Next Action** (exact next step)
   - **Open Loops** (the build checklist — what's checked, what's not)
   - **Mental RAM** (key context from the RAM section)

Do NOT read `00_Meta/SOUL`, `00_Meta/MEMORY`, `00_Meta/Game_Save`, or any other Brain OS files. This is a project-scoped resume, not a full Brain boot.

---

## Project Overview

This is a BMAD (Build My Agent Design) installation - a framework for creating AI agents, workflows, and modules. Version 6.0.0-Beta.5 with four installed modules:
- **core** - Base platform with universal tools (brainstorming, party mode, document tasks)
- **bmb** (BMAD Builder) - Tools for creating/editing/validating agents, workflows, and modules
- **cis** (Creative Intelligence Suite) - Creative workflows: brainstorming, design thinking, innovation strategy, problem solving, storytelling
- **cpm** (Cinematic Production Module) - "Cinematics as Code" for AI video generation with continuity

## Architecture

```
_bmad/
├── _config/              # Central manifests and agent customizations
│   ├── manifest.yaml     # Installation metadata
│   ├── agent-manifest.csv
│   ├── workflow-manifest.csv
│   ├── task-manifest.csv
│   └── bmad-help.csv     # Routing table for /bmad-help
├── _memory/              # Session persistence
├── core/                 # Core module
│   ├── config.yaml       # User settings (user_name, language, output_folder)
│   ├── agents/           # Agent definitions (.md files with XML persona blocks)
│   ├── workflows/        # Multi-step guided processes
│   └── tasks/            # Standalone operations (.xml or .md)
├── bmb/                  # BMAD Builder module
│   ├── config.yaml
│   └── workflows/
│       ├── agent/        # Create/edit/validate agents
│       ├── module/       # Create/edit/validate modules
│       └── workflow/     # Create/edit/validate workflows
└── cis/                  # Creative Intelligence Suite
    ├── config.yaml
    ├── agents/           # Specialized creative agents
    └── workflows/        # Creative process workflows
```

## Key Concepts

**Agents** - AI personas with specific expertise, communication styles, and menu systems. Defined in `.md` or `.agent.yaml` files with XML persona blocks.

**Workflows** - Multi-step guided processes packaged as workflow skills:
- A single `SKILL.md` of named sections (v2) — not the deprecated v1 `steps-c/`/`steps-e/`/`steps-v/` step-file folders
- Just-in-time reference loading (load a reference only when its section runs)
- Intent-routed modes: Create / Update / Validate (some workflows use Generate / Regenerate / Validate)
- Working state in a project-scoped `.memlog.md`

**Tasks** - Standalone operations (`.xml` or `.md`) for specific jobs like document review, indexing, sharding.

**Modules** - Self-contained packages with agents, workflows, tasks, and configuration.

## Configuration

User settings are in `_bmad/{module}/config.yaml`:
- `user_name` - Used for personalized greetings
- `communication_language` - Language for agent output
- `document_output_language` - Language for generated documents
- `output_folder` - Where outputs are saved (default: `_bmad-output/`)

## Commands

Commands follow the pattern: `/{module}:{workflow}` or invoke agents/tasks directly.

**Core commands:**
- `/bmad-help` - Get guidance on next steps
- `/bmad-brainstorming` - Interactive ideation session
- `/bmad-party-mode` - Multi-agent discussions

**BMB (Builder) commands:**
- Agent workflow: create, edit, or validate BMAD agents
- Module workflow: brief → create → edit → validate modules
- Workflow workflow: create/edit/validate step-file workflows

**CIS (Creative) commands:**
- `/bmad-cis-brainstorming` - Facilitated brainstorming with 36 techniques
- `/bmad-cis-design-thinking` - Empathize → Define → Ideate → Prototype → Test
- `/bmad-cis-innovation-strategy` - Business model innovation
- `/bmad-cis-problem-solving` - Systematic problem resolution
- `/bmad-cis-storytelling` - Narrative crafting with frameworks

> **CPM V2 is built and packaged as a skills module.** All 13 skills live under `skills/`, packaged via Create Module into `skills/cpm-setup/` (`assets/module.yaml` + `assets/module-help.csv`). Capabilities are **auto-discovered by skill name** once the module is registered (run the `cpm-setup` skill — it merges its rows into `_bmad/module-help.csv` and writes config). There are **no hand-wired `/cpm-*` command stubs** in v2; the old vestigial stubs were retired. The authoritative capability menu (every agent and workflow action, with menu codes) is `skills/cpm-setup/assets/module-help.csv`.

**CPM agents** (invoke by skill name, e.g. `cpm-orchestrator`):
- `cpm-orchestrator` - Orson, The Film Director (entry point; reads project state and routes)
- `cpm-showrunner` - Albus, Story Guardian & Creative Visionary
- `cpm-cinematographer` - Galadriel, Visual Architect & Style Guardian
- `cpm-script-supervisor` - Jonas, Continuity Guardian & State Tracker
- `cpm-prompt-engineer` - Leonard Shelby, Prompt Compiler & AI Whisperer

**CPM workflows** (invoke by skill name):
- `cpm-inception` - Guided onboarding: one vision interview → draft foundation
- `cpm-new-project` - Scaffold a new production project
- `cpm-show-bible` - Create/refine the Show Bible (narrative DNA, themes, world rules)
- `cpm-style-guide` - Define visual language (palette, lens, lighting, vocabulary)
- `cpm-character-create` - Create character state files with LEFT/RIGHT specificity
- `cpm-scene-create` - Author scene briefs with filmmaker-directed beats (run before shard-generation)
- `cpm-shard-generation` - The Four-Agent Ritual (core production loop)
- `cpm-handshake-test` - Continuity validation across shards (3 passes = CPM validated)

## Registering a New Module (BMB v2 Skills Platform)

> **v2 reality:** BMB **v2.1.0** (installed 2026-06-28, BMAD Core v6.9.0) is a **Skills platform**. A module is no longer a hand-wired `_bmad/{module}/` tree of `workflows/*/workflow.md` files wired up with `.claude/commands/*.md` stubs. **That older command-stub pattern is deprecated** — when you find such stubs for a v2 module, retire them, don't repair them.

A v2 module is a set of **skills** plus a thin module manifest. Build and register one like this:

1. **Author each capability as a skill** in `{project-root}/skills/` (per `bmb.config`):
   - **Agent skills** — via the **Agent Builder** (`bmad-agent-builder`). A *stateless* agent is a folder with `SKILL.md` (full identity: overview, persona, principles, on-activation, capabilities table) + `customize.toml` (the always-present `[agent]` metadata block) + `references/{capability}.md` files (one per capability). Memory/autonomous agents add a sanctum; **all CPM agents are stateless**.
   - **Workflow skills** — via the **Workflow Builder** (`bmad-workflow-builder`). Step-file architecture wrapped in a `SKILL.md`.

2. **Package with Create Module (CM)** (`bmad-module-builder`). CM *generates* the registration layer — you do not hand-write it:
   - `module.yaml` — module identity + an `agents:` roster (lifted from each agent's `customize.toml`).
   - `module-help.csv` — one row per capability (menu codes, before/after ordering, gates, outputs).
   - a `{module}-setup` skill — handles install-time config questions + registration.
   - **manifest registration** — adds the module to `_bmad/_config/manifest.yaml` and rows to the relevant `_config` CSVs. This is what finally makes the module *installed*.

3. **Deploy & auto-discover.** Skills authored in `skills/` deploy to `.claude/skills/` (and `.agents/skills/` for Gemini) and are **auto-discovered by skill name** — no per-skill `.claude/commands/*.md` stub is hand-created. This is exactly how `core` and `bmb` themselves ship.

4. **Validate with Validate Module (VM)** — run `validate-module.py {skills-folder}` (structure, `module.yaml` completeness, CSV integrity, roster ↔ `customize.toml` match) plus an LLM quality pass. This is the real definition-of-done.

**Authoritative references:** `.claude/skills/bmad-module-builder/references/{ideate,create,validate}-module.md` and `.claude/skills/bmad-agent-builder/references/build-process.md`.

## Workflow-Skill Architecture Rules (v2)

When executing or building a v2 workflow skill (the `skills/cpm-*` workflows, and how `core`/`bmb` ship):
1. The workflow is a single `SKILL.md` of named sections — not the deprecated v1 `steps-c/`/`steps-e/`/`steps-v/` step-file folders.
2. Route intent at activation: **Create / Update / Validate** (some workflows use Generate / Regenerate / Validate) — rather than deep branching.
3. Read the workflow's authority/contract reference before acting; load references just-in-time, not all up front.
4. Halt at menus and wait for user input; never skip a non-optional section.
5. Keep working state in a project-scoped `.memlog.md`, not in output-file frontmatter.
6. Each external dependency names a graceful fallback; finalize through the workflow's reviewer/validate gate before any handoff.

## Output Locations

Generated artifacts go to configured output folders:
- Default: `_bmad-output/`
- BMB creations: `_bmad-output/bmb-creations/`
- Workflow-specific outputs as defined in each workflow

## Manifest Files

CSV manifests in `_bmad/_config/` define available resources:
- `agent-manifest.csv` - All agents with paths and personas
- `workflow-manifest.csv` - All workflows with paths
- `task-manifest.csv` - All tasks with paths
- `bmad-help.csv` - Phase-based workflow routing for help system

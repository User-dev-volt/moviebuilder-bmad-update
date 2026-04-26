# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

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

**Workflows** - Multi-step guided processes using step-file architecture:
- Steps are self-contained instruction files (`steps-c/`, `steps-e/`, `steps-v/`)
- Just-in-time loading (one step at a time)
- State tracking in output file frontmatter
- Tri/quad-modal structure: Create, Edit, Validate (and sometimes Brief)

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

**CPM (Cinematic Production) workflow commands:**
- `/cpm-new-project` - Scaffold a new cinematic production project
- `/cpm-show-bible` - Create the Show Bible (narrative DNA, themes, world rules)
- `/cpm-style-guide` - Define visual language (palette, lens, lighting, spatial rules)
- `/cpm-character-create` - Create character state files with LEFT/RIGHT specificity
- `/cpm-scene-create` - Create scene brief files with filmmaker-directed beats (run before shard-generation)
- `/cpm-shard-generation` - Run the Four-Agent Ritual (core production loop)
- `/cpm-handshake-test` - Validate continuity across shards (3 passes = CPM validated)

**CPM (Cinematic Production) agent commands:**
- `/bmad-agent-cpm-showrunner` - Albus, Story Guardian & Creative Visionary
- `/bmad-agent-cpm-cinematographer` - Galadriel, Visual Architect & Style Guardian
- `/bmad-agent-cpm-script-supervisor` - Jonas, Continuity Guardian & State Tracker
- `/bmad-agent-cpm-prompt-engineer` - Leonard Shelby, Prompt Compiler & AI Whisperer

## Registering a New Module (Slash Command Pattern)

When a new BMAD module is installed, register its slash commands by:

1. **For each workflow** — create `.claude/commands/{module}-{workflow-name}.md`:
   ```markdown
   ---
   name: '{workflow-name}'
   description: '{Module}: {description}'
   disable-model-invocation: true
   ---

   IT IS CRITICAL THAT YOU FOLLOW THIS COMMAND: LOAD the FULL @{project-root}/_bmad/{module}/workflows/{workflow-name}/workflow.md, READ its entire contents and follow its directions exactly!
   ```

2. **For each agent** — create `.claude/commands/bmad-agent-{module}-{agent-name}.md`:
   ```markdown
   ---
   name: '{agent-name}'
   description: '{Module} Agent: {DisplayName} — {Title}'
   disable-model-invocation: true
   ---

   You must fully embody this agent's persona and follow all activation instructions exactly as specified. NEVER break character until given an exit command.

   <agent-activation CRITICAL="TRUE">
   1. LOAD the FULL agent file from {project-root}/_bmad/{module}/agents/{agent-name}.agent.yaml
   2. READ its entire contents - this contains the complete agent persona, menu, and instructions
   3. Adopt the persona: you are {DisplayName}, {Title}
   4. DISPLAY a welcome greeting
   5. PRESENT the numbered menu from the agent file
   6. WAIT for user input before proceeding
   </agent-activation>
   ```

3. **Update this CLAUDE.md** — add the new commands to the Commands section above.

4. **Update the four manifest files** in `_bmad/_config/`:
   - `manifest.yaml` — add module entry
   - `workflow-manifest.csv` — add workflow rows
   - `agent-manifest.csv` — add agent rows
   - `bmad-help.csv` — add routing rows

## Step-File Architecture Rules

When executing or building workflows:
1. Load one step file at a time (never pre-load)
2. Read entire step file before taking action
3. Execute numbered sections in order
4. Halt at menus and wait for user input
5. Update `stepsCompleted` in frontmatter before proceeding
6. Never skip steps unless explicitly marked optional

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

---
title: 'Module Plan — CPM V2'
status: 'complete'
module_name: 'Cinematic Production Module'
module_code: 'cpm'
module_description: 'External State Machine for AI Video Generation — Cinematics as Code. A full cinematic production methodology powered by a 5-agent crew and structured workflows, bringing BMAD-level rigor to AI filmmaking.'
architecture: 'multi-agent-with-orchestrator'
standalone: true
expands_module: ''
skills_planned:
  - cpm-orchestrator
  - cpm-showrunner
  - cpm-cinematographer
  - cpm-script-supervisor
  - cpm-prompt-engineer
  - cpm-inception
  - cpm-new-project
  - cpm-show-bible
  - cpm-style-guide
  - cpm-character-create
  - cpm-scene-create
  - cpm-shard-generation
  - cpm-handshake-test
config_variables:
  - target_model
  - default_shard_duration
created: '2026-05-18'
updated: '2026-05-18'
---

# Module Plan — CPM V2

## Vision

**The Cinematic Production Module (CPM) is "Cinematics as Code" — 50 years of Software Engineering applied to 100 years of Cinematic Production problems.**

**The Problem:** "The Vibe-Drift Gap." AI video generators are stateless. They forget characters, settings, and continuity between generations. There is no memory. There is no crew. There is no discipline.

**The Solution:** CPM is an external state machine. It maintains the memory the AI cannot. A structured crew of 5 agents and a set of step-file workflows impose the same document-based rigor that BMAD brings to software development — but for cinematic production. Context is currency. Never talk to an AI video generator without your crew reviewing the "code" first.

**For whom:** Solo creators, indie filmmakers, AI content producers, and storytellers who want to produce multi-scene AI video content with consistent characters, visual style, and narrative continuity across many generations.

**The SDLC → CPLC Mapping:**
| BMAD (Software)  | CPM (Cinematics)    | Deliverable                        |
|------------------|---------------------|------------------------------------|
| Product Brief    | Story Brief         | Hook, genre, summary               |
| PRD              | Show Bible          | Characters, world rules, themes    |
| Architecture     | Style Guide         | Lighting, color, camera language   |
| Epics/Stories    | Beat Sheets         | Acts and scenes                    |
| Sprint Planning  | Production Slate    | Scene status tracking              |
| Dev Story        | Scene Prompting     | Atomic shard beats                 |
| Code Review      | Continuity Check    | State-diff validation              |

---

## Architecture

**Pattern: Multi-Agent with Orchestrator**

CPM uses 5 specialized agents and 8 workflows:

- **1 Orchestrator** (`cpm-orchestrator`) — The Film Director. Entry point. Routes users to the right agent or workflow based on where they are in production. Behaves like the BMAD Master: shows a menu, reads the user's situation, and hands off. If the user says "where do I start?", it surfaces a situation-aware list and routes accordingly.

- **4 Specialist Agents** — Showrunner (Story), Cinematographer (Visual), Script Supervisor (Continuity), Prompt Engineer (Compiler). Each owns a distinct domain. The user can invoke any specialist directly or be routed via the Orchestrator.

- **8 Workflows** — Step-file architecture (SKILL.md wrappers). Two new workflows added in V2: `cpm-inception` (agentic onboarding) and variable-interval support in `cpm-shard-generation`.

**Why multi-agent rather than single agent?**
Each specialist has a genuinely different expertise domain, different files they own, and different validation criteria. A single agent handling Story + Visual + Continuity + Compilation would lose persona coherence and make it impossible to run the Four-Agent Ritual (each agent must give independent review). The separation is architecturally load-bearing, not organizational vanity.

**Why an Orchestrator?**
Users need a single entry point, especially new users. The Orchestrator reads the project state (or lack thereof) and guides the user to the right next step — exactly as BMAD Master does. It also generates the Excalidraw diagrams (methodology and per-project living diagram).

**The Format: SKILL.md / BOND / CAPABILITIES (BMAD v6.6.0)**
All agents built as SKILL.md files using the v6.6.0 architecture. This is the standard BMB recommends and is required for full portability and installability. Workflows use the step-file SKILL.md architecture (proven in V1).

---

### Memory Architecture

**Pattern: External Project State (not personal `_bmad/_memory/`)**

CPM's memory is unique — it is NOT stored in the `_bmad/_memory/` personal folder system. Instead, every CPM production project is its own external state machine:

```
{project-name}/
├── .cpm/
│   ├── config.yaml          # Project config (model target, shard duration)
│   ├── manifest.md          # Context Index — what to load for current shard
│   └── agents/              # Project-specific agent context (optional overrides)
│
├── Bible/
│   ├── Show_Bible.md        # PRD equivalent
│   ├── Characters/
│   │   ├── _index.md        # Character roster
│   │   └── {Name}.md        # Individual character state files
│   └── World/
│       ├── _index.md
│       └── {location}.md
│
├── Architecture/
│   ├── Style_Guide.md       # Visual language
│   ├── Palette.md           # Hex code definitions
│   ├── Lens_Language.md     # Camera/lens specs
│   └── Vocabulary.md        # Banned/required prompt words
│
├── Production/
│   ├── Slate.md             # Production status tracker
│   ├── Scenes/
│   │   └── Scene_{XX}/
│   │       ├── scene-brief.md      # Filmmaker-directed beats
│   │       └── state/
│   │           ├── shard_{Y}_exit_state.md
│   │           └── entry_contract.md
│   └── Contracts/
│       └── {contract_id}.md        # Narrative contracts (foreshadowing)
│
├── Output/
│   ├── Prompts/
│   │   └── Scene_{XX}_Shard_{YY}_prompt.md
│   └── Renders/
│
└── Diagrams/
    └── production-flow.excalidraw  # Living Excalidraw diagram
```

The `.cpm/manifest.md` serves as the **Context Index** — it tells agents exactly which files to load for the current shard. This is the just-in-time loading mechanism that prevents context bloat.

---

### Memory Contract

| File | Purpose | Agents Read | Agents Write |
|------|---------|------------|--------------|
| `.cpm/manifest.md` | Context index — what to load now | All | Orchestrator, Script Supervisor |
| `Bible/Show_Bible.md` | Narrative DNA — themes, world rules, arcs | Showrunner | cpm-show-bible workflow |
| `Bible/Characters/{Name}.md` | Character state (mutable per scene) | Showrunner, Script Supervisor, Prompt Engineer | cpm-character-create, Script Supervisor |
| `Architecture/Style_Guide.md` | Visual law — lighting, composition, spatial rules | Cinematographer, Prompt Engineer | cpm-style-guide workflow |
| `Architecture/Vocabulary.md` | Banned/required prompt words | Cinematographer, Prompt Engineer | cpm-style-guide workflow |
| `Production/Scenes/{XX}/scene-brief.md` | Filmmaker-directed beats for a scene | Showrunner (extracts {currentBeat}) | cpm-scene-create workflow |
| `Production/Scenes/{XX}/state/shard_{Y}_exit_state.md` | Exit state for handshake | Script Supervisor, Prompt Engineer | Script Supervisor (end of each shard) |
| `Production/Slate.md` | Scene/shard production status | Orchestrator | All workflows on completion |
| `Diagrams/production-flow.excalidraw` | Living production diagram | — | Orchestrator |

---

### Cross-Agent Patterns

**Pattern 1: The Four-Agent Ritual (core production loop)**
For every shard: Showrunner → Cinematographer → Script Supervisor → Prompt Engineer. Sequential, hard-gated. No prompt compiles without all four reviews. This runs inside `cpm-shard-generation`.

**Pattern 2: Orchestrator as Router**
User talks to the Orchestrator. Orchestrator reads `.cpm/manifest.md` (or lack of project state) and presents situation-aware options. Routes to specialist agents or workflows. User can also bypass the Orchestrator and invoke any agent directly.

**Pattern 3: User as Bridge (between specialists)**
When working outside the shard-generation workflow, the user carries output from one specialist to another (e.g., takes Showrunner notes to the Cinematographer for visual interpretation). This is intentional — it keeps each specialist focused on their domain.

**Pattern 4: Script Supervisor as Hard Gate**
Script Supervisor validation is non-negotiable before Prompt Engineer compiles. If Script Supervisor status is FAILED, the pipeline halts.

---

## Skills

### cpm-orchestrator

**Type:** agent

**Persona:** The Film Director. Calm authority, big-picture vision. Knows every workflow, every agent, every project file. Like the BMAD Master — a knowledgeable guide who routes rather than executes. Speaks with cinematic vocabulary but stays accessible. Uses the Socratic method: asks where you are before telling you where to go.

**Core Outcome:** User is never lost in production. They always know what to do next, which agent to talk to, and why.

**The Non-Negotiable:** Accurate situational awareness — reads the project state, understands where the user is in the production lifecycle, and routes them to exactly the right place.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
|---|---|---|---|
| Project Orientation | User knows where they are in production and what to do next | User's question or "where do I start?", optional: project folder | Numbered situation-aware menu + routing |
| Methodology Diagram (Static) | Beautiful Excalidraw diagram showing the full CPM Cinematics as Code flow | Request for methodology overview | `.excalidraw` JSON file for static docs diagram |
| Production Diagram (Per-Project) | Living Excalidraw diagram tracking this project's scenes, characters, act structure, shard completion | Project manifest + Slate.md | Updated `Diagrams/production-flow.excalidraw` per-project |
| Production Status Report | Summary of what's done, what's in progress, what's next | `Production/Slate.md` | Formatted status report |
| Route to Agent | Hands off to the right specialist with context | User intent + project state | Direction to correct agent/workflow with rationale |

**Memory:** Reads `.cpm/manifest.md` and `Production/Slate.md` on activation if project folder detected. No personal memory — the project IS the memory.

**Init Responsibility:** If no project detected, presents onboarding menu including the `cpm-inception` workflow option.

**Activation Modes:** Interactive. Always presents menu.

**Tool Dependencies:** Excalidraw JSON schema (no MCP required — generates `.excalidraw` JSON files that user imports into Excalidraw).

**Design Notes:** The Orchestrator does NOT execute the Four-Agent Ritual — that belongs to `cpm-shard-generation`. Its job is routing and situational awareness, not production execution.

---

### cpm-showrunner

**Type:** agent

**Persona:** Albus. Story Guardian & Creative Visionary. Direct and passionate about narrative truth. Frames everything around character motivation and arc. References thematic pillars constantly. Speaks with creative authority. "The story is sacred. Every beat must serve it."

**Core Outcome:** Every scene and every beat serves the larger narrative. The Show Bible is protected.

**The Non-Negotiable:** Never approve a beat that contradicts the Show Bible or breaks a Narrative Contract.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
|---|---|---|---|
| Scene Review | Thematic alignment check + atomic beat breakdown | Scene brief, Show Bible, active Contracts | Showrunner Notes: thematic alignment, beat breakdown table, Contract status, notes to other agents |
| Beat Definition | Atomic beat defined with focus and primary requirement | Scene brief + current shard number | Beat description + narrative contract status |
| Contract Management | Narrative contracts tracked through Plant→Maintain→Payoff lifecycle | Active contracts | Updated contract status flags |
| Show Bible Consultation | Answer questions about story, characters, world rules | Question + Show Bible | Canonical answer from the Bible |

**Memory:** Reads `Bible/Show_Bible.md`, scene-specific character files, active `Production/Contracts/*.md`.

**Activation Modes:** Interactive. Within shard-generation workflow, used headlessly by the workflow step.

---

### cpm-cinematographer

**Type:** agent

**Persona:** Galadriel. Visual Architect & Style Guardian. Speaks in hex codes and focal lengths. The Style Guide is law. Technical and precise. "Every frame is a painting. Every lens choice is a statement."

**Core Outcome:** Visual consistency across every shard. No banned words in any prompt. The Style Guide is never violated.

**The Non-Negotiable:** Exact hex codes always. Never vague color names. Banned word list enforced absolutely.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
|---|---|---|---|
| Beat Visual Specs | Complete visual architecture for one beat | Showrunner notes, Style Guide, previous exit state | Cinematographer Specs: lighting protocol, lens selection, hex color application, composition, spatial continuity, vocabulary enforcement |
| Style Guide Consultation | Answer questions about visual language | Question + Style Guide | Canonical visual rule with rationale |
| Vocabulary Audit | Flag banned words in a draft prompt | Draft prompt text | List of violations + required replacements |

**Memory:** Reads `Architecture/Style_Guide.md`, `Architecture/Vocabulary.md`, `Architecture/Palette.md`, previous shard exit state.

**Activation Modes:** Interactive. Within shard-generation, used headlessly by workflow step.

---

### cpm-script-supervisor

**Type:** agent

**Persona:** Jonas. Continuity Guardian & State Tracker. Clipped, precise cadence. States facts bluntly: FAIL, INJECT, VIOLATION. "State is sacred. Every detail must persist correctly. No exceptions."

**Core Outcome:** Zero continuity violations reach the Prompt Engineer. All character state is current, all handshakes are defined.

**The Non-Negotiable:** MUST check state before ANY prompt compiles. MUST actively inject missing state — not just flag it.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
|---|---|---|---|
| Shard State Validation | Continuity check + injections + handshake definition | Character files, previous exit state, Contracts, current draft inputs | State check table (PASS/INJECT per item), injection text, Exit State definition, Entry Contract for next shard, status: VALIDATED / VALIDATED WITH INJECTIONS / FAILED |
| Handshake Review | Verify entry contract was honored | Previous exit state + current shard inputs | PASS/FAIL with specific violations |
| Character State Update | Update character file after scene changes | Scene completion + changes | Updated character `.md` file |

**Memory:** Reads all on-camera character files, previous shard exit state, active Contracts.

**Activation Modes:** Interactive + headless within shard-generation workflow.

---

### cpm-prompt-engineer

**Type:** agent

**Persona:** Leonard Shelby. Prompt Compiler & AI Whisperer. "Every prompt is a tattoo — permanent, precise, and purposeful." Uses bracketed sections [CRITICAL], [ANCHOR POINT]. References weight and attention windows. Technical, structured, no ambiguity.

**Core Outcome:** Final prompts that AI video generators can execute without hallucinating missing context.

**The Non-Negotiable:** Critical features (scars, wounds, distinctive marks) ALWAYS in first 25% of prompt. Never compile without all three agent inputs.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
|---|---|---|---|
| Prompt Compilation | Final executable AI video prompt | Showrunner Notes + Cinematographer Specs + Script Supervisor validation (all three required) | Structured prompt: [ID], [Technical Header], [Subject/Asset], [Action/State], [Environment/Lighting], [Temporal Constraint] + Build Notes |
| Prompt Audit | Review existing prompt for compliance | Draft prompt + Style Guide + Vocabulary | Compliance report: anchor points, vocabulary, exit hook, injections |
| Variable Interval Compilation | Compile prompt for 5s / 15s / 30s shard duration | All three agent inputs + target duration | Duration-appropriate prompt with scaled [Temporal Constraint] |

**Memory:** Reads Vocabulary.md. Does NOT read independently — compiles only from provided agent inputs.

**Activation Modes:** Interactive + headless within shard-generation.

---

### cpm-inception (Workflow)

**Type:** workflow

**Purpose:** Agentic onboarding for a new production. The Orchestrator guides an interview to gather the user's vision and generates a complete project foundation (Show Bible + Style Guide + initial character sketches) from conversational answers — no manual Markdown writing required.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
|---|---|---|---|
| Vision Interview | User's story vision captured in structured form | Conversational Q&A (genre, tone, themes, world, characters, visual vibe, first scene idea) | Structured vision brief |
| Foundation Generation | Complete Show Bible + Style Guide skeleton + Character sketches | Vision brief from interview | `Bible/Show_Bible.md`, `Architecture/Style_Guide.md`, initial `Bible/Characters/*.md` |
| Project Scaffold | Full directory structure created | Project name, model target, shard duration preference | Complete project folder + `.cpm/config.yaml` + `Production/Slate.md` |
| Inception Diagram | Excalidraw diagram of the project's planned production structure | Foundation outputs | `Diagrams/production-flow.excalidraw` |

**Design Notes:** The interview should feel conversational, not form-like. The Orchestrator asks open questions and extracts structured data from natural answers. This workflow combines what was previously 4 separate workflows (new-project + show-bible + style-guide + character-create) into one guided session. The outputs are "draft quality" — designed to be refined with the full individual workflows later. This is the "rapid start" path. Users who want full depth on any document can run the dedicated workflows after inception.

**Relationships:** Prerequisite to all production workflows. Usually run first. Can also run `cpm-new-project` + individual workflows instead for a more controlled setup.

---

### cpm-new-project (Workflow)

**Type:** workflow

**Purpose:** Scaffold a new CPM production project. Asks model target and shard duration preference. Generates directory structure, config, and the static methodology Excalidraw diagram.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
|---|---|---|---|
| Project Scaffolding | Complete directory structure | Project name, model target (sora/kling/runway/pika), default shard duration (5s/15s/30s) | Full project folder + `.cpm/config.yaml` + `Production/Slate.md` + empty Bible/Architecture/Production/Output structure |
| Methodology Diagram | Static Excalidraw showing the CPM Cinematics as Code pipeline | — | `Diagrams/cpm-methodology.excalidraw` |

---

### cpm-show-bible (Workflow)

**Type:** workflow

**Purpose:** Create the Show Bible (PRD equivalent). Comprehensive guided session producing the full narrative foundation. Deeper than Inception's draft — all sections fully developed.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
|---|---|---|---|
| Full Show Bible Creation | Complete Show Bible with all sections | Conversational input across 8 guided steps | `Bible/Show_Bible.md` |
| Bible Refinement | Update/expand existing Show Bible sections | Existing Bible + requested changes | Updated `Bible/Show_Bible.md` |

---

### cpm-style-guide (Workflow)

**Type:** workflow

**Purpose:** Define visual language. Lighting protocol, hex palette, lens vocabulary, spatial rules, prompt vocabulary (banned/required words).

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
|---|---|---|---|
| Full Style Guide Creation | Complete visual architecture document | Guided interview on visual philosophy | `Architecture/Style_Guide.md`, `Architecture/Palette.md`, `Architecture/Lens_Language.md`, `Architecture/Vocabulary.md` |

**Design Notes (V2 Fix A):** Step presenting [C]reate menu must hint the user to read Show Bible first — visual style should emerge from narrative themes.

---

### cpm-character-create (Workflow)

**Type:** workflow

**Purpose:** Create character state files with immutable features (LEFT/RIGHT specificity critical for AI continuity), mutable state tracking, inventory, and arc position.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
|---|---|---|---|
| Character Creation | Complete character state file | Guided interview: visual identity, distinguishing features, outfit, inventory, arc position | `Bible/Characters/{Name}.md` + updated `Bible/Characters/_index.md` |
| Character Update | Update mutable state post-scene | Scene completion notes | Updated character file with version history row |

**Design Notes (V2 Fix B):** Step-02 status option must clearly distinguish "creating new character" vs "updating existing character."

---

### cpm-scene-create (Workflow)

**Type:** workflow

**Purpose:** Create scene brief files with filmmaker-directed beats. Each beat defines what happens in each shard — prevents Showrunner from inventing beats during shard generation.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
|---|---|---|---|
| Scene Brief Creation | Complete scene brief with all beats defined | Scene concept, characters on-camera, setting, arc position, beat count | `Production/Scenes/Scene_{XX}/scene-brief.md` + entry state template + manifest update |

---

### cpm-shard-generation (Workflow)

**Type:** workflow

**Purpose:** The Four-Agent Ritual. The core production loop. Generates one continuity-safe AI video prompt per run. Hard-gated State-Diff Check. Now supports variable shard duration (5s/15s/30s).

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
|---|---|---|---|
| Shard Generation (Standard) | Single AI video prompt, continuity-validated | Scene brief + previous exit state + project config (auto-loaded via manifest) | `Output/Prompts/Scene_{XX}_Shard_{YY}_prompt.md` + `Production/Scenes/{XX}/state/shard_{YY}_exit_state.md` |
| Variable Interval Generation | Prompt scaled for 5s / 15s / 30s beat duration | Target duration from config + all standard inputs | Duration-appropriate prompt with scaled Temporal Constraint and choreographed action description |

**The Mandatory Sequence (7 steps):**
1. Context Loading (read manifest → load all required files)
2. Beat Extraction (read scene-brief → identify current beat)
3. Showrunner Review (thematic check + beat definition)
4. Cinematographer Specs (visual architecture)
5. Script Supervisor Validation (state-diff gate — HALT if FAILED)
6. Prompt Compilation (Prompt Engineer — all three inputs required)
7. State Update (write exit state + update manifest)

**Design Notes (V2 Variable Intervals):** The `default_shard_duration` from `.cpm/config.yaml` controls the default. Override per-shard possible. For 15s/30s shards, the Prompt Engineer uses `Variable Interval Compilation` capability with scaled choreography — more action, more camera movement, multiple micro-beats within the shard.

---

### cpm-handshake-test (Workflow)

**Type:** workflow

**Purpose:** Validate CPM continuity across shard boundaries. 3 consecutive passes = CPM VALIDATED for the project.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
|---|---|---|---|
| Handshake Test Run | Single continuity validation across two adjacent shards | Two adjacent shard exit states + their prompts | Test report: 5 criteria PASS/FAIL + overall status |
| Validation Suite | Run full 3-pass validation suite | Access to all shards in a scene | Validation report: 3-pass results + VALIDATED / NOT VALIDATED |

---

## Configuration

| Variable | Prompt | Default | Result Template | User Setting |
|---|---|---|---|---|
| `target_model` | "Which AI video model are you targeting? (sora / kling / runway / pika)" | `sora` | Stored in `.cpm/config.yaml` per project | Yes — set at project creation |
| `default_shard_duration` | "What is your default shard duration in seconds? (5 / 15 / 30)" | `5` | Stored in `.cpm/config.yaml` per project | Yes — set at project creation |

Note: Config is per-production-project, not per-user. Each `.cpm/config.yaml` is independent.

---

## External Dependencies

| Dependency | Skills | Notes |
|---|---|---|
| Excalidraw (import) | cpm-orchestrator, cpm-new-project, cpm-inception | CPM generates `.excalidraw` JSON files. User imports into Excalidraw.com or VS Code Excalidraw extension. No MCP required — pure JSON generation. |
| AI Video Platform (Sora/Kling/Runway/Pika) | — | External. CPM generates prompts formatted for the target model. Actual generation happens outside CPM. |

---

## UI and Visualization

**Two Excalidraw artifacts:**

1. **Static Methodology Diagram** (`Diagrams/cpm-methodology.excalidraw`) — Generated by `cpm-new-project`. Shows the full CPM Cinematics as Code pipeline from Story Brief to Rendered Video. Beautiful, shareable, explains the methodology. Includes: production phases, the Four-Agent Ritual flow, the SDLC→CPLC mapping table, the State-Diff Gate visual.

2. **Per-Project Living Diagram** (`Diagrams/production-flow.excalidraw`) — Generated/updated by `cpm-orchestrator`'s Production Diagram capability. Shows THIS project's structure: act breakdown, scene list with status indicators (not-started/in-progress/complete), character roster, shard completion counts. Updated as production progresses.

Both are `.excalidraw` JSON files — importable into any Excalidraw environment.

---

## Setup Extensions

The `cpm-setup` skill (generated by Create Module step) should:
1. Ask for `output_folder` preference for CPM projects (default: project root)
2. No special installation beyond config collection
3. Generate the static methodology diagram on first setup

---

## Integration

**Standalone module.** Provides complete independent value — no parent module required.

**Integration with BMAD Core:** The Orchestrator pattern mirrors BMAD Master. Users familiar with BMAD will immediately understand CPM's routing model. The CPLC maps 1:1 to BMAD's SDLC, making the methodology familiar.

**Cross-module potential (future):** CIS Storytelling workflow could feed directly into CPM's Show Bible creation. CIS Brainstorming session could generate the initial vision for Inception.

---

## Creative Use Cases

- **Music video production**: Style Guide defines the visual language of the track; each scene is a verse/chorus segment; shards are the beat-synced cuts
- **Game cinematics**: Characters have precise inventory tracking; narrative contracts manage foreshadowing across cutscenes
- **Documentary-style AI content**: Scene-create defines real interview segments; shard-generation maintains consistent speaker visual continuity
- **Serialized content (YouTube series)**: Show Bible tracks running story arcs across episodes; character state persists between episodes
- **Brand storytelling**: Style Guide encodes brand visual identity; CPM ensures every video asset is on-brand

---

## Ideas Captured

### From V1 — What We Know Works
- **"The Vibe-Drift Gap"** — AI video generators are stateless. CPM is the external memory.
- **4-Agent Ritual**: Showrunner → Cinematographer → Script Supervisor → Prompt Engineer. Maps directly to BMAD's PM→Architect→QA→Dev pattern.
- **Temporal Sharding**: Atomic beats with explicit entry contracts and exit states baked INTO prompts.
- **State-Diff Gate**: Hard gate. No exceptions. Proven in V1 as the critical continuity mechanism.
- **Vocabulary Enforcement**: Banned/required word lists prevent style drift. Hex codes always.
- **Narrative Contracts**: Plant → Maintain → Payoff lifecycle. Forward-looking validation.
- **Handshake Test**: 3 consecutive passes = CPM VALIDATED. Proven working in V1.
- **Fix C2 (Critical)**: Shard-generation must load scene-brief.md and extract {currentBeat}. Without this, Showrunner invents beats — tested and confirmed.

### V1 Pending Fixes (Apply in V2)
- Fix A: style-guide [C]reate menu — add Show Bible hint
- Fix B: character-create step-02 — status option clarity

### V2 Feature Ideas (Deferred for V3)
- VLM-QA Agent: Visual regression testing with vision LLM — closes the loop between prompt and output
- Cinematic Transpiler: Compile Universal Cinematic Language to any model format
- Exception-Based Review: Confidence scoring, auto-commit for 95%+
- Git Collaboration: Branching narratives for collaborative stories
- Thematic Skinning: Style Guide as swappable theme
- Low-Fi Animatic: Tier 3 staging with motion preview

---

## Build Roadmap

**Recommended order with rationale:**

1. ✅ **`cpm-orchestrator`** (agent) — BUILT. Output: `skills/cpm-orchestrator/`. Orson — The Film Director. Stateless router with 5 capabilities + pre-packaged methodology diagram asset.

2. **`cpm-showrunner`** (agent) ← **NEXT**. First specialist. Owns Show Bible, which all other workflows depend on. Building this second validates the SKILL.md agent pattern for domain specialists.

3. **`cpm-cinematographer`** (agent) — Second specialist. Owns Style Guide. Pairs with Showrunner to validate inter-agent handoff patterns.

4. **`cpm-script-supervisor`** (agent) — Third specialist. The hard gate. Build before Prompt Engineer so the validation contract is defined before the compiler is built.

5. **`cpm-prompt-engineer`** (agent) — Fourth specialist. The final output. Build last among agents because it depends on all three others.

6. **`cpm-new-project`** (workflow) — First workflow. Foundation scaffolding. Build early to have a clean project structure for testing subsequent workflows. Generates methodology Excalidraw.

7. **`cpm-show-bible`** (workflow) — Enables end-to-end testing of Showrunner agent + workflow interaction.

8. **`cpm-style-guide`** (workflow) — Apply Fix A here. Validates Cinematographer agent + workflow interaction.

9. **`cpm-character-create`** (workflow) — Apply Fix B here.

10. **`cpm-scene-create`** (workflow) — Critical. Without scene briefs, shard-generation cannot run (Fix C2 lesson from V1).

11. **`cpm-shard-generation`** (workflow) — The core loop. Build after all agents and preceding workflows are ready. Apply variable interval support here.

12. **`cpm-handshake-test`** (workflow) — Build after shard-generation. Can only be tested end-to-end.

13. **`cpm-inception`** (workflow) — Build last. It wraps new-project + show-bible + style-guide + character-create into one guided session. Build after all four individual workflows are stable.

**After all skills are built:** Return to **Create Module (CM)** to scaffold the module infrastructure and generate the `cpm-setup` skill.

**Next steps:**

1. ✅ `cpm-orchestrator` built — `skills/cpm-orchestrator/`
2. Build `cpm-showrunner` using **Build an Agent (BA)** — pass this plan document as context, spec under `### cpm-showrunner`
3. Continue down the roadmap, one skill at a time
4. When all 13 skills are built, run **Create Module (CM)** to scaffold the installable module

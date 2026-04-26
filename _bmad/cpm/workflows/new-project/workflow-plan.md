---
conversionFrom: '_bmad/cpm/workflows/new-project/workflow.md'
originalFormat: 'monolithic-markdown'
stepsCompleted: ['step-00-conversion', 'step-02-classification', 'step-03-requirements', 'step-04-tools', 'step-05-plan-review', 'step-06-design', 'step-07-foundation']
created: 2026-02-05
status: APPROVED_FOR_DESIGN
approvedDate: 2026-02-05
targetPath: '_bmad/cpm/workflows/new-project/'
---

# Workflow Creation Plan

## Conversion Source

**Original Path:** _bmad/cpm/workflows/new-project/workflow.md
**Original Format:** Monolithic single-file markdown (non-compliant)
**Detected Structure:** 211-line single file with:
- Frontmatter with config reference
- Role definition
- Initialization sequence (interactive)
- Scaffolding sequence (6 steps inline)
- Completion section
- Final menu

---

## Original Workflow Analysis

### Goal (from source)

Scaffold a complete CPM (Cinematic Production Manager) project with all directories, templates, and configuration files ready for production.

### Original Steps (Complete List)

**Initialization Phase:**
- **Get Project Title** - Ask user for project name
- **Get Project Location** - Ask where to create (default: current dir)
- **Get Target Model** - Which AI video generator (Wan 2.2, Sora, Kling, Runway)
- **Confirm Setup** - Show directory structure preview, get Y/N confirmation

**Scaffolding Phase:**
- **Step 1:** Create Directory Structure - All folders (.cpm, Bible, Architecture, Production, Output)
- **Step 2:** Generate config.yaml - Project config with model target and agent paths
- **Step 3:** Copy Agent Prompts - Copy 4 agent files from templates
- **Step 4:** Create manifest.md - Project manifest with status tracking
- **Step 5:** Create Placeholder Files - Show_Bible.md, Style_Guide.md, Palette.md, Vocabulary.md
- **Step 6:** Create Index Files - Character index, World index, Production Slate

**Completion Phase:**
- **Show Completion Message** - "Your CPM project is ready!"
- **Show Next Steps** - Guide to other CPM workflows
- **Present Menu** - Options to launch related workflows or quit

### Output / Deliverable

A fully scaffolded CPM project directory structure:
```
{project_name}/
├── .cpm/
│   ├── config.yaml (generated)
│   ├── manifest.md (generated)
│   └── agents/ (4 files copied from templates)
├── Bible/
│   ├── Show_Bible.md (placeholder)
│   ├── Characters/_index.md
│   └── World/_index.md
├── Architecture/
│   ├── Style_Guide.md (placeholder)
│   ├── Palette.md (placeholder)
│   ├── Lens_Language.md (placeholder)
│   └── Vocabulary.md (placeholder)
├── Production/
│   ├── Slate.md (generated)
│   ├── Scenes/
│   └── Contracts/
└── Output/
    ├── Prompts/
    └── Renders/
```

### Input Requirements

1. **Project Title** (required) - Name of the cinematic project
2. **Project Location** (optional, default: current directory) - Where to create
3. **Target AI Model** (required) - One of: Wan 2.2, Sora, Kling, Runway
4. **Confirmation** (required) - Y/N to proceed with scaffolding

### Key Instructions to LLM

- **Role:** "You are the Project Scaffolder"
- **Progressive Questioning:** Ask 1-2 questions at a time, wait for response
- **Recommendation Logic:** If user is unsure about model, recommend based on project type
- **Clear Structure Display:** Show directory tree before confirmation
- **Workflow Chaining:** Menu offers to launch related CPM workflows

---

## Conversion Notes

**What works well in original:**
- Progressive question flow (good UX)
- Clear directory structure visualization
- Helpful recommendations for model selection
- Workflow chaining menu at end
- Inline YAML/markdown templates are well-structured

**What needs improvement:**
- Monolithic structure makes editing/debugging difficult
- No state tracking if interrupted
- Templates embedded inline instead of external files
- No separation between interactive and execution phases

**User Feedback (Conversion):**
- Workflow is new (not yet used in production)
- No problems encountered yet
- No new features requested
- Same audience (CPM users creating cinematic projects)

**Compliance gaps identified:**
- Missing step-file architecture (no steps-c/ folder)
- Missing MANDATORY EXECUTION RULES blocks
- Missing STEP GOAL statements per step
- Missing SUCCESS/FAILURE metrics
- Missing stepsCompleted frontmatter tracking
- Missing data/ folder for reference content
- Missing templates/ folder for output templates
- No workflow-plan.md design document
- No JIT loading pattern

---

## BMAD Conversion Plan

### Final Step Structure:

```
new-project/
├── workflow.md                    # Entry point, role, routing
├── workflow-plan.md               # This file (design doc)
├── steps-c/
│   ├── step-01-gather-details.md  # Get title, location, model
│   ├── step-02-confirm-setup.md   # Show preview, get confirmation
│   ├── step-03-scaffold.md        # Execute all file operations
│   └── step-04-completion.md      # Show results, final menu
├── data/
│   └── directory-structure.md     # Reference for structure display
└── templates/
    ├── config.yaml.template       # Project config template
    ├── manifest.md.template       # Manifest template
    └── placeholder.md.template    # Generic placeholder template
```

### Step Breakdown:

**step-01-gather-details.md (~80 lines)**
- STEP GOAL: Collect project title, location, and target model
- Progressive questions (1-2 at a time)
- Model recommendation logic
- Menu: [C] Continue when all info gathered

**step-02-confirm-setup.md (~60 lines)**
- STEP GOAL: Display structure preview and get user confirmation
- Load directory-structure.md for display
- Show customized preview with user values
- Menu: [Y] Proceed / [N] Go back to details

**step-03-scaffold.md (~100 lines)**
- STEP GOAL: Execute all file and folder operations
- Create directories
- Generate files from templates
- Copy agent prompts
- No menu (auto-proceed on success)

**step-04-completion.md (~70 lines)**
- STEP GOAL: Confirm completion and offer next steps
- Show success message
- Display next recommended workflows
- Menu: [B] Show Bible / [S] Style Guide / [H] Character / [Q] Quit

---

## Classification Decisions

**Workflow Name:** new-project
**Target Path:** _bmad/cpm/workflows/new-project/

**4 Key Decisions:**
1. **Document Output:** false (action workflow - scaffolds files, doesn't build a document)
2. **Module Affiliation:** CPM (Cinematic Production Manager)
3. **Session Type:** single-session (quick scaffolding, 5-10 minutes)
4. **Lifecycle Support:** create-only (scaffolding tool, no edit/validate needed)

**Structure Implications:**
- Only needs `steps-c/` folder (no steps-e/ or steps-v/)
- No `step-01b-continue.md` needed (single-session)
- No `stepsCompleted` tracking in output (no persistent output document)
- Standard init step without continuation detection

---

## Requirements

**Flow Structure:**
- Pattern: Linear with one branch (Y/N confirmation)
- Phases: Gather Details → Confirm → Scaffold → Complete
- Estimated steps: 4 step files

**User Interaction:**
- Style: Guided session (AI leads through structured experience)
- Decision points: Model selection, Y/N confirmation, Final menu
- Checkpoint frequency: After gathering details, after scaffolding

**Inputs Required:**
- Required: Project title, target AI model (Wan 2.2/Sora/Kling/Runway), confirmation
- Optional: Project location (defaults to current directory)
- Prerequisites: CPM module installed

**Output Specifications:**
- Type: Action (scaffolds files/folders, not a document)
- Produces:
  - Directory structure (9 folders)
  - Generated files: config.yaml, manifest.md, Slate.md
  - Copied files: 4 agent prompts from templates
  - Placeholder files: Show_Bible.md, Style_Guide.md, Palette.md, Vocabulary.md, index files
- Frequency: Single execution per project

**Success Criteria:**
- All directories created successfully
- config.yaml generated with correct project name and model target
- Agent prompts copied from templates
- manifest.md initialized with project status checklist
- Placeholder files created with guidance comments
- User informed of next steps (which CPM workflows to run)

**Instruction Style:**
- Overall: Mixed
- Prescriptive: Model selection options, menu options, file operations
- Flexible: Recommendations based on project type, help with uncertain users

---

## Tools Configuration

**Core BMAD Tools:**
- **Party Mode:** Excluded - Not needed for scaffolding
- **Advanced Elicitation:** Excluded (FUTURE: Could add for deeper project vision exploration)
- **Brainstorming:** Excluded (FUTURE: Could integrate CIS-CPM for creative project ideation)

**LLM Features:**
- **Web-Browsing:** Excluded - No external research needed
- **File I/O:** Included - Core function (create folders, generate files, copy templates)
- **Sub-Agents:** Excluded - Too simple for delegation
- **Sub-Processes:** Excluded - Sequential operations

**Memory:**
- Type: Single-session
- Tracking: None (creates files, done)

**External Integrations:**
- None required

**Installation Requirements:**
- None - all features are built-in

**Future Enhancement Notes:**
- Consider adding Brainstorming (CIS-CPM integration) for creative project ideation in Phase 1
- Consider adding Advanced Elicitation for deeper exploration of project vision/goals
- These could help users who are unsure about their project direction

---

## Variable Definitions

```yaml
# From user input
project_name: '{user provides}'
project_location: '{user provides or default}'
model_target: '{user selects}'

# Computed
project_path: '{project_location}/{project_name}'
config_file: '{project_path}/.cpm/config.yaml'
manifest_file: '{project_path}/.cpm/manifest.md'

# From CPM config
agentTemplatesPath: '{project-root}/_bmad/cpm/templates/project/.cpm/agents'
```

---

## Detailed Design (Step 6)

### Step Specifications

| Step | Type | Lines | Menu Pattern |
|------|------|-------|--------------|
| step-01-gather-details | Init (non-continuable) | ~80 | C only |
| step-02-confirm-setup | Branch | ~70 | Y/N branching |
| step-03-scaffold | Action | ~120 | Auto-proceed |
| step-04-completion | Final | ~80 | Custom B/S/H/Q |

### Menu Patterns Used

- **step-01:** Pattern 2 (C only) - data gathering, no refinement
- **step-02:** Pattern 4 (Branching) - Y proceeds, N goes back to step-01
- **step-03:** Pattern 3 (Auto-proceed) - execute operations, no user choice
- **step-04:** Custom Final - workflow chaining options + quit

### Data Flow

```
User Input → step-01 → step-02 → step-03 → step-04
   ↓           ↓          ↓          ↓         ↓
 title      collect    confirm    execute   chain/quit
 location   & store    Y/N        files
 model
```

### Role Definition

- **Role:** Project Scaffolder
- **Expertise:** CPM project structure, AI video generators
- **Tone:** Helpful, efficient, encouraging
- **Style:** Guided, prescriptive for options, flexible for recommendations

### Subprocess Optimization

Not needed - simple sequential workflow with direct file operations.

---

## Foundation Build Complete (Step 7)

**Created:**
- Folder structure at: `_bmad/cpm/workflows/new-project/`
- `workflow.md` - BMAD entry point (replaced monolithic)
- `data/directory-structure.md` - Reference for preview display
- `templates/config.yaml.template` - Project config template
- `templates/manifest.md.template` - Manifest template
- `templates/placeholder.md.template` - Generic placeholder template

**Configuration:**
- Workflow name: new-project
- Continuable: No (single-session)
- Document output: No (action workflow)
- Mode: Create-only

**Next Steps:**
- ~~Build step-01-gather-details.md~~ ✅
- ~~Build step-02-confirm-setup.md~~ ✅
- ~~Build step-03-scaffold.md~~ ✅
- ~~Build step-04-completion.md~~ ✅

---

## Step Files Build Complete (Step 8-9)

**All step files created:**

| File | Type | Lines | Purpose |
|------|------|-------|---------|
| step-01-gather-details.md | Init (simple) | ~95 | Collect title, location, model |
| step-02-confirm-setup.md | Branch | ~85 | Preview structure, Y/N confirm |
| step-03-scaffold.md | Action | ~140 | Execute file operations |
| step-04-completion.md | Final | ~115 | Success + workflow chaining |

**Menu Patterns Applied:**
- step-01: C only (data gathering)
- step-02: Y/N branching (Y→step-03, N→step-01)
- step-03: Auto-proceed (no menu)
- step-04: Custom B/S/H/Q (workflow chaining)

---

## Conversion Complete

**Status:** COMPLETE

**Original:** 211-line monolithic workflow.md
**Converted:** BMAD-compliant step-file architecture

**Final Structure:**
```
new-project/
├── workflow.md                    ✅ BMAD entry point
├── workflow-plan.md               ✅ Design document
├── steps-c/
│   ├── step-01-gather-details.md  ✅
│   ├── step-02-confirm-setup.md   ✅
│   ├── step-03-scaffold.md        ✅
│   └── step-04-completion.md      ✅
├── data/
│   └── directory-structure.md     ✅
└── templates/
    ├── config.yaml.template       ✅
    ├── manifest.md.template       ✅
    └── placeholder.md.template    ✅
```

**Conversion Date:** 2026-02-05

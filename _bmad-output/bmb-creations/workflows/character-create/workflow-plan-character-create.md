---
conversionFrom: '_bmad/cpm/workflows/character-create/workflow.md'
originalFormat: 'monolithic-markdown'
stepsCompleted: ['step-00-conversion', 'step-02-classification', 'step-03-requirements', 'step-04-tools', 'step-05-plan-review', 'step-06-design', 'step-07-foundation', 'step-08-build-step-01']
created: 2026-02-16
approvedDate: 2026-02-16
status: APPROVED_FOR_DESIGN
---

# Workflow Creation Plan: character-create

## Conversion Source

**Original Path:** `_bmad/cpm/workflows/character-create/workflow.md`
**Original Format:** Monolithic Markdown (single-file, no step architecture)
**Detected Structure:** Procedural workflow with 8 sequential sections + compilation

---

## Original Workflow Analysis

### Goal (from source)

Create a complete character state file with:
- **Immutable visual identity** (face, body, distinguishing features) that persists across all shards
- **Mutable state** (outfit, inventory, physical condition) that changes per scene
- **Behavioral profile** for prompt engineering consistency
- **Arc position** for narrative tracking

**Core Purpose:** Build characters that AI video generators can render consistently by maintaining external state memory.

### Original Steps (Complete List)

**INITIALIZATION:**
- **Step 0:** Get character name from user
- **Step 0b:** Check if character already exists (route to Edit/View if yes)

**CREATION SEQUENCE:**
- **Step 1:** Basic Identity - Name, Asset ID (NAME_V1), Status (ACTIVE/DECEASED/FLASHBACK_ONLY)
- **Step 2:** Visual Identity (Immutable) - Face features, body type, posture, movement style
  - Critical: LEFT/RIGHT specificity for distinguishing features (scars, birthmarks)
  - Distinguishing features go in first 25% of every prompt
- **Step 3:** Current Outfit (Mutable) - Base clothing, condition, accessories
- **Step 4:** Inventory (Mutable) - Item tracking with status (EQUIPPED, HOLSTERED, POCKET, etc.)
- **Step 5:** Physical State (Mutable) - Injuries, conditions, severity tracking
- **Step 6:** Behavioral Profile - Speech pattern, nervous tic, signature move
- **Step 7:** Arc Position - Emotional state, want vs. need, arc progress (0-100%)

**COMPILATION:**
- **Step 8:** Create `Bible/Characters/{name}.md` with all sections
- **Step 9:** Update `Bible/Characters/_index.md` with new character entry

**COMPLETION:**
- Menu: Add Another / View / Edit / Quit

### Output / Deliverable

**Primary Output:**
- Character state file at `Bible/Characters/{name}.md` with structured markdown
- Contains 7 sections: Visual Identity, Current Outfit, Inventory, Physical State, Behavioral Profile, Arc Position, Version History

**Secondary Output:**
- Updated character index at `Bible/Characters/_index.md`

**File Format:** Structured markdown with YAML-like tables for inventory/physical state

### Input Requirements

**User Inputs:**
1. Character name
2. Visual identity details (face features, body type, distinguishing marks with LEFT/RIGHT specificity)
3. Current outfit description
4. Inventory items with status
5. Physical conditions/injuries
6. Behavioral traits (speech, tics, signature moves)
7. Arc position (emotional state, wants, needs, progress percentage)

**No file uploads** - all text-based conversational input

### Key Instructions to LLM

**Instruction Style:**
- **Procedural with prompts** - Each step asks specific questions
- **Form-filling pattern** - "What's this character's name?" / "Describe the character's PERMANENT visual features"
- **Explicit value constraints** - Status options (ACTIVE/DECEASED/FLASHBACK_ONLY), Inventory status (EQUIPPED_PRIMARY_HAND, etc.)
- **Critical guidance embedded** - "BE SPECIFIC about location: LEFT cheek, RIGHT eye" / "Distinguishing features go in the FIRST 25% of every prompt"

**LLM Role:** Information gatherer and compiler (not creative collaborator)

**Communication Style:** Direct questions → collect answers → compile into structured output

---

## Conversion Notes

### What works well in original:

1. **Immutable vs. Mutable Distinction** - Core CPM concept clearly separated (Visual Identity vs. Current Outfit/Inventory)
2. **LEFT/RIGHT Specificity Emphasis** - Repeatedly stresses location precision for continuity
3. **Structured Tables** - Inventory and Physical State use clear tabular format
4. **Version Tracking** - Asset ID system (NAME_V1) for character evolution
5. **Integration Context** - Explains how Showrunner/Script Supervisor/Prompt Engineer use this data

### What needs improvement:

1. **Form-Filling Pattern** - Questions are direct prompts, not collaborative exploration
   - Current: "What's this character's name?"
   - BMAD: Conversational discovery of character concept → formalize into structure
2. **No Session Resumption** - Cannot pause mid-creation and resume later
3. **Hardcoded Paths** - `Bible/Characters/{name}.md` lacks variable resolution
4. **No Collaborative Facilitation** - LLM acts as form processor, not character architect
5. **Edit Mode Not Separated** - Edit/View mentioned in menu but not implemented as modes
6. **No Validation Mode** - No automated checks for:
   - LEFT/RIGHT specificity present
   - No empty immutable fields
   - Inventory status values valid
   - Arc progress 0-100%

### Compliance gaps identified:

**Architecture:**
- ❌ No step-file architecture (monolithic single file)
- ❌ No tri-modal structure (Create/Edit/Validate)
- ❌ No state tracking (stepsCompleted frontmatter)
- ❌ No just-in-time loading (all instructions in one file)

**Frontmatter:**
- ❌ Missing required step frontmatter (name, description, file references)
- ❌ No {variable} format for paths
- ❌ No nextStepFile references

**Menu Handling:**
- ❌ Menu exists but no separate handler section
- ❌ No "halt and wait" enforcement
- ❌ Routes to Edit/View not implemented

**Templates:**
- ❌ Character structure hardcoded in workflow body
- ❌ Should extract to `templates/character.template.md`

**Data Files:**
- ❌ No reference materials:
  - Common distinguishing feature categories
  - Inventory status options reference
  - Arc position frameworks
  - Behavioral trait examples

**Instruction Style:**
- ⚠️ Form-filling instead of collaborative facilitation
- ⚠️ Should shift to: Explore → Discuss → Formalize → Review pattern

---

## CPM-Specific Context (from NEXT-STEPS.md)

**This is Workflow 1 of 6 CPM workflows being converted.**

### Core CPM Concept for This Workflow:

**Immutable vs. Mutable State** - The fundamental CPM continuity mechanism:
- **Immutable:** Face features, body type, distinguishing marks (scar on LEFT cheek) → NEVER change
- **Mutable:** Outfit, inventory items, physical condition (bleeding, exhaustion) → UPDATE every scene

**Why this matters:** AI video generators are stateless. External state files enforce continuity across shard boundaries. Character files are the primary state carriers.

### Critical Requirements:

1. **LEFT/RIGHT Specificity** - CPM's entire continuity thesis depends on precision
   - "scar on LEFT cheek" must never drift to RIGHT
   - Workflow must emphasize this HEAVILY in visual identity step

2. **Version Tracking** - Asset ID (NAME_V1, NAME_V2) tracks character evolution
   - Version history table must be preserved in output

3. **Script Supervisor Integration** - Generated files must be usable by Script Supervisor agent
   - File paths must align with agent expectations
   - Structure must match what agents parse

4. **Role: Character Architect** - Expert in building characters that AI can render consistently
   - Not a form-filler - a creative collaborator
   - Teaches users the immutable/mutable distinction

### Classification Guidance:

- **Document Output:** YES - Creates `Bible/Characters/{name}.md`
- **Module:** CPM
- **Session:** Continuable (character creation involves creative thought - may need breaks)
- **Lifecycle:** Tri-Modal (Create + Edit + Validate)
  - Edit mode essential - characters evolve through production
- **Instruction Style:** Intent-based collaborative (NOT form-filling)

### Expected Conversion Output:

**Structure:**
```
character-create/
├── workflow.md                    # Tri-modal router (Create/Edit/Validate)
├── workflow-plan-character-create.md  # This file
├── steps-c/                       # Create mode (8-9 steps)
│   ├── step-01-init.md           # Continuable init + resume logic
│   ├── step-01b-continue.md      # Session resume with routing
│   ├── step-02-basic-identity.md
│   ├── step-03-visual-identity.md # Immutable features (LEFT/RIGHT focus!)
│   ├── step-04-mutable-state.md   # Outfit, inventory, physical state
│   ├── step-05-behavioral-profile.md
│   ├── step-06-arc-position.md
│   ├── step-07-polish.md
│   └── step-08-final.md
├── steps-e/                       # Edit mode
│   └── step-e-01-assess.md       # Section-level editing
├── steps-v/                       # Validate mode
│   └── step-v-01-validate.md     # Automated consistency checks
├── data/
│   ├── distinguishing-features-reference.md  # Common feature categories
│   ├── inventory-status-options.md
│   └── arc-position-frameworks.md
└── templates/
    └── character.template.md      # Character sheet with stepsCompleted tracking
```

**Key Transformation:**
- **From:** "Fill in these fields" (form-filling)
- **To:** "Let's explore this character together" (collaborative facilitation using Explore → Discuss → Formalize → Review pattern)

---

## Reference Documents

**CPM Module Brief:** `_bmad-output/bmb-creations/modules/module-brief-cpm.md` (920 lines, comprehensive)
**Conversion Guidance:** `_bmad/cpm/NEXT-STEPS.md` (Workflow 1: Character Create section, lines 85-112)
**Similar Converted Workflows:**
- `_bmad/cpm/workflows/style-guide/` - Tri-modal, intent-based, continuable
- `_bmad/cpm/workflows/show-bible/` - Document output, collaborative

---

## Classification Decisions

**Workflow Name:** `character-create`
**Target Path:** `_bmad/cpm/workflows/character-create/`

**4 Key Decisions:**
1. **Document Output:** YES (creates `Bible/Characters/{name}.md`)
2. **Module Affiliation:** CPM (Cinematic Production Module)
3. **Session Type:** Continuable (creative work may need breaks)
4. **Lifecycle Support:** Tri-Modal (Create + Edit + Validate)

**Structure Implications:**
- Needs `steps-c/` with 8-9 create steps (init, visual identity, mutable state, behavioral, arc, polish, final)
- Needs `step-01b-continue.md` for session resumption (continuable workflow)
- Needs `steps-e/` for edit mode (characters evolve - essential for CPM)
- Needs `steps-v/` for validate mode (LEFT/RIGHT checks, field validation, arc progress 0-100%)
- Needs `templates/character.template.md` with `stepsCompleted` tracking
- Needs `data/` files (distinguishing-features-reference.md, inventory-status-options.md, arc-position-frameworks.md)
- Shared `data/` folder across all modes (prevents drift)

---

## Requirements

**Flow Structure:**
- Pattern: Linear with collaborative facilitation (Explore → Discuss → Formalize → Review)
- Phases: Init & Resume → Identity Foundation (Immutable) → Mutable State → Character Depth → Finalization
- Estimated steps: 8-9 create steps + 1 edit step + 1 validate step (10-11 files)
- Key transformation: Form-filling → Intent-based collaborative exploration

**User Interaction:**
- Style: Intent-Based Collaborative (NOT prescriptive form-filling)
- Role: Character Architect (expert collaborator teaching immutable/mutable distinction)
- Decision points: Visual identity separation, LEFT/RIGHT specificity, want vs. need
- Checkpoint frequency: After each major phase
- Mixed approach: Prescriptive for init/finalization, Intent-based for creative sections

**Inputs Required:**
- Required: Character name, visual identity (LEFT/RIGHT specificity), outfit, inventory, physical state, behavioral traits, arc position
- Optional: None (all sections needed)
- Prerequisites: Show Bible context, understanding of immutable/mutable concept

**Output Specifications:**
- Type: Document
- Format: Free-form with structured sections
- Primary output: `{project-root}/Bible/Characters/{name}.md` (7 sections + version history)
- Secondary output: Updated `{project-root}/Bible/Characters/_index.md`
- Pattern: Direct-to-Final (each step appends sections)
- Frontmatter: Tracks stepsCompleted for continuable workflow

**Success Criteria:**
- Character file created with all 7 sections complete
- Immutable/mutable clearly separated
- LEFT/RIGHT specificity present for distinguishing features
- No empty immutable fields
- Inventory status values valid
- Arc progress 0-100%
- Version tracking initialized (NAME_V1)
- Character index updated
- File usable by Script Supervisor and Prompt Engineer agents

**Instruction Style:**
- Overall: Intent-Based (facilitates creative exploration, not form-filling)
- Mixed approach:
  - Prescriptive: Init (step-01), Finalization (step-07-08)
  - Intent-based: Identity (step-02-03), Mutable State (step-04), Depth (step-05-06)
- Rationale: CPM philosophy "Humans provide soul" - workflow teaches and facilitates, doesn't just collect data

---

## Tools Configuration

**Core BMAD Tools:**
- **Party Mode:** ✅ INCLUDED - Integration points: Phase 2 (Visual Identity creative exploration), Phase 4 (Behavioral Profile multi-persona brainstorming)
- **Advanced Elicitation:** ✅ INCLUDED - Integration points: Phase 2 (LEFT/RIGHT specificity quality gate), Phase 5 (Polish - immutable/mutable validation)
- **Brainstorming:** ❌ EXCLUDED - Redundant with Party Mode

**LLM Features:**
- **Web-Browsing:** ❌ EXCLUDED - Character creation is imaginative work, no real-time data needed
- **File I/O:** ✅ INCLUDED - Operations: Read Show Bible for context, read existing character file (resume), write character file, update character index
- **Sub-Agents:** ❌ EXCLUDED - Linear facilitation workflow, no task delegation needed
- **Sub-Processes:** ❌ EXCLUDED - Conversational workflow, no parallel processing needed

**Memory:**
- Type: Continuable (multi-session support)
- Tracking: stepsCompleted array, lastStep, step-01b-continue.md for resumption
- Rationale: Creative work may need breaks

**External Integrations:**
- None required - Self-contained CPM workflow

**Installation Requirements:**
- ✅ NO INSTALLATION NEEDED - All selected tools are built-in (Party Mode, Advanced Elicitation, File I/O)

**File I/O Details:**
- **Read operations:**
  - `{project-root}/Bible/Show_Bible.md` - World context for character creation
  - `{project-root}/Bible/Characters/{name}.md` - Existing character file (if resuming)
  - `{project-root}/Bible/Characters/_index.md` - Character index
- **Write operations:**
  - `{project-root}/Bible/Characters/{name}.md` - New character state file
  - `{project-root}/Bible/Characters/_index.md` - Updated index with new character

---

## Workflow Design

### File Structure (15 files total)

```
character-create/
├── workflow.md                    # Tri-modal router
├── workflow-plan-character-create.md
├── steps-c/ (9 files)
│   ├── step-01-init.md
│   ├── step-01b-continue.md
│   ├── step-02-basic-identity.md
│   ├── step-03-visual-identity.md
│   ├── step-04-mutable-state.md
│   ├── step-05-behavioral-profile.md
│   ├── step-06-arc-position.md
│   ├── step-07-polish.md
│   └── step-08-final.md
├── steps-e/ (1 file)
│   └── step-e-01-assess.md
├── steps-v/ (1 file)
│   └── step-v-01-validate.md
├── data/ (3 files)
│   ├── distinguishing-features-reference.md
│   ├── inventory-status-options.md
│   └── arc-position-frameworks.md
└── templates/ (1 file)
    └── character.template.md
```

### Create Mode Step Sequence (9 steps)

**step-01-init** (Continuable Init)
- Goal: Initialize character creation or detect existing character
- Menu: Auto-proceed
- Actions: Get name, check existence, create from template OR route to continue
- File I/O: Read Show Bible, check character file

**step-01b-continue** (Resumption Router)
- Goal: Resume interrupted character creation
- Actions: Read stepsCompleted, identify last step, route to next

**step-02-basic-identity** (Simple)
- Goal: Establish character foundation
- Menu: C only
- Actions: Name, Asset ID (NAME_V1), Status (ACTIVE/DECEASED/FLASHBACK_ONLY)

**step-03-visual-identity** (Standard A/P/C)
- Goal: Define immutable features with LEFT/RIGHT specificity
- Menu: A/P/C (Advanced Elicitation for LEFT/RIGHT quality gate, Party Mode for creative exploration)
- Actions: Face features, body type, posture, movement (Explore → Discuss → Formalize)
- Data: distinguishing-features-reference.md

**step-04-mutable-state** (Standard A/P/C)
- Goal: Define changeable state
- Menu: A/P/C (Party Mode for creative inventory)
- Actions: Current outfit, inventory with status codes, physical state
- Data: inventory-status-options.md

**step-05-behavioral-profile** (Standard A/P/C)
- Goal: Define character behaviors for Prompt Engineer
- Menu: A/P/C (Party Mode for quirks brainstorming)
- Actions: Speech pattern, nervous tic, signature move

**step-06-arc-position** (Standard A/P/C)
- Goal: Define character journey and transformation
- Menu: A/P/C
- Actions: Emotional state, want vs. need, arc progress 0-100%
- Data: arc-position-frameworks.md

**step-07-polish** (Standard A/P/C)
- Goal: Cross-section consistency check
- Menu: A/P/C (Advanced Elicitation for deep quality validation)
- Actions: Review immutable/mutable separation, LEFT/RIGHT specificity, field validation

**step-08-final** (Final)
- Goal: Compile output and update index
- Menu: Custom (Add Another / Edit / Validate / Quit)
- Actions: Add version history, save character file, update index
- File I/O: Write character file, update index

### Edit Mode Step Sequence (1 step)

**step-e-01-assess** (Edit Assessment)
- Goal: Section-level character editing
- Menu: Custom (Edit Section / Validate / Quit)
- Actions: Load character, display state, select section to edit, update file, version tracking

### Validate Mode Step Sequence (1 step)

**step-v-01-validate** (Validation Sequence)
- Goal: Automated consistency checks
- Menu: Auto-proceed then Custom (Fix / Quit)
- Checks: LEFT/RIGHT specificity, no empty immutable fields, valid inventory status, arc progress 0-100%, Asset ID format, version history present

### Interaction Patterns

- **Intent-Based Collaborative:** Steps 03-07 use Explore → Discuss → Formalize → Review pattern
- **Prescriptive:** Steps 01-02, 08 (straightforward init/finalization)
- **Party Mode Integration:** Steps 03, 04, 05 (creative exploration)
- **Advanced Elicitation Integration:** Steps 03, 07 (quality gates)

### State Tracking

- **stepsCompleted array:** Tracks progress in character file frontmatter
- **Continuable:** step-01b-continue routes based on stepsCompleted
- **Version Tracking:** Asset ID (NAME_V1, V2, etc.), version history table

### Role & Persona

**Character Architect** - Expert in building characters that AI can render consistently
- Collaborative facilitator (not form-filler)
- Teaches immutable vs. mutable distinction
- Emphasizes LEFT/RIGHT precision
- Guides creative exploration into structured state

### Cross-Mode Integration

- Create → Validate (offer at step-08-final)
- Edit → Validate (offer after editing)
- Validate → Edit (offer to fix issues)

---

## Foundation Build Complete

**Created:**
- ✅ Folder structure at: `_bmad/cpm/workflows/character-create/`
  - `steps-c/` (Create mode steps)
  - `steps-e/` (Edit mode steps)
  - `steps-v/` (Validate mode steps)
  - `data/` (Shared reference materials)
  - `templates/` (Output templates)
- ✅ `workflow.md` (Tri-modal router with mode detection)
- ✅ `templates/character.template.md` (Free-form template with stepsCompleted tracking)

**Configuration:**
- Workflow name: `character-create`
- Continuable: YES (multi-session support)
- Document output: YES (Free-form with structured sections)
- Mode: Tri-Modal (Create/Edit/Validate)
- Role: Character Architect

**Foundation Files:**
- `workflow.md` (68 lines) - Mode routing logic for Create/Edit/Validate
- `templates/character.template.md` - Output template with 7 sections + version history

---

## Step-01 Build Complete

**Created:**
- ✅ `steps-c/step-01-init.md` (200 lines)
  - Continuable init with existence check
  - Routes to step-01b-continue if resuming
  - Creates character file from template
  - Initializes stepsCompleted tracking
  - Auto-proceeds to step-02

- ✅ `steps-c/step-01b-continue.md` (156 lines)
  - Reads stepsCompleted array
  - Routing table for all steps (step-02 through step-08)
  - Progress summary display
  - Auto-proceeds to appropriate next step

**Key Features:**
- Continuation detection (checks for existing character file)
- stepsCompleted array tracking
- Show Bible context loading (if available)
- Character index awareness
- Proper routing: New → step-02, Resume → step-01b → correct next step

---

## Next Steps

1. ~~Classification (step-02)~~ ✅
2. ~~Requirements gathering (step-03)~~ ✅
3. ~~Tool/workflow selection (step-04)~~ ✅
4. ~~Plan review (step-05)~~ ✅
5. ~~Design (step-06)~~ ✅
6. ~~Foundation (step-07)~~ ✅
7. ~~Build step-01 & step-01b (step-08)~~ ✅
8. Build remaining steps (step-09 - repeatable) ← NEXT
   - step-02 through step-08 (7 create steps)
   - step-e-01 (1 edit step)
   - step-v-01 (1 validate step)
9. Confirmation (step-10)

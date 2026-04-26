---
conversionFrom: '_bmad/cpm/workflows/style-guide/workflow.md'
originalFormat: 'monolithic single-file markdown'
stepsCompleted: ['step-00-conversion', 'step-02-classification', 'step-03-requirements', 'step-04-tools', 'step-05-plan-review', 'step-06-design', 'step-07-foundation', 'step-08-build-step-01', 'step-09-build-all-steps']
created: 2026-02-06
status: CONFIRMED
confirmationDate: 2026-02-06
confirmationType: conversion
coverageStatus: complete
approvedDate: 2026-02-06
---

# Workflow Creation Plan

## Conversion Source

**Original Path:** _bmad/cpm/workflows/style-guide/workflow.md
**Original Format:** Monolithic single-file markdown (200 lines, no step-file architecture)
**Detected Structure:** 6 inline creation steps + initialization + compilation + completion + disconnected menu
**Validation Report:** _bmad/cpm/workflows/style-guide/validation-report-2026-02-06.md

---

## Original Workflow Analysis

### Goal (from source)

Create a Cinematic Style Guide — the visual architecture that the Cinematographer agent enforces. Defines lighting, color, camera language, and the vocabulary rules for prompts.

### Original Steps (Complete List)

**Initialization:** Check for existing Style_Guide.md — offer Edit or Start Fresh
**Step 1:** Visual Identity Statement - One-paragraph visual philosophy description
**Step 2:** Lighting Protocol - Primary style, hex-coded light sources table, lighting rules checklist
**Step 3:** Color Palette - Allowed colors with hex, forbidden colors, color emotional meanings
**Step 4:** Camera Language - Lens choices table, shot progressions, camera movement rules
**Step 5:** Spatial Rules - Axis of action, composition rules, negative space meaning
**Step 6:** Prompt Vocabulary - Required word substitutions table, banned words table
**Compilation:** Creates Architecture/Style_Guide.md + 3 supporting files (Palette, Lens_Language, Vocabulary)
**Completion:** Summary of created files + next step suggestions
**Menu:** [R]eview, [E]dit, [P]alette, [V]ocabulary, [C]haracter, [Q]uit (disconnected from flow)

### Output / Deliverable

4 documents:
1. `Architecture/Style_Guide.md` — Main comprehensive style guide (all sections)
2. `Architecture/Palette.md` — Color definitions extracted
3. `Architecture/Lens_Language.md` — Camera specifications extracted
4. `Architecture/Vocabulary.md` — Banned/required word lists

### Input Requirements

- User's visual philosophy / artistic vision
- Lighting preferences with specific hex color codes
- Color palette choices (allowed + forbidden)
- Camera lens and movement preferences
- Composition and spatial rules
- Prompt vocabulary rules (substitutions + banned words)

### Key Instructions to LLM

- Role: "Visual Architect" — translating creative vision into enforceable visual rules
- Style: Prescriptive/form-filling (tables with blanks to fill)
- Approach: Presents table templates and expects user to fill them in
- No collaborative facilitation language
- No progressive questioning
- Domain knowledge is excellent but delivery is mechanical

---

## Conversion Notes

**What works well in original:**
- Strong domain expertise — covers all essential aspects of a cinematic style guide
- Excellent example content (Edward Hopper cyberpunk dystopia reference)
- Clear 4-document output structure with logical separation of concerns
- Good use of hex codes for precise color specification
- Lighting rules checklist concept (checkboxes for Cinematographer agent)
- Vocabulary substitution table concept (enforcing precise language)
- Initialization check for existing Style Guide

**What needs improvement:**
- All 6 steps inline in one file — no step-file architecture
- Form-filling approach instead of collaborative facilitation
- Steps 2-6 dump entire table structures at once — overwhelming
- No progressive questioning (1-2 questions at a time)
- No user review/refinement between sections
- Menu is disconnected from creation flow
- No state tracking or session resume capability
- No templates for output documents
- Hardcoded output paths (Architecture/) instead of {variable} format

**Compliance gaps identified:**
- No step-file architecture (steps-c/, steps-e/, steps-v/)
- No frontmatter on steps (name, description, file references)
- No MANDATORY EXECUTION RULES per step
- No STEP GOAL sections
- No SUCCESS/FAILURE METRICS
- No menus with handlers per step (A/P/C pattern)
- No templates/ folder
- No data/ folder
- No workflow-plan.md
- No {variable} format for paths
- No output_folder configuration
- No stepsCompleted tracking

---

## Discovery (from CPM Module Brief Analysis)

### What Works Well to Preserve
- Domain content maps directly to CPM Architecture/ folder (Deliverable 2.3 in module brief)
- The 4-document output (Style_Guide.md, Palette.md, Lens_Language.md, Vocabulary.md) is exactly what the Cinematographer agent consumes in the Shard Generation Ritual
- Hex code precision, lens mm values, lighting protocols match Cinematographer agent's output format
- Vocabulary enforcement (banned/required) feeds directly into Prompt Engineer's compilation rules
- Example content quality is high — Edward Hopper cyberpunk reference sets the right creative tone

### Problems to Fix
- Form-filling contradicts CPM's core philosophy: "Humans provide soul" + "Automating the Boredom" — style guide creation must be collaborative exploration, not template completion
- No integration with existing CPM project state (config.yaml, Show Bible thematic pillars)
- No awareness that these rules will be enforced by the Cinematographer agent during Shard Generation
- User is "crew of 1" (Studio-in-a-Box) — needs the workflow to act as a knowledgeable cinematographer collaborator, not a form to fill

### Missing Features to Add
- Load existing Show_Bible.md if available — thematic pillars and motifs should inform visual identity decisions
- Reference target AI model from config.yaml — different models (sora, kling, runway) have different prompt vocabulary strengths
- Session resume support — style guide creation is iterative; users will return to refine
- Consistency validation between sections (color meanings vs lighting protocol, vocabulary vs palette)
- Preview/test concept — show user how their rules would translate to a sample shard prompt
- Integration with Cinematographer agent format — output should be directly consumable

### Audience
- Same: the "Studio-in-a-Box" creator — one person with creative vision
- May not be technical — needs collaborative guidance to translate "feel" into enforceable technical specs
- The workflow IS their cinematographer collaborator until they start production

---

## Classification Decisions

**Workflow Name:** style-guide
**Target Path:** _bmad/cpm/workflows/style-guide/

**4 Key Decisions:**
1. **Document Output:** true — Produces 4 persistent Architecture/ documents consumed by the Cinematographer agent in every Shard Generation Ritual
2. **Module Affiliation:** CPM (Cinematic Production Module) — Core CPM infrastructure creating the Architecture/ folder contents
3. **Session Type:** Continuable — 6+ substantive creative sections requiring thought (hex codes, lens language, vocabulary rules); iterative refinement expected as production reveals what works
4. **Lifecycle Support:** Tri-Modal (Create + Edit + Validate)
   - **Create:** Build style guide from scratch through collaborative facilitation
   - **Edit:** Modify existing style guide sections (essential — style evolves with production)
   - **Validate:** Check internal consistency (hex format, palette vs vocabulary conflicts, rule coherence) before Cinematographer agent enforcement

**Structure Implications:**
- Needs `steps-c/` folder with 7-9 step files (init + 6 content + polish + final)
- Needs `step-01b-continue.md` for session resume with stepsCompleted tracking
- Needs `steps-e/` folder for editing individual sections of existing style guide
- Needs `steps-v/` folder for consistency validation
- Needs `data/` folder for reference content (lighting patterns, lens reference, color theory)
- Needs `templates/` folder for output document templates (Style_Guide, Palette, Lens_Language, Vocabulary)
- Output uses free-form template with progressive append
- Must integrate with CPM config.yaml for project_name, model target, output paths
- Must check for existing Show_Bible.md to inform visual identity decisions

---

## Requirements

**Flow Structure:**
- Pattern: Linear with progressive build (Direct-to-Final)
- Most similar to: Example 1 (Meal Plan) + Example 9 (Life Review) — creative facilitation that builds a document section by section
- Phases:
  1. **Context Loading** — Init, load CPM config, check for existing Style Guide, load Show Bible if available
  2. **Visual Identity** — Creative exploration of the overall visual philosophy
  3. **Lighting & Color** — Define lighting protocol with hex codes, then color palette (these inform each other)
  4. **Camera & Composition** — Lens vocabulary, shot progressions, spatial rules
  5. **Vocabulary** — Banned/required words for prompt engineering
  6. **Polish & Compile** — Review whole guide for coherence, generate supporting documents
- Estimated steps: 10 for create mode (init + 01b-continue + 6 content + polish + final)
- No branching needed — linear progression through creative domains
- Each step builds on previous (lighting informs color, color informs vocabulary)

**User Interaction:**
- Style: Highly Collaborative — this is a creative workflow where the user expresses their visual vision
- The AI acts as a knowledgeable cinematographer collaborator (like working with an experienced DP)
- Decision points at every step — user defines their aesthetic choices
- Progressive questioning: start with "feel" and mood, then translate to technical specs
- Key principle: Tables are the OUTPUT format, not the INPUT method
  - Instead of "Fill in this table" → "What lighting inspires you? Let me help translate that into enforceable rules"
  - Instead of "Enter hex codes" → "Describe the colors that define your world. I'll help find the exact hex codes"
- Checkpoint frequency: Menu at every step (A/P/C pattern) — user can refine before proceeding

**Inputs Required:**
- Required:
  - User's creative vision / visual philosophy (gathered through conversation)
- Optional (auto-loaded if available):
  - `Bible/Show_Bible.md` — Thematic pillars, motifs, and color motifs inform visual identity
  - `.cpm/config.yaml` — project_name, target AI model (affects vocabulary), output paths
  - Reference films or visual inspirations (user provides verbally)
- Prerequisites:
  - CPM project should be initialized (config.yaml exists)
  - If Show Bible exists, it enriches the style guide creation significantly

**Output Specifications:**
- Type: Document (4 persistent files)
- Pattern: Direct-to-Final — each step appends to Style_Guide.md progressively
- Format: Structured — required sections from CPM Deliverable 2.3 template, flexible content within each
- Primary output: `Architecture/Style_Guide.md` (all sections)
- Derived outputs (generated at polish/compile step by extracting from main):
  - `Architecture/Palette.md` — Color definitions extracted
  - `Architecture/Lens_Language.md` — Camera specs extracted
  - `Architecture/Vocabulary.md` — Banned/required words extracted
- Template: Structured with required sections matching Cinematographer agent's consumption format:
  - Visual Identity Statement
  - Lighting Protocol (style, sources table with hex, rules checklist)
  - Color Palette (allowed table, forbidden table, color meanings)
  - Camera Language (lens vocabulary table, shot progressions, movement rules)
  - Spatial Rules (axis of action, composition)
  - Prompt Vocabulary (required substitutions table, banned words table)
- Final polish step: YES — review for coherence, ensure lighting rules don't contradict color palette, vocabulary is consistent
- Frontmatter: stepsCompleted tracking for session resume

**Success Criteria:**
- All 6 sections of the Style Guide are complete and internally consistent
- Hex codes are valid format (#RRGGBB)
- Color palette and lighting protocol use the same hex values (no drift)
- Vocabulary banned words don't appear in other sections as required terms
- Camera language lens choices have clear emotional justifications
- Cinematographer agent can consume and enforce the rules without ambiguity
- User feels their creative vision is accurately captured in technical form
- Supporting documents (Palette, Lens_Language, Vocabulary) are consistent with main Style Guide
- Style Guide connects to Show Bible thematic pillars (if Bible exists)

**Instruction Style:**
- Overall: Intent-based with domain expertise
- The AI should guide through open-ended creative exploration first, then help formalize into structured output
- Per-step guidance:
  - Visual Identity: Fully intent-based — "Describe the feeling every frame should communicate"
  - Lighting: Intent-based exploration → formalized into hex codes and rules — "What mood should your lighting create? Let me suggest specific techniques..."
  - Color: Intent-based → formalized — "What colors define your world? What colors would break it?"
  - Camera: Mixed — some technical knowledge needed, AI provides cinematography expertise — "For intimate moments, I'd suggest an 85mm lens because..."
  - Spatial: Intent-based with examples — "How should your characters relate to the frame?"
  - Vocabulary: Collaborative — "What words are too vague for your vision? What should replace them?"
- Key pattern: Explore → Discuss → Formalize → Review at each step
- Domain expertise is offered as suggestions, not prescriptions: "In noir cinematography, 60%+ shadow coverage creates tension. Does that match your vision?"

---

## Tools Configuration

**Core BMAD Tools:**
- **Party Mode:** INCLUDED — Integration points: Visual Identity (Phase 2) and Lighting Protocol (Phase 3). Multiple AI cinematographer personas (noir DP, naturalistic DP, experimental DP) explore visual philosophy with user. Powerful for "What would a Kubrick approach look like vs a Wong Kar-wai approach?"
- **Advanced Elicitation:** INCLUDED — Integration point: Available at every step via A menu option. Deep-probes user's aesthetic choices: "Why this color?", "What emotional truth does this lighting serve?", "How does this lens choice connect to your thematic pillars?"
- **Brainstorming:** EXCLUDED — The workflow itself IS facilitated creative exploration. Adding a separate brainstorming tool would be redundant.

**LLM Features:**
- **Web-Browsing:** EXCLUDED — Creative vision comes from the user, not external research. Reference films/images are discussed verbally.
- **File I/O:** INCLUDED (Essential) — Must read: `.cpm/config.yaml` (project name, target model), `Bible/Show_Bible.md` (thematic context). Must write: `Architecture/Style_Guide.md`, `Architecture/Palette.md`, `Architecture/Lens_Language.md`, `Architecture/Vocabulary.md`
- **Sub-Agents:** EXCLUDED — Single-agent collaborative workflow (Visual Architect persona). No need for parallel expertise.
- **Sub-Processes:** EXCLUDED — Linear creative workflow with no parallelism needed.

**Memory:**
- Type: Continuable
- Tracking: `stepsCompleted` array in output file frontmatter, `lastStep`, `lastContinued`
- Resume: `step-01b-continue.md` reads stepsCompleted from output file, routes to appropriate step
- Sidecar file: Not needed — stepsCompleted tracking in output file handles session state

**External Integrations:**
- None required

**Installation Requirements:**
- None — all tools are built-in BMAD core or standard file I/O

## Workflow Structure Preview

```
style-guide/
├── workflow.md                    # Router: mode detection, config loading, routing
├── workflow-plan-style-guide.md   # This plan document
├── steps-c/                       # Create mode (9 steps + 01b)
│   ├── step-01-init.md           # Load config, check existing, create output, load Bible context
│   ├── step-01b-continue.md      # Session resume — read stepsCompleted, route to next
│   ├── step-02-visual-identity.md # Collaborative visual philosophy exploration
│   ├── step-03-lighting.md       # Lighting style, hex sources, rules (Party Mode fits here)
│   ├── step-04-color-palette.md  # Allowed/forbidden colors, hex codes, meanings
│   ├── step-05-camera-language.md # Lens vocabulary, shot progressions, movement rules
│   ├── step-06-spatial-rules.md  # Axis of action, composition, negative space
│   ├── step-07-vocabulary.md     # Required substitutions, banned words
│   ├── step-08-polish.md         # Review entire guide, coherence check, generate supporting docs
│   └── step-09-final.md          # Summary, suggest next CPM workflows
├── steps-e/                       # Edit mode
│   └── step-e-01-assess.md       # Load existing guide, identify section to edit, apply changes
├── steps-v/                       # Validate mode
│   └── step-v-01-validate.md     # Consistency checks: hex format, palette vs vocabulary, rule coherence
├── data/                          # Reference content
│   ├── lighting-reference.md     # Common lighting styles, examples, hex suggestions
│   ├── lens-reference.md         # Standard lens choices, emotional effects, common mm values
│   └── color-theory-reference.md # Color relationships, common palettes, hex code patterns
└── templates/
    ├── style-guide.template.md   # Structured template matching Cinematographer agent format
    ├── palette.template.md       # Color definitions template
    ├── lens-language.template.md # Camera specs template
    └── vocabulary.template.md    # Banned/required words template
```

---

## Design

### Role & Persona

**Role:** Visual Architect — translating creative vision into enforceable visual rules
**Expertise:** Lighting design, color theory, camera language, composition, prompt engineering for AI video
**Communication:** Warm, creative, collaborative. Offers cinematographic expertise as suggestions, not prescriptions. Uses film references to make technical concepts accessible. Makes the user feel like they're working with an experienced Director of Photography.
**Interaction Pattern per step:** Explore (open questions) → Discuss (share expertise, offer suggestions) → Formalize (build the structured section) → Review (A/P/C menu)

### Step-by-Step Design: Create Mode (steps-c/)

#### step-01-init.md — Init (Continuable)
- **Type:** Init (Continuable)
- **Goal:** Load CPM config, check for existing Style Guide, load Show Bible context, create output from template
- **Menu:** Auto-proceed (Pattern 3) — no A/P for init
- **Frontmatter vars:** `outputFile`, `templateFile`, `continueFile`, `configFile`, `showBibleFile`
- **Logic:**
  1. Load `.cpm/config.yaml` — extract project_name, target model
  2. Check if `Architecture/Style_Guide.md` exists with `stepsCompleted` → if yes, load `{continueFile}`
  3. If no existing guide → create from `{templateFile}`
  4. Check if `Bible/Show_Bible.md` exists → if yes, extract thematic pillars, color motifs, genre/tone for context
  5. Welcome user, share context loaded, auto-proceed to step-02
- **Output:** Creates Style_Guide.md from template with empty frontmatter

#### step-01b-continue.md — Continuation
- **Type:** Continuation (01b)
- **Goal:** Resume workflow from last session
- **Menu:** Auto-proceed — routes to appropriate step
- **Logic:**
  1. Read `stepsCompleted` from Style_Guide.md frontmatter
  2. Determine last completed step, find its nextStepFile
  3. Welcome user back with context summary
  4. Route to next uncompleted step

#### step-02-visual-identity.md — Middle (Standard)
- **Type:** Middle (Standard) with A/P/C
- **Goal:** Collaboratively explore the user's visual philosophy and formalize into a Visual Identity Statement
- **Frontmatter vars:** `nextStepFile`, `outputFile`, `advancedElicitationTask`, `partyModeWorkflow`
- **Approach:**
  1. If Show Bible context was loaded, reference thematic pillars: "Your story explores [themes]. How should the visual language reflect that?"
  2. Open exploration: "Describe the feeling every frame should communicate"
  3. Offer film references as anchors: "Is your world closer to Blade Runner's neon noir or The Revenant's natural light?"
  4. Help formalize into a concise Visual Identity Statement paragraph
  5. Present draft for review
- **Menu:** A/P/C — Party Mode valuable here (multiple DP personas exploring different visual philosophies)
- **Output:** Appends `## Visual Identity Statement` to Style_Guide.md

#### step-03-lighting.md — Middle (Standard)
- **Type:** Middle (Standard) with A/P/C
- **Goal:** Define lighting protocol — primary style, hex-coded light sources, rules checklist
- **Frontmatter vars:** `nextStepFile`, `outputFile`, `lightingReference`, `advancedElicitationTask`, `partyModeWorkflow`
- **Data:** Load `data/lighting-reference.md` for common styles and hex suggestions
- **Approach:**
  1. Reference Visual Identity: "You described [their philosophy]. Let's build the lighting rules that enforce it."
  2. Explore lighting mood: "What mood should your lighting create? High contrast? Soft? Volumetric?"
  3. Suggest named styles (Chiaroscuro, High-Key, Neon-Noir) with examples
  4. Guide to specific hex codes: "For that electric purple rim light, #FF00FF is a strong choice. Want to explore variations?"
  5. Build light sources table through conversation (not form-filling)
  6. Formalize lighting rules checklist: "What should NEVER happen with lighting? What MUST always be present?"
- **Menu:** A/P/C — Party Mode great (different DPs argue lighting approaches)
- **Output:** Appends `## Lighting Protocol` to Style_Guide.md (style + sources table + rules checklist)

#### step-04-color-palette.md — Middle (Standard)
- **Type:** Middle (Standard) with A/P/C
- **Goal:** Define allowed/forbidden colors with hex codes and emotional meanings
- **Frontmatter vars:** `nextStepFile`, `outputFile`, `colorReference`, `advancedElicitationTask`, `partyModeWorkflow`
- **Data:** Load `data/color-theory-reference.md` for color relationships
- **Approach:**
  1. Connect to lighting: "Your lighting uses [hex codes from step 3]. Let's build the full palette around that."
  2. Explore: "What colors define your world? What would break it?"
  3. If Show Bible has color motifs: "Your story uses red for betrayal. Should that translate to a specific hex?"
  4. Build allowed colors table through discussion
  5. Define forbidden colors with reasons: "Why would bright yellow break your aesthetic?"
  6. Establish color meanings: "What does each color represent emotionally?"
- **Menu:** A/P/C
- **Output:** Appends `## Color Palette` to Style_Guide.md (allowed table + forbidden table + meanings)

#### step-05-camera-language.md — Middle (Standard)
- **Type:** Middle (Standard) with A/P/C
- **Goal:** Define lens vocabulary, shot progressions, camera movement rules
- **Frontmatter vars:** `nextStepFile`, `outputFile`, `lensReference`, `advancedElicitationTask`, `partyModeWorkflow`
- **Data:** Load `data/lens-reference.md` for standard lens choices and emotional effects
- **Approach:**
  1. Share expertise: "For intimate close-ups, 85mm creates oppressive isolation. For establishing shots, 24mm makes subjects feel small in vast space."
  2. Explore emotional associations: "What emotions are central to your story? Let me suggest lens pairings."
  3. Build lens vocabulary table through discussion
  4. Design shot progressions: "Paranoia might go 85mm → 24mm → 35mm (contraction → expansion → settle)"
  5. Define movement rules: "What's your default? Static? Dolly? What's FORBIDDEN?"
- **Menu:** A/P/C
- **Output:** Appends `## Camera Language` to Style_Guide.md (lens table + progressions + movement rules)

#### step-06-spatial-rules.md — Middle (Standard)
- **Type:** Middle (Standard) with A/P/C
- **Goal:** Define axis of action, composition rules, negative space meaning
- **Frontmatter vars:** `nextStepFile`, `outputFile`, `advancedElicitationTask`, `partyModeWorkflow`
- **Approach:**
  1. Explain spatial concepts accessibly: "Axis of action ensures characters stay consistent across cuts. In your shards, this means..."
  2. Define screen direction rules: "Characters entering frame-left should stay left-dominant. When should the line be crossed?"
  3. Composition: "Rule of thirds for standard shots? Center framing only for what situations?"
  4. Negative space: "What does empty space mean in your world? Psychological weight? Loneliness?"
- **Menu:** A/P/C
- **Output:** Appends `## Spatial Rules` to Style_Guide.md (axis rules + composition + negative space)

#### step-07-vocabulary.md — Middle (Standard)
- **Type:** Middle (Standard) with A/P/C
- **Goal:** Define required word substitutions and banned words for prompt engineering
- **Frontmatter vars:** `nextStepFile`, `outputFile`, `advancedElicitationTask`, `partyModeWorkflow`
- **Approach:**
  1. Explain why vocabulary matters: "The Prompt Engineer agent will compile your shard prompts. These vocabulary rules ensure precise, consistent language."
  2. Reference target model from config: "Since you're targeting [sora/kling/runway], these word choices matter for [model-specific reasons]"
  3. Build substitutions: "Instead of 'dark', what should the Prompt Engineer write? Maybe 'high-contrast, deep shadows'?"
  4. Build banned words: "What words are too vague? 'Beautiful'? 'Cinematic'? 'Nice lighting'?"
  5. Cross-reference with palette: "Your banned words shouldn't appear as required terms in other sections"
- **Menu:** A/P/C
- **Output:** Appends `## Prompt Vocabulary` to Style_Guide.md (substitutions table + banned words table)

#### step-08-polish.md — Final Polish
- **Type:** Final Polish
- **Goal:** Review entire Style Guide for coherence, generate supporting documents
- **Frontmatter vars:** `outputFile`, `paletteTemplate`, `lensTemplate`, `vocabularyTemplate`, `nextStepFile`, `advancedElicitationTask`, `partyModeWorkflow`
- **Logic:**
  1. Load entire Style_Guide.md
  2. Review for cross-section consistency:
     - Lighting hex codes match color palette hex codes
     - Vocabulary banned words don't appear in other sections as required
     - Camera lens choices have clear emotional justifications
     - Spatial rules are compatible with camera movement rules
  3. Optimize flow: transitions between sections, remove duplication, ensure ## Level 2 headers
  4. Present polished version for review
  5. Generate supporting documents:
     - `Architecture/Palette.md` — extract color definitions from Color Palette section
     - `Architecture/Lens_Language.md` — extract camera specs from Camera Language section
     - `Architecture/Vocabulary.md` — extract banned/required words from Prompt Vocabulary section
- **Menu:** A/P/C (user reviews polished version before finalizing)
- **Output:** Polished Style_Guide.md + 3 supporting documents

#### step-09-final.md — Final
- **Type:** Final (no nextStepFile)
- **Goal:** Summary of created files, suggest next CPM workflows
- **Logic:**
  1. Update Style_Guide.md frontmatter to mark complete
  2. Summary of all files created and their purposes
  3. Remind user how the Cinematographer agent will use these files
  4. Suggest next workflows: character creation (`/cpm-character-create`), shard generation
- **Menu:** No nextStepFile — completion

### Step-by-Step Design: Edit Mode (steps-e/)

#### step-e-01-assess.md — Edit Assessment
- **Type:** Init/Assessment
- **Goal:** Load existing Style Guide, check compliance, present sections for editing
- **Logic:**
  1. Load `Architecture/Style_Guide.md`
  2. Check compliance: all 6 sections present? Proper format?
  3. If non-compliant → offer route to `steps-c/step-00-conversion.md`
  4. If compliant → present section list:
     - [1] Visual Identity Statement
     - [2] Lighting Protocol
     - [3] Color Palette
     - [4] Camera Language
     - [5] Spatial Rules
     - [6] Prompt Vocabulary
  5. User selects section(s) to edit
  6. Collaborative editing of selected section(s)
  7. Update supporting documents if affected (Palette, Lens_Language, Vocabulary)
  8. Offer validation after edits

### Step-by-Step Design: Validate Mode (steps-v/)

#### step-v-01-validate.md — Validation
- **Type:** Validation Sequence (auto-proceed)
- **Goal:** Check Style Guide internal consistency
- **Checks (auto-proceed through all):**
  1. **Structure Check:** All 6 sections present with proper ## Level 2 headers
  2. **Hex Code Validation:** All hex codes match #RRGGBB format
  3. **Palette Consistency:** Lighting source hex codes appear in allowed color palette
  4. **Vocabulary Consistency:** Banned words don't appear as required terms in other sections
  5. **Lens Validity:** All mm values are realistic camera lens values
  6. **Supporting Doc Sync:** Palette.md, Lens_Language.md, Vocabulary.md match main Style Guide
  7. **Completeness:** No empty sections or placeholder text
- **Output:** Validation report with pass/fail per check + severity

### Data Flow

```
config.yaml ──────────────────┐
Show_Bible.md ────────────────┤
                              ▼
step-01-init ──→ Creates Style_Guide.md (from template)
                              │
step-02-visual-identity ──────┤ Appends ## Visual Identity Statement
step-03-lighting ─────────────┤ Appends ## Lighting Protocol
step-04-color-palette ────────┤ Appends ## Color Palette
step-05-camera-language ──────┤ Appends ## Camera Language
step-06-spatial-rules ────────┤ Appends ## Spatial Rules
step-07-vocabulary ───────────┤ Appends ## Prompt Vocabulary
                              │
step-08-polish ──────────────►│ Polishes Style_Guide.md
                              ├──→ Creates Palette.md
                              ├──→ Creates Lens_Language.md
                              └──→ Creates Vocabulary.md
step-09-final ──→ Summary + Next Steps
```

### Subprocess Optimization

- **step-08-polish:** Could use subprocess (Pattern 2) to analyze cross-section consistency before presenting to user
- **steps-v/step-v-01-validate:** Could use subprocess (Pattern 1) for grep-based hex code validation across all sections
- Not critical for create mode — steps are interactive conversations, not bulk analysis

### Workflow Chaining

- **Before this workflow:** Show Bible creation (provides `Bible/Show_Bible.md`)
- **After this workflow:** Character creation (`/cpm-character-create`), Shard generation (`/cpm-shard-generation`)
- **Consumed by:** Cinematographer agent (reads `Architecture/Style_Guide.md` + supporting docs in every Shard Generation Ritual)

---

## Foundation Build Complete

**Created:**
- Folder structure at: `_bmad-output/bmb-creations/workflows/style-guide/`
- `workflow.md` — Tri-modal router (Create/Edit/Validate) with Visual Architect role, CPM config loading, step-file architecture
- `templates/style-guide.template.md` — Main output template with stepsCompleted tracking frontmatter
- `templates/palette.template.md` — Color definitions template for Architecture/Palette.md
- `templates/lens-language.template.md` — Camera specs template for Architecture/Lens_Language.md
- `templates/vocabulary.template.md` — Banned/required words template for Architecture/Vocabulary.md

**Folder Structure:**
```
style-guide/
├── workflow.md
├── workflow-plan-style-guide.md
├── steps-c/                       # (empty — step files built next)
├── steps-e/                       # (empty — step files built next)
├── steps-v/                       # (empty — step files built next)
├── data/                          # (empty — reference files built next)
└── templates/
    ├── style-guide.template.md
    ├── palette.template.md
    ├── lens-language.template.md
    └── vocabulary.template.md
```

**Configuration:**
- Workflow name: style-guide
- Continuable: yes (stepsCompleted tracking in output frontmatter)
- Document output: yes — Structured (4 Architecture/ files)
- Mode: Tri-Modal (Create + Edit + Validate)
- Module: CPM (loads config from `_bmad/cpm/config.yaml`)

**Next Steps:**
- Step 9: Build remaining create-mode steps (02 through 09)
- Then: Build edit and validate mode steps, data files

---

## Step 01 Build Complete

**Created:**
- `steps-c/step-01-init.md` — Init (Continuable) with auto-proceed
- `steps-c/step-01b-continue.md` — Continuation routing with step mapping table

**Step Configuration:**
- Type: Continuable (checks for existing output, routes to 01b if stepsCompleted found)
- Input Discovery: No (Show Bible loaded optionally, not required)
- Menu: Auto-proceed (Pattern 3) — no A/P for init step
- Next Step: step-02-visual-identity

**Key Features:**
- Loads Show Bible context if `{output_folder}/Bible/Show_Bible.md` exists
- Creates output from `templates/style-guide.template.md`
- Continuation step uses mapping table to route to correct next step
- Warm Visual Architect welcome with production roadmap

**Supporting Files:**
- None needed — step-01 references existing templates

---

## All Steps Build Complete

### Create Mode Steps (steps-c/) — 10 files

| Step | File | Type | Menu |
|------|------|------|------|
| 01 | step-01-init.md | Init (Continuable) | Auto-proceed |
| 01b | step-01b-continue.md | Continuation | Auto-proceed (routing) |
| 02 | step-02-visual-identity.md | Middle (Standard) | A/P/C |
| 03 | step-03-lighting.md | Middle (Standard) | A/P/C |
| 04 | step-04-color-palette.md | Middle (Standard) | A/P/C |
| 05 | step-05-camera-language.md | Middle (Standard) | A/P/C |
| 06 | step-06-spatial-rules.md | Middle (Standard) | A/P/C |
| 07 | step-07-vocabulary.md | Middle (Standard) | A/P/C |
| 08 | step-08-polish.md | Final Polish | A/P/C |
| 09 | step-09-final.md | Final | None (completion) |

### Edit Mode Steps (steps-e/) — 1 file

| Step | File | Purpose |
|------|------|---------|
| E-01 | step-e-01-assess.md | Load, assess, section editing, supporting doc sync |

### Validate Mode Steps (steps-v/) — 1 file

| Step | File | Purpose |
|------|------|---------|
| V-01 | step-v-01-validate.md | 7 automated checks with consolidated report |

### Data Reference Files (data/) — 3 files

| File | Purpose | Used By |
|------|---------|---------|
| lighting-reference.md | Lighting styles, hex codes, source types, rule examples | step-03-lighting |
| lens-reference.md | Focal lengths, emotional effects, shot progressions, movement | step-05-camera-language |
| color-theory-reference.md | Color relationships, psychology, palettes, hex quick reference | step-04-color-palette |

### Templates (templates/) — 4 files

| File | Purpose |
|------|---------|
| style-guide.template.md | Main output with stepsCompleted tracking |
| palette.template.md | Architecture/Palette.md structure |
| lens-language.template.md | Architecture/Lens_Language.md structure |
| vocabulary.template.md | Architecture/Vocabulary.md structure |

### Compliance Summary

- All frontmatter: only used variables, relative paths, {variable} format
- All middle steps: A/P/C menu with full handler logic
- All steps: MANDATORY EXECUTION RULES, STEP GOAL, CONTEXT BOUNDARIES, SUCCESS/FAILURE METRICS
- Data files referenced only by steps that use them (no unused frontmatter vars)
- Init step: Auto-proceed (Pattern 3), no A/P — correct per standards
- Final step: No nextStepFile — correct per standards
- Continuation step: Mapping table covers all 8 content step transitions

**Total files created: 18** (1 workflow.md + 10 create steps + 1 edit step + 1 validate step + 3 data files + 4 templates - 2 already created in foundation = 18 new in this phase)

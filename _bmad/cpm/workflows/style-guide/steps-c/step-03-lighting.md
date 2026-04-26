---
name: 'step-03-lighting'
description: 'Define lighting protocol — primary style, hex-coded light sources, and lighting rules checklist'

nextStepFile: './step-04-color-palette.md'
outputFile: '{output_folder}/Architecture/Style_Guide.md'
lightingReference: '../data/lighting-reference.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 3: Lighting Protocol

## STEP GOAL:

Collaboratively define the lighting protocol — primary lighting style, hex-coded light sources table, and an enforceable lighting rules checklist — building on the Visual Identity Statement.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a Visual Architect — an experienced Director of Photography
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You bring lighting design expertise, the user brings their visual intuition
- ✅ Together we translate mood into enforceable lighting specifications

### Step-Specific Rules:

- 🎯 Focus ONLY on lighting — do not stray into color palette, camera, or vocabulary
- 🚫 FORBIDDEN to present empty tables to fill — build the table through conversation
- 💬 Approach: Reference their Visual Identity Statement, then explore lighting mood before getting technical
- 🔧 Hex codes are the OUTPUT of discussion, not the starting point

## EXECUTION PROTOCOLS:

- 🎯 Follow the Explore → Discuss → Formalize → Review pattern
- 💾 Append finalized Lighting Protocol to {outputFile}
- 📖 Update stepsCompleted in {outputFile} frontmatter before proceeding
- 🚫 FORBIDDEN to proceed without user approval of the lighting section

## CONTEXT BOUNDARIES:

- Available: Visual Identity Statement (from step-02), Show Bible context, {lightingReference}
- Focus: Lighting mood, style name, specific hex-coded sources, enforceable rules
- Limits: Color palette comes next — keep lighting-specific here
- Dependencies: Visual Identity Statement guides lighting mood

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Reference and Context

Load {lightingReference} for common lighting styles, techniques, and hex suggestions.

Read the `## Visual Identity Statement` from {outputFile} to ground the conversation.

"Your Visual Identity Statement describes [reference key elements]. Now let's build the lighting rules that bring this vision to life."

### 2. Explore — Lighting Mood

Start with emotional exploration before technical specifics:

- "What mood should your lighting create? Should shadows feel dangerous, peaceful, mysterious?"
- "When you imagine your most important scene lit perfectly — what does the light DO? Where does it come from?"
- "Do you want the audience to feel watched by the light, or hidden by the dark?"

### 3. Discuss — Lighting Style and Techniques

Based on exploration, offer expert suggestions:

- Suggest a named primary style: Chiaroscuro, High-Key, Neon-Noir, Naturalistic, Expressionist, etc.
- Explain what each means practically: "Chiaroscuro means 60%+ shadow coverage — subjects are sculpted by light, not revealed by it"
- Reference from {lightingReference} for technical backing
- Define 3-4 key characteristics of their chosen style

### 4. Formalize — Light Sources Table

Build the light sources table through conversation, not form-filling:

"Let's define your specific light sources. For rim lighting — what color defines the edge of your subjects?"

For each source type (Rim, Key, Fill/Ambient, Accent), collaboratively determine:
- **Color Name:** A memorable name (e.g., "Toxic Glow", "Steel Blue")
- **Hex Code:** Specific #RRGGBB value — offer suggestions: "For that cold steel feeling, #4A6FA5 is a strong starting point. Want warmer or cooler?"
- **Usage:** When this light appears (e.g., "Every exterior shot", "Only in danger scenes")

Build the table progressively as each source is discussed and agreed.

**Target format:**

| Source Type | Color Name | Hex Code | Usage |
|-------------|------------|----------|-------|
| Rim Light | {name} | #{hex} | {when to use} |
| Key Light | {name} | #{hex} | {when to use} |
| Fill/Ambient | {name} | #{hex} | {when to use} |
| Accent | {name} | #{hex} | {when to use} |

### 5. Formalize — Lighting Rules Checklist

"Now let's set the rules the Cinematographer agent will enforce. What should NEVER happen with lighting? What MUST always be present?"

Build enforceable rules as checkboxes:
- [ ] {Rule: e.g., "NEVER use flat, even lighting"}
- [ ] {Rule: e.g., "ALWAYS include volumetric atmosphere"}
- [ ] {Rule: e.g., "Rim light must define subject edges"}
- [ ] {Rule: e.g., "Shadows should occupy 60%+ of frame"}

Aim for 4-6 rules that are specific and enforceable (not vague like "make it look good").

### 6. Review — Present Complete Lighting Protocol

Present the full Lighting Protocol section for review:
- Primary Lighting Style (name + characteristics)
- Light Sources table
- Lighting Rules checklist

"Does this capture how you want every frame lit? Any rules to add, sources to change?"

### 7. Present MENU OPTIONS

Display: **Lighting Protocol Complete — Select an Option:** [A] Advanced Elicitation — explore lighting deeper [P] Party Mode — hear different DPs argue lighting approaches [C] Continue to Color Palette

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask}, and when finished redisplay the menu
- IF P: Execute {partyModeWorkflow}, and when finished redisplay the menu
- IF C: Append `## Lighting Protocol` section (style, sources table, rules checklist) to {outputFile}, update frontmatter stepsCompleted to add 'step-03-lighting', then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#7-present-menu-options)

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and the Lighting Protocol is saved to {outputFile} will you load {nextStepFile} to begin the Color Palette.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Visual Identity Statement referenced to ground lighting decisions
- Lighting reference data loaded and used for expert suggestions
- Primary style named with 3-4 defining characteristics
- Light sources table built through conversation with valid hex codes (#RRGGBB)
- 4-6 enforceable lighting rules defined as checkboxes
- User approved the complete section before proceeding

### ❌ SYSTEM FAILURE:

- Presenting empty tables to fill in
- Generating hex codes without user input
- Not connecting lighting choices to Visual Identity Statement
- Vague rules (e.g., "good lighting") instead of enforceable specifics
- Proceeding without user approval

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

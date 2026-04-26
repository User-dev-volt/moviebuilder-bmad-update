---
name: 'step-08-polish'
description: 'Review entire Style Guide for coherence, optimize, and generate supporting documents'

nextStepFile: './step-09-final.md'
outputFile: '{output_folder}/Architecture/Style_Guide.md'
paletteTemplate: '../templates/palette.template.md'
paletteOutputFile: '{output_folder}/Architecture/Palette.md'
lensTemplate: '../templates/lens-language.template.md'
lensOutputFile: '{output_folder}/Architecture/Lens_Language.md'
vocabularyTemplate: '../templates/vocabulary.template.md'
vocabularyOutputFile: '{output_folder}/Architecture/Vocabulary.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 8: Polish and Compile

## STEP GOAL:

Review the entire Style Guide for cross-section coherence, optimize flow and readability, and generate the three supporting documents (Palette.md, Lens_Language.md, Vocabulary.md) by extracting from the main guide.

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
- ✅ You bring editorial and consistency expertise, the user brings final approval
- ✅ This is the quality gate before the Cinematographer agent uses these rules

### Step-Specific Rules:

- 🎯 Focus on coherence, consistency, and compilation — no new creative content
- 🚫 FORBIDDEN to change meaning or intent without user approval
- 💬 Approach: Present findings transparently, let user decide on any changes
- 📋 This is a review step — flag issues, suggest fixes, get approval

## EXECUTION PROTOCOLS:

- 🎯 Load entire document and perform systematic review
- 💾 Save polished version to {outputFile}, create supporting documents
- 📖 Update stepsCompleted in {outputFile} frontmatter before proceeding
- 🚫 FORBIDDEN to proceed without user approval of polished version

## CONTEXT BOUNDARIES:

- Available: Complete Style Guide with all 6 sections
- Focus: Cross-section consistency, flow, compilation
- Limits: No new content — only optimization of existing content
- Dependencies: All 6 content sections must be complete

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Complete Style Guide

Read {outputFile} in its entirety. Confirm all 6 sections are present:
- Visual Identity Statement
- Lighting Protocol
- Color Palette
- Camera Language
- Spatial Rules
- Prompt Vocabulary

If any section is missing, alert the user and suggest returning to complete it.

### 2. Cross-Section Consistency Review

Perform these checks and report findings:

**Hex Code Consistency:**
- All lighting source hex codes should appear in the Color Palette allowed table
- Flag any hex codes in Lighting that are NOT in the allowed palette

**Vocabulary Consistency:**
- Banned words should NOT appear as required terms in any other section
- Required substitutions should be consistent with language used in other sections
- Flag any conflicts

**Camera-Spatial Alignment:**
- Camera movement rules should be compatible with spatial composition rules
- Lens choices should support the composition conventions defined
- Flag any contradictions

**Overall Coherence:**
- Visual Identity Statement should be reflected in all technical sections
- All sections should feel like they serve the same production
- Flag any section that feels disconnected from the whole

Present findings: "Here's what I found in my consistency review: [list findings with severity]"

### 3. Optimize Flow

If user approves changes, optimize the Style Guide:
- Ensure smooth transitions between sections
- Remove any duplication across sections
- Confirm all ## Level 2 headers are consistent
- Improve readability without changing meaning
- Preserve the user's voice and intent

Present the polished version for final review.

### 4. Generate Supporting Documents

Create the three supporting documents by extracting from the main Style Guide:

**{paletteOutputFile}** — from {paletteTemplate}:
- Extract Allowed Colors table from Color Palette section
- Extract Forbidden Colors table from Color Palette section
- Extract Color Meanings from Color Palette section

**{lensOutputFile}** — from {lensTemplate}:
- Extract Lens Vocabulary table from Camera Language section
- Extract Shot Progressions from Camera Language section
- Extract Camera Movement Rules from Camera Language section

**{vocabularyOutputFile}** — from {vocabularyTemplate}:
- Extract Required Substitutions table from Prompt Vocabulary section
- Extract Banned Words table from Prompt Vocabulary section

"I've generated the three supporting documents. These are what the Cinematographer and Prompt Engineer agents will consume directly."

### 5. Final Review

Present summary of all changes made and documents generated.

"Everything looks consistent and ready for production. Want to make any final adjustments?"

### 6. Present MENU OPTIONS

Display: **Polish Complete — Select an Option:** [A] Advanced Elicitation — deep-dive into any section [P] Party Mode — final perspectives on the guide [C] Continue to Completion

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask}, and when finished redisplay the menu
- IF P: Execute {partyModeWorkflow}, and when finished redisplay the menu
- IF C: Save polished {outputFile}, ensure supporting documents are written ({paletteOutputFile}, {lensOutputFile}, {vocabularyOutputFile}), update frontmatter stepsCompleted to add 'step-08-polish', then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#6-present-menu-options)

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and all documents are saved will you load {nextStepFile} for completion.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All 6 sections confirmed present
- Hex code consistency checked (lighting vs palette)
- Vocabulary consistency checked (banned words vs other sections)
- Camera-spatial alignment checked
- Overall coherence verified against Visual Identity
- Flow optimized with user approval
- Three supporting documents generated from templates
- User approved final polished version

### ❌ SYSTEM FAILURE:

- Not loading entire document before review
- Missing consistency checks
- Changing meaning without user approval
- Not generating all three supporting documents
- Supporting documents not matching main Style Guide
- Proceeding without user approval

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

---
name: 'step-07-vocabulary'
description: 'Define required word substitutions and banned words for prompt engineering'

nextStepFile: './step-08-polish.md'
outputFile: '{output_folder}/Architecture/Style_Guide.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 7: Prompt Vocabulary

## STEP GOAL:

Collaboratively define the prompt vocabulary — required word substitutions and banned words — ensuring the Prompt Engineer agent compiles precise, consistent language in every shard prompt.

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
- ✅ You bring prompt engineering expertise for AI video generation, the user brings their precision standards
- ✅ Together we define a vocabulary that prevents vibe drift

### Step-Specific Rules:

- 🎯 Focus ONLY on vocabulary rules — this is the last content section
- 🚫 FORBIDDEN to present empty tables — build through conversation
- 💬 Approach: Explain WHY vocabulary matters for AI generation, then collaboratively build the rules
- 🔍 Cross-reference previous sections — banned words must not appear as required terms elsewhere

## EXECUTION PROTOCOLS:

- 🎯 Follow the Explore → Discuss → Formalize → Review pattern
- 💾 Append finalized Prompt Vocabulary to {outputFile}
- 📖 Update stepsCompleted in {outputFile} frontmatter before proceeding
- 🚫 FORBIDDEN to proceed without user approval

## CONTEXT BOUNDARIES:

- Available: All previous sections (Visual Identity, Lighting, Color, Camera, Spatial)
- Focus: Word substitutions and banned words for prompt engineering
- Limits: This is the final content section — polish comes next
- Dependencies: All previous sections inform vocabulary choices

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Context and Introduction

Read the complete {outputFile} to understand all established rules.

Explain why vocabulary matters:

"The Prompt Engineer agent will compile your shard prompts using these rules. Vague words create vibe drift — 'dark' could mean anything. But 'high-contrast, deep shadows with 60% frame coverage' gives the AI a precise instruction. Let's lock down the vocabulary."

If target AI model is known from config: "Since you're targeting [model], certain word choices matter because [model-specific prompt behavior]."

### 2. Explore — Vague Words to Eliminate

"Let's start with the words that are too vague for your vision. What words do you NEVER want in a prompt?"

Guide the conversation:
- "What does 'cinematic' mean to you specifically? Because to an AI, it means nothing precise."
- "What about 'dark' — you have specific hex codes now. What should replace it?"
- "Words like 'beautiful', 'nice', 'interesting', 'cool' — these are prompt poison. What specific terms capture what those words mean in YOUR production?"

### 3. Formalize — Required Substitutions Table

Build through discussion:

"For each vague word, let's define the precise alternative."

| Instead of... | Use... |
|---------------|--------|
| "dark" | "high-contrast, deep shadows" |
| "neon" | "specific hex code + neon rim light" |
| "cinematic" | "volumetric lighting, film grain, [specific quality]" |
| {vague word} | {specific alternative using their established rules} |

Connect substitutions to previously defined rules — hex codes, lighting styles, lens choices.

### 4. Formalize — Banned Words Table

"Now the absolute banned list. These words must never appear in any prompt."

| Word | Reason | Alternative |
|------|--------|-------------|
| {word} | {why banned — what it does wrong} | {what to use instead} |

### 5. Cross-Reference Check

Review the vocabulary against all previous sections:

- "Let me check — your banned words don't appear as required terms in your Lighting Protocol, Color Palette, or Camera Language sections."
- Flag any conflicts: "Your banned word '{word}' appears in your Lighting Protocol. Should we update the protocol or change the ban?"

Resolve any conflicts with the user.

### 6. Review — Present Complete Prompt Vocabulary

Present the full Prompt Vocabulary section:
- Required substitutions table
- Banned words table
- Cross-reference results

"This is the last content section. Does the vocabulary feel complete? Any more words to ban or substitutions to add?"

### 7. Present MENU OPTIONS

Display: **Prompt Vocabulary Complete — Select an Option:** [A] Advanced Elicitation — explore vocabulary precision deeper [P] Party Mode — debate vocabulary choices [C] Continue to Polish and Compile

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask}, and when finished redisplay the menu
- IF P: Execute {partyModeWorkflow}, and when finished redisplay the menu
- IF C: Append `## Prompt Vocabulary` section (substitutions table, banned words table) to {outputFile}, update frontmatter stepsCompleted to add 'step-07-vocabulary', then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#7-present-menu-options)

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and Prompt Vocabulary is saved to {outputFile} will you load {nextStepFile} to begin Polish and Compile.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Why vocabulary matters for AI generation was explained
- Required substitutions connect to previously established rules (hex codes, styles)
- Banned words have specific reasons and alternatives
- Cross-reference check completed — no conflicts between vocabulary and other sections
- User approved complete section

### ❌ SYSTEM FAILURE:

- Presenting empty tables to fill
- Not explaining why vocabulary precision matters
- Banned words conflicting with terms used in other sections
- No cross-reference check performed
- Proceeding without user approval

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

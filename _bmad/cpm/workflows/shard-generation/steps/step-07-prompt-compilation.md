---
name: 'step-07-prompt-compilation'
description: 'Ritual Step 5 — Acting AS Prompt Engineer (Leonard Shelby), compile the final prompt'

nextStepFile: './step-08-state-update.md'
promptEngineerAgent: '{project-root}/_bmad/cpm/agents/prompt-engineer.agent.yaml'
promptStructureTemplate: '../data/prompt-structure-template.md'
promptOutputTemplate: '../templates/prompt-output.template.md'
vocabularyFile: '{project-root}/Architecture/Vocabulary.md'
promptOutputPath: '{project-root}/Output/Prompts'
---

# Step 7: Prompt Compilation (Ritual Step 5)

## STEP GOAL:

Acting AS the Prompt Engineer agent (Leonard Shelby), compile the final generation prompt from all three agent inputs. Structure for maximum AI compliance and save to the output file.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in the config `{communication_language}`

### Role Reinforcement:

- ✅ For this step, you ARE **Leonard Shelby — the Prompt Engineer** (Prompt Compiler & AI Whisperer)
- ✅ Load the Prompt Engineer agent persona from {promptEngineerAgent}
- ✅ Think in attention windows, token distribution, and weight
- ✅ Speak in structured patterns with [CRITICAL] and [ANCHOR POINT] markers
- ✅ Treat every prompt like a tattoo — permanent, precise, purposeful

### Step-Specific Rules:

- 🎯 COMPILE inputs from all three agents — do not invent new content
- 🚫 FORBIDDEN to compile without all three agent inputs (Showrunner, Cinematographer, Script Supervisor)
- 🚫 FORBIDDEN to use any banned words from Vocabulary
- 🔒 Critical features MUST appear in first 25% of prompt
- 💬 Approach: Structured, technical, attention-optimized

## EXECUTION PROTOCOLS:

- 🎯 Load Prompt Engineer agent persona and embody it
- 💾 Compile final prompt and save to output file
- 📖 Reference prompt structure template for exact format
- 🚫 Auto-proceed after saving — do not wait for user input

## REQUIRED INPUTS:

- Showrunner Notes (from step-03) — WHAT happens
- Cinematographer Specs (from step-04) — HOW it looks
- Script Supervisor Validation (from step-05) — STATE is correct, injections defined
- State-Diff Check PASSED (from step-06) — gate confirmed

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Prompt Engineer Persona

Load {promptEngineerAgent} and embody the Prompt Engineer identity:
- Name: Leonard Shelby
- Role: Prompt Compiler & AI Whisperer
- Principles: Structure for Attention, Never Compile Blind, Vocabulary Absolute, Exit Hook Always

### 2. Load Prompt Structure Reference

Load {promptStructureTemplate} for the exact prompt format and compilation rules.

### 3. Verify All Three Inputs

Confirm availability of:
- [ ] Showrunner Notes (from step-03)
- [ ] Cinematographer Specs (from step-04)
- [ ] Script Supervisor Validation + Injections (from step-05)

**HALT if any input is missing** — this should never happen if the gate passed, but verify.

### 4. Compile the Prompt

**Build prompt using the exact structure:**

```
[ID: SCENE_{sceneNumber}.{shardNumber}_{BEAT_NAME}]

[Technical Header]:
{lens from Cinematographer}mm {shot_type}, {fps}fps, {lighting from Cinematographer}, {atmosphere}.

[Subject/Asset]:
{CRITICAL FEATURES FIRST — from Script Supervisor's state check}
{Character description — from Bible files}
{Outfit/condition — from Script Supervisor's mutable state}

[Action/State]:
{What character is doing — from Showrunner's beat notes}
{Movement/position — from Script Supervisor's state}
{Held/worn items — from Script Supervisor's injections}

[Environment/Lighting]:
{Lighting with HEX CODES — from Cinematographer's protocol}
{Background elements — from Cinematographer's composition}
{Atmospheric conditions — from Style Guide}

[Temporal Constraint]:
{Duration}s. {Movement/pacing}. {EXIT STATE HOOK — from Script Supervisor's handshake}.
```

### 5. Apply Attention Window Optimization

**First 25% of prompt MUST contain:**
1. Character distinguishing features (scars, marks — with LEFT/RIGHT)
2. Character identity anchors
3. Key emotional state
4. Any state that MUST NOT drift

Reorder within sections if needed to front-load critical features.

### 6. Vocabulary Check

Check entire prompt against {vocabularyFile}:
- Replace ANY banned word with its required alternative
- Document all substitutions

### 7. Apply Script Supervisor Injections

For each injection from step-05:
- Insert exact injection text at specified location
- Verify injection doesn't conflict with other prompt content

### 8. Build Notes

Append Build Notes after the prompt:

```
**Build Notes:**
- Anchor Points: {what's in first 25%}
- Vocabulary Compliance: Banned words avoided: {list of substitutions}
- Exit Hook: {exact handshake text}
- Injections Applied: {list of injections}
- Source: Showrunner (Albus) → Cinematographer (Galadriel) → Script Supervisor (Jonas) → Prompt Engineer (Leonard Shelby)
```

### 9. Save Prompt File

Save compiled prompt to:
`{promptOutputPath}/Scene_{sceneNumber}_Shard_{shardNumber}_prompt.md`

Display: "**✅ Prompt compiled and saved:** `Output/Prompts/Scene_{sceneNumber}_Shard_{shardNumber}_prompt.md`"

### 10. Auto-Proceed to State Update

Display: "**Prompt compilation complete.** Proceeding to state update..."

**No menu needed** — Auto-proceed to {nextStepFile}.

Load, read entirely, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- Prompt Engineer persona loaded and embodied
- All three agent inputs verified present
- Prompt compiled in exact structure format
- Critical features in first 25%
- Vocabulary checked — no banned words
- All injections applied
- Build notes appended
- Prompt saved to correct output path
- Auto-proceeded to step-08

### ❌ SYSTEM FAILURE:

- Compiling without all three agent inputs
- Using banned vocabulary words
- Critical features not in first 25%
- Missing exit state hook
- Not applying Script Supervisor injections
- Not saving to correct file path
- Inventing content not provided by agents

**Master Rule:** Leonard Shelby COMPILES — he does not create. Every word comes from the three agents or the loaded context. Structure for attention. Exit hook always.

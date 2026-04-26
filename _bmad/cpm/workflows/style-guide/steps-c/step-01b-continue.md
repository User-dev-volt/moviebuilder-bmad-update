---
name: 'step-01b-continue'
description: 'Resume the Style Guide workflow from a previous session'

outputFile: '{output_folder}/Architecture/Style_Guide.md'
---

# Step 1b: Continue Style Guide

## STEP GOAL:

Resume the Style Guide workflow from where the user left off in a previous session, by reading the stepsCompleted array and routing to the correct next step.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a Visual Architect — an experienced Director of Photography
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You bring cinematographic expertise, the user brings creative vision

### Step-Specific Rules:

- 🎯 Focus ONLY on determining where to resume and routing there
- 🚫 FORBIDDEN to start or redo any creative work
- 💬 Welcome the user back with a brief summary of progress

## EXECUTION PROTOCOLS:

- 🎯 Read stepsCompleted from output file
- 💾 Update `lastContinued` date in frontmatter
- 📖 Route to the correct next step
- 🚫 FORBIDDEN to skip the routing logic

## CONTEXT BOUNDARIES:

- Available: Output file with stepsCompleted, step files in this folder
- Focus: Routing only — determine next step and load it
- Limits: Do not re-execute completed steps
- Dependencies: Requires output file with stepsCompleted

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Read Progress

Load {outputFile} and read the `stepsCompleted` array from frontmatter.

### 2. Determine Next Step

Find the last entry in `stepsCompleted`. Map to the next step file:

| Last Completed | Next Step File |
|----------------|----------------|
| step-01-init | ./step-02-visual-identity.md |
| step-02-visual-identity | ./step-03-lighting.md |
| step-03-lighting | ./step-04-color-palette.md |
| step-04-color-palette | ./step-05-camera-language.md |
| step-05-camera-language | ./step-06-spatial-rules.md |
| step-06-spatial-rules | ./step-07-vocabulary.md |
| step-07-vocabulary | ./step-08-polish.md |
| step-08-polish | ./step-09-final.md |

### 3. Welcome Back

"**Welcome back, {user_name}!**

You've completed [N] of 8 sections so far:
[list completed steps with checkmarks]

Let's pick up with [next step name]..."

Update `lastContinued` in {outputFile} frontmatter to today's date.

### 4. Route to Next Step

Load, read entire file, then execute the determined next step file.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- stepsCompleted correctly read from output file
- Next step correctly determined from mapping table
- User welcomed with progress summary
- Correct step file loaded and executed

### ❌ SYSTEM FAILURE:

- Re-executing completed steps
- Loading wrong next step
- Starting creative work instead of routing
- Skipping the progress summary

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

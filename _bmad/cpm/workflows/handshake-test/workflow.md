---
name: handshake-test
description: "Two-shard validation protocol to prove CPM maintains continuity across shard boundaries"
web_bundle: true
installed_path: '{project-root}/_bmad/cpm/workflows/handshake-test'
---

# Two-Shard Handshake Test

Validation protocol to prove that CPM maintains continuity across shard boundaries. This is the quality gate for the entire system.

## What This Workflow Does

- Creates a minimal test project with one character (Hero), one item (Silver Key), and one style rule (rim light)
- Runs Shard A: Hero picks up the Silver Key
- Runs Shard B: WITHOUT reminding the agent about the Key, scar, or position
- Validates that Shard B's prompt contains all continuity elements from state files alone
- Tracks consecutive passes — 3 passes = CPM VALIDATED

## Role

You are the **Test Coordinator** — you set up fixtures, orchestrate two shard-generation runs, and validate results objectively. You do NOT generate creative content. You do NOT provide hints to the shard-generation ritual during Shard B. You enforce the test protocol with strict procedural discipline.

---

## WORKFLOW ARCHITECTURE

This uses **step-file architecture** for disciplined execution:

### Core Principles

- **Micro-file Design**: Each step is a self-contained instruction file
- **Just-In-Time Loading**: Only the current step file is in memory
- **Sequential Enforcement**: Test steps are non-negotiable — no skipping, no reordering
- **Auto-Proceed**: Steps auto-proceed (no user menus between test steps, except final report)
- **Prescriptive Instructions**: Each step has exact required actions and exact validation checks
- **CREATE-ONLY**: No edit or validate modes — this workflow IS a validation

### Step Processing Rules

1. **READ COMPLETELY**: Always read the entire step file before taking any action
2. **FOLLOW SEQUENCE**: Execute all numbered sections in order, never deviate
3. **AUTO-PROCEED**: Steps auto-proceed to the next step (no user menu between steps)
4. **HALT ON FAILURE**: If any required file is missing or setup fails, HALT immediately
5. **LOAD NEXT**: When directed, load, read entire file, then execute the next step file

### Critical Rules (NO EXCEPTIONS)

- 🛑 **NEVER** load multiple step files simultaneously
- 📖 **ALWAYS** read entire step file before execution
- 🚫 **NEVER** skip steps or optimize the sequence
- 🎯 **ALWAYS** follow the exact instructions in the step file
- 🔒 **NEVER** provide hints about the Key, scar, or position during Shard B
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in Test Coordinator style with the config `{communication_language}`

---

## INITIALIZATION SEQUENCE

### 1. Configuration Loading

Load and read full config from {project-root}/_bmad/cpm/config.yaml and resolve:

- `user_name`, `communication_language`
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in the config `{communication_language}`

### 2. Begin Test Protocol

This is CREATE-ONLY — no mode selection needed. Proceed directly to Step 1.

Load, read completely, then execute `steps/step-01-setup.md`

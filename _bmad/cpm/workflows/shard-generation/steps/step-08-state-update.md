---
name: 'step-08-state-update'
description: 'Ritual Step 6 — Save exit state for handshake and present completion menu'

exitStateTemplate: '../templates/exit-state.template.md'
productionScenesPath: '{project-root}/Production/Scenes'
step01File: './step-01-init.md'
---

# Step 8: State Update & Completion (Ritual Step 6)

## STEP GOAL:

Save the exit state file for this shard (enabling the handshake with the next shard) and present the completion menu.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Ritual Coordinator** for this step
- ✅ This is a FILE OUTPUT step — write the exit state file
- ✅ The exit state IS the handshake — without it, the next shard has no continuity

### Step-Specific Rules:

- 🎯 Focus on writing the exit state file from Script Supervisor's handshake definition
- 🚫 FORBIDDEN to modify or reinterpret the handshake — write exactly what Jonas defined
- ⏸️ HALT at the completion menu and wait for user input
- 💬 Approach: Systematic, file-write, then menu

## EXECUTION PROTOCOLS:

- 🎯 Write exit state file from Script Supervisor's handshake (step-05)
- 💾 Save to Production/Scenes/Scene_{XX}/state/ directory
- 📖 Display ritual completion summary
- ⏸️ Present completion menu and WAIT for user input

## REQUIRED INPUTS:

- Script Supervisor's Exit State and Entry Contract (from step-05)
- Scene number and shard number (from step-01)

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Exit State Template

Load {exitStateTemplate} for the exit state file structure.

### 2. Build Exit State File

Using the Script Supervisor's handshake definition from step-05, populate the exit state template:

**For each on-camera character:**
- Position (where they end in frame)
- Facing (direction)
- Expression (emotional state)
- Action (what they're doing as shard ends)
- Holding (items in hand)
- Physical Condition (any changes this shard)

**Environment state:**
- Lighting position
- Time progression
- Active environmental elements

**Entry contract for next shard:**
- Must start with (requirements)
- Must NOT show (forbidden)

**State changes this shard:**
- What changed from previous state and why

**Active contracts:**
- Contract status after this shard

### 3. Save Exit State File

Ensure the directory exists:
`{productionScenesPath}/Scene_{sceneNumber}/state/`

Save exit state file to:
`{productionScenesPath}/Scene_{sceneNumber}/state/shard_{shardNumber}_exit_state.md`

Display: "**✅ Exit state saved:** `Production/Scenes/Scene_{sceneNumber}/state/shard_{shardNumber}_exit_state.md`"

### 4. Display Ritual Completion Summary

```
══════════════════════════════════════
✅ SHARD GENERATION RITUAL COMPLETE
   Scene {sceneNumber}, Shard {shardNumber}
══════════════════════════════════════

📋 Ritual Steps Completed:
  1. Context Loading      ✅
  2. Showrunner Review     ✅ (Albus)
  3. Cinematographer Specs ✅ (Galadriel)
  4. Script Supervisor     ✅ (Jonas)
  5. State-Diff Check      ✅ PASSED
  6. Prompt Compilation    ✅ (Leonard Shelby)
  7. State Update          ✅

📄 Files Written:
  - Output/Prompts/Scene_{sceneNumber}_Shard_{shardNumber}_prompt.md
  - Production/Scenes/Scene_{sceneNumber}/state/shard_{shardNumber}_exit_state.md

🤝 Handshake Ready:
  - Exit state saved for Shard {shardNumber + 1}
══════════════════════════════════════
```

### 5. Present MENU OPTIONS

Display:

"**Select an option:**

**[N] Next Shard** — Start fresh ritual for the next shard
**[R] Re-run** — Re-run this shard with adjustments
**[V] Validate** — Run handshake test on this shard
**[Q] Quit** — Exit the ritual"

#### Menu Handling Logic:

- IF N: Start a FRESH ritual run — load, read entirely, then execute {step01File}
- IF R: Ask user what they want to adjust, then reload {step01File} with same scene/shard
- IF V: Display "Run the Handshake Test workflow to validate this shard's continuity." and redisplay menu
- IF Q: Display "**Ritual complete. Exiting.**" and stop
- IF Any other comments or queries: help user respond then redisplay menu

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- "Next Shard" starts a FRESH run (reload step-01), not a continuation
- After menu items N and R, the full ritual restarts from step-01

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- Exit state file written with complete handshake data
- Exit state saved to correct file path
- Completion summary displayed with all steps checked
- Menu presented and halted for user input
- "Next Shard" correctly routes to fresh step-01 execution

### ❌ SYSTEM FAILURE:

- Not writing the exit state file
- Writing incomplete handshake (missing characters or entry contract)
- Not displaying completion summary
- Auto-proceeding without presenting menu
- "Next Shard" attempting to continue instead of fresh restart

**Master Rule:** The exit state IS the handshake. Without it, the next shard is blind. Write it completely, confirm it saved, then let the user decide what's next.

---
name: 'step-02-shard-a'
description: 'Execute shard-generation ritual for Shard A — Hero picks up the Silver Key'

nextStepFile: './step-03-shard-b.md'
shardGenerationWorkflow: '{project-root}/_bmad/cpm/workflows/shard-generation/workflow.md'
testProjectRoot: '{test_project_root}'
promptOutputPath: '{test_project_root}/Output/Prompts/Scene_01_Shard_01_prompt.md'
exitStatePath: '{test_project_root}/Production/Scenes/Scene_01/state/shard_01_exit_state.md'
---

# Step 2: Shard A — Item Acquisition

## STEP GOAL:

Execute the shard-generation ritual for Scene 01, Shard 01 with the narrative "Hero picks up the Silver Key." After completion, verify the ritual produced the expected output files.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in Test Coordinator style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Test Coordinator** for this step
- ✅ You are ORCHESTRATING the shard-generation ritual, not performing it
- ✅ For Shard A, you MAY provide the narrative direction (this is the setup shard, not the test shard)

### Step-Specific Rules:

- 🎯 Focus on running shard-generation for Shard A with the correct narrative
- 🚫 FORBIDDEN to skip the shard-generation ritual or simulate its output
- 💬 Approach: Orchestrate, then verify outputs

## EXECUTION PROTOCOLS:

- 🎯 Execute shard-generation workflow against the test project
- 💾 Verify prompt and exit state files were written
- 📖 The exit state from Shard A is the critical handshake that Shard B will depend on
- 🛑 HALT if shard-generation fails or produces no output

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Announce Shard A

Display:

"**SHARD A: Item Acquisition**

Running the shard-generation ritual for Scene 01, Shard 01.

**Narrative:** Hero picks up the Silver Key from the pedestal.

**Expected exit state:**
- Hero holding Silver Key in right hand
- Looking frame-left
- Scar visible on left cheek

Launching shard-generation ritual..."

### 2. Execute Shard-Generation Ritual

Load and execute {shardGenerationWorkflow}.

**When the shard-generation workflow asks for scene and shard:**
- Scene: `1`
- Shard: `1`

**IMPORTANT:** The shard-generation ritual must run against the test project at `{testProjectRoot}`. The `{project-root}` for the ritual context should resolve to `{testProjectRoot}`.

**When the Showrunner asks for narrative direction:**
- Provide: "Hero approaches the pedestal and picks up the Silver Key. Hero holds the Silver Key in their right hand, looking frame-left."

**Let the ritual run through all 8 steps.** When the shard-generation ritual completes and presents its completion menu, select **Q (Quit)** to return to the handshake test.

### 3. Verify Shard A Output

After shard-generation completes, verify these files exist:

1. **Prompt file:** `{promptOutputPath}`
2. **Exit state file:** `{exitStatePath}`

**If either file is missing:** HALT and display error.

### 4. Confirm Shard A Complete

Display:

```
✅ SHARD A COMPLETE

Prompt: Output/Prompts/Scene_01_Shard_01_prompt.md ✅
Exit State: Production/Scenes/Scene_01/state/shard_01_exit_state.md ✅

The exit state now contains the handshake data for Shard B.
Shard B will rely ENTIRELY on state files for continuity.

Proceeding to Shard B (continuity test)...
```

### 5. Auto-Proceed to Shard B

**No menu needed** — Auto-proceed to {nextStepFile}.

Load, read entirely, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- Shard-generation ritual completed for Scene 01, Shard 01
- Prompt file exists at expected path
- Exit state file exists at expected path
- Narrative included Hero picking up Silver Key
- Auto-proceeded to step-03

### ❌ SYSTEM FAILURE:

- Skipping the shard-generation ritual
- Simulating or fabricating output files
- Not providing narrative direction for Shard A
- Proceeding without verifying output files exist

**Master Rule:** Shard A is the setup. Run the real ritual. Verify the outputs. The exit state is the bridge to Shard B.

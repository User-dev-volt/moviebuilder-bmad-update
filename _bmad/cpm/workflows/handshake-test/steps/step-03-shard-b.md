---
name: 'step-03-shard-b'
description: 'Execute shard-generation ritual for Shard B — continuity test WITHOUT hints'

nextStepFile: './step-04-validate-report.md'
shardGenerationWorkflow: '{project-root}/_bmad/cpm/workflows/shard-generation/workflow.md'
testProjectRoot: '{test_project_root}'
promptOutputPath: '{test_project_root}/Output/Prompts/Scene_01_Shard_02_prompt.md'
---

# Step 3: Shard B — Continuity Test

## STEP GOAL:

Execute the shard-generation ritual for Scene 01, Shard 02. This is the ACTUAL TEST. You must NOT provide any hints about the Silver Key, the scar, the position, or the lighting. The state files must carry ALL continuity.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in Test Coordinator style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Test Coordinator** — strictly neutral during Shard B
- ✅ The ENTIRE POINT of this step is proving continuity WITHOUT human intervention
- ✅ State files must carry the continuity, not you

### Step-Specific Rules:

- 🔒 **CRITICAL — NO HINTS:** Do NOT mention the Silver Key, the scar, the position (frame-left), or the lighting (#FF00FF) when providing narrative for Shard B
- 🚫 FORBIDDEN to remind the agent about any state from Shard A
- 🚫 FORBIDDEN to add continuity details to the narrative direction
- 🎯 Provide ONLY minimal narrative: "Hero continues down the corridor"
- 💬 Let the Script Supervisor, character files, and exit state do their job

## EXECUTION PROTOCOLS:

- 🎯 Execute shard-generation with MINIMAL narrative and ZERO hints
- 🔒 This is the test — hands off. Let state files work.
- 💾 Verify prompt file was written
- 📖 Do NOT read or preview the Shard B prompt — that's for step-04

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Announce Shard B

Display:

```
══════════════════════════════════════
🧪 SHARD B: CONTINUITY TEST
══════════════════════════════════════

Running shard-generation for Scene 01, Shard 02.

⚠️  NO HINTS WILL BE PROVIDED about:
   - The Silver Key
   - The scar on the left cheek
   - The frame-left position
   - The #FF00FF rim light

The state files and character Bible must carry
ALL continuity. This is the test.

Launching shard-generation ritual...
══════════════════════════════════════
```

### 2. Execute Shard-Generation Ritual

Load and execute {shardGenerationWorkflow}.

**When the shard-generation workflow asks for scene and shard:**
- Scene: `1`
- Shard: `2`

**IMPORTANT:** The shard-generation ritual must run against the test project at `{testProjectRoot}`.

**When the Showrunner asks for narrative direction:**
- Provide ONLY: "Hero continues down the corridor."
- Do NOT add ANY other details
- Do NOT mention Key, scar, position, lighting, or any state

**Let the ritual run through all 8 steps.** The Script Supervisor (step-05 of shard-generation) should:
- Load the character file and detect the scar
- Load the Shard 1 exit state and detect the Key and position
- Inject these into the prompt

When the shard-generation ritual completes and presents its completion menu, select **Q (Quit)** to return to the handshake test.

### 3. Verify Shard B Output

After shard-generation completes, verify this file exists:

**Prompt file:** `{promptOutputPath}`

**If file is missing:** HALT and display error.

### 4. Confirm Shard B Complete

Display:

```
✅ SHARD B COMPLETE

Prompt: Output/Prompts/Scene_01_Shard_02_prompt.md ✅

Shard B ritual completed with NO hints provided.
Proceeding to validation...
```

### 5. Auto-Proceed to Validation

**No menu needed** — Auto-proceed to {nextStepFile}.

Load, read entirely, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- Shard-generation ritual completed for Scene 01, Shard 02
- NO hints were provided about Key, scar, position, or lighting
- Narrative direction was ONLY "Hero continues down the corridor"
- Prompt file exists at expected path
- Auto-proceeded to step-04

### ❌ SYSTEM FAILURE:

- Mentioning the Silver Key in narrative direction
- Mentioning the scar in narrative direction
- Mentioning frame-left position in narrative direction
- Mentioning #FF00FF or rim light in narrative direction
- Adding ANY continuity details to the narrative
- Skipping the shard-generation ritual

**Master Rule:** This is the test. ZERO HINTS. The state files either work or they don't. Your job is to stay out of the way.

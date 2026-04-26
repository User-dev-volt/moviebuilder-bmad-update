---
name: 'step-03-characters'
description: 'Select on-camera characters and verify each exists in Bible/Characters/ — HALT if any are missing'

nextStepFile: './step-04-narrative.md'
sceneBriefFile: '{project-root}/Production/Scenes/Scene_{sceneNumber}/scene-brief.md'
characterIndexFile: '{project-root}/Bible/Characters/_index.md'
characterFolder: '{project-root}/Bible/Characters'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 3: Characters

## STEP GOAL:

To identify all on-camera characters for this scene and verify that each has a character state file in `Bible/Characters/`. Missing character files are a HARD STOP — the Script Supervisor cannot do its job without them.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Scene Architect** — enforcing CPM's character continuity contract
- ✅ Character files are not optional. They are the memory. No file = no continuity = no production.
- ✅ Friendly but firm on the HALT rule

### Step-Specific Rules:

- 🎯 Focus on character selection and verification — nothing else
- 🚫 HARD STOP if any named character has no file in Bible/Characters/
- 💬 Load character index for context if it exists
- 🚫 FORBIDDEN to proceed to step-04 with unverified characters

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Character Index (If Available)

**IF {characterIndexFile} exists:**
- Load it to show available characters to the filmmaker
- Present as reference: "Here are your available characters:"
  ```
  {contents of _index.md}
  ```

**IF NOT:** Note that no index exists — filmmaker will name characters manually.

### 2. Ask for On-Camera Characters

"**Who is on camera in this scene?**

Tell me every character the camera will show — even briefly. Background figures without character files can be noted as 'background' and don't need verification.

Who's in Scene {sceneNumber}?"

Wait for response. Collect all named characters.

### 3. Verify Each Character File

For each named character:

**Build file path:** `{characterFolder}/{characterName}.md`

**Check if file exists:**

**✅ IF file exists:**
- Note: `{characterName}` — VERIFIED ✅

**🛑 IF file does NOT exist:**

"**🛑 HALT — Character file missing: {characterName}**

`Bible/Characters/{characterName}.md` does not exist. The Script Supervisor needs this file to track {characterName}'s state (outfit, inventory, physical condition) across every shard.

**You must run `/cpm-character-create` to build {characterName}'s character file before this scene can proceed.**

Once created, return here and we'll continue."

**STOP. Do not proceed until all named characters are verified.**

### 4. Report Verification Results

Once all characters checked:

"**Character Verification Complete:**

{For each character:}
- **{characterName}** — VERIFIED ✅ (`Bible/Characters/{characterName}.md`)

All on-camera characters are confirmed. Ready to proceed."

### 5. Confirm Character List

"**On-camera characters for Scene {sceneNumber}:**
{list}

Is this complete? Any other characters to add?"

Adjust if needed. Confirm final list.

### 6. Save to Scene Brief

Update {sceneBriefFile}:
- Update frontmatter: `on_camera_characters: [{character1}, {character2}, ...]`
- Append 'step-03-characters' to stepsCompleted
- Set lastStep: 'step-03-characters'
- Set lastModified: '{current_date}'

"**✅ Characters saved.**"

### 7. Present MENU OPTIONS

Display: **Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask}, then redisplay menu
- IF P: Execute {partyModeWorkflow}, then redisplay menu
- IF C: Load, read entirely, then execute {nextStepFile}
- IF Any other: Help user, redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- All named characters verified against Bible/Characters/
- Missing characters result in HALT with clear instruction
- Final list confirmed by filmmaker
- on_camera_characters updated in frontmatter
- stepsCompleted updated

### ❌ SYSTEM FAILURE:
- Proceeding with unverified characters
- Not checking Bible/Characters/ for each name
- Soft-warning instead of hard halt on missing files
- Not updating on_camera_characters in frontmatter

**Master Rule:** Every named character must have a file. No file = HALT. This is non-negotiable.

---
name: 'step-02-context-loading'
description: 'Ritual Step 1 — Load all required context files for the current scene/shard'

nextStepFile: './step-03-showrunner-review.md'
contextChecklist: '../data/context-loading-checklist.md'
manifestFile: '{project-root}/.cpm/manifest.md'
sceneBriefFile: '{productionScenesPath}/Scene_{sceneNumber}/scene-brief.md'
showBibleFile: '{project-root}/Bible/Show_Bible.md'
styleGuideFile: '{project-root}/Architecture/Style_Guide.md'
vocabularyFile: '{project-root}/Architecture/Vocabulary.md'
characterPath: '{project-root}/Bible/Characters'
contractsPath: '{project-root}/Production/Contracts'
productionScenesPath: '{project-root}/Production/Scenes'
---

# Step 2: Context Loading (Ritual Step 1)

## STEP GOAL:

To load ALL required context files for Scene {sceneNumber}, Shard {shardNumber}. HALT if any required file is missing.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in Ritual Coordinator style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Ritual Coordinator** for this step
- ✅ This is a LOADING step — read files, don't generate content
- ✅ HALT on any missing required file — do not proceed with partial context

### Step-Specific Rules:

- 🎯 Focus only on loading and verifying context files
- 🚫 FORBIDDEN to generate any creative content
- 🚫 FORBIDDEN to proceed if any required file is missing
- 💬 Approach: Systematic file loading with verification checklist

## EXECUTION PROTOCOLS:

- 🎯 Load every file listed in the context checklist
- 💾 Track which files were loaded successfully
- 📖 Display loaded context confirmation
- 🛑 HALT immediately if any required file is missing

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Context Checklist

Load {contextChecklist} for reference on required files.

### 2. Load Manifest

Load {manifestFile} to determine:
- Which characters are on-camera for Scene {sceneNumber}
- Store the character list as `{onCameraCharacters}`

**HALT if manifest does not exist.**

### 2b. Load Scene Brief

Load {sceneBriefFile} to get the filmmaker-defined beats for this scene.

**HALT if file does not exist.** Display:
"**🛑 HALT — Scene Brief missing for Scene {sceneNumber}.**
`Production/Scenes/Scene_{sceneNumber}/scene-brief.md` does not exist.
Run `/cpm-scene-create` to create it before generating shards."

**IF file exists:**
- Read `shard_count` from frontmatter — note how many shards this scene has
- Read the Beats section — locate Shard {shardNumber}'s beat definition
- If Shard {shardNumber} does not exist in the beats: HALT with "Scene {sceneNumber} only has {shard_count} shards defined. Shard {shardNumber} is out of range."
- Store the beat for Shard {shardNumber} as `{currentBeat}` (Action, Character Focus, Emotional Note)

### 3. Load Bible Files

**Show Bible:**
- Load {showBibleFile}
- **HALT if file does not exist**

**On-Camera Characters:**
For EACH character in `{onCameraCharacters}`:
- Load `{characterPath}/{character_name}.md`
- **HALT if any character file does not exist**

### 4. Load Architecture Files

- Load {styleGuideFile} — **HALT if missing**
- Load {vocabularyFile} — **HALT if missing**

### 5. Load State Files (Conditional)

**IF shardNumber > 1:**
- Load `{productionScenesPath}/Scene_{sceneNumber}/state/shard_{shardNumber-1}_exit_state.md`
- **HALT if missing** — cannot generate shard without previous shard's exit state

**IF shardNumber == 1 AND sceneNumber > 1:**
- Load `{productionScenesPath}/Scene_{sceneNumber-1}/state/scene_exit_state.md`
- **HALT if missing** — cannot generate first shard without previous scene's exit state

**IF shardNumber == 1 AND sceneNumber == 1:**
- No previous state needed — this is the first shard of the production

### 6. Load Contracts

- Check {contractsPath} for any `.md` files
- Load all active contract files found
- Note: zero contracts is valid (no active narrative contracts)

### 7. Display Context Confirmation

Display:

```
✅ CONTEXT LOADED — Scene {sceneNumber}, Shard {shardNumber}

Bible:
- Show_Bible.md ✅
- Characters: {list of loaded character names} ✅

Architecture:
- Style_Guide.md ✅
- Vocabulary.md ✅

Scene Brief:
- scene-brief.md ✅ ({shard_count} shards total)
- Shard {shardNumber}: {currentBeat.Action}

State:
- {previous exit state file name or "First shard — no previous state"} ✅

Contracts:
- {count} active contract(s) loaded ✅

All required context loaded. Beginning agent reviews...
```

### 8. Auto-Proceed to Showrunner Review

**No menu needed** — Auto-proceed to {nextStepFile}.

Load, read entirely, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- All required files loaded and verified
- Missing files caused immediate HALT
- Context confirmation displayed with all items checked
- Auto-proceeded to step-03

### ❌ SYSTEM FAILURE:

- Proceeding with missing required files
- Not loading manifest first
- Not checking previous state for shard > 1
- Generating any creative content in this step
- Not displaying context confirmation

**Master Rule:** Every required file MUST be loaded and verified. Missing files = HALT. No exceptions.

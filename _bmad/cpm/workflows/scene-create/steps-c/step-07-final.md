---
name: 'step-07-final'
description: 'Scaffold Production/Scenes/Scene_{XX}/ folder, write final scene-brief.md, update manifest — scene is ready for shard-generation'

sceneBriefFile: '{project-root}/Production/Scenes/Scene_{sceneNumber}/scene-brief.md'
sceneFolderPath: '{project-root}/Production/Scenes/Scene_{sceneNumber}'
stateFolderPath: '{project-root}/Production/Scenes/Scene_{sceneNumber}/state'
manifestFile: '{project-root}/.cpm/manifest.md'
---

# Step 7: Final

## STEP GOAL:

To scaffold the complete scene folder structure, write the final scene-brief.md with all collected content, update the project manifest with the scene entry, and confirm the scene is ready for shard-generation.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Scene Architect** — completing the production scaffold
- ✅ This step is precise and prescriptive — exact file operations, no improvising
- ✅ Celebrate completion: explain what the Showrunner will read and how it's used

### Step-Specific Rules:

- 🎯 Focus on file operations — scaffolding, writing, manifest update
- 🚫 This is the final step — no next step file to load
- 💬 Confirm file creation at each step

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Confirm Finalization

"**Ready to finalize Scene {sceneNumber}.**

Here's what I'll create:
- `Production/Scenes/Scene_{sceneNumber}/scene-brief.md` — Your complete scene brief
- `Production/Scenes/Scene_{sceneNumber}/state/` — Empty folder (shard-generation populates this)
- Updated `.cpm/manifest.md` — Scene entry added

Ready to proceed?"

Wait for confirmation.

### 2. Scaffold Folder Structure

Create the scene folder structure:

1. Create `{sceneFolderPath}/` if it doesn't exist
2. Create `{stateFolderPath}/` (empty — shard-generation populates this with exit state files)

"**✅ Folder structure created:**
```
Production/Scenes/Scene_{sceneNumber}/
├── scene-brief.md       ← writing now
└── state/               ← empty (shard-generation will populate)
```"

### 3. Write Final scene-brief.md

Load the current {sceneBriefFile} (already exists from step-01 with partial content written during steps 02-06).

Write the complete final version with:

**Frontmatter (fully populated):**
```yaml
---
stepsCompleted: ['step-01-init', 'step-02-setting', 'step-03-characters', 'step-04-narrative', 'step-05-beats', 'step-06-polish', 'step-07-final']
lastStep: 'step-07-final'
created: '{creation_date_from_frontmatter}'
lastModified: '{current_date}'
scene_number: '{sceneNumber}'
scene_id: 'SCENE_{sceneNumber}'
status: not-started
shard_count: {beatCount}
on_camera_characters:
  {for each character:}
  - {characterName}
---
```

**Body (assembled from all steps):**
```markdown
# Scene {sceneNumber}: {sceneTitle}

## Setting

- **Location:** {confirmed location from step-02}
- **Time of Day:** {confirmed time from step-02}
- **Atmosphere:** {confirmed atmosphere from step-02}

## Narrative Purpose

{confirmed purpose statement from step-04}

## Emotional Arc

- **Opens at:** {opening temperature from step-04}
- **Closes at:** {closing temperature from step-04}

## Beats

### Shard 1
- **Action:** {action from step-05}
- **Character Focus:** {focus from step-05}
- **Emotional Note:** {note from step-05}

### Shard 2
...
{all beats from step-05}
```

Save to {sceneBriefFile}.

"**✅ scene-brief.md written.**"

### 4. Update Manifest

Load {manifestFile}.

Append scene entry. Find (or create) a `## Scenes` section in the manifest and append:

```markdown
## Scene {sceneNumber}

- **Title:** {sceneTitle}
- **Status:** not-started
- **On-Camera Characters:** {character1}, {character2}, ...
- **Shard Count:** {beatCount}
- **Brief:** `Production/Scenes/Scene_{sceneNumber}/scene-brief.md`
```

Save updated manifest.

"**✅ Manifest updated.**"

### 5. Completion Message

"**🎬 Scene {sceneNumber} is production-ready!**

**Files created:**
- `Production/Scenes/Scene_{sceneNumber}/scene-brief.md`
- `Production/Scenes/Scene_{sceneNumber}/state/` (empty — awaiting shards)

**Manifest updated:** `.cpm/manifest.md` now includes Scene {sceneNumber} with {beatCount} shards.

**How this scene is used in production:**

When you run `/cpm-shard-generation` and select Scene {sceneNumber}:

1. **Context Loader** reads the manifest → finds this scene entry → loads `scene-brief.md`
2. **Showrunner (Albus)** reads the beats section — knows *exactly* what happens in Shard {N} before writing a single word
3. **Script Supervisor (Jonas)** tracks entry/exit state for each shard against character files
4. **Prompt Engineer (Leonard)** compiles the final prompt from all three inputs

**The beats you wrote are the screenplay. The crew executes it.**

Scene {sceneNumber}: {sceneTitle}
{beatCount} shards | {on_camera_characters}"

### 6. Present COMPLETION MENU

Display:

"**Select an option:**

**[A] Add Another Scene** — Create Scene {sceneNumber + 1}
**[E] Edit Scene {sceneNumber}** — Modify this scene brief
**[V] Validate Scene {sceneNumber}** — Run consistency checks
**[Q] Quit** — Exit scene creation"

#### Menu Handling Logic:

- IF A: Return to workflow.md and restart create mode (load ../workflow.md, create mode)
- IF E: Load `../steps-e/step-e-01-assess.md` with {sceneBriefFile}
- IF V: Load `../steps-v/step-v-01-validate.md` with {sceneBriefFile}
- IF Q: Exit with completion message
- IF Any other: Help filmmaker, redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- state/ folder created (empty)
- scene-brief.md fully written with complete frontmatter + all sections
- Manifest updated with scene entry
- Completion message explains how the brief is used in production
- Completion menu presented

### ❌ SYSTEM FAILURE:
- Not creating state/ folder
- Writing scene-brief.md without complete frontmatter
- Forgetting to update manifest
- Not presenting completion menu with all options

**Master Rule:** The state/ folder must exist before shard-generation runs. The manifest entry must be accurate — shard_count is read by shard-generation's "next" shortcut logic.

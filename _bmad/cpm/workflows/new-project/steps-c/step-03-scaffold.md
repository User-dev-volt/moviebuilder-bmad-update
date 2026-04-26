---
name: 'step-03-scaffold'
description: 'Execute all file and folder creation operations'

nextStepFile: './step-04-completion.md'
agentTemplatesPath: '{project-root}/_bmad/cpm/templates/project/.cpm/agents'
configTemplate: '../templates/config.yaml.template'
manifestTemplate: '../templates/manifest.md.template'
placeholderTemplate: '../templates/placeholder.md.template'
---

# Step 3: Scaffold Project

## STEP GOAL:

Execute all file and folder operations to create the complete CPM project structure.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 User has already confirmed - proceed with creation
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When complete, auto-proceed to next step
- 📋 YOU ARE EXECUTING the approved plan

### Role Reinforcement:

- ✅ You are the Project Scaffolder - now building the project
- ✅ Execute file operations systematically
- ✅ Report progress as you go
- ✅ Handle errors gracefully

### Step-Specific Rules:

- 🎯 Focus ONLY on creating files and folders
- 🚫 FORBIDDEN to ask more questions - user already confirmed
- 💬 Show progress feedback during creation
- ✅ This is an ACTION step - do the work

## EXECUTION PROTOCOLS:

- 🎯 Execute operations in order (folders first, then files)
- 💾 Use templates from ../templates/ folder
- 📖 Copy agents from {agentTemplatesPath}
- ✅ Auto-proceed to completion step when done

## CONTEXT BOUNDARIES:

- User confirmed Y in step-02
- Values available: project_title, project_location, model_target
- Templates available in workflow templates folder
- Agent prompts available in CPM templates

## MANDATORY SEQUENCE

**CRITICAL:** Execute these operations in order.

### 1. Create Directory Structure

Create all folders:

```
{project_path}/
├── .cpm/
│   └── agents/
├── Bible/
│   ├── Characters/
│   └── World/
├── Architecture/
├── Production/
│   ├── Scenes/
│   └── Contracts/
└── Output/
    ├── Prompts/
    └── Renders/
```

**Progress:** "Creating directories... ✓"

### 2. Generate config.yaml

Load {configTemplate} and generate `.cpm/config.yaml`:

Replace placeholders:
- `{{project_name}}` → {project_title}
- `{{date}}` → current date
- `{{model_target}}` → {model_target}

Write to: `{project_path}/.cpm/config.yaml`

**Progress:** "Generating config.yaml... ✓"

### 3. Copy Agent Prompts

Copy from {agentTemplatesPath} to `{project_path}/.cpm/agents/`:

- `showrunner.md`
- `cinematographer.md`
- `script-supervisor.md`
- `prompt-engineer.md`

**Progress:** "Copying agent prompts... ✓"

### 4. Generate manifest.md

Load {manifestTemplate} and generate `.cpm/manifest.md`:

Replace placeholders:
- `{{project_name}}` → {project_title}
- `{{date}}` → current date
- `{{model_target}}` → {model_target}

Write to: `{project_path}/.cpm/manifest.md`

**Progress:** "Generating manifest.md... ✓"

### 5. Create Placeholder Files

Load {placeholderTemplate} and create placeholder files:

**Bible/Show_Bible.md:**
- `{{title}}` → "Show Bible"
- `{{workflow_command}}` → "/cpm-show-bible"
- `{{purpose}}` → "Defines your story, characters, world, themes, and narrative arc"

**Architecture/Style_Guide.md:**
- `{{title}}` → "Style Guide"
- `{{workflow_command}}` → "/cpm-style-guide"
- `{{purpose}}` → "Defines your visual language, lighting, color palette, and camera style"

**Architecture/Palette.md:**
- `{{title}}` → "Color Palette"
- `{{workflow_command}}` → "/cpm-style-guide"
- `{{purpose}}` → "Defines allowed and forbidden colors for visual consistency"

**Architecture/Lens_Language.md:**
- `{{title}}` → "Lens Language"
- `{{workflow_command}}` → "/cpm-style-guide"
- `{{purpose}}` → "Defines camera choices, focal lengths, and shot types"

**Architecture/Vocabulary.md:**
- `{{title}}` → "Prompt Vocabulary"
- `{{workflow_command}}` → "/cpm-style-guide"
- `{{purpose}}` → "Defines required and banned words for prompt generation"

**Progress:** "Creating placeholder files... ✓"

### 6. Create Index Files

Create index files with minimal content:

**Bible/Characters/_index.md:**
```markdown
# Characters Index

Characters will be listed here as you create them with `/cpm-character-create`.

## Characters
(none yet)
```

**Bible/World/_index.md:**
```markdown
# World Index

World-building elements will be listed here.

## Locations
(none yet)

## Rules
(none yet)
```

**Production/Slate.md:**
```markdown
# Production Slate
## {project_title}

**Status:** Pre-production
**Current Scene:** (not started)
**Last Updated:** {date}

## Production Log
(Production tracking will appear here)
```

**Progress:** "Creating index files... ✓"

### 7. Auto-Proceed to Completion

Display: "**All files created successfully!** Loading completion..."

Then immediately load, read entire file, then execute {nextStepFile}

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All 9 directories created
- config.yaml generated with correct values
- 4 agent prompts copied
- manifest.md generated
- 5 placeholder files created
- 3 index files created
- Auto-proceeded to completion step

### ❌ SYSTEM FAILURE:

- Asking for confirmation (user already confirmed)
- Stopping to wait for input (this is auto-proceed)
- Missing any files or folders
- Wrong placeholder values
- Not auto-proceeding to step-04

**Master Rule:** This is an execution step. User confirmed in step-02. Create all files and auto-proceed.

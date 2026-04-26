---
name: 'step-02-confirm-setup'
description: 'Display directory structure preview and get user confirmation'

nextStepFile: './step-03-scaffold.md'
prevStepFile: './step-01-gather-details.md'
directoryStructureRef: '../data/directory-structure.md'
---

# Step 2: Confirm Setup

## STEP GOAL:

Display the directory structure preview with user's values and get Y/N confirmation before creating files.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER proceed without explicit user confirmation
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- 📋 YOU ARE A FACILITATOR presenting the plan for approval

### Role Reinforcement:

- ✅ You are the Project Scaffolder - showing users exactly what will be created
- ✅ Be clear and transparent about what files/folders will be made
- ✅ Give users confidence to proceed or go back if needed

### Step-Specific Rules:

- 🎯 Focus ONLY on displaying preview and getting confirmation
- 🚫 FORBIDDEN to create any files yet - that's step-03
- 💬 Show the complete structure so user knows what to expect
- 🔄 If user says N, route back to step-01 to modify details

## EXECUTION PROTOCOLS:

- 🎯 Load directory structure reference for display
- 💾 User's gathered values from step-01 are available
- 📖 Present clear visual of what will be created
- 🚫 Branch based on Y/N response

## CONTEXT BOUNDARIES:

- Values from step-01: project_title, project_location, model_target
- User has seen and confirmed their input values
- Now showing what will actually be created
- This is the last checkpoint before file operations

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Display Structure Preview

"**I'll create this project structure for {project_title}:**"

```
{project_location}/{project_title}/
├── .cpm/
│   ├── config.yaml          ← Project settings (model: {model_target})
│   ├── manifest.md          ← Context index for agents
│   └── agents/
│       ├── showrunner.md         ← Story guardian
│       ├── cinematographer.md    ← Visual architect
│       ├── script-supervisor.md  ← Continuity tracker
│       └── prompt-engineer.md    ← Prompt compiler
├── Bible/
│   ├── Show_Bible.md        ← Placeholder (run /cpm-show-bible)
│   ├── Characters/
│   │   └── _index.md
│   └── World/
│       └── _index.md
├── Architecture/
│   ├── Style_Guide.md       ← Placeholder (run /cpm-style-guide)
│   ├── Palette.md           ← Placeholder
│   ├── Lens_Language.md     ← Placeholder
│   └── Vocabulary.md        ← Placeholder
├── Production/
│   ├── Slate.md             ← Production tracking
│   ├── Scenes/
│   └── Contracts/
└── Output/
    ├── Prompts/
    └── Renders/
```

### 2. Explain What Gets Created

"**What this creates:**

| Type | Count | Description |
|------|-------|-------------|
| Folders | 9 | Complete CPM directory structure |
| Agent Files | 4 | Your film crew (copied from templates) |
| Config Files | 2 | config.yaml + manifest.md |
| Placeholders | 5 | To be filled by other CPM workflows |
| Index Files | 3 | For organizing characters, world, production |

**Total:** ~14 files ready for your cinematic production."

### 3. Present MENU OPTIONS

Display: "**Proceed with creation?** [Y] Yes, create it / [N] No, go back and change details"

#### Menu Handling Logic:

- IF Y: Display "**Creating your project...**", then load, read entire file, then execute {nextStepFile}
- IF N: Display "No problem, let's adjust.", then load, read entire file, then execute {prevStepFile}
- IF Any other: Clarify that Y proceeds and N goes back, then redisplay menu

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- Y proceeds to scaffolding (step-03)
- N returns to details gathering (step-01)
- This is a branching step - route based on user choice

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Directory structure preview displayed with user's values
- Clear explanation of what will be created
- User explicitly confirms with Y before proceeding
- N correctly routes back to step-01

### ❌ SYSTEM FAILURE:

- Proceeding without explicit Y confirmation
- Creating files in this step
- Not showing the full structure preview
- Not honoring N to go back

**Master Rule:** Never create files without explicit user confirmation. This step is the gatekeeper.

---
name: 'step-04-completion'
description: 'Confirm completion and offer workflow chaining options'
---

# Step 4: Completion

## STEP GOAL:

Confirm successful project creation and offer options to continue with other CPM workflows.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR celebrating success and guiding next steps
- ✅ This is the FINAL step - workflow ends here or chains to another

### Role Reinforcement:

- ✅ You are the Project Scaffolder - congratulating the user
- ✅ Guide them to the logical next steps in the CPM workflow chain
- ✅ Be encouraging and helpful

### Step-Specific Rules:

- 🎯 Focus on confirmation and next step guidance
- 💬 Offer clear options for workflow chaining
- ✅ This is the final step - no next step file

## EXECUTION PROTOCOLS:

- 🎯 Display success confirmation
- 💾 Show what was created
- 📖 Explain recommended next steps
- ✅ Offer menu to chain to other CPM workflows or quit

## CONTEXT BOUNDARIES:

- Project has been successfully created
- All files and folders exist
- User needs guidance on what to do next
- CPM workflow chain: new-project → show-bible → style-guide → character-create → shard-generation

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Display Success Message

"**Your CPM project is ready!**

**{project_title}** has been created at:
`{project_path}/`"

### 2. Show What Was Created

"**Created:**
- ✅ 9 directories (complete CPM structure)
- ✅ 4 agent prompts (your film crew)
- ✅ 2 config files (config.yaml, manifest.md)
- ✅ 5 placeholder files (ready for content)
- ✅ 3 index files (for organizing content)"

### 3. Explain Next Steps

"**Recommended next steps:**

1. **Create your Show Bible** → `/cpm-show-bible`
   Define your story, characters, world, and themes

2. **Define your Style Guide** → `/cpm-style-guide`
   Set your visual language, colors, and camera style

3. **Add characters** → `/cpm-character-create`
   Create character state files with visual identity

4. **Start producing** → `/cpm-shard-generation`
   Generate video prompts through the Four-Agent Ritual

**Tip:** Follow this order for best results. The Show Bible informs the Style Guide, which informs character creation."

### 4. Present MENU OPTIONS

Display: "**What would you like to do next?**

**[B]** Create Show Bible now (`/cpm-show-bible`)
**[S]** Create Style Guide now (`/cpm-style-guide`)
**[H]** Create a character now (`/cpm-character-create`)
**[Q]** Quit - I'll continue later"

#### Menu Handling Logic:

- IF B: Display "Launching Show Bible workflow...", then execute `/cpm-show-bible` workflow. When finished, redisplay this menu.
- IF S: Display "Launching Style Guide workflow...", then execute `/cpm-style-guide` workflow. When finished, redisplay this menu.
- IF H: Display "Launching Character Creator...", then execute `/cpm-character-create` workflow. When finished, redisplay this menu.
- IF Q: Display farewell message and end workflow (see below)
- IF Any other: Help user understand options, then redisplay menu

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- B/S/H launch other CPM workflows, then return to this menu
- Q ends the workflow with a farewell
- User can run multiple workflows before quitting

### 5. Quit Handling

If user selects Q:

"**Your CPM project is ready at:**
`{project_path}/`

**Remember your next steps:**
1. `/cpm-show-bible` - Define your story
2. `/cpm-style-guide` - Set your visual language
3. `/cpm-character-create` - Add characters
4. `/cpm-shard-generation` - Start producing!

Happy creating! 🎬"

**End workflow.**

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Success message displayed with project path
- Summary of created files shown
- Next steps clearly explained
- Menu offers workflow chaining options
- Q properly ends with farewell
- B/S/H properly chain to other workflows

### ❌ SYSTEM FAILURE:

- Not showing what was created
- Not explaining next steps
- Menu options don't work correctly
- Q doesn't end the workflow
- Not returning to menu after chained workflow completes

**Master Rule:** This is the final step. Celebrate success, guide next steps, and offer smooth workflow chaining.

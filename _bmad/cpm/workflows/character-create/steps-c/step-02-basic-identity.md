---
name: 'step-02-basic-identity'
description: 'Establish character foundation - name, Asset ID, and status'

nextStepFile: './step-03-visual-identity.md'
characterFile: '{project-root}/Bible/Characters/{characterName}.md'
---

# Step 2: Basic Identity

## STEP GOAL:

To establish the character's basic identity including name, Asset ID (for version tracking), and status (ACTIVE/DECEASED/FLASHBACK_ONLY).

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a **Character Architect** - teaching the Asset ID version tracking system
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You explain why version tracking matters for character evolution

### Step-Specific Rules:

- 🎯 Focus only on basic identity - name, Asset ID, status
- 🚫 FORBIDDEN to gather visual details yet (that's step-03)
- 💬 Approach: Educational about CPM's version tracking system

## EXECUTION PROTOCOLS:

- 🎯 Confirm character name
- 💾 Explain and set Asset ID (NAME_V1)
- 📖 Determine status (ACTIVE/DECEASED/FLASHBACK_ONLY)
- 🚫 This is straightforward - C only menu, no A/P needed

## CONTEXT BOUNDARIES:

- Available context: Character file created in step-01, name is set
- Focus: Asset ID and status only
- Limits: Don't gather visual or behavioral details yet
- Dependencies: Character file exists from step-01

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Confirm Character Name

"**Let's establish {characterName}'s basic identity.**

**Character Name:** {characterName}

This is the name that will be used in all production documents."

### 2. Explain and Set Asset ID

"**Asset ID: Version Tracking**

CPM uses Asset IDs to track character evolution. Think of it like software versioning:

- **V1:** Initial character state
- **V2:** After major arc change or visual transformation
- **V3:** Further evolution

**Format:** `{CHARACTERNAME_UPPERCASE}_V1`

For {characterName}, the Asset ID is: **{CHARACTERNAME_UPPERCASE}_V1**

This tracks in the Version History section. When your character undergoes a major transformation (costume change, injury, arc shift), you'll create V2."

**Update character file:**
- Ensure Asset ID is set: `{CHARACTERNAME_UPPERCASE}_V1`

### 3. Determine Character Status

"**Character Status**

This determines how the character appears in your production:

**[A]CTIVE** — On-screen in the current timeline. Receives full mutable state tracking:
             outfit, inventory, physical condition, and arc position update every shard.

**[D]ECEASED** — No longer alive in the current timeline. Appears in flashback sequences
              only. State is fixed at time of death — no ongoing tracking.

**[F]LASHBACK_ONLY** — Alive, but scoped entirely to past-timeline scenes. Does not appear
                     in current-timeline shards. No current continuity tracking needed.

**What is {characterName}'s status?** → Type **A**, **D**, or **F**"

Wait for user response (A/D/F).

**Menu Handling:**
- IF A: status = "ACTIVE"
- IF D: status = "DECEASED"
- IF F: status = "FLASHBACK_ONLY"
- IF Any other: Help user, then redisplay status options

**Confirm:** "✅ Status set to: {status}"

**Update character file:**
- Set status in frontmatter: `status: '{status}'`

### 4. Append Basic Identity Section

"**Basic Identity complete!**

- **Name:** {characterName}
- **Asset ID:** {CHARACTERNAME_UPPERCASE}_V1
- **Status:** {status}

This information is now saved in your character file.

Next, we'll define {characterName}'s **Visual Identity** - the permanent features that make them visually recognizable across all shards."

**Append to {characterFile}:**

Update the Basic Identity section that already exists in the template:
```markdown
# Character: {characterName}

**Asset ID:** {CHARACTERNAME_UPPERCASE}_V1
**Status:** {status}
```

**Update frontmatter:**
- Append to stepsCompleted: `stepsCompleted: [...existing, 'step-02-basic-identity']`
- Update lastStep: `lastStep: 'step-02-basic-identity'`
- Update lastModified: `lastModified: '{current_date}'`

### 5. Present MENU OPTIONS

Display: **[C] Continue to Visual Identity**

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- User can chat or ask questions - always respond and redisplay menu

#### Menu Handling Logic:

- IF C: Save updates to {characterFile}, then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- Character name confirmed
- Asset ID explained and set correctly
- Status determined from user input
- Basic Identity section updated in character file
- stepsCompleted appended with 'step-02-basic-identity'
- Proceeded to step-03

### ❌ SYSTEM FAILURE:

- Not explaining Asset ID concept
- Skipping status determination
- Not updating character file
- Not appending to stepsCompleted
- Proceeding without user selecting 'C'

**Master Rule:** This is foundational - Asset ID tracking is critical for CPM character evolution. Explain it well.

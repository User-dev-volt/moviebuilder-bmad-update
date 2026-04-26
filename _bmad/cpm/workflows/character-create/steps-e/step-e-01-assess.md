---
name: 'step-e-01-assess'
description: 'Edit mode - load character, select section to edit, update file with version tracking'

characterFile: '{characterFilePath}'
validationWorkflow: '../steps-v/step-v-01-validate.md'
---

# Edit Step 1: Assess & Edit Character

## STEP GOAL:

To load an existing character, display current state, allow section-level editing, and update the character file with proper version tracking.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a **Character Architect** - helping users evolve their characters
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You track version changes (V1 → V2 for major transformations)

### Step-Specific Rules:

- 🎯 Focus on section-level editing
- 🚫 FORBIDDEN to recreate character - we're editing existing
- 💬 Approach: Load, display, edit, save with version tracking

## EXECUTION PROTOCOLS:

- 🎯 Load character file and display current state
- 💾 Edit selected section
- 📖 Update version if major transformation
- 🚫 This is edit mode - repeatable for multiple sections

## MANDATORY SEQUENCE

### 1. Load Character File

Load {characterFile} and read all content.

"**Loading {characterName}...**

**Current Asset ID:** {assetID}
**Status:** {status}
**Last Modified:** {lastModified}"

### 2. Display Current State

Display complete character state:
- Visual Identity (Immutable)
- Current Outfit (Mutable)
- Inventory (Mutable)
- Physical State (Mutable)
- Behavioral Profile
- Arc Position
- Version History

### 3. Section Selection Menu

"**Which section would you like to edit?**

**[1] Visual Identity** (Immutable) - Face, body, distinguishing features
**[2] Current Outfit** (Mutable) - Wardrobe update
**[3] Inventory** (Mutable) - Add/remove items
**[4] Physical State** (Mutable) - Injuries, conditions
**[5] Behavioral Profile** - Speech, tic, signature move
**[6] Arc Position** - Emotional state, want/need, progress
**[7] Status** - ACTIVE/DECEASED/FLASHBACK_ONLY
**[V] Validate** - Run consistency checks
**[Q] Quit** - Exit edit mode"

### 4. Edit Selected Section

**Based on selection:**

**IF 1 (Visual Identity):**
- Display current immutable features
- **WARNING:** "Visual Identity is immutable. Editing changes permanent features. Consider version increment (V1 → V2) if major change."
- Allow editing face/body features
- Emphasize LEFT/RIGHT specificity

**IF 2 (Current Outfit):**
- Display current outfit
- Allow editing base, condition, accessories
- No version increment needed (mutable state)

**IF 3 (Inventory):**
- Display current inventory table
- Options: Add item, Remove item, Change status
- Update inventory table
- No version increment (mutable state)

**IF 4 (Physical State):**
- Display current conditions
- Options: Add condition, Remove condition, Update severity
- Update physical state table
- No version increment (mutable state)

**IF 5 (Behavioral Profile):**
- Display current behaviors
- Allow editing speech, tic, signature move

**IF 6 (Arc Position):**
- Display current arc position
- Allow editing emotional state, want, need, progress (0-100%)

**IF 7 (Status):**
- Display current status
- Allow changing ACTIVE/DECEASED/FLASHBACK_ONLY

**IF V:** Load {validationWorkflow} and execute

**IF Q:** Exit with save confirmation

### 5. Version Tracking Decision

**IF editing Visual Identity (major change):**

"**Version Increment?**

This is a major change to immutable features.

**Current:** {current_assetID}
**Increment to:** {next_version} ?

**[Y]es** - Create new version
**[N]o** - Keep current version"

**IF Yes:**
- Increment Asset ID (V1 → V2)
- Add entry to Version History table

### 6. Save Changes

Update {characterFile}:
- Save edited section
- Update lastModified date
- Update Asset ID if incremented
- Add version history entry if applicable

"**✅ Changes saved!**

{characterName} updated successfully."

### 7. Continuation Menu

"**Continue editing?**

**[E] Edit Another Section**
**[V] Validate Character**
**[Q] Quit**"

- IF E: Return to section selection menu
- IF V: Load {validationWorkflow}
- IF Q: Exit

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

✅ **SUCCESS:** Character loaded; section edited; version tracked; file saved

❌ **FAILURE:** Not loading character; breaking immutable/mutable distinction; not tracking versions

**Master Rule:** Edit mode evolves characters. Track versions for major changes.

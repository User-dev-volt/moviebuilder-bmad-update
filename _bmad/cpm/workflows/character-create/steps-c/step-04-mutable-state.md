---
name: 'step-04-mutable-state'
description: 'Define changeable state - current outfit, inventory, and physical condition that updates per scene'

nextStepFile: './step-05-behavioral-profile.md'
characterFile: '{project-root}/Bible/Characters/{characterName}.md'
inventoryStatusData: '../data/inventory-status-options.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 4: Mutable State

## STEP GOAL:

To define the character's changeable state - current outfit, inventory, and physical condition - that will UPDATE every scene as the story progresses.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a **Character Architect** - teaching mutable state tracking
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You emphasize: mutable state changes EVERY SCENE
- ✅ Together we define the STARTING state

### Step-Specific Rules:

- 🎯 Focus ONLY on current/starting mutable state
- 🚫 FORBIDDEN to revisit immutable features (face/body - that's step-03)
- 💬 Approach: Define starting state, explain how it will update later

## EXECUTION PROTOCOLS:

- 🎯 Define current outfit, inventory, physical condition
- 💾 Explain this is the STARTING state (Scene 1 or current point in story)
- 📖 Use inventory status codes for precision
- 🚫 Mutable state will be edited frequently - keep it clear

## CONTEXT BOUNDARIES:

- Available context: Visual Identity (immutable) complete
- Focus: Current outfit, inventory items, physical condition
- Limits: This is STARTING state only
- Dependencies: Character file exists with visual identity

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Explain Mutable State

"**Now let's define {characterName}'s Mutable State - the things that CHANGE as the story progresses.**

**In step-03, we defined:**
- **Immutable:** Face features, body type (NEVER change)

**In this step, we define:**
- **Mutable:** Current outfit, inventory, physical condition (UPDATE every scene)

**Why track mutable state?**
- Script Supervisor checks continuity: "Did they have the key in the last scene? Are they still bleeding?"
- Mutable state prevents errors like: character drops key in Scene 3, but key appears again in Scene 5

**We're defining the STARTING state** - what {characterName} looks like and has RIGHT NOW (Scene 1 or current story point)."

### 2. Define Current Outfit

"**What is {characterName} wearing RIGHT NOW?**

**Think about:**
- Base clothing: jacket, shirt, pants, dress, armor?
- Condition: pristine, worn, damaged, bloodstained?
- Accessories: visible items like hat, glasses, jewelry?

**Describe {characterName}'s current outfit...**"

**Engage in conversational exploration:**
- Follow-up for details
- Note condition (pristine vs. damaged matters for continuity)
- Clarify visible vs. hidden accessories

**Formalize into:**
- **Base:** {main clothing items}
- **Condition:** {any damage, stains, wear}
- **Accessories:** {visible items}

### 3. Define Inventory

"**What items does {characterName} currently possess?**

**Important: Items must be explicitly tracked.**
- If it's not in inventory, they don't have it
- If they acquire something in Scene 3, we ADD it to inventory
- If they drop something in Scene 5, we REMOVE it from inventory

**For each item, we track:**
- Item name
- **Status code** (where it is)
- When acquired
- Notes (if relevant)

**Does {characterName} have any items to start with?** (weapons, tools, personal items, quest items)"

**IF user lists items:**

Load {inventoryStatusData} for status code reference.

**For each item, determine status:**
- **EQUIPPED_PRIMARY_HAND** - Actively holding (right hand)
- **EQUIPPED_SECONDARY_HAND** - Actively holding (left hand)
- **HOLSTERED** - On belt/hip, quick access
- **POCKET** - In pockets
- **BACKPACK** - In bag/pack
- **HIDDEN** - Concealed on person

**Example dialogue:**
- User: "They have a revolver"
- You: "Where is the revolver? Equipped in hand, holstered, or in a pocket?"
- User: "Holstered"
- You: "Perfect. And when did they get it?"
- User: "Scene 1 - it's their starting equipment"

**Build inventory table:**
```
| Item | Status | Acquired | Notes |
|------|--------|----------|-------|
| Revolver | HOLSTERED | Scene 1 | Starting equipment |
```

**IF user says "no items":**

"Got it. {characterName} starts with no inventory items. As they acquire items in future scenes, we'll update this table."

**Inventory table:**
```
| Item | Status | Acquired | Notes |
|------|--------|----------|-------|
| (none) |        |          |       |
```

### 4. Define Physical State

"**Any injuries, conditions, or physical states to track?**

**Examples:**
- Injuries: bleeding, broken bone, bruise
- Conditions: exhaustion, poisoned, sick
- Physical states: pregnant, elderly, recovering

**For each condition, we track:**
- Condition name
- Location (which body part)
- Severity (Permanent/Temporary/Active)
- Since when (which scene)

**Does {characterName} have any physical conditions to track?**"

**IF user lists conditions:**

**For each condition, gather details:**
- What: injury/condition name
- Where: body location
- Severity: Permanent (scars, lost limb), Temporary (healing wound), Active (currently bleeding)
- Since: which scene

**Build physical state table:**
```
| Condition | Location | Severity | Since |
|-----------|----------|----------|-------|
| Bullet wound (healing) | Right shoulder | Temporary | Scene 8 |
```

**IF user says "no conditions":**

"Got it. {characterName} starts healthy with no physical conditions. We'll track any injuries or conditions as they occur."

**Physical state table:**
```
| Condition | Location | Severity | Since |
|-----------|----------|----------|-------|
| (none) |          |          |       |
```

### 5. Emphasize Mutable State Updates

"**Remember: Mutable state gets updated EVERY SCENE.**

**When you run shard generation:**
- Script Supervisor loads this character file
- Checks current outfit, inventory, physical state
- After the scene, **EXIT STATE is captured**
- This file gets updated with changes

**Example:**
- Before Scene 3: No key in inventory
- Scene 3 action: {characterName} picks up a rusty key
- After Scene 3: Key added to inventory with status POCKET

This is how CPM maintains continuity - external state tracking."

### 6. Append Mutable State Sections

**Update {characterFile}:**

Append the three mutable state sections:

```markdown
## Current Outfit (Mutable - Update Per Scene)

- **Base:** {base clothing}
- **Condition:** {condition}
- **Accessories:** {accessories}

## Inventory (Mutable)

{inventory table}

## Physical State (Mutable)

{physical state table}
```

**Update frontmatter:**
- Append to stepsCompleted: `['...existing', 'step-04-mutable-state']`
- Update lastStep: `'step-04-mutable-state'`
- Update lastModified: `'{current_date}'`

"**✅ Mutable State complete!**

We've defined {characterName}'s starting state:
- Current outfit
- Starting inventory
- Physical condition

Next, we'll define {characterName}'s **Behavioral Profile** - how they speak and act."

### 7. Present MENU OPTIONS

Display: **Select:** [A] Advanced Elicitation [P] Party Mode [C] Continue

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask}, and when finished redisplay the menu
- IF P: Execute {partyModeWorkflow}, and when finished redisplay the menu
- IF C: Save updates to {characterFile}, then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- Mutable state concept explained clearly
- Current outfit defined with condition
- Inventory items tracked with status codes
- Physical conditions documented with severity
- User understands mutable state updates every scene
- Three mutable sections appended to character file
- stepsCompleted updated

### ❌ SYSTEM FAILURE:

- Not explaining mutable vs. immutable distinction
- Missing inventory status codes
- Not tracking physical condition location/severity
- Confusing starting state with immutable features
- Not explaining how state updates in production

**Master Rule:** Mutable state is the CORE of CPM continuity tracking. Explain it well. Use status codes for precision.

---
name: 'step-05-world'
description: 'Establish world rules - physics, society, technology'

nextStepFile: './step-06-arc.md'
outputFile: 'Bible/Show_Bible.md'
---

# Step 5: World Rules

## STEP GOAL:

To establish the rules that govern the story's world - physics, society, and technology.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator

### Role Reinforcement:

- ✅ You are the **Story Architect** - helping define the LAWS of this universe
- ✅ Consistency is key - rules must be enforceable
- ✅ The Showrunner agent will enforce these rules across all shards
- ✅ What's established here becomes CANON

### Step-Specific Rules:

- 🎯 Focus on rules that affect storytelling
- 🚫 FORBIDDEN to create rules for them - draw out their vision
- 💬 Approach each category separately - don't overwhelm

## EXECUTION PROTOCOLS:

- 🎯 Guide through world-building in three categories
- 💾 Save to {outputFile} before proceeding
- 📖 Update stepsCompleted before loading next step
- ⏸️ ALWAYS halt at menu and wait for user input

## MANDATORY SEQUENCE

### 1. Introduce World Rules

Display:
"**What rules govern your world?**

This is where we define what's possible and impossible. These become the laws the Showrunner enforces.

We'll cover three areas:
- **Physics** - What's possible/impossible? Any supernatural or sci-fi elements?
- **Society** - How is power structured? What are the norms?
- **Technology** - What tech exists? What are its limits?

Let's start with **Physics**..."

### 2. Explore Physics

Display:
"**Physics Rules:**

What's physically possible in your world? Are there supernatural elements? Sci-fi tech that bends normal rules?

For example:
- *'Magic exists but costs the user their memories'*
- *'FTL travel is possible but time passes differently'*
- *'The dead can return, but only for 24 hours'*

What physical rules or exceptions exist in your world?"

Listen and help them articulate. Then move to Society.

### 3. Explore Society

Display:
"**Society Rules:**

How is your world organized? Who has power? What are the unwritten rules people live by?

Consider:
- *'Corporations have replaced governments'*
- *'Class is determined by genetic modification level'*
- *'Violence is ritualized and publicly broadcast'*

What social structures shape your world?"

Listen and help them articulate. Then move to Technology.

### 4. Explore Technology

Display:
"**Technology Rules:**

What technology exists? What can it do? What are its limitations?

Consider:
- *'AI exists but is legally required to be distinguishable from humans'*
- *'Memory transfer is possible but illegal'*
- *'Communication is instant but monitored'*

What tech shapes your world and what are its limits?"

### 5. Confirm World Rules

Once all three areas are defined:

Display:
"**Your World Rules:**

**Physics:**
{their physics rules}

**Society:**
{their society rules}

**Technology:**
{their technology rules}

These are the constitutional laws of your universe. The Showrunner will flag any scene that violates them.

**Select:** [A] Refine Further [P] Get Other Perspectives [C] Continue to Story Arc"

### 6. Present MENU OPTIONS

Display: "**Select:** [A] Refine Further [P] Get Other Perspectives [C] Continue"

#### Menu Handling Logic:

- IF A: "Which area needs work? Physics? Society? Technology?" → Facilitate → Redisplay menu
- IF P: Suggest implications or edge cases of their rules → Redisplay menu
- IF C: Save to {outputFile}, update frontmatter, then load {nextStepFile}
- IF Any other: Help user respond, then redisplay menu

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

### 7. Save and Proceed (On 'C')

1. Update {outputFile} - replace the World Rules section (all three subsections)
2. Update frontmatter: append `'step-05-world'` to `stepsCompleted`
3. Load, read entire file, then execute {nextStepFile}

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Explored all three categories (Physics, Society, Technology)
- Rules are specific and enforceable
- User defined THEIR world
- Saved complete World Rules section
- Updated stepsCompleted

### ❌ SYSTEM FAILURE:

- Skipping categories
- Rules too vague to enforce
- Creating rules for them
- Not saving all three sections

**Master Rule:** World rules are laws. They must be clear enough to enforce.

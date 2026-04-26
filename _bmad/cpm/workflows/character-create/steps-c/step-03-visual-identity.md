---
name: 'step-03-visual-identity'
description: 'Define immutable visual features with LEFT/RIGHT specificity - the core CPM continuity mechanism'

nextStepFile: './step-04-mutable-state.md'
characterFile: '{project-root}/Bible/Characters/{characterName}.md'
distinguishingFeaturesData: '../data/distinguishing-features-reference.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 3: Visual Identity (Immutable)

## STEP GOAL:

To define the character's permanent visual features with LEFT/RIGHT specificity - the immutable identity that will NEVER change and ensures AI can render the character consistently across all shards.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a **Character Architect** - teaching the immutable vs. mutable distinction
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You emphasize LEFT/RIGHT precision - this is CRITICAL for CPM continuity
- ✅ Together we explore visual concepts and formalize them into structured state

### Step-Specific Rules:

- 🎯 Focus ONLY on permanent, immutable visual features
- 🚫 FORBIDDEN to discuss outfit, inventory, or changeable state (that's step-04)
- 💬 Approach: Explore → Discuss → Formalize → Review (NOT form-filling)
- 🔴 **CRITICAL:** Emphasize LEFT/RIGHT specificity for distinguishing features

## EXECUTION PROTOCOLS:

- 🎯 Teach immutable vs. mutable distinction
- 💾 Emphasize LEFT/RIGHT precision (scar on LEFT cheek, not just "scar on cheek")
- 📖 Collaborative exploration, not form-filling
- 🚫 This step is CRITICAL - takes time, uses Party Mode and Advanced Elicitation

## CONTEXT BOUNDARIES:

- Available context: Basic Identity complete (name, Asset ID, status)
- Focus: Face, body, permanent distinguishing features
- Limits: NO outfit, inventory, or mutable state yet
- Dependencies: Character file exists with basic identity

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Teach Immutable vs. Mutable Distinction

"**Now let's define {characterName}'s Visual Identity - the features that will NEVER change.**

**This is the most important concept in CPM:**

**IMMUTABLE (permanent):**
- Face features: scar on LEFT cheek, blue eyes, crooked nose
- Body type: athletic build, 6'2" tall
- Movement style: confident stride
- **These NEVER change** (unless the story explicitly changes them)

**MUTABLE (changeable):**
- Current outfit: leather jacket (changes per scene)
- Inventory: carrying a key (acquired in Scene 3)
- Physical condition: bleeding from right arm (from Scene 8)
- **These UPDATE every scene**

**Why this matters:** AI video generators are stateless. They forget. The immutable features are your character's visual anchor - the Script Supervisor checks these FIRST to ensure continuity.

**Ready to define {characterName}'s permanent visual identity?**"

Wait for user acknowledgment.

### 2. Explore Face Features

"**Let's start with {characterName}'s face - the features that make them instantly recognizable.**

**Think about:**
- What makes this face unique?
- Any distinguishing marks? (scars, birthmarks, tattoos)
- Default expression? (how they usually look)
- How old do they appear?

**Tell me about {characterName}'s face...**"

**Engage in conversational exploration:**
- Ask follow-up questions
- Probe for specificity
- **CRITICAL:** If they mention distinguishing features, ask for LEFT/RIGHT location
- Load {distinguishingFeaturesData} for reference if needed

**Example dialogue:**
- User: "They have a scar from a knife fight"
- You: "Where exactly is this scar? Left cheek, right cheek, forehead? And how long - small nick or runs across the whole cheek?"
- User: "Left cheek, about 2 inches"
- You: "Perfect! 'Scar on LEFT cheek, 2 inches, from knife fight.' This specificity is what keeps continuity."

**Formalize into:**
- **Distinguishing Features:** [with LEFT/RIGHT specificity]
- **Expression Default:** [how they usually look]
- **Age Appearance:** [how old they appear]

### 3. Explore Body and Movement

"**Now let's define {characterName}'s body and how they move.**

**Think about:**
- Build: athletic, slim, heavy, muscular?
- Posture: confident, hunched, rigid, relaxed?
- Movement style: graceful, deliberate, nervous, energetic?

**How would you describe {characterName}'s physical presence?**"

**Engage in conversational exploration:**
- Follow-up questions for clarity
- Help user visualize the character
- Formalize responses into structured format

**Formalize into:**
- **Build:** [body type]
- **Posture:** [how they carry themselves]
- **Movement Style:** [how they move]

### 4. Emphasize Distinguishing Features in Prompts

"**One more critical thing about distinguishing features:**

In AI video generation, **distinguishing features go in the FIRST 25% of every prompt.**

Why? Because AI attention degrades through the prompt. If you bury '{characterName} has a scar on LEFT cheek' at the end, the AI will miss it.

**Prompt structure for {characterName}:**
1. Name + distinguishing features FIRST
2. Then body type, posture, movement
3. Then scene-specific details

This is how the Prompt Engineer will structure every shard."

### 5. Review and Confirm

"**Let me summarize {characterName}'s Visual Identity (Immutable):**

**Face:**
- Distinguishing Features: {features with LEFT/RIGHT specificity}
- Expression Default: {expression}
- Age Appearance: {age}

**Body:**
- Build: {build}
- Posture: {posture}
- Movement Style: {movement}

**Does this capture {characterName}'s permanent visual identity?**

Would you like to:
- **[R]efine** - Adjust any details
- **[C]onfirm** - Lock in this identity and continue"

**Menu Handling:**
- IF R: Return to relevant section for refinement
- IF C: Proceed to append section
- IF Any other: Help user, then redisplay menu

### 6. Append Visual Identity Section

**Update {characterFile}:**

Append to the Visual Identity section:
```markdown
## Visual Identity (Immutable Unless Story Changes)

### Face
- **Distinguishing Features:** {features}
- **Expression Default:** {expression}
- **Age Appearance:** {age}

### Body
- **Build:** {build}
- **Posture:** {posture}
- **Movement Style:** {movement}
```

**Update frontmatter:**
- Append to stepsCompleted: `['...existing', 'step-03-visual-identity']`
- Update lastStep: `'step-03-visual-identity'`
- Update lastModified: `'{current_date}'`

"**✅ Visual Identity (Immutable) complete!**

This is {characterName}'s permanent identity. The Script Supervisor will verify these features in EVERY shard.

Next, we'll define the **Mutable State** - outfit, inventory, and physical condition that changes per scene."

### 7. Present MENU OPTIONS

Display: **Select:** [A] Advanced Elicitation [P] Party Mode [C] Continue

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask}, and when finished redisplay the menu
- IF P: Execute {partyModeWorkflow}, and when finished redisplay the menu
- IF C: Save updates to {characterFile}, then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- Immutable vs. mutable distinction taught clearly
- LEFT/RIGHT specificity emphasized and enforced
- Face features captured with precise distinguishing marks
- Body and movement defined
- Collaborative exploration (NOT form-filling)
- Visual Identity section appended to character file
- stepsCompleted updated
- User understands why this matters for continuity

### ❌ SYSTEM FAILURE:

- Form-filling instead of collaborative exploration
- Allowing "scar on cheek" without LEFT/RIGHT specificity
- Not emphasizing distinguishing features in first 25% of prompts
- Rushing through this critical step
- Not using Party Mode/Advanced Elicitation when valuable
- Skipping immutable vs. mutable teaching

**Master Rule:** This is the MOST CRITICAL step for CPM continuity. Take time. Emphasize LEFT/RIGHT precision. Use collaborative facilitation.

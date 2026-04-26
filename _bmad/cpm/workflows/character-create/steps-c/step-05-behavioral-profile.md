---
name: 'step-05-behavioral-profile'
description: 'Define character behaviors for Prompt Engineer - speech pattern, nervous tic, signature move'

nextStepFile: './step-06-arc-position.md'
characterFile: '{project-root}/Bible/Characters/{characterName}.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 5: Behavioral Profile

## STEP GOAL:

To define {characterName}'s behavioral traits - speech pattern, nervous tic, and signature move - that help the Prompt Engineer capture character essence in AI video generation.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a **Character Architect** - exploring character quirks and behavioral essence
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You help users discover unique behaviors that make characters memorable

### Step-Specific Rules:

- 🎯 Focus on observable behaviors - how they speak and act
- 🚫 FORBIDDEN to revisit visual or mutable state
- 💬 Approach: Creative exploration of character quirks

## EXECUTION PROTOCOLS:

- 🎯 Explore speech pattern, nervous tic, signature move
- 💾 These are for Prompt Engineer to capture character essence
- 📖 Make behaviors specific and actionable for prompting

## MANDATORY SEQUENCE

### 1. Explain Behavioral Profile

"**Now let's define how {characterName} behaves.**

**This section helps the Prompt Engineer capture {characterName}'s essence:**
- How they speak
- What they do when stressed
- Their signature action

**These aren't just character notes - they become prompting instructions.**"

### 2. Define Speech Pattern

"**How does {characterName} speak?**

**Examples:**
- Short, clipped sentences (military background)
- Formal, verbose (academic)
- Uses slang and contractions (street-smart)
- Soft-spoken, hesitant (shy)
- Commands, no questions (authoritative)

**What's {characterName}'s speech pattern?**"

Formalize: **Speech Pattern:** {pattern}

### 3. Define Nervous Tic

"**What does {characterName} do when stressed or lying?**

**Examples:**
- Touches scar on LEFT cheek
- Fidgets with wedding ring
- Avoids eye contact
- Clenches jaw
- Laughs inappropriately

**What's {characterName}'s nervous tic?**"

Formalize: **Nervous Tic:** {tic}

### 4. Define Signature Move

"**What's {characterName}'s signature action - the thing they do that defines them?**

**Examples:**
- Always checks exits when entering a room
- Spins revolver before holstering
- Adjusts glasses before speaking
- Crosses arms when challenged

**What's {characterName}'s signature move?**"

Formalize: **Signature Move:** {move}

### 5. Append Behavioral Profile

Update {characterFile}:

```markdown
## Behavioral Profile (For Prompt Engineer)

- **Speech Pattern:** {speech}
- **Nervous Tic:** {tic}
- **Signature Move:** {move}
```

Update frontmatter: Append 'step-05-behavioral-profile' to stepsCompleted

"**✅ Behavioral Profile complete!**

Next: **Arc Position** - where {characterName} is in their journey."

### 6. Present MENU OPTIONS

Display: **Select:** [A] Advanced Elicitation [P] Party Mode [C] Continue

- IF A: Execute {advancedElicitationTask}, redisplay menu
- IF P: Execute {partyModeWorkflow}, redisplay menu
- IF C: Save to {characterFile}, load {nextStepFile}
- IF Any other: help user, redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

✅ **SUCCESS:** Speech, tic, move defined; Behavioral Profile appended; stepsCompleted updated

❌ **FAILURE:** Form-filling; not exploring creatively; vague behaviors

**Master Rule:** Behaviors must be specific and actionable for prompting.

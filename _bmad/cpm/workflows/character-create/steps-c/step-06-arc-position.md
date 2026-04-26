---
name: 'step-06-arc-position'
description: 'Define character journey - emotional state, want vs. need, arc progress'

nextStepFile: './step-07-polish.md'
characterFile: '{project-root}/Bible/Characters/{characterName}.md'
arcFrameworksData: '../data/arc-position-frameworks.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 6: Arc Position

## STEP GOAL:

To define where {characterName} is in their character journey - emotional state, want vs. need, and arc progress.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a **Character Architect** - exploring character transformation
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You help users understand want vs. need distinction

### Step-Specific Rules:

- 🎯 Focus on character journey and transformation
- 🚫 FORBIDDEN to revisit visual, mutable, or behavioral details
- 💬 Approach: Explore emotional state and arc trajectory

## EXECUTION PROTOCOLS:

- 🎯 Define emotional state, want, need, arc progress
- 💾 Arc progress is 0-100% (0 = start, 100 = transformed)
- 📖 Want vs. need often differ - that's the arc

## MANDATORY SEQUENCE

### 1. Explain Arc Position

"**Arc Position tracks {characterName}'s transformation journey.**

**Showrunner uses this to ensure:**
- Character actions are motivated by arc
- Transformation feels earned, not sudden
- Emotional state matches story point

**We'll define:**
- Current emotional state
- Want (what they pursue)
- Need (what they actually need - often different!)
- Arc progress (0-100%)"

### 2. Define Current Emotional State

"**Where is {characterName} emotionally RIGHT NOW?**

**Examples:** desperate, hopeful, broken, confident, vengeful, lost, determined, fearful

**What's {characterName}'s current emotional state?**"

Formalize: **Current Emotional State:** {state}

### 3. Define Want vs. Need

"**Character Want vs. Need - the engine of transformation:**

**WANT:** What {characterName} is actively pursuing (conscious goal)
**NEED:** What {characterName} actually needs (often unconscious)

**Examples:**
- **Want:** Revenge on the person who killed their partner
- **Need:** To learn forgiveness and move on

**OR:**
- **Want:** Prove they're the best detective
- **Need:** To accept they can't save everyone

**What does {characterName} WANT? (conscious goal)**"

Wait for response.

"**What does {characterName} actually NEED? (often different from want)**"

Wait for response.

Formalize:
- **Character Want:** {want}
- **Character Need:** {need}

### 4. Define Arc Progress

"**Arc Progress: 0-100%**

**Where is {characterName} in their transformation?**
- **0-25%:** Beginning - hasn't realized need yet
- **26-50%:** Awareness - starting to see the truth
- **51-75%:** Struggle - resisting change
- **76-100%:** Transformation - embracing need

**What's {characterName}'s arc progress?** (0-100)"

Validate: Must be 0-100

Formalize: **Arc Progress:** {progress}%

### 5. Append Arc Position

Update {characterFile}:

```markdown
## Arc Position

- **Current Emotional State:** {emotional_state}
- **Character Want:** {want}
- **Character Need:** {need}
- **Arc Progress:** {progress}%
```

Update frontmatter: Append 'step-06-arc-position' to stepsCompleted

"**✅ Arc Position complete!**

Next: **Polish** - cross-section consistency check."

### 6. Present MENU OPTIONS

Display: **Select:** [A] Advanced Elicitation [P] Party Mode [C] Continue

- IF A: Execute {advancedElicitationTask}, redisplay menu
- IF P: Execute {partyModeWorkflow}, redisplay menu
- IF C: Save to {characterFile}, load {nextStepFile}
- IF Any other: help user, redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

✅ **SUCCESS:** Emotional state, want, need, progress defined; Arc Position appended; stepsCompleted updated

❌ **FAILURE:** Not explaining want vs. need; arc progress outside 0-100%; vague emotional state

**Master Rule:** Want vs. need distinction drives character transformation.

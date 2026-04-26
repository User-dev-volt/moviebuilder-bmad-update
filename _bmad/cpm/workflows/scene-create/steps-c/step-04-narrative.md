---
name: 'step-04-narrative'
description: 'Define scene narrative purpose and emotional arc — linked to Show Bible themes if available'

nextStepFile: './step-05-beats.md'
sceneBriefFile: '{project-root}/Production/Scenes/Scene_{sceneNumber}/scene-brief.md'
sceneStructureReference: '../data/scene-structure-reference.md'
showBibleFile: '{project-root}/Bible/Show_Bible.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 4: Narrative

## STEP GOAL:

To define what this scene accomplishes in the story — its narrative purpose — and the emotional arc it travels, from opening temperature to closing temperature. This gives the Showrunner the "why" behind every beat.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Scene Architect** — helping filmmakers articulate WHY this scene exists
- ✅ Load scene-structure-reference.md to help filmmakers who aren't sure how to frame narrative function
- ✅ If Show Bible was loaded in step-01, use its thematic pillars as reference points here

### Step-Specific Rules:

- 🎯 Focus on narrative purpose and emotional arc — two things only
- 🚫 FORBIDDEN to generate beats or setting details
- 💬 Approach: "What changes because this scene exists?" is the core question
- 🎯 Emotional arc = where it opens, where it closes. Not plot — temperature.

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Scene Structure Reference

Load {sceneStructureReference} for reference during facilitation.

Use the scene types table and emotional arc patterns internally — reference them when filmmaker seems stuck.

### 2. Show Bible Linkage (If Available)

**IF Show Bible was loaded in step-01 (or load {showBibleFile} now if it exists):**

Briefly surface the relevant context:

"Your Show Bible has these thematic pillars: {list themes}. We'll come back to these when we discuss what this scene serves."

**IF no Show Bible:** Skip this note.

### 3. Ask for Narrative Purpose

"**What does this scene accomplish?**

Every scene should change something — a relationship, a character's understanding, the stakes, what the audience knows. What changes because Scene {sceneNumber} exists?

Don't worry about phrasing it perfectly. Just tell me what this scene does."

Wait for response. Listen for: what shifts, whose story it serves, what information is revealed or withheld.

**If filmmaker is stuck**, offer a prompt from the scene types:

"Here are some ways to think about it:
- Is this an **arrival** — someone entering a new situation?
- A **confrontation** — two forces meeting?
- A **revelation** — something hidden becoming known?
- An **intimate moment** — two characters sharing something private?

Which feels closest?"

### 4. Distill to One or Two Sentences

Help filmmaker sharpen their narrative purpose statement to 1-2 sentences. It should answer: "Why does this scene exist in the story?"

"Let me see if I can distill that:

*{distilled version}*

Does that capture it? What should I adjust?"

Revise until filmmaker approves.

### 5. Define the Emotional Arc

"**Now let's map the emotional journey.**

A scene opens at one emotional temperature and closes at a different one. The beats are the path between them.

**Where does Scene {sceneNumber} open?** What's the emotional state when we first cut in?

And **where does it close?** What's the temperature when we cut out?"

Listen for emotional descriptors. These should be atmospheric, not psychological:
- Good: "cautious optimism", "brittle formality", "unspoken grief", "held breath"
- Too clinical: "Elias is angry" (that's a character state, not a scene temperature)

Guide toward two descriptors: opens at _____, closes at _____.

**If the open and close feel the same**, probe:

"If the scene opens and closes at the same temperature, is it a transition scene — moving story position without an arc? Or is there a shift you haven't named yet?"

### 6. Link to Show Bible (If Available)

**IF Show Bible exists:**

"**Thematic check:** Which of your Show Bible's pillars does this scene serve?

{list thematic pillars from Show Bible}

You don't need to serve all of them — one is enough. Which one does Scene {sceneNumber} carry?"

Document the thematic connection.

**IF no Show Bible:** Skip.

### 7. Formalize and Confirm

"**Here's the narrative section:**

**Narrative Purpose:**
{1-2 sentence purpose statement}

**Emotional Arc:**
- Opens at: {opening temperature}
- Closes at: {closing temperature}
{If Show Bible: **Serves theme:** {theme}}

Does this look right?"

Wait for confirmation. Adjust if needed.

### 8. Save to Scene Brief

Append to {sceneBriefFile} (update Narrative Purpose and Emotional Arc sections):

```markdown
## Narrative Purpose

{confirmed purpose statement}

## Emotional Arc

- **Opens at:** {opening temperature}
- **Closes at:** {closing temperature}
```

Update frontmatter:
- Append 'step-04-narrative' to stepsCompleted
- Set lastStep: 'step-04-narrative'
- Set lastModified: '{current_date}'

"**✅ Narrative saved.**"

### 9. Present MENU OPTIONS

Display: **Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask}, then redisplay menu
- IF P: Execute {partyModeWorkflow}, then redisplay menu
- IF C: Load, read entirely, then execute {nextStepFile}
- IF Any other: Help user, redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- Narrative purpose is 1-2 sentences, answers "why does this scene exist"
- Emotional arc has two distinct temperatures (open ≠ close, or intentionally transitional)
- Filmmaker confirmed before saving
- Saved to scene-brief.md with stepsCompleted updated

### ❌ SYSTEM FAILURE:
- Accepting "it's important" as narrative purpose
- Not probing when open and close temperature feel identical
- Generating purpose statement without filmmaker input
- Not updating stepsCompleted

**Master Rule:** "What changes?" is the question. If nothing changes, probe until it does or filmmaker accepts a transitional scene.

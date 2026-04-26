---
name: 'step-02-setting'
description: 'Collaboratively explore and define the scene setting — location, time of day, atmosphere'

nextStepFile: './step-03-characters.md'
sceneBriefFile: '{project-root}/Production/Scenes/Scene_{sceneNumber}/scene-brief.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 2: Setting

## STEP GOAL:

To collaboratively explore and define where and when this scene takes place — with enough specificity that the Cinematographer can make visual decisions and the Prompt Engineer can anchor the environment.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Scene Architect** — helping filmmakers see their location before they define their beats
- ✅ Setting is not decoration — it's a character. The kitchen's clutter tells us who Mara is.
- ✅ Collaborative dialogue: explore first, formalize second

### Step-Specific Rules:

- 🎯 Focus on location, time, atmosphere — three things only
- 🚫 FORBIDDEN to gather characters or beats yet
- 💬 Approach: Start with "Where are we?" — let filmmaker paint the picture, then distill
- 🎯 Atmosphere is the visual + sensory texture — light quality, sounds, smells, emotional weight of the space

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Open the Location

Start with an open invitation:

"**Let's establish your scene.**

Where does this scene take place? Don't worry about being precise yet — just paint the picture. Where are we?"

Wait for filmmaker's response. Listen for: specific location, mood cues, any visual details they mention.

### 2. Deepen the Location

Follow up on what they've given you:

- If vague ("a room"): "Which room? Whose room? What does it tell us about the person who lives here?"
- If a familiar space: "Is this the first time we're seeing it, or do we know it already?"
- If exterior: "What's the scale? Are they dwarfed by it or does it feel contained?"

Guide toward a **specific, named location** within the production's world.

### 3. Establish Time of Day

"**When does this scene happen?**

Time of day changes everything — morning light is honest, late afternoon is golden and a little melancholy, night compresses the frame. When are we?"

Listen for: explicit time, mood cues that imply time, references to what came before/after.

Distill to a specific answer: morning / midday / golden hour / late afternoon / dusk / night / pre-dawn.

### 4. Define Atmosphere

"**What's the texture of this space?**

Not the plot — the feeling. What does the air feel like? Is it quiet or full of ambient sound? Is the light warm or cold? What's the emotional weight of the room itself?"

This is about the environmental conditions that the Cinematographer and Prompt Engineer will render:
- Light quality (harsh overhead, soft diffused, single-source rim)
- Sound texture (silence, ambient, score-heavy)
- Environmental details that carry meaning

Listen and distill to 1-3 specific atmospheric descriptors.

### 5. Formalize and Confirm

Reflect back what you've heard in the structured format:

"**Here's the setting as I've understood it:**

- **Location:** {specific location}
- **Time of Day:** {time}
- **Atmosphere:** {descriptors}

Does this capture it? Anything to adjust?"

Wait for confirmation or adjustments. Revise until filmmaker approves.

### 6. Save to Scene Brief

Append to {sceneBriefFile} (update the Setting section):

```markdown
## Setting

- **Location:** {confirmed location}
- **Time of Day:** {confirmed time}
- **Atmosphere:** {confirmed atmosphere}
```

Also update frontmatter:
- Append 'step-02-setting' to stepsCompleted
- Set lastStep: 'step-02-setting'
- Set lastModified: '{current_date}'

"**✅ Setting saved.**"

### 7. Present MENU OPTIONS

Display: **Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C'

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask}, then redisplay menu
- IF P: Execute {partyModeWorkflow}, then redisplay menu
- IF C: Load, read entirely, then execute {nextStepFile}
- IF Any other: Help user, redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- Location is specific and named (not "a room")
- Time of day is defined
- Atmosphere has 1-3 concrete descriptors
- Filmmaker confirmed before saving
- Setting saved to scene-brief.md with stepsCompleted updated

### ❌ SYSTEM FAILURE:
- Accepting "a room" or "somewhere" as location
- Skipping confirmation step
- Generating atmospheric descriptors without filmmaker input
- Forgetting to update stepsCompleted in frontmatter

**Master Rule:** Explore → Discuss → Formalize → Confirm. Never fill in blanks without the filmmaker.

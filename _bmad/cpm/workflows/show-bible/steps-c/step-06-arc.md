---
name: 'step-06-arc'
description: 'Map the three-act story structure'

nextStepFile: './step-07-motifs.md'
outputFile: 'Bible/Show_Bible.md'
---

# Step 6: Story Arc

## STEP GOAL:

To map the high-level three-act structure of the story.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator

### Role Reinforcement:

- ✅ You are the **Story Architect** - helping shape the journey
- ✅ This is high-level structure, not detailed beats
- ✅ The arc should serve the themes established earlier
- ✅ Help them see the whole before the parts

### Step-Specific Rules:

- 🎯 Focus on the three-act macro structure
- 🚫 FORBIDDEN to outline the plot for them
- 💬 Approach each act separately

## EXECUTION PROTOCOLS:

- 🎯 Guide through act-by-act structure
- 💾 Save to {outputFile} before proceeding
- 📖 Update stepsCompleted before loading next step
- ⏸️ ALWAYS halt at menu and wait for user input

## MANDATORY SEQUENCE

### 1. Introduce Story Arc

Display:
"**What's the high-level story structure?**

We're mapping the journey - not every scene, but the major movements. Think of it as the shape of your story.

We'll work through three acts:
- **Act I** - Setup: World, protagonist, inciting incident
- **Act II** - Confrontation: Obstacles, stakes, midpoint shift
- **Act III** - Resolution: Climax, resolution, final image

Let's start with **Act I**..."

### 2. Explore Act I

Display:
"**Act I: Setup**

This is where we meet the world and the protagonist before everything changes.

- What's the world like at the start?
- Who is your protagonist and what's their normal?
- What's the inciting incident that disrupts everything?

Walk me through your Act I..."

Listen and help them articulate the setup, protagonist, and inciting incident.

### 3. Explore Act II

Display:
"**Act II: Confrontation**

This is the longest act - the struggle, complications, rising stakes.

- What obstacles does the protagonist face?
- What's at stake if they fail?
- What's the midpoint shift that changes everything?

Walk me through your Act II..."

Listen and help them articulate obstacles, stakes, and the midpoint turn.

### 4. Explore Act III

Display:
"**Act III: Resolution**

This is the final push - climax, confrontation, aftermath.

- How does it build to climax?
- What's resolved (and what isn't)?
- What's the final image we're left with?

Walk me through your Act III..."

Listen and help them articulate climax, resolution, and final image.

### 5. Confirm Story Arc

Once all three acts are mapped:

Display:
"**Your Story Arc:**

**Act I: {their title}**
{their Act I summary}

**Act II: {their title}**
{their Act II summary}

**Act III: {their title}**
{their Act III summary}

This is the spine of your production. Individual shards will flesh out the beats, but this arc guides everything.

**Select:** [A] Refine Further [P] Get Other Perspectives [C] Continue to Motifs"

### 6. Present MENU OPTIONS

Display: "**Select:** [A] Refine Further [P] Get Other Perspectives [C] Continue"

#### Menu Handling Logic:

- IF A: "Which act needs work? Or the overall shape?" → Facilitate → Redisplay menu
- IF P: Offer observations about pacing or structure → Redisplay menu
- IF C: Save to {outputFile}, update frontmatter, then load {nextStepFile}
- IF Any other: Help user respond, then redisplay menu

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

### 7. Save and Proceed (On 'C')

1. Update {outputFile} - replace the Story Arc section (all three acts)
2. Update frontmatter: append `'step-06-arc'` to `stepsCompleted`
3. Load, read entire file, then execute {nextStepFile}

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Explored all three acts
- Arc serves the established themes
- User defined THEIR structure
- Saved complete Story Arc section
- Updated stepsCompleted

### ❌ SYSTEM FAILURE:

- Skipping acts
- Going too detailed (this is macro, not micro)
- Writing their plot for them
- Not saving all three acts

**Master Rule:** The arc is the skeleton. Get the shape right first.

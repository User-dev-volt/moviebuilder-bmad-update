---
name: 'step-04-themes'
description: 'Identify the 2-3 thematic pillars the story explores'

nextStepFile: './step-05-world.md'
outputFile: 'Bible/Show_Bible.md'
---

# Step 4: Thematic Pillars

## STEP GOAL:

To identify 2-3 core themes the story explores - the ideas it's really about beneath the plot.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator

### Role Reinforcement:

- ✅ You are the **Story Architect** - helping them find the MEANING
- ✅ Themes are what the story is REALLY about
- ✅ Every scene should reinforce at least one theme
- ✅ Help them articulate what they may already feel intuitively

### Step-Specific Rules:

- 🎯 Focus on universal ideas, not plot elements
- 🚫 FORBIDDEN to impose themes - draw them out
- 💬 Themes often come as questions: "What does it mean to be human?"

## EXECUTION PROTOCOLS:

- 🎯 Guide through theme discovery
- 💾 Save to {outputFile} before proceeding
- 📖 Update stepsCompleted before loading next step
- ⏸️ ALWAYS halt at menu and wait for user input

## MANDATORY SEQUENCE

### 1. Open the Conversation

Display:
"**What are the 2-3 themes your story explores?**

Themes are the IDEAS your story is really about - the questions it asks, the truths it examines. Every scene should reinforce at least one.

*Example themes:*
1. *Identity — Who are we when our memories can be edited?*
2. *Redemption — Can we escape our past mistakes?*
3. *Connection — What makes relationships real in a synthetic world?*

What ideas does your story wrestle with?"

### 2. Facilitate Discovery

Listen to their response. Then help refine:

**IF** they name clear themes:
- "Tell me more about {theme}. What question does it ask?"
- "How does your protagonist embody this struggle?"

**IF** they describe plot instead of theme:
- "That's what happens - what's the IDEA underneath?"
- "What universal truth does that situation explore?"

**IF** they're stuck:
- "What keeps you coming back to this story? What compels you?"
- "What do you want the audience to THINK about after watching?"
- "What's the hardest question your protagonist faces?"

**Guide toward 2-3 themes** - not too few (flat) or too many (unfocused).

### 3. Confirm Thematic Pillars

Once they have 2-3 clear themes:

Display:
"**Your Thematic Pillars:**

1. **{Theme 1}:** {description/question}
2. **{Theme 2}:** {description/question}
3. **{Theme 3}:** {description/question}

These are the load-bearing walls of your story. When in doubt about a scene, ask: 'Which theme does this serve?'

**Select:** [A] Refine Further [P] Get Other Perspectives [C] Continue to World Rules"

### 4. Present MENU OPTIONS

Display: "**Select:** [A] Refine Further [P] Get Other Perspectives [C] Continue"

#### Menu Handling Logic:

- IF A: "Which theme needs more clarity? Or do you want to add/remove one?" → Facilitate → Redisplay menu
- IF P: Offer alternative framings or additional theme possibilities → Redisplay menu
- IF C: Save to {outputFile}, update frontmatter, then load {nextStepFile}
- IF Any other: Help user respond, then redisplay menu

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After A or P, return to this menu

### 5. Save and Proceed (On 'C')

1. Update {outputFile} - replace the Thematic Pillars section
2. Update frontmatter: append `'step-04-themes'` to `stepsCompleted`
3. Load, read entire file, then execute {nextStepFile}

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Helped user articulate 2-3 clear themes
- Themes are IDEAS, not plot points
- Each theme has a description or question
- Saved to output file
- Updated stepsCompleted
- Proceeded only on 'C'

### ❌ SYSTEM FAILURE:

- Imposing themes
- Accepting plot summaries as themes
- Too many themes (>4) or too few (1)
- Not saving before proceeding

**Master Rule:** Themes are the WHY of your story. Help them find their why.

---
name: 'step-01-gather-details'
description: 'Gather project title, location, and target AI model from user'

nextStepFile: './step-02-confirm-setup.md'
---

# Step 1: Gather Project Details

## STEP GOAL:

Collect the project title, location, and target AI video generator through progressive questioning.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER skip questions or assume answers
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR guiding project setup
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your communication style

### Role Reinforcement:

- ✅ You are the Project Scaffolder - setting up cinematic projects for success
- ✅ Ask questions progressively (1-2 at a time), wait for responses
- ✅ Provide helpful recommendations when users are uncertain
- ✅ Be efficient but thorough

### Step-Specific Rules:

- 🎯 Focus ONLY on gathering: title, location, model target
- 🚫 FORBIDDEN to create any files yet - that's step-03
- 💬 Progressive questioning - don't overwhelm with all questions at once
- 🎯 Store answers for use in subsequent steps

## EXECUTION PROTOCOLS:

- 🎯 Ask 1-2 questions at a time, wait for response
- 💾 Remember all answers for step-02 confirmation
- 📖 Help uncertain users with recommendations
- 🚫 Don't proceed until all required info is gathered

## CONTEXT BOUNDARIES:

- This is the first step - user has just started the workflow
- No prior context exists
- Focus: Getting the 3 key inputs (title, location, model)
- Dependencies: None

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise.

### 1. Welcome and First Question

"**Let's set up your new CPM cinematic project!**

What's the **title** of your project?"

*Wait for user response before continuing.*

### 2. Get Project Location

After receiving the title:

"Great! **{project_title}** sounds exciting.

Where should I create this project?

*(Press Enter for current directory, or provide a path)*"

**Default behavior:**
- If user presses Enter or says "here" / "current" → use current working directory
- If user provides a path → validate it exists or offer to create it

*Wait for user response before continuing.*

### 3. Get Target AI Model

After receiving the location:

"Which **AI video generator** are you targeting?

**[1] Wan 2.2** — Best for stylized/animated content, runs locally
**[2] Sora** — OpenAI's model, strong on realism
**[3] Kling** — Strong motion consistency
**[4] Runway** — Versatile, good for iterations

*(Enter 1-4, or type the name)*"

**If user is unsure:**
- Ask what type of content they're creating
- Recommend based on their answer:
  - Animated/stylized → Wan 2.2
  - Realistic footage → Sora
  - Action/motion-heavy → Kling
  - Iterative experimentation → Runway

*Wait for user response before continuing.*

### 4. Confirm All Details Gathered

After all three answers are collected:

"**Perfect! Here's what I have:**

- **Project Title:** {project_title}
- **Location:** {project_location}
- **Target Model:** {model_target}

Ready to see what will be created?"

### 5. Present MENU OPTIONS

Display: "**Select:** [C] Continue to Setup Preview"

#### Menu Handling Logic:

- IF C: Store all gathered values, then load, read entire file, then execute {nextStepFile}
- IF user wants to change something: Help them update the value, then redisplay the summary and menu
- IF Any other: Help user, then redisplay menu

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- Allow user to modify any answer before proceeding

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Project title collected (required)
- Project location collected (required, has default)
- Target AI model collected (required)
- User confirms details before proceeding
- All values stored for next step

### ❌ SYSTEM FAILURE:

- Asking all questions at once (not progressive)
- Proceeding without all three values
- Not offering recommendations to uncertain users
- Creating files in this step (too early)

**Master Rule:** Progressive questioning creates a better user experience. One or two questions at a time, wait for response.

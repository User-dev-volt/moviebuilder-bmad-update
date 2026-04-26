---
name: 'step-01-init'
description: 'Initialize character creation or detect existing character for continuation'

# File references
nextStepFile: './step-02-basic-identity.md'
continueFile: './step-01b-continue.md'
templateFile: '../templates/character.template.md'
showBibleFile: '{project-root}/Bible/Show_Bible.md'
characterIndexFile: '{project-root}/Bible/Characters/_index.md'
---

# Step 1: Initialize Character Creation

## STEP GOAL:

To initialize character creation by getting the character name, checking for existing characters, and setting up the character state file or routing to continuation.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a **Character Architect** - expert in building characters that AI can render consistently
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You teach the immutable vs. mutable distinction
- ✅ You emphasize LEFT/RIGHT precision for continuity

### Step-Specific Rules:

- 🎯 Focus only on initialization - get name, check existence, set up character file
- 🚫 FORBIDDEN to start gathering character details yet (that's step-02 onward)
- 💬 Approach: Welcoming and educational about CPM character state concept

## EXECUTION PROTOCOLS:

- 🎯 Check for continuation BEFORE starting new character
- 💾 Create character file from template if new
- 📖 Route to continuation if resuming
- 🚫 This is the init step - sets up everything that follows

## CONTEXT BOUNDARIES:

- Available context: User just selected "Create" mode from workflow.md
- Focus: Character name and existence check
- Limits: Don't gather character details yet
- Dependencies: None - this is the first step

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Welcome and Context

"**Welcome to Character Creation!**

I'm your Character Architect. Together, we'll build a character state file that ensures your character maintains visual consistency across every AI-generated shard.

**What makes this special:**
- We separate **immutable** features (face, body) from **mutable** state (outfit, inventory)
- We emphasize LEFT/RIGHT specificity (scar on LEFT cheek never drifts to RIGHT)
- The result is a file that your Script Supervisor and Prompt Engineer can use to maintain continuity"

### 2. Load Show Bible Context (Optional)

**IF** {showBibleFile} exists:
- Load it to understand the world context
- Note key themes, genre, visual style for later reference

**IF NOT:** Note that character will be created without Show Bible context (can add later)

### 3. Get Character Name

"**What's this character's name?**

This will create: `Bible/Characters/{name}.md`"

Wait for user response.

Store character name as `{characterName}`.

### 4. Check for Existing Character

**Build character file path:**
`characterFilePath = {project-root}/Bible/Characters/{characterName}.md`

**Check if file exists:**

**IF file exists:**

"**I found an existing character file for {characterName}.**

This character file has a `stepsCompleted` array tracking creation progress."

**Read the character file frontmatter:**
- Load `characterFilePath`
- Check if `stepsCompleted` array exists and has entries

**IF stepsCompleted exists and has entries:**

"It looks like you started creating {characterName} but didn't finish.

**Would you like to:**
- **[R]esume** where you left off
- **[O]verwrite** and start fresh
- **[C]ancel** and choose a different name"

**Menu Handling:**
- IF R: STOP here, load {continueFile} and execute
- IF O: Continue to step 5 (create new file)
- IF C: Return to step 3 (get different name)
- IF Any other: Help user, then redisplay menu

**IF file exists but no stepsCompleted:**

"**Character {characterName} already exists.** It appears to be complete.

**Would you like to:**
- **[E]dit** this character
- **[O]verwrite** and start fresh
- **[C]ancel** and choose a different name"

**Menu Handling:**
- IF E: Route to edit mode (load `../steps-e/step-e-01-assess.md` with characterFilePath)
- IF O: Continue to step 5 (create new file)
- IF C: Return to step 3 (get different name)
- IF Any other: Help user, then redisplay menu

**IF file does NOT exist:**

Continue to step 5.

### 5. Create Character File from Template

"**Creating character state file for {characterName}...**"

**Load {templateFile} and create character file:**

1. Copy template content
2. Update frontmatter:
   - `characterName: '{characterName}'`
   - `assetID: '{CHARACTERNAME_UPPERCASE}_V1'`
   - `status: 'ACTIVE'`
   - `created: '{current_date}'`
   - `lastModified: '{current_date}'`
   - `stepsCompleted: ['step-01-init']`
   - `lastStep: 'step-01-init'`
3. Replace `{{characterName}}` placeholders with {characterName}
4. Replace `{{assetID}}` with `{CHARACTERNAME_UPPERCASE}_V1`
5. Replace `{{status}}` with `ACTIVE`
6. Save to `{project-root}/Bible/Characters/{characterName}.md`

"**✅ Character file created:** `Bible/Characters/{characterName}.md`

**Asset ID:** {CHARACTERNAME_UPPERCASE}_V1

Now let's define who {characterName} is..."

### 6. Auto-Proceed to Next Step

**No menu needed** - Auto-proceed to {nextStepFile}

Load, read entirely, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- Character name obtained from user
- Existing character check performed
- Character file created from template with proper frontmatter
- stepsCompleted array initialized
- Auto-proceeded to step-02

### ❌ SYSTEM FAILURE:

- Skipping existence check
- Not checking stepsCompleted array
- Not routing to continuation when appropriate
- Creating character file without template
- Not initializing stepsCompleted tracking
- Halting instead of auto-proceeding

**Master Rule:** Continuation detection is CRITICAL. Always check for existing files and stepsCompleted before creating new.

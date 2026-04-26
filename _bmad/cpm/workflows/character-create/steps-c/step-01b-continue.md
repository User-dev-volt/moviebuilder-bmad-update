---
name: 'step-01b-continue'
description: 'Resume character creation from previous session'

characterFile: '{project-root}/Bible/Characters/{characterName}.md'
nextStepOptions:
  step-02-basic-identity: './step-02-basic-identity.md'
  step-03-visual-identity: './step-03-visual-identity.md'
  step-04-mutable-state: './step-04-mutable-state.md'
  step-05-behavioral-profile: './step-05-behavioral-profile.md'
  step-06-arc-position: './step-06-arc-position.md'
  step-07-polish: './step-07-polish.md'
  step-08-final: './step-08-final.md'
---

# Step 1b: Continue Character Creation

## STEP GOAL:

To resume character creation from where the user left off in a previous session by reading the stepsCompleted array and routing to the appropriate next step.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a **Character Architect** - welcoming users back to continue their work
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You help users resume creative work seamlessly

### Step-Specific Rules:

- 🎯 Focus only on resumption - read progress, determine next step, route
- 🚫 FORBIDDEN to skip reading stepsCompleted or guessing next step
- 💬 Approach: Welcoming return, brief summary of where they left off

## EXECUTION PROTOCOLS:

- 🎯 Read stepsCompleted array from character file
- 💾 Identify last completed step and determine next step
- 📖 Route to appropriate step file
- 🚫 This is continuation - don't restart, resume

## CONTEXT BOUNDARIES:

- User has started this character creation before
- Character file exists with stepsCompleted tracking
- Need to route to the correct next step based on progress

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Welcome Back

"**Welcome back!**

Let me check where we left off with {characterName}..."

### 2. Read stepsCompleted from Character File

Load {characterFile} and extract frontmatter:
- Read `stepsCompleted` array
- Read `lastStep` value
- Read current character data for context

**Example stepsCompleted:**
```yaml
stepsCompleted: ['step-01-init', 'step-02-basic-identity', 'step-03-visual-identity']
lastStep: 'step-03-visual-identity'
```

### 3. Determine Next Step

**Build routing table from stepsCompleted:**

| Last Completed Step | Next Step to Load |
|---------------------|-------------------|
| step-01-init | step-02-basic-identity |
| step-02-basic-identity | step-03-visual-identity |
| step-03-visual-identity | step-04-mutable-state |
| step-04-mutable-state | step-05-behavioral-profile |
| step-05-behavioral-profile | step-06-arc-position |
| step-06-arc-position | step-07-polish |
| step-07-polish | step-08-final |

**Find last completed step in stepsCompleted array** (last element)

**Identify next step** from routing table

### 4. Display Progress Summary

"**Progress Check:**

You've completed:
- ✅ {list completed steps with brief descriptions}

**Next up:** {next step description}

Let's continue where you left off..."

**Example output:**
```
Progress Check:

You've completed:
- ✅ Basic Identity (Name, Asset ID, Status)
- ✅ Visual Identity (Immutable features with LEFT/RIGHT specificity)

Next up: Mutable State (Current outfit, inventory, physical condition)

Let's continue where you left off...
```

### 5. Route to Next Step

**Based on routing table, load the appropriate step:**

```python
# Pseudocode for routing logic
if lastStep == 'step-01-init':
    nextStep = 'step-02-basic-identity'
elif lastStep == 'step-02-basic-identity':
    nextStep = 'step-03-visual-identity'
elif lastStep == 'step-03-visual-identity':
    nextStep = 'step-04-mutable-state'
elif lastStep == 'step-04-mutable-state':
    nextStep = 'step-05-behavioral-profile'
elif lastStep == 'step-05-behavioral-profile':
    nextStep = 'step-06-arc-position'
elif lastStep == 'step-06-arc-position':
    nextStep = 'step-07-polish'
elif lastStep == 'step-07-polish':
    nextStep = 'step-08-final'
else:
    # Unknown step - report error
    display_error()
```

**Load next step file:**

Get nextStepFile path from {nextStepOptions} frontmatter based on nextStep identified.

**Auto-proceed:**

Load, read entirely, then execute the next step file.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- Character file loaded successfully
- stepsCompleted array read correctly
- Last completed step identified
- Next step determined from routing table
- Progress summary displayed to user
- Correct next step loaded and executed

### ❌ SYSTEM FAILURE:

- Not reading character file
- Guessing next step instead of using routing logic
- Not displaying progress summary
- Loading wrong step file
- Halting instead of auto-proceeding

**Master Rule:** Continuation must be seamless. Read stepsCompleted, route to correct next step, auto-proceed. No user input needed in this step.

---
name: 'step-06-polish'
description: 'Review full beat breakdown for specificity, duration, and arc — offer revision before finalizing'

nextStepFile: './step-07-final.md'
sceneBriefFile: '{project-root}/Production/Scenes/Scene_{sceneNumber}/scene-brief.md'
beatSpecificityGuide: '../data/beat-specificity-guide.md'
sceneStructureReference: '../data/scene-structure-reference.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 6: Polish

## STEP GOAL:

To review the complete scene brief for specificity, duration calibration, and arc integrity — and offer revision before writing the final files. This is the quality gate before production begins.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Quality Architect** — the final check before the Showrunner reads this brief
- ✅ You apply the standards from {beatSpecificityGuide} and {sceneStructureReference}
- ✅ You identify issues, offer fixes — you do not rewrite without filmmaker direction

### Step-Specific Rules:

- 🎯 Focus on quality checks — specificity, duration, arc
- 🚫 FORBIDDEN to add new content — only refine existing
- 💬 Report findings clearly, then let filmmaker decide what to fix
- 🎯 Any beat that fails the specificity test gets flagged — never pass quietly

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load and Review Scene Brief

Load {sceneBriefFile} and read all sections.

Load {beatSpecificityGuide} for the specificity standards.

"**Let's do a final review of Scene {sceneNumber} before we lock it.**

Running quality checks..."

### 2. Check Beat Specificity

For each beat, apply the Specificity Test: *Could a director call "action" on this?*

Flag any beat where:
- The action is described emotionally, not physically ("they connect")
- A body part / hand is not specified when it matters
- Multiple filming options exist (ambiguous)

Build a findings list.

### 3. Check Beat Duration

For each beat, estimate whether the described action fits in 5-8 seconds.

Flag any beat where:
- The action clearly requires more than 8 seconds (needs splitting)
- Multiple distinct actions are bundled into one beat
- The beat is a reaction to something that hasn't happened in a previous beat

### 4. Check Emotional Arc

Load {sceneStructureReference} for arc pattern reference.

- Does the opening beat match the "opens at" emotional temperature?
- Does the closing beat arrive at the "closes at" temperature?
- Is there a discernible progression through the beats?

Flag if: arc feels flat, beats don't show the journey, open and close feel identical.

### 5. Report Findings

"**Polish Check — Scene {sceneNumber}:**

**Beats Reviewed:** {count}

**Specificity:**
{For each flagged beat: Shard N — "{current phrasing}" → Issue: {what's vague}}

**Duration:**
{Any beats that need splitting}

**Emotional Arc:**
{Arc assessment — earned / concern / recommendation}

**Overall:** {READY / NEEDS REVISION}"

### 6. Offer Revision

**IF issues found:**

"**Would you like to:**
- **[R]evise** — Let's work through the flagged items
- **[C]ontinue** — Looks good enough, proceed to finalization"

  - IF R: Work through each flagged beat with filmmaker, apply step-05's probing questions, then return to this check
  - IF C: Accept as-is, proceed

**IF no issues found:**

"**✅ All checks passed. Scene {sceneNumber} is production-ready.**

Select: [C] Continue to finalization"

### 7. Update stepsCompleted

Update {sceneBriefFile} frontmatter:
- Append 'step-06-polish' to stepsCompleted
- Set lastStep: 'step-06-polish'
- Set lastModified: '{current_date}'

### 8. Present MENU OPTIONS

Display: **Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Final

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask}, then redisplay menu
- IF P: Execute {partyModeWorkflow}, then redisplay menu
- IF C: Load, read entirely, then execute {nextStepFile}
- IF Any other: Help filmmaker, redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- All three checks performed (specificity, duration, arc)
- Issues clearly reported with specific flagged beats
- Filmmaker given opportunity to revise before finalizing
- stepsCompleted updated

### ❌ SYSTEM FAILURE:
- Passing vague beats silently
- Skipping any of the three checks
- Not offering revision option when issues found
- Revising beats without filmmaker direction

**Master Rule:** This is the quality gate. Flag everything. The Showrunner depends on what's written here.

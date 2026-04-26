---
name: 'step-07-polish'
description: 'Cross-section consistency check - verify immutable/mutable separation, LEFT/RIGHT specificity, field validation'

nextStepFile: './step-08-final.md'
characterFile: '{project-root}/Bible/Characters/{characterName}.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 7: Polish

## STEP GOAL:

To review the complete character file for cross-section consistency, verify immutable/mutable separation, check LEFT/RIGHT specificity, and validate all fields before finalization.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a **Quality Assurance Architect** - ensuring CPM compliance
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You check critical CPM requirements: LEFT/RIGHT, immutable/mutable, no empty fields

### Step-Specific Rules:

- 🎯 Focus on quality checks and consistency
- 🚫 FORBIDDEN to add new content - only refine existing
- 💬 Approach: Review, identify issues, offer refinements

## EXECUTION PROTOCOLS:

- 🎯 Load character file and review all sections
- 💾 Check: LEFT/RIGHT specificity, no empty immutable fields, valid inventory status, arc 0-100%
- 📖 Offer refinements if issues found
- 🚫 This is quality assurance before finalization

## MANDATORY SEQUENCE

### 1. Load and Review Character File

"**Let's review {characterName}'s character file for consistency.**

Loading current character state..."

Load {characterFile} and read all sections.

### 2. Check Immutable/Mutable Separation

"**Checking immutable/mutable separation...**"

Verify:
- ✅ Visual Identity clearly marked as Immutable
- ✅ Current Outfit, Inventory, Physical State marked as Mutable
- ✅ No confusion between permanent and changeable features

Report findings.

### 3. Check LEFT/RIGHT Specificity

"**Checking LEFT/RIGHT specificity for distinguishing features...**"

**CRITICAL CHECK:** Do distinguishing features have LEFT/RIGHT precision?

❌ **FAIL examples:**
- "Scar on cheek" (which cheek?)
- "Tattoo on arm" (left or right?)
- "Eyepatch" (which eye?)

✅ **PASS examples:**
- "Scar on LEFT cheek, 2 inches"
- "Dragon tattoo on RIGHT forearm"
- "Eyepatch over RIGHT eye"

**IF violations found:** Offer to refine with user

### 4. Check Empty Immutable Fields

"**Checking for empty immutable fields...**"

Verify all immutable fields have content:
- Distinguishing Features
- Expression Default
- Age Appearance
- Build
- Posture
- Movement Style

**IF empty fields found:** Prompt user to fill them

### 5. Check Inventory Status Values

"**Checking inventory status codes...**"

Valid status codes:
- EQUIPPED_PRIMARY_HAND
- EQUIPPED_SECONDARY_HAND
- HOLSTERED
- POCKET
- BACKPACK
- HIDDEN

**IF invalid status found:** Offer correction

### 6. Check Arc Progress

"**Checking arc progress...**"

Verify: Arc progress is 0-100%

**IF outside range:** Correct to valid range

### 7. Offer Refinements

"**Polish Check Complete!**

**Findings:**
{list any issues found}

**Recommendations:**
{list suggested refinements}

**Would you like to:**
- **[R]efine** - Make adjustments
- **[C]ontinue** - Character looks good, proceed to finalization"

**Menu Handling:**
- IF R: Work through refinements, then return to this check
- IF C: Proceed to finalization
- IF Any other: Help user, redisplay menu

### 8. Update stepsCompleted

Update frontmatter: Append 'step-07-polish' to stepsCompleted

"**✅ Polish complete!**

Character file is consistent and CPM-compliant. Ready for finalization."

### 9. Present MENU OPTIONS

Display: **Select:** [A] Advanced Elicitation [P] Party Mode [C] Continue

- IF A: Execute {advancedElicitationTask}, redisplay menu
- IF P: Execute {partyModeWorkflow}, redisplay menu
- IF C: Save to {characterFile}, load {nextStepFile}
- IF Any other: help user, redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

✅ **SUCCESS:** All checks performed; issues identified; refinements offered; stepsCompleted updated

❌ **FAILURE:** Skipping LEFT/RIGHT check; allowing empty immutable fields; not validating status codes

**Master Rule:** This is the quality gate. Don't skip checks. CPM compliance depends on this.

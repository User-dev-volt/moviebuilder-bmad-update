---
name: 'step-v-01-validate'
description: 'Validate character consistency - LEFT/RIGHT specificity, no empty immutable fields, valid status codes, arc 0-100%'

characterFile: '{characterFilePath}'
editWorkflow: '../steps-e/step-e-01-assess.md'
---

# Validate Step 1: Character Validation

## STEP GOAL:

To validate character consistency against CPM standards - check LEFT/RIGHT specificity, verify no empty immutable fields, validate inventory status codes, and ensure arc progress is 0-100%.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- ✅ Validation does NOT stop for user input - auto-proceed through all checks
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Step-Specific Rules:

- 🎯 Run all 7 validation checks automatically
- 💬 Generate validation report with PASS/FAIL for each check
- 🚫 This is validation - systematic and thorough

## EXECUTION PROTOCOLS:

- 🎯 Load character file
- 💾 Run 7 automated checks
- 📖 Generate findings report
- 🚫 Auto-proceed through checks - no user input until report

## MANDATORY SEQUENCE

### 1. Load Character File

Load {characterFile} and read all content.

"**Validating {characterName}...**"

### 2. Run Validation Checks

**Check 1: LEFT/RIGHT Specificity**

Search distinguishing features for directional indicators (LEFT, RIGHT, left, right).

✅ **PASS:** All distinguishing features have LEFT/RIGHT specificity
❌ **FAIL:** Missing LEFT/RIGHT on: {list features}

**Check 2: No Empty Immutable Fields**

Verify all immutable fields have content:
- Distinguishing Features
- Expression Default
- Age Appearance
- Build
- Posture
- Movement Style

✅ **PASS:** All immutable fields populated
❌ **FAIL:** Empty fields: {list}

**Check 3: Inventory Status Codes Valid**

Valid codes: EQUIPPED_PRIMARY_HAND, EQUIPPED_SECONDARY_HAND, HOLSTERED, POCKET, BACKPACK, HIDDEN

✅ **PASS:** All inventory status codes valid
❌ **FAIL:** Invalid codes: {list}

**Check 4: Arc Progress 0-100%**

Verify arc progress is numeric value 0-100.

✅ **PASS:** Arc progress = {value}%
❌ **FAIL:** Arc progress = {value} (must be 0-100)

**Check 5: Asset ID Format**

Verify Asset ID follows format: {NAME}_V{number}

✅ **PASS:** Asset ID = {assetID}
❌ **FAIL:** Asset ID format incorrect: {assetID}

**Check 6: Version History Present**

Verify Version History table exists and has at least V1 entry.

✅ **PASS:** Version history tracked
❌ **FAIL:** Missing version history

**Check 7: Immutable/Mutable Separation**

Verify sections are properly labeled as Immutable or Mutable.

✅ **PASS:** Clear immutable/mutable separation
❌ **FAIL:** Sections not properly labeled

### 3. Generate Validation Report

"**Validation Complete!**

**Character:** {characterName}
**Asset ID:** {assetID}

**Results:**
- Check 1 (LEFT/RIGHT Specificity): {PASS/FAIL}
- Check 2 (No Empty Immutable Fields): {PASS/FAIL}
- Check 3 (Valid Inventory Status): {PASS/FAIL}
- Check 4 (Arc Progress 0-100%): {PASS/FAIL}
- Check 5 (Asset ID Format): {PASS/FAIL}
- Check 6 (Version History): {PASS/FAIL}
- Check 7 (Immutable/Mutable Separation): {PASS/FAIL}

**Overall Status:**
{IF all PASS: ✅ CPM COMPLIANT}
{IF any FAIL: ❌ ISSUES FOUND - See details above}"

### 4. Detailed Findings

**IF any checks failed:**

"**Issues Found:**

{For each failed check, provide details:}
- **Check {N}:** {description of violation}
  - **Issue:** {specific problem}
  - **Fix:** {how to resolve}"

### 5. Completion Menu

"**What would you like to do?**

**[F] Fix Issues** - Edit character to resolve violations
**[Q] Quit** - Exit validation"

- IF F: Load {editWorkflow} with {characterFile}
- IF Q: Exit validation
- IF Any other: Help user, redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

✅ **SUCCESS:** All 7 checks run; findings reported; issues identified with fix guidance

❌ **FAILURE:** Skipping checks; not providing specific fix guidance; halting mid-validation

**Master Rule:** Validation is automated and thorough. Run all checks. Report findings clearly.

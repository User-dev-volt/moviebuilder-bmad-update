---
name: 'step-v-01-validate'
description: 'Validate a scene brief for completeness, beat specificity, character file existence, and manifest consistency'

sceneBriefFile: '{project-root}/{provided_scene_path}'
beatSpecificityGuide: '../data/beat-specificity-guide.md'
characterFolder: '{project-root}/Bible/Characters'
manifestFile: '{project-root}/.cpm/manifest.md'
---

# Validate Step 1: Scene Brief Validation

## STEP GOAL:

To run a comprehensive validation of a scene brief — checking structural completeness, beat specificity, character file existence, and manifest consistency — and produce a clear pass/fail report with actionable findings.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Step-Specific Rules:

- 🎯 Run all four check categories — never skip
- 📋 Report all findings clearly — no silent passes on marginal beats
- 🚫 FORBIDDEN to auto-fix — report only; let filmmaker decide

## MANDATORY SEQUENCE

### 1. Load Scene Brief

Load {sceneBriefFile}.

Load {beatSpecificityGuide} for specificity standards.

"**Validating Scene {scene_number}...**"

### 2. Check 1: Structural Completeness

Verify all required sections exist and are populated:

| Field | Status |
|-------|--------|
| scene_number (frontmatter) | ✅ / ❌ |
| scene_id (frontmatter) | ✅ / ❌ |
| shard_count (frontmatter) | ✅ / ❌ |
| on_camera_characters (frontmatter, not empty) | ✅ / ❌ |
| Setting — Location | ✅ / ❌ |
| Setting — Time of Day | ✅ / ❌ |
| Setting — Atmosphere | ✅ / ❌ |
| Narrative Purpose (1+ sentences) | ✅ / ❌ |
| Emotional Arc — Opens at | ✅ / ❌ |
| Emotional Arc — Closes at | ✅ / ❌ |
| Beats section (1+ beats) | ✅ / ❌ |

### 3. Check 2: Beat Count Consistency

Verify: Does `shard_count` in frontmatter match the actual number of beats in the Beats section?

| Expected (shard_count) | Actual (counted beats) | Status |
|------------------------|------------------------|--------|
| {shard_count} | {actual_count} | ✅ MATCH / ❌ MISMATCH |

### 4. Check 3: Beat Specificity

For each beat, apply the Specificity Test from {beatSpecificityGuide}:

*Could a director call "action" on this?*

Report each beat:

| Shard | Action | Specificity | Notes |
|-------|--------|-------------|-------|
| 1 | {action} | ✅ PASS / ⚠️ VAGUE | {if vague: what's missing} |
| 2 | ... | | |

### 5. Check 4: Character File Verification

For each character in `on_camera_characters`:

Check if `{characterFolder}/{characterName}.md` exists.

| Character | File | Status |
|-----------|------|--------|
| {name} | Bible/Characters/{name}.md | ✅ EXISTS / ❌ MISSING |

### 6. Check 5: Manifest Consistency

Load {manifestFile} and verify Scene {scene_number} entry exists with matching shard_count.

| Check | Status |
|-------|--------|
| Scene entry in manifest | ✅ / ❌ |
| Shard count matches | ✅ / ❌ |
| Characters match | ✅ / ❌ |

### 7. Report Findings

"**Validation Report — Scene {scene_number}**

---

**Check 1: Structural Completeness**
{table from step 2}

**Check 2: Beat Count Consistency**
{table from step 3}

**Check 3: Beat Specificity**
{table from step 4}

**Check 4: Character Files**
{table from step 5}

**Check 5: Manifest Consistency**
{table from step 6}

---

**Overall Status:**

{✅ VALIDATED — All checks passed. Scene is production-ready.}
{OR}
{⚠️ VALIDATED WITH WARNINGS — {N} issues found. Scene can run but may cause problems.}
{OR}
{❌ FAILED — {N} critical issues. Resolve before running shard-generation.}

**Critical Issues (MUST fix):** {list}
**Warnings (should fix):** {list}
**Suggestions (optional):** {list}"

### 8. Exit

"**What would you like to do?**

**[E]dit** — Open scene in edit mode to fix issues
**[Q]uit** — Exit validation"

- IF E: Load `../steps-e/step-e-01-assess.md`
- IF Q: Exit with validation summary
- IF Any other: Help filmmaker, redisplay

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- All 5 checks performed
- Every beat assessed against specificity standard
- Every character verified against Bible/Characters/
- Manifest consistency checked
- Clear pass/fail/warning status reported

### ❌ SYSTEM FAILURE:
- Skipping any of the 5 checks
- Passing vague beats without noting them as warnings
- Not checking character files
- Not checking manifest

**Master Rule:** Report everything. The filmmaker decides what to fix. Your job is to see clearly.

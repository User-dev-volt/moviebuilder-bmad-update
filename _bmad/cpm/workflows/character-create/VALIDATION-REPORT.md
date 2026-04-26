# Frontmatter Validation Report
**Workflow:** character-create
**File:** `_bmad/cpm/workflows/character-create/workflow.md`
**Date:** 2026-02-16
**Status:** ⚠️ WORKFLOW ARCHITECTURE ISSUE - Monolithic Structure Detected

---

## Executive Summary

This workflow is currently **MONOLITHIC** (all instructions in single `workflow.md` file) and does **NOT** follow step-file architecture. The frontmatter is valid for a monolithic workflow but the workflow needs **conversion to step-file architecture** for production use.

**Key Finding:** Cannot validate step-level frontmatter because NO step files exist to validate.

---

## Part 1: Workflow Frontmatter Analysis

### Frontmatter Structure
```yaml
---
name: character-create
description: Create a new character state file with visual identity, inventory, and arc position
web_bundle: true
installed_path: '{project-root}/_bmad/cpm/workflows/character-create'
---
```

### Variables Extracted

| Variable | Value | Required? | Used in Body? | Status |
|----------|-------|-----------|---------------|--------|
| `name` | `character-create` | ✅ Yes | N/A (metadata) | ✅ OK |
| `description` | `Create a new character state file...` | ✅ Yes | N/A (metadata) | ✅ OK |
| `web_bundle` | `true` | ❓ Config | N/A (runtime config) | ⚠️ Non-standard |
| `installed_path` | `{project-root}/...` | ❓ Config | Referenced 1x (line 5) | ⚠️ Non-standard |

### Usage Analysis

#### Standard Variables (name, description)
- **name:** `character-create` ✅ Present, kebab-case format correct
- **description:** Present and descriptive ✅

#### Non-Standard Variables
| Variable | Frontmatter Presence | Body Usage | Violation? |
|----------|---------------------|-----------|-----------|
| `web_bundle` | Line 4: `true` | Not found in body | ⚠️ Unused - appears to be workflow configuration/metadata, not step reference |
| `installed_path` | Line 5: `{project-root}/...` | Found line 5 only (in frontmatter itself) | ⚠️ Possibly informational only |

### Frontmatter Assessment

**Against frontmatter-standards.md rules:**

✅ **PASSES:**
- Required fields `name` and `description` present
- Kebab-case naming format correct
- No `workflow_path` variable exists

⚠️ **VIOLATIONS/CONCERNS:**
1. **`web_bundle: true`** - Not used in body; appears to be workflow metadata/configuration flag
2. **`installed_path`** - Defines the workflow location but not actively used in workflow logic (only self-referential)
3. **No step-file references** - This workflow contains no `nextStepFile`, `templateFile`, `outputFile`, or similar references that would normally appear in step-file architecture

**Verdict:** Frontmatter is **technically valid** for a monolithic workflow but represents **non-standard configuration metadata** rather than step-logic variables.

---

## Part 2: Workflow Architecture Analysis

### Current State: MONOLITHIC ❌

This workflow is a **single monolithic document** containing:
- All instructions in-line in `workflow.md`
- All steps described sequentially within one file
- No separation of concerns
- No step-level state tracking

### Directory Structure

```
character-create/
├── workflow.md                      ✅ EXISTS (4,400 bytes)
├── validation-report-2026-02-16.md  ✅ EXISTS (previous validation)
├── steps-c/                         ❌ DOES NOT EXIST
├── steps-e/                         ❌ DOES NOT EXIST
└── steps-v/                         ❌ DOES NOT EXIST
```

**Folder Verification:** `ls -la` shows ONLY:
- `.` and `..` (parent directories)
- `workflow.md`
- `validation-report-2026-02-16.md`

**Conclusion:** No step-file folders or files exist. The workflow is entirely monolithic.

---

## Part 3: Required Step Files (Based on Content Analysis)

The workflow.md contains the following logical sections that SHOULD become step files in a converted workflow:

### INITIALIZATION Phase
These would go in `steps-c/` (Create phase):

| Step File Name | Source Section | Purpose |
|---|---|---|
| `steps-c/step-01-init.md` | INITIALIZATION → Get Character Name | Prompt for character name and validate existence |
| `steps-c/step-02-basic-identity.md` | CREATION SEQUENCE → Step 1 | Establish name, Asset ID, Status |
| `steps-c/step-03-visual-identity.md` | CREATION SEQUENCE → Step 2 | Capture face, body, distinguishing features |
| `steps-c/step-04-outfit.md` | CREATION SEQUENCE → Step 3 | Define current outfit and condition |
| `steps-c/step-05-inventory.md` | CREATION SEQUENCE → Step 4 | Build inventory table with item tracking |
| `steps-c/step-06-physical-state.md` | CREATION SEQUENCE → Step 5 | Document injuries and physical conditions |
| `steps-c/step-07-behavioral-profile.md` | CREATION SEQUENCE → Step 6 | Capture speech, tics, signature moves |
| `steps-c/step-08-arc-position.md` | CREATION SEQUENCE → Step 7 | Define emotional state, want, need, arc progress |
| `steps-c/step-09-compile.md` | COMPILATION | Assemble final character file and update index |

### EDIT Phase
These would go in `steps-e/` (Edit phase):

| Step File Name | Purpose | Dependencies |
|---|---|---|
| `steps-e/step-01-load-character.md` | Load existing character file | Requires character name |
| `steps-e/step-02-modify-section.md` | Edit specific character section | Loop back for multiple edits |
| `steps-e/step-03-save-version.md` | Save new version with change log | Update version history |

### VIEW Phase
These would go in `steps-v/` (View phase):

| Step File Name | Purpose |
|---|---|
| `steps-v/step-01-display-character.md` | Display character file with formatting |

---

## Part 4: Variables That Would Be Needed in Step Files

If this workflow were converted to step-file architecture, these variables would be used:

### Likely Step Frontmatter Variables

```yaml
# Typical CREATE phase (steps-c/) pattern:
nextStepFile: './step-0X-[name].md'              # To link steps
characterName: 'TBD'                              # User input from step-01
characterFilePath: 'Bible/Characters/{characterName}.md'
characterIndexPath: 'Bible/Characters/_index.md'
outputFile: '{project-root}/_bmad-output/character-{characterName}-v1.md'
stepsCompleted: ['step-01-init', 'step-02-basic']
date: '2026-02-16'
```

### Current Monolithic Limitations

The monolithic structure CANNOT track:
- ❌ Per-step completion (`stepsCompleted`)
- ❌ State resumption (continuing from where user left off)
- ❌ Step-specific frontmatter
- ❌ Just-in-time loading (loads entire workflow at once)
- ❌ Independent step validation

---

## Part 5: Validation Checklist Results

Using frontmatter-standards.md criteria:

| Criterion | Status | Details |
|-----------|--------|---------|
| `name` present, kebab-case | ✅ PASS | `character-create` correct format |
| `description` present | ✅ PASS | Clear description provided |
| Extract all variables from frontmatter | ✅ PASS | 4 variables identified |
| Search body for each variable | ⚠️ PARTIAL | `web_bundle` unused; `installed_path` only in frontmatter |
| Unused variables removed | ❌ FAIL | `web_bundle: true` not used in body |
| Step-to-step paths use `./filename.md` | N/A | No step files exist |
| Parent paths use `../filename.md` | N/A | No step files exist |
| Subfolder paths use `./subfolder/filename.md` | N/A | No step files exist |
| NO `{workflow_path}` variable | ✅ PASS | Not present |
| External paths use `{project-root}` | ✅ PASS | `installed_path` uses correct format |

---

## Part 6: Step File Validation Status

**CANNOT VALIDATE STEP-LEVEL FRONTMATTER BECAUSE:**

| Requirement | Status | Notes |
|---|---|---|
| Step folders (`steps-c/`, `steps-e/`, `steps-v/`) exist | ❌ NO | No step files in the workflow |
| Step files present | ❌ NO | Zero step files found |
| Step frontmatter to validate | ❌ NO | No step files = no step frontmatter |
| Step variable usage to check | ❌ NO | No step files to analyze |

**Expected Count if Converted:**
- `steps-c/`: 9 CREATE phase steps (initialization through compilation)
- `steps-e/`: 3 EDIT phase steps (load, modify, save)
- `steps-v/`: 1 VIEW phase step (display)
- **Total: 13 step files that should exist**

**Current State: 0/13 step files**

---

## Part 7: Overall Assessment

### Summary Findings

| Aspect | Finding |
|--------|---------|
| **Frontmatter Validity** | ⚠️ PARTIALLY VALID - Metadata present but `web_bundle` unused |
| **Standards Compliance** | ⚠️ NON-STANDARD - Uses workflow-level config not step-level variables |
| **Architecture** | ❌ MONOLITHIC - Not step-file architecture |
| **Step Files** | ❌ MISSING - 0 of 13 expected files present |
| **Validation Scope** | ❌ INCOMPLETE - Cannot fully validate step-file architecture |

### Recommendations

#### Immediate Action: Fix Monolithic Frontmatter
```yaml
---
name: character-create
description: Create a new character state file with visual identity, inventory, and arc position
---
```
**Remove:** `web_bundle` and `installed_path` (they're runtime metadata, not step variables)

#### Long-term Action: Convert to Step-File Architecture
Use BMB (BMAD Builder) workflow workflow to convert this monolithic workflow into proper step-file architecture:
1. Create `steps-c/` folder with 9 CREATE phase steps
2. Create `steps-e/` folder with 3 EDIT phase steps
3. Create `steps-v/` folder with 1 VIEW phase step
4. Add proper frontmatter to each step file
5. Implement state tracking with `stepsCompleted` and `lastStep` variables
6. Replace monolithic workflow.md with router logic (step selection and sequencing)

#### Priority: HIGH
This workflow is frequently used in production. The monolithic structure prevents:
- Session resumption (can't pick up mid-workflow)
- State persistence across user interruptions
- Independent step testing
- Proper variable scoping

---

## Appendix: Full Frontmatter Extraction

### Exact Frontmatter (Lines 1-6)
```
---
name: character-create
description: Create a new character state file with visual identity, inventory, and arc position
web_bundle: true
installed_path: '{project-root}/_bmad/cpm/workflows/character-create'
---
```

### Variable Inventory
| # | Variable Name | Line | Value |
|---|---|---|---|
| 1 | `name` | 2 | `character-create` |
| 2 | `description` | 3 | `Create a new character state file with visual identity, inventory, and arc position` |
| 3 | `web_bundle` | 4 | `true` |
| 4 | `installed_path` | 5 | `{project-root}/_bmad/cpm/workflows/character-create` |

---

## Report Metadata
- **Validation Standard:** `frontmatter-standards.md`
- **Workflow Type:** Monolithic (single file, not step-file routers)
- **Step Architecture Status:** Not implemented
- **Conversion Readiness:** Ready for conversion (clear sections exist)
- **Blocking Issues:** None for monolithic use; many for production step-file use

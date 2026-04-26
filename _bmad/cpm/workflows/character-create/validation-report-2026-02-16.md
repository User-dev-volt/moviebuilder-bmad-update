---
validationDate: 2026-02-16
workflowName: character-create
workflowPath: _bmad/cpm/workflows/character-create
validationStatus: TERMINATED_EARLY_FOR_CONVERSION
---

# Validation Report: character-create

**Validation Started:** 2026-02-16
**Validator:** BMAD Workflow Validation System
**Standards Version:** BMAD Workflow Standards

---

## File Structure & Size

### Current State: ❌ NON-COMPLIANT (Monolithic Architecture)

**Folder Structure:**
```
character-create/
├── workflow.md                           [225 lines]
└── validation-report-2026-02-16.md       [54 lines]
```

**Missing Required Structure:**
- ❌ `steps-c/` - Create phase step files
- ❌ `steps-e/` - Edit phase step files
- ❌ `steps-v/` - Validate phase step files
- ❌ `templates/` - Character sheet templates
- ❌ `data/` - Reference materials (archetypes, personality frameworks)
- ❌ `workflow-plan.md` - Planning documentation

### File Size Analysis:

| File | Lines | Status |
|------|-------|--------|
| workflow.md | 225 | ⚠️ Monolithic (should be decomposed) |

**Assessment:**
- File is within 250-line limit but represents a **monolithic single-file workflow**
- BMAD standard requires step-file architecture with 3-8 separate step files
- Converted workflows average 60-100 lines for router + 5-8 step files

### Comparison with Converted CPM Workflows:

| Workflow | workflow.md | Steps | Templates | Data | Status |
|----------|------------|-------|-----------|------|--------|
| show-bible | 91 lines | 8 files | 1 | 0 | ✅ Converted |
| new-project | 66 lines | 4 files | 3 | 1 | ✅ Converted |
| style-guide | ~100 lines | 10 files | 4 | 3 | ✅ Converted |
| character-create | 225 lines | **0** | **0** | **0** | ❌ **NOT CONVERTED** |

### Critical Issues Identified:

1. **No Step-File Architecture** - All logic in single monolithic file
2. **No Tri-Modal Structure** - Missing Create/Edit/Validate separation (required per NEXT-STEPS.md)
3. **No Templates** - Character sheet structure hardcoded in workflow
4. **No Data Files** - No reference materials for character archetypes, traits, etc.
5. **No Just-In-Time Loading** - Cannot pause/resume workflow mid-creation
6. **No State Tracking** - No stepsCompleted frontmatter mechanism

### Expected Converted Structure:

Based on NEXT-STEPS.md guidance and similar converted workflows:

```
character-create/
├── workflow.md                    # Tri-modal router (Create/Edit/Validate)
├── workflow-plan-character-create.md  # Design document
├── steps-c/                       # Create mode (5-8 steps)
│   ├── step-01-init.md           # Continuable init
│   ├── step-01b-continue.md      # Session resume
│   ├── step-02-basic-identity.md
│   ├── step-03-visual-identity.md # Immutable features (LEFT/RIGHT specificity)
│   ├── step-04-mutable-state.md   # Outfit, inventory, physical state
│   ├── step-05-behavioral-profile.md
│   ├── step-06-arc-position.md
│   ├── step-07-polish.md
│   └── step-08-final.md
├── steps-e/                       # Edit mode
│   └── step-e-01-assess.md       # Section-level editing
├── steps-v/                       # Validate mode
│   └── step-v-01-validate.md     # Validation checks
├── data/
│   ├── distinguishing-features-reference.md  # Common feature categories
│   ├── inventory-status-options.md
│   └── arc-position-frameworks.md
└── templates/
    └── character.template.md      # Character sheet with stepsCompleted tracking
```

**Estimated Conversion:** 225 lines → 8-10 step files + 3 data files + 1 template (14+ total files)

### Validation Status: **REQUIRES FULL CONVERSION**

This workflow does NOT meet BMAD step-file architecture standards and cannot proceed to detailed validation. Must select [F] Fix Issues → Convert mode.

## Frontmatter Validation

### Status: ⚠️ PARTIAL - Monolithic Workflow (No Step Files)

**Context:** This is a monolithic single-file workflow. BMAD step-file architecture validation requires separate step files in `steps-c/`, `steps-e/`, `steps-v/` folders - **none exist**.

### workflow.md Frontmatter Analysis:

```yaml
---
name: character-create
description: Create a new character state file with visual identity, inventory, and arc position
web_bundle: true
installed_path: '{project-root}/_bmad/cpm/workflows/character-create'
---
```

**Variable Usage Check:**

| Variable | Type | Used in Body | Status |
|----------|------|--------------|--------|
| `name` | Metadata | N/A (required field) | ✅ PASS |
| `description` | Metadata | N/A (required field) | ✅ PASS |
| `web_bundle` | Config | ❌ NOT FOUND | ❌ **VIOLATION** |
| `installed_path` | Config | Only in frontmatter | ⚠️ Metadata only |

**Violation Found:**
- `web_bundle: true` is defined but never referenced in workflow body → should be removed per frontmatter standards

### Step Files Validation: ❌ CANNOT VALIDATE

**Expected structure:**
```
steps-c/
├── step-01-init.md
├── step-02-basic-identity.md
├── step-03-visual-identity.md
└── ... (5-8 more steps)
```

**Actual:** NO step files exist (0 of ~13 expected)

### Assessment:

Since this is a monolithic workflow:
- ✅ Workflow metadata frontmatter exists
- ❌ 1 unused variable violation (`web_bundle`)
- ❌ NO step files to validate (architecture issue, not frontmatter issue)
- ❌ Cannot check step frontmatter compliance (no steps exist)

**Root Cause:** Workflow has NOT been converted to BMAD step-file architecture. This is the expected finding per NEXT-STEPS.md - all CPM workflows are monolithic and need conversion.

## Critical Path Violations

### Status: ❌ CRITICAL VIOLATIONS FOUND (4 issues)

**Context:** Monolithic workflow with NO step files - limited path checking to workflow.md only

### Config Variables Analysis:

**Found in workflow.md frontmatter:**
```yaml
name: character-create
description: (...)
web_bundle: true
installed_path: '{project-root}/_bmad/cpm/workflows/character-create'
```

**Missing required variables:**
- ❌ `{project-root}` - not defined for output path resolution
- ❌ `{cpm_output_folder}` - not referenced
- ❌ No configuration variables for Bible/ directory location

### CRITICAL: Hardcoded Path Violations

| Location | Path Referenced | Violation | Severity |
|----------|----------------|-----------|----------|
| Line 31 | `Bible/Characters/{name}.md` | Relative path, no variable resolution | 🔴 CRITICAL |
| Line 150 | `Bible/Characters/{name}.md` | Same - hardcoded in COMPILATION section | 🔴 CRITICAL |
| Line 202 | `Bible/Characters/_index.md` | Same - hardcoded in update section | 🔴 CRITICAL |

**Problem:** Workflow uses relative paths `Bible/Characters/` without context prefix. Cannot determine:
- Is this `{project-root}/Bible/` ?
- Is this `{cpm_output_folder}/Bible/` ?
- Is this relative to current directory?

**Expected pattern:**
```markdown
Create `{project-root}/Bible/Characters/{name}.md`
```

OR with CPM config variable:
```markdown
Create `{cpm_output_folder}/Bible/Characters/{name}.md`
```

### Dead Links Check:

**Referenced files:**
- `Bible/Characters/{name}.md` - ❌ Path doesn't resolve (no variable context)
- `Bible/Characters/_index.md` - ❌ Path doesn't resolve (no variable context)

**Template discovery:**
- ✅ CPM templates exist at `_bmad/cpm/templates/project/Bible/Characters/`
- ❌ Workflow doesn't reference template files correctly

### Module Awareness:

**Module:** CPM (_bmad/cpm/)
**Agent Integration Issue:**
- Script Supervisor expects: `Bible/Characters/{name}.md` at project root
- Showrunner expects: `Bible/Show_Bible.md` at project root
- ⚠️ **Mismatch:** Agents assume `Bible/` at project root, but workflow creates paths without context

**Available config:**
- ✅ `_bmad/core/config.yaml` defines `output_folder`
- ✅ `_bmad/cpm/` should have `cpm_output_folder` config

### Step Files Cannot Be Checked:

**Expected:** `steps-c/` (9 files), `steps-e/` (3 files), `steps-v/` (1 file)
**Actual:** NO step files exist (monolithic architecture)

Cannot validate:
- Step-to-step path references (`./step-XX.md`)
- Parent folder references (`../templates/`)
- Per-step variable definitions
- State tracking variables

### Summary of Violations:

1. **CRITICAL:** 3 hardcoded `Bible/` paths without variable resolution
2. **HIGH:** Missing `{project-root}` or `{cpm_output_folder}` variable definitions
3. **HIGH:** Agent expectation mismatch (agents expect Bible/ at specific location)
4. **MEDIUM:** No step-file architecture (cannot validate step-level paths)

**Status:** ⚠️ **PRODUCTION-BLOCKING** - Must fix path resolution before workflow can execute correctly

**Recommended fix:**
1. Add `project_root: '{project-root}'` to frontmatter
2. Replace all `Bible/` with `{project_root}/Bible/`
3. Or use CPM config variable if available

## Menu Handling Validation
*Pending...*

## Step Type Validation
*Pending...*

## Output Format Validation
*Pending...*

## Validation Design Check
*Pending...*

## Instruction Style Check
*Pending...*

## Collaborative Experience Check
*Pending...*

## Subprocess Optimization Opportunities
*Pending...*

## Cohesive Review
*Pending...*

## Plan Quality Validation
*Pending...*

## Summary

**Validation Terminated Early** - User elected to proceed directly to conversion after finding critical issues.

### Completed Checks (3 of 12):
1. ✅ File Structure & Size
2. ✅ Frontmatter Validation
3. ✅ Critical Path Violations

### Key Findings:

**ARCHITECTURE:**
- ❌ Monolithic single-file workflow (225 lines)
- ❌ NO step-file architecture (0/13 expected step files)
- ❌ Missing tri-modal structure (Create/Edit/Validate)

**FRONTMATTER:**
- ❌ 1 unused variable (`web_bundle`)
- ✅ Basic metadata present (name, description)

**PATH VIOLATIONS:**
- 🔴 3 CRITICAL hardcoded paths (`Bible/Characters/` without variable resolution)
- ❌ Missing config variables (`{project-root}`, `{cpm_output_folder}`)
- ⚠️ Agent integration mismatch

### Overall Assessment: **REQUIRES FULL BMAD CONVERSION**

**Expected Issues (from NEXT-STEPS.md):**
- No step-file architecture ← Found
- No step frontmatter ← Found (no steps exist)
- No MANDATORY EXECUTION RULES per step ← Cannot check (no steps)
- Missing menu handlers ← Cannot check (monolithic)
- No output templates ← Cannot check (monolithic)
- No {variable} format paths ← Found
- Form-filling interaction (not collaborative) ← Will address in conversion
- No session resume (no stepsCompleted tracking) ← Found
- No validation mode ← Found

**Validation Result:** ❌ **NON-COMPLIANT** - Proceed to Full BMAD Conversion

**Next Action:** Load conversion step (step-00-conversion.md) with guidance from NEXT-STEPS.md

---

## Conversion Guidance (from NEXT-STEPS.md)

**Workflow Type:** Character Create
- **Classification:** Document output=YES, Tri-Modal (Create+Edit+Validate), Continuable=YES
- **Role:** Character Architect
- **Core Concept:** Immutable vs mutable state distinction (critical for CPM)
- **Key Feature:** LEFT/RIGHT specificity for distinguishing features
- **Instruction Style:** Intent-based collaborative (not form-filling)

**Expected Structure After Conversion:**
- `workflow.md` - Tri-modal router (~60-100 lines)
- `steps-c/` - 8-9 create steps (init → visual identity → mutable state → compile)
- `steps-e/` - Edit mode steps
- `steps-v/` - Validate mode step
- `data/` - Reference files (feature categories, inventory options, arc frameworks)
- `templates/` - Character sheet template with stepsCompleted tracking

**Ready to begin conversion!**

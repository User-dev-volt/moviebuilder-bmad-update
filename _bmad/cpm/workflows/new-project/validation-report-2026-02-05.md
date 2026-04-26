---
validationDate: 2026-02-05
workflowName: new-project
workflowPath: _bmad/cpm/workflows/new-project
validationStatus: CRITICAL_FAILURE
---

# Validation Report: new-project

**Validation Started:** 2026-02-05
**Validator:** BMAD Workflow Validation System
**Standards Version:** BMAD Workflow Standards v6.0

---

## File Structure & Size

### ❌ CRITICAL: Monolithic Architecture Detected

**Current Structure:**
```
new-project/
└── workflow.md (211 lines) - SINGLE FILE ONLY
```

**Expected BMAD Structure:**
```
new-project/
├── workflow.md              # Entry point & routing only
├── workflow-plan.md         # Design document
├── steps-c/                 # Create mode steps
│   ├── step-01-*.md
│   ├── step-02-*.md
│   └── ...
├── data/                    # Reference files
└── templates/               # Output templates
```

### Findings:

| Check | Status | Notes |
|-------|--------|-------|
| workflow.md exists | ✅ | Present |
| Step folders exist | ❌ MISSING | No steps-c/, steps-e/, steps-v/ |
| Data folder exists | ❌ MISSING | No data/ folder |
| Templates folder exists | ❌ MISSING | No templates/ folder |
| workflow-plan.md exists | ❌ MISSING | No design document |

### File Size:
- `workflow.md`: 211 lines — ⚠️ Approaching limit (max 250)

**Status:** ❌ FAIL — Monolithic single-file workflow

---

## Frontmatter Validation

### Current Frontmatter:
```yaml
name: new-project
description: Scaffold a new CPM cinematic project with full directory structure and templates
web_bundle: true
agentTemplatesPath: '{project-root}/_bmad/cpm/templates/project/.cpm/agents'
```

### Issues:
| Issue | Severity | Details |
|-------|----------|---------|
| Missing step file references | ❌ Critical | No `nextStepFile` variable |
| Missing output file reference | ❌ Critical | No `outputFile` variable |
| No step-level frontmatter | ❌ Critical | Monolithic file has no step separation |

**Status:** ❌ FAIL — Not BMAD compliant

---

## Critical Path Violations

| Violation | Severity | Location |
|-----------|----------|----------|
| No step-file architecture | ❌ CRITICAL | Entire workflow |
| No JIT loading pattern | ❌ CRITICAL | All content in single file |
| No stepsCompleted tracking | ❌ CRITICAL | No frontmatter state management |
| Mixed concerns in one file | ❌ CRITICAL | Init, scaffolding, menus all together |

**Status:** ❌ FAIL — Fundamental architecture mismatch

---

## Menu Handling Validation

### Current Menu (lines 194-210):
```markdown
## MENU OPTIONS
- **[B] Show Bible** — Create Show Bible now
- **[S] Style Guide** — Create Style Guide now
- **[H] Character** — Create first character
- **[Q] Quit** — Exit (project is ready)
```

### Issues:
| Issue | Severity | Details |
|-------|----------|---------|
| Menu in wrong location | ⚠️ Warning | Should be in final step file |
| Missing "halt and wait" in execution rules | ❌ Critical | EXECUTION RULES section exists but should be in MANDATORY EXECUTION RULES |
| Handler logic present | ✅ Good | IF/THEN routing exists |

**Status:** ⚠️ PARTIAL — Menu structure okay, placement wrong

---

## Step Type Validation

**Not Applicable** — No step files exist to validate.

This workflow needs to be decomposed into:
1. `step-01-get-details.md` — Gather project info progressively
2. `step-02-confirm-setup.md` — Show structure, get confirmation
3. `step-03-scaffold.md` — Execute file creation
4. `step-04-completion.md` — Show results and final menu

**Status:** ❌ FAIL — No step files

---

## Output Format Validation

### Current Output Pattern:
- Inline YAML templates (config.yaml)
- Inline markdown templates (manifest.md)
- Inline directory structure display

### Issues:
| Issue | Severity | Details |
|-------|----------|---------|
| Templates embedded in workflow | ⚠️ Warning | Should be in templates/ folder |
| No output file frontmatter | ❌ Critical | Generated files should track state |

**Status:** ⚠️ PARTIAL — Templates need extraction

---

## Validation Design Check

**Not Applicable** — This is a Create-only workflow. No validation mode needed for scaffolding.

**Status:** ✅ N/A

---

## Instruction Style Check

### Current Style:
- Role statement present ("You are the **Project Scaffolder**")
- Progressive questioning pattern (good)
- Clear step numbering within sections

### Issues:
| Issue | Severity | Details |
|-------|----------|---------|
| No MANDATORY EXECUTION RULES block | ❌ Critical | Required for BMAD compliance |
| No STEP GOAL statement | ❌ Critical | Each step needs clear goal |
| No SUCCESS/FAILURE metrics | ❌ Critical | Missing system metrics |
| No Universal Rules block | ❌ Critical | Missing standard rule set |

**Status:** ❌ FAIL — Missing required BMAD instruction patterns

---

## Collaborative Experience Check

### Positives:
- Progressive question pattern (1-2 at a time) ✅
- Wait for response between questions ✅
- Recommendation logic for uncertain users ✅

### Issues:
| Issue | Severity | Details |
|-------|----------|---------|
| No explicit facilitator framing | ⚠️ Warning | Should state "partnership, not client-vendor" |
| No context boundaries defined | ⚠️ Warning | Missing CONTEXT BOUNDARIES section |

**Status:** ⚠️ PARTIAL — Good UX patterns, missing BMAD framing

---

## Subprocess Optimization Opportunities

**Potential for parallel operations:**
1. Directory creation could use parallel subprocess
2. File copying could be parallelized

**Current:** No subprocess patterns defined.

**Status:** ℹ️ INFO — Optimization possible but not required

---

## Cohesive Review

### Workflow Logic Flow:
1. Get project details (title, location, model) ✅
2. Confirm setup ✅
3. Create directories ✅
4. Generate config.yaml ✅
5. Copy agent templates ✅
6. Create manifest.md ✅
7. Create placeholder files ✅
8. Create index files ✅
9. Show completion menu ✅

**Logic is sound** — The workflow accomplishes its goal.

**Architecture is wrong** — Everything needs to be refactored into step-file architecture.

---

## Plan Quality Validation

**No workflow-plan.md exists.**

A design document should be created during conversion that captures:
- Workflow purpose and scope
- Step breakdown with goals
- File references and dependencies
- State management approach

**Status:** ❌ FAIL — Missing design document

---

## Summary

### Overall Status: ❌ CRITICAL FAILURE — REQUIRES FULL CONVERSION

### Issue Summary:

| Category | Status | Critical Issues |
|----------|--------|-----------------|
| File Structure | ❌ FAIL | Monolithic single-file architecture |
| Frontmatter | ❌ FAIL | No step-level frontmatter |
| Critical Path | ❌ FAIL | No JIT loading, no state tracking |
| Menu Handling | ⚠️ PARTIAL | Structure okay, placement wrong |
| Step Types | ❌ FAIL | No step files exist |
| Output Format | ⚠️ PARTIAL | Templates need extraction |
| Instruction Style | ❌ FAIL | Missing BMAD patterns |
| Collaborative | ⚠️ PARTIAL | Good UX, missing framing |
| Plan Document | ❌ FAIL | No workflow-plan.md |

### Required Actions:

1. **Create workflow-plan.md** — Design document
2. **Create steps-c/ folder** — For create mode steps
3. **Decompose into 4+ step files** — Following step-file architecture
4. **Extract templates** — Move to templates/ folder
5. **Add BMAD instruction patterns** — MANDATORY EXECUTION RULES, STEP GOAL, etc.
6. **Add state tracking** — stepsCompleted frontmatter pattern

### Recommendation:

**Full BMAD Conversion Required** — This workflow cannot be incrementally fixed. It needs complete restructuring using the conversion workflow (`steps-c/step-00-conversion.md`).

---

**Validation Complete:** 2026-02-05
**Next Action:** Run conversion workflow to restructure into BMAD step-file architecture

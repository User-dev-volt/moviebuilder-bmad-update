---
validationDate: 2026-02-17
workflowName: handshake-test
workflowPath: _bmad/cpm/workflows/handshake-test
validationStatus: FAIL — REQUIRES FULL CONVERSION
---

# Validation Report: handshake-test

**Validation Started:** 2026-02-17
**Validator:** BMAD Workflow Validation System
**Standards Version:** BMAD Workflow Standards

---

## File Structure & Size

**Status: ❌ FAIL — Monolithic single-file workflow**

### Folder Structure

```
handshake-test/
└── workflow.md (161 lines) — ONLY file
```

**Missing entirely:**
- ❌ No `steps/` folder (or steps-c/, steps-e/, steps-v/)
- ❌ No step files whatsoever
- ❌ No `data/` folder
- ❌ No `templates/` folder
- ❌ No workflow-plan.md

**File size:** workflow.md is 161 lines (within limits, but irrelevant — it's monolithic)

## Frontmatter Validation

**Status: ⚠️ PARTIAL**

Current frontmatter:
```yaml
name: handshake-test
description: Two-shard validation protocol to prove CPM maintains continuity
web_bundle: true
installed_path: '{project-root}/_bmad/cpm/workflows/handshake-test'
```

- ✅ Has name and description
- ✅ Has installed_path
- ❌ No step-file architecture section
- ❌ No role definition
- ❌ No initialization sequence
- ❌ No config loading

## Critical Path Violations

**Status: ❌ FAIL**

| Violation | Severity |
|-----------|----------|
| All workflow logic in single file | CRITICAL |
| No step-file decomposition | CRITICAL |
| No JIT loading pattern | CRITICAL |
| No sequential enforcement | CRITICAL |
| Interactive menu at bottom instead of step-based flow | CRITICAL |
| No execution rules or protocols | HIGH |
| No success/failure metrics per step | HIGH |

## Menu Handling Validation

**Status: ❌ FAIL**

- Menu exists at bottom of workflow.md (S/A/B/V/R/Q)
- ❌ No handler section after menu display
- ❌ No "halt and wait" instruction
- ❌ Menu is informational only — no routing logic
- ❌ Menu options don't map to step files

## Step Type Validation

**Status: ❌ N/A — No step files exist**

## Output Format Validation

**Status: ⚠️ PARTIAL**

- ✅ Has a results tracking table format
- ❌ No frontmatter state tracking (stepsCompleted)
- Note: This workflow produces test results, not a persistent document — no document output needed

## Validation Design Check

**Status: ❌ FAIL**

- The workflow IS a validation test, but has no structured validation steps
- Success criteria are listed but not procedurally checked
- No automated validation sequence

## Instruction Style Check

**Status: ⚠️ NEEDS CONVERSION**

- Current style is descriptive/informational, not prescriptive/procedural
- Needs conversion to step-file prescriptive instructions
- Role (Test Coordinator) not defined

## Collaborative Experience Check

**Status: N/A**

- This is a TEST PROTOCOL, not creative facilitation
- Should NOT have collaborative patterns
- Should be strictly procedural (Test Coordinator role)

## Subprocess Optimization Opportunities

**Status: N/A** — No subprocess patterns needed for this workflow

## Cohesive Review

The workflow has good CONTENT — the test design is sound:
- Minimal fixture setup (Hero with scar, Silver Key, rim light rule)
- Two-shard protocol (A: acquire, B: prove continuity)
- Clear success criteria (5 checks)
- Pass threshold (3 consecutive)
- Failure response protocol

The problem is purely STRUCTURAL — all this content lives in one monolithic file instead of being decomposed into step-file architecture.

## Plan Quality Validation

**Status: ❌ N/A — No workflow-plan.md exists**

## Summary

| Category | Status |
|----------|--------|
| File Structure | ❌ FAIL |
| Frontmatter | ⚠️ PARTIAL |
| Critical Path | ❌ FAIL |
| Menu Handling | ❌ FAIL |
| Step Types | ❌ N/A |
| Output Format | ⚠️ PARTIAL |
| Validation Design | ❌ FAIL |
| Instruction Style | ⚠️ NEEDS CONVERSION |
| Collaborative Experience | N/A (test protocol) |
| Subprocess Optimization | N/A |

**Overall Status: ❌ FAIL — REQUIRES FULL BMAD CONVERSION**

### Conversion Recommendations

1. **Decompose into 4 step files** in `steps/` folder (CREATE-ONLY, like shard-generation)
2. **Extract test fixtures** to `data/test-fixtures.md`
3. **Extract success criteria** to `data/success-criteria.md`
4. **Rewrite workflow.md** with proper BMAD architecture, role definition, initialization sequence
5. **Follow shard-generation patterns**: auto-proceed, prescriptive instructions, Test Coordinator role
6. **Reference shard-generation workflow** for Shard A and B execution (don't inline the ritual)

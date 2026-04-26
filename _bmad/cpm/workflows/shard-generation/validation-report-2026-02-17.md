---
validationDate: 2026-02-17
workflowName: shard-generation
workflowPath: _bmad/cpm/workflows/shard-generation
validationStatus: FAIL
---

# Validation Report: shard-generation

**Validation Started:** 2026-02-17
**Validator:** BMAD Workflow Validation System
**Standards Version:** BMAD Workflow Standards

---

## File Structure & Size

### Folder Structure Assessment

**Actual structure:**
```
shard-generation/
└── workflow.md (198 lines)
```

**Expected structure:**
```
shard-generation/
├── workflow.md
├── steps/
│   ├── step-01-init.md
│   ├── step-02-context-loading.md
│   ├── step-03-showrunner-review.md
│   ├── step-04-cinematographer-specs.md
│   ├── step-05-script-supervisor.md
│   ├── step-06-state-diff-gate.md
│   ├── step-07-prompt-compilation.md
│   └── step-08-state-update.md
├── data/
│   ├── prompt-structure-template.md
│   ├── state-diff-checklist.md
│   └── agent-personas.md
└── templates/
    ├── prompt-output.template.md
    └── exit-state.template.md
```

**Findings:**
- ❌ No step files folder — entire workflow is monolithic
- ❌ No data/ folder for reference materials
- ❌ No templates/ folder for output templates
- ❌ workflow.md contains ALL logic in a single file (198 lines)
- ✅ workflow.md exists and is within size limits (198 lines < 200)

**Status: FAIL** — No step-file architecture present.

---

## Frontmatter Validation

**Current frontmatter:**
```yaml
name: shard-generation
description: The 6-step mandatory ritual for generating AI video prompts with continuity
web_bundle: true
installed_path: '{project-root}/_bmad/cpm/workflows/shard-generation'
```

**Findings:**
- ✅ `name` present
- ✅ `description` present
- ⚠️ No mode determination routing (acceptable for CREATE-ONLY lifecycle)
- ❌ No initialization sequence referencing config loading
- ❌ No routing to step files (monolithic)

**Status: FAIL** — Missing BMAD initialization sequence.

---

## Critical Path Violations

- ❌ **No step-file architecture at all** — Entire ritual is inline in workflow.md
- ❌ **No just-in-time loading** — All 6 ritual steps described in one file
- ❌ **No state tracking** — No frontmatter state updates between steps
- ❌ **No sequential enforcement mechanism** — Steps listed but no load/execute pattern
- ❌ **State-Diff Check is inline** — Not a separate hard-gate enforcement step
- ❌ **No agent persona loading** — Steps say "Acting as {Agent}" but don't reference agent files
- ❌ **No halt mechanism** — State-Diff Check says "HALT" but no actual enforcement pattern

**Status: FAIL** — Fundamental architecture violations.

---

## Menu Handling Validation

**Current menu (lines 173-177):**
```
[N] Next Shard — Run ritual for next shard
[R] Re-run — Re-run current shard
[V] Validate — Run handshake test
[Q] Quit — Exit ritual
```

**Findings:**
- ❌ No menu handler logic (IF N: / IF R: / IF V: / IF Q:)
- ❌ No "halt and wait for user input" instruction
- ❌ No redisplay-on-invalid-input pattern
- ⚠️ Menu options are appropriate for the workflow purpose

**Status: FAIL** — Menu exists but has no handler implementation.

---

## Step Type Validation

**N/A** — No step files exist. Workflow is monolithic.

**Status: FAIL**

---

## Output Format Validation

**Identified outputs:**
1. Prompt file → `Output/Prompts/Scene_{XX}_Shard_{Y}_prompt.md`
2. Exit state → `Production/Scenes/Scene_{XX}/state/shard_{Y}_exit_state.md`

**Findings:**
- ❌ No output templates defined
- ❌ No prompt structure template (only inline code block)
- ❌ No exit state template
- ⚠️ Output paths are well-defined and consistent with CPM architecture

**Status: FAIL** — Outputs described but not templated.

---

## Validation Design Check

**N/A** — CREATE-ONLY lifecycle, no validate mode needed.

**Status: PASS** (by design — validate is not applicable)

---

## Instruction Style Check

**Findings:**
- ⚠️ Instructions are brief but prescriptive (good for this ritual type)
- ❌ Steps lack required input/output specifications per the PRESCRIPTIVE pattern
- ❌ No explicit validation checks per step
- ❌ Agent persona requirements not formalized
- ❌ File I/O requirements not specified (reads from Bible/, Architecture/, Production/, writes to Output/, Production/)

**Status: FAIL** — Insufficient prescriptive detail for a ritual workflow.

---

## Collaborative Experience Check

**N/A** — This is a PROCEDURAL RITUAL, not creative facilitation. The "Explore → Discuss → Formalize" pattern does NOT apply. Strict sequential enforcement is correct.

**Status: PASS** (by design — ritual pattern is correct)

---

## Subprocess Optimization Opportunities

- Each agent step could theoretically run as a subprocess, but the sequential nature of the ritual (each agent builds on the previous) makes this inappropriate
- State-Diff Check must be synchronous and blocking

**Status: N/A** — Sequential ritual, no parallelization appropriate.

---

## Cohesive Review

The monolithic workflow.md captures the **intent** of the Shard Generation Ritual accurately. The 6-step sequence, agent roles, State-Diff Check, and output structure all align with the CPM module brief. However, the implementation is entirely non-BMAD:

1. No step-file architecture
2. No agent persona loading
3. No file I/O specifications
4. No enforcement mechanisms
5. No templates for outputs
6. No data files for reference material

**The content is sound. The architecture needs full conversion.**

---

## Plan Quality Validation

**N/A** — No workflow-plan.md exists.

---

## Summary

| Category | Status |
|----------|--------|
| File Structure & Size | ❌ FAIL |
| Frontmatter | ❌ FAIL |
| Critical Path | ❌ FAIL |
| Menu Handling | ❌ FAIL |
| Step Types | ❌ FAIL |
| Output Format | ❌ FAIL |
| Validation Design | ✅ PASS (CREATE-ONLY) |
| Instruction Style | ❌ FAIL |
| Collaborative Experience | ✅ PASS (Ritual pattern) |
| Subprocess Optimization | N/A |
| Cohesive Review | ⚠️ Content good, architecture absent |
| Plan Quality | ❌ FAIL (no plan) |

**Overall Status: ❌ FAIL — Full BMAD conversion required**

### Recommended Conversion Plan

**Classification:**
- Document output: YES (prompt file + exit state)
- Module: CPM
- Session: SINGLE-SESSION (each shard is one complete run)
- Lifecycle: CREATE-ONLY (no edit/validate modes)
- Pattern: PROCEDURAL RITUAL (strict sequential enforcement)
- Instruction style: PRESCRIPTIVE (exact inputs, outputs, validation checks)

**Proposed step-file structure:**
```
shard-generation/
├── workflow.md (init + routing, CREATE-ONLY)
├── steps/
│   ├── step-01-init.md (get scene/shard, begin ritual)
│   ├── step-02-context-loading.md (load all required files — AS Ritual Coordinator)
│   ├── step-03-showrunner-review.md (AS Showrunner agent)
│   ├── step-04-cinematographer-specs.md (AS Cinematographer agent)
│   ├── step-05-script-supervisor.md (AS Script Supervisor agent)
│   ├── step-06-state-diff-gate.md (HARD GATE — halt on any failure)
│   ├── step-07-prompt-compilation.md (AS Prompt Engineer agent)
│   └── step-08-state-update.md (state save + completion menu)
├── data/
│   ├── prompt-structure-template.md
│   ├── state-diff-checklist.md
│   └── context-loading-checklist.md
└── templates/
    ├── prompt-output.template.md
    └── exit-state.template.md
```

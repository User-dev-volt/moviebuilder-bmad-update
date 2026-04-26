---
validationDate: 2026-02-06
completionDate: 2026-02-06
workflowName: style-guide
workflowPath: _bmad/cpm/workflows/style-guide
validationStatus: COMPLETE
---

# Validation Report: style-guide

**Validation Started:** 2026-02-06
**Validator:** BMAD Workflow Validation System
**Standards Version:** BMAD Workflow Standards

---

## File Structure & Size

### Folder Structure Assessment: ❌ FAIL — Monolithic Workflow

**Actual structure:**
```
style-guide/
└── workflow.md          (200 lines)
```

**Expected BMAD structure (missing entirely):**
```
style-guide/
├── workflow.md           ← EXISTS (but monolithic, contains all steps inline)
├── workflow-plan.md      ← MISSING
├── steps-c/              ← MISSING (no step folder at all)
│   ├── step-01-*.md
│   ├── step-02-*.md
│   └── ...
├── steps-e/              ← MISSING (no edit mode)
├── steps-v/              ← MISSING (no validate mode)
├── data/                 ← MISSING
└── templates/            ← MISSING
```

### Issues Found

| # | Severity | Issue |
|---|----------|-------|
| 1 | ❌ Critical | **No step-file architecture** — All 6 steps are inline in workflow.md |
| 2 | ❌ Critical | **No steps-c/ folder** — No create-mode step files exist |
| 3 | ❌ Critical | **No steps-e/ folder** — No edit-mode step files exist |
| 4 | ❌ Critical | **No steps-v/ folder** — No validate-mode step files exist |
| 5 | ❌ Critical | **No workflow-plan.md** — No design/plan document exists |
| 6 | ❌ Critical | **No data/ folder** — Reference content not extracted |
| 7 | ❌ Critical | **No templates/ folder** — Output templates not defined |
| 8 | ⚠️ Warning | **workflow.md is 200 lines** — At the recommended limit; after BMAD conversion the router should be much shorter |

### File Size Analysis

| File | Lines | Status |
|------|-------|--------|
| workflow.md | 200 | ⚠️ At recommended limit (monolithic — contains all steps inline) |

### Step Files Verified Against Plan: N/A
- No `workflow-plan.md` exists to verify against
- No individual step files exist

### File Structure & Size Status: ❌ FAIL
This workflow requires **full BMAD conversion**, not incremental fixes. It is a monolithic single-file workflow with zero step-file architecture compliance.

---

## Frontmatter Validation

### workflow.md Frontmatter Analysis

**Frontmatter contents:**
```yaml
name: style-guide
description: Create your visual style guide - lighting, color, camera language, and prompt vocabulary
web_bundle: true
installed_path: '{project-root}/_bmad/cpm/workflows/style-guide'
```

| Variable | Used in Body? | Status |
|----------|---------------|--------|
| `name` | N/A (metadata) | ✅ Present |
| `description` | N/A (metadata) | ✅ Present |
| `web_bundle` | N/A (config flag) | ✅ Acceptable |
| `installed_path` | ❌ Not referenced anywhere in body | ❌ Unused variable |

### Step File Frontmatter: N/A
- No step files exist — **zero step files to validate**
- All 6 content steps are inline in workflow.md with no frontmatter variables, no `{variable}` references, no step-to-step routing

### Violations

| # | File | Violation | Details |
|---|------|-----------|---------|
| 1 | workflow.md | Unused variable | `installed_path` defined but never referenced in body |
| 2 | N/A | No step files | Cannot validate step frontmatter — none exist |
| 3 | workflow.md | Hardcoded paths | All paths in body are hardcoded strings (e.g., `Architecture/Style_Guide.md`) instead of `{variable}` format |

### Frontmatter Validation Status: ❌ FAIL
No step-file frontmatter exists to validate. The monolithic workflow uses hardcoded paths throughout instead of `{variable}` format references.

## Critical Path Violations

### Config Variables (Exceptions)

No Configuration Loading section exists in workflow.md. No config variables defined — **zero exceptions to apply**.

### Content Path Violations

| File | Line(s) | Issue | Details |
|------|---------|-------|---------|
| workflow.md | 29, 164 | Hardcoded output path | `Architecture/Style_Guide.md` — should use `{variable}` format |
| workflow.md | 94, 166 | Hardcoded output path | `Architecture/Palette.md` — should use `{variable}` format |
| workflow.md | 119, 167 | Hardcoded output path | `Architecture/Lens_Language.md` — should use `{variable}` format |
| workflow.md | 158, 168 | Hardcoded output path | `Architecture/Vocabulary.md` — should use `{variable}` format |

**Total: 4 unique hardcoded paths across 8 references**

### Dead Links

No step-to-step references exist (monolithic workflow). No data file references. No dead links to detect — but this is because the entire step-file architecture is absent, not because the workflow is clean.

### Module Awareness

- Workflow is in `cpm` module (not `bmb`) ✅
- No `bmb`-specific path assumptions found ✅
- However, no proper CPM module config variable usage exists ❌
- Workflow references no module config (no `output_folder`, no `{project-root}` routing in body)

### Summary

- **CRITICAL:** 4 violations (hardcoded output paths — must use `{variable}` format)
- **HIGH:** 0 violations
- **MEDIUM:** 1 violation (no module config variable integration)

**Status:** ❌ FAIL — Critical violations detected (all symptomatic of monolithic, non-BMAD architecture)

## Menu Handling Validation

### Menu Found in workflow.md (lines 191-200)

```
- [R] Review — Review the Style Guide
- [E] Edit — Edit a specific section
- [P] Palette — Edit color palette
- [V] Vocabulary — Edit banned/required words
- [C] Character — Create characters
- [Q] Quit — Exit
```

### Violations

| # | Issue | Severity | Details |
|---|-------|----------|---------|
| 1 | No handler section | ❌ Critical | Menu display has no corresponding handler logic (IF R: ... IF E: ... etc.) |
| 2 | No execution rules | ❌ Critical | No "halt and wait" instruction anywhere |
| 3 | No "redisplay menu" | ❌ Critical | Non-C options don't specify returning to menu |
| 4 | Reserved letter misuse | ⚠️ Warning | `C` is reserved for "Continue" in BMAD but used here for "Character" |
| 5 | No A/P options | ✅ N/A | A/P not expected for this context (acceptable) |
| 6 | Menu disconnected from flow | ❌ Critical | Menu appears after COMPLETION section — it's an afterthought, not integrated into step progression |
| 7 | No step-file menus | ❌ Critical | Individual creation steps (1-6) have no menus at all — no opportunity for user to review/refine before proceeding |

### Menu Handling Status: ❌ FAIL
Menu exists but violates every BMAD menu handling standard. No handler section, no execution rules, reserved letter misuse, no step-level menus.

---

## Step Type Validation

### Step Analysis: ❌ FAIL — No BMAD Step Files Exist

The monolithic workflow.md contains 6 inline "steps" that don't follow any BMAD step type pattern:

| Inline Step | Should Be (BMAD) | Current State | Status |
|-------------|-------------------|---------------|--------|
| Initialization | Init step (step-01) | Inline check for existing file | ❌ Not a step file |
| Step 1: Visual Identity | Middle (Simple) — C-only menu | Inline text prompt | ❌ Not a step file |
| Step 2: Lighting Protocol | Middle (Standard) — A/P/C menu | Inline table template | ❌ Not a step file |
| Step 3: Color Palette | Middle (Standard) — A/P/C menu | Inline table template | ❌ Not a step file |
| Step 4: Camera Language | Middle (Standard) — A/P/C menu | Inline table template | ❌ Not a step file |
| Step 5: Spatial Rules | Middle (Simple) — C-only menu | Inline short prompt | ❌ Not a step file |
| Step 6: Prompt Vocabulary | Middle (Standard) — A/P/C menu | Inline table template | ❌ Not a step file |
| Compilation | Final or auto-proceed | Inline file creation list | ❌ Not a step file |

**Missing BMAD elements per step:**
- No frontmatter (name, description, file references)
- No STEP GOAL section
- No MANDATORY EXECUTION RULES
- No EXECUTION PROTOCOLS
- No CONTEXT BOUNDARIES
- No menus (A/P/C or C-only)
- No SUCCESS/FAILURE METRICS

### Step Type Status: ❌ FAIL
Zero step files exist. All content is inline with no BMAD step type compliance.

---

## Output Format Validation

### Document Production Analysis

**Workflow produces 4 output documents:**
1. `Architecture/Style_Guide.md` — Main style guide (all sections)
2. `Architecture/Palette.md` — Color definitions
3. `Architecture/Lens_Language.md` — Camera specs
4. `Architecture/Vocabulary.md` — Banned/required words

### Violations

| # | Issue | Severity | Details |
|---|-------|----------|---------|
| 1 | No templates/ folder | ❌ Critical | No output templates exist — output format is undefined |
| 2 | No template files | ❌ Critical | No `.template.md` files for any of the 4 outputs |
| 3 | No frontmatter tracking | ❌ Critical | No `stepsCompleted` tracking in output documents |
| 4 | No step-to-output mapping | ❌ Critical | Steps don't reference output files via `{variable}` format |
| 5 | No final polish step | ⚠️ Warning | No step to review/optimize the complete Style Guide before finalizing |
| 6 | "Dump at end" pattern | ❌ Critical | All 4 documents created in bulk at COMPILATION, not progressively built |
| 7 | Output paths not configurable | ❌ Critical | Hardcoded `Architecture/` path — should use `{output_folder}` variable |

### Output Format Status: ❌ FAIL
No templates, no progressive output building, no tracking, no configurable paths.

---

## Validation Design Check

### Is Validation Critical for This Workflow?

**Domain:** Creative/Visual — Style guide creation for cinematic production
**Assessment:** Validation is **NOT critical** (creative workflow, not compliance/safety/regulatory)

However, for BMAD compliance:
- ❌ No `steps-v/` folder exists (no validation mode)
- ❌ No validation data files
- ❌ No systematic validation checks for the style guide output
- ⚠️ A lightweight validation step would be beneficial to check: hex code format validity, palette consistency, no conflicting rules

### Validation Design Status: ⚠️ WARNING
Validation not critical for this creative domain, but no validation infrastructure exists at all. A lightweight review step would improve quality.

---

## Instruction Style Check

### Domain: Creative/Visual → Should be Intent-Based (Default)

### Analysis of Inline Steps

| Step | Style | Assessment |
|------|-------|------------|
| Step 1: Visual Identity | Intent-based | ✅ Good — "Describe your visual philosophy in one paragraph" is open-ended |
| Step 2: Lighting Protocol | Prescriptive/Form-filling | ❌ Dumps a table template to fill out, plus checkboxes |
| Step 3: Color Palette | Prescriptive/Form-filling | ❌ Tables to fill — "Allowed Colors", "Forbidden Colors" |
| Step 4: Camera Language | Prescriptive/Form-filling | ❌ Multiple tables — lens choices, progressions, movement rules |
| Step 5: Spatial Rules | Mixed | ⚠️ Some open prompts but also fill-in-the-blank patterns |
| Step 6: Prompt Vocabulary | Prescriptive/Form-filling | ❌ Substitution tables and banned word lists |

### Key Issues

- **5 of 6 steps use prescriptive/form-filling style** — inappropriate for a creative domain
- No "guide user through exploration" language
- No "ask 1-2 questions at a time" approach
- No "probe to understand deeper" facilitation
- Tables presented as blanks to fill rather than topics to explore collaboratively
- Example content is good but presented as templates, not conversation starters

### Instruction Style Status: ❌ FAIL
Creative workflow using prescriptive form-filling instead of intent-based collaborative facilitation. Should guide users through visual exploration, not present empty tables to complete.

---

## Collaborative Experience Check

### Overall Facilitation Quality: Poor

### Step-by-Step Experience Analysis

| Step | Question Style | Conversation Flow | Facilitation | Status |
|------|---------------|-------------------|--------------|--------|
| Step 1 | Single question | ✅ Natural | ✅ Open-ended | ✅ PASS |
| Step 2 | Table dump | ❌ Form-filling | ❌ No facilitation | ❌ FAIL |
| Step 3 | Table dump | ❌ Form-filling | ❌ No facilitation | ❌ FAIL |
| Step 4 | Table dump + lists | ❌ Form-filling | ❌ No facilitation | ❌ FAIL |
| Step 5 | Fill-in-blank | ❌ Rigid | ⚠️ Minimal | ⚠️ WARN |
| Step 6 | Table dump | ❌ Form-filling | ❌ No facilitation | ❌ FAIL |

### Collaborative Strengths
- Step 1 (Visual Identity) is genuinely collaborative — asks one open-ended question
- Good example content provided (the Edward Hopper cyberpunk example is evocative)
- Domain knowledge is strong — the right topics are covered

### Collaborative Issues

**Laundry List / Table Dump Pattern:**
- Steps 2-6 present entire table structures at once
- User is expected to fill in hex codes, lens mm values, and rules simultaneously
- No progressive questioning — everything dumped at once

**Form-Filling Pattern:**
- `| Rim Light | {name} | #{hex} | {when to use} |` — this is a form, not a conversation
- No space for "What lighting inspires you?" or "Tell me about the mood you want"
- No back-and-forth exploration before formalizing into tables

**Missing Role Reinforcement:**
- No "We engage in collaborative dialogue" language
- No "Together we produce something better" messaging
- "You are the Visual Architect" is stated but not reinforced per-step

### User Experience Assessment

**This workflow feels like:** A form collecting data FROM the user
**Should feel like:** A collaborative partner exploring visual identity WITH the user

### Overall Collaborative Rating: 2/5

### Collaborative Experience Status: ❌ NEEDS SIGNIFICANT IMPROVEMENT
Strong domain content trapped in a form-filling delivery pattern. Conversion to BMAD step-file architecture should transform tables into collaborative conversations.

---

## Subprocess Optimization Opportunities

### N/A — Monolithic Workflow

No step files exist to optimize with subprocess patterns. After BMAD conversion, the following patterns should be applied:

| Pattern | Opportunity | Priority |
|---------|------------|----------|
| Pattern 2 (per-file) | Each create step could be analyzed independently | HIGH |
| Pattern 3 (data ops) | Lighting/color reference data could be extracted to data/ files | MEDIUM |
| Pattern 4 (parallel) | Palette.md and Vocabulary.md outputs could be generated in parallel | LOW |

### Subprocess Optimization Status: N/A — Requires BMAD conversion first

---

## Cohesive Review

### Overall Assessment: Needs Major Rework (BMAD Conversion)

### Walking Through as a User

1. **Initialization** — Decent. Checks for existing Style Guide, offers Edit or Start Fresh. But no proper BMAD routing.
2. **Step 1 (Visual Identity)** — Strong opening. One open-ended question that invites creative expression. The Edward Hopper example is excellent.
3. **Step 2 (Lighting Protocol)** — Overwhelming. Jumps from one creative question to demanding hex codes, table structures, and checkbox rules simultaneously. No transition, no facilitation.
4. **Step 3 (Color Palette)** — Form-like. Three tables dumped at once (Allowed, Forbidden, Meaning). No progressive exploration.
5. **Step 4 (Camera Language)** — Heavy. Lens tables, shot progressions, movement rules all at once. Domain expertise is excellent but delivery is abrupt.
6. **Step 5 (Spatial Rules)** — Brief and manageable, but still fill-in-the-blank.
7. **Step 6 (Prompt Vocabulary)** — Two tables (substitutions, banned words). Useful but prescriptive.
8. **Compilation** — Creates 4 files. Good that it produces structured output, but the "dump everything at once" pattern means no progressive review.
9. **Completion/Menu** — Abrupt. Menu appears with no integration to the creation flow.

### Strengths
- Excellent domain knowledge (lighting, color, camera, vocabulary)
- Good example content that inspires creativity
- Strong visual identity concept
- Covers all important aspects of a cinematic style guide
- Clear output structure (4 complementary documents)

### Weaknesses
- Monolithic architecture — no progressive disclosure
- Form-filling approach kills collaborative potential
- No user review/refinement between sections
- Overwhelming steps (2, 3, 4 dump entire table structures)
- No facilitation language or progressive questioning
- Menu disconnected from creation flow
- No error handling or guidance for stuck users

### Critical Issues
- Zero BMAD compliance
- Would fail as an AI-facilitated workflow — presents as a document template, not a guided experience
- No state tracking means no session resume capability

### Recommendation: **Major Rework — Full BMAD Conversion Required**

The domain content is excellent and should be preserved. The architecture must be completely rebuilt as BMAD step-file workflow with collaborative facilitation replacing form-filling.

---

## Plan Quality Validation

### No Plan File Found

No `workflow-plan.md` exists at `_bmad/cpm/workflows/style-guide/workflow-plan.md`.

This workflow was built without the BMAD create-workflow process. A workflow plan should be created as part of the BMAD conversion to define:
- Step breakdown and routing
- Template type (likely free-form with polish)
- Collaborative facilitation approach
- Output file structure and variables

### Plan Quality Status: N/A — No plan file exists

---

## Summary

**Validation Completed:** 2026-02-06
**Overall Status:** ❌ FAIL — Full BMAD Conversion Required

### Validation Results

| Check | Result |
|-------|--------|
| File Structure & Size | ❌ FAIL — Monolithic, no step files |
| Frontmatter Validation | ❌ FAIL — No step frontmatter, unused variable |
| Critical Path Violations | ❌ FAIL — 4 hardcoded paths, no config variables |
| Menu Handling | ❌ FAIL — No handlers, no execution rules |
| Step Type Validation | ❌ FAIL — Zero step files, all inline |
| Output Format | ❌ FAIL — No templates, no tracking, no progressive build |
| Validation Design | ⚠️ WARNING — Not critical but no infrastructure |
| Instruction Style | ❌ FAIL — Form-filling instead of intent-based |
| Collaborative Experience | ❌ FAIL — 2/5 stars, form-like delivery |
| Subprocess Optimization | N/A — Requires conversion first |
| Cohesive Review | Needs Major Rework |
| Plan Quality | N/A — No plan file |

### Critical Issues (Must Fix): 9
### Warnings: 2
### Passes: 0

### Key Strengths to Preserve
- Excellent domain knowledge (lighting, color, camera, vocabulary)
- Strong visual identity concept
- Good example content (Edward Hopper cyberpunk example)
- Clear 4-document output structure
- Comprehensive coverage of style guide topics

### Recommendation: Full BMAD Conversion

This workflow has **strong domain content** trapped in a **non-BMAD monolithic architecture**. It should be converted to a full BMAD step-file workflow that:

1. Creates a `workflow-plan.md` documenting the design
2. Builds `steps-c/` folder with 6-8 individual step files
3. Transforms table dumps into collaborative conversations
4. Adds proper frontmatter, menus, execution rules per step
5. Creates `templates/` with output document templates
6. Extracts reference data to `data/` folder
7. Adds `steps-e/` for edit mode (modify existing style guide)
8. Considers `steps-v/` for lightweight validation (hex code checks, consistency)
9. Replaces hardcoded paths with `{variable}` format
10. Implements progressive output building with state tracking

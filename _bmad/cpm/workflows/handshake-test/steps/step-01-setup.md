---
name: 'step-01-setup'
description: 'Create minimal test project with fixture files for the handshake test'

nextStepFile: './step-02-shard-a.md'
testFixtures: '../data/test-fixtures.md'
---

# Step 1: Test Setup

## STEP GOAL:

Create a minimal CPM test project with all required fixture files so the shard-generation ritual can run against it.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in Test Coordinator style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Test Coordinator** — objective, procedural, validates results
- ✅ This is a TEST PROTOCOL, not creative facilitation
- ✅ Fixtures are intentionally minimal — do not embellish them

### Step-Specific Rules:

- 🎯 Focus only on creating the test project directory and fixture files
- 🚫 FORBIDDEN to modify fixture content (they are standardized test inputs)
- 🚫 FORBIDDEN to start any shard generation yet
- 💬 Approach: Direct, procedural, efficient

## EXECUTION PROTOCOLS:

- 🎯 Create test project directory structure
- 💾 Write all fixture files from {testFixtures}
- 📖 Verify all files were created
- 🚫 This is setup only — no shard generation

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Announce Test Protocol

Display:

"**Two-Shard Handshake Test**

I'm the Test Coordinator. I orchestrate the validation protocol that proves CPM maintains continuity across shard boundaries.

**The test runs 4 steps:**
1. Setup — Create minimal test project (this step)
2. Shard A — Hero picks up the Silver Key
3. Shard B — Continuity check (NO hints given)
4. Validate & Report — Check success criteria

**Pass threshold:** 3 consecutive PASS results = CPM VALIDATED

Setting up test fixtures..."

### 2. Get Test Project Location

Ask the user:

"**Where should I create the test project?**

Default: `{project-root}/_bmad-output/handshake-test`

Press Enter for default, or provide a path."

Wait for user response. Store as `{test_project_root}`.

### 3. Load Test Fixtures

Load {testFixtures} for all file definitions and the directory structure.

### 4. Create Directory Structure

Create the following directories at `{test_project_root}`:

```
.cpm/
Bible/
Bible/Characters/
Architecture/
Production/
Production/Scenes/
Production/Scenes/Scene_01/
Production/Scenes/Scene_01/state/
Output/
Output/Prompts/
```

### 5. Write Fixture Files

Write each file from {testFixtures} to its specified path under `{test_project_root}`:

1. `.cpm/config.yaml`
2. `.cpm/manifest.md`
3. `Bible/Show_Bible.md`
4. `Bible/Characters/hero.md`
5. `Architecture/Style_Guide.md`
6. `Architecture/Vocabulary.md`
7. `Production/Scenes/Scene_01/beat_sheet.md`

### 6. Verify Setup

Confirm all files were created by listing the test project directory.

Display:

```
✅ TEST PROJECT CREATED at {test_project_root}

Files:
  .cpm/config.yaml          ✅
  .cpm/manifest.md           ✅
  Bible/Show_Bible.md        ✅
  Bible/Characters/hero.md   ✅
  Architecture/Style_Guide.md ✅
  Architecture/Vocabulary.md  ✅
  Production/Scenes/Scene_01/beat_sheet.md ✅

Test fixtures ready. Proceeding to Shard A...
```

### 7. Auto-Proceed to Shard A

**No menu needed** — Auto-proceed to {nextStepFile}.

Load, read entirely, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- All 7 fixture files created at correct paths
- Directory structure matches specification
- Fixture content matches {testFixtures} exactly (no embellishment)
- Auto-proceeded to step-02

### ❌ SYSTEM FAILURE:

- Missing any fixture file
- Modifying fixture content (test inputs are standardized)
- Starting shard generation in this step
- Not verifying file creation

**Master Rule:** Fixtures are standardized. Write them exactly as specified. Do not add, remove, or modify any content.

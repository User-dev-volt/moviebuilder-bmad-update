# CPM Next Steps

Your module structure is built and registered. Here's the path to completion.

---

## Current Status

**Phase 1 COMPLETE:** All 4 agents validated (YAML format).
**Phase 2 COMPLETE:** All 6 workflows converted to BMAD step-file architecture.
**Phase 3 COMPLETE:** CPM registered in BMAD manifests + 10 slash commands + CLAUDE.md updated.
**Phase 4 IN PROGRESS:** 6/7 workflows tested. /cpm-scene-create ✅ tested 2026-02-21. /cpm-shard-generation ✅ Shard 1 tested 2026-02-21. /cpm-handshake-test — READY.

---

## Phase 4: Test Workflows — In Progress

| Test | Command | Status | Notes |
|------|---------|--------|-------|
| 1 | `/cpm-new-project` | ✅ DONE | Scaffolded "The Second Receipt" |
| 2 | `/cpm-show-bible` | ✅ DONE | Full 8-step Bible completed |
| 3 | `/cpm-style-guide` | ✅ DONE | 9 steps, 6 sections, 3 supporting docs |
| 4 | `/cpm-character-create` | ✅ DONE | Elias + Mara complete (8 steps each) |
| 5 | `/cpm-scene-create` | ✅ DONE | Scene 01 "The Functional Ghost" created 2026-02-21 (6 shards, Elias solo) |
| 6 | `/cpm-shard-generation` | ✅ DONE (Shard 1) | Scene 01 Shard 1 generated 2026-02-21. Exit state + prompt confirmed. Continue for shards 2-6. |
| 7 | `/cpm-handshake-test` | 🔜 READY | All blockers cleared — run 3 consecutive passes |

**YOU ARE HERE:** Run `/cpm-handshake-test` — 3 consecutive passes required to declare CPM validated.

---

## Fix A: Style Guide — Show Bible Awareness (Minor)

**Problem:** When `/cpm-style-guide` presents the mode selection menu, the `[C]reate` option gives no indication that a Show Bible can/should be used as creative foundation. Users don't know to expect Show Bible context.

**File:** `_bmad/cpm/workflows/style-guide/workflow.md`

**Change:** In the INITIALIZATION SEQUENCE → Mode Determination block, update the mode selection menu to:

```
"Welcome to the Cinematic Style Guide workflow! What would you like to do?

**[C]reate** - Build a new Style Guide through collaborative exploration
         *(Has a Show_Bible.md? I'll use it as our visual foundation.)*
**[V]alidate** - Check an existing Style Guide for internal consistency
**[E]dit** - Modify specific sections of an existing Style Guide

Please select: [C]reate / [V]alidate / [E]dit"
```

**Also in step-01-init.md:** Confirm that it already checks for Show Bible and loads it if found. If it doesn't, add: after presenting the welcome, check for `{project-root}/Bible/Show_Bible.md` — if found, load it and say "I found your Show Bible. I'll use it as context throughout our session."

**This is a direct file edit** — no Builder needed. Small wording change.

---

## Fix B: Character Create — Status Option Clarity (Minor)

**Problem:** When `/cpm-character-create` asks for character status (`ACTIVE / DECEASED / FLASHBACK_ONLY`), users don't understand what each means in production terms — specifically what state tracking each status receives.

**File:** `_bmad/cpm/workflows/character-create/steps-c/step-02-basic-identity.md`

**Change:** In the "Determine Character Status" section, update the option descriptions:

```
**[A]CTIVE** — On-screen in the current timeline. Receives full mutable state tracking:
             outfit, inventory, physical condition, and arc position update every shard.

**[D]ECEASED** — No longer alive in the current timeline. Appears in flashback sequences
              only. State is fixed at time of death — no ongoing tracking.

**[F]LASHBACK_ONLY** — Alive, but scoped entirely to past-timeline scenes. Does not appear
                     in current-timeline shards. No current continuity tracking needed.
```

**This is a direct file edit** — no Builder needed. Wording update only.

---

## Fix C: Scene Create Workflow — CRITICAL BLOCKER

**Problem:** `/cpm-shard-generation` requires scene context that does not exist. Two specific gaps:

1. **No scene brief file** — Shard-generation's Showrunner (step-03) must analyze "what happens in Shard {N}" but no file defines the beats. Without a scene brief, Albus invents beats from scratch with no filmmaker direction.
2. **step-02 (context-loading) doesn't load the scene brief** — Even when scene briefs exist, shard-generation's context loader doesn't read them.
3. **Manifest doesn't have scene entries** — The `.cpm/manifest.md` has no scene rows because nothing created them.

**Fix requires two actions:**

### Action C1: Build `/cpm-scene-create` Workflow

Use the BMB Workflow Builder in a fresh context window. Copy-paste prompt below.

### Action C2: Fix Shard-Generation Context Loading

After scene-create is built, update `shard-generation` to load the scene brief:

- **`data/context-loading-checklist.md`** — Add scene brief as a required file:
  ```
  | Scene Brief | `{project-root}/Production/Scenes/Scene_{XX}/scene-brief.md` | YES — always |
  ```
- **`steps/step-02-context-loading.md`** — After loading manifest (section 2), add:
  ```
  **Scene Brief:**
  - Load `{productionScenesPath}/Scene_{sceneNumber}/scene-brief.md`
  - **HALT if file does not exist**
  ```
- **`steps/step-03-showrunner-review.md`** — Add scene brief to REQUIRED INPUTS list and reference it in the Atomic Beat Breakdown section: "Refer to the scene-brief.md beats for this shard's defined action."

**Action C2 is direct file edits** — no Builder needed after you understand what scene-brief.md contains.

---

### Builder Prompt — `/cpm-scene-create` Workflow

Run this in a **fresh context window** using `/bmad-bmb-workflow`:

```
Build a new CPM workflow called `scene-create`.

## Reference Material

Read the CPM module brief at:
`_bmad-output/bmb-creations/modules/module-brief-cpm.md`

Use your best judgement for all design decisions based on this brief. Do NOT ask discovery questions that the brief answers.

## What This Workflow Does

`/cpm-scene-create` is the missing production step between `/cpm-character-create` and
`/cpm-shard-generation`. It creates scene brief files and scaffolds the scene folder
structure that shard-generation depends on. Without scenes, the production loop cannot run.

## What the Workflow Must Produce

For each scene:
1. `Production/Scenes/Scene_{XX}/scene-brief.md` — Scene definition with beats (see format below)
2. `Production/Scenes/Scene_{XX}/state/` — Empty folder (shard-generation populates this)
3. Update `.cpm/manifest.md` — Add scene entry with on-camera characters and shard count

## Scene Brief Format (scene-brief.md)

The scene-brief.md is the primary input the Showrunner reads during shard generation. It must include:

```yaml
---
scene_number: "01"
scene_id: SCENE_01
status: not-started
shard_count: 4
on_camera_characters:
  - CharacterName1
  - CharacterName2
---
```

```markdown
# Scene 01: {Scene Title}

## Setting
- **Location:** {specific location within the production's world}
- **Time of Day:** {morning / midday / golden hour / night / etc.}
- **Atmosphere:** {weather, light quality, environmental conditions}

## Narrative Purpose
{1-2 sentences: what this scene accomplishes in the story arc}

## Emotional Arc
- **Opens at:** {emotional tone at scene start}
- **Closes at:** {emotional tone at scene end}

## Beats

### Shard 1
- **Action:** {what physically happens — specific, observable, 5-8 seconds}
- **Character Focus:** {who the camera emphasizes}
- **Emotional Note:** {the feeling of this moment}

### Shard 2
...
```

## Manifest Update Format

The `.cpm/manifest.md` must be updated with a scene block:

```markdown
## Scene 01
status: not-started
on-camera-characters:
  - CharacterName1
  - CharacterName2
shard-count: 4
```

## Important Design Constraints

- **Shard beats must be filmmaker-directed, not AI-invented** — the collaborative process
  must get specific beats from the user. Each beat is a 5-8 second moment with a clear
  physical action. This is the creative core of the workflow.
- **Characters must exist** — when gathering on-camera characters, the workflow must verify
  each name exists in `Bible/Characters/`. HALT and warn if a character file is missing.
- **Beat count = shard count** — the number of beats defined becomes the shard_count in
  the manifest. This number matters for shard-generation's "next" shortcut logic.

## Workflow Archetype

This is a **Creative Facilitation** workflow (same archetype as character-create):
- Use `steps-c/` folder (tri-modal: Create / Edit / Validate)
- Explore → Discuss → Formalize → Review pattern per section
- Collaborative dialogue — do not ask the user to fill in a form
- Continuable across sessions (stepsCompleted tracking in frontmatter)

## Suggested Step Structure

1. **step-01-init** — Welcome, check for existing scenes (offer to continue), determine scene number, verify manifest exists. Continuable — loads step-01b if resuming.
2. **step-01b-continue** — Resume routing table (same pattern as character-create)
3. **step-02-setting** — Explore location, time, atmosphere collaboratively
4. **step-03-characters** — Select on-camera characters, verify each exists in Bible/Characters/
5. **step-04-narrative** — Define scene purpose + emotional arc (link to Show Bible themes if available)
6. **step-05-beats** — The creative core: build beats one by one. Each beat = one shard. Guide user through specificity ("what does Elias's hand DO?" not "they interact").
7. **step-06-polish** — Review full beat breakdown. Check: are beats specific? 5-8 seconds each? Is the emotional arc earned? Offer revision before finalizing.
8. **step-07-final** — Scaffold `Production/Scenes/Scene_{XX}/` folder, write scene-brief.md, update manifest, confirm completion with summary.

## Data Files Needed

- `data/beat-specificity-guide.md` — Examples of vague vs. specific beats, shard duration calibration guide (what can realistically happen in 5-8 seconds)
- `data/scene-structure-reference.md` — Scene types, emotional arc patterns, narrative function options

## Registration After Build

After the workflow is built:
1. Deploy to `_bmad/cpm/workflows/scene-create/`
2. Create `.claude/commands/cpm-scene-create.md` (follow existing CPM command file pattern)
3. Add to `_bmad/_config/workflow-manifest.csv`
4. Add to `_bmad/_config/bmad-help.csv` (phase: 3-production, sequence: before shard-generation)
5. Update `CLAUDE.md` CPM commands section with `/cpm-scene-create`

Use your best judgement for all remaining design details.
```

---

## After Fix C: Continue Phase 4 Testing

Once scene-create workflow is built and shard-generation's context loading is fixed:

| Step | Action |
|------|--------|
| 1 | Run `/cpm-scene-create` — create Scene 01 for "The Second Receipt" |
| 2 | Verify `Production/Scenes/Scene_01/scene-brief.md` created correctly |
| 3 | Verify `.cpm/manifest.md` updated with scene entry |
| 4 | Run `/cpm-shard-generation` — Scene 01, Shard 1 |
| 5 | Verify context loads, 4-agent ritual runs, prompt output created |
| 6 | Verify exit state file created at `Production/Scenes/Scene_01/state/shard_1_exit_state.md` |

---

## Phase 5: Run the Handshake Test (Final Validation)

**Command:** `/cpm-handshake-test`

**Success Criteria:**
- [ ] Key persists to Shard B (without human reminder)
- [ ] Scar stays on LEFT cheek
- [ ] Lighting matches Style Guide
- [ ] Position matches exit state

**Pass threshold:** 3 consecutive successful runs

---

## Priority Order — Complete Checklist

1. ✅ Validate agents with BMB
2. ✅ Convert all 6 workflows
3. ✅ Suite validation (2 fixes applied)
4. ✅ Create `config.yaml`
5. ✅ Register CPM in BMAD manifests
6. ✅ Create slash commands (10 files)
7. ✅ Test `/cpm-new-project`
8. ✅ Test `/cpm-show-bible`
9. ✅ Test `/cpm-style-guide`
10. ✅ Test `/cpm-character-create`
11. **[✅] Fix A** — style-guide Show Bible hint in menu — DONE (2026-04-22)
12. **[✅] Fix B** — character-create status clarity — DONE (2026-04-22)
13. **[✅] Fix C** — Built `/cpm-scene-create` workflow — DONE (14 files, 2026-02-20)
14. **[✅] Fix C2** — Shard-generation context loading patched — DONE (2026-02-20)
15. **[✅] Manifest template fixed** — ## Scenes section + /cpm-scene-create added — DONE
16. **[✅] Test `/cpm-scene-create`** — Scene 01 "The Functional Ghost" created 2026-02-21
17. **[✅] Test `/cpm-shard-generation`** — Scene 01 Shard 1 generated 2026-02-21
18. **[ ] Test `/cpm-handshake-test`** — 3 consecutive passes ← NEXT

---

## Files Reference

| What | Where |
|------|-------|
| Module | `_bmad/cpm/` |
| Agents (all validated) | `_bmad/cpm/agents/*.agent.yaml` |
| Workflows | `_bmad/cpm/workflows/*/workflow.md` |
| CPM Module Brief | `_bmad-output/bmb-creations/modules/module-brief-cpm.md` |
| Build Tracker | `_bmad-output/bmb-creations/modules/module-build-cpm.md` |
| Suite Validation Report | `_bmad/cpm/workflows/suite-validation-report.md` |
| Test Project | `_bmad-output/cpm-projects/The Second Receipt/` |

---

## Historical: Lessons Learned

**The BMB Workflow Builder process:** validate → fix → convert (step-00) → classify (step-02) → requirements (step-03) → tools (step-04) → plan review (step-05) → design (step-06) → foundation (step-07) → build step-01 (step-08) → build remaining steps (step-09) → confirm (step-10). ~12 builder steps per workflow, full context window each.

**What makes conversions fast:**
1. Front-load the CPM module brief — say "use your best judgement" to skip discovery Q&A
2. Skip post-validation steps once monolithic structure is confirmed

**Two Workflow Archetypes:**

| | Creative Facilitation | Procedural / Ritual |
|---|---|---|
| **Workflows** | show-bible, new-project, style-guide, character-create, **scene-create** | shard-generation, handshake-test |
| **Step folder** | `steps-c/` (tri-modal) | `steps/` (single-mode, CREATE-ONLY) |
| **Interaction style** | Explore → Discuss → Formalize → Review | Prescriptive, auto-proceed |
| **Menus** | A/P/C between steps | Auto-proceed, menu only at end |
| **Continuable** | Yes (stepsCompleted + step-01b routing) | No (fresh run each time) |

**Critical Pattern — Form-Filling → Collaborative Facilitation:**
Tables and structured output are the RESULT of conversation, not forms to fill. Monolithic files presented empty tables; converted workflows use Explore → Discuss → Formalize → Review. The beats section in scene-create is the same pattern — never ask the user to fill in a beats table.

**Cross-Workflow Dependencies:**
- `handshake-test` orchestrates `shard-generation` (loads its workflow.md)
- `shard-generation` depends on `scene-create` outputs (scene-brief.md + manifest entries)
- `scene-create` depends on `character-create` outputs (character files must exist)

---

## Historical: Converted Workflow Structures

**new-project/** (2026-02-05)
```
├── workflow.md
├── workflow-plan.md
├── steps-c/
│   ├── step-01-gather-details.md
│   ├── step-02-confirm-setup.md
│   ├── step-03-scaffold.md
│   └── step-04-completion.md
├── data/
│   └── directory-structure.md
└── templates/
    ├── config.yaml.template
    ├── manifest.md.template
    └── placeholder.md.template
```

**show-bible/** (2026-02-05)
```
├── workflow.md
├── workflow-plan.md
├── steps-c/
│   ├── step-01-init.md
│   ├── step-02-hook.md
│   ├── step-03-genre.md
│   ├── step-04-themes.md
│   ├── step-05-world.md
│   ├── step-06-arc.md
│   ├── step-07-motifs.md
│   └── step-08-compile.md
└── templates/
    └── show-bible.template.md
```

**style-guide/** (2026-02-06)
```
├── workflow.md
├── workflow-plan-style-guide.md
├── steps-c/ (10 files)
│   ├── step-01-init.md
│   ├── step-01b-continue.md
│   ├── step-02-visual-identity.md
│   ├── step-03-lighting.md
│   ├── step-04-color-palette.md
│   ├── step-05-camera-language.md
│   ├── step-06-spatial-rules.md
│   ├── step-07-vocabulary.md
│   ├── step-08-polish.md
│   └── step-09-final.md
├── steps-e/
│   └── step-e-01-assess.md
├── steps-v/
│   └── step-v-01-validate.md
├── data/
│   ├── lighting-reference.md
│   ├── lens-reference.md
│   └── color-theory-reference.md
└── templates/
    ├── style-guide.template.md
    ├── palette.template.md
    ├── lens-language.template.md
    └── vocabulary.template.md
```

**character-create/** (2026-02-16)
```
├── workflow.md
├── workflow-plan-character-create.md
├── steps-c/ (11 files)
│   ├── step-01-init.md
│   ├── step-01b-continue.md
│   ├── step-02-basic-identity.md
│   ├── step-03-visual-identity.md
│   ├── step-04-mutable-state.md
│   ├── step-05-behavioral-profile.md
│   ├── step-06-arc-position.md
│   ├── step-07-polish.md
│   └── step-08-final.md
├── steps-e/
│   └── step-e-01-assess.md
├── steps-v/
│   └── step-v-01-validate.md
├── data/
│   ├── arc-position-frameworks.md
│   ├── inventory-status-options.md
│   └── distinguishing-features-reference.md
└── templates/
    └── character.template.md
```

**shard-generation/** (2026-02-17)
```
├── workflow.md (CREATE-ONLY)
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
│   ├── context-loading-checklist.md
│   ├── state-diff-checklist.md
│   └── prompt-structure-template.md
└── templates/
    ├── prompt-output.template.md
    └── exit-state.template.md
```

**handshake-test/** (2026-02-17)
```
├── workflow.md (CREATE-ONLY)
├── steps/
│   ├── step-01-setup.md
│   ├── step-02-shard-a.md
│   ├── step-03-shard-b.md
│   └── step-04-validate-report.md
└── data/
    ├── test-fixtures.md
    └── success-criteria.md
```

---

## Historical: Suite Validation Results (2026-02-17)

Full report: `_bmad/cpm/workflows/suite-validation-report.md`

| # | Severity | Issue | Resolution |
|---|----------|-------|------------|
| X1 | CRITICAL | `_bmad/cpm/config.yaml` missing | ✅ FIXED |
| X2 | CRITICAL | style-guide stuck in bmb-creations output | ✅ FIXED — deployed |
| X3 | CRITICAL | handshake-test referenced wrong config | ✅ FIXED |
| 4 | HIGH | character-create step-04 at 284 lines (max 250) | DEFERRED — accuracy requires it |

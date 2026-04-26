---
stepsCompleted: ['step-01-discovery', 'step-02-classification', 'step-03-requirements', 'step-04-tools', 'step-05-plan-review', 'step-06-design', 'step-07-foundation']
status: APPROVED_FOR_DESIGN
approvedDate: 2026-02-20
---

# Workflow Creation Plan: scene-create

## Discovery Notes

**User's Vision:**
`/cpm-scene-create` is the missing production step between `/cpm-character-create` and `/cpm-shard-generation`. It creates scene brief files and scaffolds the scene folder structure that shard-generation depends on. Without it, the Showrunner invents beats from scratch with no filmmaker direction — and the production loop cannot run.

**Who It's For:**
CPM filmmakers who have completed their Show Bible, Style Guide, and character files, and are now ready to define what actually happens scene-by-scene before generating shards.

**What It Produces:**
- `Production/Scenes/Scene_{XX}/scene-brief.md` — Scene definition with beats (one beat = one shard)
- `Production/Scenes/Scene_{XX}/state/` — Empty folder (shard-generation populates this)
- Updated `.cpm/manifest.md` — Scene entry with on-camera characters and shard count

**Key Insights:**
- Beats must be filmmaker-directed, not AI-invented (this is the creative core)
- Characters must be verified against Bible/Characters/ before proceeding
- Beat count = shard_count in manifest (matters for shard-generation logic)
- Same Creative Facilitation archetype as character-create (Explore → Discuss → Formalize → Review)

---

## Classification Decisions

**Workflow Name:** `scene-create`
**Target Path:** `_bmad/cpm/workflows/scene-create/`
**Plan Doc Path:** `_bmad-output/bmb-creations/workflows/scene-create/`

**4 Key Decisions:**
1. **Document Output:** true — produces `scene-brief.md`
2. **Module Affiliation:** CPM — `_bmad/cpm/workflows/scene-create/`
3. **Session Type:** Continuable — complex creative process, may span sessions
4. **Lifecycle Support:** Tri-modal — Create + Edit + Validate

**Structure Implications:**
- Needs `steps-c/`, `steps-e/`, `steps-v/`
- Needs `step-01b-continue.md` for resume routing
- `stepsCompleted` tracked in `scene-brief.md` frontmatter
- `targetWorkflowPath = _bmad/cpm/workflows/scene-create/` (NOT bmb-creations)

---

## Requirements

**Flow Structure:**
- Pattern: Linear with one loop (beats phase loops until filmmaker is done)
- Phases: Init → Setting → Characters → Narrative → Beats (loop) → Polish → Final
- Estimated steps: 8 (step-01-init, step-01b-continue, step-02 through step-07)

**User Interaction:**
- Style: Highly collaborative (Creative Facilitation archetype)
- Decision points: Character verification (HALT if missing), beats loop (A/Done), polish revision gate
- Checkpoint frequency: Every step (A/P/C menus); auto-proceed only on step-01

**Inputs Required:**
- Required: `.cpm/manifest.md` must exist (HALT if not — need new-project first)
- Required: Each on-camera character must have a file in `Bible/Characters/`
- Optional: `Bible/Show_Bible.md` — loaded for narrative/theme context if found

**Output Specifications:**
- Type: Document — `scene-brief.md`
- Format: Structured (defined schema with frontmatter + markdown sections)
- Sections: frontmatter metadata, Setting, Narrative Purpose, Emotional Arc, Beats

**Success Criteria:**
- `Production/Scenes/Scene_{XX}/scene-brief.md` written with complete, specific beats
- `Production/Scenes/Scene_{XX}/state/` folder exists
- `.cpm/manifest.md` updated with scene entry
- All beats are specific and actionable (5-8 seconds, physical action)

**Instruction Style:**
- Overall: Mixed
- Creative phases (setting, beats): intent-based — guide conversation
- Verification phases (character check, manifest check): prescriptive — explicit HALT rules
- Final phase: prescriptive — exact file operations

---

## Tools Configuration

**Core BMAD Tools:**
- **Party Mode:** Available at all A/P/C menus
- **Advanced Elicitation:** Available at all A/P/C menus
- **Brainstorming:** Not included — workflow is already facilitated

**LLM Features:**
- **File I/O:** YES — read manifest, read character files, write scene-brief.md, update manifest, create state/ folder
- **Web-Browsing:** No
- **Sub-Agents:** No
- **Sub-Processes:** No

**Memory:**
- Type: Continuable
- Tracking: `stepsCompleted` array + `lastStep` in scene-brief.md frontmatter

---

## Step Design

| Step | File | Type | Goal |
|------|------|------|------|
| 1 | step-01-init.md | Init (Continuable) | Welcome, verify manifest, determine scene number, create file |
| 1b | step-01b-continue.md | Continuation | Resume from stepsCompleted |
| 2 | step-02-setting.md | Middle (Standard) | Explore location, time, atmosphere collaboratively |
| 3 | step-03-characters.md | Middle (Standard) | Select on-camera characters, verify each exists |
| 4 | step-04-narrative.md | Middle (Standard) | Define scene purpose + emotional arc |
| 5 | step-05-beats.md | Middle (Loop) | Build beats one by one — creative core |
| 6 | step-06-polish.md | Polish | Review all beats for specificity + arc; offer revision |
| 7 | step-07-final.md | Final | Scaffold folder, write scene-brief.md, update manifest |

**Supporting Files:**
- `data/beat-specificity-guide.md` — Vague vs. specific beat examples; 5-8 second calibration
- `data/scene-structure-reference.md` — Scene types, emotional arc patterns, narrative functions
- `templates/scene-brief.template.md` — Output template with frontmatter schema

**Edit/Validate:**
- `steps-e/step-e-01-assess.md` — Load existing scene brief, present edit options
- `steps-v/step-v-01-validate.md` — Check scene brief completeness and beat specificity

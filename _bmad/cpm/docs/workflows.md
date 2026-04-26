# Workflows Reference

CPM includes 6 workflows organized into Production and Setup categories:

---

## Production Workflows

### Shard Generation Ritual

**Command:** `/cpm-shard-generation`
**Purpose:** The 6-step mandatory sequence for generating AI video prompts

This is the core workflow. Every shard must go through this ritual.

**The 6 Steps:**
1. **Context Loading** — Read all required files for the scene
2. **Showrunner Review** — Story alignment and beat breakdown
3. **Cinematographer Specs** — Visual specifications
4. **Script Supervisor Validation** — Continuity check and injections
5. **Prompt Compilation** — Generate final AI-ready prompt
6. **State Update** — Record exit state for next shard

**Critical Gate:** State-Diff Check before Step 5
- Previous shard exit state was read
- All character states are current
- All injections have been applied
- Handshake is defined

**If any check fails → HALT and fix before compiling.**

**Output:**
- `Output/Prompts/Scene_{XX}_Shard_{Y}_prompt.md`
- `Production/Scenes/Scene_{XX}/state/shard_{Y}_exit_state.md`

---

### Handshake Test

**Command:** `/cpm-handshake-test`
**Purpose:** Two-shard validation protocol to prove CPM maintains continuity

This validates that the entire system works without human intervention.

**Test Setup:**
- One character with distinctive feature (scar)
- One item to be acquired (Key)
- Basic Style Guide (one lighting rule)

**Test Procedure:**
1. Run Shard A — Hero picks up Key
2. Record exit state
3. Run Shard B — WITHOUT reminding about Key
4. Validate Script Supervisor catches it automatically

**Success Criteria:**
- [ ] Shard B contains Key in hero's hand
- [ ] Shard B maintains distinctive feature (scar)
- [ ] Shard B honors Style Guide lighting
- [ ] Shard B starts with correct position
- [ ] ALL achieved WITHOUT human reminding

**Pass Threshold:** 3 consecutive successful runs = CPM VALIDATED

---

## Setup Workflows

### New Project

**Command:** `/cpm-new-project`
**Purpose:** Scaffold a new CPM cinematic project

Creates the complete directory structure and copies all templates.

**Creates:**
```
{project}/
├── .cpm/
│   ├── config.yaml
│   ├── manifest.md
│   └── agents/
├── Bible/
│   ├── Show_Bible.md
│   ├── Characters/
│   └── World/
├── Architecture/
│   ├── Style_Guide.md
│   ├── Palette.md
│   └── Vocabulary.md
├── Production/
│   ├── Slate.md
│   ├── Scenes/
│   └── Contracts/
└── Output/
    ├── Prompts/
    └── Renders/
```

**Configuration:**
- Project name
- Model target (Wan 2.2 / Sora / Kling / Runway)
- Shard duration
- Validation strictness

---

### Show Bible

**Command:** `/cpm-show-bible`
**Purpose:** Guided workflow to create your Show Bible

Walks you through each section:

1. **The Hook** — One-sentence logline
2. **Genre & Tone** — Genre, tone, comparables
3. **Thematic Pillars** — 2-3 themes your story explores
4. **World Rules** — Physics, society, technology
5. **Story Arc** — Act I, II, III structure
6. **Recurring Motifs** — Visual, dialogue, color motifs

**Output:** `Bible/Show_Bible.md`

---

### Style Guide

**Command:** `/cpm-style-guide`
**Purpose:** Create your visual style guide

Walks you through:

1. **Visual Identity Statement** — Overall philosophy
2. **Lighting Protocol** — Light sources with hex codes
3. **Color Palette** — Allowed/forbidden colors
4. **Camera Language** — Lens choices and rules
5. **Spatial Rules** — Composition and axis
6. **Prompt Vocabulary** — Banned/required words

**Output:**
- `Architecture/Style_Guide.md`
- `Architecture/Palette.md`
- `Architecture/Vocabulary.md`
- `Architecture/Lens_Language.md`

---

### Character Create

**Command:** `/cpm-character-create`
**Purpose:** Create a new character state file

Captures everything needed for continuity:

1. **Basic Identity** — Name, Asset ID, Status
2. **Visual Identity (Immutable)** — Face, body, distinguishing features
3. **Current Outfit (Mutable)** — What they're wearing now
4. **Inventory (Mutable)** — What items they have
5. **Physical State (Mutable)** — Injuries, conditions
6. **Behavioral Profile** — Speech, tics, signature moves
7. **Arc Position** — Emotional state, wants, needs

**Output:** `Bible/Characters/{name}.md`

**Critical:** Distinguishing features (scars, marks) must specify LEFT/RIGHT/LOCATION explicitly.

---

## Workflow Interaction Map

```
Setup Phase:
  new-project → show-bible → style-guide → character-create
                    ↓              ↓              ↓
                Bible/         Architecture/    Bible/Characters/

Production Phase:
  shard-generation ←→ (all files)
         ↓
  Output/Prompts/

Validation Phase:
  handshake-test → validates shard-generation
```

---

## Workflow Best Practices

### Before Production
1. Complete Show Bible — Don't start without story foundation
2. Complete Style Guide — Visual rules prevent drift
3. Create all on-camera characters — State tracking requires them

### During Production
1. Run full ritual for every shard — No shortcuts
2. Trust the State-Diff Check — If it fails, fix before continuing
3. Update state files — Exit states are handshakes to future shards

### Validation
1. Run Handshake Test early — Validates your setup
2. Document failures — They reveal weak points
3. Iterate agent prompts — Strengthen based on failures

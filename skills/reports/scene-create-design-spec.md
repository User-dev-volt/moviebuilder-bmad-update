---
title: 'Design Spec — cpm-scene-create'
status: 'spec'            # spec / not-yet-built — this document specifies the workflow; it does NOT build it
build_state: 'not-built'  # _bmad/cpm/ does not exist; only the V1 plan + proven outputs exist
skill_name: 'cpm-scene-create'
skill_type: 'workflow'
lifecycle: 'tri-modal'    # Create / Edit / Validate
backlog_position: 10      # skill #10 in the CPM build backlog
module_code: 'cpm'
authored: '2026-06-29'
source_plan: 'skills/reports/module-plan-cpm-v2.md (### cpm-scene-create)'
proven_reference: '_bmad-output/cpm-projects/The Second Receipt/Production/Scenes/Scene_01/scene-brief.md (V1, status: complete)'
builder: 'bmad-workflow-builder (BMB v2 — step-file SKILL.md, tri-modal Create/Edit/Validate)'
---

# Design Spec — `cpm-scene-create`

> **STATUS: SPEC / NOT-YET-BUILT.** This document specifies the `cpm-scene-create`
> workflow so it can be built later via the Workflow Builder (`bmad-workflow-builder`).
> It is the prerequisite the CPM build plan flags as missing: *"#10 cpm-scene-create —
> needs a design spec authored; none exists yet."* Nothing here is executable. Build via
> **Build a Workflow (BW)**, passing this spec + `skills/reports/module-plan-cpm-v2.md`
> as context.
>
> **Proven-output reference USED:** yes — `Scene_01/scene-brief.md` (V1, 6 beats, status
> complete) is the concrete output-format reference; its shape is **standardized** here.
> A second V1 brief (`Scene_02`) exists in a *divergent* shape; this spec reconciles the
> two into one canonical schema.

---

## 1. Purpose & Problem Solved

`cpm-scene-create` produces a **scene-brief.md**: a filmmaker-directed definition of every
beat in a scene, authored **up front**, before any shard is generated. Each beat is the
pre-commitment for exactly one shard.

**The problem it solves — Fix C2 (the load-bearing V1 lesson).** AI video generators are
stateless; CPM is the external state machine. During the Four-Agent Ritual
(`cpm-shard-generation`, #11), the Showrunner (Albus) must define the *current beat*. If no
scene-brief exists, **the Showrunner invents beats from scratch** with no filmmaker
direction — tested and confirmed in V1 as the failure that breaks narrative continuity and
drifts the production. The plan states it directly:

> *"Fix C2 (Critical): Shard-generation must load scene-brief.md and extract {currentBeat}.
> Without this, Showrunner invents beats — tested and confirmed."*
> — `module-plan-cpm-v2.md`, Ideas Captured

The scene-brief is therefore the filmmaker's **pre-authored beat contract**. The Showrunner
*loads* a beat instead of *inventing* one. In the CPLC mapping this is the **Beat Sheet /
Dev-Story equivalent**: the unit of work the production loop executes against.

**Hard dependency:** Without scene-briefs, `cpm-shard-generation` (#11) **cannot run** — its
Step 2 (Beat Extraction) has nothing to read. This is why #10 must ship before #11.

**Core outcome:** every shard the production will ever generate has a beat that was
*directed by a human filmmaker*, carrying a single non-negotiable Primary Requirement, and
extractable deterministically by integer shard number.

---

## 2. Pipeline Position

```
FOUNDATION (must exist first)                  THIS SPEC            CORE LOOP           VALIDATION
┌───────────────┐ ┌───────────────┐ ┌────────────────┐   ┌──────────────────┐   ┌──────────────────┐   ┌────────────────┐
│ cpm-new-      │→│ cpm-show-bible │→│ cpm-style-guide│ → │ cpm-character-   │ → │ ▶ cpm-scene-     │ → │ cpm-shard-     │ → cpm-handshake-test
│ project (#6)  │ │ (#7)           │ │ (#8)           │   │ create (#9)      │   │   create  (#10)  │   │ generation(#11)│
└───────────────┘ └───────────────┘ └────────────────┘   └──────────────────┘   └────────┬─────────┘   └────────┬───────┘
                                                                                          │ writes               │ reads scene-brief,
                                                                                          │ scene-brief.md        │ extracts {currentBeat}
                                                                                          ▼                       ▼
                                                                                   Showrunner (Albus) ── Scene Review + Beat Definition
```

- **Runs after** the foundation is in place: `.cpm/` project scaffold, `Bible/Show_Bible.md`,
  `Architecture/Style_Guide.md` (+ `Palette.md`, `Vocabulary.md`), and the
  `Bible/Characters/{Name}.md` files for everyone who will be on camera.
- **Runs before** `cpm-shard-generation` and is its prerequisite (Fix C2).
- **Consumed by** the **Showrunner (Albus)**:
  - *Scene Review* reads the whole brief (theme/arc check + emits its **beat breakdown table**).
  - *Beat Definition* extracts a single beat row by shard number → `{currentBeat}`.
- Invoked directly (`/cpm-scene-create`) or routed by the **Orchestrator (Orson)** —
  `route-to-agent.md` already lists: *"Creating a scene brief → cpm-scene-create workflow →
  bring Project folder path, Show Bible."*

---

## 3. Inputs

| Input | Required | Source | Notes |
|---|---|---|---|
| Project context (`.cpm/manifest.md`) | **Yes — HALT if absent** | Project folder | Confirms a CPM project exists. No manifest → HALT, route to `cpm-new-project`. |
| Scene concept | Yes | User (conversational) | What this scene is about; the spine the beats hang on. |
| On-camera characters | Yes | User | List of character **names**; each **must** resolve to `Bible/Characters/{Name}.md`. Missing file → HALT, offer `cpm-character-create`. |
| Setting | Yes | User | Location, time of day, atmosphere. |
| Arc position | Yes | User (+ `Show_Bible.md`) | Where the scene sits in the overall narrative (act/sequence). |
| Beat count | Yes | User | Number of beats = number of shards (`shard_count`). |
| Per-beat **Focus** | Yes (per beat) | User | Subject of attention + rough framing for that beat. |
| Per-beat **Primary Requirement** | Yes (per beat) | User | The single non-negotiable that beat must deliver (the anti-vagueness gate). |
| Shard duration (5 / 15 / 30s) | Yes (per beat) | `.cpm/config.yaml` `default_shard_duration`, override per beat | Drives `cpm-shard-generation` variable-interval choreography. |
| `Bible/Show_Bible.md` | Optional (recommended) | Project | Theme + arc context for Narrative Purpose. Degrade gracefully if absent. |
| `Architecture/Style_Guide.md`, `Palette.md` | Optional (recommended) | Project | Hex codes + visual law so Focus/Primary Requirement are written in canon. Degrade gracefully. |

---

## 4. Outputs

| # | Artifact | Path | Purpose |
|---|---|---|---|
| 1 | **scene-brief.md** | `Production/Scenes/Scene_{XX}/scene-brief.md` | The deliverable. Frontmatter + sections + Beat Table + Beat Details. |
| 2 | **Entry-state template** | `Production/Scenes/Scene_{XX}/state/entry_contract.md` | Seeds Shard 1's carry-in state for the Script Supervisor. (`state/` folder is scaffolded here.) |
| 3 | **Manifest update** | `.cpm/manifest.md` (bounded: `### Scenes` block + `Project Status` checkbox) | Registers the scene so the Orchestrator & shard-generation can find it. |
| 4 | **Slate update** | `Production/Slate.md` (Scenes status table + Production Log line) | Production status tracking. |

`{XX}` = zero-padded two-digit scene number (`01`, `02`, …).

---

## 5. scene-brief.md SCHEMA (canonical)

This schema **standardizes** the proven `Scene_01` shape and folds in the useful additions
from `Scene_02`, reconciling the two divergent V1 forms into one. The defining decision:

> **Two-layer Beats section.** A machine-read **Beat Table** (the four columns the plan says
> the Showrunner reads) is the *authoritative index*; prose **Beat Detail** blocks carry the
> filmmaker direction. The table is what makes `{currentBeat}` extraction deterministic; the
> details are what make the scene worth filming.

### 5.1 Frontmatter (YAML)

```yaml
---
# --- workflow state (managed by cpm-scene-create, Create mode) ---
stepsCompleted: []          # array of completed Create-mode stage ids (resume trail)
lastStep: ''                # last completed stage id (resume pointer)
# --- identity ---
scene_number: '01'          # STRING, zero-padded two digits
scene_id: 'SCENE_01'        # canonical id, MUST equal "SCENE_" + scene_number
scene_title: 'The Functional Ghost'
# --- production ---
status: 'ready'             # not-started | ready | in-progress | complete  (PRODUCTION status of the scene)
shard_count: 6              # INTEGER. MUST equal beat count = Beat Table rows = Beat Detail blocks = max(Beat)
default_shard_duration: 5   # seconds, inherited from .cpm/config.yaml; per-beat overrides live in the Beat Table
on_camera_characters:       # list of character NAMES; each MUST resolve to Bible/Characters/{Name}.md
  - Elias
arc_position: 'Act I — opening scene'
created: '2026-02-21'
lastModified: '2026-02-21'
---
```

**Field rules**
- `scene_id` **MUST** equal `"SCENE_" + scene_number` (Validate enforces).
- `shard_count` **MUST** equal beat count (Validate enforces all four equalities below in §9).
- `on_camera_characters` are **plain names** (`Elias`), not asset IDs. *(Standardization:
  Scene_02 used `ELIAS_V1`/`MARA_V1`; that is dropped here — the name resolves to the file,
  and the assetID is captured inside `entry_contract.md`, not the brief frontmatter.)*
- `status` lifecycle: `cpm-scene-create` sets **`ready`** on successful finalize (brief
  complete, shards not yet generated). `cpm-shard-generation` later flips it to
  `in-progress`/`complete`. *(Scene_01's `not-started` is the pre-standardization value.)*

### 5.2 Ordered section list

| Order | Section | Required | Source field shape |
|---|---|---|---|
| H1 | `# Scene {XX}: {Title}` | Yes | — |
| 1 | `## Setting` | Yes | **Location** / **Time of Day** / **Atmosphere** (bold sub-labels) |
| 2 | `## On-Camera Characters` | Optional (recommend for ≥2 chars) | per char: name → `Bible/Characters/{Name}.md` link → one-line role-in-scene |
| 3 | `## Narrative Purpose` | Yes | prose + **Serves theme:** line (names ≥1 Show Bible theme) |
| 4 | `## Emotional Arc` | Yes | **Opens at:** / **Closes at:** |
| 5 | `## Beats` | Yes | contains `### Beat Table` then `### Beat Details` |
| 5a | `### Beat Table` | Yes | the 4-column machine-read table (§5.3) |
| 5b | `### Beat Details` | Yes | `#### Beat {N} — {Title}` prose blocks (§5.4) |
| 6 | `## Continuity Carry-Out` | Optional | scene-level exit intent for the next scene (authoritative carry-out still comes from the last shard's exit state) |

### 5.3 The Beat Table (authoritative, machine-read) — **MUST align with the Showrunner**

Columns are **exactly** `Beat | Duration | Focus | Primary Requirement` — identical to the
plan's Memory Contract and to the Showrunner's *Scene Review* "beat breakdown table" output,
so consumption requires **zero transformation**.

```markdown
### Beat Table

| Beat | Duration | Focus | Primary Requirement |
|------|----------|-------|---------------------|
| 1 | 5s | Elias — face, 85mm clinical CU; RIGHT hand off-screen | Functional Ghost expression locked (jaw clenched, mouth a firm horizontal line); harsh Tablet Blue #5B8DD9 uplight from below; single precise RIGHT-hand swipe; no blink |
| 2 | 5s | Elias — LEFT wrist + RIGHT gloved finger, 100mm ECU | Smartwatch countdown visible on LEFT wrist; RIGHT gloved index taps glass once, cutting Sarah's voice; returns to symmetrical stillness |
| 3 | 5s | Elias — hands + paper, 85mm MCU | Repossession paper #F0F4F8 squared to perfect 90° against tablet edge with rigid RIGHT index finger (The Geometric Imposition); single jaw twitch at alignment |
| 4 | 5s | Elias — full body, 35mm tracking (exterior→hallway) | Car-door slam → plunge into System Green #8FBCAA fluorescent; RIGHT thumb traces LEFT glove seam (The Boundary Check); spine snaps vertical |
| 5 | 5s | Elias — full figure, 24mm wide, system dolly | Camera tracks backward matched to pace; metronomic march dead-center down peeling-linoleum hallway; Slate Blue #2C3E50 silhouette boxed by receding lines |
| 6 | 5s | Elias — LEFT fist + door, 85mm clinical CU | Stops with zero drift at chipped wooden door; LEFT glove curls to fist; strikes wood exactly 3 times (mathematically identical); freezes, eyes forward |
```

*(This table is the standardized form of the proven `Scene_01` 6 beats — content preserved,
shape canonicalized.)*

**Column definitions**
- **Beat** — integer `1..shard_count`, **contiguous, one row per integer**. This integer is
  the deterministic join key. **Beat N ⇄ Shard N (1:1).**
- **Duration** — target seconds for that beat's shard, ∈ `{5, 15, 30}`. Defaults to
  `default_shard_duration`; may be overridden per beat. This is the V2 variable-interval
  control: `cpm-shard-generation` passes it to the Prompt Engineer's *Variable Interval
  Compilation* (more micro-beats/choreography inside a 15s/30s shard; the 1:1 beat⇄shard
  mapping is unchanged).
- **Focus** — subject of attention + framing (which character/asset + lens). The character
  named here **must** be in `on_camera_characters`. *Names a character; never redefines that
  character's immutable identity — that lives in the character file (see §5.5).*
- **Primary Requirement** — the **single non-negotiable** that beat must deliver. This is the
  beat's load-bearing element: the Script Supervisor checks it, the Prompt Engineer
  front-loads it. **Must name ≥1 concrete, checkable element** (a hex code, a lens, a
  LEFT/RIGHT designation, a named prop, or a condition flag). Vague requirements fail Validate.
  This field is exactly what the Showrunner would otherwise *invent* — pre-authoring it here
  is the mechanical implementation of Fix C2.

### 5.4 Beat Details (filmmaker direction, prose)

One block per beat, **keyed by the same integer** as the table. Detail blocks **do not
restate** Duration or Primary Requirement (the table owns those — prevents drift; Validate
checks table↔detail consistency by integer).

```markdown
### Beat Details

#### Beat 1 — The Asset Scan
- **Action:** Elias, face locked in the Functional Ghost expression (jaw clenched, mouth a
  firm horizontal line), stares downward into harsh Tablet Blue (#5B8DD9) light from
  off-screen. He performs a single precise swipe with his RIGHT hand — just off-screen — and
  the blue light on his face flickers as the file turns. He does not blink.
- **Emotional Note:** Absolute Zero. A machine executing a routine command. No human cost registered.
- **Shot:** 85mm clinical close-up; key from below-screen tablet uplight only.
- **Continuity In:** (Beat 1 only) carry-in per `state/entry_contract.md`.
- **State Change:** none — arc holds at 0%.
```

**Beat Detail fields**
| Field | Required | Maps to V1 | Definition |
|---|---|---|---|
| **Action** | Yes | Scene_01 "Action" / Scene_02 "What happens" | The staged physical action — the meat of the shard. |
| **Emotional Note** | Yes | Scene_01 "Emotional Note" | The emotional state/shift the beat carries. |
| **Shot** | Recommended | Scene_02 "Shot" | Fuller camera spec (lens, movement, framing) beyond the table's one-line Focus. |
| **Continuity In** | Beat 1: yes (→ `entry_contract.md`); else optional | Scene_02 "Continuity from Scene_XX" | Carry-in state this beat assumes. |
| **State Change** | Optional | Scene_02 "State change" | What changes this beat: condition flags, inventory, arc % delta. Feeds the Script Supervisor's exit-state authoring downstream. |

### 5.5 Reference-don't-duplicate rule (DRY with the character file)

The scene-brief **references characters by name** and **never restates immutable visual
identity** (scar, hair part, build). Those live solely in `Bible/Characters/{Name}.md` (e.g.
Elias's *"faint crescent scar, half-inch, RIGHT lower jawline"*). The Beat Table's Primary
Requirement may *reference* such a feature as a checkable item (e.g. "RIGHT jawline scar must
read") but must not redefine it. This keeps the character file the single source of truth and
prevents drift. *(It also serves the Prompt Engineer's non-negotiable that critical features
land in the first 25% of the compiled prompt — pulled from the character file, anchored by
the brief's Focus + Primary Requirement.)*

---

## 6. Entry-state template — `state/entry_contract.md`

Seeds **Shard 1's** carry-in state (Shards 2..N validate against the *previous shard's*
`shard_{Y}_exit_state.md`, written later by the Script Supervisor). For **Scene 01** it is
derived from the characters' initial state; for **later scenes**, pre-populated from the prior
scene's last `shard_{last}_exit_state.md` if present, else emitted as a stub with `TODO`
markers (graceful degradation).

```markdown
---
scene_id: 'SCENE_01'
applies_to_shard: 1
derived_from: 'character-initial-state'   # or 'Scene_{XX-1}/state/shard_{last}_exit_state.md'
created: '2026-02-21'
---

# Entry Contract — Scene 01, Shard 1

## On-Camera Characters (carry-in)
### Elias — Bible/Characters/Elias.md (assetID ELIAS_V1)
- **Conditions (carry-in):** ACUTE_JAW_TENSION (active), RESTRICTED_BREATHING (active), THERMAL_RIGIDITY (active)
- **Inventory in-hand:** Tablet — LEFT (#5B8DD9 uplight); Repossession order — RIGHT (#F0F4F8, pristine)
- **Outfit:** per character file — charcoal-navy suit #2C3E50, thin black leather gloves, smartwatch #5B8DD9 (LEFT)
- **Arc progress (carry-in):** 0%

## Open Narrative Contracts (carry-in)
- (list active Production/Contracts/*.md, or "none")

## Setting at Entry
- **Location:** Elias's corporate sedan (sealed; Tablet Blue glow)
- **Light state:** Synthetic Cold — Tablet Blue #5B8DD9 only; no city bleed

## Notes to Script Supervisor (Jonas)
- Seed entry state. Validate Shard 1 against this; later shards validate against shard_{Y-1}_exit_state.md.
```

Condition-flag vocabulary (`ACUTE_JAW_TENSION`, etc.) and arc-progress-% conventions mirror
the character files exactly (see `Bible/Characters/Elias.md`, Physical State + Arc Position),
so the Script Supervisor's diff is apples-to-apples.

---

## 7. Manifest update — `.cpm/manifest.md` (bounded write)

`cpm-scene-create` writes **only** two regions of the manifest:

1. The **`### Scenes`** registry block (below the existing
   `<!-- scene-create updates this section automatically -->` marker), appending or replacing
   the entry for this scene:

   ```markdown
   ## Scene 01
   - **Title:** The Functional Ghost
   - **Status:** ready
   - **On-Camera Characters:** Elias
   - **Shard Count:** 6
   - **Brief:** `Production/Scenes/Scene_01/scene-brief.md`
   ```

2. The **Project Status** checkbox `- [x] Scenes defined …` once ≥1 scene exists.

It does **NOT** touch **Active Scene Context** (`Current Scene` / `Current Shard` /
`Characters On Camera`) — that live production cursor is owned by the Script Supervisor /
Orchestrator during `cpm-shard-generation`. *(This split is the proposed reconciliation of the
Memory Contract conflict — see §11 and Open Question O1.)*

---

## 8. Slate update — `Production/Slate.md`

Maintain a Scenes status table and append a Production Log line on finalize:

```markdown
## Scenes
| Scene | Title | Status | Shards | Brief |
|-------|-------|--------|--------|-------|
| 01 | The Functional Ghost | ready | 6 | Production/Scenes/Scene_01/scene-brief.md |

## Production Log
- 2026-02-21 — Scene 01 "The Functional Ghost" brief created (6 beats); status: ready.
```

Read by the Orchestrator's *Production Status Report* + *Production Diagram* capabilities.

---

## 9. Tri-modal workflow shape (Create / Edit / Validate)

Per BMB v2 conventions (`bmad-workflow-builder`): step-file SKILL.md, descriptive stage names
(no numbered prefixes on disk), resume via `stepsCompleted`, facilitator persona (operator is
the expert), graceful degradation, mode selected at activation from user intent.

### 9.1 CREATE mode (`steps-c/`)

Derived from the **proven V1 7-step sequence** (recorded in the proven brief's
`stepsCompleted`: init → setting → characters → narrative → beats → polish → final),
renamed to BMB v2 descriptive ids:

| Stage (id) | Goal | Key rules |
|---|---|---|
| **init** | New-vs-update gate (§10); verify `.cpm/manifest.md` (**HALT** if absent → `cpm-new-project`); determine scene number; create/locate `Scene_{XX}/` + brief; load Show Bible + Style Guide for context (degrade if absent). | Auto-proceed allowed; everything after gates on user input. |
| **setting** | Location, Time of Day, Atmosphere (collaborative). | Intent-based. |
| **characters** | Select on-camera characters; **verify each `Bible/Characters/{Name}.md` exists** (**HALT** / offer `cpm-character-create` if missing); record plain names. | Prescriptive verification. |
| **narrative** | Narrative Purpose (+ Serves-theme, checked against Show Bible) + Emotional Arc (Opens/Closes). | Intent-based. |
| **beats** | **Loop**: author each beat — Action, Focus, Primary Requirement, Emotional Note, Shot, optional Continuity In / State Change; set per-beat Duration (default from config, override allowed). Builds **both** the Beat Table and Beat Details. Continue until filmmaker says done. | Creative core; A/Done loop. Each Primary Requirement must name a concrete checkable element. |
| **polish** | Review all beats for specificity, arc coherence, contiguous 1:1 beat⇄shard, duration sanity; offer revision. Party Mode / Advanced Elicitation available. | Polish gate. |
| **finalize** | Scaffold `Scene_{XX}/state/`; write `scene-brief.md`; generate `entry_contract.md`; update manifest Scenes block + Project Status; update Slate; set `status: ready`; stamp `stepsCompleted`/`lastModified`. | Prescriptive; exact file ops. |

**Resume:** on activation against a partially complete brief, read `stepsCompleted` and route
to the next incomplete stage (the V1 plan's `step-01b-continue` role). Existing *complete*
briefs (Scene_01/02) won't trigger resume, so there is no migration burden.

**Supporting assets (recommended, per V1 plan):**
- `assets/scene-brief.template.md` — the §5 schema as a fill-in template.
- `assets/entry-contract.template.md` — the §6 template.
- `data/beat-specificity-guide.md` — vague-vs-specific beat examples; 5/15/30s calibration.
- `data/scene-structure-reference.md` — scene types, emotional-arc patterns, narrative functions.

### 9.2 EDIT mode (`steps-e/`)

Load the existing `scene-brief.md`; present an edit menu: **setting / characters / narrative /
edit a beat / add beat / remove beat / reorder beats / change durations / carry-out**. Rules:
- Any change to beat count **recomputes `shard_count`** and re-numbers beats to stay contiguous.
- Editing beats **re-syncs Beat Table ↔ Beat Details** (no drift) and re-runs the §9.4 checks.
- If shards were already generated (check Slate `status`/log), **warn** that removing/reordering
  beats may invalidate downstream shards before applying (surface the conflict first — per
  producing-workflow-patterns *Update mode*).
- On finalize: bump `lastModified`, re-sync manifest Scenes block + Slate.

### 9.3 VALIDATE mode (`steps-v/`)

Read-only; writes nothing the user must keep. Emits a per-check table + overall **PASS /
PASS WITH WARNINGS / FAIL**. Checks (§9.4).

### 9.4 Validate checks (the determinism + quality gate)

1. Frontmatter well-formed; `scene_id == "SCENE_" + scene_number`; `scene_number` zero-padded.
2. **The four-way equality** (deterministic-extraction precondition):
   `shard_count == Beat-Table row count == Beat-Detail block count == max(Beat)`.
3. `Beat` column is **contiguous integers `1..shard_count`**, exactly one row each.
4. Beat Table has **exactly** the columns `Beat | Duration | Focus | Primary Requirement`.
5. Every Beat Table row has a matching `#### Beat {N}` detail block and vice versa (by integer).
6. Each `on_camera_characters` entry resolves to `Bible/Characters/{Name}.md`.
7. Each beat: `Focus` non-empty; `Action` present; `Duration ∈ {5,15,30}`; **`Primary
   Requirement` names ≥1 concrete checkable element** (hex / lens / LEFT-RIGHT / named prop /
   condition flag) — the anti-vagueness gate.
8. `## Emotional Arc` has Opens/Closes; `## Narrative Purpose` names ≥1 theme.
9. `state/entry_contract.md` exists; manifest `### Scenes` has this scene; Slate has this scene.

A script (`scripts/validate_scene_brief.py`) should own checks 1–6 and 9 (pure structure —
determinism belongs in code); the model judges 7–8 (specificity is judgment). This split
follows BMB's intelligence-placement rule.

---

## 10. New-vs-Update clarity (the Fix-B analog)

`cpm-character-create` has **Fix B** ("step-02 status option must clearly distinguish
*creating new* vs *updating existing*"). `cpm-scene-create` needs the exact analog at **init**,
so "new scene" vs "update existing scene" is **unambiguous at entry** and an existing brief is
**never silently overwritten**:

Detection — given the target scene number, glob `Production/Scenes/Scene_{XX}/scene-brief.md`:

- **Absent → NEW scene.** Scaffold `Scene_{XX}/` + `state/`, create the brief, run Create mode.
- **Present → EXISTING scene.** Present an explicit choice, defaulting to the safe path:
  - **[E] Edit** this existing brief (→ Edit mode) ← default
  - **[V] Validate/view** it (→ Validate mode)
  - **[N] New** — a *different* scene (prompt for an unused number)
  - **[O] Overwrite** — **DESTRUCTIVE**; requires typed confirmation (e.g. type the scene id)

If the user launched in Create mode but the scene exists, **route to Edit rather than clobber**.
If intent is ambiguous, ask the one disambiguating question, then route (producing-workflow
*mode selection at activation, not a quiz*).

---

## 11. Memory-contract alignment

Citing the plan's **Memory Contract** table (`module-plan-cpm-v2.md` §Memory Contract):

| File | Plan row says | This workflow | Status |
|---|---|---|---|
| `Production/Scenes/{XX}/scene-brief.md` | Read by **Showrunner (extracts {currentBeat})**; **Written by cpm-scene-create** | **Writes** (Create/Edit); Showrunner reads | ✅ Clean — exactly as the plan states. |
| `Production/Slate.md` | Read by Orchestrator; **Written by All workflows on completion** | **Writes** on finalize | ✅ Clean — scene-create is one of "all workflows." |
| `.cpm/manifest.md` | Read by All; **Written by Orchestrator, Script Supervisor** | **Writes** the bounded `### Scenes` block + Project Status checkbox (§7) | ⚠️ **Conflict** — plan does not list scene-create as a manifest writer, yet the V1 manifest carries a `<!-- scene-create updates this section automatically -->` block. → **O1**. |
| `Production/Scenes/{XX}/state/entry_contract.md` | **Not in the table** (table lists `shard_{Y}_exit_state.md` only) | **Writes** the seed (§6); Script Supervisor + Prompt Engineer read it at Shard 1 | ⚠️ **Gap** — entry_contract.md is unlisted. → **O2**. |
| `Bible/Show_Bible.md` | Read by Showrunner | **Reads** (optional context) | ✅ Consistent with "Read by … ". |
| `Architecture/Style_Guide.md`, `Palette.md`, `Vocabulary.md` | Read by Cinematographer, Prompt Engineer | **Reads** (optional context, for in-canon hex/visual language) | ✅ Read-only, additive. |
| `Bible/Characters/{Name}.md` | Read by Showrunner/Script Supervisor/Prompt Engineer; written by character-create + Script Supervisor | **Reads** (existence check + assetID lookup); **never writes** | ✅ Read-only — DRY rule §5.5. |

**Proposed Memory-Contract amendments (need sign-off):**
- **O1:** add `cpm-scene-create` as a *bounded* writer of `.cpm/manifest.md` (scope: the
  `### Scenes` registry block + the `Scenes defined` Project-Status checkbox). Active Scene
  Context stays owned by Script Supervisor/Orchestrator.
- **O2:** add a Memory-Contract row for `Production/Scenes/{XX}/state/entry_contract.md` —
  **Written by** cpm-scene-create (seed) + Script Supervisor (updates); **Read by** Script
  Supervisor, Prompt Engineer (at Shard 1).

---

## 12. `{currentBeat}` extraction contract (how shard-generation reads this deterministically)

This is the mechanical fulfillment of Fix C2. `cpm-shard-generation` Step 2 (Beat Extraction):

1. Resolve `currentBeat = currentShardNumber` (the **1:1 integer mapping**).
2. Read `scene-brief.md` → `## Beats` → `### Beat Table` → the **row where `Beat ==
   currentShardNumber`**.
3. `{currentBeat}` = that row's `Duration | Focus | Primary Requirement` **plus** the matching
   `#### Beat {N}` detail block (Action, Emotional Note, Shot, Continuity In, State Change).

Determinism is guaranteed by the §9.4 schema invariants — contiguous integer `Beat` column,
one row per integer, `shard_count == max(Beat)`, table↔detail 1:1. There is **no fuzzy parsing
and no model judgment** in the lookup: it is an integer key. Because every beat is
pre-authored with a Primary Requirement, the **Showrunner *loads* the beat instead of
*inventing* it** — which is the entire point of this workflow.

---

## 13. Showrunner alignment (the brief FEEDS what Albus consumes)

| Showrunner capability (plan) | What it reads from the brief | Why the schema fits |
|---|---|---|
| **Scene Review** — thematic alignment + atomic beat breakdown | Narrative Purpose (theme check vs Show Bible), Emotional Arc, the **whole Beat Table**, Continuity Carry-Out | The Showrunner's output "beat breakdown table" has the **same four columns** as §5.3 — it can emit the brief's table with zero transformation. |
| **Beat Definition** — atomic beat with focus + primary requirement | The single Beat Table row + detail block for `{currentBeat}` | The brief's **Focus** and **Primary Requirement** columns are named to match the Showrunner's required outputs exactly. Pre-authored = not invented (Fix C2). |
| **Contract Management** | `## Continuity Carry-Out` + `entry_contract.md` open-contracts list | Surfaces which Narrative Contracts a scene plants/maintains/pays off. |

The column choice `Beat | Duration | Focus | Primary Requirement` is therefore **not arbitrary**
— it is the Showrunner's read/emit contract, made the brief's authored shape.

---

## 14. Acceptance criteria / Definition-of-Done (for the eventual build)

The built workflow is **done** when:

1. Skill exists at the BMB v2 output location (recommended `skills/cpm-scene-create/`, matching
   the already-built `skills/cpm-orchestrator/`; see **O4**) with: `SKILL.md`, `steps-c/`,
   `steps-e/`, `steps-v/`, `assets/scene-brief.template.md`, `assets/entry-contract.template.md`,
   `data/beat-specificity-guide.md`, `data/scene-structure-reference.md`,
   `scripts/validate_scene_brief.py`.
2. **Create** produces a `scene-brief.md` that **passes Validate** (§9.4) and conforms to the
   §5 schema. Re-creating Scene_01 from its inputs yields a Beat Table of **6 contiguous beats**
   whose content matches the proven brief (round-trip fidelity).
3. **Edit** can add/remove/reorder beats and change durations while keeping `shard_count`, Beat
   Table, Beat Details, manifest, and Slate **in sync**, surfacing downstream-invalidation
   conflicts before applying.
4. **Validate** catches: non-contiguous beats, table↔detail mismatch, `shard_count` drift,
   vague Primary Requirement, missing character file, malformed `scene_id`.
5. **New-vs-update gate** (§10) never silently overwrites; overwrite requires typed confirmation.
6. On finalize: `entry_contract.md` seeded, manifest `### Scenes` + Project Status updated,
   Slate scene row + log line written, scene `status: ready`.
7. **HALT conditions** honored: no `.cpm/manifest.md` → HALT (→ `cpm-new-project`); missing
   `Bible/Characters/{Name}.md` → HALT (→ `cpm-character-create`).
8. **End-to-end gate (verifiable once #11 exists):** a generated brief is consumed by
   `cpm-shard-generation`'s Beat Extraction with **zero ambiguity** — `{currentBeat}` resolves
   by integer for every shard `1..shard_count`.
9. `SKILL.md` within BMB token budget; passes `quick_validate.py`, `scan-path-standards.py`,
   `scan-scripts.py`; structure checks (§9.4 items 1–6, 9) implemented in the validation script,
   not the prompt.

---

## 15. Open questions / decisions needed before building

- **O1 — Manifest writer (Memory-Contract amendment).** Confirm `cpm-scene-create` may write
  the bounded `### Scenes` block + Project-Status checkbox in `.cpm/manifest.md` (recommended),
  vs. having the Orchestrator sync it. *Recommendation: scene-create owns the static Scenes
  registry; Script Supervisor/Orchestrator own Active Scene Context.*
- **O2 — `entry_contract.md` in the Memory Contract.** Confirm adding the row (writer:
  scene-create seed + Script Supervisor; readers: Script Supervisor, Prompt Engineer). Confirm
  the filename `entry_contract.md` (matches the plan's Memory Architecture diagram).
- **O3 — Beat⇄Shard cardinality under variable intervals.** Spec assumes **1 beat = 1 shard**,
  with Duration scaling choreography *inside* the shard (the plan's "multiple micro-beats within
  the shard"). Confirm this holds for 30s shards, because a beat-spans-multiple-shards model
  would break the integer extraction key in §12.
- **O4 — Output location.** `skills/cpm-scene-create/` (BMB v2 default, matches the built
  orchestrator) vs the V1 plan's `_bmad/cpm/workflows/scene-create/`. *Recommendation:
  `skills/cpm-scene-create/`* — but note `_bmad/cpm/` does not yet exist, so the module's final
  home is itself a pending decision (CPM is not built).
- **O5 — Scene `status` enum + transition ownership.** Confirm scene-create sets `ready` on
  finalize and `cpm-shard-generation` owns `in-progress`/`complete`. (Standardize away
  Scene_01's `not-started`.)
- **O6 — `Continuity Carry-Out` section: required or optional?** It overlaps the authoritative
  carry-out that the last shard's exit state produces during shard-generation. *Recommendation:
  optional scene-level *intent* note; authoritative carry-out remains the shard exit state.*
- **O7 — entry_contract pre-population vs stub.** For scenes after the first: pre-populate from
  the prior scene's last `shard_{last}_exit_state.md` when present, else emit a `TODO` stub
  (graceful degradation). For Scene 01, derive from character initial state. Confirm.
- **O8 — `on_camera_characters` representation.** Confirm **plain names** (resolve to file) over
  asset IDs (`ELIAS_V1`); assetID captured inside `entry_contract.md`. (Standardizes away the
  Scene_02 divergence.)
- **O9 — `model_target` quirk.** The proven project's `.cpm/manifest.md` says `Model Target:
  wan`, but the plan's config enum is `sora/kling/runway/pika`. Not blocking for scene-create
  (it doesn't read model target), but flag for `cpm-new-project`/config so the enum and real
  data agree.

---

## 16. Resolutions — DECIDED 2026-06-29 (supersede any stale text above)

**Format correction (this spec predates the locked workflow format).** Build `cpm-scene-create` exactly like the foundation workflows #6–#9: a single inline **`SKILL.md`** with **create / update / validate** intent modes — **NOT** the `steps-c/e/v` folders or `stepsCompleted` frontmatter described in §9/§14 — plus `customize.toml [workflow]`, `references/scene-brief-contract.md` (the R1 authority doc), `assets/` templates (`scene-brief.template.md`, `entry-contract.template.md`, the two `data/` guides), `scripts/validate_scene_brief.py` + `scripts/tests/`, and a runtime **memlog** beside the artifact for resume. The generated `scene-brief.md` **drops** the V1 `stepsCompleted`/`lastStep` frontmatter (R4 — build jargon in a shipped artifact); resume uses the memlog, mirroring #7–#9. Mirror the pattern-setter `skills/cpm-new-project` and apply R1–R6.

**Open-question outcomes:**
- **O1 — Manifest writer:** ✅ scene-create writes the bounded `### Scenes` block + the `Scenes defined` Project-Status checkbox; Active Scene Context stays with the Script Supervisor/Orchestrator. (Already pinned; #6's manifest skeleton carries the `<!-- scene-create updates this section automatically -->` marker.)
- **O2 — entry_contract in Memory Contract:** ✅ add the row — **writer:** cpm-scene-create (seed) + Script Supervisor (updates); **readers:** Script Supervisor, Prompt Engineer (at Shard 1). Filename `entry_contract.md`.
- **O3 — Beat⇄Shard cardinality:** ✅ **1 beat = 1 shard.** Duration (5/15/30s) scales choreography *inside* the single shard; the integer Beat column stays the deterministic join key for `{currentBeat}` (Fix C2).
- **O4 — Output location:** ✅ `skills/cpm-scene-create/`.
- **O5 — Scene status:** ✅ enum `ready → in-progress → complete`; scene-create finalizes a brief to `ready`; shard-generation owns `in-progress`/`complete`; `not-started` dropped.
- **O6 — Continuity Carry-Out:** ✅ **optional** scene-level intent note; the authoritative carry-out is the last shard's exit state.
- **O7 — entry_contract for later scenes:** ✅ **seed from the prior scene's last exit-state if present, else write an explicit gap-marked stub** ("unresolved — Script Supervisor fills before Shard 1") that Validate flags; non-blocking, never a silent hollow handoff. Scene 01 derives from character initial state.
- **O8 — on_camera_characters:** ✅ plain names resolving to `Bible/Characters/{Name}.md`; asset ID captured in `entry_contract.md`. (Drops Scene_02's `ELIAS_V1`.)
- **O9 — model_target:** ✅ non-issue — #6's config treats `model.target` as an open string (sora/kling/runway/pika + any id), so `wan` is valid. (Optional polish: add `wan` to the documented options comment in #6's config template.)

**Validate gate (§9.4) stands as specified** — the four-way equality (`shard_count == Beat-Table rows == Beat-Detail blocks == max(Beat)`), contiguous integer Beat column, exactly the 4 columns, table↔detail 1:1, character-file resolution, and the anti-vagueness Primary-Requirement check — with structure checks 1–6 & 9 in `validate_scene_brief.py` and 7–8 (specificity/theme) judged by the prompt. This is the R3 deterministic gate, exactly the split used by the check scripts in #7–#9.

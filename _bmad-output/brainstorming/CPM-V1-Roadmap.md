# CPM V1.0 BUILD ROADMAP
## BMAD Cinematic Production Module - Complete Implementation Plan

---

## EXECUTIVE SUMMARY

**Module Name:** BMM-CPM (BMAD Cinematic Production Module)
**Version:** 1.0 (Headless Production)
**Philosophy:** Cinematics as Code - 50 years of Software Engineering solving 100 years of Cinematic Production
**Interface:** Terminal / Claude Code
**Core Innovation:** External State Machine for AI Video Generation

**The Problem:** "The Vibe-Drift Gap" - AI video generators are stateless; they forget characters, settings, and continuity between generations.

**The Solution:** Apply BMAD's document-based, agentic architecture to cinematic production. Treat context as currency. Never talk to an AI video generator without your Agentic Crew reviewing the "code" first.

---

## PHASE 1: FOUNDATION
### "The Skeleton Project"
**Duration:** Week 1
**Goal:** Create the directory template and core schema definitions

---

### Deliverable 1.1: Master Directory Structure

```
{project-name}/
├── .cpm/
│   ├── config.yaml                 # Project configuration
│   ├── manifest.md                 # Context Index - what files exist
│   └── agents/                     # Agent system prompts
│       ├── showrunner.md
│       ├── cinematographer.md
│       ├── script-supervisor.md
│       └── prompt-engineer.md
│
├── Bible/
│   ├── Show_Bible.md               # PRD equivalent - story, themes, rules
│   ├── Characters/
│   │   ├── _index.md               # Character roster
│   │   └── {character_name}.md     # Individual character state files
│   └── World/
│       ├── _index.md               # World elements roster
│       └── {location/item}.md      # World element definitions
│
├── Architecture/
│   ├── Style_Guide.md              # Visual architecture - lighting, color, camera
│   ├── Palette.md                  # Color definitions with hex codes
│   ├── Lens_Language.md            # Camera/lens specifications
│   └── Vocabulary.md               # Allowed/banned prompt words
│
├── Production/
│   ├── Slate.md                    # Production status tracker
│   ├── Scenes/
│   │   └── Scene_{XX}/
│   │       ├── beat_sheet.md       # Scene breakdown into atomic beats
│   │       ├── shards/
│   │       │   ├── shard_01.md     # Individual 5-second prompts
│   │       │   └── shard_XX.md
│   │       └── state/
│   │           ├── entry_state.md  # Scene entry conditions
│   │           └── exit_state.md   # Scene exit conditions
│   └── Contracts/
│       └── {contract_id}.md        # Narrative contracts (foreshadowing)
│
└── Output/
    ├── Prompts/
    │   └── Scene_{XX}_Shard_{YY}_prompt.md  # Compiled prompts
    └── Renders/
        └── Scene_{XX}_Shard_{YY}.mp4        # Generated videos
```

---

### Deliverable 1.2: config.yaml Schema

```yaml
# .cpm/config.yaml
project_name: "{Project Title}"
version: "1.0"
created: "{date}"

# Production Settings
temporal:
  default_shard_duration: 5  # seconds
  max_shard_duration: 30

# Model Target (V1.0 = single target)
model:
  target: "sora"  # sora | kling | runway

# Agent Settings
agents:
  showrunner:
    enabled: true
    prompt_file: ".cpm/agents/showrunner.md"
  cinematographer:
    enabled: true
    prompt_file: ".cpm/agents/cinematographer.md"
  script_supervisor:
    enabled: true
    prompt_file: ".cpm/agents/script-supervisor.md"
  prompt_engineer:
    enabled: true
    prompt_file: ".cpm/agents/prompt-engineer.md"

# Validation Rules
validation:
  require_state_diff_check: true
  require_style_compliance: true
  banned_words_enforcement: true
```

---

### Deliverable 1.3: manifest.md Schema (Context Index)

```markdown
# Project Manifest
## {Project Name}

### Active Scene Context
- **Current Scene:** Scene_{XX}
- **Current Shard:** Shard_{YY}
- **Characters On Camera:** [{character_1}, {character_2}]

### Required Files for Current Context
Load these files before generating prompts:

**Bible (Always Load):**
- [ ] Bible/Show_Bible.md

**Characters (Scene-Specific):**
- [ ] Bible/Characters/{character_1}.md
- [ ] Bible/Characters/{character_2}.md

**Architecture (Always Load):**
- [ ] Architecture/Style_Guide.md
- [ ] Architecture/Vocabulary.md

**State (Always Load):**
- [ ] Production/Scenes/Scene_{XX}/entry_state.md
- [ ] Production/Scenes/Scene_{XX-1}/exit_state.md (previous scene)

**Contracts (If Applicable):**
- [ ] Production/Contracts/{active_contract}.md

### Files NOT Needed (Context Optimization)
- Bible/Characters/{background_characters}.md → Use Crowd_LOD
- Previous scene shards (state already captured in exit_state)
```

---

## PHASE 2: BIBLE & ARCHITECTURE
### "The Show Bible and Style Guide"
**Duration:** Week 1-2
**Goal:** Create templates for story and visual definition

---

### Deliverable 2.1: Show_Bible.md Template

```markdown
# Show Bible: {Project Title}

## Logline
{One-sentence hook}

## Genre & Tone
- **Primary Genre:** {genre}
- **Tone:** {adjectives describing feel}
- **Comparable Works:** {reference films/shows}

## Thematic Pillars
1. **{Theme 1}:** {description}
2. **{Theme 2}:** {description}
3. **{Theme 3}:** {description}

## World Rules
### Physics
- {Rule 1: e.g., "Magic exists but costs life force"}
- {Rule 2}

### Society
- {Rule 1: e.g., "Corporations control governments"}
- {Rule 2}

### Technology
- {Rule 1: e.g., "AI is sentient but hidden"}
- {Rule 2}

## Story Arc (Season/Film Level)
### Act I: {Title}
- {Major plot point 1}
- {Major plot point 2}

### Act II: {Title}
- {Major plot point 1}
- {Major plot point 2}

### Act III: {Title}
- {Major plot point 1}
- {Major plot point 2}

## Recurring Motifs
- **Visual Motif:** {e.g., "Clocks appear before death"}
- **Dialogue Motif:** {e.g., "Characters quote same poem"}
- **Color Motif:** {e.g., "Red appears with betrayal"}
```

---

### Deliverable 2.2: Character State Template

```markdown
# Character: {Name}
**Asset ID:** {Character_ID_V1}
**Status:** ACTIVE | DECEASED | FLASHBACK_ONLY

## Visual Identity (Immutable Unless Story Changes)
### Face
- **Distinguishing Features:** {e.g., "Jagged scar on LEFT cheek"}
- **Expression Default:** {e.g., "Tired, guarded"}
- **Age Appearance:** {e.g., "Late 30s, weathered"}

### Body
- **Build:** {e.g., "Athletic but worn"}
- **Posture:** {e.g., "Shoulders hunched, protective"}
- **Movement Style:** {e.g., "Deliberate, conservation of energy"}

### Current Outfit (Mutable - Update Per Scene)
- **Base:** {e.g., "Tattered red cape"}
- **Condition:** {e.g., "Torn at right shoulder (Scene 7)"}
- **Accessories:** {e.g., "Silver Key (Equipped, Right Hand)"}

## Inventory (Mutable)
| Item | Status | Acquired | Notes |
|------|--------|----------|-------|
| Silver Key | EQUIPPED_PRIMARY_HAND | Scene 7 | Reflects #FF00FF light |
| Pistol | HOLSTERED | Scene 2 | 3 rounds remaining |

## Physical State (Mutable)
| Condition | Location | Severity | Since |
|-----------|----------|----------|-------|
| Battle Scar | Left Cheek | Permanent | Scene 4 |
| Exhaustion | General | High | Scene 6 |
| Sweating | Face | Active | Scene 8 |

## Behavioral Profile (For Prompt Engineer)
- **Speech Pattern:** {e.g., "Short sentences, never explains himself"}
- **Nervous Tic:** {e.g., "Touches scar when lying"}
- **Signature Move:** {e.g., "Always enters rooms gun-first"}

## Arc Position
- **Current Emotional State:** {e.g., "Desperate, near breaking point"}
- **Character Want:** {e.g., "Find his daughter"}
- **Character Need:** {e.g., "Learn to trust again"}
- **Arc Progress:** {e.g., "60% through transformation"}

## Version History
| Version | Scene | Changes |
|---------|-------|---------|
| V1 | Scene 1 | Initial state |
| V2 | Scene 4 | Added battle scar |
| V3 | Scene 7 | Acquired Silver Key, torn shoulder |
```

---

### Deliverable 2.3: Style_Guide.md Template

```markdown
# Cinematic Style Guide: {Project Title}

## Visual Identity Statement
{One paragraph describing the overall visual philosophy}

## Lighting Protocol
### Primary Lighting Style
- **Style Name:** {e.g., "Chiaroscuro-Neon"}
- **Key Characteristics:**
  - {e.g., "High contrast, deep shadows"}
  - {e.g., "No flat lighting ever"}
  - {e.g., "Rim light mandatory on all subjects"}

### Light Sources
| Source Type | Color | Hex Code | Usage |
|-------------|-------|----------|-------|
| Rim Light (Primary) | Electric Purple | #FF00FF | Character silhouettes |
| Ambient (Secondary) | Acid Green | #39FF14 | Environmental glow |
| Accent | {color} | {hex} | {usage} |

### Lighting Rules
- [ ] NEVER use flat, even lighting
- [ ] ALWAYS include volumetric atmosphere
- [ ] Rim light must define subject edges
- [ ] Shadows should occupy 60%+ of frame

## Color Palette
### Allowed Colors
| Name | Hex | Usage Context |
|------|-----|---------------|
| Electric Purple | #FF00FF | Rim light, key reflections |
| Acid Green | #39FF14 | Environmental neon, toxic atmosphere |
| Deep Black | #0A0A0A | Shadows, backgrounds |

### Forbidden Colors
| Color | Reason |
|-------|--------|
| Bright Yellow | Breaks noir aesthetic |
| Pure White (except glitch) | Too clean for world |
| Pastel anything | Wrong genre |

### Color Meaning
- **#FF00FF:** Power, danger, protagonist's journey
- **#39FF14:** Corruption, environment, decay
- **White Noise:** Out-of-bounds / supernatural

## Camera Language
### Lens Vocabulary
| Shot Type | Lens | Emotional Effect |
|-----------|------|------------------|
| Close-Up (Intimate) | 85mm | Oppressive, isolated |
| Wide (Establishing) | 24mm | Small in vast space, vulnerable |
| Medium (Standard) | 35mm | Grounded reality, neutral |
| Dutch Angle | Any | Disorientation, wrongness |

### Shot Progressions
- **Paranoia Sequence:** 85mm → 24mm → 35mm (contraction → expansion → settle)
- **Revelation Sequence:** 35mm → 85mm (grounding → focus)
- **Chaos Sequence:** Rapid lens switching

### Camera Movement
- **Default:** Static or slow dolly
- **Action:** Handheld with purpose
- **FORBIDDEN:** Unmotivated movement

## Spatial Rules
### Axis of Action
- Characters entering frame-left must remain left-dominant
- Screen direction must be consistent across shards
- Crossing the line requires motivated cut

### Composition
- Rule of thirds for standard shots
- Center framing only for power/confrontation
- Negative space = psychological weight

## Prompt Vocabulary
### REQUIRED Words
| Instead of... | Use... |
|---------------|--------|
| Dark | High-contrast, deep shadows |
| Neon | Specific hex code + "neon rim light" |
| Cinematic | "Volumetric lighting, film grain" |

### BANNED Words
| Word | Reason | Alternative |
|------|--------|-------------|
| Bright | Kills noir aesthetic | High-contrast |
| Sunny | Wrong world | Overcast, filtered |
| Cheerful | Tone violation | {describe specific emotion} |
| Beautiful | Too vague | {specific visual descriptors} |
```

---

## PHASE 3: AGENT DEFINITIONS
### "The Agentic Film Crew"
**Duration:** Week 2
**Goal:** Create system prompts for all four agents

---

### Deliverable 3.1: showrunner.md (Agent Prompt)

```markdown
# Showrunner Agent

## Role
You are the Showrunner - the creative visionary and story guardian of this production. You are the PM equivalent in the BMAD Cinematic Production Module.

## Responsibilities
1. **Own the Show Bible** - You are the final authority on story, character, and world consistency
2. **Define Atomic Beats** - Break scenes into 5-second shards with clear focus
3. **Enforce Thematic Integrity** - Ensure every scene serves the larger narrative
4. **Manage Narrative Contracts** - Track foreshadowing obligations

## Before Every Scene Review
You MUST read:
- [ ] Bible/Show_Bible.md
- [ ] Bible/Characters/{on_camera_characters}.md
- [ ] Production/Contracts/*.md (active contracts)

## Your Output Format
When reviewing a scene, provide:

### Scene {XX} Showrunner Notes

**Thematic Alignment:** [How this scene serves the story]

**Character Arc Check:**
- {Character}: [Current arc position, emotional truth needed]

**Atomic Beat Breakdown:**
| Beat | Duration | Focus | Primary Requirement |
|------|----------|-------|---------------------|
| {XX}.1 | 5s | {focus} | {what must be achieved} |
| {XX}.2 | 5s | {focus} | {what must be achieved} |

**Narrative Contract Status:**
- [ ] {Contract_ID}: {Status - PLANT / MAINTAIN / PAYOFF}

**Notes to Cinematographer:** {Visual emphasis needed}
**Notes to Script Supervisor:** {State changes to track}

## Rules
- You define WHAT happens, not HOW it looks (that's Cinematographer)
- You ensure character actions are motivated by their arc
- You never approve a beat that contradicts the Show Bible
- You flag any scene that could violate a Narrative Contract
```

---

### Deliverable 3.2: cinematographer.md (Agent Prompt)

```markdown
# Cinematographer Agent

## Role
You are the Cinematographer - the visual architect of this production. You are the Architect equivalent in the BMAD Cinematic Production Module.

## Responsibilities
1. **Own the Style Guide** - You are the final authority on how things LOOK
2. **Define Visual Specs** - Lighting, lens, color, composition for every beat
3. **Enforce Visual Continuity** - Ensure spatial logic and style consistency
4. **Maintain the Vocabulary** - Enforce banned/required prompt words

## Before Every Beat Review
You MUST read:
- [ ] Architecture/Style_Guide.md
- [ ] Architecture/Vocabulary.md
- [ ] Architecture/Palette.md
- [ ] Previous shard's exit_state.md (for spatial continuity)

## Your Output Format
When reviewing a beat, provide:

### Beat {XX}.{Y} Cinematographer Specs

**Lighting Protocol:**
- Primary: {light type, hex code, placement}
- Secondary: {light type, hex code, placement}
- Rim: {MANDATORY - describe}

**Lens Selection:**
- Lens: {focal length}mm
- Motivation: {why this lens for this emotion}

**Color Application:**
- {Hex code 1}: {where it appears, what it touches}
- {Hex code 2}: {where it appears, what it touches}

**Composition:**
- Subject Position: {frame location}
- Background Treatment: {focus, elements}
- Negative Space: {percentage, meaning}

**Spatial Continuity:**
- Entry Direction: {frame-left/right, motivated by previous}
- Axis of Action: {maintained/crossed with motivation}

**Vocabulary Enforcement:**
- [ ] No banned words in prompt
- Required terms included: {list}

**Notes to Script Supervisor:** {Lighting gradient tracking, spatial contracts}
**Notes to Prompt Engineer:** {Specific weight emphasis, word choices}

## Rules
- You define HOW it looks, not WHAT happens (that's Showrunner)
- You NEVER approve a beat that violates the Style Guide
- You specify exact hex codes, never vague color names
- You enforce the banned word list absolutely
- You track spatial logic across shards
```

---

### Deliverable 3.3: script-supervisor.md (Agent Prompt)

```markdown
# Script Supervisor Agent

## Role
You are the Script Supervisor - the continuity guardian and state tracker. You are the QA/Scrum Master equivalent in the BMAD Cinematic Production Module.

## Responsibilities
1. **Own the Workflow-Status** - Track what has happened and what must persist
2. **Validate State Continuity** - Ensure characters have correct items, wounds, positions
3. **Manage Handshakes** - Define exit states and entry contracts between shards
4. **Enforce Narrative Contracts** - Flag violations of planted foreshadowing

## Before Every Shard Validation
You MUST read:
- [ ] Bible/Characters/{on_camera_characters}.md (current state)
- [ ] Production/Scenes/Scene_{XX-1}/exit_state.md (previous scene)
- [ ] Production/Scenes/Scene_{XX}/shards/shard_{YY-1}_exit.md (previous shard)
- [ ] Production/Contracts/*.md (check for violations)

## Your Output Format
When validating a shard prompt, provide:

### Shard {XX}.{Y} Continuity Validation

**State Check:**
| Character | Required State | In Prompt? | Status |
|-----------|---------------|------------|--------|
| {name} | Scar on left cheek | ✓/✗ | PASS/INJECT |
| {name} | Holding Silver Key | ✓/✗ | PASS/INJECT |
| {name} | Torn right shoulder | ✓/✗ | PASS/INJECT |

**Injections Required:**
- [ ] Add: "{exact text to inject into prompt}"

**Handshake Definition:**
**Exit State (Shard {XX}.{Y}):**
- Position: {where character ends}
- Facing: {direction}
- Expression: {emotional state}
- Action: {what they're doing as shard ends}

**Entry Contract (Shard {XX}.{Y+1}):**
- Must start with: {position, facing, expression}
- Must NOT show: {anything that would break continuity}

**Narrative Contract Check:**
- [ ] {Contract_ID}: {No violation / VIOLATION DETECTED}

**Protected Objects Check:**
- [ ] {Object}: {Not improperly revealed / VIOLATION}

**Lighting Gradient:**
- Current Position: {X-axis location}
- Expected #39FF14 Intensity: {low/medium/high}

**Status:** VALIDATED | VALIDATED WITH INJECTIONS | FAILED

## Rules
- You MUST check state before ANY prompt goes to Prompt Engineer
- You actively INJECT missing state, not just flag it
- You define explicit handshakes - no assumed continuity
- You protect Narrative Contracts absolutely
- You track lighting gradients as position-based state
```

---

### Deliverable 3.4: prompt-engineer.md (Agent Prompt)

```markdown
# Prompt Engineer Agent

## Role
You are the Prompt Engineer - the compiler that transforms requirements into executable AI prompts. You are the Developer equivalent in the BMAD Cinematic Production Module.

## Responsibilities
1. **Compile Final Prompts** - Synthesize Showrunner, Cinematographer, and Script Supervisor inputs
2. **Structure for AI Attention** - Place critical elements in first 25% of prompt
3. **Enforce Vocabulary** - Use only allowed words, never banned words
4. **Embed Handshakes** - Build exit states INTO the prompt structure

## Before Every Prompt Compilation
You MUST have received:
- [ ] Showrunner's beat notes (WHAT happens)
- [ ] Cinematographer's visual specs (HOW it looks)
- [ ] Script Supervisor's validation (STATE is correct)

## Your Output Format
Compile prompts using this EXACT structure:

```
[ID: SCENE_{XX}.{Y}_{BEAT_NAME}]

[Technical Header]:
{lens}mm {shot_type}, {fps}fps, {lighting_style}, {atmosphere_keywords}.

[Subject/Asset]:
{CRITICAL FEATURES FIRST - scar, distinguishing marks}
{Character description with current state}
{Outfit with current condition}

[Action/State]:
{What the character is DOING}
{How they are moving/positioned}
{What they are holding/wearing}

[Environment/Lighting]:
{Lighting description with HEX CODES}
{Background elements}
{Atmospheric conditions}

[Temporal Constraint]:
{Duration} seconds. {Movement/pacing description}. {EXIT STATE HOOK - how the shard ends}.
```

**Build Notes:**
- Anchor Points: {What's in first 25%}
- Vocabulary Compliance: {Banned words avoided: list}
- Exit Hook: {Exact handshake text}
- Injections Applied: {State injected from Script Supervisor}

## Rules
- NEVER compile without all three agent inputs
- ALWAYS place scars, wounds, critical features in first 25%
- NEVER use banned words - use required alternatives
- ALWAYS end with an exit state hook for handshake
- Use specific hex codes, never vague color names
- Include [Asset: ID] references for standardized elements
```

---

## PHASE 4: WORKFLOW RITUALS
### "The State-Diff Discipline"
**Duration:** Week 2-3
**Goal:** Define the mandatory workflows that prevent context loss

---

### Deliverable 4.1: Shard Generation Ritual

```markdown
# Shard Generation Ritual

## The Non-Negotiable Sequence

Every shard MUST follow this sequence. No exceptions.

### Step 1: Context Loading
```
Claude: "Read the following files for Scene {XX}, Shard {Y}:"
- .cpm/manifest.md (to know what to load)
- {All files listed in manifest}
```

### Step 2: Showrunner Review
```
Claude: "Acting as Showrunner, review Scene {XX}, Shard {Y}.
What is the atomic focus? What narrative contracts apply?"
```
Output: Showrunner Notes

### Step 3: Cinematographer Specs
```
Claude: "Acting as Cinematographer, specify the visual architecture
for this shard based on the Showrunner's notes."
```
Output: Visual Specs

### Step 4: Script Supervisor Validation
```
Claude: "Acting as Script Supervisor, validate the state for this shard.
What must be injected? Define the handshake."
```
Output: Validation + Injections + Handshake

### Step 5: Prompt Compilation
```
Claude: "Acting as Prompt Engineer, compile the final prompt
using all three inputs. Structure for maximum AI compliance."
```
Output: Final Prompt → Output/Prompts/Scene_{XX}_Shard_{Y}_prompt.md

### Step 6: State Update
```
Claude: "Update the exit_state.md for Shard {Y}."
```
Output: Production/Scenes/Scene_{XX}/state/shard_{Y}_exit_state.md

## CRITICAL: The State-Diff Check
Before Step 5, Script Supervisor MUST confirm:
- [ ] Previous shard exit state was read
- [ ] All character states are current
- [ ] All injections have been applied
- [ ] Handshake is defined

If ANY check fails → HALT and fix before compiling.
```

---

### Deliverable 4.2: Two-Shard Handshake Test Protocol

```markdown
# Validation Test: Two-Shard Handshake

## Purpose
Prove that CPM maintains continuity across shard boundaries.

## Setup
1. Create a minimal test project with:
   - One character (Hero) with distinctive feature (scar)
   - One item to be acquired (Key)
   - Basic Style Guide (one lighting rule)

## Test Procedure

### Shard A: Item Acquisition
1. Run full ritual for Shard A
2. Narrative: Hero picks up the Key
3. Generate prompt
4. Record exit_state: "Hero holding Key in right hand, looking frame-left"

### Shard B: Continuity Check
1. Run full ritual for Shard B
2. DO NOT remind the agent about the Key
3. Let Script Supervisor validate

## Success Criteria
- [ ] Shard B prompt contains Key in hero's hand
- [ ] Shard B prompt maintains hero's distinctive feature (scar)
- [ ] Shard B prompt honors lighting specs from Style Guide
- [ ] Shard B prompt starts with correct spatial position (frame-left)
- [ ] All above achieved WITHOUT human reminding the agent

## Failure Response
If any criterion fails:
1. Document which check failed
2. Identify where in the ritual the context was lost
3. Strengthen that agent's prompt or add explicit checks
4. Re-run test

## Pass Threshold
3 consecutive successful runs = CPM VALIDATED
```

---

## PHASE 5: INTEGRATION & TESTING
### "The First Real Scene"
**Duration:** Week 3-4
**Goal:** Build one complete scene using the full CPM workflow

---

### Deliverable 5.1: Test Scene Specification

**Scene 8: The Abandoned Cathedral**
(The scene designed during brainstorming Persona Journey)

**Setup:**
- Protagonist: Battle-scarred (left cheek), holding Silver Key, torn red cape (right shoulder)
- Location: Abandoned Cathedral, Cyberpunk-Noir aesthetic
- Narrative Contract: S12_ALTAR_SECRET - the Final Door is hidden behind the altar

**Beats:**
| Beat | Duration | Focus | Key Challenge |
|------|----------|-------|---------------|
| 8.1 | 5s | Entry & Burden | Character state (scar, torn shirt, Key) |
| 8.2 | 5s | Environment & Footsteps | Lighting gradient, spatial logic |
| 8.3 | 5s | Contractual Seed | Narrative Contract planting (altar glitch) |

**Visual Specs (From Brainstorming):**
- Lighting: Chiaroscuro-Neon, Volumetric, #FF00FF rim light, #39FF14 from pillars
- Lens Sequence: 85mm (8.1) → 24mm (8.2) → 35mm (8.3)
- Axis of Action: Enter frame-left, maintain left-third positioning

**Success Criteria:**
- [ ] All 3 beats generated without context loss
- [ ] Handshakes maintained between all beats
- [ ] Style Guide enforced (no banned words)
- [ ] Character state persisted (scar, outfit, Key)
- [ ] Narrative Contract logged for Scene 12
- [ ] Altar marked as Protected Object

---

### Deliverable 5.2: V1.0 Complete Checklist

```markdown
# CPM V1.0 Release Checklist

## Directory Structure
- [ ] .cpm/config.yaml - complete and valid
- [ ] .cpm/manifest.md - template ready
- [ ] .cpm/agents/ - all 4 agents defined

## Bible Templates
- [ ] Show_Bible.md - template with all sections
- [ ] Character State template - all fields defined
- [ ] World element template - basic structure

## Architecture Templates
- [ ] Style_Guide.md - complete with all categories
- [ ] Vocabulary.md - banned/required words
- [ ] Palette.md - color definitions

## Agent Prompts
- [ ] showrunner.md - complete with output format
- [ ] cinematographer.md - complete with output format
- [ ] script-supervisor.md - complete with output format
- [ ] prompt-engineer.md - complete with output format

## Workflow
- [ ] Shard Generation Ritual - documented
- [ ] State-Diff Check - mandatory sequence
- [ ] Handshake format - standardized

## Validation
- [ ] Two-Shard Handshake Test - PASSED (3 consecutive runs)
- [ ] Test Scene (8.1-8.3) - complete without failures

## Documentation
- [ ] README.md - quick start guide
- [ ] WORKFLOW.md - full ritual documentation
- [ ] TROUBLESHOOTING.md - common failures and fixes
```

---

## V1.0 DELIVERABLES SUMMARY

| # | Deliverable | Type | Priority | Status |
|---|-------------|------|----------|--------|
| 1.1 | Master Directory Structure | Folder Template | CRITICAL | [ ] |
| 1.2 | config.yaml Schema | Configuration | CRITICAL | [ ] |
| 1.3 | manifest.md Schema | Context Index | CRITICAL | [ ] |
| 2.1 | Show_Bible.md Template | Bible | CRITICAL | [ ] |
| 2.2 | Character State Template | Bible | CRITICAL | [ ] |
| 2.3 | Style_Guide.md Template | Architecture | CRITICAL | [ ] |
| 3.1 | showrunner.md | Agent Prompt | CRITICAL | [ ] |
| 3.2 | cinematographer.md | Agent Prompt | CRITICAL | [ ] |
| 3.3 | script-supervisor.md | Agent Prompt | CRITICAL | [ ] |
| 3.4 | prompt-engineer.md | Agent Prompt | CRITICAL | [ ] |
| 4.1 | Shard Generation Ritual | Workflow | CRITICAL | [ ] |
| 4.2 | Two-Shard Handshake Test | Validation | CRITICAL | [ ] |
| 5.1 | Test Scene Specification | Integration | HIGH | [ ] |
| 5.2 | V1.0 Complete Checklist | Quality Gate | HIGH | [ ] |

---

## SUCCESS METRICS

**V1.0 is COMPLETE when:**
1. A user can create a new CPM project from the template
2. The Four-Agent Ritual produces consistent prompts
3. The Two-Shard Handshake Test passes 3 consecutive times
4. A complete 3-beat scene can be generated without context loss
5. Style Guide violations are caught before prompts compile

---

## V2.0 ROADMAP (Future Features)

| Feature | Description | Dependency |
|---------|-------------|------------|
| VLM-QA Agent | Visual regression testing with GPT-4o/Gemini | V1.0 validated |
| Cinematic Transpiler | Universal Cinematic Language + Model Adapters | Prompt format stable |
| Exception-Based Review | Confidence scoring, auto-commit for 95%+ | VLM-QA working |
| Agentic Inception | Interview-based onboarding (no Markdown writing) | Core templates done |
| Git Collaboration | Branching narratives, merge conflict resolution | Multi-user need |
| Thematic Skinning | Style Guide as swappable theme | Style Guide proven |
| Variable Intervals | 5s/15s/30s shards with choreographed scripts | Atomic beats working |
| Low-Fi Animatic | Tier 3 staging with motion preview | Keyframe validation working |

---

## CORE CONCEPTS REFERENCE

### The SDLC → CPLC Mapping

| BMAD (Software) | CPM (Cinematics) | Deliverable |
|-----------------|------------------|-------------|
| Product Brief | Story Brief | Hook, genre, summary |
| PRD | Show Bible | Characters, world rules, themes |
| Architecture | Style Guide | Lighting, color, camera language |
| Epics/Stories | Beat Sheets / Scenework | Acts and Scenes |
| Sprint Planning | Production Slate | Scene status tracking |
| Dev Story | Scene Prompting | 5-second atomic beats |
| Code Review | Continuity Check | CAC validation |

### The Agentic Film Crew

| Agent | Role | Owns | Equivalent |
|-------|------|------|------------|
| Showrunner | Story Guardian | Show Bible | PM |
| Cinematographer | Visual Architect | Style Guide | Architect |
| Script Supervisor | Continuity Tracker | State Files | QA/Scrum |
| Prompt Engineer | Compiler | Final Prompts | Developer |

### Key Innovations

1. **Continuity Acceptance Criteria (CAC)** - Unit testing for cinema
2. **Three-Tiered Staging** - Dev (text) → UAT (keyframe) → Staging (animatic)
3. **Temporal Sharding** - 5-second atomic beats with handshakes
4. **Narrative Contracts** - Forward-looking validation (foreshadowing)
5. **External State Machine** - AI is stateless; CPM is the memory

---

## PHILOSOPHY

> "Cinematics as Code - 50 years of Software Engineering solving 100 years of Cinematic Production problems."

> "Context as Currency - treating context with BMAD rigor unlocks Hollywood-scale storytelling with a fraction of the resources."

> "Automating the Boredom - Agents handle rigid discipline; humans provide soul."

> "Studio-in-a-Box - Democratization of the blockbuster; crew of 200 → crew of 1."

---

*Generated from CPM Brainstorming Session - 2026-02-01*
*82 ideas across 4 techniques: Analogical Thinking, Persona Journey, Six Thinking Hats, What If Scenarios*

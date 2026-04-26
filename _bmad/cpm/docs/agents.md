# Agents Reference

CPM includes 4 specialized agents that form your Film Crew:

---

## Showrunner

**Icon:** 🎬
**Role:** Story Guardian & Creative Visionary
**Equivalent:** Product Manager (PM)

### What They Own
- `Bible/Show_Bible.md` — The story, themes, and world rules
- `Production/Contracts/*.md` — Narrative contracts (foreshadowing)

### What They Do
- Define WHAT happens in each shard
- Break scenes into atomic 5-second beats
- Ensure every scene serves the larger narrative
- Track narrative contracts (foreshadowing obligations)
- Validate character actions against their arc

### When They're Invoked
- Step 2 of Shard Generation Ritual
- Scene review and beat breakdown
- Narrative contract management

### Key Rules
- Defines WHAT happens, not HOW it looks
- Never approves a beat that contradicts the Show Bible
- Flags any scene that could violate a Narrative Contract

### Output Format
```
### Scene {XX} Showrunner Notes

**Thematic Alignment:** [How this scene serves the story]

**Character Arc Check:**
- {Character}: [Current arc position, emotional truth needed]

**Atomic Beat Breakdown:**
| Beat | Duration | Focus | Primary Requirement |
|------|----------|-------|---------------------|

**Narrative Contract Status:**
- [ ] {Contract_ID}: {Status - PLANT / MAINTAIN / PAYOFF}

**Notes to Cinematographer:** {Visual emphasis needed}
**Notes to Script Supervisor:** {State changes to track}
```

---

## Cinematographer

**Icon:** 📷
**Role:** Visual Architect & Style Guardian
**Equivalent:** System Architect

### What They Own
- `Architecture/Style_Guide.md` — Visual language and rules
- `Architecture/Palette.md` — Color definitions with hex codes
- `Architecture/Vocabulary.md` — Banned/required prompt words

### What They Do
- Define HOW things look in each shard
- Specify lighting, lens, color, composition
- Enforce visual continuity across shards
- Maintain the prompt vocabulary (banned/required words)
- Track spatial logic and axis of action

### When They're Invoked
- Step 3 of Shard Generation Ritual
- Visual spec definition
- Style Guide enforcement

### Key Rules
- Defines HOW it looks, not WHAT happens
- Never approves a beat that violates the Style Guide
- Specifies exact hex codes, never vague color names
- Enforces the banned word list absolutely

### Output Format
```
### Beat {XX}.{Y} Cinematographer Specs

**Lighting Protocol:**
- Primary: {light type, hex code, placement}
- Secondary: {light type, hex code, placement}
- Rim: {MANDATORY - describe}

**Lens Selection:**
- Lens: {focal length}mm
- Motivation: {why this lens for this emotion}

**Color Application:**
- {Hex code 1}: {where it appears}
- {Hex code 2}: {where it appears}

**Composition:**
- Subject Position: {frame location}
- Negative Space: {percentage, meaning}

**Vocabulary Enforcement:**
- [ ] No banned words in prompt
- Required terms included: {list}
```

---

## Script Supervisor

**Icon:** 📋
**Role:** Continuity Guardian & State Tracker
**Equivalent:** QA / Scrum Master

### What They Own
- `Bible/Characters/*.md` — Character state files
- `Production/Scenes/*/state/*.md` — Entry/exit states
- State tracking across all shards

### What They Do
- Validate continuity before prompt compilation
- Track character state (items, wounds, positions)
- Define handshakes between shards
- Inject missing state into prompts
- Enforce narrative contracts

### When They're Invoked
- Step 4 of Shard Generation Ritual (Validation)
- Step 6 of Shard Generation Ritual (State Update)
- Continuity checks

### Key Rules
- Must check state before ANY prompt goes to Prompt Engineer
- Actively INJECTS missing state, not just flags it
- Defines explicit handshakes — no assumed continuity
- Protects Narrative Contracts absolutely

### Output Format
```
### Shard {XX}.{Y} Continuity Validation

**State Check:**
| Character | Required State | In Prompt? | Status |
|-----------|---------------|------------|--------|
| {name} | Scar on left cheek | ✓/✗ | PASS/INJECT |

**Injections Required:**
- [ ] Add: "{exact text to inject}"

**Handshake Definition:**
**Exit State (Shard {XX}.{Y}):**
- Position: {where character ends}
- Facing: {direction}
- Expression: {emotional state}

**Entry Contract (Shard {XX}.{Y+1}):**
- Must start with: {position, facing, expression}

**Status:** VALIDATED | VALIDATED WITH INJECTIONS | FAILED
```

---

## Prompt Engineer

**Icon:** ⚙️
**Role:** Prompt Compiler & AI Whisperer
**Equivalent:** Developer

### What They Own
- `Output/Prompts/*.md` — Final compiled prompts
- Prompt structure and optimization

### What They Do
- Compile final prompts from all agent inputs
- Structure prompts for AI attention (critical features in first 25%)
- Enforce vocabulary (banned/required words)
- Embed exit state hooks for handshakes

### When They're Invoked
- Step 5 of Shard Generation Ritual
- Prompt optimization

### Key Rules
- NEVER compiles without all three agent inputs
- ALWAYS places scars, wounds, critical features in first 25%
- NEVER uses banned words — uses required alternatives
- ALWAYS ends with an exit state hook for handshake

### Output Format
```
[ID: SCENE_{XX}.{Y}_{BEAT_NAME}]

[Technical Header]:
{lens}mm {shot_type}, {fps}fps, {lighting_style}.

[Subject/Asset]:
{CRITICAL FEATURES FIRST - scar, marks}
{Character description with current state}
{Outfit with current condition}

[Action/State]:
{What the character is DOING}
{What they are holding/wearing}

[Environment/Lighting]:
{Lighting with HEX CODES}
{Background elements}

[Temporal Constraint]:
{Duration} seconds. {EXIT STATE HOOK}.
```

---

## Agent Collaboration Flow

```
Showrunner (WHAT)
     ↓
Cinematographer (HOW)
     ↓
Script Supervisor (STATE) ←→ State Files
     ↓
Prompt Engineer (COMPILE)
     ↓
Final Prompt → AI Video Generator
```

Each agent builds on the previous agent's work. No agent can be skipped.

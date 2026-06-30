---
capability: shard-state-validation
description: The State-Diff Gate — validates continuity for a shard, actively injects missing state, writes the full exit-state handshake, and returns a binding pass/fail Status that gates the pipeline.
---

# Shard State Validation

## What Success Looks Like

The State-Diff Gate passes only when every required character detail is present in the draft (or has been actively injected), the full exit-state handshake is written, no narrative contract or protected object is violated, and position-based lighting is continuous with the previous shard. Zero continuity errors reach the Prompt Engineer. The output is a single artifact — the **Continuity Validation** — ending in a binding **Status**.

## Read First — Every Time

This agent is stateless. You cannot enforce continuity against state you have not loaded. Before validating, read fresh from the production project:

- [ ] `Bible/Characters/{on_camera_characters}.md` — current state of every character on camera: immutable features, mutable state, inventory, arc position
- [ ] the previous shard's exit state — `Production/Scenes/Scene_{XX}/state/shard_{Y-1}_exit_state.md` — including its **Entry Contract** for this shard, its per-character Holding / Physical Condition, and its Environment/Lighting state (this is the baseline every continuity check compares against)
- [ ] the previous scene's final exit state — `Production/Scenes/Scene_{XX-1}/state/` (the last shard's `exit_state.md`) — when this is the scene's first shard
- [ ] `Production/Contracts/*.md` — every active narrative contract, AND any protected-object entry (what must not be revealed yet)
- [ ] `Architecture/Style_Guide.md` — the position→lighting-intensity gradient rule, so an "expected intensity" can be judged (you verify against it; you do not author it)
- [ ] `.cpm/config.yaml` — `validation.require_state_diff_check` (this gate) and `temporal.default_shard_duration` (the shard's end moment, where the Exit State is measured)

Do not validate from memory or from the draft alone. The character files and exit states are the authority.

## Inputs

- The current draft inputs to validate: the **Showrunner Notes** (WHAT happens) and the **Cinematographer Specs** (HOW it looks)
- The current shard number `{XX}.{Y}`
- The authority files read above

## Output Format — Continuity Validation

Produce exactly this structure:

### Shard {XX}.{Y} Continuity Validation

**State Check:**

| Character | Required State | In Prompt? | Status |
|-----------|---------------|------------|--------|
| {Name} | {immutable feature — e.g. scar on LEFT cheek} | ✓ / ✗ | PASS / INJECT / FAIL |
| {Name} | {inventory — e.g. holding the silver key} | ✓ / ✗ | PASS / INJECT / FAIL |
| {Name} | {mutable state — e.g. torn RIGHT shoulder} | ✓ / ✗ | PASS / INJECT / FAIL |

(PASS = present and correct. INJECT = missing-but-known, injected below. FAIL = the draft contradicts an immutable feature and cannot be injected to match canon — a blocking item.)

**Injections Required:** (the exact text to add to the draft — you inject, you do not merely flag)

- [ ] Add: "{exact prompt text to inject}"

(If none required: "None — all required state already present in the draft.")

**Handshake Definition — Exit State (Shard {XX}.{Y}):**

This block **is** the `shard_{Y}_exit_state.md` you write at the shard's end. It must carry the full state the next shard, its Entry Contract, and the Prompt Engineer all depend on — not a position alone.

*Per on-camera character:*
- **Position:** {where they end — X-axis / frame location}
- **Facing:** {direction}
- **Expression:** {emotional state}
- **Action:** {what they are doing as the shard ends}
- **Holding:** {inventory — every item carried, with hand and on/off-screen}
- **Physical Condition:** {mutable state — wounds, wardrobe condition, named condition flags — plus arc progress %}

*Environment State:*
- **Lighting:** {source + position + the {signature_hex} value + intensity (low/medium/high)} — the baseline the next shard's lighting check reads
- **Time Progression:** {time of day / any change this shard}
- **Active Environmental Elements:** {set, soundscape, framing notes that must persist}

*State Changes This Shard:*

| Element | Previous Value | New Value | Reason |
|---------|---------------|-----------|--------|
| {element} | {prev} | {new} | {what caused it} |

*Active Contracts:*

| Contract ID | Status | Notes |
|-------------|--------|-------|
| {Contract_ID or "(none)"} | PLANT / MAINTAIN / PAYOFF / AT-RISK | {one line} |

**Entry Contract (for Shard {XX}.{Y+1}):**
- **MUST start with:** {position, facing, expression, lighting the next shard must open on}
- **MUST NOT show:** {anything that would break continuity — blinks, banned light sources, not-yet-revealed objects}

**Narrative Contract Check:**

- [ ] {Contract_ID}: No violation / VIOLATION DETECTED — {what breaks}

**Protected Objects Check:**

- [ ] {Object}: Not improperly revealed / VIOLATION — {what leaks}

**Lighting Gradient:** (position-based state — the value is set by the Cinematographer Specs / Style Guide; you verify continuity, you do not set it)

- Current Position: {X-axis location}
- Expected {signature_hex} Intensity (per the Style Guide gradient rule): low / medium / high
- Continuous with the previous shard's recorded exit-state intensity? ✓ / ✗

**Status:** VALIDATED | VALIDATED WITH INJECTIONS | FAILED

- **VALIDATED** — every required detail present, the full exit state written, the handshake defined, no violation. Hand off to the Prompt Engineer.
- **VALIDATED WITH INJECTIONS** — required state was missing and has been actively injected (exact text above); the exit state and handshake are defined and no violation remains. Hand off with the injections applied.
- **FAILED** — at least one of: a state contradiction that cannot be injected to match canon, a narrative-contract VIOLATION, a protected-object VIOLATION, a broken inherited Entry Contract, or a lighting-gradient discontinuity against the previous exit state. **A FAILED status HALTS `cpm-shard-generation` at the State-Diff Gate. No prompt compiles and nothing reaches the Prompt Engineer until every blocking item below is resolved.**

**If FAILED — Blocking Items:** (enumerate every blocker and the exact change required — nothing proceeds while this list is non-empty)

- {item}: {what is wrong} → {what must change before this shard can pass}

> **Duration:** the shard's end moment — where the Exit State is measured — is the shard's duration from the scene brief / `temporal.default_shard_duration` in `.cpm/config.yaml` (default 5s; a production may run longer, up to `temporal.max_shard_duration`, 30s). Do not assume 5s.

## The Rules

- **Check state before any prompt compiles.** This gate runs before the Prompt Engineer, every shard, without exception. `validation.require_state_diff_check` does not make the gate optional — it *is* the gate.
- **Actively inject missing state — never merely flag it.** A missing-but-known detail is written into the draft as exact text and the Status becomes VALIDATED WITH INJECTIONS. A flag with no injection is not a pass.
- **Write the full exit state — not a position alone.** The Exit State you record (Holding, Physical Condition, Environment/Lighting, State Changes, Active Contracts) is the only baseline the next shard has. An exit state that omits lighting or inventory leaves the next shard's continuity checks with nothing to compare against — that is itself a failure to validate.
- **Every violation is a hard FAIL at the same hardness.** A narrative-contract violation, a protected-object reveal, a broken handshake, and a lighting discontinuity each force Status: FAILED and halt the pipeline. None of them is softened to a note that travels downstream with the prompt.
- Injection covers the character state you own — immutable features, mutable state, inventory, position. A conflict in the story or the visuals is not yours to inject away: FAIL it and return it to the Showrunner or the Cinematographer.
- Immutable features (LEFT/RIGHT-specific scars, marks, permanent traits) are required state, never variable. If the draft contradicts an immutable feature and it cannot be injected to match canon, that is a FAIL, not an injection.
- Define explicit handshakes — no assumed continuity. Every shard ends with a full Exit State and hands the next shard an Entry Contract; an undefined handshake is itself a failure to validate.

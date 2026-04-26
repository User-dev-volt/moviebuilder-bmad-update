# Examples & Use Cases

This section provides practical examples for using CPM.

---

## Example: The Cathedral Scene

This example walks through generating a 3-beat scene from the CPM roadmap.

### Setup

**Scene 8: The Abandoned Cathedral**

**Character:** Protagonist
- Battle scar on LEFT cheek
- Holding Silver Key in right hand
- Torn red cape (right shoulder)

**Location:** Abandoned Cathedral, Cyberpunk-Noir

**Narrative Contract:** S12_ALTAR_SECRET — the Final Door is hidden behind the altar

### Beat Breakdown

| Beat | Duration | Focus | Challenge |
|------|----------|-------|-----------|
| 8.1 | 5s | Entry & Burden | Character state (scar, cape, Key) |
| 8.2 | 5s | Environment | Lighting gradient, spatial logic |
| 8.3 | 5s | Contractual Seed | Narrative Contract planting |

### Beat 8.1: Showrunner Notes

```markdown
**Thematic Alignment:** Isolation and burden — the protagonist carries
the weight of their journey into a space of former sanctuary.

**Character Arc Check:**
- Protagonist: 60% through transformation. Desperate but determined.
  Emotional truth: exhaustion meeting resolve.

**Atomic Beat Breakdown:**
| Beat | Duration | Focus | Primary Requirement |
|------|----------|-------|---------------------|
| 8.1 | 5s | Entry & Burden | Establish character state visually |

**Narrative Contract Status:**
- [ ] S12_ALTAR_SECRET: PLANT phase — do NOT reveal altar yet

**Notes to Cinematographer:** Close lens to emphasize isolation and burden
**Notes to Script Supervisor:** Track Key, scar, cape damage
```

### Beat 8.1: Cinematographer Specs

```markdown
**Lighting Protocol:**
- Primary: #FF00FF rim light from above-right, defining silhouette
- Secondary: #39FF14 ambient from distant pillars, toxic glow
- Rim: MANDATORY — electric purple edge on cape and profile

**Lens Selection:**
- Lens: 85mm
- Motivation: Oppressive, isolated — character small against burden

**Color Application:**
- #FF00FF: Rim on character, Key reflection
- #39FF14: Pillar glow, environment only
- #0A0A0A: Deep shadows, 70% of frame

**Composition:**
- Subject Position: Left-third, facing right
- Negative Space: 60% right side — emphasizes isolation

**Vocabulary Enforcement:**
- [ ] No banned words (bright, sunny, cheerful, beautiful)
- Required: "high-contrast", "volumetric", "deep shadows"
```

### Beat 8.1: Script Supervisor Validation

```markdown
**State Check:**
| Character | Required State | In Prompt? | Status |
|-----------|---------------|------------|--------|
| Protagonist | Scar on LEFT cheek | ✗ | INJECT |
| Protagonist | Silver Key in RIGHT hand | ✗ | INJECT |
| Protagonist | Red cape torn RIGHT shoulder | ✗ | INJECT |
| Protagonist | Exhausted expression | ✗ | INJECT |

**Injections Required:**
- [ ] Add: "jagged scar on LEFT cheek"
- [ ] Add: "Silver Key gripped in RIGHT hand, reflecting #FF00FF"
- [ ] Add: "tattered red cape, torn at RIGHT shoulder"
- [ ] Add: "exhausted, weathered expression"

**Exit State (Shard 8.1):**
- Position: Frame-left, facing right
- Facing: Into cathedral (right)
- Expression: Exhausted determination
- Action: Standing at threshold

**Entry Contract (Shard 8.2):**
- Must start with: Character frame-left, facing right
- Must NOT show: Altar (protected by Narrative Contract)

**Status:** VALIDATED WITH INJECTIONS
```

### Beat 8.1: Final Prompt

```
[ID: SCENE_08.1_ENTRY_BURDEN]

[Technical Header]:
85mm close-up, 24fps, chiaroscuro-neon, volumetric atmosphere, film grain.

[Subject/Asset]:
Jagged scar on LEFT cheek — weathered, permanent.
Male protagonist, late 30s, exhausted determination in eyes.
Tattered red cape, torn at RIGHT shoulder, fabric catching light.
Silver Key gripped in RIGHT hand, surface reflecting #FF00FF rim light.

[Action/State]:
Standing at cathedral threshold, weight of journey visible in posture.
Shoulders slightly hunched, breathing heavy.
Key held close to chest, protective grip.

[Environment/Lighting]:
#FF00FF neon rim light from above-right, defining silhouette edge.
#39FF14 toxic glow from distant pillars, environmental only.
Deep shadows (#0A0A0A) consuming 70% of frame.
Volumetric dust particles catching purple light.
Gothic architecture barely visible in darkness.

[Temporal Constraint]:
5 seconds. Slow, deliberate breath. Ends with: character frame-left,
facing right into cathedral, exhausted determination, Key in right hand.
```

---

## Common Scenarios

### Scenario: Character Acquires Item

1. **Pre-acquisition shard:** Character sees/approaches item
2. **Acquisition shard:** Character picks up item
3. **Post-acquisition:** Script Supervisor adds to inventory

**State file update:**
```markdown
## Inventory (Mutable)
| Item | Status | Acquired | Notes |
|------|--------|----------|-------|
| Silver Key | EQUIPPED_PRIMARY_HAND | Scene 7 | Reflects #FF00FF |
```

### Scenario: Character Gets Injured

1. **Injury shard:** Injury occurs on-screen
2. **Script Supervisor:** Adds to Physical State
3. **All future shards:** Injury must be visible

**State file update:**
```markdown
## Physical State (Mutable)
| Condition | Location | Severity | Since |
|-----------|----------|----------|-------|
| Fresh cut | Right forearm | Active/bleeding | Scene 8 |
```

### Scenario: Crossing Scene Boundary

1. **Scene N exit_state:** Capture full character state
2. **Scene N+1 entry_state:** Read previous exit
3. **Script Supervisor:** Validates continuity across scenes

---

## Tips & Tricks

### For Better Continuity

1. **Be specific about LEFT/RIGHT** — "Scar on cheek" will drift. "Scar on LEFT cheek" persists.

2. **Put critical features first** — AI attention fades. Scars, items, injuries go in first 25%.

3. **Use hex codes, not color names** — "Purple" varies. "#FF00FF" is exact.

4. **Define exit states explicitly** — "Character walks away" drifts. "Character frame-right, back to camera, walking toward door" persists.

### For Style Consistency

1. **Create a banned word list early** — Common drift words: "bright", "beautiful", "cinematic"

2. **Define your rim light rule** — Rim light is the most effective continuity anchor

3. **Pick 3-4 colors max** — Limited palette = consistent look

### For Workflow Efficiency

1. **Run Handshake Test before real production** — Validates your entire setup

2. **Trust the Script Supervisor** — If it says INJECT, inject. Don't skip.

3. **Update state files immediately** — Don't batch updates. Do it per-shard.

---

## Troubleshooting

### Problem: Character features drifting

**Symptom:** Scar moves from left to right cheek, or disappears.

**Cause:** Feature not in first 25% of prompt, or not specific enough.

**Fix:**
1. Always specify LEFT/RIGHT explicitly
2. Put distinguishing features immediately after Technical Header
3. Add to Script Supervisor's required injection list

### Problem: Items disappearing

**Symptom:** Character no longer holding item they should have.

**Cause:** Script Supervisor didn't inject, or exit state wasn't read.

**Fix:**
1. Check exit_state.md from previous shard
2. Verify item is in character's Inventory with correct status
3. Ensure Script Supervisor validation ran before compilation

### Problem: Lighting inconsistent

**Symptom:** Colors shifting between shards.

**Cause:** Vague color descriptions or missing hex codes.

**Fix:**
1. Always use hex codes: "#FF00FF" not "purple"
2. Check Style Guide for allowed colors
3. Verify Cinematographer specs include all light sources

### Problem: Spatial continuity breaking

**Symptom:** Character jumps from frame-left to frame-right.

**Cause:** Exit state didn't capture position, or wasn't read.

**Fix:**
1. Always include frame position in exit state
2. Always include facing direction
3. Script Supervisor should catch this — check validation ran

### Problem: Handshake Test failing

**Symptom:** Test fails on Key or scar persistence.

**Cause:** Weak agent prompts or missing file reads.

**Fix:**
1. Identify which check failed
2. Strengthen that agent's "Before Every" checklist
3. Add explicit validation rules
4. Re-run test (need 3 consecutive passes)

---

## Getting More Help

- Review the main BMAD documentation
- Check module configuration in `.cpm/config.yaml`
- Verify all required files exist before running shard-generation
- Run `/cpm-handshake-test` to validate your setup

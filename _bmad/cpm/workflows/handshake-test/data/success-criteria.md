# Handshake Test — Success Criteria

## What to Validate

Check Shard B's compiled prompt (Output/Prompts/Scene_01_Shard_02_prompt.md) against these criteria. ALL must pass WITHOUT human intervention during the shard-generation ritual.

---

## Criteria

### 1. Key Present
- **Check:** Shard B prompt mentions the Silver Key in the hero's hand
- **Why:** The Key was acquired in Shard A and recorded in the exit state. The Script Supervisor must inject it.
- **Search for:** "Silver Key", "key", references to held items
- **FAIL if:** Key is absent from Shard B prompt

### 2. Scar Correct
- **Check:** Shard B prompt includes the jagged scar on the hero's LEFT cheek
- **Why:** Immutable distinguishing feature defined in Bible/Characters/hero.md
- **Search for:** "scar", "LEFT cheek", "left cheek"
- **FAIL if:** Scar is missing OR on wrong cheek

### 3. Lighting OK
- **Check:** Shard B prompt specifies #FF00FF rim light
- **Why:** Style Guide mandates rim light on all subjects with this color
- **Search for:** "#FF00FF", "rim light", "magenta"
- **FAIL if:** Rim light color is missing or wrong

### 4. Position OK
- **Check:** Shard B prompt starts hero in the correct spatial position (frame-left)
- **Why:** Shard A exit state specified "looking frame-left" — the handshake must preserve spatial continuity
- **Search for:** "frame-left", "left third", screen direction references
- **FAIL if:** Hero position doesn't match Shard A exit state

### 5. No Human Hints
- **Check:** All above were achieved without the test coordinator providing hints during Shard B
- **Why:** The entire point — the External State Machine must carry continuity, not the human
- **FAIL if:** Any hint was given about key, scar, position, or lighting during Shard B setup

---

## Results Table Format

| Run | Key Present | Scar Correct | Lighting OK | Position OK | No Hints | Result |
|-----|-------------|--------------|-------------|-------------|----------|--------|
| 1   | PASS/FAIL   | PASS/FAIL    | PASS/FAIL   | PASS/FAIL   | PASS/FAIL | PASS/FAIL |

**Pass Threshold:** 3 consecutive PASS results = CPM VALIDATED

---

## Failure Response

If any criterion fails:

1. **Document which check failed** — Was it the Key? The scar? The position? The lighting?
2. **Identify where in the ritual context was lost:**
   - Was the character file not read?
   - Was the exit state not loaded?
   - Was the injection not applied by Script Supervisor?
   - Was the style guide not enforced by Cinematographer?
3. **Strengthen that agent's prompt or add explicit checks**
4. **Re-run test from scratch** — do not carry over fixes mid-test

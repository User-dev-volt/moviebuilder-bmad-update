---
reportType: 'handshake'
sceneNumber: '{XX}'
shardA: {N}
shardB: {N+1}
boundary: 'SCENE_{XX}.{N} -> SCENE_{XX}.{N+1}'
generatedDate: '{date}'
verdict: '{PASS | FAIL}'
---

# Handshake Report — Scene {XX}, Shard {N} → Shard {N+1}

_A single continuity boundary under test: shard A (Shard {N}) hands shard B (Shard {N+1}) its
opening through the exit state's entry contract. This report grades shard B against that contract on
the five continuity criteria and the MUST-NOT-Show floor. It reads two generated artifacts and
changes neither — the report is its only output._

## Boundary Under Test

- **Scene:** {XX}
- **Shard A (exit state):** Shard {N} — `Production/Scenes/Scene_{XX}/state/shard_{N}_exit_state.md`
- **Shard B (compiled prompt):** Shard {N+1} — `Output/Prompts/Scene_{XX}_Shard_{N+1}_prompt.md`
- **Structural floor (`validate_handshake.py`):** _pass / hold / no_boundary, plus any token the floor reported missing, forbidden, or absent._

## Inherited Entry Contract (from Shard {N} exit state)

- **MUST Start With:** _every bullet from shard A's entry contract — carried objects and the hand, distinctive features and the side, signature lighting, opening framing._
- **MUST NOT Show:** _every bullet shard A forbids._

## Continuity Criteria

_Each criterion is graded at the same hardness. The boundary PASSES only when every row reads PASS
and the floor holds — a single FAIL forces the overall verdict to FAIL._

| # | Criterion | Result | Evidence in Shard B |
|---|-----------|--------|---------------------|
| 1 | Carried-object / inventory — every held object present in the SAME hand | _PASS / FAIL_ | _the object and hand as shard B carries them_ |
| 2 | Distinctive-feature / identity — every LEFT/RIGHT-specific feature on the same side | _PASS / FAIL_ | _the feature as shard B names it_ |
| 3 | Style / lighting — signature hex and placement honoured, Style Guide upheld | _PASS / FAIL_ | _shard B's [Environment/Lighting] line_ |
| 4 | Spatial-position — shard B opens on the mandated framing, placement, and facing | _PASS / FAIL_ | _shard B's opening framing_ |
| 5 | Autonomy — every continuous element traces to shard A's contract, no human reminder | _PASS / FAIL_ | _each element mapped to the contract line it came from_ |
| Floor | MUST NOT Show — nothing shard A forbids appears in shard B | _PASS / FAIL_ | _absent, or the forbidden element found_ |

## Blocking Continuity Breaks

_Every FAIL from the table above, one per line — the criterion, what broke in shard B, and the exact
fix. **This list is empty if and only if the verdict is PASS;** a single entry forces FAIL.
Continuity is not negotiable here, so nothing is waved through with a note attached._

- _{criterion}: {what broke in shard B} → {what must change to honour Shard {N}'s contract}_

## Verdict

**{PASS | FAIL}**

- **PASS** — every one of the five criteria reads PASS and the MUST-NOT-Show floor holds; the
  Blocking Continuity Breaks list above is empty. Continuity survived the boundary on the contract
  alone, with no human reminder.
- **FAIL** — any criterion FAILED, or any forbidden element appeared in shard B. The Blocking
  Continuity Breaks list above is non-empty and names each one. Shard {N+1} is not continuity-safe
  against Shard {N}; regenerate it through shard-generation before production proceeds.

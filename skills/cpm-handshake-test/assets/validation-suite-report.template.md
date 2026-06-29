---
reportType: 'validation-suite'
sceneNumber: '{XX}'
boundariesTested: {testable-boundary-count}
consecutivePassesRequired: 3
longestPassStreak: {longest-consecutive-pass-count}
generatedDate: '{date}'
verdict: '{VALIDATED | NOT VALIDATED}'
---

# Validation Suite Report — Scene {XX}

_The full continuity validation for a scene: the handshake test chained across every adjacent
boundary, governed by the three-consecutive-pass law. Three consecutive boundaries PASS and CPM is
VALIDATED; any FAIL breaks the streak and the verdict is NOT VALIDATED. This reads the scene's
generated shards and writes this report; it changes no production artifact._

## Boundaries Under Test

_A scene of shard_count S offers S-1 testable boundaries — one per adjacent pair; the final shard
owes no contract. They run in order from Shard 1._

- **Scene:** {XX}
- **Shard count (S):** {shard-count}
- **Testable boundaries (S-1):** {testable-boundary-count}

## Per-Pass Results

_One row per boundary, in order. Each result is the single-boundary verdict — see that boundary's
own handshake report for the full per-criterion grade. A PASS extends the consecutive streak; a FAIL
breaks it and restarts the count at zero._

| Pass | Boundary | Result | Consecutive-PASS streak | Breaks (if FAIL) |
|------|----------|--------|-------------------------|------------------|
| 1 | Shard 1 → Shard 2 | _PASS / FAIL_ | _running count_ | _the failing criteria, or —_ |
| 2 | Shard 2 → Shard 3 | _PASS / FAIL_ | _running count_ | _the failing criteria, or —_ |
| 3 | Shard 3 → Shard 4 | _PASS / FAIL_ | _running count_ | _the failing criteria, or —_ |

## Blocking Failures

_Every boundary that FAILED, with the criteria it broke. **This list is empty if and only if the
verdict is VALIDATED** — a single failed boundary forces NOT VALIDATED. (See each boundary's
handshake report for the full per-criterion grade and the fix.)_

- _Shard {N} → Shard {N+1}: {the failing criteria and the fix each needs}_

## Evidence Sufficiency

_VALIDATED requires three CONSECUTIVE PASS boundaries. A scene that cannot field three — fewer than
three testable boundaries exist, or a no-boundary ended the chain early — cannot be declared
VALIDATED no matter how clean its passes. This is insufficient evidence, not a continuity FAIL._

- **Testable boundaries available:** {testable-boundary-count}
- **Longest consecutive-PASS streak:** {longest-consecutive-pass-count}
- **Three-consecutive-pass bar met:** _yes / no — if no, name the gap (how many more shards continuity needs in this scene to prove out)._

## Verdict

**{VALIDATED | NOT VALIDATED}**

- **VALIDATED** — three consecutive boundaries PASSED, the Blocking Failures list above is empty, and
  the scene fielded enough boundaries to clear the three-consecutive-pass bar. CPM held continuity
  across the seam, on the contract alone, three times running.
- **NOT VALIDATED** — a boundary FAILED (the Blocking Failures list is non-empty), or the scene could
  not field three consecutive testable boundaries (see Evidence Sufficiency). Continuity is not yet
  proven; resolve the failing boundaries through shard-generation, or generate the shards the proof
  still needs, then re-run the suite.

---
sceneNumber: '{XX}'
shardNumber: '{YY}'
beatName: '{BEATNAME}'
generatedDate: '{date}'
agentInputs:
  showrunner: true
  cinematographer: true
  scriptSupervisor: true
  promptEngineer: true
stateDiffPassed: true
---

[ID: SCENE_{XX}.{YY}_{BEATNAME}]

[Technical Header]:
_Lens and fps, then the hex-coded lighting style with its placement, then the atmosphere, then
interior or exterior. Every colour is a hex code from the Palette — never a vague colour name._

[Subject/Asset]:
_The character spec, critical anchors first. The `[ANCHOR POINT]` and `[CRITICAL]` features — the
LEFT/RIGHT-specific scar, the permanent crease, the expression, any unblinking mandate — lead the
block so they land inside the first 25%. Then the build, the wardrobe in its current condition, and
the held inventory. Reference a recurring element by its `[Asset: ID]`; do not re-describe it._

[Action/State]:
_What the character is doing this beat — the staged action, how they move and where they end. For a
15s or 30s beat, sequence the choreographed micro-beats here with explicit pacing; for a 5s beat,
one clean action._

[Environment/Lighting]:
_The lighting with hex codes and placement, the void and shadow with their hex, the background
treatment. The non-illuminated half, the negative space, the set — all in the production's colour
language._

[Temporal Constraint]:
{D} seconds. _The camera move and pacing, then the exit-state freeze — the exact end position,
expression, gaze, hand placement, and light state the next shard must open on. This is the handshake
the next shard reads. For 15s/30s, the scaled choreography and beat timing live here too._

---

**Build Notes:**
- Anchor Points: _what sits in the first 25% — the critical features that must survive the attention window._
- Vocabulary Compliance: _each banned word avoided and the required term swapped in for it._
- Exit Hook: _the exact handshake text the next shard's entry contract will read._
- Injections Applied: _the state the Script Supervisor injected, now baked into the prompt._
- Source Agents: Showrunner → Cinematographer → Script Supervisor → Prompt Engineer

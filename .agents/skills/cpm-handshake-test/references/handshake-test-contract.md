# CPM Handshake Test Contract

The required method for proving CPM holds continuity across a shard boundary — the seam where one
shard's exit state hands the next shard its opening. A Handshake Test Run grades a single adjacent
boundary; a Validation Suite chains that test across a scene and renders the binding CPM-VALIDATED
verdict. `scripts/validate_handshake.py` enforces the structural floor deterministically — this
document is the human-readable authority and the guide for grading by hand when the script is
unavailable. It teaches the method so it generalizes to any production; the examples are
illustrations, not fixed content.

A handshake test reads two already-generated artifacts and writes one report. It never edits a
shard, an exit state, the manifest, or the Slate — the production is the subject under test, never
the thing the test changes. What it proves is narrow and total: that everything the next shard
needs to stay continuous travelled to it through the exit state's entry contract alone, with no
human leaning in to remind the generator.

## What a boundary is

A handshake boundary lives inside one scene and spans exactly two adjacent shards: shard **A** is
shard `N`, shard **B** is shard `N+1`. Shard A's exit state carries the section `## Entry Contract
for Next Shard` — its `### MUST Start With:` and `### MUST NOT Show:` subsections. Shard B is the
compiled prompt with its six bracketed sections. The test grades shard B against the contract shard
A handed it; it does not re-derive the contract.

A scene's final shard owes no next-shard contract — it hands nothing forward. Its boundary is
therefore **not a testable handshake boundary**, and that is graceful, not an error: a no-boundary
result is reported as such and is never graded PASS or FAIL.

## The five continuity criteria

Each criterion is defined against the exit-state and compiled-prompt artifacts, and every one is
graded at the same hardness.

1. **Carried-object / inventory continuity.** Every object shard A is Holding — and every object
   named in its MUST Start With — appears in shard B's prompt, in the SAME hand (RIGHT / LEFT). A
   key carried in the RIGHT hand as shard A closes is in the RIGHT hand as shard B opens, named by
   the same `[Asset: ID]`. An object that vanishes, or migrates to the other hand, is a break.
   *(Structural floor: the `[Asset: ID]` and the RIGHT/LEFT hand marker from MUST Start With must be
   present in shard B.)*

2. **Distinctive-feature / identity continuity.** Every immutable LEFT/RIGHT-specific feature shard
   A carries — a scar along the LEFT jaw, a permanent crease — appears in shard B's prompt, on the
   same side. These features are the character's identity; the generator must hold them every shard,
   and the boundary is where drift first shows. *(Structural floor: the LEFT/RIGHT side marker; the
   feature itself is read by eye — a stray uppercase LEFT for a held object is not proof the scar
   survived.)*

3. **Style / lighting continuity.** Shard B's `[Environment/Lighting]` honours the Style Guide and
   carries the signature lighting from shard A's exit-state **Lighting Position** — the same
   signature hex and the same placement. A cold rim light raking from frame-left as shard A closes
   still rakes from frame-left, in the same hex, as shard B opens. *(Structural floor: shard A's
   signature hex must appear in shard B's `[Environment/Lighting]`; placement and Style-Guide
   compliance are read by eye when the project's `validation.require_style_compliance` gate in
   `.cpm/config.yaml` is on, its default.)*

4. **Spatial-position continuity.** Shard B opens on the position and facing shard A's MUST Start
   With mandates — the same framing (lens), the same screen placement, the same axis. A figure held
   at frame-left in 85mm, squared to the door, opens shard B exactly there. *(Structural floor: the
   lens and framing markers from MUST Start With must be present in shard B.)*

5. **Autonomy — no human reminder.** Every continuity element shard B honours traces to shard A's
   exit state and entry contract; nothing shard B got right required an out-of-band human
   re-injection. The entry contract was a complete enough carrier on its own. This is the criterion
   the whole module exists to satisfy: continuity that survives because the state machine carried
   it, not because a person re-typed it at the generator. Grading it means confirming each honoured
   element above maps to a line shard A actually wrote — if shard B is continuous only because a
   human hand-fed the detail, the boundary FAILS this even when criteria 1–4 read clean.

## The MUST-NOT-Show floor

Binding: **nothing on shard A's MUST NOT Show appears in shard B.** A warm tungsten wash shard A
forbids, a blink it forbids, an object not yet meant to be revealed — any one present in shard B
fails the boundary, at the same hardness as a missing required element. The entry contract is
binding in both directions: every MUST Start With met, nothing from MUST NOT Show present. A broken
handshake is the exact discontinuity this test exists to catch. *(Structural floor: no MUST NOT
Show token may appear in shard B.)*

## The same-hardness rule — the by-hand grading method

Grade every criterion, and the floor, at the **same hardness**. There is no softening one to a flag
or a note that travels on. A FAIL on ANY of the five criteria, or any MUST-NOT-Show element present,
fails the boundary — a boundary is PASS only when all five read PASS and the floor holds.

The method, so it generalizes to any production:

- **Read shard A's exit state.** Extract its entry contract — every MUST Start With bullet and every
  MUST NOT Show bullet — and its **Lighting Position** line (the signature hex and its placement).
  List the carried objects and their hands from **Holding**, and the distinctive features from the
  character spec the contract names.
- **Read shard B's compiled prompt.** For each MUST Start With element, find it in shard B and
  confirm it matches exactly — the same object in the same hand, the same feature on the same side,
  the same signature hex in the same placement, the same framing and facing. For each MUST NOT Show
  element, confirm it is absent.
- **Grade each of the five criteria PASS / FAIL** against what you found, then grade the floor.
- The boundary PASSES only if all five criteria and the floor are PASS. Name every FAIL with the
  criterion, what broke in shard B, and the exact fix.

The structural floor below reports which tokens are present, missing, or forbidden; it cannot read
meaning. The five criteria are the reading judgment that sits on top of it.

## The three-consecutive-pass law

A single PASS proves one boundary. **CPM is VALIDATED only when three CONSECUTIVE boundaries PASS.**
Any FAIL breaks the streak — the verdict is NOT VALIDATED, and the count restarts. Three consecutive
clean passes is the bar because continuity that holds once may be luck; continuity that holds three
times running is the system working.

A scene offers one boundary per adjacent pair: a `shard_count` of `S` yields `S-1` testable
boundaries, since the final shard owes none. A suite that cannot field three consecutive testable
boundaries — fewer than three exist, or a no-boundary ends the chain early — **cannot declare
VALIDATED.** That is not a continuity FAIL; it is insufficient evidence, and the report names the
gap: how many boundaries the scene offers, and how many more shards continuity would need to prove
out.

## What the script enforces vs what is judged by hand

The script owns the deterministic floor: locating and identity-matching the adjacent pair (shard A
is shard `N`, shard B is shard `N+1`, the same scene); confirming shard A handed a non-empty entry
contract, or is the final shard and so reports no-boundary; confirming each machine-extractable MUST
Start With token (a hex code, an `[Asset: ID]`, a RIGHT/LEFT marker, a lens spec) survives into
shard B; confirming no MUST NOT Show token appears in shard B; and confirming shard A's signature
lighting hex appears in shard B's `[Environment/Lighting]`. It reports which tokens are present,
missing, or forbidden — never whether the boundary "feels" continuous.

What stays a reading judgment: whether the carried object is genuinely the same object in the same
hand (criterion 1), whether the distinctive feature itself is named on the correct side (criterion
2), whether shard B's lighting honours the Style Guide's placement and not only the bare hex
(criterion 3), whether the framing actually opens the shard rather than trailing it (criterion 4),
and — the one no token can prove — whether every continuous element traces to shard A's contract
rather than a human reminder (criterion 5). Structure is held in code; substance is graded by the
reviewer.

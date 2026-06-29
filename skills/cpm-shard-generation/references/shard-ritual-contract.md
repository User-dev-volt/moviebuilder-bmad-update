# CPM Shard Ritual Contract

The required shape of a single run of the Four-Agent Ritual — the core production loop that turns
one pre-authored beat into one continuity-safe AI video prompt and the exit state that hands the
next shard its handshake. The Generate flow writes both artifacts; Regenerate rewrites them for a
beat already produced; Validate grades them against this contract. `scripts/validate_shard.py`
enforces the structural clauses deterministically — this document is the human-readable authority
and the guide for grading by hand when the script is unavailable. It teaches the method so it
generalizes to any production; the examples are illustrations, not fixed content.

One run produces **one shard** for **one beat**. The whole ritual exists to make that one prompt
safe to generate: every immutable feature in the attention window, every colour a hex code, the
state continuous with the shard before it, and an exit hook the shard after it can read.

## The governing law: one beat is one shard, loaded by integer

The current shard's content is **loaded**, never invented. The shard number resolves the current
beat — `currentBeat = currentShardNumber` — and the production loop pulls the one Beat Table row
whose Beat equals that number, plus its matching detail block, straight from the scene brief. The
Showrunner sharpens that loaded beat into the WHAT; the Showrunner does not author a new one on the
spot. This is the entire reason the scene brief is written up front: the beat is a pre-commitment,
and the ritual honours it.

A beat carries a single Primary Requirement — the one non-negotiable that shard must deliver. That
requirement rides through the whole ritual: the Showrunner restates it, the Cinematographer renders
it in hex and lens, the Script Supervisor checks it survived, and the Prompt Engineer front-loads
whatever of it is a critical anchor. If the loaded beat would contradict the Show Bible or break a
narrative contract, the Showrunner stops and raises it — a broken beat is held, not compiled.

## The Four-Agent Ritual — the hard-gated sequence

Four specialists run in a fixed order, each consuming the one before. The order is not negotiable,
and it is not parallel — STATE gates COMPILE.

1. **Showrunner — WHAT.** Loads beat N from the Beat Table and emits the **Showrunner Notes**: the
   beat's narrative intent and emotional truth, the Primary Requirement restated as the
   non-negotiable, and any narrative contract this beat plants, maintains, or pays off.
2. **Cinematographer — HOW.** Consumes the Showrunner Notes against the Style Guide, Palette, Lens
   Language, and Vocabulary, and emits the **Cinematographer Specs**: lens and fps, hex-coded
   lighting with placement, composition and negative space, camera move, atmosphere — every colour
   a hex code from the Palette, no banned word, the mandatory rim light present.
3. **Script Supervisor — STATE (the gate).** Consumes the entry contract, the character files, the
   prior exit state, the Showrunner Notes, and the Cinematographer Specs, and emits the **Continuity
   Validation** ending in a binding **Status**. This is the State-Diff Gate (below). Only a PASS
   moves forward.
4. **Prompt Engineer — COMPILE.** Only on a PASS, consumes all three upstream outputs plus the
   Vocabulary and compiles the final prompt. It refuses if any of the three inputs is missing or the
   Status is FAILED — a missing input is a refusal, never a guess.

The Script Supervisor is the one specialist that writes project state — the exit state, the manifest
Active Scene Context, and the Slate. The other three produce outputs the loop carries; they do not
write to the project.

## The State-Diff Gate — the load-bearing refusal

The gate is the safety of the whole loop. It compares the drafted beat against the state that must
persist and returns one of three Statuses:

- **VALIDATED** — every required detail is present, the full exit state is written, the handshake is
  defined, and no violation stands. Hand off to compilation.
- **VALIDATED WITH INJECTIONS** — a missing-but-known detail was actively written into the draft as
  exact text (the Script Supervisor injects; it never merely flags). Hand off with the injections
  applied.
- **FAILED** — the gate holds the pipeline. **No prompt compiles, no exit state is written, no
  manifest or Slate update happens.** The output is a structured hold that names every blocking item
  and the exact change required, routed back to the agent who owns the gap.

The non-negotiable: **every violation class holds at the same hardness.** A narrative-contract
breach, a protected-object reveal, a broken inherited handshake, and a position-based lighting
discontinuity each force FAILED. None of them is softened to a note that travels downstream with the
prompt. A failed gate is not a warning — it is a refusal, and the refusal is the point.

## The variable-interval rule

A beat's Duration is one of `5s`, `15s`, or `30s`, and it drives two things: the `[Temporal
Constraint]` of the compiled prompt and the choreography density of the action.

| Duration | Choreography | `[Temporal Constraint]` opens with |
|----------|--------------|------------------------------------|
| **5s** | One atomic action, one clean beat. | `5 seconds.` then the single movement and the exit hook. |
| **15s** | Two to three choreographed micro-beats; one camera move. | `15 seconds.` then sequenced micro-beats with pacing and the exit hook. |
| **30s** | Three to five micro-beats; multiple camera moves; evolving light. | `30 seconds.` then full choreography with beat timing and the exit hook. |

Duration scales the choreography *inside* one shard — it never changes the one-beat-one-shard
mapping, and it never relaxes the gate. A shard never spans two beats, and no shard is compiled
longer than `temporal.max_shard_duration`. Whatever the duration, the critical anchors stay in the
first 25% of the prompt: the attention window is fixed, not proportional to the clock.

## The compiled prompt — required shape

Written to `{project}/Output/Prompts/Scene_{XX}_Shard_{YY}_prompt.md`, where `{XX}` is the
two-digit scene number and `{YY}` is the bare shard integer (`Scene_01_Shard_1_prompt.md`).

Frontmatter carries exactly:

- **sceneNumber** — a string, zero-padded to two digits (`'01'`).
- **shardNumber** — a string, the bare beat integer (`'1'`).
- **beatName** — the UPPER_SNAKE form of the beat title (`'THE_ASSET_SCAN'`).
- **generatedDate** — the date.
- **agentInputs** — a mapping with `showrunner`, `cinematographer`, `scriptSupervisor`, and
  `promptEngineer`, each `true`. Every seat at the ritual is accounted for.
- **stateDiffPassed** — `true`. A prompt is never written while the gate reads false; the field is a
  structural truth, not a label.

The body carries six bracketed sections, in this order:

1. `[ID: SCENE_{XX}.{YY}_{BEATNAME}]` — the shard's identity (`[ID: SCENE_01.1_THE_ASSET_SCAN]`).
2. `[Technical Header]:` — lens and fps, hex-coded lighting, atmosphere, interior or exterior.
3. `[Subject/Asset]:` — the character spec. The critical anchors lead: the `[ANCHOR POINT]` and
   `[CRITICAL]` features sit in the first 25%, ahead of everything else.
4. `[Action/State]:` — what happens this beat; for a longer interval, the sequenced micro-beats.
5. `[Environment/Lighting]:` — hex-coded lighting with placement plus the void and shadow.
6. `[Temporal Constraint]:` — opens with the duration in seconds, then the camera move and the
   exit-state freeze the next shard handshakes against.

Then `**Build Notes:**` — bullets for Anchor Points (what sits in the first 25%), Vocabulary
Compliance (each banned word and the required term swapped in), Exit Hook (the exact handshake text),
Injections Applied (the state the Script Supervisor baked in), and Source Agents (the ritual order).

## The exit state — required shape

Written to `{project}/Production/Scenes/Scene_{XX}/state/shard_{YY}_exit_state.md`, the bare shard
integer again (`shard_1_exit_state.md`). It is the only baseline the next shard has, so it carries
the full state, never a position alone.

Frontmatter: **sceneNumber**, **shardNumber** (matching the prompt), **generatedDate**, and
**generatedBy** (`'shard-generation-ritual'`). Sections, with these exact headings:

- `## Character States` — one `### {Name}` per on-camera character, each with **Position**,
  **Facing**, **Expression**, **Action**, **Holding**, and **Physical Condition** (the condition
  flags plus arc progress %).
- `## Environment State` — **Lighting Position**, **Time Progression**, **Active Environmental
  Elements**.
- `## Entry Contract for Next Shard` — `### MUST Start With:` and `### MUST NOT Show:`, each a bullet
  list. This handshake is **mandatory and non-empty on every shard but the scene's last**; the final
  shard owes no next-shard contract.
- `## State Changes This Shard` — a table `| Element | Previous Value | New Value | Reason |`.
- `## Active Contracts` — a table `| Contract ID | Status | Notes |`.

## What the script enforces vs what is judged by hand

The script owns the deterministic structure: the prompt frontmatter field set, `stateDiffPassed`
true, all four `agentInputs` true, the six bracketed sections in order, the `[Temporal Constraint]`
opening on a 5/15/30-second duration, the sibling exit state's existence and identity match, the
exit-state sections (and a non-final shard's non-empty entry contract), and — when the scene brief
carries a machine-readable Beat Table — the cross-checks that the shard number is in range, the beat
exists in the table, and the prompt's duration equals the beat's Duration. When the brief carries no
Beat Table, those cross-checks degrade to a single warning rather than a hold, because a production
may carry an older brief shape.

What stays a reading judgment: whether the critical anchors genuinely sit in the first 25%, whether
the prompt is continuity-safe against the entry contract, whether any banned word slipped through,
and whether the exit hook is one the next shard can actually handshake against. Structure is held in
code; substance is graded by the reviewer.

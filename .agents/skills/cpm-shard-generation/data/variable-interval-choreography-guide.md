# Variable-Interval Choreography Guide

A beat's Duration is one of `5s`, `15s`, or `30s`. Duration does one job: it scales how much
choreography is packed *inside* a single shard. It never splits a beat across two shards, and it
never relaxes the State-Diff Gate. This guide calibrates the density so a longer shard stays one
atomic beat with more motion — not two beats wearing one number.

The default comes from `temporal.default_shard_duration` in `.cpm/config.yaml`; a beat may override
it in the Beat Table. No shard is ever compiled longer than `temporal.max_shard_duration`.

## The one rule that does not scale with the clock

The attention window is fixed. The critical anchors — the LEFT/RIGHT-specific scar, the permanent
crease, the expression, the unblinking mandate — sit in the first 25% of the prompt whether the
shard is 5 seconds or 30. A 30s prompt is longer, so 25% of it is more text; the anchors still lead
it. Length buys more choreography, never a later scar.

## 5 seconds — one clean beat

- **Choreography:** a single atomic action. One thing happens, cleanly, and the shard ends on it.
- **Camera:** one move, or a held frame. No sequence.
- **`[Action/State]`:** one staged action described in full.
- **`[Temporal Constraint]`:** opens `5 seconds.`, then the single movement, then the exit-state
  freeze.
- **Exit hook:** the end position of that one action.

_Example shape:_ the subject performs a single precise swipe; the light flickers once as the file
turns; the body returns to stillness. One micro-beat, one freeze.

## 15 seconds — two to three micro-beats, one camera move

- **Choreography:** two or three choreographed micro-beats that serve one narrative through-line.
  They are moments of the same beat, not separate beats — the Primary Requirement is delivered once,
  across the sequence.
- **Camera:** one deliberate move (a dolly, a rack, a track) carrying the sequence.
- **`[Action/State]`:** sequence the micro-beats with explicit pacing — beat one lands, then beat
  two, then the close — so the generator paces them rather than rushing or stalling.
- **`[Temporal Constraint]`:** opens `15 seconds.`, then the sequenced micro-beats with their pacing,
  then the exit hook.
- **Exit hook:** the end position of the *last* micro-beat.

_Example shape:_ the subject steps out, the thumb traces the glove seam, the head turns to the
corridor — three moments of one armoring ritual, carried by a single tracking move.

## 30 seconds — three to five micro-beats, multiple moves, evolving light

- **Choreography:** three to five micro-beats, still one beat's through-line. The most a single shard
  carries. If the action wants more than five distinct moments, it is two beats — send it back to the
  scene brief, do not overload the shard.
- **Camera:** multiple moves; the light may evolve across the shard (a gradient shift, a source
  entering frame) — record the evolution in the exit state so the next shard's lighting check has a
  baseline.
- **`[Action/State]`:** the full choreographed sequence with beat timing.
- **`[Temporal Constraint]`:** opens `30 seconds.`, then the full choreography with timing, then the
  exit hook.
- **Exit hook:** the end position of the final micro-beat and the final light state.

## The over-packing test

If a 15s or 30s shard cannot state its Primary Requirement as a single non-negotiable — if it needs
two — the beat was split wrong upstream. A shard is one beat at any duration. More seconds buy more
choreography of the same beat; they never buy a second beat. When the density stops feeling like one
continuous action, stop and fix the beat in the scene brief rather than compiling a shard that hides
two beats inside one number.

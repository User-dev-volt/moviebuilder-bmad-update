---
capability: variable-interval-compilation
description: Compiles a final prompt for a target shard duration of 5s, 15s, or 30s — scaling the Temporal Constraint and choreography while keeping critical features in the first 25%.
---

# Variable Interval Compilation

## What Success Looks Like

The compiled prompt matches the shard's target duration. A 5s shard holds one clean beat; a 15s or 30s shard carries choreographed micro-beats and more camera movement — without ever pushing the critical features out of the first 25%. The duration comes from config, not a guess.

## Read First — Every Time (Inputs Required)

The same three required inputs as standard compilation, plus the target duration. **Refuse to compile if any box is unchecked:**

- [ ] **Showrunner Notes (WHAT)** — the beat; for 15s/30s, the narrative through-line the micro-beats serve.
- [ ] **Cinematographer Specs (HOW)** — lens, lighting, hex palette, composition; plus any camera movement for the longer interval.
- [ ] **Script Supervisor validation (STATE)** — must read **VALIDATED**. If **FAILED**, halt — do not compile.
- [ ] `Architecture/Vocabulary.md` — the banned/required word list.
- [ ] **Target duration** — from `temporal.default_shard_duration` in `.cpm/config.yaml` (default 5), or a per-shard override. Honor `temporal.max_shard_duration` (default 30) as the ceiling — never compile a shard longer than the max.

If any of the three agent inputs is missing, or the Script Supervisor status is FAILED, do not compile — emit the refusal and stop. Longer duration never relaxes the gate.

## Scaling the Shard

| Duration | Choreography | `[Temporal Constraint]` |
|---|---|---|
| **5s** | One atomic action. One clean beat. | {5} seconds, single movement, exit-state hook. |
| **15s** | 2–3 choreographed micro-beats; one camera move. | {15} seconds, sequenced micro-beats with pacing, exit-state hook. |
| **30s** | 3–5 micro-beats; multiple camera moves; evolving light. | {30} seconds, full choreography with beat timing, exit-state hook. |

Whatever the duration, the `[Subject/Asset]` block leads with the critical features — the attention window does not stretch with the clock. The scar sits in the first 25% of a 30s prompt exactly as it does in a 5s prompt.

## Output

The same compiled prompt structure as standard Prompt Compilation (see `references/prompt-compilation.md`), with two adjustments:

- a `[Temporal Constraint]` scaled to the target duration, and
- for 15s/30s, an `[Action/State]` block that sequences the micro-beats with explicit pacing and camera movement.

End with the same **Build Notes** (Anchor Points, Vocabulary Compliance, Exit Hook, Injections Applied).

**If compilation is blocked**, emit this instead of the prompt block:

> **CANNOT COMPILE — missing/blocked:** {missing input(s), or "Script Supervisor status = FAILED"}.
> Nothing compiled. Resolve upstream with the owning agent, then re-run. No partial prompt is emitted.

## The Rules

- **All three agent inputs are still required, and FAILED still halts.** A longer duration never waives the gate.
- **Critical features stay in the first 25%** regardless of duration — the attention window is fixed, not proportional.
- **Never exceed `temporal.max_shard_duration`** (default 30s). If a request asks for more, hold and flag it rather than compile it.
- **No banned words; hex codes always; always an exit-state hook** — the longer the shard, the more state there is to keep honest.

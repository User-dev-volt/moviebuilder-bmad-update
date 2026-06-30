---
capability: beat-definition
description: Defines the single atomic beat for the current shard — its focus and primary narrative requirement — extracted from the scene brief.
---

# Beat Definition

## What Success Looks Like

The current shard has exactly one atomic beat, with a clear focus and a single primary requirement the rest of the crew can build on. The beat is extracted from the scene brief — not invented — and its narrative contract status is known.

## Read First — Every Time

This agent is stateless. Before defining the beat, read fresh from the production project — you cannot enforce canon you haven't loaded:

- [ ] `Bible/Show_Bible.md` — themes, world rules, and character arcs (the canon the beat must not contradict)
- [ ] `Bible/Characters/{on_camera_characters}.md` — arc position and current state, for the Motivation check
- [ ] The scene brief — `Production/Scenes/Scene_{XX}/scene-brief.md`
- [ ] The current shard number (the beat to define)
- [ ] Active `Production/Contracts/*.md` — to set contract status on this beat

## The Extraction Rule — Critical

When a scene brief exists, **the beat already exists** — your job is to extract and sharpen it, not to author a new one. The filmmaker directed these beats during scene creation; inventing beats here is the failure mode this guards against. Only when no scene brief exists may you propose a beat — and then you must flag that a scene brief should be created via `cpm-scene-create`.

## Output — the Showrunner Notes for the current beat

This is the **Showrunner Notes** the headless Four-Agent Ritual hands downstream — the WHAT for one shard, that the Cinematographer renders and the Script Supervisor tracks. For the current shard, define:

- **Beat ID:** {XX}.{shard}
- **Duration:** inherited from the scene brief / the `temporal.default_shard_duration` key in `.cpm/config.yaml` (default 5s; may be 15s or 30s)
- **Focus:** the one thing this beat is about
- **Primary Requirement:** what must be achieved narratively for this beat to count
- **Motivation:** the arc-driven reason the character does what they do here (checked against the arc in `Bible/Characters/*.md`)
- **Narrative Contract Status:** {Contract_ID}: PLANT / MAINTAIN / PAYOFF — or AT-RISK / BROKEN if this beat strands or breaks the contract
- **Note to Cinematographer:** what this beat needs emphasized visually — WHAT to emphasize, never how to light it; the visual interpretation is hers
- **Note to Script Supervisor:** the state this beat changes or must hold, for the exit-state handshake to track

For longer shards (15s / 30s), the beat may contain choreographed micro-moments — describe the narrative through-line and let the Cinematographer and Prompt Engineer handle choreography density. The beat stays atomic: one focus, one primary requirement.

## The Rule

**Never define a beat that contradicts the Show Bible or breaks a Narrative Contract.** If the scene brief's beat does either, stop and raise it — a BROKEN beat is held, not passed downstream.

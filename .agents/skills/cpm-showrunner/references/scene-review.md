---
capability: scene-review
description: Reviews a scene for thematic alignment and breaks it into atomic beats, producing the Showrunner Notes the rest of the crew builds on.
---

# Scene Review

## What Success Looks Like

The scene is confirmed to serve the larger narrative, every beat is motivated by character arc, and the crew downstream (Cinematographer, Script Supervisor, Prompt Engineer) receives a clear, atomic beat breakdown with no ambiguity about WHAT happens or WHY. The output is a single artifact: the **Showrunner Notes**.

## Read First — Every Time

This agent is stateless. Before writing a single note, read fresh from the production project:

- [ ] `Bible/Show_Bible.md` — themes, world rules, character arcs (the canon)
- [ ] `Bible/Characters/{on_camera_characters}.md` — current state and arc position of every character on camera
- [ ] `Production/Contracts/*.md` — every active narrative contract

Do not review a scene from memory or from the scene brief alone. The Bible is the authority.

## Inputs

- The scene brief — `Production/Scenes/Scene_{XX}/scene-brief.md` — the filmmaker-directed beats for this scene
- The Show Bible, on-camera character files, and active contracts (read above)

## Output Format — Showrunner Notes

Produce exactly this structure:

### Scene {XX} Showrunner Notes

**Thematic Alignment:** How this scene serves the story — name the thematic pillar(s) it advances.

**Character Arc Check:**
- {Character}: current arc position, and the emotional truth this scene must land.

**Atomic Beat Breakdown:**

| Beat | Duration | Focus | Primary Requirement |
|------|----------|-------|---------------------|
| {XX}.1 | {duration} | {focus} | {what must be achieved} |
| {XX}.2 | {duration} | {focus} | {what must be achieved} |

**Narrative Contract Status:**
- {Contract_ID}: PLANT / MAINTAIN / PAYOFF / AT-RISK / BROKEN

**Canon & Contract Check:** PASS — every beat serves the Show Bible and honors all active contracts. / HELD — {beat id}: {the Bible section or Contract_ID it violates}, held for rework. A non-PASS result blocks the downstream notes below: do not hand a broken beat to the crew.

**Notes to Cinematographer:** Visual emphasis needed (WHAT to emphasize — not how to light it).

**Notes to Script Supervisor:** State changes to track this scene.

> **Duration:** beats inherit the scene's shard duration from the scene brief / the `temporal.default_shard_duration` key in `.cpm/config.yaml` (default 5s). Do not assume 5s — a production may run 15s or 30s shards.

## The Rules

- Define WHAT happens, not HOW it looks. Visual interpretation is the Cinematographer's domain — your notes to her say what matters, not how to shoot it.
- Every beat's action must be motivated by the character's arc. If a beat isn't motivated, send it back rather than rationalize it.
- **Never approve a beat that contradicts the Show Bible.** This is the hard gate of Scene Review — a beautiful beat that breaks canon is a rejected beat.
- **Never approve a beat that breaks or strands a Narrative Contract.** Same hard gate as the Bible: a contract you cannot honor is a beat you hold and send back — surface it now, do not pass it downstream with a note attached.
- Beats come from the scene brief. When a brief exists, your breakdown extracts and sharpens its beats — you do not invent new ones.

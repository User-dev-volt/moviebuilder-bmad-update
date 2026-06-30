---
scene_number: '{XX}'
scene_id: 'SCENE_{XX}'
scene_title: '{Title}'
status: 'ready'
shard_count: {N}
default_shard_duration: {D}
on_camera_characters:
  - {Name}
arc_position: '{where this scene sits in the overall arc}'
created: '{date}'
lastModified: '{date}'
---

# Scene {XX}: {Title}

## Setting

- **Location:** _Where the scene happens — name the spaces and how they read on camera._
- **Time of Day:** _The hour and the quality of light it brings._
- **Atmosphere:** _The felt air of the place — sound, temperature, what the space does to a person._

## On-Camera Characters

_Optional; recommended once two or more characters share the frame. One entry per character —
the plain name, a link to their state file, and a one-line role in this scene. Each name here
must also appear in the `on_camera_characters` frontmatter and resolve to a character file._

- **{Name}** — `Bible/Characters/{Name}.md` — _their role in this scene._

## Narrative Purpose

_What this scene is for in the story — the spine every beat hangs on._

**Serves theme:** _name at least one theme from the Show Bible this scene advances._

## Emotional Arc

- **Opens at:** _the emotional state the scene begins in._
- **Closes at:** _the emotional state it lands on — the change the scene buys._

## Beats

_Two layers. The **Beat Table** is the authoritative, machine-read index — the production loop
pulls the one row whose Beat equals the shard number, with zero transformation. The **Beat
Details** carry the filmmaker direction. They must stay 1:1 by integer: the four-way equality
holds (shard_count == Beat-Table rows == Beat-Detail blocks == max(Beat)) and the Beat column is
contiguous integers 1..shard_count, exactly one row each. Beat N is Shard N._

### Beat Table

_Columns are exactly `Beat | Duration | Focus | Primary Requirement` — no more, no fewer, this
order. One row per beat. Duration is 5s, 15s, or 30s (default {D}s, override per beat). Focus
names a character from `on_camera_characters` plus framing. Primary Requirement is the single
non-negotiable that beat must deliver and must name at least one concrete checkable element — a
hex code, a lens, a LEFT/RIGHT designation, a named prop, or a condition flag._

| Beat | Duration | Focus | Primary Requirement |
|------|----------|-------|---------------------|
| 1 | {D}s | _{Name} — subject + lens/framing_ | _the single non-negotiable; name at least one concrete checkable element_ |
| 2 | {D}s | _{Name} — subject + lens/framing_ | _the single non-negotiable; name at least one concrete checkable element_ |

### Beat Details

_One block per beat, keyed by the same integer as the table. Details do not restate Duration or
Primary Requirement — the table owns those, which keeps the two layers from drifting. Reference
characters by name; never restate their immutable visual identity (scar, hair part, build) —
that lives only in the character file._

#### Beat 1 — {Beat Title}
- **Action:** _The staged physical action — the meat of the shard._
- **Emotional Note:** _The emotional state or shift this beat carries._
- **Shot:** _Fuller camera spec — lens, movement, framing — beyond the table's one-line Focus._
- **Continuity In:** _Beat 1: carry-in per `state/entry_contract.md`. Later beats: optional._
- **State Change:** _Optional — condition flags, inventory, or arc-% delta this beat produces._

#### Beat 2 — {Beat Title}
- **Action:** _The staged physical action._
- **Emotional Note:** _The emotional state or shift._
- **Shot:** _Lens, movement, framing._
- **State Change:** _Optional._

## Continuity Carry-Out

_Optional — a scene-level note of what the next scene should assume. The authoritative carry-out
is still the last shard's exit state, written later during shard generation; this is intent, not
the contract._

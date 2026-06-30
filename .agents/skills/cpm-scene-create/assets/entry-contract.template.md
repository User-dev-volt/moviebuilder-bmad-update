---
scene_id: 'SCENE_{XX}'
applies_to_shard: 1
derived_from: '{character-initial-state | Scene_{XX-1}/state/shard_{last}_exit_state.md}'
created: '{date}'
---

# Entry Contract — Scene {XX}, Shard 1

_Seeds Shard 1's carry-in state. The Script Supervisor validates Shard 1 against this; every
later shard validates against the previous shard's `shard_{Y}_exit_state.md`. Asset IDs (e.g.
`{NAME}_V1`) are captured here, not in the brief frontmatter — the brief names characters
plainly._

_Author this in one of two ways:_

- **Scene 01, or when the prior scene's last exit state exists:** derive the carry-in below from
  the character state files (and that exit state, when present). Set `derived_from` accordingly.
- **A later scene whose prior exit state does not exist yet:** keep the section shapes but mark
  the unknown values as an explicit gap with the line:
  `> unresolved — Script Supervisor fills before Shard 1`
  Point `derived_from` at the expected `Scene_{XX-1}/state/shard_{last}_exit_state.md` path. This
  marks the handoff instead of leaving it silently hollow; Validate surfaces it as a warning, not
  a hold.

## On-Camera Characters (carry-in)

### {Name} — Bible/Characters/{Name}.md (assetID {NAME}_V1)
- **Conditions (carry-in):** _active condition flags, matching the character file's vocabulary._
- **Inventory in-hand:** _items and the hand or place they occupy (RIGHT / LEFT / POCKET / NECK)._
- **Outfit:** _per the character file — base garment and the colors that must read._
- **Arc progress (carry-in):** _a percentage, matching the character file's Arc Position._

## Open Narrative Contracts (carry-in)

- _list active `Production/Contracts/*.md`, or "none"._

## Setting at Entry

- **Location:** _where the scene opens._
- **Light state:** _the named light condition and its hex, if the Style Guide defines one._

## Notes to Script Supervisor

- Seed entry state. Validate Shard 1 against this; later shards validate against
  `shard_{Y-1}_exit_state.md`.

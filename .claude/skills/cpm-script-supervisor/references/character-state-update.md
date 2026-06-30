---
capability: character-state-update
description: Updates a character's state file after a scene's events, applying only mutable changes and appending a version-history row so prior state is never silently dropped.
---

# Character State Update

## What Success Looks Like

After a scene's events, the character's file reflects the new mutable state — and the change is auditable. Immutable features are untouched, prior state is never silently dropped, and a version-history row records what changed and why. The output is the updated `Bible/Characters/{Name}.md`.

## Read First — Every Time

This agent is stateless and this capability **writes**. You cannot safely update a file you have not read — that is exactly how prior state gets dropped. Before writing, read fresh from the production project:

- [ ] `Bible/Characters/{Name}.md` — the full current file: immutable features, mutable state, inventory, arc position, and the existing version-history table
- [ ] the scene completion notes — what actually changed this scene (new wounds, lost/gained inventory, arc movement, position at scene end)
- [ ] the scene's final exit state — `Production/Scenes/Scene_{XX}/state/` (the last shard's `exit_state.md`) — to reconcile end-of-scene position and condition

## What You May and May Not Change

- **Mutable state** — wounds, dirt, wardrobe condition, inventory, emotional/arc position, last-known position. Update to match the scene's outcome.
- **Immutable features** — LEFT/RIGHT-specific scars, marks, permanent traits, core identity. Never change these here. If the completion notes appear to alter an immutable feature, that is a contradiction, not an update: HOLD and raise it.

## Output — Updated Character File + Version-History Row

1. Apply the mutable-state changes to the relevant sections of `Bible/Characters/{Name}.md`.
2. Append a row to the file's existing **Version History** table — match the table's own columns (the established character-file format is `| Version | Scene | Changes |`), and never overwrite or delete prior rows:

| Version | Scene | Changes |
|---|---|---|
| V{n} | Scene {XX} | {the exact mutable fields changed (old → new), and the scene event that caused it} |

3. Write the file. Prior state remains legible in the history; nothing is silently dropped.

**If the update cannot be made cleanly — HOLD:** (refusal slot — do not write while this is unresolved)

- State the conflict — e.g. a completion note that would overwrite an immutable feature, or two notes that contradict each other — and do not write until it is reconciled. A corrupted character file breaks continuity for every future shard, so a clean HOLD is correct and a wrong guess is not.

## The Rule

**Never silently drop prior state, and never overwrite an immutable feature.** Every change is additive to the version history and confined to mutable state. When the notes are ambiguous or conflict with canon, HOLD and surface the conflict rather than writing a guess into the file that every downstream shard will trust.

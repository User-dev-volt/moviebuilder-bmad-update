# CPM Character State File Contract

The required shape of a character state file — the continuity anchor the Script Supervisor and Prompt Engineer reload every shard. Create writes this in full; Update changes mutable state without touching the immutable identity; Validate grades a file against it. `scripts/check_character.py` enforces the structural clauses deterministically — this document is the human-readable authority and the guide for grading by hand when the script is unavailable. It teaches the method so it generalizes to any production; the examples are illustrations, not fixed content.

## The non-negotiable: lateral specificity

Every asymmetric immutable feature is pinned to LEFT or RIGHT, and BOTH sides are accounted for. This is the whole reason the file exists: an AI video model is stateless and will mirror or drift any side left unstated, so a scar described only as "on the jawline" lands on a different side every generation. A crease above the LEFT eyebrow, a part on the LEFT, a childhood scar on the RIGHT jawline, a hand that always leads with the RIGHT while the LEFT carries weight — each pinned, both sides resolved.

Write each side as the literal uppercase token `LEFT` or `RIGHT` in the authored feature text. The structural check scans only the authored immutable content for those tokens (template guidance and the section intro are stripped first, so boilerplate that names both sides cannot pass for a non-anchored file), so even a deliberately symmetric feature still names both — e.g. "symmetrical laugh lines, LEFT and RIGHT matched."

Treat the two sides at equal hardness. A character that specifies one side and leaves the other unstated is held, not shipped — the same as a character missing a required section. There is no "flag the missing side and proceed."

## Required header

- An H1 title line: `# Character: {Name}`
- `**Asset ID:**` — the character's stable identifier with its current state version, convention `{NAME}_V1` (uppercase). The version suffix is bumped only when a confirmed story event changes an immutable feature.
- `**Status:**` — the casting status, e.g. `ACTIVE`, `RETIRED`, `DRAFT`.

A small frontmatter block carrying `characterName`, `assetID`, `status`, `created`, and `lastModified` is conventional and recommended, but the H1 and the two bold fields above are the load-bearing header.

## Immutable vs mutable

| Part | Immutable? | Owned by |
|------|------------|----------|
| Visual Identity (Face, Body, Movement) | Immutable unless a story event changes it | Create; Update only on a surfaced, confirmed conflict |
| Current Outfit | Mutable per scene | Create and Update |
| Inventory | Mutable per scene | Create and Update |
| Physical State | Mutable per scene | Create and Update |
| Behavioral Profile | Stable, rarely changes | Create and Update |
| Arc Position | Mutable as the arc advances | Create and Update |

## Required sections

- **`## Visual Identity (Immutable Unless Story Changes)`** — the anchor, with two subsections:
  - **`### Face`** — Distinguishing Features (the permanent marks, each anchored LEFT/RIGHT), Expression Default (the resting face), Age Appearance.
  - **`### Body`** — Build, Posture, and Movement Style (note any LEFT/RIGHT-dominant habit). Movement may be its own `### Movement` subsection when it carries weight, but the Movement Style detail belongs in this section either way.
- **`## Current Outfit (Mutable - Update Per Scene)`** — Base, Condition, Accessories.
- **`## Inventory (Mutable)`** — a table: `| Item | Status | Acquired | Notes |`. Status uses a slot vocabulary such as `EQUIPPED_PRIMARY_HAND (RIGHT)`, `EQUIPPED_SECONDARY_HAND (LEFT)`, `POCKET`, `NECK (Worn)`, `HIDDEN`, `*_ENVIRONMENT`.
- **`## Physical State (Mutable)`** — a table: `| Condition | Location | Severity | Since |`. Holds the bodily conditions a shard must render (tension, breathing, injury) and how they progress.
- **`## Behavioral Profile (For Prompt Engineer)`** — Speech Pattern, Nervous Tic, Signature Move.
- **`## Arc Position`** — Current Emotional State, Character Want, Character Need, Arc Progress (a percentage).
- **`## Version History`** — a table: `| Version | Scene | Changes |`. Starts at `V1 | {scene} | Initial state`.

## The roster index row

`Bible/Characters/_index.md` carries one table: `| Character | Description | Asset ID | Status |`. Every character has exactly one row:

```
| **{Name}** | {one-line visual signature — the few details that identify them at a glance, including the load-bearing lateral marks} | {AssetID} | {Status} |
```

The character's name appears bolded as `**{Name}**` so the structural check can confirm the row exists. When a character is created and no index exists yet, the index is created from its template first, then the row appended.

## What Update may and may not touch

Update changes mutable state only and appends a row to Version History for every change. It never silently overwrites an immutable Visual Identity feature on either side. When a requested change would alter an immutable feature, the conflict is surfaced first and changed only on explicit confirmation that a story event justifies it; that change bumps the Asset ID version and is logged as an override with its reasoning. The roster row is updated whenever the visual signature, Asset ID, or status changes.

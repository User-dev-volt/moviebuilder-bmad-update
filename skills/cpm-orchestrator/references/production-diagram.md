---
capability: production-diagram
description: Generates or updates the per-project living Excalidraw diagram showing this production's scenes, characters, act structure, and shard completion.
---

# Production Diagram

## What Success Looks Like

The user receives an updated `Diagrams/production-flow.excalidraw` file in their project folder that visually maps THIS production's current state — acts, scenes (with status), characters on set, and shard completion counts. The diagram evolves as production progresses.

## Required Inputs

Read the following before generating (all from the production project folder):

- `Production/Slate.md` — scene list, shard counts, status per scene
- `Bible/Show_Bible.md` — act structure, title, themes
- `Bible/Characters/_index.md` — character roster with brief descriptions
- `.cpm/manifest.md` — active scene and current shard context

## Diagram Architecture

Generate a `.excalidraw` JSON file structured as:

**Section 1: Production Header**
- Project title (from Show Bible)
- Target model + default shard duration (from `.cpm/config.yaml`)
- Overall completion status

**Section 2: Act Structure**
- Horizontal bands for each act
- Scene nodes within each act, sized by shard count
- Status color coding: Not Started (light gray), In Progress (blue `#3b82f6`), Complete (green `#a7f3d0`), Validated (deep green `#047857`)

**Section 3: Character Roster**
- Character names in a column on the left
- Horizontal lines showing which scenes each character appears in (derived from character files' scene tracking)

**Section 4: Production Progress**
- Shard completion bar per scene
- Handshake test status

## Color Conventions

Follow the same semantic palette as the methodology diagram:
- Not started: `#dbeafe` / `#1e40af` (dashed stroke)
- In progress: `#3b82f6` / `#1e3a5f`
- Complete: `#a7f3d0` / `#047857`
- CPM Validated: `#a7f3d0` fill with bold `#047857` border (3px)
- Active/current scene: `#ddd6fe` / `#6d28d9` (AI/highlight color)

## Output

Write the generated `.excalidraw` JSON to `{project-folder}/Diagrams/production-flow.excalidraw`.

If the file already exists, update it — preserve the layout of completed sections, update status colors and shard counts for in-progress scenes.

Confirm the file path to the user and provide import instructions if they haven't used Excalidraw before.

---
capability: production-status
description: Reads Production/Slate.md and formats a clear production progress report.
---

# Production Status Report

## What Success Looks Like

The user gets a clean, scannable report showing exactly where the production stands — which scenes are done, which are in progress, what's next, and whether any continuity has been validated.

## Required Inputs

Read (all from the production project folder):
- `Production/Slate.md` — the primary source
- `.cpm/manifest.md` — active scene context
- Any `Production/Scenes/{XX}/state/` folders — to count exit states and check handshake status

## Report Format

```
## Production Status: {Project Title}
**Model:** {target_model} | **Default Shard Duration:** {default_shard_duration}s
**Last Updated:** {date from Slate.md}

### Scene Progress

| Scene | Status | Shards | Handshake |
|---|---|---|---|
| Scene 01: {title} | ✅ Complete | 6/6 | ✅ Validated |
| Scene 02: {title} | 🔵 In Progress | 3/8 | — |
| Scene 03: {title} | ⬜ Not Started | 0/? | — |

### Active Context
**Current scene:** {scene from manifest}
**Next shard:** #{number}
**Entry contract:** {set / not set}

### Open Items
{Any scenes missing entry contracts, failed handshakes, or character state needing update}

### Recommended Next Action
{Single specific recommendation based on the state above}
```

## Handling Missing Data

If `Production/Slate.md` doesn't exist, report that the project hasn't been scaffolded yet and suggest running `cpm-new-project` or `cpm-inception`. Don't invent status data.

If shard counts in `Slate.md` don't match the `Production/Scenes/` folder structure, note the discrepancy and recommend a manifest update.

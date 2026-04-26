# Context Loading Checklist

## Required Files for Shard Generation

Every shard generation MUST load these files before any agent review begins.

### Bible (Always Load)

| File | Path | Required |
|------|------|----------|
| Show Bible | `{project-root}/Bible/Show_Bible.md` | YES — always |
| On-Camera Characters | `{project-root}/Bible/Characters/{character_name}.md` | YES — per manifest |

### Architecture (Always Load)

| File | Path | Required |
|------|------|----------|
| Style Guide | `{project-root}/Architecture/Style_Guide.md` | YES — always |
| Vocabulary | `{project-root}/Architecture/Vocabulary.md` | YES — always |

### Production (Always Load)

| File | Path | Required |
|------|------|----------|
| Scene Brief | `{project-root}/Production/Scenes/Scene_{XX}/scene-brief.md` | YES — always (defines the beats the Showrunner interprets for this scene) |

### State (Conditional)

| File | Path | Required |
|------|------|----------|
| Previous Shard Exit State | `{project-root}/Production/Scenes/Scene_{XX}/state/shard_{Y-1}_exit_state.md` | YES — if shard > 1 |
| Previous Scene Exit State | `{project-root}/Production/Scenes/Scene_{XX-1}/state/scene_exit_state.md` | YES — if scene > 1 and shard == 1 |

### Contracts (If Any Exist)

| File | Path | Required |
|------|------|----------|
| Active Contracts | `{project-root}/Production/Contracts/*.md` | YES — if directory has files |

### Context Index

| File | Path | Required |
|------|------|----------|
| Manifest | `{project-root}/.cpm/manifest.md` | YES — always (lists which characters are on-camera) |

## HALT Conditions

**HALT the ritual if ANY of these are true:**
- Show Bible does not exist
- Style Guide does not exist
- Vocabulary does not exist
- Manifest does not exist
- Scene Brief does not exist for the current scene (`Production/Scenes/Scene_{XX}/scene-brief.md`) — run `/cpm-scene-create` first
- Any on-camera character file listed in manifest does not exist
- Previous shard exit state does not exist (when shard > 1)
- Previous scene exit state does not exist (when scene > 1 and shard == 1)

## Context Loaded Confirmation

After loading all files, display:

```
✅ Context Loaded for Scene {XX}, Shard {Y}
- Bible: Show_Bible.md
- Characters: {list of loaded character names}
- Architecture: Style_Guide.md, Vocabulary.md
- Scene Brief: scene-brief.md ({shard_count} shards — Shard {Y}: {beat action summary})
- State: {previous exit state file or "First shard — no previous state"}
- Contracts: {count} active contracts loaded
```

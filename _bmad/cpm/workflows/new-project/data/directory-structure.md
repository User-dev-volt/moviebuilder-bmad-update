# CPM Project Directory Structure

This reference shows the complete directory structure created by the new-project workflow.

## Structure Preview

```
{project_name}/
├── .cpm/
│   ├── config.yaml          # Project configuration
│   ├── manifest.md          # Context index for agents
│   └── agents/
│       ├── showrunner.md         # Story guardian
│       ├── cinematographer.md    # Visual architect
│       ├── script-supervisor.md  # Continuity tracker
│       └── prompt-engineer.md    # Prompt compiler
├── Bible/
│   ├── Show_Bible.md        # Story bible (placeholder)
│   ├── Characters/
│   │   └── _index.md        # Character index
│   └── World/
│       └── _index.md        # World-building index
├── Architecture/
│   ├── Style_Guide.md       # Visual style guide (placeholder)
│   ├── Palette.md           # Color palette (placeholder)
│   ├── Lens_Language.md     # Camera language (placeholder)
│   └── Vocabulary.md        # Prompt vocabulary (placeholder)
├── Production/
│   ├── Slate.md             # Production status
│   ├── Scenes/              # Scene files
│   └── Contracts/           # Narrative contracts
└── Output/
    ├── Prompts/             # Generated prompts
    └── Renders/             # Rendered outputs
```

## Folder Purposes

| Folder | Purpose |
|--------|---------|
| `.cpm/` | Project configuration and agent prompts |
| `Bible/` | Story content - Show Bible, characters, world |
| `Architecture/` | Visual language - style guide, palette, vocabulary |
| `Production/` | Active production - scenes, shards, contracts |
| `Output/` | Generated content - prompts and renders |

## Files Created

### Generated Files (content filled by workflow)
- `.cpm/config.yaml` - Project settings with model target
- `.cpm/manifest.md` - Context index for current production state
- `Production/Slate.md` - Production tracking

### Copied Files (from CPM templates)
- `.cpm/agents/*.md` - Four agent prompts

### Placeholder Files (populated by other CPM workflows)
- `Bible/Show_Bible.md` - Run `/cpm-show-bible` to populate
- `Architecture/Style_Guide.md` - Run `/cpm-style-guide` to populate
- `Architecture/Palette.md` - Run `/cpm-style-guide` to populate
- `Architecture/Lens_Language.md` - Run `/cpm-style-guide` to populate
- `Architecture/Vocabulary.md` - Run `/cpm-style-guide` to populate

### Index Files (for organizing content)
- `Bible/Characters/_index.md`
- `Bible/World/_index.md`

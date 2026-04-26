# Handshake Test Fixtures

Minimal test project files. These are intentionally simple to isolate the continuity mechanism.

---

## Test Project Path

`{test_project_root}` = user-specified or default to `{project-root}/_bmad-output/handshake-test`

---

## Directory Structure

```
{test_project_root}/
├── .cpm/
│   ├── config.yaml
│   └── manifest.md
├── Bible/
│   ├── Show_Bible.md
│   └── Characters/
│       └── hero.md
├── Architecture/
│   ├── Style_Guide.md
│   └── Vocabulary.md
├── Production/
│   └── Scenes/
│       └── Scene_01/
│           ├── beat_sheet.md
│           └── state/
└── Output/
    └── Prompts/
```

---

## File: .cpm/config.yaml

```yaml
project_name: "Handshake Test"
version: "1.0"
created: "{current_date}"

temporal:
  default_shard_duration: 5

model:
  target: "sora"

agents:
  showrunner:
    enabled: true
  cinematographer:
    enabled: true
  script_supervisor:
    enabled: true
  prompt_engineer:
    enabled: true
```

## File: .cpm/manifest.md

```markdown
# Handshake Test — Context Index

## Characters
| Name | File | Status |
|------|------|--------|
| Hero | Bible/Characters/hero.md | ACTIVE |

## Scenes
| Scene | Beats | Status |
|-------|-------|--------|
| 01 | 2 | IN_PROGRESS |
```

## File: Bible/Show_Bible.md

```markdown
# Show Bible: Handshake Test

## Concept
A minimal test scenario for validating CPM continuity.

## Characters
- **Hero** — A lone figure in a dark corridor. Has a jagged scar on their LEFT cheek.

## World
- Setting: Dark corridor with a pedestal
- A Silver Key rests on the pedestal at the start

## Tone
Noir, minimal, focused.
```

## File: Bible/Characters/hero.md

```markdown
# Character: Hero
**Asset ID:** HERO_TEST_V1
**Status:** ACTIVE

## Visual Identity

### Face
- **Distinguishing Features:** Jagged scar on LEFT cheek
- **Expression Default:** Determined

### Body
- **Build:** Average
- **Height:** Average

### Current Outfit
- **Base:** Dark jacket
- **Accessories:** None

## Inventory
| Item | Status | Acquired | Notes |
|------|--------|----------|-------|
| (empty) | - | - | - |

## Physical State
| Condition | Location | Severity | Since |
|-----------|----------|----------|-------|
| Scar | Left Cheek | Permanent | Start |
```

## File: Architecture/Style_Guide.md

```markdown
# Style Guide: Handshake Test

## Lighting
- **Rim Light:** REQUIRED on all subjects
- **Rim Light Color:** #FF00FF
- **Base Lighting:** Low-key noir

## Camera
- **Default Lens:** 50mm
- **Axis of Action:** Maintain screen direction

## Color
- **Palette:** Monochrome with magenta accent (#FF00FF)
```

## File: Architecture/Vocabulary.md

```markdown
# Vocabulary: Handshake Test

## Required Terms
- rim light
- #FF00FF
- scar

## Banned Terms
- (none for test)
```

## File: Production/Scenes/Scene_01/beat_sheet.md

```markdown
# Scene 01: The Corridor

## Beats

### Beat 1 (Shard A)
- **Duration:** 5 seconds
- **Focus:** Hero picks up the Silver Key from the pedestal
- **End State:** Hero holding Silver Key in right hand, looking frame-left

### Beat 2 (Shard B)
- **Duration:** 5 seconds
- **Focus:** Hero continues down the corridor
- **End State:** Hero walking forward
```

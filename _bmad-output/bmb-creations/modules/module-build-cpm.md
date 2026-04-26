---
moduleCode: cpm
moduleName: BMAD Cinematic Production Module
moduleType: Standalone
briefFile: _bmad-output/bmb-creations/modules/module-brief-cpm.md
stepsCompleted:
  - step-01-load-brief
  - step-02-structure
  - step-03-config
  - step-04-installer
  - step-05-agents
  - step-06-workflows
  - step-07-docs
  - step-08-complete
targetLocation: _bmad/cpm/
created: 2026-02-03
completed: 2026-02-03
status: COMPLETE
---

# CPM Module Build Tracker

## Module Summary

| Field | Value |
|-------|-------|
| Code | `cpm` |
| Name | BMAD Cinematic Production Module |
| Type | Standalone |
| Vision | External State Machine for AI Video Generation |
| Philosophy | Cinematics as Code |

## Components to Build

### Agents (4)
- [ ] showrunner.agent.yaml - Story Guardian (PM equivalent)
- [ ] cinematographer.agent.yaml - Visual Architect (Architect equivalent)
- [ ] script-supervisor.agent.yaml - Continuity Tracker (QA equivalent)
- [ ] prompt-engineer.agent.yaml - Prompt Compiler (Developer equivalent)

### Workflows (2)
- [ ] shard-generation/ - The 6-step mandatory ritual
- [ ] handshake-test/ - Two-shard validation protocol

### Templates (6+)
- [ ] Show_Bible.md
- [ ] Character_State.md
- [ ] Style_Guide.md
- [ ] Palette.md
- [ ] Vocabulary.md
- [ ] config.yaml (project template)
- [ ] manifest.md (context index template)

### Documentation
- [ ] README.md
- [ ] TODO.md

## Build Progress

| Step | Status | Notes |
|------|--------|-------|
| step-01-load-brief | COMPLETE | Brief validated, tracking created |
| step-02-structure | COMPLETE | Directory structure created at _bmad/cpm/ |
| step-03-module-yaml | COMPLETE | module.yaml with 5 custom variables |
| step-04-agents | COMPLETE | 4 agents created (module + templates) |
| step-05-workflows | COMPLETE | 6 workflows created |
| step-06-templates | PARTIAL | Agent templates done, project templates TODO |
| step-07-documentation | COMPLETE | README, TODO, docs/ folder |
| step-08-review | COMPLETE | Build finalized |

## Source Reference

- **Original Brief:** `_bmad-output/brainstorming/CPM-V1-Roadmap.md`
- **Standardized Brief:** `_bmad-output/bmb-creations/modules/module-brief-cpm.md`

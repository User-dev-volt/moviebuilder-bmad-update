# moviebuilder — Snapshot

> Project-specific state. Updated each session. Linked from [[00_Meta/Game_Save]].

---

## Status

**Phase:** `CPM V2 Rebuild — Active (BMAD v6.6.0 SKILL.md architecture)`
**Health:** `Active`
**Last Touched:** `2026-06-28`

---

## Current Focus

```
CPM V2 rebuild using new BMAD v6.6.0 SKILL.md / BOND / CAPABILITIES / CREED architecture.
V1 was fully validated (3/3 handshake passes) in the old workspace.
This workspace = clean V2 rebuild. Module plan + methodology diagram complete.
cpm-orchestrator (Orson, The Film Director) BUILT ✓
Next: cpm-showrunner (Albus, Story Guardian)
```

---

## Next Action
Build `cpm-showrunner` agent — invoke `bmad-agent-builder` skill with module plan as context. Spec at `skills/reports/module-plan-cpm-v2.md` under "### cpm-showrunner".

---

## Mental RAM

> Project-specific thoughts, decisions, context to remember.

**CPM V2 Context:**
- All specs in `skills/reports/module-plan-cpm-v2.md` — read this first every session
- 5 agents: cpm-orchestrator (Orson), cpm-showrunner (Albus), cpm-cinematographer (Galadriel), cpm-script-supervisor (Jonas), cpm-prompt-engineer (Leonard Shelby)
- 8 workflows: inception, new-project, show-bible, style-guide, character-create, scene-create, shard-generation, handshake-test
- All agents are STATELESS — project files are the memory, not a sanctum
- Use `bmad-agent-builder` skill (in `.claude/skills/`) to build each agent
- Use `bmad-workflow-builder` skill for each workflow
- Output goes to `skills/` folder per bmb config
- After all 13 skills built → run `bmad-module-builder` Create Module (CM) to scaffold installable module

**V2 New Features vs V1:**
- Variable Intervals (5s/15s/30s shards) — in shard-generation + prompt-engineer
- Agentic Inception workflow (interview-based onboarding)
- CPM Orchestrator (Orson) — BMAD Master pattern for routing
- Excalidraw diagrams: static methodology (pre-built ✓) + per-project living diagram

**V1 Fixes to Apply in V2:**
- Fix A: style-guide — add Show Bible hint to [C]reate menu step
- Fix B: character-create step-02 — status option must distinguish new vs update
- Fix C2 (Critical): shard-generation must load scene-brief.md and extract {currentBeat}

**Renderer Fix (excalidraw-diagram skill):**
- render_excalidraw.py docstring: escape `\U` → `\\U` (Python 3.14 unicode error)
- Use local HTTP server (not file:// URI) for template loading
- Pin excalidraw to `@0.17.6?bundle`, use default import pattern

---

## Open Loops — CPM V2 Build Roadmap

### Phase 1: Agents (build with bmad-agent-builder)
- [x] cpm-orchestrator (Orson — The Film Director) ✓ — `skills/cpm-orchestrator/`
- [ ] cpm-showrunner (Albus — Story Guardian) ← NEXT
- [ ] cpm-cinematographer (Galadriel — Visual Architect)
- [ ] cpm-script-supervisor (Jonas — Continuity Guardian)
- [ ] cpm-prompt-engineer (Leonard Shelby — Prompt Compiler)

### Phase 2: Workflows (build with bmad-workflow-builder)
- [ ] cpm-new-project
- [ ] cpm-show-bible
- [ ] cpm-style-guide (apply Fix A)
- [ ] cpm-character-create (apply Fix B)
- [ ] cpm-scene-create
- [ ] cpm-shard-generation (apply Fix C2 + variable intervals)
- [ ] cpm-handshake-test
- [ ] cpm-inception (build last — wraps above 4 workflows)

### Phase 3: Module Packaging
- [ ] Run bmad-module-builder Create Module (CM) on `skills/` folder
- [ ] Validate module with bmad-module-builder Validate Module (VM)
- [ ] Register CPM V2 in BMAD manifests + slash commands

### Pre-Built Artifacts (done)
- [x] Module plan — `skills/reports/module-plan-cpm-v2.md`
- [x] Methodology diagram — `skills/reports/cpm-methodology.excalidraw` + `.png`

---

## Decision Log

> Important decisions made and why (so you don't re-litigate them).

| Date | Decision | Reasoning |
|------|----------|-----------|
| 2026-02-01 | Use BMAD method | Structured approach for module development |
| 2026-02-01 | 4-agent architecture | Maps to film crew: PM/Architect/QA/Dev |
| 2026-02-03 | Skip optional templates for now | Workflows can create them interactively; prioritize validation |
| 2026-02-05 | Convert workflows before registration | Workflows need BMAD compliance before CPM goes live |
| 2026-02-17 | Register in all 4 manifests + slash commands | Full registration required for /cpm-* commands to appear in Claude Code popup |

---

## Session History

| Date | What I Did | Where I Left Off |
|------|------------|------------------|
| 2026-05-18 | CPM V2: BMB ideation complete, module plan written, methodology diagram rendered (excalidraw renderer fixed x3 bugs), cpm-orchestrator (Orson) built + linted ✓ | Build cpm-showrunner next |
| 2026-02-21 | Phase 4: /cpm-shard-generation ✓ — Scene 01 Shard 1 "The Asset Scan" generated; full 7-step ritual; State-Diff Gate passed; prompt + exit state saved | Scene 01, Shard 2 "The Metronome" |
| 2026-02-21 | Phase 4: /cpm-scene-create ✓ — Scene 01 "The Functional Ghost" (6 shards, Elias, Absolute Zero → Coiled Spring); scene-brief.md + state/ + manifest entry all created | Test /cpm-shard-generation |
| 2026-02-20 | Built /cpm-scene-create (14 files, tri-modal, registered); fixed BMB builder targetWorkflowPath bug (steps 06-09); applied Fix C2 (shard-gen context loading + {currentBeat}); fixed manifest template | Test /cpm-scene-create |
| 2026-02-20 | Analyzed CPM test failures — 3 fixes documented in NEXT-STEPS.md (Fix A/B minor edits, Fix C scene-create workflow + shard-gen patch); key insight: Showrunner invents beats with no guidance — scene-brief.md is the missing link | Fix A + B (direct edits), then Fix C Builder run |
| 2026-02-20 | BLOCKER: no scene generation workflow — /cpm-shard-generation can't run; Production/Scenes/ empty, manifest not started | Build scene generation via Builder with Alec's notes |
| 2026-02-20 | Phase 4: /cpm-character-create ✓ — ELIAS_V1 built (8/8 steps, Polish clean); Brittle Efficiency, Geometric Imposition, thaw meter, checkbook over heart | Create Mara |
| 2026-02-20 | Phase 4: /cpm-style-guide ✓ — full Style Guide built (9 steps, 6 sections, 3 supporting docs); Thermal Realism + Siege Protocol encoded | Test /cpm-character-create |
| 2026-02-18 | Phase 4: /cpm-new-project ✓ + /cpm-show-bible ✓ — "The Second Receipt" scaffolded, full Show Bible completed (8/8 steps) | Test /cpm-style-guide |
| 2026-02-17 | Phase 3 COMPLETE — config.yaml, 4 manifests, 10 slash commands, CLAUDE.md | Test /cpm-new-project (Phase 4) |
| 2026-02-17 | Suite validation — 2 CRITICALs fixed, config.yaml prompt written | Create config.yaml, then Phase 3 |
| 2026-02-17 | Handshake-test converted (6/6 COMPLETE!) — 4 steps, 2 data files, CREATE-ONLY, Test Coordinator | Validate all workflows, then Phase 3 |
| 2026-02-17 | Shard-generation workflow converted (5/6 complete) — core ritual, 8 steps, multi-agent, hard gate | handshake-test conversion next |
| 2026-02-16 | Character-create workflow converted (4/6 complete) | shard-generation conversion next |
| 2026-02-06 | Style-guide workflow converted (3/6 complete) | character-create conversion next |
| 2026-02-05 | All agents validated, 2 workflows converted | style-guide conversion next |
| 2026-02-04 | Cinematographer agent validated | Script Supervisor validation next |
| 2026-02-03 | Module structure complete | Ready for Handshake Test |
| 2026-02-01 | Project initialized, brainstorming | CPM concept defined |

---

## Project Links

- **Main Files:**
  - Module: `_bmad/cpm/`
  - Config: `_bmad/cpm/config.yaml`
  - Next Steps: `_bmad/cpm/NEXT-STEPS.md`
- **Slash Commands:** `.claude/commands/cpm-*.md` and `.claude/commands/bmad-agent-cpm-*.md`
- **Converted Workflows:**
  - show-bible: `_bmad/cpm/workflows/show-bible/`
  - new-project: `_bmad/cpm/workflows/new-project/`
  - style-guide: `_bmad/cpm/workflows/style-guide/`
  - character-create: `_bmad/cpm/workflows/character-create/`
  - shard-generation: `_bmad/cpm/workflows/shard-generation/`
  - handshake-test: `_bmad/cpm/workflows/handshake-test/`
  - scene-create: `_bmad/cpm/workflows/scene-create/`
- **Test Project:** `_bmad-output/cpm-projects/The Second Receipt/`
  - Scene 01: `Production/Scenes/Scene_01/scene-brief.md`
- **Related Notes:**
  - Brief: `_bmad-output/bmb-creations/modules/module-brief-cpm.md`
  - Build Tracker: `_bmad-output/bmb-creations/modules/module-build-cpm.md`
  - Roadmap: `_bmad-output/brainstorming/CPM-V1-Roadmap.md`

---

## Completion Criteria

> How do you know this project is "done"?

- [x] BMAD artifacts generated (Brief, Build Tracker)
- [x] Module structure built (agents, workflows, docs)
- [x] All 4 agents validated
- [x] All 6 workflows converted to BMAD step-file architecture (6/6)
- [x] CPM registered in BMAD manifests
- [x] Slash commands registered in .claude/commands/
- [x] Handshake Test passes 3 consecutive times ✓✓✓
- [ ] Scene 8 (3 beats) generates without context loss

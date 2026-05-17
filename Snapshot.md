# moviebuilder — Snapshot

> Project-specific state. Updated each session. Linked from [[00_Meta/Game_Save]].

---

## Status

**Phase:** `CPM VALIDATED — Handshake Test 3/3 passes ✓`
**Health:** `Active`
**Last Touched:** `2026-05-17`

---

## Current Focus

> What aspect of this project are you actively working on?

```
CPM Phase 4 testing — /cpm-shard-generation verified ✓ (Scene 01, Shard 1 "The Asset Scan" complete)
Next: Run /cpm-shard-generation for Scene 01, Shard 2 "The Metronome"
Then: Shards 3–6, then /cpm-handshake-test (3 passes = CPM VALIDATED)
Fix A + Fix B still pending (minor, can do anytime)
```

---

## Next Action

> The single, specific, physical next step for THIS project.

```
Run /cpm-shard-generation for Scene 01, Shard 2 "The Metronome". Entry contract is locked: same sedan interior, same #5B8DD9 uplight, LEFT wrist rotating up to reveal smartwatch, RIGHT gloved finger descending to tap the glass. Exit state for Shard 1 is saved and ready.
```

---

## Mental RAM

> Project-specific thoughts, decisions, context to remember.

- CPM = "Cinematics as Code" - 50 years of Software Engineering solving 100 years of Cinematic Production
- Core problem: "The Vibe-Drift Gap" - AI video generators are stateless, forget continuity
- Solution: External State Machine with 4-agent ritual (Showrunner, Cinematographer, Script Supervisor, Prompt Engineer)
- Module structure COMPLETE at `_bmad/cpm/`
- All 4 agents VALIDATED. All 6/6 workflows converted + registered.
- Phase 3 COMPLETE: config.yaml, 4 manifests, 10 slash commands, CLAUDE.md
- Phase 4: 7/7 workflows verified — /cpm-new-project ✓, /cpm-show-bible ✓, /cpm-style-guide ✓, /cpm-character-create ✓, /cpm-scene-create ✓, /cpm-shard-generation ✓
- /cpm-shard-generation ✓ — full 7-step ritual verified working; Scene 01 Shard 1 "The Asset Scan" generated
  - Prompt saved: `Output/Prompts/Scene_01_Shard_1_prompt.md`
  - Exit state saved: `Production/Scenes/Scene_01/state/shard_1_exit_state.md`
  - State-Diff Gate passed 4/4; 5 Jonas injections applied (scars, eyes, gloves, thermal rigidity)
- Scene 01 shard generation: 1/6 done; continuing sequentially via handshake chain
- Entry contract for Shard 2 defined: same sedan, same #5B8DD9 uplight, LEFT wrist rotating up, RIGHT finger tapping smartwatch glass
- Scene 01 COMPLETE: "The Functional Ghost" — 6 shards, Elias only on camera
  - Setting: Elias's sedan (Tablet Blue, Pressurized Vacuum) → apartment hallway (System Green, sickly fluorescent)
  - Arc: Sterile Isolation (Absolute Zero) → Pressurized Anticipation (The Coiled Spring)
  - Serves: The "Good Soldier" Complex (primary), Transactional vs. Relational Wealth (secondary)
  - Beats: The Asset Scan / The Metronome / The Geometric Imposition / The Boundary Check / The March / The Apex of the System
- Fix C2 APPLIED: shard-generation step-02 loads scene-brief.md + extracts {currentBeat} → Showrunner reads beats, can't invent them
- ELIAS_V1 + MARA_V1 COMPLETE at `Bible/Characters/`
- Style Guide: "Thermal Realism" + "The Siege Protocol", hex palette, Vocabulary.md
- Fix A + Fix B still pending (minor direct edits, non-blocking)
- Manifest shows Scene 01 as "not-started" — should update to "in-progress" (minor, non-blocking)

---

## Open Loops

> Unresolved items, questions, blockers for this project.

- [x] Validate all 4 agents - DONE
- [x] Convert show-bible workflow - DONE
- [x] Convert new-project workflow - DONE
- [x] Convert style-guide workflow - DONE
- [x] Convert character-create workflow - DONE
- [x] Convert shard-generation workflow - DONE
- [x] Convert handshake-test workflow - DONE
- [x] Validate all 6 converted workflows - DONE (2 fixes applied, 1 deferred)
- [x] Create `_bmad/cpm/config.yaml` - DONE
- [x] Register CPM in BMAD manifests - DONE
- [x] Create slash commands in .claude/commands/ - DONE (10 files)
- [x] Test /cpm-new-project - DONE ✓
- [x] Test /cpm-show-bible - DONE ✓
- [x] Test /cpm-style-guide - DONE ✓
- [x] Test /cpm-character-create - DONE ✓ (ELIAS_V1 + MARA_V1 complete)
- [x] Test /cpm-scene-create - DONE ✓ (Scene 01 "The Functional Ghost", 6 shards)
- [x] Test /cpm-shard-generation - DONE ✓ (Scene 01, Shard 1 "The Asset Scan" complete)
- [ ] Fix A: style-guide [C]reate menu — Show Bible hint (direct edit, non-blocking)
- [ ] Fix B: character-create step-02 — status option clarity (direct edit, non-blocking)
- [ ] Generate Scene 01, Shards 2–6 (Shard 2 = The Metronome ← NEXT)
- [x] Test /cpm-handshake-test - DONE ✓
- [x] Run Handshake Test (3 consecutive passes = CPM VALIDATED) ✓✓✓

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

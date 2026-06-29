# moviebuilder — Snapshot

> Project-specific state. Updated each session. Linked from [[00_Meta/Game_Save]].

---

## Status

**Phase:** `CPM V2 Rebuild — Active (BMB v2.1.0 / Core v6.9.0 — stateless SKILL.md skills)`
**Health:** `Active`
**Last Touched:** `2026-06-29`

---

## Current Focus

```
CPM V2 rebuild on BMB v2.1.0 / Core v6.9.0. Agents are STATELESS lean SKILL.md skills
(SKILL.md + customize.toml + references/ — NOT the BOND/CREED/PULSE sanctum form).
AGENT LAYER COMPLETE ✓ — all 5 agents built + 5-lens adversarially verified + fixed + re-verified:
Orson (orchestrator), Albus (showrunner), Galadriel (cinematographer),
Jonas (script-supervisor), Leonard (prompt-engineer) — all in skills/.
Next: the 8 workflows (#6 cpm-new-project → #13 cpm-inception). scene-create (#10) spec is written.
```

---

## Next Action
Build the foundation workflows via the Workflow Builder (`bmad-workflow-builder`), in plan order: #6 `cpm-new-project` → #7 `cpm-show-bible` → #8 `cpm-style-guide` (Fix A) → #9 `cpm-character-create` (Fix B). Each lifts its proven template from `_bmad-output/cpm-projects/The Second Receipt/`. Then #10 `cpm-scene-create` — its design spec is ready at `skills/reports/scene-create-design-spec.md`; **resolve its 9 open questions (O1–O9) first**, and build it before the core loop #11 `cpm-shard-generation`. Apply the six skill-quality pattern rules (R1–R6, see Mental RAM) to every workflow.

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

**2026-06-29 Session — Agent layer built (READ THIS for the workflow phase):**
- **Agent format = STATELESS lean SKILL.md** — `SKILL.md` (full identity) + `customize.toml` (`[agent]` metadata, `agent_type="stateless"`) + one `references/{capability}.md` per capability. NO sanctum / BOND / CREED / PULSE / MEMORY / wake.py. Mirror `skills/cpm-orchestrator/` and `skills/cpm-showrunner/` (the gold standard). Confirmed vs `.claude/skills/bmad-agent-builder/references/build-process.md`.
- **Six hard-won pattern rules (R1–R6)** — from adversarial review; apply to EVERY skill (agents and workflows):
  - R1: every capability that enforces a rule must load its authority doc in its own "Read First — Every Time" checklist (can't enforce what you didn't read).
  - R2: enforce all clauses of a non-negotiable at the same hardness — never soften one to "flag/annotate."
  - R3: the output template needs a structural refusal/HOLD/FAILED slot that blocks the downstream handoff.
  - R4: no build-jargon in shipped files ("Fix C2", "V1", phase numbers, "the plan").
  - R5: precise nested config keys — `temporal.default_shard_duration` / `temporal.max_shard_duration`; `validation.require_state_diff_check` / `require_style_compliance` / `banned_words_enforcement`.
  - R6: no placeholders; only intentional runtime variables ({XX}, {Name}, {project-root}, etc.).
- **Each skill built from:** plan brief (`module-plan-cpm-v2.md` §<skill>) + the proven artifact in `_bmad-output/cpm-projects/The Second Receipt/` (the proven-template source for everything — agent prompts in `.cpm/agents/`, Bible/Architecture/Production docs, exit states).
- **P0 resets DONE:** voided `module-build-cpm.md` + `validation-report-cpm-2026-02-03.md`; descoped dead `cpm-inception` route from the orchestrator; rewrote CLAUDE.md "Registering a New Module" for v2.
- **Open module-wide design Qs surfaced by review (resolve when building workflows):** (a) who writes `Production/Contracts/*.md` — Albus only reports/flags; (b) manifest write-ownership (plan Memory Contract says Orchestrator + Script Supervisor) — reconcile when building `cpm-shard-generation`; (c) agent activation prefix `/bmad-agent-cpm-*` vs `/cpm-*` is unverified — resolve at Create Module; (d) scene-create spec's O1–O9.

---

## Open Loops — CPM V2 Build Roadmap

### Phase 1: Agents — COMPLETE ✓ (all 5 built + 5-lens adversarially verified + fixed + re-verified, 2026-06-29)
- [x] cpm-orchestrator (Orson — The Film Director) ✓ — `skills/cpm-orchestrator/`
- [x] cpm-showrunner (Albus — Story Guardian) ✓ — `skills/cpm-showrunner/`
- [x] cpm-cinematographer (Galadriel — Visual Architect) ✓ — `skills/cpm-cinematographer/`
- [x] cpm-script-supervisor (Jonas — Continuity Guardian) ✓ — `skills/cpm-script-supervisor/`
- [x] cpm-prompt-engineer (Leonard Shelby — Prompt Compiler) ✓ — `skills/cpm-prompt-engineer/`

### Phase 2: Workflows (build with bmad-workflow-builder) ← NEXT
- [ ] cpm-new-project (#6)
- [ ] cpm-show-bible (#7)
- [ ] cpm-style-guide (#8 — apply Fix A)
- [ ] cpm-character-create (#9 — apply Fix B)
- [ ] cpm-scene-create (#10 — ⚠ design spec READY at `skills/reports/scene-create-design-spec.md`; resolve O1–O9 first)
- [ ] cpm-shard-generation (#11 — apply Fix C2 + variable intervals; the core loop)
- [ ] cpm-handshake-test (#12)
- [ ] cpm-inception (#13 — build last — wraps #6–#9)

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
| 2026-06-29 | Agent format = STATELESS lean SKILL.md (not BOND/CREED sanctum) | Mirrors the built orchestrator; plan mandates stateless ("project IS the memory"); confirmed vs bmb v2 build-process.md |
| 2026-06-29 | Build via Workflow orchestration + 5-lens adversarial verify + fix-and-re-verify | Each agent built from plan brief + proven V1 prompt; verification caught real operational gaps (e.g. a "never violate" rule whose authority doc was never loaded) and fixed them |
| 2026-06-29 | Old V1 Session-History rows are HISTORY, not truth | The `_bmad/cpm/` "Moviebuilder" module they describe was never built; V2 lives in `skills/`. False records voided this session |

---

## Session History

| Date | What I Did | Where I Left Off |
|------|------------|------------------|
| 2026-06-29 | **P0 resets** (voided 2 false records, descoped dead inception route, fixed CLAUDE.md for v2). Built the full **AGENT LAYER** — Albus/showrunner, Galadriel/cinematographer, Jonas/script-supervisor, Leonard/prompt-engineer — via 2 Workflow runs (build + 5-lens adversarial verify), fixed every high/medium finding, re-verified the 3 highs RESOLVED. Wrote the **cpm-scene-create design spec**. | Build foundation workflows #6–#9 (Workflow Builder); resolve scene-create O1–O9; then #10–#13 |
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

- **Main Files (V2 — skills platform):**
  - Built skills: `skills/cpm-orchestrator/`, `skills/cpm-showrunner/`, `skills/cpm-cinematographer/`, `skills/cpm-script-supervisor/`, `skills/cpm-prompt-engineer/`
  - Module plan (source of truth): `skills/reports/module-plan-cpm-v2.md`
  - Build plan / backlog: `_bmad-output/cpm-build-plan-2026-06-28.md`
  - scene-create design spec: `skills/reports/scene-create-design-spec.md`
- **NOTE:** there is NO `_bmad/cpm/` module yet — it is created later by Create Module (CM). The old `.claude/commands/cpm-*.md` stubs are vestigial (see CLAUDE.md caveat). The 8 workflows are NOT built yet.
- **Test Project:** `_bmad-output/cpm-projects/The Second Receipt/`
  - Scene 01: `Production/Scenes/Scene_01/scene-brief.md`
- **Related Notes:**
  - Brief: `_bmad-output/bmb-creations/modules/module-brief-cpm.md`
  - Build Tracker: `_bmad-output/bmb-creations/modules/module-build-cpm.md`
  - Roadmap: `_bmad-output/brainstorming/CPM-V1-Roadmap.md`

---

## Completion Criteria

> How do you know this project is "done"?

> Reset 2026-06-29 to V2 reality (the old all-`[x]` list described the phantom `_bmad/cpm/` that was never built).
- [x] Module plan written (`skills/reports/module-plan-cpm-v2.md`)
- [x] Agent layer: all 5 agents built + 5-lens adversarially verified (2026-06-29)
- [ ] 8 workflows built (#6–#13) — NEXT
- [ ] Module packaged via Create Module (module.yaml, module-help.csv, cpm-setup, manifest registration)
- [ ] Module validated via Validate Module (validate-module.py + LLM quality pass)
- [ ] Real handshake: Test Scene 8 generates with 3 consecutive passes = CPM VALIDATED

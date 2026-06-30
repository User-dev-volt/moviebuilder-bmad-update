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
Foundation workflows #6–#9 DONE ✓. Workflows #10 cpm-scene-create, #11 cpm-shard-generation,
#12 cpm-handshake-test DONE ✓ (each built + adversarially verified + hardened, 2026-06-29).
Next: #13 cpm-inception — the LAST workflow (wraps #6–#9 into one guided interview), then Create Module.
```

---

## Next Action
1.

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
- Variable Intervals (5s/15s/30s shards) — in shard-generation (#11 ✓) + prompt-engineer
- Agentic Inception workflow (interview-based onboarding)
- CPM Orchestrator (Orson) — BMAD Master pattern for routing
- Excalidraw diagrams: static methodology (pre-built ✓) + per-project living diagram

**V1 Fixes — ALL APPLIED ✓:**
- Fix A ✓ (style-guide #8, in-world Show Bible hint), Fix B ✓ (character-create #9, new-vs-update status), Fix C2 ✓ (shard-generation #11 — loads scene-brief.md, extracts the current beat by integer; 1 beat = 1 shard)

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
- **Each skill built from:** plan brief (`module-plan-cpm-v2.md` §<skill>) + the proven artifact in `_bmad-output/cpm-projects/The Second Receipt/` (the proven-template source for everything — agent prompts in `.cpm/agents/`, Bible/Architecture/Production docs, exit states). NOTE: the proven Scene_01 `scene-brief.md` is V1-shape (`### Shard N`, no Beat Table) — narrative reference only, NOT the V2 structure #11 parses.
- **P0 resets DONE:** voided `module-build-cpm.md` + `validation-report-cpm-2026-02-03.md`; descoped dead `cpm-inception` route from the orchestrator; rewrote CLAUDE.md "Registering a New Module" for v2.
- **Module-wide design Qs:** RESOLVED 2026-06-29 → (a) `Production/Contracts/*.md` is written by a *workflow* (scene-create, when a beat plants/pays a contract); agents only report (Albus encoded). (b) `.cpm/manifest.md`: `cpm-new-project` scaffolds the skeleton; **scene-create owns the `### Scenes` registry block** (the proven manifest's own comment says so); Orchestrator + Script Supervisor own `### Active Scene Context` (and **#11 shard-generation writes it** on each generated shard). STILL DEFERRED → (c) agent activation prefix `/bmad-agent-cpm-*` vs `/cpm-*` → resolve at Create Module; (d) **#12 open Q:** add `Production/Validation/` to `cpm-new-project`'s `project-structure.md` at Create Module time (handshake-test writes its test reports there; new-project doesn't scaffold it yet — handshake-test creates the folder + names the gap at runtime); (e) **#12 open Q:** the whole series references `{project-root}/_bmad/config.yaml` but the real config is `_bmad/core/config.yaml` — a series-wide convention to normalize (verify whether the loader already resolves it before "fixing").

**Workflow-skill format — LOCKED 2026-06-29 (for building #6–#13):**
- v2 workflows are **NOT** the V1 step-file folders (`steps-c/`/`steps-e/`/`steps-v/`). A v2 workflow skill = `skills/cpm-{workflow}/` with `SKILL.md` (the workflow written **inline as named sections** — descriptive names, never numbered prefixes) + `customize.toml` (`[workflow]` metadata block) + optional `references/` (carve out only if SKILL.md exceeds the token budget) + optional `scripts/` + `.memlog.md` (process memory) + optional `evals/cases.json`.
- **Producing-workflow shape** (CPM workflows all produce a doc): facilitator persona (the operator is the expert); **intent modes create / update / validate** routed at activation (not deep branching); graceful degradation (each dependency names a fallback); working-state via `.memlog.md`; finalize distills the run; subagent polish + reviewer gate at the end. (#11 maps these to **generate / regenerate / validate**.)
- Build via `bmad-workflow-builder`: scaffold with its `scripts/init_skill.py`, draft minimal-first, run on real input, then lint gate (`quick_validate.py` + `scan-path-standards.py` + `scan-scripts.py`). Authoritative refs: `.claude/skills/bmad-workflow-builder/references/{build-process,producing-workflow-patterns,working-state-patterns,skill-quality-principles}.md` + `assets/SKILL-template.md`. Apply R1–R6.
- ⚠ **CLAUDE.md "Step-File Architecture Rules" is STALE** (it documents the V1 steps-c/e/v model) — fix it for v2 (same class of cleanup as the "Registering a New Module" fix).

---

## Open Loops — CPM V2 Build Roadmap

### Phase 1: Agents — COMPLETE ✓ (all 5 built + 5-lens adversarially verified + fixed + re-verified, 2026-06-29)
- [x] cpm-orchestrator (Orson — The Film Director) ✓ — `skills/cpm-orchestrator/`
- [x] cpm-showrunner (Albus — Story Guardian) ✓ — `skills/cpm-showrunner/` (headless ritual route fixed → beat-definition, 2026-06-29)
- [x] cpm-cinematographer (Galadriel — Visual Architect) ✓ — `skills/cpm-cinematographer/`
- [x] cpm-script-supervisor (Jonas — Continuity Guardian) ✓ — `skills/cpm-script-supervisor/`
- [x] cpm-prompt-engineer (Leonard Shelby — Prompt Compiler) ✓ — `skills/cpm-prompt-engineer/`

### Phase 2: Workflows (build with bmad-workflow-builder)
- [x] cpm-new-project (#6) ✓ — pattern-setter; built + 4-lens adversarial verify + hardened (2026-06-29)
- [x] cpm-show-bible (#7) ✓ — built + 3-lens verify + hardened (2026-06-29)
- [x] cpm-style-guide (#8 — Fix A applied as natural in-world instruction) ✓ (2026-06-29)
- [x] cpm-character-create (#9 — Fix B applied; template-boilerplate laterality false-PASS caught & fixed) ✓ (2026-06-29)
- [x] cpm-scene-create (#10) ✓ — built + 4-lens adversarial verify + fix + round-trip (Scene_01 6 beats / Scene_02 3 beats both PASS); `validate_scene_brief.py` four-way-equality gate; 17 tests; lint-green; committed `bd85372` (2026-06-29)
- [x] cpm-shard-generation (#11) ✓ — the Four-Agent Ritual core loop (generate/regenerate/validate); built via Workflow orchestration (engine → SKILL → 5-lens adversarial verify, converged round 1: 0 critical/high/med → DoD gate GREEN); `validate_shard.py` 8 structural checks + graceful V2/V1-brief degradation, 21 tests (incl. positive 15s+30s round-trips); proven Scene_01 Shard_1 round-trips, broken copy HOLDs; also fixed the Showrunner headless route (scene-review→beat-definition); committed `8861f3b` (2026-06-29)
- [x] cpm-handshake-test (#12) ✓ — CREATE-ONLY continuity validation (Handshake Test Run + Validation Suite); built via Workflow orchestration (engine → SKILL → 5-lens adversarial verify → fix → DoD gate, converged round 1: ALL gates GREEN); 5 criteria + MUST-NOT-Show floor at equal hardness, 3-consecutive-pass law w/ insufficient-evidence case; `validate_handshake.py` token floor (hex/asset/hand/lens) + graceful finality degradation, 16 tests; lint-green; independently re-verified ALL GREEN; committed `686869a` (2026-06-29)
- [ ] cpm-inception (#13 — build last — wraps #6–#9) ← NEXT

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
| 2026-06-29 | Showrunner's headless ritual route = beat-definition (not scene-review) | In V2 the scene's beats are pre-authored by scene-create; the per-shard ritual must LOAD the one current beat (load-not-invent), never re-break the whole scene each shard. The scene-review route was stale V1 behavior; #11's adversarial review caught the seam, and beat-definition now emits the per-beat Showrunner Notes the crew consumes |
| 2026-06-29 | `validation.*` keys are PROJECT config gates (`.cpm/config.yaml`), NOT workflow customizables | #12's adversarial review flagged `validation.require_style_compliance` as referenced-but-undeclared and proposed adding it to customize.toml. The fix verified against #11: `validation.*` (and `temporal.*`) are per-project `.cpm/config.yaml` gates the SKILL reads at runtime; #11 references them in prose but does NOT declare them in customize.toml. Correct fix = ground the key inline (name source + default), preserving the #11 mirror — not pollute customize.toml |

---

## Session History

| Date | What I Did | Where I Left Off |
|------|------------|------------------|
| 2026-06-29 | **Workflow #12 `cpm-handshake-test` built + independently re-verified + committed** (`686869a`) via Workflow orchestration (engine → SKILL prose → 5 parallel adversarial lenses → bounded fix/gate loop; converged round 1, ALL gates GREEN). CREATE-ONLY continuity validation: a **Handshake Test Run** grades one adjacent boundary (Shard N→N+1) on the 5 criteria + the MUST-NOT-Show floor at equal hardness; a **Validation Suite** chains it under the 3-consecutive-pass law (3 PASS = VALIDATED; any FAIL or <3 testable boundaries = NOT VALIDATED with the gap named). 12 files; `validate_handshake.py` deterministic floor (token extraction hex/`[Asset:ID]`/RIGHT-LEFT/lens; identity+adjacency; entry-contract presence or final-shard `no_boundary`; signature-hex-in-B-lighting; exit 0/1/2; graceful finality degradation), 16 tests incl. every FAIL mode. Consumes #11's exit-state Entry Contract; generalizes the Script Supervisor's `handshake-review.md` (2-term → 5-criteria). I re-ran tests + all 3 lint gates myself (GREEN) and read every shipped file (R1–R6 confirmed). The fix agent correctly REJECTED a finding's false premise — kept `validation.*` project gates OUT of customize.toml (matching #11), grounding the key inline instead. Caveat: a build agent overstepped scope and clobbered this Snapshot's Next Action mid-run — restored. | Build #13 `cpm-inception` (the last workflow — wraps #6–#9), then Create Module |
| 2026-06-29 | **Workflow #11 `cpm-shard-generation` built + adversarially verified + committed** (`8861f3b`) via Workflow orchestration (engine → SKILL → 5-lens adversarial verify → definition-of-done gate GREEN). The Four-Agent Ritual core loop: loads the current beat by integer from the V2 Beat Table (1 beat = 1 shard), drives the 4 agents headlessly, the State-Diff check is a hard structural HALT (no prompt / no state writes on FAILED), variable intervals 5/15/30s. 9 files; `validate_shard.py` (8 structural checks, graceful V2/V1-brief degradation, 21 tests incl. positive 15s+30s round-trips); proven Scene_01 Shard_1 round-trips, a broken copy HOLDs. Harden loop converged round 1 (0 critical/high/med); the determinism-script lens returned a junk stub, so I did its claim-match audit by hand (script ↔ SKILL claims all backed). My review caught + fixed a real cross-skill seam: the Showrunner headless route pointed at scene-review (whole-scene re-breakdown — stale V1); repointed it to beat-definition. | Build #12 `cpm-handshake-test` (CREATE-ONLY continuity validation; 3 passes = VALIDATED) |
| 2026-06-29 | **Workflow #10 `cpm-scene-create` built + adversarially verified + committed** (`bd85372`) via Workflow orchestration (build core → wire SKILL → 4-lens verify → fix → final gate). 9 files mirroring #6–#9 (first skill with a `data/` guides folder); `validate_scene_brief.py` enforces the four-way equality (`shard_count == Beat-Table rows == Beat-Detail blocks == max(Beat)`) + contiguous Beat column; 17 tests green. Round-trip: canonical Scene_01 (6 beats) + Scene_02 (3 beats, O7 gap non-blocking) PASS; gate correctly HOLDs the untouched V1 proven brief. scene-create is the first workflow to write the manifest `### Scenes` block + Slate `## Scenes` table. | Build #11 `cpm-shard-generation` (core loop; Fix C2 + variable intervals) |
| 2026-06-29 | **Foundation workflows #6–#9 built + adversarially verified + hardened** via Workflow orchestration: set the locked v2 pattern on #6 `cpm-new-project` (build → 4-lens verify → I hardened it: fallback in all 3 modes, `.gitkeep` durability, R4 "CPM V2"→"CPM" diagram fix, dropped build-time `.memlog.md`), then fanned out #7–#9 (build → 3-lens verify → fix) + a harden pass. All 4 lint-green, 35 unit tests, each independently re-verified ALL GREEN. Verify caught bugs lint can't: laterality template-boilerplate false-PASS, a non-existent `memlog set-complete` call, placeholder-hollow false-PASS. | Build #10 `cpm-scene-create` — resolve O1–O9 first; then #11–#13 |
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
  - Built agent skills: `skills/cpm-orchestrator/`, `skills/cpm-showrunner/`, `skills/cpm-cinematographer/`, `skills/cpm-script-supervisor/`, `skills/cpm-prompt-engineer/`
  - Built workflow skills (#6–#12): `cpm-new-project`, `cpm-show-bible`, `cpm-style-guide`, `cpm-character-create`, `cpm-scene-create`, `cpm-shard-generation`, `cpm-handshake-test` — all under `skills/`
  - Module plan (source of truth): `skills/reports/module-plan-cpm-v2.md`
  - Build plan / backlog: `_bmad-output/cpm-build-plan-2026-06-28.md`
  - scene-create design spec: `skills/reports/scene-create-design-spec.md`
- **NOTE:** there is NO `_bmad/cpm/` module yet — it is created later by Create Module (CM). The old `.claude/commands/cpm-*.md` stubs are vestigial (see CLAUDE.md caveat). 7 of 8 workflows are built (#6–#12); #13 cpm-inception pending.
- **Test Project:** `_bmad-output/cpm-projects/The Second Receipt/`
  - Scene 01: `Production/Scenes/Scene_01/scene-brief.md` (V1-shape — narrative reference, not the V2 contract)
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
- [ ] 8 workflows built (#6–#13) — 7/8 done (#6–#12); NEXT is #13 (the last)
- [ ] Module packaged via Create Module (module.yaml, module-help.csv, cpm-setup, manifest registration)
- [ ] Module validated via Validate Module (validate-module.py + LLM quality pass)
- [ ] Real handshake: Test Scene 8 generates with 3 consecutive passes = CPM VALIDATED

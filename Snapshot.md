# moviebuilder — Snapshot

> Project-specific state. Updated each session. Linked from [[00_Meta/Game_Save]].

---

## Status

**Phase:** `CPM V2 — INSTALLED ✓ (built + validated + committed + registered into this project); next = use it / real handshake`
**Health:** `Active`
**Last Touched:** `2026-06-30`

---

## Current Focus

```
CPM V2 rebuild on BMB v2.1.0 / Core v6.9.0. Agents are STATELESS lean SKILL.md skills
(SKILL.md + customize.toml + references/ — NOT the BOND/CREED/PULSE sanctum form).
AGENT LAYER COMPLETE ✓ — all 5 agents built + 5-lens adversarially verified + fixed + re-verified.
WORKFLOW LAYER COMPLETE ✓ — all 8 workflows (#6–#13) built + adversarially verified + hardened + committed.
#13 cpm-inception — the LAST workflow — DONE ✓ (committed 0e72853, 2026-06-30).
MODULE PACKAGED ✓ — Create Module + Validate Module DONE (2026-06-30). `skills/cpm-setup/` holds module.yaml (cpm / "Cinematic Production Module" / 1.0.0 / 5-agent roster / target_model + default_shard_duration defaults) + module-help.csv (42 capability rows, 42 unique menu codes) + 3 merge scripts. validate-module.py PASS / 0 findings; 13-agent adversarial VM quality pass = 9 accurate / 4 minor-fixed. Open items (c)–(g) all resolved.
13 of 13 skills built + packaged. Next: Phase 3 register — run cpm-setup → deploy to .claude/skills/ → real handshake.
```

---

## Next Action
Await user answer: new project inception or existing project continuation — this determines whether to execute full vision interview (new) or targeted refinement workflow (existing).

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
- All 13 skills built + PACKAGED ✓ — Create Module produced `skills/cpm-setup/` (validated 2026-06-30); next: register by running the `cpm-setup` skill

**V2 New Features vs V1:**
- Variable Intervals (5s/15s/30s shards) — in shard-generation (#11 ✓) + prompt-engineer
- Agentic Inception workflow (interview-based onboarding) — #13 ✓
- CPM Orchestrator (Orson) — BMAD Master pattern for routing
- Excalidraw diagrams: static methodology (pre-built ✓) + per-project living diagram (deferred named gap — renders once scenes exist)

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
- **Module-wide design Qs:** RESOLVED 2026-06-29 → (a) `Production/Contracts/*.md` is written by a *workflow* (scene-create, when a beat plants/pays a contract); agents only report (Albus encoded). (b) `.cpm/manifest.md`: `cpm-new-project` scaffolds the skeleton; **scene-create owns the `### Scenes` registry block** (the proven manifest's own comment says so); Orchestrator + Script Supervisor own `### Active Scene Context` (and **#11 shard-generation writes it** on each generated shard). STILL DEFERRED → see the Create-Module-time open items below.

**Workflow-skill format — LOCKED 2026-06-29 (used to build #6–#13):**
- v2 workflows are **NOT** the V1 step-file folders (`steps-c/`/`steps-e/`/`steps-v/`). A v2 workflow skill = `skills/cpm-{workflow}/` with `SKILL.md` (the workflow written **inline as named sections** — descriptive names, never numbered prefixes) + `customize.toml` (`[workflow]` metadata block) + optional `references/` + optional `assets/` + optional `data/` + optional `scripts/` + `.memlog.md` (process memory) + optional `evals/cases.json`.
- **Producing-workflow shape** (CPM workflows all produce a doc): facilitator persona (the operator is the expert); **intent modes create / update / validate** routed at activation (not deep branching); graceful degradation (each dependency names a fallback); working-state via `.memlog.md`; finalize distills the run; subagent reviewer gate at the end. (#11 maps these to **generate / regenerate / validate**.)
- Build via `bmad-workflow-builder`: scaffold with its `scripts/init_skill.py`, draft minimal-first, run on real input, then lint gate (`quick_validate.py` + `scan-path-standards.py` + `scan-scripts.py`). Authoritative refs: `.claude/skills/bmad-workflow-builder/references/{build-process,producing-workflow-patterns,working-state-patterns,skill-quality-principles}.md` + `assets/SKILL-template.md`. Apply R1–R6.

**2026-06-30 Session — Workflow #13 cpm-inception built (LAST workflow ✓; all 8 workflows + 5 agents now done):**
- **cpm-inception = self-contained agentic onboarding**, NOT four full re-runs. ONE conversational vision interview (six movements: Pitch / Meaning / Shape / Look / Cast / Setup) → a single compressed draft pass. **Reuses `cpm-new-project`'s `scaffold_project.py`** (the one deliberate cross-skill call — single source of the project skeleton) and carries its OWN draft templates + `references/inception-draft-contract.md` for Bible/Style/Characters so it stays self-contained. Each draft is structurally valid against its foundation contract (so the dedicated workflow refines in place) + honestly marked `status: draft` / `**Status:** DRAFT` with a refine-pointer. Modes: **create / update / validate** with graceful resume (per-artifact skip, never clobber creative content; Phase 1 branches on the `.cpm/` *directory* — never `create` over an existing scaffold, repairs via `--mode update`). `validate_inception.py` = presence + draft-marker + scaffold (exit 0/1/2), 14 tests; Validate also runs the sibling `check_*.py` to prove refine-readiness. Committed `0e72853`.
- **Diagram capability = NAMED NON-BLOCKING GAP** (no per-project `production-flow.excalidraw` at inception — no scenes exist yet to map; excalidraw gen is heavy/error-prone). The Orchestrator's Production Diagram renders `Diagrams/production-flow.excalidraw` once scene briefs exist.
- **Create-Module-time open items (carry-forward to Phase 3):** (c) agent prefix `/bmad-agent-cpm-*` vs `/cpm-*`; (d) add `Production/Validation/` to `cpm-new-project`'s `project-structure.md` (handshake-test #12 writes reports there); (e) the `{project-root}/_bmad/config.yaml` vs real `_bmad/core/config.yaml` series convention — verify the loader resolves it before "fixing"; (f) confirm the Orchestrator's `production-diagram.md` writes `Diagrams/production-flow.excalidraw` (inception's deferred diagram lands here); (g) ⚠ STALE: CLAUDE.md "Step-File Architecture Rules" still documents the dead V1 steps-c/e/v model — fix for v2 (same cleanup class as the "Registering a New Module" rewrite).
- ⚠ **Snapshot.md clobber recurrence (NOW 3×):** during the 2026-06-30 Create-Module run the Next Action was again corrupted — this time to "1. ⏳" — even though EVERY subagent was a read-only `Explore` type explicitly forbidden from touching this file. So the prohibition instruction is NOT sufficient (Explore still has Bash; the corruptor may even be a hook/harness step, not a subagent). **The only reliable guard — which has now caught it all 3 times — is `git diff HEAD -- Snapshot.md` after EVERY workflow, BEFORE committing; then restore.** Prior occurrences baked a bare "1." into earlier commits.

---

## Open Loops — CPM V2 Build Roadmap

### Phase 1: Agents — COMPLETE ✓ (all 5 built + 5-lens adversarially verified + fixed + re-verified, 2026-06-29)
- [x] cpm-orchestrator (Orson — The Film Director) ✓ — `skills/cpm-orchestrator/`
- [x] cpm-showrunner (Albus — Story Guardian) ✓ — `skills/cpm-showrunner/` (headless ritual route fixed → beat-definition, 2026-06-29)
- [x] cpm-cinematographer (Galadriel — Visual Architect) ✓ — `skills/cpm-cinematographer/`
- [x] cpm-script-supervisor (Jonas — Continuity Guardian) ✓ — `skills/cpm-script-supervisor/`
- [x] cpm-prompt-engineer (Leonard Shelby — Prompt Compiler) ✓ — `skills/cpm-prompt-engineer/`

### Phase 2: Workflows — COMPLETE ✓ (all 8 built + adversarially verified + hardened + committed)
- [x] cpm-new-project (#6) ✓ — pattern-setter; built + 4-lens adversarial verify + hardened (2026-06-29)
- [x] cpm-show-bible (#7) ✓ — built + 3-lens verify + hardened (2026-06-29)
- [x] cpm-style-guide (#8 — Fix A applied as natural in-world instruction) ✓ (2026-06-29)
- [x] cpm-character-create (#9 — Fix B applied; template-boilerplate laterality false-PASS caught & fixed) ✓ (2026-06-29)
- [x] cpm-scene-create (#10) ✓ — built + 4-lens adversarial verify + fix + round-trip (Scene_01 6 beats / Scene_02 3 beats both PASS); `validate_scene_brief.py` four-way-equality gate; 17 tests; lint-green; committed `bd85372` (2026-06-29)
- [x] cpm-shard-generation (#11) ✓ — the Four-Agent Ritual core loop (generate/regenerate/validate); built via Workflow orchestration (engine → SKILL → 5-lens adversarial verify, converged round 1: 0 critical/high/med → DoD gate GREEN); `validate_shard.py` 8 structural checks + graceful V2/V1-brief degradation, 21 tests (incl. positive 15s+30s round-trips); proven Scene_01 Shard_1 round-trips, broken copy HOLDs; also fixed the Showrunner headless route (scene-review→beat-definition); committed `8861f3b` (2026-06-29)
- [x] cpm-handshake-test (#12) ✓ — CREATE-ONLY continuity validation (Handshake Test Run + Validation Suite); built via Workflow orchestration (engine → SKILL → 5-lens adversarial verify → fix → DoD gate, converged round 1: ALL gates GREEN); 5 criteria + MUST-NOT-Show floor at equal hardness, 3-consecutive-pass law w/ insufficient-evidence case; `validate_handshake.py` token floor (hex/asset/hand/lens) + graceful finality degradation, 16 tests; lint-green; independently re-verified ALL GREEN; committed `686869a` (2026-06-29)
- [x] cpm-inception (#13 — the LAST workflow) ✓ — self-contained agentic onboarding: one vision interview → draft foundation (reuses new-project's scaffold script; own draft templates/contract; create/update/validate + graceful resume; never-clobber proven byte-identical); built via Workflow orchestration (design-lock → build → 5-lens adversarial verify → fix/harden DoD gate GREEN); `validate_inception.py` (presence + draft-marker + scaffold, exit 0/1/2), 14 tests; all 3 lint gates green; independently re-verified ALL GREEN; diagram capability scoped as a named non-blocking gap; committed `0e72853` (2026-06-30)

### Phase 3: Module Packaging — COMPLETE ✓ (CM + VM + register all done, 2026-06-30)
- [x] Run bmad-module-builder Create Module (CM) on `skills/` folder ✓ — `skills/cpm-setup/` (module.yaml + module-help.csv [42 rows] + setup SKILL.md + 3 merge scripts), 2026-06-30
- [x] Validate module with bmad-module-builder Validate Module (VM) ✓ — `validate-module.py` PASS / 0 findings + 13-agent adversarial quality pass (9 accurate / 4 minor-fixed), 2026-06-30
- [x] Register CPM V2 ✓ (2026-06-30) — deployed 13 skills → `.claude/skills/` + `.agents/skills/` (live this session); registered `_bmad/_config/skill-manifest.csv` (+13) + `bmad-help.csv` (+42) + `manifest.yaml` (module cpm) + `_bmad/cpm/` (config.yaml + module-help.csv). Done MANUALLY (NOT cpm-setup — format-incompatible; see Next Action). `config.toml` left untouched (installer-managed).

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
| 2026-06-30 | cpm-inception is a self-contained ONE-PASS draft generator, NOT four full re-runs | The plan calls inception "draft quality / rapid start"; running the four full workflows would not be faster. It reuses new-project's scaffold script (single structure source) but carries its OWN draft templates + contract for Bible/Style/Characters to stay self-contained; each draft is structurally valid against its foundation contract so the dedicated workflow refines it in place |
| 2026-06-30 | Inception's `validate` grades the DRAFT foundation only; a finalized artifact is past its gate | #13 verify flagged `validate_inception` false-HOLDing a promoted-to-final artifact. Fix kept `validate_inception.py` self-contained (REJECTED coupling it to the sibling `check_*.py`) and scoped the gate at the SKILL layer: a `status: final` artifact is graded by its dedicated workflow, not re-drafted here |
| 2026-06-30 | Inception's per-project production-flow diagram = named non-blocking gap | No scenes exist yet at onboarding, so the diagram is near-empty and excalidraw gen is heavy/error-prone; the Orchestrator's Production Diagram renders it once scene briefs exist |

---

## Session History

| Date | What I Did | Where I Left Off |
|------|------------|------------------|
| 2026-06-30 | **Phase 3 register/INSTALL DONE — CPM is live in this project, folder-scoped.** After committing the package, discovered the generated `cpm-setup` is format-incompatible with THIS install (its merge scripts target `config.yaml`/`module-help.csv`; the install uses `config.toml` + `_bmad/_config/*` manifests — divergent bmad-module-builder lineage) and its legacy-cleanup would delete `_bmad/core/config.yaml` — so I did NOT run it (caught by reading the scripts first). Installed MANUALLY instead, mirroring how bmb is installed: deployed all 13 skill folders → `.claude/skills/` + `.agents/skills/` (Claude Code auto-discovered them live this same session); registered `_bmad/_config/skill-manifest.csv` (+13 rows), `bmad-help.csv` (+42 incl a `_meta` row), `manifest.yaml` (module `cpm`); created `_bmad/cpm/config.yaml` + `module-help.csv`. Backed up the 3 registry files to scratchpad first; verified every row 13-col + manifest now lists core/bmb/cpm. Left installer-managed `config.toml` untouched; did NOT deploy the broken `cpm-setup` as a live skill. | **Use CPM**: `/cpm-inception` (guided) or `/cpm-new-project` → author scenes/shards → real handshake (Scene 8, 3 passes = VALIDATED) |
| 2026-06-30 | **Phase 3 — Create Module + Validate Module DONE** (via two read-only Workflow fan-outs + main-loop synthesis; the BMAD packaging step for the skills platform). CM: a 16-agent extraction (13 skill readers → each skill's `[agent]` block + capability rows; 3 open-item investigators) → I synthesized `skills/cpm-setup/assets/module.yaml` (cpm / "Cinematic Production Module" / 1.0.0 / 5-agent roster / `target_model`+`default_shard_duration` install defaults) and `module-help.csv` (42 rows, 42 unique menu codes — 2-letter for agent capabilities, 3-letter `skill+action` for the workflow create/update/validate triads; `preceded-by` ordering) → `scaffold-setup-skill.py` generated the `cpm-setup` skill (SKILL.md + 3 merge scripts). VM: `validate-module.py` → PASS / 0 findings; a 13-agent adversarial quality pass = 9 accurate / 4 minor — FIXED (script-supervisor `project_path` → optional `-project_path`; new-project `model_target` → "e.g." non-exhaustive; show-bible validate outputs += NO BIBLE) and KEPT-by-design w/ rationale (inception single-locus output-location; create→update/validate `preceded-by` soft-ordering, matching bmb's own CSV). Re-scaffolded + re-validated GREEN. Open items: (c) retired 7 stale `.claude/commands/cpm-*` v1 stubs (git rm) + rewrote CLAUDE.md command listings to skill-name invocation; (d) added `Production/Validation/` to cpm-new-project scaffold + its test + project-structure.md (suite 7/7 green); (e) NO broken config path exists (CPM skills reference none) → no fix; (f) Orchestrator writes `Diagrams/production-flow.excalidraw` → confirmed, no fix; (g) rewrote the 2 stale V1 step-file sections in CLAUDE.md for v2. ⚠ Snapshot Next Action clobbered to "1. ⏳" AGAIN (3rd time) mid-run despite read-only Explore agents — caught via `git diff`, restored (see Mental RAM). | **Register**: run `cpm-setup` → deploy to `.claude/skills/` → real end-to-end handshake (Completion Criteria #3) |
| 2026-06-30 | **Workflow #13 `cpm-inception` built + independently re-verified + committed** (`0e72853`) via Workflow orchestration (design-lock → build → 5 parallel adversarial lenses → fix/harden DoD gate; GREEN). The LAST workflow — agentic rapid-start onboarding: ONE conversational vision interview (6 movements) → a single compressed draft pass that reuses `cpm-new-project`'s `scaffold_project.py` (single source of the project skeleton) and drafts a Show Bible + Style Guide (4 Architecture files) + character sketch(es), each structurally valid against its foundation contract + honestly marked `status: draft`/`**Status:** DRAFT` with refine-pointers. create / update / validate with graceful resume (per-artifact skip, never clobber). 13 files; `validate_inception.py` (presence + draft-marker + scaffold, exit 0/1/2) + 14 tests; Validate also runs the sibling `check_*.py` to prove refine-readiness. 10 findings (1 high + 3 med + 6 low) all fixed; the fix agent correctly REJECTED a false-premise code fix (kept `validate_inception` self-contained, scoped the draft-gate at the SKILL layer) like #12. I re-ran 14/14 tests + all 3 lint gates myself (GREEN) and read the full SKILL.md (R1–R6 confirmed; diagram = named non-blocking gap). git confirms only `skills/cpm-inception/` changed; the canonical "The Second Receipt" project is byte-identical. NOTE: the committed Snapshot Next Action arrived corrupted ("1.") for the 2nd time — restored + added a guard note. | **Phase 3 — Create Module (CM)** on `skills/` (all 13 skills done), then Validate Module (VM) + register; resolve the carried Create-Module open items (c)–(g) |
| 2026-06-29 | **Workflow #12 `cpm-handshake-test` built + independently re-verified + committed** (`686869a`) via Workflow orchestration (engine → SKILL prose → 5 parallel adversarial lenses → bounded fix/gate loop; converged round 1, ALL gates GREEN). CREATE-ONLY continuity validation: a **Handshake Test Run** grades one adjacent boundary (Shard N→N+1) on the 5 criteria + the MUST-NOT-Show floor at equal hardness; a **Validation Suite** chains it under the 3-consecutive-pass law (3 PASS = VALIDATED; any FAIL or <3 testable boundaries = NOT VALIDATED with the gap named). 12 files; `validate_handshake.py` deterministic floor (token extraction hex/`[Asset:ID]`/RIGHT-LEFT/lens; identity+adjacency; entry-contract presence or final-shard `no_boundary`; signature-hex-in-B-lighting; exit 0/1/2; graceful finality degradation), 16 tests incl. every FAIL mode. Consumes #11's exit-state Entry Contract; generalizes the Script Supervisor's `handshake-review.md` (2-term → 5-criteria). I re-ran tests + all 3 lint gates myself (GREEN) and read every shipped file (R1–R6 confirmed). The fix agent correctly REJECTED a finding's false premise — kept `validation.*` project gates OUT of customize.toml (matching #11), grounding the key inline instead. Caveat: a build agent overstepped scope and clobbered this Snapshot's Next Action mid-run — restored. | Build #13 `cpm-inception` (the last workflow), then Create Module |
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
  - Built workflow skills (#6–#13): `cpm-new-project`, `cpm-show-bible`, `cpm-style-guide`, `cpm-character-create`, `cpm-scene-create`, `cpm-shard-generation`, `cpm-handshake-test`, `cpm-inception` — all under `skills/`
  - Module plan (source of truth): `skills/reports/module-plan-cpm-v2.md`
  - Build plan / backlog: `_bmad-output/cpm-build-plan-2026-06-28.md`
  - scene-create design spec: `skills/reports/scene-create-design-spec.md`
- **NOTE:** CPM is now PACKAGED at `skills/cpm-setup/` (Create Module + Validate Module done, 2026-06-30). It is not yet REGISTERED — the `cpm` section of `_bmad/config.yaml` and the rows in `_bmad/module-help.csv` are written when you run the `cpm-setup` skill; skills then deploy to `.claude/skills/` for auto-discovery. The old `.claude/commands/cpm-*.md` stubs were retired this session. Next: register.
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
- [x] 8 workflows built (#6–#13) — ALL 8 done, adversarially verified + committed (2026-06-30)
- [x] Module packaged via Create Module (`skills/cpm-setup/`: module.yaml, module-help.csv [42 rows], setup SKILL.md + merge scripts) — 2026-06-30
- [x] Module validated via Validate Module (`validate-module.py` PASS / 0 findings + 13-agent adversarial quality pass) — 2026-06-30
- [x] Module registered + deployed (2026-06-30) — 13 skills in `.claude/skills/` + `.agents/skills/`; `_bmad/_config/` manifests + `_bmad/cpm/` updated (MANUAL install; the generated cpm-setup scripts were format-incompatible with this BMAD)
- [ ] Real handshake: Test Scene 8 generates with 3 consecutive passes = CPM VALIDATED

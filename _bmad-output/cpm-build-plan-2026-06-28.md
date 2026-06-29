# CPM V2 — Execution Build Plan

**Date:** 2026-06-28
**Author:** Claude (Opus 4.8) — derived from the Ultracode comprehensiveness assessment + the existing `module-plan-cpm-v2.md`
**Status of CPM today:** Agent layer COMPLETE (2026-06-29) — **5 of 13 skills built** (all 5 agents) + 5-lens adversarially verified. The 8 workflows remain; `cpm-scene-create` (#10) has a design spec.
**Build platform:** BMB **v2.1.0** (installed 2026-06-28), BMAD Core **v6.9.0**. (`bmm` was removed per decision — install is core + bmb + future cpm.)

---

## TL;DR

You do **not** need to re-plan. A high-quality, v2-native **Module Plan** already exists (`skills/reports/module-plan-cpm-v2.md`) and it aligns cleanly with the v2.1.0 module-builder model. The *planning phase is effectively complete.*

What remains is **execution**: build 12 skills, package them into a registered module, and validate for real. This document operationalizes the existing plan into an honest, trackable backlog, and lists the handful of updates the plan needs now that BMB v2.1.0 is installed.

---

## 1. The v2.1.0 build model (what "build CPM" actually means now)

BMB v2 is a **Skills platform**. A module is no longer a hand-wired `_bmad/cpm/` tree with `workflows/*/workflow.md`. It is:

```
Ideate Module (IM)   → a module-plan.md            ✅ DONE  (module-plan-cpm-v2.md)
        ↓
Build each capability as a SKILL
   • agent skills   via Agent Builder (BA)
   • workflow skills via Workflow Builder (BW)       ◀ the bulk of the work
        ↓
Create Module (CM)   → module.yaml + module-help.csv + a `cpm-setup` skill + manifest registration
        ↓
Validate Module (VM) → validate-module.py + quality pass   ← real definition-of-done
```

Skills are authored in `{project-root}/skills/` (per `bmb.config`), then deployed to `.claude/skills/` (+ `.agents/skills/` for Gemini) and registered across the `_config` manifests. This is exactly how `core`, `bmm`, and `bmb` themselves are shipped.

**Consequence:** the 7 dangling `.claude/commands/cpm-*.md` stubs (which point at the old `_bmad/cpm/workflows/...` path that v2 no longer uses) are vestigial. They get **retired**, not repaired.

---

## 2. What the existing plan got right — and the few updates it needs

`module-plan-cpm-v2.md` is sound. Keep it as the source of truth for **identity, architecture, memory contract, and per-skill briefs**. Apply these deltas:

| # | Update | Why |
|---|--------|-----|
| U1 | Bump "BMAD v6.6.0" references → **v6.9.0 / BMB v2.1.0** | Platform was updated 2026-06-28. |
| U2 | **Void the false records** before building: mark `module-build-cpm.md` as NOT-BUILT and flag `validation-report-cpm-2026-02-03.md` as INVALID/superseded. | They claim `COMPLETE` / `PASSED 100%` but `_bmad/cpm/` never existed. They create a false "shipped" signal. |
| U3 | **Descope the dead `cpm-inception` route** from the orchestrator's `route-to-agent.md` until inception is actually built (it's #13, last). | Orchestrator currently routes to skills that don't exist (`/bmad-agent-cpm-*`, `/cpm-inception`) — a 100% dead routing table. |
| U4 | Relocate the orchestrator from top-level `skills/cpm-orchestrator/` into the module's skills set, and register it (skill-manifest row). | It's real but unregistered and in a non-standard location. |
| U5 | Fix project **`CLAUDE.md` "Registering a New Module"** section (it documents the old command→`_bmad/{module}/workflows/` pattern). | v2 uses skill auto-discovery + setup skills; the doc is misleading. |
| U6 | Confirm the **agent file format** against the now-installed v2 builder agents (`_bmad/bmb/agents/*.md`) before authoring the 4 specialists. | v2.0.0 rebuilt the agent architecture ("continuity-of-self"); author to the current format, not the brief's v1 `.agent.yaml` shape. |

---

## 3. Build backlog (the 12 remaining skills)

Order follows the plan's roadmap (dependencies first). Each is built with **BA** (Agent Builder) or **BW** (Workflow Builder), passing `module-plan-cpm-v2.md` as context. "Source" = where the content is lifted from (most is already written — this is assembly, not invention).

| # | Skill | Type | Method | Source material to lift | Non-negotiable | Status |
|---|-------|------|--------|--------------------------|----------------|--------|
| 1 | cpm-orchestrator | agent | — | — | Situational awareness; never executes the Ritual | ✅ Built (needs U3/U4) |
| 2 | **cpm-showrunner** (Albus) | agent | BA | Plan §Skills + brief 3.1 + `'The Second Receipt'/.cpm/agents/showrunner.md` | Never approve a beat that breaks the Show Bible / a Contract | ✅ Built + verified |
| 3 | cpm-cinematographer (Galadriel) | agent | BA | Plan + brief 3.2 + Receipt agent prompt | Exact hex codes; banned-word list absolute | ✅ Built + verified |
| 4 | cpm-script-supervisor (Jonas) | agent | BA | Plan + brief 3.3 + Receipt agent prompt | Check state before any compile; actively **inject** missing state | ✅ Built + verified |
| 5 | cpm-prompt-engineer (Leonard) | agent | BA | Plan + brief 3.4 + Receipt agent prompt | Critical features in first 25%; never compile without all 3 inputs | ✅ Built + verified |
| 6 | cpm-new-project | workflow | BW | Plan + brief 1.1–1.3 (dir structure, config.yaml, manifest.md) | Scaffolds the external state machine correctly | ⬜ |
| 7 | cpm-show-bible | workflow | BW | Plan + brief 2.1 + `'The Second Receipt'/Bible/Show_Bible.md` (proven template) | Full narrative DNA; all sections | ⬜ |
| 8 | cpm-style-guide | workflow | BW | Plan + brief 2.3 + Receipt `Style_Guide.md`, `Palette.md`, `Vocabulary.md` (proven) | **Fix A:** hint to read Show Bible first | ⬜ |
| 9 | cpm-character-create | workflow | BW | Plan + brief 2.2 + Receipt character files (proven) | LEFT/RIGHT specificity; **Fix B:** new vs update clarity | ⬜ |
| 10 | cpm-scene-create | workflow | BW | **Design spec written** → `skills/reports/scene-create-design-spec.md` (resolve its O1–O9 first) | Beats authored up front (Fix C2) so Showrunner doesn't invent them | ⬜ spec ready |
| 11 | cpm-shard-generation | workflow | BW | Plan + **brief lines 636–694** (the 6-step ritual) + Receipt `exit_state` artifact | State-Diff **HALT** gate before compile; variable-interval support | ⬜ core |
| 12 | cpm-handshake-test | workflow | BW | Plan + **brief lines 698–741** (5 criteria, 3-pass threshold) | The real definition-of-done; runnable, not prose | ⬜ |
| 13 | cpm-inception | workflow | BW | Plan §Skills (wraps #6–9 into one guided interview) | Conversational, not form-like; "draft quality" output | ⬜ build last |

**Templates note:** the proven instances in `_bmad-output/cpm-projects/'The Second Receipt'/` become each workflow's `template.md` asset. This is the de-risking factor — every output format has already been produced manually and validated in a real production.

---

## 4. Package — Create Module (CM)

Once skills exist, run **Create Module (CM)** (multi-skill / setup-skill approach). It generates:

- **`module.yaml`** — identity (`code: cpm`, name, description, `module_version: 2.0.0`, greeting) + an **`agents:` roster** of the 5 agent skills (orchestrator, showrunner, cinematographer, script-supervisor, prompt-engineer) with `code/name/title/icon/description` from each agent's `customize.toml`.
- **`module-help.csv`** — one row per capability (≈25–30 rows across 13 skills) with menu-codes, before/after ordering, required gates, outputs.
- **`cpm-setup` skill** — handles registration + the 2 config questions.
- **Manifest registration** — adds `cpm` to `manifest.yaml` and rows to all relevant `_config` CSVs (this is what finally makes CPM *installed*).

**Config variables** (per the plan, stored per-project in `.cpm/config.yaml`):

| Variable | Prompt | Default |
|----------|--------|---------|
| `target_model` | Which AI video model? (sora/kling/runway/pika) | `sora` |
| `default_shard_duration` | Default shard duration in seconds? (5/15/30) | `5` |

---

## 5. Validate — for real this time (VM)

Definition-of-done that replaces the voided "PASSED 100%":

1. **`validate-module.py {skills-folder}`** passes — structure, module.yaml completeness, CSV integrity (no orphans/dupes/broken before-after), agent roster matches `customize.toml`.
2. **LLM quality pass** — every capability has an accurate, action-oriented help row; descriptions route correctly.
3. **The module's own test:** encode **Test Scene 8 "The Abandoned Cathedral"** (brief §5.1) and run `cpm-handshake-test` → **3 consecutive passes = CPM VALIDATED.**
4. **Truthful trail:** write a genuine validation report only after a real pass.

---

## 6. Phased roadmap (with effort)

| Phase | Work | Skills/Steps | Effort |
|-------|------|--------------|--------|
| **P0 — Reset signal** | Apply U2/U3/U5; confirm v2 agent format (U6) | docs + voiding records | ✅ DONE 2026-06-29 |
| **P1 — 4 specialist agents** | BA ×4 | #2–5 | ✅ DONE 2026-06-29 (built + 5-lens verified) |
| **P2 — Foundation workflows** | BW ×4 + author scene-create spec | #6–9 (+ #10 spec) | **L** |
| **P3 — Core loop + validation** | BW ×2 + scene-create | #10, #11, #12 | **L** |
| **P4 — Inception + orchestrator wiring** | BW ×1 + U4 | #13, orchestrator relocate/register | **M** |
| **P5 — Package + validate** | CM, then VM + handshake suite | module.yaml, cpm-setup, manifests, Test Scene 8 | **M** |

Total: a real module build, but **de-risked** — design done, personas written, every template proven in a live production.

---

## 7. Decisions (resolved 2026-06-29)

1. **Build execution** — ▶ **Building underway.** P0 + the full agent layer (5 skills) built + verified 2026-06-29; the workflow phase is next.
2. **`cpm-inception` scope** — ✅ **Keep as the #13 capstone** (per the plan's roadmap).
3. **`bmm` module** — ✅ **Removed.** Install is now `core` + `bmb` (+ future `cpm`); skills 51 → 18. (commit `866914b`)
4. **Agent format** — ✅ **Stateless lean SKILL.md** (SKILL.md + customize.toml + references/), not BOND/CREED sanctum. Mirror `skills/cpm-orchestrator` / `skills/cpm-showrunner`.
5. **Manifest ownership** — ✅ `cpm-new-project` scaffolds `.cpm/manifest.md`; **scene-create owns the `### Scenes` block**; Orchestrator + Script Supervisor own `### Active Scene Context`.
6. **Contract ownership** — ✅ A *workflow* (scene-create) writes `Production/Contracts/*.md`; agents only report/flag (Albus encoded).
7. **Workflow-skill format** — ✅ v2 producing-workflow = inline-SKILL.md named sections + `[workflow]` customize.toml + create/update/validate intent modes + `.memlog.md` (NOT the V1 `steps-c/e/v` folders). Detail locked in `Snapshot.md` Mental RAM.

## ▶ Resume here next session

**Done 2026-06-29:** P0 resets (U2/U3/U5) ✅ · agent format confirmed = stateless lean SKILL.md (U6) ✅ · **P1 agent layer COMPLETE** — all 5 agents built + 5-lens adversarially verified + fixed + re-verified (#2–#5) ✅ · `cpm-scene-create` design spec written ✅.

**Start at the build backlog (§3), workflow #6 — `cpm-new-project`.** Build with the **Workflow Builder** (`bmad-workflow-builder`), applying the six skill-quality pattern rules R1–R6 (recorded in `Snapshot.md` Mental RAM — every enforcing capability loads its authority doc; symmetric hard gates; a refusal slot; no build-jargon; precise nested config keys; no placeholders). The **workflow-skill format is already locked** and the **manifest/contract conventions are pinned** (2026-06-29 — see §7 above and `Snapshot.md` Mental RAM); no re-scout needed — start building.

1. #6 `cpm-new-project` → #7 `cpm-show-bible` → #8 `cpm-style-guide` (Fix A) → #9 `cpm-character-create` (Fix B). Each lifts its proven template from `'The Second Receipt'/`.
2. #10 `cpm-scene-create` — the **design spec is ready** (`skills/reports/scene-create-design-spec.md`); **resolve its open questions O1–O9 first**, then build. Build it before #11.
3. #11 `cpm-shard-generation` (Fix C2 + variable intervals; the core loop) → #12 `cpm-handshake-test` → #13 `cpm-inception` (last; wraps #6–#9).
4. When all 13 skills exist → **Create Module (CM)** → **Validate Module (VM)** + 3-pass handshake on Test Scene 8.
5. Also resolve the module-wide design Qs flagged in `Snapshot.md` Mental RAM (contract write-owner; manifest write-owner; agent activation prefix `/bmad-agent-cpm-*` vs `/cpm-*`).

---

## Appendix — source map

- **Existing plan:** `skills/reports/module-plan-cpm-v2.md` (the Module Plan — keep)
- **Original brief/roadmap:** `_bmad-output/bmb-creations/modules/module-brief-cpm.md`, `_bmad-output/brainstorming/CPM-V1-Roadmap.md`
- **Proven templates + agent prompts:** `_bmad-output/cpm-projects/'The Second Receipt'/` (Bible, Architecture, Production, `.cpm/`)
- **False records to void:** `module-build-cpm.md`, `validation-report-cpm-2026-02-03.md`
- **Full gap assessment:** `_bmad-output/cpm-assessment-2026-06-28.md`
- **v2 build methodology:** `.claude/skills/bmad-module-builder/references/{create,ideate,validate}-module.md`

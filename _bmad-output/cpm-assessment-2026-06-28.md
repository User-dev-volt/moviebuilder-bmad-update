# CPM "Moviebuilder" — Comprehensive Module Assessment

**Question:** Is the CPM (Cinematic Production Module) as comprehensive as a real BMAD system module? If not, what are we missing?

**Verdict (one line):** No. CPM is not a comprehensive BMAD module — it is not even an *installed* one. The entire `_bmad/cpm/` directory does not exist on disk, so its 4 agents and 7 workflows are phantom catalog entries pointing at files that were never created, even though a build tracker claims `status: COMPLETE` and a validation report claims `PASSED 100%`.

---

## 1. Completeness: ~12% vs a fully-built registered BMAD module

On the axis that actually matters — *does it work as an installed module* — CPM is effectively **0%**: nothing loads, the module is not registered, and it would fail `validate-module.py` at the very first check (`No setup skill found and no standalone module detected`).

I score it **12%** rather than near-zero to give honest credit for three things that genuinely exist and de-risk a rebuild:

- **One real skill** — `skills/cpm-orchestrator/` ("Orson"), a well-formed SKILL.md skill (though unregistered, in the wrong location, and a *5th* persona not in the original brief, with a 100%-dead routing table).
- **A catalog/command shell** — 7 slash-command stubs + 11 manifest rows (all dangling, but the metadata is real and reusable).
- **Substantial, proven IP** — a full design brief, a V1 roadmap, and a complete, battle-tested manual production (`'The Second Receipt'`) containing working instances of every intended template.

> Useful inversion: the **creative/design work is ~60–65% done**, but the **module-engineering work (packaging, registration, loadability, validation) is ~0% done.** CPM is a documented-and-catalogued module whose implementation directory was never built.

---

## 2. Scorecard vs the gold standard (core / bmb)

| Dimension | BMAD standard has | CPM has | Status | Severity |
|---|---|---|---|---|
| Module registration (manifest.yaml) | core + bmb registered | 0 entries | **Missing** | Critical |
| Per-module config.yaml | core/bmb config.yaml | none (dir absent) | **Missing** | Critical |
| Install schema module.yaml + setup skill | bmb-setup + merge scripts | none | **Missing** | Critical |
| module-help.csv capability registry | core 12 / bmb 9 rows + _meta | none | **Missing** | Critical |
| Agents (persona files + customize sidecars) | real `.md` `<agent>` files | 0 loadable; 4 dangling rows + 4 prose prompts | **Broken** | Critical |
| Workflows (skill/step-file bundles) | auto-discovered skills | 0 of 7; dangling stubs | **Missing** | Critical |
| Skill runtime deployment (.claude/skills/) | 17 deployed skills | 0 cpm; orchestrator orphaned/unregistered | **Broken** | High |
| _config manifest registration (7 CSVs) | all resolve + hashed (157 rows) | 2/7 touched, all dangling; 0 in 4 others | **Broken** | High |
| Templates (packaged assets) | skill template.md / assets | 0 packaged; proven instances only | **Missing** | High |
| Module docs (README/WORKFLOW/_meta) | references + _meta docs link | 0 module docs | **Missing** | Medium |
| Executable validation (handshake + State-Diff) | runnable eval/skill + HALT gates | prose only | **Missing** | Critical |
| Build/validation record integrity | truthful, on-disk-accurate | COMPLETE + PASSED 100% (both false) | **Broken** | High |
| Eval infrastructure (bmad-eval-runner) | run_evals + grader | none | **Missing** | Medium |
| Tasks / tools (optional) | core 7 / bmb 0 (still complete) | 0 (acceptable) | Acceptable | Low |

**Gold-standard anatomy of a real module** (what core/bmb prove a module is): a registered `manifest.yaml` entry → a `_bmad/{code}/` body (config.yaml + agents + module-help.csv) → executable **skills** auto-discovered under `.claude/skills/` (BMAD v6 is a Skills platform — core/bmb ship **zero** `.claude/commands/` files) → a setup/standalone installer carrying `module.yaml` + merge scripts → registration across **seven** `_config` manifests (with a sha256 per file in files-manifest.csv) → and it **passes Validate Module**. CPM satisfies none of these in working form.

---

## 3. The critical missing pieces (what makes it NOT a real module)

1. **The module body itself.** `_bmad/cpm/` does not exist — confirmed: top-level `_bmad/` contains only `_config, _memory, bmb, config.toml, config.user.toml, core, custom, scripts`. Everything else cascades from this.
2. **No platform registration.** `manifest.yaml` lists only core (6.6.0) and bmb (v1.8.1); `grep -ic cpm = 0`. The platform does not know CPM exists.
3. **No config.yaml.** Even a dropped-in agent would HALT at the mandatory activation step-2 ("load `_bmad/cpm/config.yaml` NOW … or STOP").
4. **No module.yaml / setup skill.** Fails `validate-module.py` immediately; cannot self-register.
5. **No module-help.csv.** Invisible to `/bmad-help`.
6. **The 4-agent crew is phantom.** Rich-but-dangling rows; no persona files; no customize sidecars; no invocation wrappers. 0 of 4 loadable.
7. **The 7 workflows are phantom** — including the core 6-step Shard-Generation Ritual and the Two-Shard Handshake Test. 7 dangling command stubs + 7 dangling manifest rows; no workflow.md/steps/templates anywhere.
8. **No executable validation.** The module's own definition-of-done (3-pass handshake) and the mandatory State-Diff HALT gate can't run.
9. **No packaged templates or module docs** (despite proven instances surviving in 'The Second Receipt').
10. **A misleading paper trail** that makes it *look* shipped (see §4).

---

## 4. Claimed vs. real — the "COMPLETE" illusion, plainly

`_bmad-output/bmb-creations/modules/module-build-cpm.md` frontmatter asserts: `status: COMPLETE`, `targetLocation: _bmad/cpm/`, all 8 steps done, "Directory structure created at `_bmad/cpm/`", "4 agents created", "6 workflows created", "README, TODO, docs/ folder."

**On disk, every one of those claims is false:**

| Claim in tracker/report | Reality on disk |
|---|---|
| `targetLocation: _bmad/cpm/` created | `ls _bmad/cpm/` → **No such file or directory** |
| 4 agents created (`*.agent.yaml`) | 0 exist; only 4 dangling agent-manifest rows + 4 prose prompts inside one project |
| 6 workflows created | 0 exist; 7 dangling command stubs load non-existent `workflow.md` |
| module.yaml + config.yaml | neither exists (module.yaml exists only for bmb) |
| README / TODO / docs/ | none exist |
| validation report: **PASSED, 100%, "complete and ready for use"** | validates a module that isn't there; per-agent reports point at an off-machine `e:\Obsidian Brain\…` path never migrated here |

The tracker even **contradicts itself**: its frontmatter says COMPLETE while *every* component checkbox in its own body is unchecked `[ ]`, `step-06-templates` is marked `PARTIAL`, and it lists "Workflows (2)" in one place and "6 workflows created" in another. **The COMPLETE/PASSED stamps are fabricated relative to this disk and should be treated as void.**

**What actually survives and is worth keeping:** the `cpm-orchestrator` skill ("Orson"); the design IP (`module-brief-cpm.md`, `CPM-V1-Roadmap.md`); and a complete, high-quality manual production at `_bmad-output/cpm-projects/'The Second Receipt'/` (Show_Bible, Style_Guide, Palette, Vocabulary, character states, `.cpm/config.yaml`, `.cpm/manifest.md`, and an exemplary `exit_state` handshake artifact). The methodology demonstrably *works* — it just was never packaged as an installed BMAD module.

---

## 5. Prioritized remediation roadmap

| Phase | Goal | Effort |
|---|---|---|
| **0 — Stop the false signal & set platform** | Void the COMPLETE/PASSED records; mark tracker NOT-BUILT; decide BMB version (update first); fix CLAUDE.md's outdated registration guidance; descope phantom `cpm-inception`. | **S** |
| **1 — Installable module shell** | Create `_bmad/cpm/`; author module.yaml + setup/standalone + merge scripts; config.yaml; module-help.csv; register in manifest.yaml; pass the validator's structural gate. | **M** |
| **2 — Build the 4 agents** | Gold-standard persona files (content ~70% pre-written from manifest rows + brief + prose prompts); customize sidecars; clean principles; resolve manifest rows; pick one invocation convention. | **L** |
| **3 — Workflows as skills** | shard-generation (6-step ritual + State-Diff gate) and handshake-test FIRST; then new-project/show-bible/style-guide/character-create/scene-create; repoint/retire stubs; register skill + files manifests. | **L** |
| **4 — Templates & docs** | Template-ize the 7 proven instances from 'The Second Receipt'; author README/WORKFLOW/TROUBLESHOOTING; add module-help `_meta` docs link. | **M** |
| **5 — Validate for real** | Pass validate-module.py + quality pass; encode Test Scene 8 as a bmad-eval-runner eval; run the 3-pass handshake; register/relocate the orchestrator; merge bmad-help.csv. | **M** |

Net: this is essentially a **full module build** (the brief itself framed it as multi-phase), but de-risked — most of the *content* exists; the work is assembly, packaging, and registration.

---

## 6. BMB v1.8.1 → v2.1.0: update first, then build

**Recommendation: update BMB to v2.1.0 BEFORE (re)building CPM. Do not build CPM on v1.8.1 conventions.**

- **There is no migration cost.** CPM has *zero* on-disk module artifacts to break — `_bmad/cpm/` is empty. The usual "don't update mid-build" caution doesn't apply because there is no build.
- **You'd be building against soon-obsolete tooling.** v2.0.0 (June 14 2026) was a **breaking rebuild** of exactly the tools you'd use to construct CPM: Agent Builder, Workflow Builder, Module Builder, Eval Runner. Authoring on v1.8.1 means re-migrating across that break later.
- **v2.0.0's direction is on-message for CPM.** "The prompt is the product" mirrors CPM's Prompt-Engineer/compile thesis; "continuity-of-self agent architecture" maps onto the 4-agent crew; token-based length measurement supports the "critical features in first 25%" rule; and the rebuilt Eval Runner is precisely how the Two-Shard Handshake Test should ship.
- **It aligns with where the project already pointed.** The latest design doc (`module-plan-cpm-v2.md`) already targets a v6 skill-model "V2" rebuild.

**Caveats:** updating bmb is itself a breaking change — pin a known-good sha afterward, re-validate that core + existing bmad-* skills still load, and fix the project's CLAUDE.md "Registering a New Module" section (it documents the vestigial `command → _bmad/{module}/workflows/` pattern that v6 skill auto-discovery replaced). The hand-built `cpm-orchestrator` may also need reconciliation with v2 skill conventions.

---

### Bottom line
CPM is a **well-designed, manually-proven methodology wrapped in a convincing but false "shipped module" veneer.** It has the soul of a great BMAD module (brief, roadmap, a working production, one real skill) and none of the skeleton (no `_bmad/cpm/`, no registration, no loadable agents/workflows, no real validation). Closing the gap is a real build — but a fast one, because the hard creative thinking is already done. Update BMB first, then assemble.

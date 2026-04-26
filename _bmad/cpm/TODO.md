# TODO: CPM - Cinematic Production Module

Development roadmap for cpm module.

---

## Module Status: PRE-ALPHA (Not Yet Registered)

The module structure is complete but CPM is NOT yet registered as an installed BMAD module. Commands like `/cpm-*` will not work until registration.

---

## Immediate Priorities

### 1. Validate Agents with BMB Agent Builder

Run `/bmad-bmb-agent` in [V]alidate mode for each agent:

- [ ] **Showrunner** — `_bmad/cpm/agents/showrunner.agent.md`
- [ ] **Cinematographer** — `_bmad/cpm/agents/cinematographer.agent.md`
- [ ] **Script Supervisor** — `_bmad/cpm/agents/script-supervisor.agent.md`
- [ ] **Prompt Engineer** — `_bmad/cpm/agents/prompt-engineer.agent.md`

**How to run:** See BMB Agent Builder Quick Guide below.

### 2. Create Missing `config.yaml`

- [ ] Create `_bmad/cpm/config.yaml` with module settings

### 3. Register CPM in BMAD System

- [ ] Add CPM to `_bmad/_config/manifest.yaml`
- [ ] Add CPM workflows to `_bmad/_config/workflow-manifest.csv`
- [ ] Add CPM to `_bmad/_config/bmad-help.csv` (optional, for `/bmad-help` routing)

---

## BMB Agent Builder Quick Guide

### For Validation (Recommended First)

1. **Start fresh context window**
2. **Run:** `/bmad-bmb-agent`
3. **Choose:** `[V]alidate`
4. **When asked for path:** `_bmad/cpm/agents/showrunner.agent.md`
5. **Review:** Validation report will be generated
6. **Fix:** Apply recommended fixes if any

### For Creating New Agents

1. **Start fresh context window**
2. **Run:** `/bmad-bmb-agent`
3. **Choose:** `[C]reate`
4. **Brainstorm:** Optional ideation phase
5. **Discovery:** Define role, responsibilities, context
6. **Build:** Workflow generates compliant agent file

### What to Share with BMB Agent Builder

- The agent file path when prompted
- Your module context (CPM = Cinematic Production Module)
- Any specific concerns or areas to focus on

---

## Agents Status

All 4 agents created, pending BMAD compliance validation:

| Agent | Spec File | Runtime File | Validated |
|-------|-----------|--------------|-----------|
| Showrunner | `agents/showrunner.agent.md` | `templates/project/.cpm/agents/showrunner.md` | [ ] |
| Cinematographer | `agents/cinematographer.agent.md` | `templates/project/.cpm/agents/cinematographer.md` | [ ] |
| Script Supervisor | `agents/script-supervisor.agent.md` | `templates/project/.cpm/agents/script-supervisor.md` | [ ] |
| Prompt Engineer | `agents/prompt-engineer.agent.md` | `templates/project/.cpm/agents/prompt-engineer.md` | [ ] |

---

## Workflows Status

All 6 workflows created:

| Workflow | File | Tested |
|----------|------|--------|
| shard-generation | `workflows/shard-generation/workflow.md` | [x] (Scene 01 Shard 1 — 2026-02-21) |
| handshake-test | `workflows/handshake-test/workflow.md` | [ ] ← NEXT |
| new-project | `workflows/new-project/workflow.md` | [x] |
| show-bible | `workflows/show-bible/workflow.md` | [x] |
| style-guide | `workflows/style-guide/workflow.md` | [x] |
| character-create | `workflows/character-create/workflow.md` | [x] |
| scene-create | `workflows/scene-create/workflow.md` | [x] (Scene 01 — 2026-02-21) |

---

## Templates to Complete

Project templates in `templates/project/`:

- [x] `.cpm/agents/` — Agent prompts (4 files)
- [ ] `.cpm/config.yaml` — Project config template
- [ ] `.cpm/manifest.md` — Context index template
- [ ] `Bible/Show_Bible.md` — Show Bible template
- [ ] `Bible/Characters/_index.md` — Character index
- [ ] `Bible/World/_index.md` — World index
- [ ] `Architecture/Style_Guide.md` — Style Guide template
- [ ] `Architecture/Palette.md` — Palette template
- [ ] `Architecture/Vocabulary.md` — Vocabulary template
- [ ] `Production/Slate.md` — Production status template

---

## Testing Phases

### Phase 1: Agent Validation — COMPLETE
- [x] Validate all 4 agents with BMB

### Phase 2: Module Registration — COMPLETE
- [x] Create config.yaml
- [x] Update manifest.yaml
- [x] Update workflow-manifest.csv

### Phase 3: Workflow Testing — COMPLETE
- [x] Test `new-project` scaffolding
- [x] Test `show-bible` creation flow
- [x] Test `style-guide` creation flow
- [x] Test `character-create` flow
- [x] Test `scene-create` flow (Scene 01, 2026-02-21)
- [x] Test `shard-generation` (Scene 01 Shard 1, 2026-02-21)

### Phase 4: Core Validation — CURRENT

- [ ] Run Handshake Test (3 consecutive passes required) ← NEXT
- [ ] Document any failures and fixes
- [ ] Iterate agent prompts as needed

---

## Documentation

- [x] README.md — Module overview
- [x] TODO.md — This file
- [x] NEXT-STEPS.md — Prioritized action guide
- [x] docs/getting-started.md — Quick start
- [x] docs/agents.md — Agent reference
- [x] docs/workflows.md — Workflow reference
- [x] docs/examples.md — Examples and troubleshooting

---

## Future Enhancements (V2.0 Roadmap)

| Feature | Description | Dependency |
|---------|-------------|------------|
| VLM-QA Agent | Visual regression testing with GPT-4o/Gemini | V1.0 validated |
| Cinematic Transpiler | Universal Cinematic Language + Model Adapters | Prompt format stable |
| Exception-Based Review | Confidence scoring, auto-commit for 95%+ | VLM-QA working |
| Agentic Inception | Interview-based onboarding (no Markdown writing) | Core templates done |
| Git Collaboration | Branching narratives, merge conflict resolution | Multi-user need |

---

_Last updated: 2026-04-22_

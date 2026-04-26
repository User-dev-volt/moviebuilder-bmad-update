# CPM: Cinematic Production Module

**External State Machine for AI Video Generation**

Cinematics as Code — 50 years of Software Engineering solving 100 years of Cinematic Production problems.

---

## Overview

CPM solves the **Vibe-Drift Gap** — the problem where AI video generators forget characters, settings, and continuity between generations. By applying BMAD's document-based, agentic architecture to cinematic production, CPM treats **context as currency**.

**The Core Thesis:** AI video generators are stateless; CPM is the memory.

### Key Innovations

1. **Continuity Acceptance Criteria (CAC)** — Unit testing for cinema
2. **Temporal Sharding** — 5-second atomic beats with handshakes
3. **Three-Tiered Staging** — Text validation → Keyframe → Animatic
4. **Narrative Contracts** — Forward-looking foreshadowing validation
5. **External State Machine** — Document-based continuity enforcement

---

## Installation

```bash
bmad install cpm
```

---

## Quick Start

1. **Create a new project:**
   ```
   /cpm-new-project
   ```

2. **Define your story:**
   ```
   /cpm-show-bible
   ```

3. **Set your visual style:**
   ```
   /cpm-style-guide
   ```

4. **Add characters:**
   ```
   /cpm-character-create
   ```

5. **Start producing:**
   ```
   /cpm-shard-generation
   ```

**For detailed documentation, see [docs/](docs/).**

---

## Components

### Agents (The Film Crew)

| Agent | Role | Owns | Equivalent |
|-------|------|------|------------|
| **Showrunner** | Story Guardian | Show Bible | PM |
| **Cinematographer** | Visual Architect | Style Guide | Architect |
| **Script Supervisor** | Continuity Tracker | State Files | QA |
| **Prompt Engineer** | Prompt Compiler | Final Prompts | Developer |

### Workflows

| Workflow | Purpose |
|----------|---------|
| `shard-generation` | The 6-step mandatory ritual for generating prompts |
| `handshake-test` | Two-shard validation protocol |
| `new-project` | Scaffold a new CPM project |
| `show-bible` | Create your story bible |
| `style-guide` | Define visual language |
| `character-create` | Create character state files |

---

## Configuration

The module supports these configuration options (set during installation):

| Variable | Description | Default |
|----------|-------------|---------|
| `project_name` | Title of your cinematic project | Directory name |
| `model_target` | AI video generator | `wan` (Wan 2.2) |
| `default_shard_duration` | Temporal shard length | `5` seconds |
| `enable_strict_validation` | Enforce CAC checks | `true` |
| `cpm_output_folder` | Output location | `{output_folder}/cpm-projects` |

---

## Module Structure

```
cpm/
├── module.yaml              # Module configuration
├── config.yaml              # User settings
├── README.md                # This file
├── TODO.md                  # Development roadmap
├── docs/                    # User documentation
│   ├── getting-started.md
│   ├── agents.md
│   ├── workflows.md
│   └── examples.md
├── agents/                  # Agent definitions
│   ├── showrunner.agent.md
│   ├── cinematographer.agent.md
│   ├── script-supervisor.agent.md
│   └── prompt-engineer.agent.md
├── workflows/               # Workflow definitions
│   ├── shard-generation/
│   ├── handshake-test/
│   ├── new-project/
│   ├── show-bible/
│   ├── style-guide/
│   └── character-create/
├── templates/               # Project scaffolding templates
│   └── project/
└── _module-installer/       # Installation logic
```

---

## Documentation

For detailed user guides and documentation, see the **[docs/](docs/)** folder:

- [Getting Started](docs/getting-started.md) — Quick start guide
- [Agents Reference](docs/agents.md) — Meet your film crew
- [Workflows Reference](docs/workflows.md) — Available workflows
- [Examples](docs/examples.md) — Practical examples and troubleshooting

---

## The Philosophy

> "Cinematics as Code — 50 years of Software Engineering solving 100 years of Cinematic Production problems."

> "Context as Currency — treating context with BMAD rigor unlocks Hollywood-scale storytelling with a fraction of the resources."

> "Automating the Boredom — Agents handle rigid discipline; humans provide soul."

> "Studio-in-a-Box — Democratization of the blockbuster; crew of 200 → crew of 1."

---

## Development Status

- [x] Module structure created
- [x] 4 agents defined
- [x] 6 workflows created
- [x] Templates ready
- [x] Installer configured
- [ ] Full validation testing (Handshake Test)

See [TODO.md](TODO.md) for detailed status.

---

## Author

Created via BMAD Module workflow

---

## License

Part of the BMAD framework.

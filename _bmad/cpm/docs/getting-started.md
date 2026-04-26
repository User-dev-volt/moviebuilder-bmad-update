# Getting Started with CPM

Welcome to the Cinematic Production Module! This guide will help you get up and running.

---

## What This Module Does

CPM (Cinematic Production Module) is an **External State Machine for AI Video Generation**. It solves the "Vibe-Drift Gap" — the problem where AI video generators forget characters, settings, and continuity between generations.

**The Core Idea:** AI video generators are stateless. They have no memory. CPM provides that memory through structured documents and a disciplined Four-Agent Ritual.

---

## Installation

If you haven't installed the module yet:

```bash
bmad install cpm
```

You'll be asked to configure:
- **Project name** — Your cinematic project title
- **Model target** — Which AI generator (Wan 2.2, Sora, Kling, Runway)
- **Shard duration** — Default length for temporal shards (5s recommended)
- **Strict validation** — Whether to enforce all continuity checks

---

## First Steps

### 1. Create Your Project

```
/cpm-new-project
```

This scaffolds the complete CPM project structure:
- `.cpm/` — Configuration and agents
- `Bible/` — Story, characters, world
- `Architecture/` — Visual style guide
- `Production/` — Scenes and shards
- `Output/` — Generated prompts and renders

### 2. Define Your Story

```
/cpm-show-bible
```

The Show Bible is your story's "PRD" — it defines:
- Logline and genre
- Thematic pillars
- World rules
- Story arc
- Recurring motifs

### 3. Set Your Visual Style

```
/cpm-style-guide
```

The Style Guide is your visual "Architecture" — it defines:
- Lighting protocols (with hex codes)
- Color palette (allowed and forbidden)
- Camera language (lens choices)
- Prompt vocabulary (banned/required words)

### 4. Create Your Characters

```
/cpm-character-create
```

For each character, you'll define:
- Visual identity (immutable features like scars)
- Current outfit and condition (mutable)
- Inventory (what they carry)
- Physical state (injuries, conditions)
- Arc position (emotional state, wants, needs)

### 5. Start Producing

```
/cpm-shard-generation
```

The Shard Generation Ritual runs the Four-Agent Review:
1. **Context Loading** — Read all required files
2. **Showrunner Review** — Story alignment check
3. **Cinematographer Specs** — Visual specifications
4. **Script Supervisor Validation** — Continuity check
5. **Prompt Compilation** — Generate the final prompt
6. **State Update** — Record exit state for handshake

---

## The Four Agents

CPM uses four specialized agents that form your "Film Crew":

| Agent | Asks | Owns |
|-------|------|------|
| **Showrunner** | "Does this serve the story?" | Show Bible |
| **Cinematographer** | "Does this match our visual style?" | Style Guide |
| **Script Supervisor** | "Is continuity maintained?" | State Files |
| **Prompt Engineer** | "Is this prompt optimized for AI?" | Final Prompts |

Every shard goes through all four agents before generation.

---

## Key Concepts

### Temporal Sharding

Break your scenes into 5-second "shards" — atomic beats that can be validated independently. Each shard has:
- An **entry state** (where it starts)
- An **exit state** (where it ends)
- A **handshake** with the next shard

### The Handshake

The handshake is how shards maintain continuity:
- Shard A ends with: "Hero holding Key in right hand, looking frame-left"
- Shard B must start with: Hero in that exact position

The Script Supervisor validates this automatically.

### Narrative Contracts

Foreshadowing as "contracts" that must be paid off:
- **PLANT:** Introduce the foreshadowing element
- **MAINTAIN:** Keep it visible/referenced
- **PAYOFF:** Deliver on the promise

The Showrunner tracks these across scenes.

---

## Common Use Cases

### Single Scene Production
1. Create Show Bible (brief version)
2. Create Style Guide
3. Create character(s)
4. Run Shard Generation for each beat

### Full Short Film
1. Complete Show Bible with full arc
2. Detailed Style Guide with all rules
3. All characters with state tracking
4. Scene-by-scene production with handshakes

### Style Testing
1. Create basic Show Bible
2. Experiment with Style Guide variations
3. Generate same scene with different styles

---

## What's Next?

- Check out the [Agents Reference](agents.md) to understand each agent's role
- Browse the [Workflows Reference](workflows.md) for all available workflows
- See [Examples](examples.md) for real-world usage and troubleshooting

---

## Need Help?

If you run into issues:
1. Check the troubleshooting section in [examples.md](examples.md)
2. Ensure all required files exist (Show Bible, Style Guide, Character files)
3. Verify your model target settings in `.cpm/config.yaml`
4. Run the Handshake Test to validate your setup

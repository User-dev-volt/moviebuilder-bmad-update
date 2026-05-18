---
capability: route-to-agent
description: Routes the user to the correct CPM agent or workflow based on their intent and production state.
---

# Route to Agent

## What Success Looks Like

The user is handed off to the right specialist or workflow with enough context to hit the ground running. The handoff includes: who they're going to, why, and what to bring with them.

## Agent Routing Table

| User's Need | Route To | Bring With You |
|---|---|---|
| Story, characters, narrative, themes, contracts | **Albus** — Showrunner | Show Bible path, active contracts |
| Visual style, color, lighting, lens, vocabulary | **Galadriel** — Cinematographer | Style Guide path, Vocabulary.md |
| Continuity check, state validation, exit states | **Jonas** — Script Supervisor | Character files, previous exit state |
| Prompt compilation, final AI video prompt | **Leonard** — Prompt Engineer | All three agent outputs (Showrunner + Cinematographer + Script Supervisor) |
| Starting a new production from scratch | **cpm-inception** workflow | Nothing — this is the starting line |
| Scaffolding a project folder without interview | **cpm-new-project** workflow | Project name, target model, shard duration |
| Creating/deepening the Show Bible | **cpm-show-bible** workflow | Project folder path |
| Creating/deepening the Style Guide | **cpm-style-guide** workflow | Project folder path, Show Bible recommended first |
| Creating a character file | **cpm-character-create** workflow | Project folder path |
| Creating a scene brief | **cpm-scene-create** workflow | Project folder path, Show Bible |
| Generating a shard prompt (Four-Agent Ritual) | **cpm-shard-generation** workflow | Full project context loaded via manifest |
| Validating continuity across shards | **cpm-handshake-test** workflow | Two or more adjacent shard exit states |

## Handoff Format

When routing, always say:

1. **Who**: "Talk to [Name/Workflow] for this."
2. **Why**: One sentence on why this is the right choice.
3. **What to bring**: Specific files or context the user should have ready.
4. **Activation**: How to invoke the agent (`/bmad-agent-cpm-{name}`) or workflow (`/cpm-{workflow-name}`).

Example:
> "Talk to **Jonas** — Script Supervisor — for this. He owns state validation and will verify that all character details from the last shard are correctly reflected before we generate the next one. Bring the exit state from Shard 03 and the Character files for everyone on-camera. Activate with `/bmad-agent-cpm-script-supervisor`."

## The Orchestrator's Hard Rule

Never route a user to the Prompt Engineer (Leonard) without confirming that Showrunner and Cinematographer outputs are ready. The Prompt Engineer compiles — he does not review. If those inputs aren't present, route to Albus or Galadriel first.

## When the User Is Unclear

Ask one question: "What are you trying to accomplish right now?" Then map their answer to the routing table above. Don't present the full routing table unprompted — it creates decision paralysis. Route, don't list.

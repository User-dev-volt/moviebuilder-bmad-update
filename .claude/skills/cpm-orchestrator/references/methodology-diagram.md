---
capability: methodology-diagram
description: Provides the static CPM Cinematics as Code methodology Excalidraw diagram.
---

# Methodology Diagram

## What Success Looks Like

The user receives an `.excalidraw` JSON file they can import into Excalidraw.com or the VS Code Excalidraw extension — a beautiful, shareable visual that explains the full CPM methodology: the CPLC phases, the Four-Agent Ritual, the State-Diff Gate, and the Handshake Protocol.

## Pre-Built Asset

The CPM methodology diagram is a pre-built asset included with the module at:

```
{skill-root}/assets/cpm-methodology.excalidraw
```

**This is the canonical methodology diagram.** Do not regenerate it from scratch — copy or reference this file.

## Delivery Options

1. **If the user has a CPM production project open:** Copy the diagram to `{project-folder}/Diagrams/cpm-methodology.excalidraw` and confirm the path.

2. **If no project is open:** Output the full path to the pre-built asset and instruct the user to import it directly into Excalidraw.

3. **If the user wants to understand what it shows:** Summarize the diagram's five sections:
   - **Header**: The Vibe-Drift Gap problem and CPM as solution
   - **Production Pipeline**: 8 phases from INCEPTION to OUTPUT with SDLC mapping
   - **Agent Crew**: The 5-agent structure with Orchestrator and specialist grid
   - **Four-Agent Ritual**: Sequential per-shard production loop with State-Diff Gate
   - **Handshake Protocol**: Shard-to-shard continuity validation (3 passes = VALIDATED)

## Import Instructions (provide to user)

> To open in Excalidraw.com: go to excalidraw.com → Load → select the `.excalidraw` file
> To open in VS Code: install the "Excalidraw" extension → open the `.excalidraw` file directly

---
capability: project-orientation
description: Reads production state and presents a situation-aware menu that routes the user to their next right move.
---

# Project Orientation

## What Success Looks Like

The user leaves this capability knowing exactly what to do next and which agent or workflow to use. No ambiguity. The menu presented reflects their actual production state — not a generic list of features.

## Context Signals

Read the following before presenting any options (load whichever are available):

- `.cpm/manifest.md` — context index: which scene is active, which shard is next, what's loaded
- `Production/Slate.md` — scene/shard completion status across the whole project
- `Bible/Show_Bible.md` — exists? (signals foundation work is complete)
- `Architecture/Style_Guide.md` — exists? (signals visual architecture is done)
- `Bible/Characters/_index.md` — exists and populated? (signals character creation done)

## Situation Map

Derive the user's situation from the context signals and route accordingly:

| Situation | Signal | Present These Options |
|---|---|---|
| **No project** | No `.cpm/` folder found | Start with Inception (full guided onboarding) OR New Project (manual setup) |
| **Project exists, no foundation** | No Show Bible or Style Guide | Continue with Show Bible and/or Style Guide workflows |
| **Foundation done, no scenes** | Bible + Style Guide exist, no `Production/Scenes/` | Create first Scene Brief |
| **Scenes exist, ready to generate** | Scene brief exists, entry contract set | Run Shard Generation |
| **Shard in progress** | Exit state from previous shard exists | Run next Shard or Handshake Test |
| **Testing continuity** | Multiple shards complete | Run Handshake Test |
| **General question** | User describes what they want | Route to the right agent (see `references/route-to-agent.md`) |

## Presenting the Menu

Show only options relevant to the user's current situation. Lead with the recommended next step. Explain in one sentence WHY that's the right next step. Never show more than 5 options — if there are more, prioritize by production order.

Format:
```
**Where you are:** [one sentence describing the production state]

**Recommended next:** [specific action + why]

**Other options:**
1. [option] — [reason]
2. [option] — [reason]
...

What would you like to do?
```

## When the User Says "Where Do I Start?"

Walk them through the CPM production lifecycle in sequence:
1. Story Brief → Show Bible
2. Style Guide
3. Character files
4. Scene briefs
5. Shard generation (Four-Agent Ritual)
6. Handshake testing

Ask which stage they're at. If they have existing work, read the project folder to determine it yourself.

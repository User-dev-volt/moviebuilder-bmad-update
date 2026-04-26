---
name: show-bible-plan
version: 1.0.0
created: 2026-02-05
lastValidated: 2026-02-05
---

# Show Bible Workflow Plan

## Purpose

Guide creators through building a comprehensive Show Bible - the foundational document that defines story, characters, world, and thematic pillars for a cinematic production.

## Target User

Filmmakers, showrunners, writers developing a new cinematic project who need to document their creative vision in a structured, enforceable format.

## Output

**Document:** `Bible/Show_Bible.md`
**Template Type:** Structured (required sections, consistent format)

## Step Design

| Step | File | Type | Purpose |
|------|------|------|---------|
| 1 | step-01-init.md | Init | Check for existing Bible, create output file |
| 2 | step-02-hook.md | Middle | Capture the logline (1-sentence hook) |
| 3 | step-03-genre.md | Middle | Define genre, tone, comparable works |
| 4 | step-04-themes.md | Middle | Identify 2-3 thematic pillars |
| 5 | step-05-world.md | Middle | Establish world rules (physics, society, tech) |
| 6 | step-06-arc.md | Middle | Map the 3-act story structure |
| 7 | step-07-motifs.md | Middle | Define recurring visual/narrative motifs |
| 8 | step-08-compile.md | Final | Review, polish, complete |

## Facilitation Approach

- **Role:** Story Architect - collaborative partner, not form filler
- **Style:** Intent-based with open-ended questions
- **Questions:** 1-2 at a time, with inspiring examples
- **Progression:** Abstract to concrete (Hook → Details → Structure)

## State Management

- Output file frontmatter tracks `stepsCompleted`
- Each step appends its number before proceeding
- Supports continuation if interrupted

## Instruction Style

Intent-based for creative domain:
- Open-ended questions that inspire
- Examples that show format without prescribing content
- User controls all creative decisions

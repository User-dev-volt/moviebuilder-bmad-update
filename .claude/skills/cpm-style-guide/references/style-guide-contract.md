# CPM Style Guide Contract

The required content of a production's visual law — the four files written into the project's `Architecture/` folder. Create writes all four; Update revises them without losing precision; Validate grades them against this document. `scripts/check_style.py` enforces the deterministic subset of this contract (files present, required sections present, exact hex codes in the palette, a banned list and a required list in the vocabulary). This document is the human-readable authority and the guide for writing or grading the guide by hand when the script is unavailable. Generated file content uses `{document_output_language}`; all conversation uses `{communication_language}`.

The guiding principle: the visual language serves the story. Every palette color, lighting rule, lens, and banned word should trace back to a theme, tone, or world-rule in the Show Bible. A style guide that reads as generic "good cinematography" has failed — it must encode *this* film's specific look so tightly that a stateless generator reproduces it shard after shard.

## The four files and who consumes them

| File | What it holds | Consumer |
|------|---------------|----------|
| `Style_Guide.md` | The master visual law — identity, lighting, color, camera, spatial rules | Cinematographer (Galadriel), Prompt Engineer |
| `Palette.md` | The agent-facing extract of exact hex codes — allowed, forbidden, and their meanings | Cinematographer |
| `Lens_Language.md` | The agent-facing extract of camera and lens specs | Cinematographer |
| `Vocabulary.md` | The agent-facing extract of banned and required prompt words | Cinematographer, Prompt Engineer |

`Style_Guide.md` is the master; the other three are focused extracts of its color, lens, and vocabulary decisions, kept as separate files because the agents load them just-in-time during shard generation without wanting the whole master in context. The same decisions appear in the master and in their extract — write them once, project them into both.

## Required sections

**`Style_Guide.md`** — the master, carrying at minimum:

- **Visual Identity** — a statement of the film's overall look and the single visual idea that organizes it (the worked reference production names its idea, ties it to a core world-rule, and describes the visual arc across the film).
- **Lighting Protocol** — the lighting regime(s), their characteristics, and explicit rules (what is always done, what is never done). Name motivated sources.
- **Color Palette** — the allowed and forbidden colors with exact hex codes and what each color means in the story.
- **Camera Language** — the lens vocabulary (shot type → focal length → emotional effect), shot progressions, and camera-movement rules including what is forbidden.
- **Spatial Rules** — axis of action, composition rules per subject, and negative-space rules.

**`Palette.md`** — the color extract:

- **Allowed Colors** — a table of named colors, each with an **exact hex code** and its usage context. At least one exact hex code must be present; the bar is that *every* allowed color carries one.
- **Forbidden Colors** — colors that must never appear, each with the reason it is banned (a hex example is encouraged so the rule is unambiguous).
- **Color Meanings** — what each allowed color signifies narratively, so the Cinematographer applies it for meaning, not decoration.

**`Lens_Language.md`** — the camera extract:

- **Lens Vocabulary** — shot type → focal length → emotional effect.
- **Shot Progressions** — named multi-shot sequences and the focal-length arc each follows.
- **Camera Movement Rules** — default movement per act or mode, and an explicit forbidden list.

**`Vocabulary.md`** — the prompt-word extract, and the most enforcement-critical file:

- **Required Substitutions** — the **required list**: vague words mapped to the concrete phrasing that must replace them (e.g. a generic mood word → an exact lighting description with hex codes). Must carry at least one entry.
- **Banned Words** — the **banned list**: words that must never reach a generator, each with the reason it drifts and the alternative to use. Must carry at least one entry.

## The bar, graded at one hardness

The guide is ready only when all of these hold, and each is blocking at the same hardness — never soften one to a warning while hard-gating another:

- All four files present.
- Every required section present in each file.
- **Exact hex codes** in the palette — vague color names ("warm gold", "moody blue") instead of hex codes force a HOLD.
- **A complete banned-word list** — a missing or empty banned list forces a HOLD, with exactly the same weight as missing hex codes.
- A required-substitutions list present and non-empty.
- Substance, judged beyond the structural check: every allowed color carries a hex, every banned word names what it drifts toward, every lens choice serves a stated emotion, and the choices trace to the Show Bible.

When any clause fails, the guide is on HOLD: the Cinematographer cannot enforce a look that is not fully specified, so the guide does not hand off to shard generation until the gap is closed.

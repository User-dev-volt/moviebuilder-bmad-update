---
capability: beat-visual-specs
description: Translates a beat's Showrunner Notes into complete visual architecture — lighting, lens, color, composition, and spatial continuity — producing the Cinematographer Specs the rest of the crew builds on.
---

# Beat Visual Specs

## What Success Looks Like

One beat has a complete visual architecture: every light has a hex code and a placement, the lens is chosen for the emotion, every color is an exact hex code mapped to what it touches, composition and negative space carry meaning, and spatial continuity with the previous shard holds. No banned word survives, and every required term is present. The Style Guide is honored in full. The output is a single artifact: the **Cinematographer Specs**.

## Read First — Every Time

This agent is stateless. You cannot enforce a rule you have not loaded. Before writing a single spec, read fresh from the production project:

- [ ] `Architecture/Style_Guide.md` — the visual law (lighting protocol, composition, spatial rules, lens language)
- [ ] `Architecture/Vocabulary.md` — the banned-word list and the required terms
- [ ] `Architecture/Palette.md` — the exact hex codes you are allowed to use
- [ ] `Production/Scenes/Scene_{XX}/state/shard_{Y}_exit_state.md` — the previous shard's exit state, for spatial continuity (entry direction, axis of action)

Do not spec a beat from memory. The Style Guide is the authority; the Palette is the only source of color.

## Inputs

- The **Showrunner Notes** for the beat — WHAT happens and the emotional truth to land (produced by the Showrunner's Scene Review capability in the `cpm-showrunner` skill, or passed in by the `cpm-shard-generation` workflow)
- The Style Guide, Palette, Vocabulary, and previous exit state (read above)

## Output Format — Cinematographer Specs

Produce exactly this structure:

### Beat {XX}.{Y} Cinematographer Specs

**Lighting Protocol:**
- Primary: {light type} + {hex code} + {placement}
- Secondary: {light type} + {hex code} + {placement}
- Rim: MANDATORY — {light type} + {hex code} + {placement}

**Lens Selection:**
- Lens: {focal length}mm
- Motivation: why this focal length serves the beat's emotion

**Color Application:**
- {hex code}: where it appears / what it touches
- {hex code}: where it appears / what it touches

**Composition:**
- Subject Position: {frame location}
- Background Treatment: {focus depth, elements}
- Negative Space: {percentage}% — {what the emptiness means}

**Spatial Continuity:**
- Entry Direction: frame-{left/right} — motivated by the previous shard's exit state
- Axis of Action: {maintained / crossed} — with the motivation for the choice

**Vocabulary Enforcement:**
- [ ] No banned words present in any spec text above
- Required terms included: {list of required terms from Vocabulary.md}

**Style Compliance:** PASS — every visual honors the Style Guide, every color is an exact hex code, and no banned word appears. / HELD — {the Style Guide rule violated, the vague color name found, or the banned word found}, held for rework. A non-PASS result blocks the two Notes below: do not hand failing specs to the crew.

**Notes to Script Supervisor:** lighting gradients and spatial contracts to track across the handshake.

**Notes to Prompt Engineer:** specific weight emphasis and exact word choices for compilation.

> **Duration:** the beat inherits its shard duration from the Showrunner Notes / the `temporal.default_shard_duration` key in `.cpm/config.yaml` (default 5s; a production may run 15s or 30s, never exceeding `temporal.max_shard_duration`, default 30). For longer shards, choreograph the movement of light and camera across the beat — do not add new beats.

## The Rules

- Define HOW it looks, not WHAT happens. Narrative is the Showrunner's domain — if a beat's story feels wrong, raise it with Albus; do not rewrite it in your specs.
- **Exact hex codes only — never a vague color name.** Every color in the specs is a hex code drawn from `Architecture/Palette.md`. "Warm," "moody," and "golden" are not colors. A spec carrying a vague color name is incomplete and is HELD until the hex code is supplied.
- **The banned-word list is absolute.** A single banned word found in any spec text is a HOLD, not a footnote — replace it with the required term before the specs move downstream.
- **The Rim light is mandatory.** Every beat separates subject from background. A beat with no Rim light is incomplete — supply it before the specs pass.
- **Never approve a beat whose visuals violate the Style Guide.** This is the hard gate of Beat Visual Specs, and it has one hardness for every clause: a Style-Guide violation, a vague color name, and a banned word are each a HELD result — none of them passes downstream with a flag attached. The Notes to Script Supervisor and Notes to Prompt Engineer are written only after **Style Compliance** reads PASS.

Within `cpm-shard-generation`, this gate is enforced by `validation.require_style_compliance` and `validation.banned_words_enforcement` in `.cpm/config.yaml`. Galadriel holds the same line in interactive mode whether or not those keys are set — the standard does not depend on a toggle.

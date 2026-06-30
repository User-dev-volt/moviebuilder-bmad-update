# Inception Draft Contract

The authority for what a *draft* foundation artifact must contain. Inception produces draft foundations fast, from one conversational interview — but a draft is shallow on purpose, never broken. The bar a draft must clear is this: it is **structurally valid against its foundation contract**, so the dedicated workflow can refine it *in place* rather than rebuild it, and it is **honestly marked** as a draft so nothing downstream mistakes it for full-depth canon.

This document is the destination Create drafts toward and the by-hand grading reference for Validate when a sibling check script is unavailable. It carries inception's own copy of each floor so inception stays self-contained — but it never restates a foundation contract; it cites it. Each draft must pass the same deterministic check the dedicated workflow uses:

- Show Bible draft → the Show Bible contract (`cpm-show-bible/references/show-bible-contract.md`), checked by `check_bible.py`.
- Style Guide draft → the Style Guide contract (`cpm-style-guide/references/style-guide-contract.md`), checked by `check_style.py`.
- Character sketch draft → the Character contract (`cpm-character-create/references/character-contract.md`), checked by `check_character.py`.

## The two things every draft owes

1. **Structural validity against its foundation contract.** A draft Bible carries all six required sections with real authored content; a draft Style Guide is all four files with every required section, exact hex, and a non-empty banned list; a draft character pins LEFT/RIGHT and rosters itself. "Draft" lowers the *depth*, never the *structure* — if the dedicated check would hold it, it is not a valid draft.
2. **An honest draft marker plus a refine pointer.** Bible and Style Guide carry frontmatter `status: draft`; a character carries `**Status:** DRAFT`. Each artifact names the workflow that refines it to full depth. The per-artifact native marker is deliberate (the character contract's status field already uses `DRAFT`); the deterministic check accepts each artifact's native form.

## The non-negotiables hold at full hardness — even in a draft

A draft is allowed to be thin. It is **not** allowed to break a continuity-critical rule, because those rules gate shard generation regardless of depth. Graded at one hardness, no softening to a "flag" or "note":

- **Lateral specificity (character).** Every asymmetric immutable feature is pinned LEFT or RIGHT with both sides accounted for, written as the uppercase tokens `LEFT`/`RIGHT`. One side stated and the other left blank holds the sketch exactly as hard as a missing required section. An AI video model mirrors or drifts any unstated side; a one-sided sketch is not continuity-ready even as a draft.
- **Exact hex (palette).** Every allowed color in the draft Palette is an exact `#RRGGBB` code. A vague color name ("warm gold", "moody blue") is a HOLD even in a draft.
- **The banned-word list (vocabulary).** The draft Vocabulary carries a non-empty banned list and a non-empty required-substitutions list. A project's `.cpm/config.yaml` sets `validation.require_style_compliance` and `validation.banned_words_enforcement` (both default true), which hard-gate the Palette and Vocabulary at shard generation no matter the draft status — so these lists are not optional in a draft.

## Draft floor — Show Bible

All six required H2 sections present with at least one real authored line each (so `check_bible.py` passes): Logline, Genre & Tone, Thematic Pillars, World Rules, Story Arc, Recurring Motifs. Minimum substance for each:

- **Logline** — protagonist, central conflict, and the stakes, complete in a sentence or two.
- **Genre & Tone** — the genre, one tonal line, and one comparable work.
- **Thematic Pillars** — two or more pillars, each phrased specifically enough that a scene could be judged to serve it or not.
- **World Rules** — at least one enforceable rule with a consequence (a rule a beat could be checked against, not atmosphere) under at least one lens.
- **Story Arc** — the act spine, with the protagonist's want → need → change legible through it.
- **Recurring Motifs** — at least one motif with where it recurs and what it means.

Honestly shallow / deferred to cpm-show-bible: secondary character arcs, the full world-rule set across every lens, the traced tonal arc, multiple motifs per category.

## Draft floor — Style Guide

Structurally COMPLETE across all four `Architecture/` files, thematically thin — not partial (so `check_style.py` passes):

- **Style_Guide.md** — all five sections (Visual Identity, Lighting Protocol, Color Palette, Camera Language, Spatial Rules); a single lighting regime is acceptable at draft depth.
- **Palette.md** — Allowed Colors with EVERY color an exact hex, at least one Forbidden Color, at least one Color Meaning.
- **Lens_Language.md** — at least one lens row, at least one shot progression, a default and at least one forbidden camera movement.
- **Vocabulary.md** — at least one required substitution and a banned list seeded with the universal AI-video offenders (cinematic, epic, beautiful, dramatic lighting) plus any story-specific bans from the interview.

Honestly shallow / deferred to cpm-style-guide: the full motivated-source lighting taxonomy, per-act movement progressions, the exhaustive banned list, negative-space subtleties.

## Draft floor — character sketch

Passes `check_character.py`: the load-bearing header, the required sections, the LEFT/RIGHT anchor on both sides, and a roster row. Minimum substance:

- **Header** — the `# Character: {Name}` H1, `**Asset ID:** {NAME}_V1`, `**Status:** DRAFT`.
- **Visual Identity (Immutable)** — `### Face` with anchored Distinguishing Features (the laterality non-negotiable above), an Expression Default, and an Age Appearance; `### Body` with Build, Posture, and Movement Style.
- **The remaining required sections** — Current Outfit, Inventory, Physical State, Behavioral Profile, Arc Position (want and need at minimum), Version History (the V1 row).
- **Roster** — one `**{Name}**` row appended to `Bible/Characters/_index.md`.

Protagonist mandatory; one or two named others if the interview surfaced them. Honestly shallow / deferred to cpm-character-create: full inventory and physical-state tracking, signature moves, the exhaustive behavioral profile, the secondary cast.

## What "ready to refine" means, in one line

A draft is ready when its dedicated workflow could open it and *deepen* it without first having to *repair* it. A draft that would fail its own foundation check is not a draft — it is a gap wearing a draft label, and Validate holds the whole foundation until it is fixed.

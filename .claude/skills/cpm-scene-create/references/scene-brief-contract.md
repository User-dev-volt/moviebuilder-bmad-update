# CPM Scene Brief Contract

The required shape of a scene brief — the filmmaker-directed definition of every beat in a scene,
authored up front, before any shard is generated. Each beat is the pre-commitment for exactly one
shard. Create writes this in full; Update changes beats while keeping the layers in sync; Validate
grades a brief against it. `scripts/validate_scene_brief.py` enforces the structural clauses
deterministically — this document is the human-readable authority and the guide for grading by
hand when the script is unavailable. It teaches the method so it generalizes to any production; the
examples are illustrations, not fixed content.

Two readers depend on this shape. The Showrunner reads the whole Beat Table to review the scene and
emits a beat breakdown with the same four columns — zero transformation. The production loop that
generates each shard extracts the current beat by integer: it resolves `currentBeat =
currentShardNumber` and pulls the one Beat Table row whose Beat equals that number, plus the
matching detail block. Because every beat is pre-authored with a single non-negotiable, the
Showrunner *loads* a beat instead of *inventing* one — which is the whole reason this brief exists.

## The non-negotiable: the four-way equality

The integer lookup is only deterministic if four counts agree:

> `shard_count == Beat-Table rows == Beat-Detail blocks == max(Beat)`

and the Beat column is **contiguous integers `1..shard_count`, exactly one row per integer**. Beat
N is Shard N — a one-to-one mapping. If any of the four counts disagrees, or a beat number is
skipped, repeated, or out of range, the lookup is no longer a pure integer key and the brief is
held, not shipped. This is the single most load-bearing rule in the file; the script checks it
first.

Duration (5s / 15s / 30s) scales the choreography *inside* a single shard — more micro-beats packed
into a 15s or 30s shard — but it never changes the one-beat-one-shard mapping. A beat never spans
two shards.

## The two-layer Beats design

The `## Beats` section carries two layers, and both are required:

- **`### Beat Table`** — the authoritative, machine-read index. This is what makes extraction
  deterministic.
- **`### Beat Details`** — the prose filmmaker direction, one block per beat. This is what makes the
  scene worth filming.

They are kept 1:1 by integer. The details **do not restate** Duration or Primary Requirement — the
table owns those. Two sources for the same fact is how drift starts; the table is the single source
for the machine-read fields.

## The Beat Table

Columns are **exactly** `Beat | Duration | Focus | Primary Requirement` — no more, no fewer, this
order. The order and names are the Showrunner's read/emit contract, so the choice is not arbitrary.

- **Beat** — the integer join key. Contiguous `1..shard_count`, one row each.
- **Duration** — target seconds for that beat's shard, one of `5s`, `15s`, `30s`. Defaults to
  `default_shard_duration`; may be overridden per beat.
- **Focus** — the subject of attention plus framing (which character or asset, and the lens). The
  character named here must be one of the `on_camera_characters`. Name the character; never redefine
  their immutable identity — that lives in the character file.
- **Primary Requirement** — the single non-negotiable that beat must deliver. This is the field the
  Showrunner would otherwise invent; pre-authoring it here is the point. See the anti-vagueness gate
  below.

## Beat Details

One block per beat, headed `#### Beat {N} — {Title}` and keyed by the same integer as the table.
Fields:

| Field | Required | Definition |
|-------|----------|------------|
| **Action** | Yes | The staged physical action — the meat of the shard. |
| **Emotional Note** | Yes | The emotional state or shift the beat carries. |
| **Shot** | Recommended | Fuller camera spec — lens, movement, framing — beyond the table's Focus. |
| **Continuity In** | Beat 1: yes (carry-in per `state/entry_contract.md`); else optional | The carry-in state this beat assumes. |
| **State Change** | Optional | What this beat changes — condition flags, inventory, arc-% delta — feeding the exit state authored downstream. |

## The anti-vagueness gate

A Primary Requirement is only useful if it can be checked. Every one **must name at least one
concrete checkable element**: a hex code (`#5B8DD9`), a lens (`85mm`), a LEFT/RIGHT designation, a
named prop (the repossession order), or a condition flag (`ACUTE_JAW_TENSION`). "He looks cold and
controlled" cannot be verified and is held; "RIGHT gloved index taps the glass once; smartwatch
countdown visible on LEFT wrist" can. Treat this at the same hardness as any structural failure —
there is no "flag the vague requirement and proceed." The script confirms each Primary Requirement
is present and non-empty; whether the named element is genuinely concrete is a judgment the
reviewer makes by reading it.

## Reference, don't duplicate

The brief references characters by name and **never restates immutable visual identity** — a scar,
a hair part, a build. Those live solely in `Bible/Characters/{Name}.md`. A Primary Requirement may
*reference* such a feature as a checkable item ("RIGHT jawline scar must read") but must not
redefine it. This keeps the character file the single source of truth and prevents the two files
from drifting apart.

## Frontmatter

The brief carries exactly these fields — and not the workflow's own bookkeeping (resume lives in
the memlog beside the brief, never in the shipped artifact):

- **scene_number** — a string, zero-padded to two digits (`'01'`).
- **scene_id** — must equal `"SCENE_" + scene_number` (`'SCENE_01'`). This is a law the script
  enforces.
- **scene_title** — the human title.
- **status** — the production status of the scene: `ready` on finalize, then `in-progress` and
  `complete` as shards are generated downstream. A finished brief whose shards are not yet generated
  is `ready`.
- **shard_count** — an integer, equal to the beat count (see the four-way equality).
- **default_shard_duration** — seconds, inherited from the project config; per-beat overrides live
  in the Beat Table.
- **on_camera_characters** — a list of **plain names** (`Elias`, not `ELIAS_V1`). Each must resolve
  to `Bible/Characters/{Name}.md`. The asset ID is captured in the entry contract, not here.
- **arc_position** — where the scene sits in the overall arc.
- **created** / **lastModified** — dates.

## The side artifacts

Finalizing a brief is not finished until three companions are written; Validate checks all three:

- **`state/entry_contract.md`** (beside the brief) — seeds Shard 1's carry-in. For Scene 01 it is
  derived from the characters' initial state. For a later scene it is seeded from the prior scene's
  last exit state when that exists; when it does not, it is written as an **explicit gap stub**
  (`unresolved — Script Supervisor fills before Shard 1`) rather than a silent hollow handoff.
  Validate flags that stub as a **warning, never a hold**.
- **The manifest Scenes registry** — a `## Scene {XX}` block under the Scenes marker, plus the
  `Scenes defined` project-status checkbox once at least one scene exists. The brief writes only
  that block; it never touches the live Active Scene Context.
- **The Slate** — a row in the Scenes status table and a Production Log line on finalize.

## What the script enforces vs what is judged by hand

The script owns the deterministic structure: frontmatter identity (`scene_id` law, two-digit
`scene_number`), the four-way equality, the contiguous Beat column, the exact four columns, the
table-to-detail 1:1 mapping, character-file resolution, the side artifacts, and the deterministic
halves of beat quality (Duration is 5/15/30, Focus non-empty, Action present). What stays a reading
judgment: whether each Primary Requirement names a genuinely concrete element, whether the Narrative
Purpose names a real theme, and whether the Emotional Arc's opening and closing states earn the
change. Structure is held in code; substance is graded by the reviewer.

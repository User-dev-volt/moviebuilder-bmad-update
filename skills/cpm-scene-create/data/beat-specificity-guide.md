# Beat Specificity Guide

> Loaded while authoring, polishing, and validating a scene brief. It teaches the one
> standard every beat must clear: a **Primary Requirement** concrete enough that the next pair
> of eyes — the Script Supervisor checking the finished shard, the Prompt Engineer front-loading
> it — can confirm it landed without guessing. Vague beats are the failure this whole brief
> exists to prevent. The examples below are drawn from *The Second Receipt* to show the method;
> your own production's hex codes, props, and characters go in their place.

---

## The single test

A **Primary Requirement** is the one non-negotiable a beat must deliver — the thing you would
reject the finished shard for missing, no matter how good the rest looks. There is exactly one
per beat, and it has to be **checkable**:

> Could the Script Supervisor look at the generated frame and return a clean yes/no — and would
> two reviewers reach the same verdict?

If the answer is yes, the requirement is concrete. If two careful people could disagree about
whether it was met — "is that *cold* enough? is that *tense* enough?" — it is vague, and it
fails. A mood is not a requirement. A mood is what the beat should *feel* like; the requirement
is what must be *on screen* for that feeling to exist.

---

## What makes a requirement concrete

A Primary Requirement is concrete when it names **at least one** of these five checkable
elements. Most strong beats name two or three, bundled into a single demand.

| Element | What it pins down | Grounded illustration | Why it checks |
|---|---|---|---|
| **A hex code** | The exact color, in a named place | Harsh `#5B8DD9` Tablet Blue uplight on Elias's face; `#F0C04A` Legacy Gold flooding the corridor full-face | Either that exact value is in that place, or it isn't — no "kind of blue" |
| **A lens / focal length** | The framing and its compression | 85mm clinical close-up; 100mm extreme close-up on hands; 24mm wide for the march | The lens language carries the meaning; the wrong focal length is the wrong shot |
| **A LEFT / RIGHT designation** | Which hand, wrist, or side | RIGHT gloved index taps the glass; smartwatch on the LEFT wrist; RIGHT thumb traces the LEFT glove seam | Mirror flips are the single most common continuity break in generated video — pin the side every time |
| **A named prop** | Which object, in which hand, in what condition | The repossession order (`#F0F4F8`, pristine, RIGHT hand); the flannel dusting cloth in Mara's LEFT hand; the tea service already set | "A piece of paper" is not the repossession order; name it, place it, state its condition |
| **A condition flag** | A documented physical state and its visible signature | `ACUTE_JAW_TENSION` active; `DEEP_DIAPHRAGMATIC_BREATHING` visible; the Boundary Check initiating | The flag's on-screen signature is defined in the character file, so the check is exact, not impressionistic |

**Reference, never redefine.** A requirement may *point at* a character's immutable feature as
a checkable item — "the RIGHT-jawline scar must read" — but it must never restate what that
feature is. The scar's geometry (faint crescent, half-inch, aged white) lives in the character
file and nowhere else. Naming it here keeps the brief honest; redefining it here invites two
sources of truth to drift apart.

---

## Vague to concrete

Each rewrite below keeps the *intent* of the vague version and makes it checkable. Read the
"why it passes" line — that is the move you are learning, not the specific content.

**The opening expression.**
- Vague: *Elias looks cold and detached.*
- Concrete: *Functional Ghost expression locked (jaw clenched, mouth a firm horizontal line);
  harsh `#5B8DD9` Tablet Blue uplight from below; a single precise RIGHT-hand swipe; no blink.*
- Why it passes: a condition (the locked expression), a hex (`#5B8DD9`) in a named place, and a
  RIGHT-hand action — three things a reviewer can confirm frame by frame.

**Silencing the call.**
- Vague: *He shuts the voice up.*
- Concrete: *Smartwatch countdown visible on the LEFT wrist; RIGHT gloved index taps the glass
  once, cutting the voice mid-sentence; returns to symmetrical stillness.*
- Why it passes: a named prop on a named side, a single counted action, a defined end-state —
  no ambiguity about which hand or how many taps.

**Squaring the paper.**
- Vague: *He neatly straightens the document.*
- Concrete: *Repossession paper (`#F0F4F8`) squared to a perfect 90° against the tablet edge
  with the rigid RIGHT index finger; a single jaw twitch at alignment.*
- Why it passes: "neatly" is a feeling; "90° against the tablet edge with the RIGHT index" is a
  geometry a reviewer can measure against the frame.

**The warm welcome.**
- Vague: *Mara greets him warmly and kindly.*
- Concrete: *Warm `#F0C04A` Legacy Gold floods the corridor and hits Elias full-face; her RIGHT
  hand performs the Conducted Invitation arc from her heart outward; `DEEP_DIAPHRAGMATIC_BREATHING`
  visible; the piano reads over her LEFT shoulder.*
- Why it passes: "warmly" becomes an exact color event, a named gesture on a named hand, a
  visible condition flag, and a specific background element.

**The first crack.**
- Vague: *He starts to lose his composure a little.*
- Concrete: *RIGHT thumb presses the LEFT glove seam — the Boundary Check at low intensity, for
  the first time; all three cold conditions still active (`ACUTE_JAW_TENSION`,
  `RESTRICTED_BREATHING`, `THERMAL_RIGIDITY`); the `#5B8DD9` tablet uplight now sharing the frame
  with `#F0C04A`.*
- Why it passes: an internal shift becomes one observable gesture on a named side plus a precise
  light event — the crack is *shown*, not asserted.

---

## Anti-patterns to catch in polish

- **The mood label** — "looks menacing," "feels warm," "seems tense." Names a feeling, names no
  element. Ask what must be on screen for that feeling to exist, and require *that*.
- **The color hedge** — "some kind of blue light," "a warm glow." A color family is not a hex.
  Pull it to the exact value from the palette.
- **The floating hand** — "he gestures," "she reaches out." No side named, so the generator is
  free to flip it. Pin LEFT or RIGHT.
- **The unnamed object** — "a piece of paper," "his device." Which prop, in which hand, in what
  condition? Name it.
- **The redefinition** — restating a scar, a hair part, or a build that already lives in the
  character file. Reference it as checkable; do not author it twice.
- **The everything-beat** — three separate demands fighting to be the one non-negotiable. Pick
  the load-bearing one; the rest belong in the Action prose or in a second beat.

---

## Duration calibration — 5s, 15s, 30s

**One beat is always one shard.** Duration does not change that. A longer Duration does not add
shards; it gives that single shard more screen-time, and therefore room for more choreography
*inside* it. Beat N is Shard N at every interval — that is what lets the production loop pull the
right beat by its number alone. Duration is the **choreography budget** for the one shard: pick
the smallest interval the beat's action fits cleanly into.

| Duration | What fits inside the one shard | Shape | Grounded illustration |
|---|---|---|---|
| **5s** | A single discrete action — one gesture, one expression lock, one continuous move. No internal reversal. | One micro-beat | Every beat of *The Functional Ghost*: the swipe; the single tap; the square-and-knock. Six 5s beats make a tight 30-second scene. |
| **15s** | A short chained sequence — two or three linked micro-beats with a clear beginning, middle, and end. One staging change. | A gesture-chain | A closed door opens → warm light floods Elias full-face → Mara's Conducted Invitation arc → she holds, not yet stepping aside. |
| **30s** | A full staged exchange — several micro-beats including a turn or reversal, with room for a spoken line and a held reaction. This is the ceiling. | A small scene inside the shard | A name spoken → one second of system-error stillness → the threshold crossing → two light sources coexisting → the Boundary Check initiating. |

**Match the budget to the content, both directions.**

- **Don't overstuff a 5s beat.** Three reversals crammed into five seconds will not play — the
  generator drops or blurs them. If a beat contains two genuinely separable turns, it is two
  beats. Split it; the shard count rises by one, and each half gets its own clean shard.
- **Don't pad a 30s beat.** A single gesture stretched to thirty seconds forces the generator to
  invent filler to fill the time, and invented filler is exactly the drift this brief prevents.
  If the action is one clean move, give it 5s.
- **30s is the ceiling.** A beat that genuinely needs more than thirty seconds to play is not one
  beat — it is a short sequence wearing a single number. Break it into contiguous beats so every
  shard stays inside the budget.

The default Duration is inherited from the project's configuration and can be overridden per
beat. Set it honestly against what the beat actually contains: the Prompt Engineer stages
micro-beats to fill it, and the Script Supervisor budgets continuity against it. A dishonest
Duration mis-briefs both.

---

## Quick checklist for every beat

- [ ] The Primary Requirement names at least one of: a hex, a lens, a LEFT/RIGHT side, a named
  prop, or a condition flag.
- [ ] It states **one** non-negotiable — the thing you would reject the shard for.
- [ ] Two reviewers would agree on whether it was met.
- [ ] It references immutable character features rather than redefining them.
- [ ] The Duration matches how much choreography the beat actually contains — no overstuffing, no
  padding, nothing over 30s.

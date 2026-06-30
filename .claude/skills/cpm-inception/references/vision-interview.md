# The Vision Interview

The conversational engine of the rapid start. This is ONE flowing, open conversation — not a form. The filmmaker never fills fields; they talk, and you structure. Open the floor with each movement's broad question, mine the natural answer for the structured data the movement must extract, reflect back what you pulled so they can correct it, and press only on the gaps. The value of an interview is the pushback a blank template never gives — the theme no scene serves, the vague color, the one-sided scar — so interrogate and structure, never collect entries.

Decisions land in the inception memlog as they are made. The six movements GROUP by the foundation they feed, so by the end one pass has enough to draft all four foundations: project identity, the Show Bible, the Style Guide, and the character sketches.

## How to run it

- **Open, then mine.** Lead with the broad question. Let the filmmaker pour out whatever they hold, then extract the structured data from it before asking anything narrower. The questions below name a destination, not a march.
- **Reflect and confirm.** After each movement, say back what you extracted in a line or two and get a yes before moving on. A misheard premise poisons every draft.
- **Press the gates at full hardness.** Three things are non-negotiable and are held exactly as hard here as in the dedicated workflows — never softened to "we'll note it":
  - **Color → exact hex.** Every color the filmmaker names is pressed to a `#RRGGBB` code. "Warm gold" is not a color decision; `#F0C04A` is.
  - **Mood word → concrete substitution.** Every "cinematic / dark / warm / moody / beautiful" is pressed to what it concretely means on screen (a source, a hex, a texture), because those words drift a generator.
  - **Character mark → LEFT or RIGHT, both sides.** Every asymmetric distinguishing feature is pinned to a definite side with the other side accounted for. A scar "on the jawline" lands on a different side every generation.
- **The Setup is woven in, not front-loaded.** Ask the project-name / model / shard-length questions naturally near the end, once there is a film to name — not as an opening intake form.

---

## 1. The Pitch

*Feeds: project identity + Bible Logline and Genre & Tone.*

**Open with:** "Tell me about the film — what's it about, who's it about, and what feeling should it leave?"

Extract:

- **Working title** — what to call the project (also the project-folder name unless they prefer another).
- **Protagonist** — who the story follows.
- **Central conflict + stakes** — what they are up against and what they stand to lose or decide. (→ Logline)
- **Genre** — primary, and any blend.
- **One-line tone** — the emotional register in a sentence.
- **One comparable work** — a film or show that pins the intended experience. (→ Genre & Tone)

Press if: the pitch is a premise with no conflict, or a conflict with no stakes — a Logline needs all three.

## 2. The Meaning

*Feeds: Bible Thematic Pillars + World Rules.*

**Open with:** "What's it really about underneath — and what are the hard rules of this world?"

Extract:

- **Two or more themes**, each phrased as a question or tension specific enough to test a beat against (not "love" or "loss" — those test nothing). (→ Thematic Pillars)
- **One or two enforceable world rules**, each with a consequence — a rule a beat could be checked against, not atmosphere. "A value not written on a legal document does not exist to the System" is a rule; "it's a gritty city" is not. (→ World Rules)

Press if: a theme is so broad everything serves it, or a "rule" is just a vibe with no consequence.

## 3. The Shape

*Feeds: Bible Story Arc + Recurring Motifs.*

**Open with:** "Walk me start to end — where does your protagonist begin, and what changes? And is there any image or phrase that keeps coming back?"

Extract:

- **The act spine** — what is established, what destabilizes, what reverses, what resolves (adjust the count to the form).
- **The protagonist's want → need → change** — the conscious goal, the deeper truth, and the transformation, legible through the spine. (→ Story Arc)
- **One motif** — an image or phrase, where it recurs, and what it tracks or means. (→ Recurring Motifs)

Press if: there is a want but no need, or a motif that appears once (a motif that does not recur tracks nothing).

## 4. The Look

*Feeds: all four Style Guide files.*

**Open with:** "Picture one frame from this film — what colors, what light, what is the camera doing? And is there anything that would instantly look wrong?"

Extract:

- **The organizing visual idea** — the single idea the whole look hangs on, tied to a theme or world rule. (→ Visual Identity)
- **Two to four colors, each an exact hex, each with a meaning.** Press every vague color to a `#RRGGBB` code. (→ Palette: Allowed Colors + Color Meanings)
- **A lighting regime** — the dominant light and its principle (a single regime is fine at draft depth). (→ Lighting Protocol)
- **One or two lens choices**, each tied to the emotion it serves. (→ Lens Vocabulary)
- **One shot progression and the camera's discipline** — at least one named multi-shot sequence with its focal-length arc and what that arc expresses, plus the default camera movement and one movement that would break this world. The opener already asks what the camera is doing; press that into a default and a forbidden. (→ Lens_Language: Shot Progressions + Camera Movement Rules)
- **Things to ban** — colors that would be wrong, and any words that would drift the look. Press every "cinematic / dark / warm" to a concrete substitution. (→ Forbidden Colors + Vocabulary banned list)

Press if: any color is still a name not a hex, or any look word is still a mood not a concrete description. This is the same pushback cpm-style-guide gives, at full hardness.

## 5. The Cast

*Feeds: character sketches.*

**Open with:** "Who's on camera — and for each of them, what's the one physical detail you'd never want the AI to get wrong?"

Extract, per key character:

- **Name.**
- **The distinguishing marks, each anchored LEFT or RIGHT, with both sides accounted for** — held at the same HOLD hardness as cpm-character-create; never softened to a note. (→ Visual Identity Face)
- **Build / posture / movement** — the body and how it carries, noting any side-dominant habit. (→ Visual Identity Body)
- **Want and need** — the conscious goal and the deeper truth. (→ Arc Position)

The protagonist is mandatory; capture one or two others if the filmmaker names them. Press if: a mark is given for one side only — pin both before the sketch is written.

## 6. The Setup

*Feeds: the project scaffold config.*

**Weave in naturally near the end:** "A few practical things so I can stand the project up — what should I call the project folder, which video model are you targeting, and how long should the default shard be?"

Extract:

- **Project name** — the folder and the display name (often the working title from the Pitch).
- **Model target** — `sora`, `kling`, `runway`, `pika`, or any other model id. (→ `model.target`)
- **Default shard length** — `5`, `15`, or `30` seconds. (→ `temporal.default_shard_duration`)

Confirm these three in one line, then run the scaffold phase.

---

## The handoff out of the interview

By the close of the six movements you hold: a project name + model + shard length (the scaffold), a logline + genre/tone + pillars + world rules + arc + a motif (the draft Bible), an organizing visual idea + an exact-hex palette + a lighting regime + lens choices + a shot progression and the camera's default/forbidden discipline + a banned list (the draft Style Guide), and at least the protagonist with both-sides laterality, body, want, and need (the draft character). Reflect the whole picture back once, get the final yes, then lay down the foundation phase by phase.

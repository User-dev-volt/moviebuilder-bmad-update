# Show Bible Contract

The Show Bible is the narrative DNA of a cinematic production — the canon, the equivalent of a product requirements document for a film. Everything downstream treats it as law: the Showrunner (Albus) guards it and measures every proposed beat against it, and the Style Guide, characters, scenes, and shards all inherit from it. A Bible with a missing or hollow section cannot be guarded — the guardian has nothing to check against — so the bar is absolute and symmetric: **every required section below is present and substantively complete, at the same hardness. None is optional, and none may be downgraded to a soft suggestion while another is enforced.**

`scripts/check_bible.py` enforces the structural half of this contract deterministically (each required section present and non-empty). This document is the human-readable authority for what each section *is* and what makes it *complete* — the substance that the structural check cannot see and that a reviewer must judge. Load it in create (the destination you author toward), in refine (the bar a change must still clear), and in validate (the standard you grade against).

This teaches the method so it generalizes to any production; it is not a fill-in-the-blanks form, and the depth — not a particular story's answers — is what makes a Bible complete.

## Required sections

### Logline
One or two sentences that hold the whole story in a breath: the protagonist, the central conflict, and the irreversible choice or the stakes at its heart. Complete when a reader who knows nothing else can name who the story is about, what they are up against, and what they stand to lose or decide. A premise without a conflict, or a conflict without stakes, is draft-thin.

### Genre & Tone
The genre (primary, and any blend) and the tone — the emotional register and, crucially, how it moves across the piece rather than a single adjective. Comparable works pin it down by reference. Complete when a new collaborator could feel the intended experience: the genre named, the tonal arc described (where it starts, where it travels), and at least one comparison that sharpens it. "It's a drama" is not a tone.

### Thematic Pillars
The load-bearing themes the story is actually about — typically two to four, each a named pillar plus the question or tension it forces the story to keep asking. These are the test the Showrunner applies to every beat. Complete when each pillar is specific enough that a scene could be judged to serve it or not; a pillar so broad that everything serves it ("love", "loss") tests nothing and is not complete.

### World Rules
The laws of this world that constrain what can and cannot happen — the rules a downstream agent could actually check a beat against, not atmosphere. The proven cut organizes these as Physics (the literal/sensory laws, including any single permitted unreality), Society (how the world's institutions and values operate), and Technology (the tools and what they mean), but the lens may be renamed or replaced to fit the world. Complete when the governing rules are articulated as enforceable constraints with consequences, not vibes; "it's a gritty city" is not a world rule, "a value not written on a legal document does not exist to the System" is.

### Story Arc
How the narrative *and the principal characters' arcs* move across the piece — the act or movement structure (adjust the count to the form), where each block names what is established, what destabilizes, what reverses, and what resolves. This is where character arcs live at narrative-DNA level: for each principal, the want (the conscious goal) and the need (the deeper truth they must reach) traced through the structure to the transformation. Complete when the spine is unbroken (each act follows from the last), the climax is identifiable, and at least the protagonist's want→need→change is legible through the structure. The detailed, mutable character state files belong to the character workflow, not here — but the roster and arcs must be present here.

### Recurring Motifs
The images, phrases, and colors threaded deliberately through the piece, each recurring on purpose and carrying meaning — not decoration. The proven cut separates Visual motifs, Dialogue motifs, and Color motifs; name each motif, where it recurs, and what it tracks or means. (Exact hex values are the Style Guide's domain, not the Bible's — name colors by their narrative meaning here.) Complete when each listed motif recurs at least twice and its meaning is stated; a motif that appears once tracks nothing and does not belong.

## What "complete" means, in one line

A section is complete when the Showrunner could *use* it to accept or reject a beat. A section that only describes is draft-thin; a section that *constrains* is done. Validate holds the Bible the moment any required section is missing, structurally empty, or present but draft-thin — and the hold blocks the handoff to the Showrunner and to every production workflow until it is resolved.

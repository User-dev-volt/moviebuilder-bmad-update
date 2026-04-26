# Prompt Structure Template

## Standard CPM Prompt Format

Every compiled prompt MUST follow this exact structure. The Prompt Engineer compiles inputs from Showrunner, Cinematographer, and Script Supervisor into this format.

## Structure

```
[ID: SCENE_{XX}.{Y}_{BEAT_NAME}]

[Technical Header]:
{lens}mm {shot_type}, {fps}fps, {lighting_style}, {atmosphere_keywords}.

[Subject/Asset]:
{CRITICAL FEATURES FIRST — scar, distinguishing marks, LEFT/RIGHT specificity}
{Character description with current state from Bible file}
{Outfit with current condition from mutable state}

[Action/State]:
{What the character is DOING — from Showrunner's beat notes}
{How they are moving/positioned — from Script Supervisor's state}
{What they are holding/wearing — from Script Supervisor's injections}

[Environment/Lighting]:
{Lighting description with HEX CODES — from Cinematographer's specs}
{Background elements — from Cinematographer's composition}
{Atmospheric conditions — from Style Guide compliance}

[Temporal Constraint]:
{Duration} seconds. {Movement/pacing description}. {EXIT STATE HOOK — how the shard ends, from Script Supervisor's handshake}.
```

## Compilation Rules

### Attention Window (First 25%)
The first quarter of the prompt receives maximum AI attention. Place here:
1. Critical distinguishing features (scars, marks — with LEFT/RIGHT)
2. Character identity anchors
3. Key emotional state
4. Any state that MUST NOT drift

### Vocabulary Compliance
- Check ALL text against `Architecture/Vocabulary.md`
- Replace ANY banned word with its required alternative
- Document all substitutions in Build Notes

### Build Notes (Appended After Prompt)
```
**Build Notes:**
- Anchor Points: {What's in first 25%}
- Vocabulary Compliance: {Banned words avoided: list}
- Exit Hook: {Exact handshake text from Script Supervisor}
- Injections Applied: {State injections from Script Supervisor}
- Source Agents: Showrunner → Cinematographer → Script Supervisor → Prompt Engineer
```

## Anti-Patterns

- ❌ NEVER compile without all three agent inputs
- ❌ NEVER use vague color descriptions (always hex codes)
- ❌ NEVER omit the exit state hook
- ❌ NEVER place critical features after the 25% mark
- ❌ NEVER use banned vocabulary words

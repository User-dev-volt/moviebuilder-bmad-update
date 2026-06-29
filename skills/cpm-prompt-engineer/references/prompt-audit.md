---
capability: prompt-audit
description: Reviews an existing draft prompt for compliance — critical-feature anchoring, vocabulary, exit hook, state injections, and visual fidelity — returning a pass/fix report.
---

# Prompt Audit

## What Success Looks Like

A draft prompt is graded against the things that make a CPM prompt safe to send to the generator: critical features in the first 25%, no banned words, an exit-state hook, the Script Supervisor's injected state present, and lens/lighting/color matching the Style Guide. Every line of the report is either PASS or a specific, actionable fix. A prompt that fails the audit does not ship until the fixes are made.

## Read First — Every Time

This agent is stateless. You cannot audit compliance against a document you have not loaded. Before auditing, read fresh:

- [ ] The draft prompt under review
- [ ] the **Script Supervisor validation** that accompanies the prompt (its State Check + Injections Required) — the authority for what state SHOULD be present, so the Injections check has something to verify against
- [ ] `Architecture/Style_Guide.md` — the visual law the prompt must honor (lens, lighting, composition, hex palette)
- [ ] `Architecture/Vocabulary.md` — the banned/required word list (banned-word enforcement is set by `validation.banned_words_enforcement` in `.cpm/config.yaml`)

The audit checks whether the prompt honors what the crew already decided. It is not a redesign — Leonard does not overrule the Showrunner, Cinematographer, or Script Supervisor.

## How to Audit

Grade each check PASS, or give the specific fix:

- **Anchor Points** — are the critical features (scars, wounds, distinctive marks) inside the first 25% of the prompt? PASS, or: move {feature} up into the opening lines of `[Subject/Asset]`.
- **Vocabulary** — does any banned word appear? PASS, or: replace {banned word} with {required alternative} from `Architecture/Vocabulary.md`.
- **Exit Hook** — does `[Temporal Constraint]` end on an exit-state hook? PASS, or: add the handshake text describing how the shard ends.
- **Injections** — is the Script Supervisor's state present (current outfit condition, wounds, inventory)? PASS, or: inject {missing state}.
- **Visual Compliance** — do lens / lighting / hex values match the Style Guide? PASS, or: correct {value} to the Style Guide's {spec}.

## Output — Compliance Report

### Prompt Audit — Scene {XX} Shard {YY}

| Check | Result |
|---|---|
| Anchor Points (critical features in first 25%) | PASS / FIX: {specific fix} |
| Vocabulary (no banned words) | PASS / FIX: {word} → {required alternative} |
| Exit Hook (present) | PASS / FIX: {add hook text} |
| Injections (Script Supervisor state present) | PASS / FIX: {inject state} |
| Visual Compliance (matches Style Guide) | PASS / FIX: {correction} |

**Verdict:** PASS — clear to ship. / FAIL — {n} fixes required; the prompt does not ship until they are made.

A FAIL verdict blocks the prompt — it returns to compilation for rework before any handoff or render.

## The Rule

The audit is a compliance check, not a redesign. Leonard verifies the prompt honors the crew's decisions — he does not overrule the Showrunner, Cinematographer, or Script Supervisor. A failing prompt is sent back with specific, named fixes; it does not ship until every check reads PASS.

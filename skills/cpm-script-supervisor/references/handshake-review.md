---
capability: handshake-review
description: Verifies that the current shard honors the Entry Contract handed to it by the previous shard's exit state, returning a binding pass/fail that blocks compilation on failure.
---

# Handshake Review

## What Success Looks Like

The current shard honors the Entry Contract the previous shard handed it: every "must start with" condition is met and nothing on the "must NOT show" list appears. The output is a binding PASS or FAIL — and a FAIL blocks compilation until the handshake is reconciled.

## Read First — Every Time

This agent is stateless. You cannot verify a contract you have not loaded. Before reviewing, read fresh from the production project:

- [ ] the previous shard's exit state — `Production/Scenes/Scene_{XX}/state/shard_{Y-1}_exit_state.md` — specifically its **Entry Contract** for this shard (Must start with / Must NOT show)
- [ ] the current shard's inputs — the Showrunner Notes and Cinematographer Specs (and the draft prompt, if one exists)
- [ ] when this is the scene's first shard, the previous scene's final exit state — `Production/Scenes/Scene_{XX-1}/state/` (the last shard's `exit_state.md`) — which carries the inherited contract

## What a Handshake Is

A handshake is the contract between two adjacent shards. Shard `{Y-1}`'s exit state defines the Entry Contract for shard `{Y}`: where it must open (position, facing, expression) and what it must not show (anything that would break continuity). Reviewing the handshake means checking the current shard against the contract it inherited — not re-deriving it.

## Output Format — Handshake Review

### Shard {XX}.{Y} Handshake Review

**Inherited Entry Contract (from Shard {XX}.{Y-1} exit state):**
- Must start with: {position, facing, expression}
- Must NOT show: {continuity-breaking content}

**Verification:**

| Contract Term | Honored? | Notes |
|---|---|---|
| Must start with: {…} | ✓ / ✗ | {what the current shard actually opens on} |
| Must NOT show: {…} | ✓ / ✗ | {present or absent in the current shard} |

**Status:** PASS / FAIL

- **PASS** — every "must start with" term met, nothing from "must NOT show" present. Continuity holds; proceed.
- **FAIL** — one or more contract terms broken. **A FAIL blocks compilation** — the shard does not proceed to the Prompt Engineer until the handshake is reconciled.

**If FAIL — Violations:** (enumerate every broken term and its fix — nothing proceeds while this list is non-empty)

- {contract term}: {how the current shard breaks it} → {what must change to honor the contract}

## The Rule

The Entry Contract is binding. **Never pass a shard whose opening contradicts the Entry Contract it inherited** — a broken handshake is the exact discontinuity this review exists to catch, and it carries the same hardness as any state violation. Enumerate every broken term; do not wave a single one through with a note attached.

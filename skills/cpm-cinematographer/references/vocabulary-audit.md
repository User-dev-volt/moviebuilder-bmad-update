---
capability: vocabulary-audit
description: Scans a draft prompt for banned words and missing required terms, returning every violation with its required replacement and an unambiguous PASS or HOLD.
---

# Vocabulary Audit

## What Success Looks Like

A draft prompt is scanned against the project's Vocabulary. Every banned word is found and paired with its required replacement, every missing required term is named, and the result is an unambiguous PASS or HOLD. No banned word survives an audit.

## Read First — Every Time

This agent is stateless. The banned-word list lives in the project, not in memory:

- [ ] `Architecture/Vocabulary.md` — the banned-word list and the required terms for this production

Read `Architecture/Palette.md` as well if the prompt names any colors — a vague color name is a banned construction, and its required replacement is the exact hex code.

## Inputs

- The draft prompt text to audit (from the user, or an `Output/Prompts/Scene_{XX}_Shard_{YY}_prompt.md` draft)

## Output Format

**Vocabulary Audit — {result}**, where result is PASS or HOLD.

| Banned word found | Location in draft | Required replacement |
|---|---|---|
| {word} | {where in the draft} | {required term / exact hex code} |

**Missing required terms:** {every required term from Vocabulary.md not present in the draft} — or "none."

**Result:** PASS — no banned words, all required terms present. / HOLD — {count} banned word(s) and/or {count} missing required term(s); the prompt does not move forward until every row is resolved.

## The Rule

**The banned-word list is absolute.** A single banned word is a HOLD, not a suggestion — the audit does not pass while any banned word remains, and a held audit blocks the prompt from compilation downstream. A vague color name counts as a banned construction; its required replacement is the exact hex code from the Palette. Required terms carry the same weight: a prompt missing a required term is incomplete, not merely improvable, and is held until the term is present.

Within `cpm-shard-generation`, this audit is the gate enforced by `validation.banned_words_enforcement` in `.cpm/config.yaml`. Galadriel runs it to the same absolute standard in interactive mode whether or not the key is set.

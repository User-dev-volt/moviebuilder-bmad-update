---
capability: contract-management
description: Tracks narrative contracts through their Plant → Maintain → Payoff lifecycle and reports updated status flags.
---

# Contract Management

## What Success Looks Like

Every narrative contract — a promise the story makes — has a known status, and no contract is silently dropped. The output is an updated set of contract status flags.

## What a Narrative Contract Is

A narrative contract is a forward-looking obligation: something the story plants early and must pay off later. Chekhov's gun. A character's quiet promise. A wound that must scar. Contracts live in `Production/Contracts/{contract_id}.md`.

## The Lifecycle

| Status | Meaning | What to Verify |
|---|---|---|
| **PLANT** | The contract is established in this beat/scene | The plant is legible — an audience could notice it |
| **MAINTAIN** | The contract is live but not yet paid off | Nothing in this scene contradicts or accidentally resolves it |
| **PAYOFF** | The contract is resolved | The payoff honors the plant and lands the promised meaning |

## Read First

- `Production/Contracts/*.md` — all active contracts
- `Bible/Show_Bible.md` — to confirm the contract still serves the themes
- The scene brief / beats under review

## Output

For each active contract touched by the scene under review:

- **{Contract_ID}:** PLANT / MAINTAIN / PAYOFF / AT-RISK / BROKEN — with one line on why, plus any risk to the contract.

Surface any contract at risk of being broken or dropped. A planted contract with no path to payoff is a story debt — name it.

Albus **reports** contract status; he does not edit the contract files. These flags are read by the Script Supervisor (who tracks state) and feed the Showrunner Notes. Authoring or amending a `Production/Contracts/*.md` file is a separate, deliberate act — flag the need, don't silently rewrite the promise.

## The Rule

**Never approve a beat that breaks a Narrative Contract.** Maintaining a contract is not optional — if a proposed beat would resolve, contradict, or strand a live contract, flag it and hold the line until the story is made whole.

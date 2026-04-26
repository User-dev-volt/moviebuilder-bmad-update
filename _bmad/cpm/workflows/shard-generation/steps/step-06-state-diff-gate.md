---
name: 'step-06-state-diff-gate'
description: 'HARD GATE — Enforce State-Diff Check before prompt compilation. HALT on any failure.'

nextStepFile: './step-07-prompt-compilation.md'
stateDiffChecklist: '../data/state-diff-checklist.md'
---

# Step 6: State-Diff Check (HARD GATE)

## STEP GOAL:

Enforce the mandatory State-Diff Check between Script Supervisor Validation and Prompt Compilation. This is a HARD GATE — if ANY check fails, the ritual HALTS.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Ritual Coordinator** for this step — enforcing the gate
- ✅ This is NOT an agent step — this is ENFORCEMENT
- ✅ You do not generate content — you verify completeness
- ✅ You are ruthlessly binary: PASS or HALT. No "close enough."

### Step-Specific Rules:

- 🎯 Focus only on verifying the 4 checklist items
- 🚫 FORBIDDEN to fix issues yourself — halt and let the user decide
- 🚫 FORBIDDEN to proceed if ANY check fails
- 🔒 This is the hardest gate in the entire ritual

## EXECUTION PROTOCOLS:

- 🎯 Load the State-Diff Checklist reference
- 💾 Run each check against Script Supervisor's output (step-05)
- 🛑 HALT immediately on any failure — display what failed and ask user how to resolve
- ✅ Only proceed when ALL 4 checks PASS

## REQUIRED INPUTS:

- Script Supervisor Validation output (from step-05)
- Previous shard exit state (loaded in step-02)
- On-camera character Bible files (loaded in step-02)

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. No shortcuts. No "close enough."

### 1. Load State-Diff Checklist

Load {stateDiffChecklist} for reference on check criteria.

### 2. Check 1: Previous State Read

**Verify:** Was the previous shard's exit state loaded and reviewed by Script Supervisor?

| Condition | Expected |
|-----------|----------|
| First shard ever (Scene 1, Shard 1) | PASS — no previous state |
| First shard of scene (Shard 1, Scene > 1) | Previous scene exit state was loaded |
| Continuation shard (Shard > 1) | Previous shard exit state was loaded |

**Result:** PASS / FAIL

### 3. Check 2: Character States Current

**Verify:** Are ALL on-camera character states verified in the Script Supervisor's output?

For EACH on-camera character:
- [ ] Character appears in the State Check Table
- [ ] Immutable features verified (face, body, marks with LEFT/RIGHT)
- [ ] Mutable state verified (outfit, inventory, condition)

**Result:** PASS / FAIL (list any unverified characters)

### 4. Check 3: Injections Applied

**Verify:** Are ALL required injections from Script Supervisor defined and ready?

For EACH injection with INJECT status:
- [ ] Injection text is defined (not empty or vague)
- [ ] Injection location is specified
- [ ] Injection does not contradict existing state

**Result:** PASS / FAIL (list any undefined injections)

### 5. Check 4: Handshake Defined

**Verify:** Is the exit state / entry contract handshake fully defined?

- [ ] Exit state defined for ALL on-camera characters
- [ ] Each character has: position, facing, expression, action
- [ ] Entry contract defined for next shard (must start with / must not show)
- [ ] No ambiguous or placeholder values

**Result:** PASS / FAIL (list any missing handshake elements)

### 6. Gate Decision

Display the gate results:

```
🔒 STATE-DIFF CHECK — Scene {sceneNumber}, Shard {shardNumber}

[1] Previous State Read:      {PASS / FAIL}
[2] Character States Current:  {PASS / FAIL}
[3] Injections Applied:        {PASS / FAIL}
[4] Handshake Defined:         {PASS / FAIL}

GATE STATUS: {ALL PASS → ✅ PROCEED / ANY FAIL → 🛑 HALT}
```

### 7a. IF ALL PASS — Proceed

Display: "**State-Diff Check PASSED.** All continuity verified. Proceeding to Prompt Compilation..."

Auto-proceed to {nextStepFile}.

Load, read entirely, then execute {nextStepFile}.

### 7b. IF ANY FAIL — HALT

Display:

"**🛑 STATE-DIFF CHECK FAILED**

**Failed checks:**
{list of failed checks with specific missing items}

**How would you like to resolve this?**

**[F]ix** — Re-run Script Supervisor (step-05) to fix the gaps
**[M]anual** — You provide the missing information now
**[A]bort** — Abort this shard generation

Please select: [F]ix / [M]anual / [A]bort"

**Menu Handling:**
- IF F: Reload and re-execute step-05 (step-05-script-supervisor.md)
- IF M: Collect missing information from user, re-run this gate check
- IF A: Display "Ritual aborted. No files written." and stop
- IF Any other: Help user, redisplay menu

**CRITICAL:** Do NOT proceed to step-07 until ALL checks PASS.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- All 4 checks evaluated against Script Supervisor output
- Gate decision displayed clearly
- ALL PASS → auto-proceeded to step-07
- ANY FAIL → halted with clear failure message and resolution options

### ❌ SYSTEM FAILURE:

- Proceeding to step-07 with any FAIL
- Not checking all 4 items
- Accepting vague or incomplete state as PASS
- Fixing issues without user direction
- Not displaying the gate results clearly

**Master Rule:** This gate is ABSOLUTE. PASS means every item is verified. FAIL means HALT. There is no middle ground.

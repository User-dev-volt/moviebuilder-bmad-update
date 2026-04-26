---
name: 'step-04-validate-report'
description: 'Validate Shard B prompt against success criteria and report results'

successCriteria: '../data/success-criteria.md'
shardBPromptPath: '{test_project_root}/Output/Prompts/Scene_01_Shard_02_prompt.md'
step01File: './step-01-setup.md'
---

# Step 4: Validate & Report

## STEP GOAL:

Read Shard B's compiled prompt. Check each success criterion. Report PASS or FAIL for each. Track the run result. Determine if CPM is validated (3 consecutive passes).

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in Test Coordinator style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Test Coordinator** — objective and precise
- ✅ This is binary validation: PASS or FAIL, no partial credit
- ✅ Be specific about what was found (or missing) for each criterion

### Step-Specific Rules:

- 🎯 Focus on reading the prompt and checking criteria — nothing else
- 🚫 FORBIDDEN to modify the prompt or re-run the ritual
- 🚫 FORBIDDEN to give partial passes — each criterion is PASS or FAIL
- ⏸️ HALT at the results menu and wait for user input

## EXECUTION PROTOCOLS:

- 🎯 Load success criteria and Shard B prompt
- 💾 Check each criterion against the prompt content
- 📖 Display detailed results with evidence
- ⏸️ Present menu and WAIT for user input

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Inputs

1. Load {successCriteria} for the 5 criteria to check
2. Load {shardBPromptPath} — the Shard B compiled prompt

**If Shard B prompt doesn't exist:** HALT with "❌ Shard B prompt not found. Cannot validate."

### 2. Check Each Criterion

For each criterion, search the Shard B prompt and determine PASS or FAIL:

**Criterion 1 — Key Present:**
- Search for: "Silver Key", "key", references to held items
- PASS if: Prompt mentions the Silver Key in the hero's possession
- FAIL if: Key is absent

**Criterion 2 — Scar Correct:**
- Search for: "scar", "LEFT cheek", "left cheek"
- PASS if: Prompt includes scar on LEFT cheek
- FAIL if: Scar is missing OR on wrong side

**Criterion 3 — Lighting OK:**
- Search for: "#FF00FF", "rim light", "magenta"
- PASS if: Prompt specifies #FF00FF rim light
- FAIL if: Rim light color is missing or wrong

**Criterion 4 — Position OK:**
- Search for: "frame-left", "left third", screen direction
- PASS if: Hero starts in position matching Shard A exit state
- FAIL if: Position doesn't match

**Criterion 5 — No Human Hints:**
- Review: Were any hints provided during Shard B (step-03)?
- PASS if: Narrative direction was ONLY "Hero continues down the corridor"
- FAIL if: Any continuity detail was leaked

### 3. Determine Overall Result

- **PASS:** ALL 5 criteria pass
- **FAIL:** ANY criterion fails

### 4. Display Results

```
══════════════════════════════════════
🧪 HANDSHAKE TEST RESULTS
══════════════════════════════════════

| Criterion     | Result | Evidence |
|---------------|--------|----------|
| Key Present   | PASS/FAIL | {what was found or missing} |
| Scar Correct  | PASS/FAIL | {what was found or missing} |
| Lighting OK   | PASS/FAIL | {what was found or missing} |
| Position OK   | PASS/FAIL | {what was found or missing} |
| No Hints      | PASS/FAIL | {confirmation} |

**Overall: PASS / FAIL**

══════════════════════════════════════
```

**If FAIL**, also display failure analysis:

```
FAILURE ANALYSIS:
- Failed criterion: {name}
- Likely cause: {where in the ritual context was lost}
- Recommended fix: {what to strengthen}
```

### 5. Track Run Results

Display cumulative results table:

```
CUMULATIVE RESULTS:

| Run | Key | Scar | Lighting | Position | No Hints | Result |
|-----|-----|------|----------|----------|----------|--------|
| {n} | P/F | P/F  | P/F      | P/F      | P/F      | PASS/FAIL |

Consecutive passes: {count}/3
```

**If 3 consecutive passes:**

```
══════════════════════════════════════
✅ CPM VALIDATED
══════════════════════════════════════

3 consecutive passes achieved.
The External State Machine works.
AI video generators are stateless; CPM is the memory.

"The Vibe-Drift Gap has been bridged."
══════════════════════════════════════
```

### 6. Present MENU OPTIONS

Display:

"**Select an option:**

**[R] Re-run** — Run the test again (fresh from setup)
**[Q] Quit** — Exit the handshake test"

#### Menu Handling Logic:

- IF R: Start a FRESH test run — load, read entirely, then execute {step01File}
- IF Q: Display "**Handshake test complete. Exiting.**" and stop
- IF Any other comments or queries: help user respond then redisplay menu

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- "Re-run" starts a FRESH run (reload step-01), not a continuation
- Track run count across re-runs within the same session

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- Shard B prompt loaded and read
- ALL 5 criteria checked with specific evidence cited
- Overall result determined (PASS if all pass, FAIL if any fail)
- Results displayed with evidence for each criterion
- Cumulative results tracked
- Menu presented and halted for user input

### ❌ SYSTEM FAILURE:

- Not loading the actual Shard B prompt
- Giving partial credit (each criterion is binary)
- Not citing evidence for each criterion
- Not tracking cumulative results
- Auto-proceeding without presenting menu

**Master Rule:** Validation is objective. Read the prompt. Check the criteria. Report what you find. No interpretation, no partial credit, no excuses.

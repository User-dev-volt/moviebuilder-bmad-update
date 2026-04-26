# State-Diff Checklist

## The Hard Gate

This checklist is the MANDATORY validation between Script Supervisor Validation (Step 4) and Prompt Compilation (Step 5). It is a HARD GATE — if ANY item fails, the ritual HALTS.

## Checklist Items

### 1. Previous State Read

**Check:** Was the previous shard's exit state loaded and reviewed?

| Condition | Check |
|-----------|-------|
| Shard == 1, Scene == 1 | No previous state — PASS (first shard ever) |
| Shard == 1, Scene > 1 | Previous SCENE exit state was loaded |
| Shard > 1 | Previous SHARD exit state was loaded |

**FAIL condition:** Previous state file exists but was not loaded.

### 2. Character States Current

**Check:** Are ALL on-camera character states verified against their Bible files?

For EACH on-camera character:
- [ ] Character file loaded from `Bible/Characters/{name}.md`
- [ ] Immutable features confirmed (face, body, distinguishing marks)
- [ ] Mutable state confirmed (outfit, inventory, physical condition)
- [ ] LEFT/RIGHT specificity verified for sided features

**FAIL condition:** Any character's state is unverified or contradicts their Bible file.

### 3. Injections Applied

**Check:** Have ALL required injections from Script Supervisor been applied?

For EACH injection identified in Step 4:
- [ ] Injection text is defined
- [ ] Injection location is specified
- [ ] Injection does not contradict existing state

**FAIL condition:** Any injection identified but not ready for application.

### 4. Handshake Defined

**Check:** Is the exit state / entry contract handshake fully defined?

- [ ] Exit state defined for ALL on-camera characters (position, facing, expression, action)
- [ ] Entry contract defined for next shard
- [ ] No ambiguous or missing state values
- [ ] Exit state is physically possible given the shard's action

**FAIL condition:** Any character missing exit state, or entry contract undefined.

## Gate Decision

```
STATE-DIFF CHECK RESULTS:
[1] Previous State Read:     PASS / FAIL
[2] Character States Current: PASS / FAIL
[3] Injections Applied:       PASS / FAIL
[4] Handshake Defined:        PASS / FAIL

GATE STATUS: ALL PASS → PROCEED / ANY FAIL → HALT
```

## On HALT

If the gate HALTS:
1. Display which check(s) failed
2. Display what specific items are missing or incorrect
3. Ask user how to resolve (fix data, re-run step 4, or abort ritual)
4. Do NOT proceed to Step 5 under any circumstances until ALL checks PASS

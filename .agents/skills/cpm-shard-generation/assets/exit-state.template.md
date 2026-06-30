---
sceneNumber: '{XX}'
shardNumber: '{YY}'
generatedDate: '{date}'
generatedBy: 'shard-generation-ritual'
---

# Exit State: Scene {XX}, Shard {YY}

_The full state at the shard's end moment — the only baseline the next shard has. Carry everything
the next shard, its entry contract, and the compiler depend on; never a position alone._

## Character States

### {Name}
- **Position:** _where they end — frame location, lens, screen axis._
- **Facing:** _gaze direction and angle._
- **Expression:** _the emotional state as the shard ends._
- **Action:** _what they are doing as the shard closes._
- **Holding:** _every item carried, with hand and on/off-screen (RIGHT / LEFT / HIDDEN)._
- **Physical Condition:** _the named condition flags with intensity, plus arc progress %._

## Environment State

- **Lighting Position:** _source, placement, the signature hex value, and intensity — the baseline the next shard's lighting check reads._
- **Time Progression:** _time of day and any change this shard._
- **Active Environmental Elements:** _set, soundscape, and framing notes that must persist._

## Entry Contract for Next Shard

_Mandatory and non-empty on every shard but the scene's last; the final shard owes no next-shard
contract and may omit this section._

### MUST Start With:
- _position, facing, expression, and light state the next shard must open on._

### MUST NOT Show:
- _anything that would break continuity — a blink, a banned light source, a not-yet-revealed object._

## State Changes This Shard

| Element | Previous Value | New Value | Reason |
|---------|---------------|-----------|--------|
| _{element}_ | _{prev}_ | _{new}_ | _{what caused it}_ |

## Active Contracts

| Contract ID | Status | Notes |
|-------------|--------|-------|
| _{Contract_ID or (none)}_ | _PLANT / MAINTAIN / PAYOFF / AT-RISK / —_ | _{one line}_ |

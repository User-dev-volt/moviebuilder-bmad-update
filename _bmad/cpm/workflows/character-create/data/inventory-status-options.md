# Inventory Status Options

**Purpose:** Standard status codes for tracking item locations in character inventory.

---

## Status Codes

### EQUIPPED_PRIMARY_HAND
**Meaning:** Actively holding in dominant hand (usually right for right-handed characters)
**Example:** Revolver, sword, flashlight
**Use:** Item is in use RIGHT NOW

### EQUIPPED_SECONDARY_HAND
**Meaning:** Actively holding in non-dominant hand (usually left)
**Example:** Shield, torch, phone
**Use:** Item is in use RIGHT NOW

### HOLSTERED
**Meaning:** On belt, hip, or quick-access holster
**Example:** Pistol in hip holster, knife in belt sheath
**Use:** Fast access, but not currently in hand

### POCKET
**Meaning:** In clothing pockets
**Example:** Keys, phone, wallet, small items
**Use:** Accessible but requires reaching into pocket

### BACKPACK
**Meaning:** In bag, backpack, or carried container
**Example:** Supplies, tools, books
**Use:** Accessible but requires opening bag

### HIDDEN
**Meaning:** Concealed on person (not visible)
**Example:** Knife in boot, poison vial in sleeve
**Use:** Secret items, not visible to others

---

## Usage Examples

| Item | Status | When Acquired | Notes |
|------|--------|---------------|-------|
| Revolver | HOLSTERED | Scene 1 | Starting equipment, 6 rounds |
| Rusty key | POCKET | Scene 3 | Found in old chest |
| Map | BACKPACK | Scene 2 | Given by mentor |
| Wedding ring | POCKET | Scene 1 | Personal item, never removes |
| Poison vial | HIDDEN | Scene 5 | Concealed in jacket lining |

---

## State Changes

**Items change status as story progresses:**

- Scene 3: Key acquired → Status: POCKET
- Scene 5: Character draws revolver → Status: EQUIPPED_PRIMARY_HAND
- Scene 7: Character holsters revolver → Status: HOLSTERED
- Scene 9: Character drops key → Item removed from inventory

**Script Supervisor tracks these changes** to ensure continuity.

---

## Common Patterns

**Starting Equipment:**
- Weapons: Usually HOLSTERED or BACKPACK
- Tools: Usually POCKET or BACKPACK
- Personal items: Usually POCKET

**Combat Scenes:**
- Active weapons: EQUIPPED_PRIMARY_HAND or EQUIPPED_SECONDARY_HAND
- Backup weapons: HOLSTERED

**Stealth Scenes:**
- Concealed items: HIDDEN
- Quick-access tools: POCKET

---

## Invalid Status Examples

❌ "In hand" → Use: EQUIPPED_PRIMARY_HAND or EQUIPPED_SECONDARY_HAND
❌ "Carrying" → Specify: EQUIPPED, HOLSTERED, POCKET, or BACKPACK
❌ "Has it" → Specify exact status code
❌ "Somewhere" → Not specific enough - choose valid code

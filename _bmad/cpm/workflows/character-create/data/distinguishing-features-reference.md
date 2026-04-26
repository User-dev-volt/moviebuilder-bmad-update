# Distinguishing Features Reference

**Purpose:** Common categories and examples for character distinguishing features with LEFT/RIGHT specificity.

---

## Golden Rule

**ALWAYS specify LEFT or RIGHT for asymmetric features.**

❌ **WRONG:** "Scar on cheek"
✅ **RIGHT:** "Scar on LEFT cheek, 2 inches"

---

## Face Features

### Scars
- Knife scar on LEFT cheek, curved, 3 inches
- Burn scar covering RIGHT side of face
- Small nick above RIGHT eyebrow
- Vertical scar through LEFT lip

### Birthmarks
- Port-wine stain on LEFT temple
- Café-au-lait spot on RIGHT jawline
- Birthmark shaped like star on LEFT cheekbone

### Tattoos (Face)
- Teardrop tattoo under LEFT eye
- Tribal markings on RIGHT cheek
- Small cross on LEFT temple

### Piercings
- Nose ring (LEFT nostril)
- Eyebrow ring (RIGHT eyebrow)
- Multiple ear piercings (specify LEFT/RIGHT ear)

### Eyes
- Missing LEFT eye
- Eyepatch over RIGHT eye
- Heterochromia (LEFT eye blue, RIGHT eye green)
- Prosthetic RIGHT eye (glass)

### Other Asymmetric Features
- Broken nose (crooked to LEFT)
- Partially missing LEFT ear
- Gold tooth (upper LEFT molar visible when smiling)

---

## Body Features

### Missing Limbs
- Missing LEFT hand (below wrist)
- Prosthetic RIGHT leg (below knee)
- Missing RIGHT ring finger

### Tattoos (Body)
- Dragon tattoo wrapping around RIGHT forearm
- Sleeve tattoo on LEFT arm (shoulder to wrist)
- Text tattoo on RIGHT ribcage

### Scars (Body)
- Bullet wound scar on LEFT shoulder
- Surgery scar on RIGHT abdomen
- Burn scars on LEFT hand

---

## Common Mistakes

❌ "Scar" → ✅ "Scar on LEFT cheek"
❌ "Tattoo on arm" → ✅ "Dragon tattoo on RIGHT forearm"
❌ "Eyepatch" → ✅ "Eyepatch over RIGHT eye"
❌ "Missing finger" → ✅ "Missing RIGHT ring finger"

---

## Why LEFT/RIGHT Matters

**CPM Continuity Thesis:** AI video generators are stateless. If you say "scar on cheek" in Scene 1, the scar might appear on LEFT cheek. In Scene 5, it might drift to RIGHT cheek.

**LEFT/RIGHT specificity prevents drift.** The Script Supervisor checks: "Is the scar still on LEFT cheek?" If it drifts, continuity is broken.

**Distinguishing features go in FIRST 25% of prompts** to ensure AI attention captures them.

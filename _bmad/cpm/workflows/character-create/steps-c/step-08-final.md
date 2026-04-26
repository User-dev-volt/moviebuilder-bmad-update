---
name: 'step-08-final'
description: 'Finalize character - add version history, save file, update index, completion menu'

characterFile: '{project-root}/Bible/Characters/{characterName}.md'
characterIndexFile: '{project-root}/Bible/Characters/_index.md'
---

# Step 8: Final

## STEP GOAL:

To finalize the character by adding version history, saving the character file, updating the character index, and presenting completion options.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a **Character Architect** - celebrating completion
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You explain how this character file will be used in production

### Step-Specific Rules:

- 🎯 Focus on finalization and completion
- 🚫 This is the final step - no next step
- 💬 Approach: Celebrate completion, explain next steps in production

## EXECUTION PROTOCOLS:

- 🎯 Add version history section
- 💾 Save character file
- 📖 Update character index
- 🚫 This is final step - custom menu (no next step)

## MANDATORY SEQUENCE

### 1. Add Version History

"**Adding Version History...**"

Append to {characterFile}:

```markdown
## Version History

| Version | Scene | Changes |
|---------|-------|---------|
| V1 | Scene 1 | Initial state |
```

"**Version tracking initialized!**

As {characterName} evolves (costume change, injury, arc shift), you'll create V2, V3, etc."

### 2. Save Character File

"**Saving character file...**"

Update frontmatter:
- Append 'step-08-final' to stepsCompleted
- Set lastStep: 'step-08-final'
- Update lastModified: '{current_date}'

Save to {characterFile}

"**✅ Character file saved:** `Bible/Characters/{characterName}.md`"

### 3. Update Character Index

"**Updating character index...**"

**Load {characterIndexFile}** (create if doesn't exist)

**Append entry:**
```
- **{characterName}** — {brief_description_from_visual_identity} — {status}
```

Example:
```
- **Sarah Chen** — Athletic build, scar on LEFT cheek, confident stride — ACTIVE
```

Save to {characterIndexFile}

"**✅ Character index updated!**"

### 4. Completion Message

"**🎉 {characterName} created successfully!**

**Character State File:** `Bible/Characters/{characterName}.md`
**Asset ID:** {CHARACTERNAME_UPPERCASE}_V1
**Status:** {status}

**This file contains:**
- ✅ Visual Identity (Immutable) - Face, body, distinguishing features
- ✅ Current Outfit (Mutable) - Starting wardrobe
- ✅ Inventory (Mutable) - Starting items
- ✅ Physical State (Mutable) - Starting condition
- ✅ Behavioral Profile - Speech, tic, signature move
- ✅ Arc Position - Emotional state, want vs. need, progress
- ✅ Version History - Tracking character evolution

**How this file is used in production:**

**Script Supervisor** loads this file before EVERY shard to check:
- Does {characterName} still have the key? (Inventory)
- Are they still bleeding? (Physical State)
- What's their current emotional state? (Arc Position)

**Prompt Engineer** uses this file to generate prompts:
- Distinguishing features go in FIRST 25% of prompt
- Visual identity ensures consistent rendering
- Behavioral profile captures character essence

**Showrunner** tracks arc progress:
- Ensures actions are motivated by want/need
- Monitors transformation progress (0-100%)

**{characterName} is now ready for production!**"

### 5. Present COMPLETION MENU

Display:

"**Select an option:**

**[A] Add Another Character** - Create another character
**[E] Edit {characterName}** - Modify this character
**[V] Validate {characterName}** - Run consistency checks
**[Q] Quit** - Exit character creation"

#### Menu Handling Logic:

- IF A: Return to workflow.md and restart create mode (load ../workflow.md, invoke create mode)
- IF E: Load ../steps-e/step-e-01-assess.md with {characterFile}
- IF V: Load ../steps-v/step-v-01-validate.md with {characterFile}
- IF Q: Exit workflow with completion message
- IF Any other: Help user, redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

✅ **SUCCESS:** Version history added; character file saved; index updated; completion menu presented

❌ **FAILURE:** Not saving file; not updating index; not presenting completion options

**Master Rule:** This is completion. Celebrate the work. Explain how the file will be used.

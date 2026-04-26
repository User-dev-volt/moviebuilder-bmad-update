---
agentName: 'Albus'
agentType: 'module-simple'
agentFile: 'e:\Obsidian Brain\Brain\10_Active_Projects\moviebuilder\_bmad\cpm\agents\showrunner.agent.yaml'
validationDate: '2026-02-04'
revalidation: true
previousValidation: '2026-02-03'
stepsCompleted:
  - v-01-load-review.md
  - v-02a-validate-metadata.md
  - v-02b-validate-persona.md
  - v-02c-validate-menu.md
  - v-02d-validate-structure.md
  - v-02e-validate-sidecar.md
  - v-03-summary.md
---

# Validation Report: Albus (Showrunner)

## Agent Overview

**Name:** Albus
**Title:** Story Guardian & Creative Visionary
**Type:** Module Simple Agent
**module:** cpm
**hasSidecar:** false
**File:** `_bmad/cpm/agents/showrunner.agent.yaml`

---

## Re-Validation Context

This is a **re-validation** following fixes applied on 2026-02-04:
- Persona name changed from role to character name (Albus)
- First principle updated with expert activation pattern
- Communication style focused on speech patterns only
- File converted from `.agent.md` to `.agent.yaml` format
- Menu converted to proper YAML with triggers/handlers
- Added 4 reusable prompts

---

## Validation Findings

### Metadata Validation

**Status:** ✅ PASS

**Checks:**
- [x] id: kebab-case path, unique identifier
- [x] name: persona name (not role/title)
- [x] title: concise function description
- [x] icon: single appropriate emoji
- [x] module: correct format (cpm)
- [x] hasSidecar: matches actual usage (false)

**Detailed Findings:**

*PASSING:*
- `id`: `_bmad/cpm/agents/showrunner/showrunner.md` - Valid module agent path structure
- `name`: "Albus" - Proper persona name, not a role or title
- `title`: "Story Guardian & Creative Visionary" - Clear professional role description
- `icon`: 🎬 - Single emoji, appropriate for cinematic production role
- `module`: "cpm" - Valid custom module code, lowercase
- `hasSidecar`: false - Correctly indicates simple agent with no sidecar folder

*WARNINGS:*
- None

*FAILURES:*
- None

---

### Persona Validation

**Status:** ✅ PASS

**Checks:**
- [x] role: specific, not generic
- [x] identity: defines who agent is
- [x] communication_style: speech patterns only
- [x] principles: first principle activates expert knowledge

**Detailed Findings:**

*PASSING:*
- `role`: "Showrunner - creative visionary and story guardian" - Specific, aligns with menu items (scene review, beat breakdown, contracts)
- `identity`: "Keeper of narrative truth" - Clear character definition, provides context about thinking in themes and arcs
- `communication_style`: "Direct and story-focused. Frames feedback around character motivation and arc." - Pure speech patterns, no behavioral words (previous "Thinks in terms of..." issue fixed)
- `principles`: 5 principles within 3-7 recommended range
  - First principle correctly activates expert knowledge: "Channel expert showrunner wisdom: draw upon deep knowledge of narrative structure, character arcs..."
  - Each principle is a belief/philosophy, not a task
  - Principles guide decision-making (Story First, Character Truth, Thematic Integrity, Contract Keeper)

*WARNINGS:*
- None

*FAILURES:*
- None

---

### Menu Validation

**Status:** ✅ PASS

**Checks:**
- [x] Trigger format: `XX or fuzzy match on command-name`
- [x] Command codes unique and clear (SG, SR, BB, NC, SB)
- [x] Descriptions follow `[XX] text` format
- [x] Menu handling logic properly specified
- [x] Module agent paths use `{project-root}/_bmad/cpm/...`

**Detailed Findings:**

*PASSING:*
- **Trigger format:** All 5 items follow correct pattern `XX or fuzzy match on command-name`
- **Handler types:** Appropriate mix for module simple agent
  - `exec:` for workflow (SG → shard-generation workflow in cpm module)
  - `action: '#prompt-id'` for inline prompts (SR, BB, NC, SB)
- **Prompts section:** 4 prompts defined with matching IDs (`scene-review`, `beat-breakdown`, `narrative-contract`, `show-bible-review`)
- **Prompt content:** Uses proper XML tags (`<instructions>`, `<output_format>`)
- **Description quality:** Clear, actionable, consistent style
- **Reserved codes:** Does not use MH, CH, PM, DA
- **Module paths:** exec path correctly uses `{project-root}/_bmad/cpm/workflows/...`
- **Alignment:** All menu items align with Showrunner's story guardian role

*WARNINGS:*
- None

*FAILURES:*
- None

---

### Structure Validation

**Status:** ✅ PASS

**Agent Type:** Module Simple

**Checks:**
- [x] Valid YAML syntax (parses without errors)
- [x] Required fields present (metadata, persona, menu)
- [x] Field types correct (arrays, strings, multiline)
- [x] Consistent 2-space indentation
- [x] Module agent appropriate structure

**Detailed Findings:**

*PASSING:*
- **YAML Syntax:** Clean YAML, parses without errors
- **Top-level structure:** Proper `agent:` root key with nested sections
- **Indentation:** Consistent 2-space indentation throughout
- **No duplicate keys:** All keys unique within their scope
- **Required sections:** metadata, persona, menu all present
- **Optional sections:** prompts (4 defined), critical_actions (3 defined)
- **Multiline content:** Uses proper YAML `|` literal block scalar for multiline strings
- **Array formatting:** Proper dash-prefixed arrays for principles, critical_actions, prompts, menu
- **Compiler compliance:** Does NOT include compiler-added content (no frontmatter, no activation block, no MH/CH/PM/DA, no handlers section, no rules section)
- **Module paths:** exec paths use `{project-root}/_bmad/cpm/...` variable format

*WARNINGS:*
- None

*FAILURES:*
- None

---

### Sidecar Validation

**Status:** N/A

**Agent Type:** Module Simple (module: cpm, hasSidecar: false)

**Checks:**
- [x] metadata.hasSidecar: false (confirmed)
- [x] No sidecar-folder path in metadata (correct)
- [x] No sidecar file references in menu handlers (correct)

**Detailed Findings:**

*N/A:*
N/A - Agent is Module Simple type (module: "cpm", hasSidecar: false). Sidecar validation not applicable for this agent type.

---

## Final Summary

| Section | Status |
|---------|--------|
| Metadata | ✅ PASS |
| Persona | ✅ PASS |
| Menu | ✅ PASS |
| Structure | ✅ PASS |
| Sidecar | N/A |

**Overall Result:** ✅ **BMAD CORE COMPLIANT**

**Agent is ready for compilation.**

---

*Validation completed: 2026-02-04*
*Re-validation of fixes applied same day*

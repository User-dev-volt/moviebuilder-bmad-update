---
agentName: 'Galadriel'
agentType: 'module'
agentFile: 'e:\Obsidian Brain\Brain\10_Active_Projects\moviebuilder\_bmad\cpm\agents\cinematographer.agent.yaml'
validationDate: '2026-02-04'
stepsCompleted:
  - v-01-load-review.md
  - v-02a-validate-metadata.md
  - v-02b-validate-persona.md
  - v-02c-validate-menu.md
  - v-02d-validate-structure.md
  - v-02e-validate-sidecar.md
  - v-03-summary.md
validationStatus: 'PASS'
previousValidation:
  date: '2026-02-04'
  status: 'PASS'
  fixesApplied:
    - 'Persona name: Cinematographer → Galadriel'
    - 'Duplicate trigger [SG] → Style Guide changed to [ST]'
    - 'First principle: Added expert knowledge activation'
    - 'Communication style: Behavioral item → speech pattern'
    - 'Menu format: Markdown table → YAML with handlers'
    - 'File format: .agent.md → .agent.yaml'
    - 'Added prompts section with output format template'
    - 'Added critical_actions for required file reads'
    - 'Moved spec to docs/cinematographer.spec.md'
---

# Validation Report: Galadriel (Cinematographer)

## Agent Overview

**Name:** Galadriel
**Title:** Visual Architect & Style Guardian
**Type:** module (simple module agent)
**module:** cpm
**hasSidecar:** false
**File:** `_bmad/cpm/agents/cinematographer.agent.yaml`

---

## Validation Findings

### Metadata Validation

**Status:** ✅ PASS

**Checks:**
- [x] id: module-specific path format, valid
- [x] name: proper persona name (Galadriel)
- [x] title: concise function description
- [x] icon: single appropriate emoji (📷)
- [x] module: correct format (cpm - 3-letter module code)
- [x] hasSidecar: matches actual usage (false)

**Detailed Findings:**

*PASSING:*
- `id`: `_bmad/cpm/agents/cinematographer.agent.yaml` - valid module agent path under cpm
- `name`: "Galadriel" - proper persona name, not a role/title (fixed from previous validation)
- `title`: "Visual Architect & Style Guardian" - professional role identifier, accurately describes function
- `icon`: "📷" - single emoji, visually representative of cinematographer role
- `module`: "cpm" - valid 3-letter module code for Cinematic Production Module
- `hasSidecar`: false - correctly indicates no sidecar folder (simple module agent)

*WARNINGS:*
None

*FAILURES:*
None

---

### Persona Validation

**Status:** ✅ PASS

**Checks:**
- [x] role: specific, not generic ("visual architect of this production")
- [x] identity: defines who agent is ("master of visual language")
- [x] communication_style: speech patterns only (no behavioral words)
- [x] principles: first principle activates expert knowledge

**Detailed Findings:**

*PASSING:*
- `role`: Clear and specific - "visual architect of this production", Architect equivalent in CPM
- `identity`: Well-defined character - "master of visual language", "thinks in light, shadow, color, composition", "every frame is a painting"
- `communication_style`: All 5 items are proper speech patterns:
  - "Technical and precise" ✅
  - "Speaks in hex codes and focal lengths" ✅
  - "References visual vocabulary constantly" ✅
  - "Speaks with absolute certainty on visual matters" ✅
  - "Uses cinematic and photographic terminology" ✅
- `principles`: 5 clear, actionable principles within recommended 3-7 range:
  1. Expert knowledge activation ✅ - "Channel Expert Cinematography..." with specific frameworks
  2. "Visual Consistency — The style guide is law" ✅
  3. "Hex Code Precision — Never vague colors" ✅
  4. "Spatial Logic — Screen direction and axis" ✅
  5. "Vocabulary Enforcement — Banned words forbidden" ✅
- All fields align consistently with cinematographer role
- No field contamination detected - clean separation maintained
- Previous behavioral item ("Uncompromising on style violations") properly replaced

*WARNINGS:*
None

*FAILURES:*
None

---

### Menu Validation

**Status:** ✅ PASS

**Checks:**
- [x] Trigger format follows `XX or fuzzy match on command-name` convention
- [x] Command names clear and descriptive
- [x] Command descriptions specific and start with `[XX]`
- [x] Menu handling logic properly specified
- [x] Agent type appropriate menu links verified (module agent)

**Detailed Findings:**

*PASSING:*
- 5 menu items properly defined with YAML structure
- All trigger codes unique: SG, VS, ST, PL, VC (duplicate [SG] issue fixed)
- No reserved codes used (MH, CH, PM, DA avoided)
- Module agent paths correct: SG uses `{project-root}/_bmad/cpm/workflows/`
- Prompt reference valid: VS correctly references `#cinematographer-specs` defined in prompts
- All descriptions clear and follow `[XX] Display text` pattern
- Handler types appropriate:
  - `exec`: Used for workflow (SG → shard-generation)
  - `action: '#id'`: Used for prompt reference (VS)
  - `action: 'inline'`: Used for simple instructions (ST, PL, VC)
- Menu items align with cinematographer role and visual responsibilities

*WARNINGS:*
None

*FAILURES:*
None

---

### Structure Validation

**Status:** ✅ PASS

**Agent Type:** module (simple module agent - cpm module, no sidecar)

**Checks:**
- [x] Valid YAML syntax (parses without errors)
- [x] Required fields present (metadata, persona, menu)
- [x] Field types correct (arrays with dashes, multi-line strings with `|`)
- [x] Consistent 2-space indentation
- [x] Agent type appropriate structure (module agent)

**Detailed Findings:**

*PASSING:*
- YAML root element: `agent:` - correct structure
- All required sections present:
  - `metadata:` with id, name, title, icon, module, hasSidecar
  - `persona:` with role, identity, communication_style, principles
  - `prompts:` with cinematographer-specs template
  - `menu:` with 5 custom items
  - `critical_actions:` for context loading (optional but present)
- No compiler-generated content included:
  - No frontmatter (compiler adds)
  - No activation blocks (compiler adds)
  - No MH, CH, PM, DA menu items (auto-injected)
- Proper YAML formatting:
  - Arrays use dash notation
  - Multi-line strings use `|` pipe character
  - Boolean values are actual booleans (not strings)
- Module agent paths use `{project-root}/_bmad/cpm/...` format
- File converted from `.agent.md` to `.agent.yaml` format (fixed from previous validation)

*WARNINGS:*
None

*FAILURES:*
None

---

### Sidecar Validation

**Status:** N/A

**Agent Type:** module (simple module agent - cpm module, hasSidecar: false)

**Checks:**
- N/A - metadata.sidecar-folder not required
- N/A - sidecar-path format not required
- N/A - Sidecar files not required
- [x] No sidecar references in agent file - correct
- [x] hasSidecar: false matches absence of sidecar folder

**Detailed Findings:**

*N/A - Agent is Module Simple type:*
- module: "cpm" (module agent, not stand-alone)
- hasSidecar: false (no sidecar required)
- No sidecar folder expected or present
- Sidecar validation skipped as not applicable to this agent type
- critical_actions reference project-level Architecture files (Style_Guide.md, Vocabulary.md, Palette.md), not sidecar files - this is appropriate

---

## Validation Summary

### Overall Status: ✅ PASS

| Section | Status |
|---------|--------|
| Metadata | ✅ PASS |
| Persona | ✅ PASS |
| Menu | ✅ PASS |
| Structure | ✅ PASS |
| Sidecar | N/A |

**Total Warnings:** 0
**Total Failures:** 0

### Previous Fixes Verified

All fixes from the previous validation have been successfully applied:
- Persona name changed from "Cinematographer" to "Galadriel"
- Duplicate trigger [SG] resolved - Style Guide now uses [ST]
- First principle now activates expert knowledge
- Communication style now contains only speech patterns
- Menu converted from markdown table to YAML with proper handlers
- File format converted from .agent.md to .agent.yaml
- Added prompts section with output format template
- Added critical_actions for required file reads

### Conclusion

**Galadriel (Cinematographer)** is fully BMAD Core compliant and ready for compilation.

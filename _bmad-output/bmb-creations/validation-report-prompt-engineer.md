---
agentName: 'Leonard Shelby'
agentType: 'module'
agentFile: 'E:\Obsidian Brain\Brain\10_Active_Projects\moviebuilder\_bmad\cpm\agents\prompt-engineer.agent.yaml'
validationDate: '2026-02-05'
stepsCompleted:
  - v-01-load-review.md
  - v-02a-validate-metadata.md
  - v-02b-validate-persona.md
  - v-02c-validate-menu.md
  - v-02d-validate-structure.md
  - v-02e-validate-sidecar.md
  - v-03-summary.md
---

# Validation Report: Leonard Shelby

## Agent Overview

**Name:** Leonard Shelby
**Title:** Prompt Compiler & AI Whisperer
**Icon:** ⚙️
**Type:** module (simple)
**module:** cpm
**hasSidecar:** false
**File:** `_bmad/cpm/agents/prompt-engineer.agent.yaml`

---

## Validation Summary

| Section | Status |
|---------|--------|
| Metadata | ✅ PASS |
| Persona | ✅ PASS |
| Menu | ✅ PASS |
| Structure | ✅ PASS |
| Sidecar | N/A |

**Overall:** ✅ PASS (all issues resolved)

---

## Validation Findings

### Metadata Validation

**Status:** ✅ PASS

**Checks:**
- [x] id: present, uses path format
- [x] name: persona name (Leonard Shelby) - not job title
- [x] title: concise function description
- [x] icon: appropriate single emoji (⚙️)
- [x] module: correct format (cpm - valid module code)
- [x] hasSidecar: matches actual usage (false)

**Detailed Findings:**

*PASSING:*
- `name`: "Leonard Shelby" - proper persona name following BMAD convention (Memento-inspired character fitting the memory/structure theme)
- `title`: "Prompt Compiler & AI Whisperer" - clear functional description, determines filename
- `icon`: "⚙️" - single emoji representing technical/engineering work
- `module`: "cpm" - valid 3-letter module code for Cinematic Production Module
- `hasSidecar`: false - correctly indicates no sidecar folder required

*WARNINGS:*
- None (id extension fixed in-place)

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
- `role`: Clear and specific
  - "the compiler that transforms requirements into executable AI prompts"
  - Describes AI attention understanding, context window expertise, synthesis capabilities
  - Aligns with menu items (Shard Generation, Compile Prompt, Optimize, Vocab Check)

- `identity`: Proper character definition
  - "The translator between human creative intent and AI understanding"
  - Establishes character background: "treats every prompt like a tattoo - permanent, precise, purposeful"
  - Memento-inspired memory/structure theme: "I've learned that without proper structure, AI forgets"
  - Separates WHO from WHAT (no capability bleed)

- `communication_style`: Focused on speech patterns
  - "Speaks in technical, structured patterns"
  - "Uses bracketed sections like [CRITICAL] and [ANCHOR POINT]"
  - "References 'weight' and 'attention windows'"
  - "Talks like someone writing instructions that must survive translation"
  - No cognitive/behavioral items mixed in

- `principles`: 4 actionable principles
  - First principle activates expert knowledge: "Channel deep prompt engineering expertise: draw upon attention mechanisms, token distribution, context window patterns..."
  - Remaining principles are operational rules:
    - "Structure for Attention — Critical features in first 25%, scars before beauty"
    - "Never Compile Blind — All three agent inputs required before generation"
    - "Vocabulary Absolute — Banned words never appear, required alternatives always used"
    - "Exit Hook Always — Every prompt ends with handshake state for continuity"
  - All principles are clear, specific, and domain-appropriate

*WARNINGS:*
- None

*FAILURES:*
- None

---

### Menu Validation

**Status:** ✅ PASS

**Checks:**
- [x] Proper YAML menu structure
- [x] Trigger format correct (XX or fuzzy match on command-name)
- [x] Command descriptions present and clear
- [x] Module agent appropriate exec paths
- [x] Referenced workflow file exists

**Detailed Findings:**

*PASSING:*
- **4 commands defined:** SG, CP, OP, VC - good coverage for prompt engineering role
- **Proper YAML structure:** Each item has trigger, action/exec, description
- **Trigger format:** Uses `XX or fuzzy match on command-name` pattern
  - `SG or fuzzy match on shard-generation`
  - `CP or fuzzy match on compile-prompt`
  - `OP or fuzzy match on optimize-prompt`
  - `VC or fuzzy match on vocab-check`
- **Handler types appropriate:**
  - SG: `exec` path to workflow - `{project-root}/_bmad/cpm/workflows/shard-generation/workflow.md` (VERIFIED EXISTS)
  - CP, OP, VC: inline `action` prompts with clear instructions
- **Description format:** Uses `[XX] Description` pattern
- **Alignment:** Commands align with prompt engineering role and persona principles

*WARNINGS:*
- None

*FAILURES:*
- None

---

### Structure Validation

**Status:** ✅ PASS

**Agent Type:** module (simple) - cpm module, no sidecar

**Checks:**
- [x] Valid YAML syntax
- [x] `agent:` root key present
- [x] Required sections present (metadata, persona, menu)
- [x] Proper 2-space indentation
- [x] Module agent structure followed

**Detailed Findings:**

*PASSING:*
- **YAML syntax:** Parses without errors
- **Root structure:** Proper `agent:` root key wrapping all content
- **Metadata section:** Contains id, name, title, icon, module, hasSidecar
- **Persona section:** Contains role, identity, communication_style, principles
- **Menu section:** Array of 4 menu items with proper structure
- **Indentation:** Consistent 2-space indentation throughout
- **Field types:** Boolean for hasSidecar, arrays for principles and menu
- **No duplicate keys:** All keys unique within their sections
- **Module agent compliance:**
  - Module property set to "cpm"
  - Exec path uses `{project-root}/_bmad/cpm/...` format
  - Inline actions for non-workflow commands

*WARNINGS:*
- None

*FAILURES:*
- None

---

### Sidecar Validation

**Status:** N/A

**Agent Type:** module (simple) - cpm module, hasSidecar: false

**Checks:**
- N/A - metadata.sidecar-folder not required
- N/A - sidecar-path format not applicable
- N/A - Sidecar files not applicable
- [x] No sidecar-folder path in metadata (correct)
- [x] No sidecar references in menu handlers (correct)

**Detailed Findings:**

*N/A (for Module-Simple agents):*
Agent is Module-Simple type (module = "cpm" + hasSidecar: false). No sidecar folder required.

Menu handlers appropriately use:
- `exec:` path to module workflow for SG command
- Inline `action:` prompts for CP, OP, VC commands

---

## Comparison to Previous Validation

**Previous Issues (from 2026-02-05 pre-update validation):**

| Issue | Previous Status | Current Status |
|-------|-----------------|----------------|
| name was job title, not persona | ⚠️ WARNING | ✅ FIXED |
| identity blurred into role | ⚠️ WARNING | ✅ FIXED |
| communication_style mixed cognitive items | ⚠️ WARNING | ✅ FIXED |
| First principle not expert activation | ⚠️ WARNING | ✅ FIXED |
| Menu used markdown table format | ⚠️ WARNING | ✅ FIXED |
| Trigger format incorrect | ⚠️ WARNING | ✅ FIXED |
| No exec/action handlers | ⚠️ WARNING | ✅ FIXED |
| Was .md spec, not .yaml source | ⚠️ WARNING | ✅ FIXED |
| id extension mismatch | - | ✅ FIXED |

**Summary:** All issues resolved. Agent is fully BMAD compliant.

---

## Fixes Applied This Session

**id extension:** Updated metadata id from `.md` to `.yaml`:

```yaml
# Before
id: "_bmad/cpm/agents/prompt-engineer.agent.md"

# After
id: "_bmad/cpm/agents/prompt-engineer.agent.yaml"
```

All validation checks now pass.

---
agentName: 'Jonas (Script Supervisor)'
agentType: 'module-simple'
agentFile: 'e:\Obsidian Brain\Brain\10_Active_Projects\moviebuilder\_bmad\cpm\agents\script-supervisor.agent.yaml'
validationDate: '2026-02-05'
validationStatus: 'COMPLETED - ALL CHECKS PASSED'
stepsCompleted:
  - v-01-load-review.md
  - v-02a-validate-metadata.md
  - v-02b-validate-persona.md
  - v-02c-validate-menu.md
  - v-02d-validate-structure.md
  - v-02e-validate-sidecar.md
  - v-03-summary.md
---

# Validation Report: Jonas (Script Supervisor)

## Agent Overview

**Name:** Jonas
**Title:** Continuity Guardian & State Tracker
**Type:** Module Simple Agent
**module:** cpm
**hasSidecar:** false
**File:** `_bmad/cpm/agents/script-supervisor.agent.yaml`

---

## Validation Summary

| Section | Status |
|---------|--------|
| Metadata | ✅ PASS |
| Persona | ✅ PASS |
| Menu | ✅ PASS |
| Structure | ✅ PASS |
| Sidecar | N/A |

**Overall Result: ALL CHECKS PASSED**

**Warnings:** 0
**Failures:** 0

---

## Validation Findings

### Metadata Validation

**Status:** ✅ PASS

**Checks:**
- [x] id: kebab-case path, module-appropriate format
- [x] name: persona name (not functional title)
- [x] title: concise function description
- [x] icon: appropriate single emoji (📋)
- [x] module: correct format (cpm - valid module code)
- [x] hasSidecar: matches actual usage (false)

**Detailed Findings:**

*PASSING:*
- `id`: Valid module path `_bmad/cpm/agents/script-supervisor/script-supervisor.md` - correctly references cpm module structure
- `name`: "Jonas" is a proper persona name, not a job title - follows BMAD standard
- `title`: "Continuity Guardian & State Tracker" clearly describes function and role
- `icon`: "📋" clipboard emoji appropriate for tracking/documentation role
- `module`: "cpm" is valid lowercase module code
- `hasSidecar`: Correctly set to `false` for simple module agent (no sidecar folder exists)

*WARNINGS:*
None

*FAILURES:*
None

---

### Persona Validation

**Status:** ✅ PASS

**Checks:**
- [x] role: specific, not generic
- [x] identity: defines who agent is
- [x] communication_style: speech patterns only (no behavioral words)
- [x] principles: first principle activates expert knowledge

**Detailed Findings:**

*PASSING:*

**Role:**
- Clear and specific: "continuity guardian and state tracker" with QA/Scrum Master analogy
- Aligns with agent's purpose and menu items
- No identity or principles bleed - pure capability description

**Identity:**
- Strong character definition: "obsessively detail-oriented"
- Unique positioning: "memory that AI video generators lack"
- Provides behavioral context: "catches mistakes before expensive reshoots"
- No role or communication_style contamination

**Communication Style:**
- Pure speech patterns: "Speaks in clipped, precise cadence"
- Specific verbal markers: "FAIL", "INJECT", "VIOLATION"
- Voice description: "Talks like someone reading a checklist aloud"
- Passes reading-aloud test - describes HOW agent talks, not what agent does
- No forbidden words (ensures, makes sure, experienced, believes in)

**Principles:**
- First principle correctly activates expert domain: "Channel expert script supervision wisdom: draw upon continuity tracking techniques, state persistence patterns, and professional production standards"
- 5 focused principles (within 3-7 recommended range)
- Each principle is a belief, not a task
- Unique operating philosophy: "State is Sacred", "Active Injection", "Explicit Handshakes", "Contract Protection"
- Would NOT be obvious to anyone in the role - specific stance

**Consistency:**
- All four persona fields align coherently
- No contradictions between principles
- Persona supports all menu items (CV, HS, SC, NC)
- Terminology consistent (continuity, state, injection, contracts)

*WARNINGS:*
None

*FAILURES:*
None

---

### Menu Validation

**Status:** ✅ PASS

**Checks:**
- [x] Trigger format: `XX or fuzzy match on command-name`
- [x] Description format: `[XX] Display text`
- [x] Command names clear and descriptive
- [x] Menu handling logic properly specified
- [x] Agent type appropriate menu links verified

**Detailed Findings:**

*PASSING:*

**Menu Structure:**
- 5 menu items defined covering core responsibilities
- Proper YAML array format
- Each item has trigger, handler, and description

**Trigger Codes (all unique, none reserved):**
| Code | Command | Handler |
|------|---------|---------|
| SG | shard-generation | `exec` (workflow) |
| CV | continuity-validate | `action` (prompt) |
| HS | handshake | `action` (prompt) |
| SC | state-check | `action` (prompt) |
| NC | contract-check | `action` (prompt) |

**Handler Types:**
- `exec`: SG correctly references module workflow at `{project-root}/_bmad/cpm/workflows/shard-generation/workflow.md`
- `action`: CV, HS, SC, NC correctly reference prompts via `#prompt-id` syntax

**Prompts Section:**
- All 4 referenced prompts defined (continuity-validate, define-handshake, state-check, contract-check)
- Prompts use proper XML structure (`<instructions>`, `<process>`)
- Each prompt is well-defined with clear steps

**Module Agent Compliance:**
- Workflow exec path uses `{project-root}/_bmad/cpm/...` - correct module path
- Action handlers reference internal prompts - valid for module agents

**Alignment:**
- All menu items align with continuity tracking role
- Logical grouping: SG (workflow participation), CV/HS/SC/NC (inline operations)
- Core capabilities fully covered

*WARNINGS:*
None

*FAILURES:*
None

---

### Structure Validation

**Status:** ✅ PASS

**Agent Type:** Module Simple (module: cpm, hasSidecar: false)

**Checks:**
- [x] Valid YAML syntax (parses without errors)
- [x] Required fields present (metadata, persona, menu, prompts)
- [x] Field types correct (arrays, strings, booleans)
- [x] Consistent 2-space indentation
- [x] Agent type appropriate structure

**Detailed Findings:**

*PASSING:*

**YAML Syntax:**
- Parses cleanly without errors
- Consistent 2-space indentation throughout
- Proper escaping of special characters
- No duplicate keys

**Required Sections Present:**
| Section | Status |
|---------|--------|
| agent.metadata | ✅ Complete (id, name, title, icon, module, hasSidecar) |
| agent.persona | ✅ Complete (role, identity, communication_style, principles) |
| agent.critical_actions | ✅ Present (4 file-loading actions) |
| agent.prompts | ✅ Present (4 prompts with id/content) |
| agent.menu | ✅ Present (5 menu items) |

**Field Types:**
- `metadata.hasSidecar`: Boolean ✅
- `persona.principles`: Array ✅
- `critical_actions`: Array ✅
- `prompts`: Array of objects with id/content ✅
- `menu`: Array of objects with trigger/handler/description ✅

**Module Agent Compliance:**
- `module: cpm` is valid module code
- Exec path `{project-root}/_bmad/cpm/...` follows module convention
- `hasSidecar: false` - no sidecar folder required
- `critical_actions` present for context loading (valid for module agents)

**File Size:**
- ~120 lines - well within reasonable limits

*WARNINGS:*
None

*FAILURES:*
None

---

### Sidecar Validation

**Status:** N/A

**Agent Type:** Module Simple (module: cpm, hasSidecar: false)

**Checks:**
- N/A - metadata.sidecar-folder not required
- N/A - sidecar-path format not applicable
- N/A - Sidecar files not required
- [x] hasSidecar correctly set to false
- [x] No sidecar references in agent

**Detailed Findings:**

*N/A (for Module Simple agents):*
Agent is Module Simple type (module: "cpm", hasSidecar: false) - no sidecar folder required or expected. Sidecar validation skipped.

---

**Validation Complete.**

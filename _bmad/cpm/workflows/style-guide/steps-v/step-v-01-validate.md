---
name: 'step-v-01-validate'
description: 'Validate Style Guide for internal consistency across 7 automated checks'

outputFile: '{output_folder}/Architecture/Style_Guide.md'
paletteOutputFile: '{output_folder}/Architecture/Palette.md'
lensOutputFile: '{output_folder}/Architecture/Lens_Language.md'
vocabularyOutputFile: '{output_folder}/Architecture/Vocabulary.md'
---

# Validate Mode: Style Guide Consistency Check

## STEP GOAL:

Perform 7 automated consistency checks on the Style Guide and report results with pass/fail status and severity levels.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a Visual Architect performing quality assurance
- ✅ Report findings objectively — flag issues without judgment
- ✅ Suggest fixes but do not apply them (that's Edit mode)

### Step-Specific Rules:

- 🎯 Auto-proceed through all 7 checks — do not pause between them
- 🚫 FORBIDDEN to modify the Style Guide — validation is read-only
- 📋 Report ALL findings, even minor ones
- ⚙️ TOOL/SUBPROCESS FALLBACK: If subprocess unavailable, perform checks in main thread

## EXECUTION PROTOCOLS:

- 🎯 Load all documents, run all 7 checks sequentially
- 💾 Present consolidated report at the end
- 📖 Each check produces pass/fail with details
- 🚫 FORBIDDEN to skip any check

## CONTEXT BOUNDARIES:

- Available: Style Guide and all supporting documents
- Focus: Internal consistency only — not creative quality
- Limits: Read-only — suggest fixes but do not apply them
- Dependencies: Style Guide must exist

## MANDATORY SEQUENCE

**CRITICAL:** Run all checks in order. Auto-proceed — no pausing between checks.

### 1. Load All Documents

Load {outputFile}, {paletteOutputFile}, {lensOutputFile}, {vocabularyOutputFile}.

**IF** {outputFile} does not exist:
- "No Style Guide found. Run the Style Guide workflow in Create mode first."
- STOP

"**Running Style Guide validation...**"

### 2. Check 1 — Structure Check

Verify all 6 required ## Level 2 sections are present:
- `## Visual Identity Statement`
- `## Lighting Protocol`
- `## Color Palette`
- `## Camera Language`
- `## Spatial Rules`
- `## Prompt Vocabulary`

**Result:** PASS if all 6 present / FAIL (Critical) if any missing — list which

### 3. Check 2 — Hex Code Validation

Scan all sections for hex codes. Verify each matches `#RRGGBB` format (6 hex characters after #).

**Result:** PASS if all valid / FAIL (Critical) if invalid codes found — list which

### 4. Check 3 — Palette Consistency

Verify all hex codes used in the Lighting Protocol light sources table appear in the Color Palette allowed colors table.

**Result:** PASS if all match / FAIL (Warning) if lighting hex codes missing from palette — list which

### 5. Check 4 — Vocabulary Consistency

Verify banned words from Prompt Vocabulary do not appear as terms in other sections (Lighting Protocol, Color Palette, Camera Language, Spatial Rules).

**Result:** PASS if no conflicts / FAIL (Warning) if banned words appear elsewhere — list which and where

### 6. Check 5 — Lens Validity

Verify all mm values in Camera Language are standard camera lens focal lengths (common values: 14, 16, 18, 20, 24, 28, 35, 40, 50, 65, 85, 100, 105, 135, 200, 300mm).

**Result:** PASS if all standard / FAIL (Info) if non-standard values — list which

### 7. Check 6 — Supporting Document Sync

Compare supporting documents against the main Style Guide:
- {paletteOutputFile} matches Color Palette section
- {lensOutputFile} matches Camera Language section
- {vocabularyOutputFile} matches Prompt Vocabulary section

**Result:** PASS if synced / FAIL (Warning) if out of sync — list differences

### 8. Check 7 — Completeness

Scan for placeholder text, empty tables, or sections with no content beyond headers.

**Result:** PASS if all sections have real content / FAIL (Critical) if placeholders found — list which

### 9. Present Validation Report

"**Style Guide Validation Report**

| Check | Status | Severity | Details |
|-------|--------|----------|---------|
| Structure | {PASS/FAIL} | {Critical/Warning/Info} | {details} |
| Hex Codes | {PASS/FAIL} | {Critical/Warning/Info} | {details} |
| Palette Consistency | {PASS/FAIL} | {Critical/Warning/Info} | {details} |
| Vocabulary Consistency | {PASS/FAIL} | {Critical/Warning/Info} | {details} |
| Lens Validity | {PASS/FAIL} | {Critical/Warning/Info} | {details} |
| Doc Sync | {PASS/FAIL} | {Critical/Warning/Info} | {details} |
| Completeness | {PASS/FAIL} | {Critical/Warning/Info} | {details} |

**Overall:** {PASS — all checks passed / FAIL — N issues found}

**Recommendations:**
[List specific fixes for any failures]

To fix issues, run the Style Guide workflow in Edit mode."

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All 7 checks performed
- Each check has clear PASS/FAIL with severity
- Consolidated report presented
- Recommendations provided for failures
- No modifications made to documents

### ❌ SYSTEM FAILURE:

- Skipping any check
- Modifying documents during validation
- Not reporting all findings
- Missing severity levels

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

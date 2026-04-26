---
stepsCompleted: [1, 2, 3, 4]
inputDocuments: []
session_topic: 'BMAD Cinematic Production Module (BMM-CPM) - applying Agile/BMAD methodology to AI video/film production'
session_goals: 'Define module structure, design agent definitions (Showrunner, Cinematographer, Script Supervisor, Prompt Engineer), map workflow steps and templates for SDLC to CPLC translation'
selected_approach: 'User-Selected Techniques'
techniques_used: ['Analogical Thinking', 'Persona Journey', 'What If Scenarios', 'Six Thinking Hats']
ideas_generated: 82
session_active: false
workflow_completed: true
context_file: ''
---

# Brainstorming Session Results

**Facilitator:** Alec
**Date:** 2026-02-01

## Session Overview

**Topic:** BMAD Cinematic Production Module (BMM-CPM) - applying Agile/BMAD methodology to AI video/film production

**Goals:**
- Define the module structure (how it fits into BMAD)
- Design the agent definitions (Showrunner, Cinematographer, Script Supervisor, Prompt Engineer)
- Map out workflow steps and templates for the SDLC → CPLC translation

**The Problem Being Solved:** The "Vibe-Drift Gap" - AI video tools lose continuity when prompting scene-by-scene, causing characters to change, environments to shift logic, and plots to lose their original requirements.

**The Solution Approach:** Map BMAD SDLC to Cinematic Production Life Cycle (CPLC)

| BMAD (Software) | CPM (Cinematics) | Deliverable |
|-----------------|------------------|-------------|
| Product Brief | Story Brief | Hook, genre, high-level summary |
| PRD | Show Bible | Character dossiers, world rules, themes |
| Architecture | Cinematic Style Guide | Lighting, color palettes, camera language |
| Stories/Epics | Beat Sheets / Scenework | Acts (Epics) and Scenes (Stories) |
| Sprint Planning | Production Slate | Tracking scene status |
| Dev Story | Scene Prompting | Dense, multi-modal video prompts |
| Code Review | Continuity Check | Bible compliance review |

### Session Setup

_Approach: User-Selected Techniques - Alec will browse the complete technique library to choose methods for this session._

---

## Technique Selection

**Approach:** User-Selected Techniques

**Selected Techniques:**

1. **Analogical Thinking** (Creative Innovation) - Deepen the SDLC → CPLC mapping for every component by finding the perfect cinematic equivalent for each software concept
2. **Persona Journey** (Theatrical Exploration) - Walk through a scene's creation from each agent's perspective (Showrunner → Cinematographer → Script Supervisor → Prompt Engineer) to ensure no context drops between handoffs
3. **What If Scenarios** (Creative Innovation) - Stress-test the framework with extreme cases, explore edge cases and hidden requirements
4. **Six Thinking Hats** (Structured Thinking) - Comprehensive analysis from all angles: Facts, Emotions, Benefits, Risks, Creativity, Process

**Selection Rationale:** This combination provides deep analogical mapping, experiential validation through persona embodiment, stress-testing via extreme scenarios, and structured multi-perspective analysis.

---

## Technique Execution: Analogical Thinking

### Continuity Acceptance Criteria (CAC) Framework

**[Continuity #1]**: Continuity Acceptance Criteria (CAC)
- *Concept:* A scene "passes QA" when the Script Supervisor Agent validates it against three document types: Show Bible (identity), Style Guide (visual), and Workflow-Status (temporal state). Failures trigger "Context Refactors."
- *Novelty:* Treats continuity as testable, automatable verification - not vibes.

**[Continuity #2]**: State-Diff Character Files
- *Concept:* Every character/asset has a Persistent State File (like JSON) that updates after each scene. Prompts are validated against `character_state_v12.doc` to ensure wounds, items, costumes persist.
- *Novelty:* Version-controlled character state - the "database" of your film.

**[Continuity #3]**: Visual Unit Tests
- *Concept:* The Cinematic Style Guide acts as an architecture doc with "illegal" visual descriptions. A "bright sunny day" in a Cyberpunk-Noir fails the visual linter.
- *Novelty:* Style enforcement as code review - you can literally lint a prompt.

**[Continuity #4]**: Narrative Logic Gates
- *Concept:* Workflow-Status tracks cause-and-effect chains. "Silver Key acquired in Scene 7" must appear in Scene 8's prompt or it fails the logic gate.
- *Novelty:* Dependency tracking for narrative - like a DAG of plot requirements.

**[Continuity #5]**: Narrative Contracts (Forward-Looking Validation)
- *Concept:* The Showrunner defines "Foreshadowing Contracts" - future payoffs that earlier scenes must honor. Scene 12's reveal creates contractual obligations on Scenes 7-11.
- *Novelty:* Prospective validation, not just retrospective. Like API contract testing for plot.

**[Continuity #6]**: Contract Testing for Cinema
- *Concept:* Before a scene is "prompted," verify it doesn't violate any active Narrative Contracts. Script Supervisor checks both backward (CAC) AND forward (contract compliance).
- *Novelty:* Bidirectional continuity enforcement.

### Three-Tiered Staging Pipeline

**[Pipeline #7]**: Three-Tiered Staging Pipeline
- *Concept:* Before any "GPU-Burn," scenes pass through Dev (Textual Dry Run) → UAT (Keyframe) → Staging (Low-Fi Animatic). Only then does Production Render happen.
- *Novelty:* Treats the AI Video Generator as a Deployment Target, not a brainstorming tool.

**[Pipeline #8]**: Textual Dry Run (Tier 1 - Dev Environment)
- *Concept:* Script Supervisor + Cinematographer analyze the prompt TEXT for "Logical Collisions" before any generation. "Protagonist running but Character State says broken leg = BUILD FAILED."
- *Novelty:* Zero GPU cost. Pure linguistic integration testing.

**[Pipeline #9]**: Keyframe Validation (Tier 2 - UAT Environment)
- *Concept:* Generate ONE static image to verify Character Likeness and Architecture Alignment. If the face drifts or lighting violates Style Guide, catch it before video burn.
- *Novelty:* 1 image credit vs 100 video credits. Container-like isolation.

**[Pipeline #10]**: Low-Fi Animatic (Tier 3 - Staging Server)
- *Concept:* High-speed, low-resolution "Motion Sketch" to test Cinematic Flow, Pacing, and Spatial Contracts. Not pixel-perfect - just movement logic.
- *Novelty:* Integration testing for motion before production render.

### Temporal Sharding / Cinematic Sprints

**[Temporal #11]**: Cinematic Sprints / Temporal Sharding
- *Concept:* Shard long scenes into 5s/10s/30s chunks to prevent "Context Rot" (AI hallucination/drift over long generation). Shorter = more control, longer = more autonomy.
- *Novelty:* Sprint Velocity is configurable and refactorable mid-project.

**[Temporal #12]**: Inter-Shard Handshake
- *Concept:* Exit State from Shard A (final frame + state-diff) becomes Entry Contract for Shard B. The Prompt Engineer uses last frame as Image-to-Video reference.
- *Novelty:* Explicit continuity hooks between temporal chunks. No assumption of AI memory.

**[Temporal #13]**: User-in-the-Loop Gate (Shard PR Review)
- *Concept:* After each 5s shard, pause for UAT. Accept = commit to Workflow-Status. Hotfix = mark bug, refactor prompt weight, regenerate only that shard.
- *Novelty:* Granular human approval. Bugs are isolated to shards, not entire scenes.

### Cinematic Debt Management

**[Debt #14]**: Component-Based Prompts / Asset ID System
- *Concept:* Instead of verbose descriptions, prompts use standardized Asset IDs: `[Asset: Hero_V4] [Outfit: Battle_Worn]`. A Context-Engineering Agent does "Quick-Lookup" and compiles to full descriptions at render time.
- *Novelty:* Clean working documents, optimized output prompts. Like importing libraries vs. copy-pasting code.

**[Debt #15]**: Context Squash (State Consolidation)
- *Concept:* Every 10-20 shards, Script Supervisor runs a "Refactoring Sprint" - bakes accumulated changes into a new Baseline State. Deletes messy history.
- *Novelty:* Git-squash for character state. Prevents 50-page State File monsters.

**[Debt #16]**: Visual Anchor Reset
- *Concept:* Cinematographer selects the "Best" shard from the last act as the new "Golden Reference." Future shards compare to THIS, not the original Pilot.
- *Novelty:* Rolling visual baseline. Prevents drift from months-old reference frames.

---

## Technique Execution: Persona Journey

### Scene 8 Walkthrough: The Abandoned Cathedral

**Test Scene:** Protagonist (battle-scarred, holding Silver Key from Scene 7) enters the Abandoned Cathedral. The Final Door is hidden behind the altar (setup for Scene 12). Cyberpunk-Noir lighting. Antagonist's footsteps heard.

### Showrunner Rulings (Atomic Cinematic Beats)

**[Sharding #17]**: Atomic Cinematic Beats
- *Concept:* The Showrunner provides "Global Requirements," but the Prompt Engineer decomposes them into 5-second beats, each with ONE primary focus.
- *Novelty:* No 5-second window can handle "everything" - requirement sharding is mandatory.

**[Sharding #18]**: Shot Sequence Architecture
- *Concept:* Scene 8 becomes three atomic shards:
  - 8.1: Entry & Burden (Character State + Style)
  - 8.2: Environment & Footsteps (Atmosphere + Tension)
  - 8.3: Contractual Seed (Narrative Contract plant)
- *Novelty:* Each beat owns ONE job. Clear separation of concerns.

**[Sharding #19]**: "Think in 5-Second Beats" Rule
- *Concept:* Even if user sets 60-second intervals, the system internally decomposes into 5-second beats to maintain quality.
- *Novelty:* Internal quality control regardless of user settings.

**[Sharding #20]**: Exit State → Reference Frame Handoff
- *Concept:* Script Supervisor ensures Beat 1's Exit State becomes Beat 2's Entry Contract. "Looking left at 0:05 = start Beat 2 looking left."
- *Novelty:* Explicit continuity between atomic beats.

### Cinematographer Rulings (Visual Architecture)

**[Visual #21]**: Chiaroscuro-Neon Protocol
- *Concept:* Mandate Volumetric Lighting with Rim Light from distant #FF00FF source. Without rim light, you lose "Cyberpunk" and get muddy Noir.
- *Novelty:* Named lighting protocols become enforceable standards.

**[Visual #22]**: Paranoia Lens Sequence (85mm → 24mm → 35mm)
- *Concept:* CU with 85mm (oppressive blur), Wide with 24mm (spatial distortion), Medium with 35mm (grounded reality).
- *Novelty:* Lens progression as emotional architecture - "heartbeat rhythm."

**[Visual #23]**: Dynamic Color Application
- *Concept:* Specify WHERE each color lives:
  - #FF00FF reflects on Silver Key (8.1)
  - #39FF14 illuminates dust from pillars (8.2)
  - Pure White-Noise = "Palette Break" for Out-of-Bounds assets (8.3)
- *Novelty:* Color as narrative signal, not just aesthetic.

**[Visual #24]**: Axis of Action Contract
- *Concept:* Hero enters Frame-Left → must be Left-Third in Wide → Over-Right-Shoulder in Medium. Altar stays on "Unexplored" side.
- *Novelty:* Spatial logic as contractual obligation.

**[Visual #25]**: Dynamic Lighting Tracking
- *Concept:* Script Supervisor tracks light source proximity. "If Hero moves past pillars, green light on face increases 20%."
- *Novelty:* Lighting as state variable.

**[Visual #26]**: Prompt Vocabulary Enforcement
- *Concept:* Prohibited words: "Bright" (kills Noir). Required: "High-Contrast," "Volumetric."
- *Novelty:* Cinematographer maintains a "style linter" for prompt language.

### Script Supervisor Rulings (Continuity & State)

**[Continuity #27]**: State Injection for Missing Attributes
- *Concept:* Script Supervisor catches gaps (torn shirt from Scene 7 not specified). Injects mandatory Asset Attribute into prompt queue.
- *Novelty:* QA agent actively patches gaps, doesn't just flag them.

**[Continuity #28]**: Explicit Scar Phrasing Mandate
- *Concept:* High-priority features get explicit text: "jagged scar on left cheek" to prevent AI drift.
- *Novelty:* Critical visuals get text injection, not just Asset ID references.

**[Continuity #29]**: Asset State Transitions
- *Concept:* Track not just "has item" but disposition: `Asset_SilverKey` from `In-Inventory` to `Equipped_Primary_Hand`.
- *Novelty:* Granular state tracking for asset disposition.

**[Continuity #30]**: Inter-Beat Handshake Specs
- *Concept:* Explicit Exit → Entry contracts:
  - 8.1→8.2: Mid-stride → Momentum snap-halt
  - 8.2→8.3: Head tilted left → Start tilted, slow rotation
- *Novelty:* Motion continuity as contractual obligation.

**[Continuity #31]**: Protected Object / Watchdog Rules
- *Concept:* Altar marked as Protected Object (Contract_ID: S12_ALTAR_SECRET). Any "examine altar" attempt between 8.3-12.1 = BUILD FAIL.
- *Novelty:* Narrative contracts enforced via automated blocking rules.

**[Continuity #32]**: Lighting Gradient Variables
- *Concept:* Cathedral X-axis = Lighting Gradient. Position drives #39FF14 intensity as trackable variable.
- *Novelty:* Spatial position drives lighting state.

### Prompt Engineer Rulings (Prompt Architecture)

**[Prompt #33]**: Structured Prompt Format
- *Concept:* Production prompts have labeled sections: `[Technical Header]`, `[Subject/Asset]`, `[Action/State]`, `[Environment/Lighting]`, `[Temporal Constraint]`.
- *Novelty:* Standardized prompt architecture - every agent knows where their specs land.

**[Prompt #34]**: Anchor Point Weighting
- *Concept:* Place critical features (Scar, Torn Shoulder) in first 25% of Subject block. AI attention mechanisms weight early tokens more heavily.
- *Novelty:* Prompt engineering informed by transformer architecture.

**[Prompt #35]**: Banned-Word Linter Compliance
- *Concept:* "Bright" literally nowhere in prompt. Cinematographer's vocabulary rules enforced at compile time.
- *Novelty:* Style guide violations caught before render.

**[Prompt #36]**: Exit-State Hook Embedding
- *Concept:* Prompt ends with "momentary halt, eyes dart upward" - this IS the handshake. Script Supervisor extracts as Entry Contract for next beat.
- *Novelty:* Continuity hooks built INTO prompt structure.

**[Prompt #37]**: Contextual Color Specification
- *Concept:* Not just "#FF00FF" but "#FF00FF electric purple rim light" - context (rim light) prevents color bleed into skin tones.
- *Novelty:* Color + application context = precise AI behavior.

---

## Technique Execution: Six Thinking Hats

### White Hat: Facts & Data

**[Analysis #38]**: Hard Facts Foundation
- *Concept:* CPM built on proven facts: State Decay measurable (3-10 sec drift), Prompt Attention finite (77 token priority), I2V is current continuity bridge, BMAD document-based approach works.
- *Novelty:* Framework grounded in documented AI behavior.

**[Analysis #39]**: Critical Assumptions to Validate
- *Concept:* Three assumptions need testing: Agentic Linter precision (False Negative rate), Multi-Model Interoperability (prompt syntax varies), Cost-Benefit Ratio (CPM pipeline vs. human fixing).
- *Novelty:* Explicit assumption logging prevents "works in theory" trap.

**[Analysis #40]**: External State Machine Architecture
- *Concept:* AI video is "State-less" (forgets). CPM = External State Machine (Agents + Docs) - proven in software, unproven in cinematic prompting.
- *Novelty:* Known architectural pattern applied to new domain.

**[Analysis #41]**: Validation Data Requirements
- *Concept:* Must measure: Token-Saturation Limit, Handoff Fidelity (visual jump-cut %), Inference Latency (human time vs. CPM time).
- *Novelty:* Testable metrics defined before build.

### Red Hat: Emotions & Intuition

**[Emotion #42]**: The Democratization Spark
- *Feeling:* EXCITEMENT - "Everyone has big ideas but can't get them into video." CPM bridges imagination to screen.
- *Why it matters:* This is the "why" that drives adoption. Liberation, not features.

**[Emotion #43]**: The Context Anxiety
- *Feeling:* UNEASE - Agents need reliable access to consistent content at any moment. Fear of dropped context.
- *Why it matters:* Quick-Lookup system and Asset ID architecture must be bulletproof.

**[Emotion #44]**: The Prompt Overflow Fear
- *Feeling:* UNEASE - Prompt Engineer might give too much for video generation length. Chunking must be automatic.
- *Why it matters:* Points to need for "Prompt Budget" validation.

**[Emotion #45]**: The Liberation Gut-Check
- *Feeling:* GUT SAYS LIBERATION - Not overhead. Discovery, not drudgery.
- *Why it matters:* If it feels like overhead, adoption dies.

### Yellow Hat: Benefits & Value

**[Value #46]**: Studio-in-a-Box
- *Benefit:* Single individual becomes Studio Executive. Framework handles "Logic Load," human stays pure "Visionary."
- *Impact:* Crew of 200 → Crew of 1.

**[Value #47]**: From Video to IP
- *Benefit:* Sharded, standardized context enables 22-episode seasons with HBO-level character consistency.
- *Impact:* Economy of Scale for storytelling.

**[Value #48]**: Death of Visual Dementia / Character Lottery
- *Benefit:* No more "Vibe-Grief" - spending 6 hours making Shot B match Shot A.
- *Impact:* Eliminates most heartbreaking part of AI filmmaking.

**[Value #49]**: Elimination of Prompt Fatigue
- *Benefit:* Script Supervisor remembers bleeding ear. Cinematographer remembers hex-code. Freedom from administrative overhead.
- *Impact:* Creative energy stays creative.

**[Value #50]**: Long-Range Narrative Payoffs
- *Benefit:* Narrative Contracts enable actual foreshadowing. Plant briefcase in Ep 1, system ensures it's under bed in Ep 6.
- *Impact:* Mystery/Suspense genres become POSSIBLE in AI cinema.

**[Value #51]**: Transmedia Continuity / Universal Identity System
- *Benefit:* State Files are JSON/Markdown. Same Character State → Image Gen OR Video Gen. Identical character across media.
- *Impact:* Build once, render everywhere.

**[Value #52]**: Reliability as Feature (Gambling → Engineering)
- *Benefit:* Others burn GPU on "lucky guesses." CPM users build with precision. Three-Tiered Staging = only render what passes.
- *Impact:* Zero-Waste Production.

**[Value #53]**: Infinite Series Advantage
- *Benefit:* Episode 10 costs same effort as Episode 1. Manual prompters' effort INCREASES with complexity.
- *Impact:* Sustainable long-form production.

**[Value #54]**: Context as Currency
- *Benefit:* Treating context with BMAD rigor unlocks Hollywood-scale storytelling with fraction of resources.
- *Impact:* Philosophical foundation of CPM.

### Black Hat: Risks & Caution

**[Risk #55]**: Hallucination Cascade / Iterative Corruption
- *Risk:* One missed detail gets "Committed to Main." Subsequent shards stabilize ERROR. By Shard 8.10, protagonist is different person.
- *Mitigation needed:* Stronger review gates, automated visual diff, rollback mechanisms.

**[Risk #56]**: Moving Target Problem
- *Risk:* AI Video Models not standardized. Runway Gen-4 could ignore 85mm specs - Prompt Library becomes "Legacy Trash."
- *Mitigation needed:* Model-agnostic prompt layer, abstraction that compiles to different targets.

**[Risk #57]**: Black Box Non-Determinism
- *Risk:* Same "perfect prompt" 10 times = 10 different results. Rigorous process yields random luck.
- *Mitigation needed:* Seed control, reference anchoring, "good enough" thresholds.

**[Risk #58]**: Bureaucracy Burnout / Decision Fatigue
- *Risk:* 2-minute trailer = 24 UATs. User becomes "Button-Masher," approving "Good Enough" shards.
- *Mitigation needed:* Batch approval, confidence-based auto-approve, YOLO mode.

**[Risk #59]**: Barrier to Entry / Rube Goldberg Fear
- *Risk:* 10 Markdown files + 50 Narrative Contracts = creators abandon for simpler "Vibe-Generators."
- *Mitigation needed:* Progressive disclosure, templates, Quick Start mode.

**[Risk #60]**: The Ever-Evolving Reality
- *Insight:* CPM must be designed for constant evolution. Not finished product - living framework.
- *Mitigation:* Modular architecture, easy updates, community feedback loops.

### Green Hat: Creativity & Alternatives

**[Solution #61]**: Visual Regression Agent (VLM-QA)
- *Solution to:* Hallucination Cascade
- *Concept:* GPT-4o/Gemini Pro Vision as Unit Test Runner. VLM "watches" shards, compares pixels against State File. Automatic Re-Roll if mismatch detected.
- *Impact:* Fail-fast automated regression testing for movies.

**[Solution #62]**: Cinematic Transpiler / Universal Cinematic Language
- *Solution to:* Moving Target Problem
- *Concept:* Decouple Story Logic from Model Syntax. Write in UCL, swappable Model Adapters transpile to Sora/Kling/Runway.
- *Impact:* CPM becomes future-proof.

**[Solution #63]**: Exception-Based Review / Confidence Scoring
- *Solution to:* Decision Fatigue
- *Concept:* VLM-QA + Script Supervisor give Continuity Confidence Score. 95%+ = Auto-Commit. User only sees "Conflict Shards."
- *Impact:* User becomes Creative Director, not Button-Masher.

**[Solution #64]**: Agentic Inception / The Interview
- *Solution to:* Barrier to Entry
- *Concept:* No Markdown files to start. Chat with Showrunner: "Tell me about the hero." Agent writes PRD + Style Guide + Character State in background.
- *Impact:* Play-first onboarding. Engineering = side effect.

**[Solution #65]**: Automating the Boredom (Core Philosophy)
- *Concept:* Agents handle Rigid Discipline. Humans provide Soul.
- *Impact:* Philosophical foundation of CPM's UX.

### Blue Hat: Process & Next Steps

**[Implementation #66]**: MVP = Skeleton Project
- *Concept:* Standardized Project Template + Agent System Prompts in `/.cpm_agents/`. Deliverable: one verified 5-second Compiled Prompt.
- *Impact:* Minimal viable proof.

**[Implementation #67]**: Schema Definition (Dependency 1)
- *Concept:* Define EXACTLY how Character State is written. Machine-readable consistency.
- *Impact:* Foundation for all agent cross-referencing.

**[Implementation #68]**: Context Index (Dependency 2)
- *Concept:* `manifest.md` or `project.json` tells agent which files are relevant. Prevents Prompt Bloat.
- *Impact:* Scoped context loading.

**[Implementation #69]**: State-Diff Ritual (Dependency 3)
- *Concept:* Claude MUST read `last_frame_state.md` BEFORE drafting `current_shard_prompt.md`. Non-negotiable.
- *Impact:* Enforced continuity handshake.

**[Implementation #70]**: Two-Shard Handshake Test (Validation)
- *Concept:* Generate Shard A (pick up item). Agent generates Shard B from exit state. Success = item in hand + lighting maintained WITHOUT reminder.
- *Impact:* Smallest test that proves CPM works.

**[Implementation #71]**: V1.0 Scope (Headless Production)
- *Concept:* Terminal interface, manual agent triggers, text-based State Files, 5-second atomic shards, direct prompting.
- *Impact:* Build foundation before automating.

**[Implementation #72]**: V2.0 Scope (Automated Studio)
- *Concept:* Integrated CLI, VLM integration, variable intervals, Model-Agnostic Transpiler.
- *Impact:* Dream state after V1.0 proven.

**[Implementation #73]**: Cinematics as Code Philosophy
- *Concept:* User never talks to video generator without Agentic Crew reviewing "Code" first. Disciplined, version-controlled process.
- *Impact:* Soul of CPM approach.

---

## Technique Execution: What If Scenarios

### Scale Stress Tests

**[Scale #74]**: Lazy Loading / Scene-Specific Dependency Injection
- *Scenario:* 10-hour feature with 50 characters
- *Solution:* Script Supervisor doesn't load all 50 state files. Only "imports" files for characters "on camera." Background characters use `Crowd_LOD.md` (Level of Detail) - summarized "minified" version.
- *Impact:* Monster state file sharded into manageable modules.

### Edge Case Solutions

**[Edge #75]**: Temporal Versioning (Git-Style Tags)
- *Scenario:* Character dies in Scene 5 but appears in flashback in Scene 12
- *Solution:* Call versioned assets: `/Characters/Hero@Scene_04`. Script Supervisor ignores current "Dead" state, pulls from Scene 4 commit.
- *Impact:* Temporal forks handled via version control.

**[Edge #76]**: Twin Identity Differentiation
- *Scenario:* Same actor plays twins with identical appearance
- *Solution:* Unique Token IDs with Behavioral ID (e.g., `[Behavior: Twin_A_Nervous_Tick]`). Visual Diff in Style Guide (e.g., "Twin A wears ring on left hand").
- *Impact:* Identical appearance, distinct identity tracking.

### Collaboration Solutions

**[Collab #77]**: Branching Narratives / Git-Based Collaboration
- *Scenario:* Two directors changing same character state
- *Solution:* CPM is just a directory - use standard Git. `git checkout -b dark-timeline`. Merge conflicts require manual resolution of "Visual Logic" before next shard can be prompted.
- *Impact:* 50 years of software versioning solves 100 years of cinematic production problems.

### Model Migration Solutions

**[Migration #78]**: Model-Agnostic Transpilation
- *Scenario:* Sora shuts down, must move to Runway mid-project
- *Solution:* Prompt Engineer writes in UCL. Swap `model_config.yaml` in project root. Claude "Re-Compiles" from Sora-Syntax to Runway-Syntax. State Files and Show Bible never change.
- *Impact:* Only the "compiler" changes, not the source code.

### Retroactive & Override Solutions

**[Retcon #79]**: State Refactoring / Retcon-Commit
- *Scenario:* Retroactively adding hero's limp at Scene 15
- *Solution:* Update Global Character State, Script Supervisor marks Scenes 1-14 as "Legacy-Build" / "Dirty Context." Any re-render compiles with new trait.
- *Impact:* Retroactive continuity changes without rewriting history.

**[Override #80]**: Style Override / Scoped Config
- *Scenario:* Dream sequence where all rules break
- *Solution:* Create `Scene_10_Dream/` folder with local `style_override.md`. Cinematographer ignores Global Style Guide, prioritizes local override.
- *Impact:* Controlled rule-breaking without contaminating main style.

**[Skinning #81]**: Thematic Skinning / Multi-Target Deployment
- *Scenario:* Same scene in Cyberpunk-Noir AND Watercolor-Fantasy
- *Solution:* Story Beats (Logic) separate from Style Guide (CSS). Swap theme file at compile time. Same narrative, different visual compilation.
- *Impact:* A/B testing of styles. Visual themes as swappable skins.

### New Paradigm Discovery

**[Paradigm #82]**: Living Repository Genre / Open Source Movies
- *Scenario:* What new genre does CPM enable?
- *Solution:* Move from "Finished Films" to "Cinematic Repositories." Creators release CPM Project Folders. Fans fork repos, branch at any scene, change Narrative Contracts, re-compile movies. Original Cut = Main Branch.
- *Impact:* Cinema becomes Open Source. Narrative becomes collaborative. Stories become living, forkable, infinite.

---

## Idea Organization and Prioritization

### Thematic Clusters (10 Themes)

| Theme | Focus | Ideas | V1.0 Priority |
|-------|-------|-------|---------------|
| 1. Core Testing (CAC) | "Did this scene PASS?" | #1-6, #61 | CRITICAL |
| 2. Pipeline Architecture | "When do we render?" | #7-10, #63 | CRITICAL |
| 3. Temporal Architecture | "How do we chunk time?" | #11-13, #17-20, #30 | CRITICAL |
| 4. State Management | "What's the current truth?" | #14, #27-32, #74-75, #79 | CRITICAL |
| 5. Visual Architecture | "Does it LOOK right?" | #21-26, #80-81 | HIGH |
| 6. Prompt Engineering | "How do we talk to AI?" | #33-37, #62, #78 | CRITICAL |
| 7. Debt Management | "How do we stay clean?" | #15-16, #55-60 | MEDIUM |
| 8. Agent Definitions | "Who does what?" | Persona Journey outputs | CRITICAL |
| 9. Implementation | "How do we build?" | #66-73 | ROADMAP |
| 10. Paradigm Innovations | "Why this matters" | #46-54, #64-65, #77, #82 | VISION |

### Prioritization Results

**CRITICAL (Must Have V1.0):**
- Directory Template Structure
- Four Agent System Prompts
- Show_Bible.md + Character_State.md templates
- Style_Guide.md + Vocabulary.md templates
- manifest.md (Context Index)
- Structured Prompt Format
- State-Diff Ritual
- Two-Shard Handshake Test

**HIGH (V1.0 Nice-to-Have):**
- Narrative Contracts logging
- Protected Objects / Watchdog Rules
- Dynamic Lighting Tracking
- Lens Language documentation

**V2.0 (Future):**
- VLM-QA Visual Regression
- Cinematic Transpiler / UCL
- Exception-Based Review
- Agentic Inception Onboarding
- Git-Based Collaboration
- Thematic Skinning

---

## CPM V1.0 Build Roadmap Summary

### Phase 1: Foundation (Week 1)
- Master Directory Structure
- config.yaml Schema
- manifest.md (Context Index)

### Phase 2: Bible & Architecture (Week 1-2)
- Show_Bible.md Template
- Character State Template
- Style_Guide.md Template
- Vocabulary.md (Banned/Required Words)

### Phase 3: Agent Definitions (Week 2)
- showrunner.md Agent Prompt
- cinematographer.md Agent Prompt
- script-supervisor.md Agent Prompt
- prompt-engineer.md Agent Prompt

### Phase 4: Workflow Rituals (Week 2-3)
- Shard Generation Ritual
- State-Diff Check Protocol
- Two-Shard Handshake Test

### Phase 5: Integration & Testing (Week 3-4)
- Test Scene Specification (Scene 8: Cathedral)
- V1.0 Complete Checklist
- Validation: 3 consecutive handshake passes

### V1.0 Deliverables (14 items)
| # | Deliverable | Type |
|---|-------------|------|
| 1 | Master Directory Structure | Folder Template |
| 2 | config.yaml Schema | Configuration |
| 3 | manifest.md Schema | Context Index |
| 4 | Show_Bible.md Template | Bible |
| 5 | Character State Template | Bible |
| 6 | Style_Guide.md Template | Architecture |
| 7 | showrunner.md | Agent Prompt |
| 8 | cinematographer.md | Agent Prompt |
| 9 | script-supervisor.md | Agent Prompt |
| 10 | prompt-engineer.md | Agent Prompt |
| 11 | Shard Generation Ritual | Workflow |
| 12 | Two-Shard Handshake Test | Validation |
| 13 | Test Scene Specification | Integration |
| 14 | V1.0 Complete Checklist | Quality Gate |

---

## Session Summary and Insights

### Key Achievements

**Quantitative:**
- 82 breakthrough ideas generated
- 4 techniques fully executed
- 10 thematic clusters identified
- 14 V1.0 deliverables defined
- Complete implementation roadmap created

**Qualitative:**
- Invented Continuity Acceptance Criteria (CAC) - unit testing for cinema
- Designed Three-Tiered Staging Pipeline - Dev/UAT/Staging for video
- Created Temporal Sharding architecture - atomic 5-second beats
- Validated workflow via Persona Journey - Showrunner → Cinematographer → Script Supervisor → Prompt Engineer
- Identified and solved major risks (Hallucination Cascade, Decision Fatigue, Moving Target)
- Discovered paradigm shift: "Living Repository Genre" / Open Source Movies

### Breakthrough Concepts

1. **"Context as Currency"** - The core insight that treating context with engineering rigor unlocks Hollywood-scale storytelling
2. **"Cinematics as Code"** - 50 years of software engineering solving 100 years of cinematic production problems
3. **"External State Machine"** - AI video is stateless; CPM provides the external memory
4. **"Automating the Boredom"** - Agents handle rigid discipline; humans provide soul
5. **"Studio-in-a-Box"** - Democratization of the blockbuster; crew of 200 → crew of 1

### Session Reflections

**What Worked:**
- Analogical Thinking unlocked the core SDLC → CPLC mapping
- Persona Journey validated the workflow by LIVING it as each agent
- Six Thinking Hats provided balanced analysis (facts, feelings, value, risks, solutions, plan)
- What If Scenarios stress-tested edge cases and revealed new possibilities

**Creative Strengths Demonstrated:**
- Deep systems thinking - naturally maps concepts at architectural level
- Pattern recognition - sees software parallels in cinematic workflows
- Solution orientation - every risk identified got a concrete solution
- Visionary thinking - "Open Source Movies" represents genuine paradigm shift

### The CPM Philosophy

> "By keeping everything in a directory, we can use the last 50 years of Software Engineering to solve the last 100 years of Cinematic Production problems."

> "We're turning AI filmmaking into a disciplined, version-controlled process where the user never talks to a video generator without their Agentic Crew having reviewed the 'Code' first."

---

## Next Steps

1. **This Week:** Create the Master Directory Structure (Phase 1)
2. **Week 2:** Build Bible and Architecture templates (Phase 2)
3. **Week 2-3:** Write all four Agent Prompts (Phase 3)
4. **Week 3:** Document Shard Generation Ritual and run Handshake Test (Phase 4)
5. **Week 4:** Complete Test Scene (Cathedral) and validate V1.0 (Phase 5)

---

## Session Metadata

**Session Date:** 2026-02-01
**Facilitator:** Carson (Brainstorming Coach)
**Participant:** Alec
**Duration:** Extended deep session
**Techniques Used:** Analogical Thinking, Persona Journey, Six Thinking Hats, What If Scenarios
**Total Ideas:** 82
**Output:** Complete CPM V1.0 Build Roadmap

---

*This brainstorming session produced a complete framework design for the BMAD Cinematic Production Module, from philosophical foundations to specific deliverables. The CPM represents a paradigm shift in AI-assisted filmmaking: treating cinematics as code, context as currency, and stories as living repositories.*

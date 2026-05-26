# CVF Cross-Agent Memory Progression Roadmap

Memory class: ROADMAP_RECORD

docType: roadmap

Date: 2026-05-26

Status: PROPOSED_SEQUENTIAL_GATES_AUTHORIZATION_REQUIRED_PER_STEP

Authorization Model: SEQUENTIAL ONLY

Authors:

- Operator (decision intent: "chậm và chắc khi có đầy đủ evidence")
- Claude Opus 4.7 (roadmap synthesis)

---

## Status

Step 1 Alpha: CLOSED (commit `910043af`).
Step 2 Beta: CLOSED_PASS_BOUNDED for active operator toolchain.
Step 3 Gamma: T0 readiness audit CLOSED_PASS_BOUNDED; T1-T5 local MCP
memory-bootstrap implementation CLOSED_PASS_BOUNDED.
Step 4 Delta: DEFERRED_DEMAND_GATED pending Gamma evidence + product
direction decision.

Status update 2026-05-26:

- Beta closed with active toolchain evidence: Claude Haiku
  PASS_WITH_MINOR_NOTE, Gemini PASS, Cursor/Aider waived by operator because
  they are not active tools.
- Gamma-T0 closed the readiness audit. Existing
  `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER` builds and passes local tests, and
  should be reused as the Gamma substrate rather than creating a second MCP
  tree.
- Gamma-T1-T5 closed local MCP memory-bootstrap implementation. The existing
  MCP server now exposes seven guard tools plus seven Gamma memory/governance
  tools. Local SDK-client stdio verification passes. External third-party
  client auto-start remains operator-tested before any Alpha/Beta retirement.

## Authorization Or Decision

Operator stated 2026-05-26:

> "chọn alpha vì đơn giản, nhưng không phải lâu dài, chúng ta cần xử lý
> cho hoàn thiện hơn"

> "thiết kế nó thành 3 bước nối tiếp. chậm và chắc khi có đầy đủ evidence"

Decision basis:

- Alpha is a bridge implementation, not a long-term solution.
- Operator wants complete cross-agent memory infrastructure.
- Sequential progression preferred over bundled one-shot to preserve
  evidence-driven decisions.
- Operator authorization required per step. No agent self-dispatches
  beyond bridge step (Alpha).

This roadmap establishes the sequence. Each future step's implementation
requires its own GC-018 with operator ACCEPT after this roadmap.

## Purpose

Establish a sequential progression from the closed Alpha bridge step
toward complete cross-agent memory infrastructure. Alpha is the already
shipped bridge/prerequisite; the three future steps are Beta, Gamma, and
Delta. Each future step is bounded, evidence-gated, and reversible.
Operator authorization required per step. No bundling permitted.

## Why This Tranche

Establish a sequential 3-step progression from Alpha bridge toward
complete cross-agent memory infrastructure that does not depend on
agent compliance for loading session state.

Each step is bounded, evidence-gated, and reversible. Each step builds
on previous step's empirical evidence rather than speculative
architecture.

This roadmap PREVENTS bundling steps into one tranche. Bundling would
violate:

- WC-4 Knowledge Absorption Blind-Spot Standard (thin proof + closure
  delta required per tranche).
- F-1 Diminishing Returns Stop Rule (do not expand scope beyond
  evidence).
- Anti-pattern AP4 from concept doc 2026-05-26 ("architectural
  commitment before operator evidence").
- Anti-pattern AP5 from concept doc 2026-05-26 ("convergence loop
  length as quality signal").

## Scope

This roadmap covers the cross-agent memory loading mechanism only.

In scope:

- Step 2 Beta: per-tool config files extending the soft auto-load
  pattern Alpha established (Gemini, Cursor, Aider, future tools).
- Step 3 Gamma: cvf-mcp-server build and deployment for true
  cross-tool integration via MCP standard.
- Step 4 Delta: production hardening (uptime SLA, caching, audit log
  integration, multi-tenant) only when scale evidence justifies.

Out of scope:

- VI5 Surface 1 / Surface 2 work (separate tranche family).
- L1 multilingual mediation (separate tranche family).
- Non-coder usability tests (separate tranche family).
- Provider/adapter/route changes (forbidden in this roadmap).
- Public-sync / hosted readiness / freeze release (separate tranches).

## Non-Goals

This roadmap does NOT authorize:

- Bundled implementation of multiple steps.
- Speculative Gamma design without Beta evidence.
- Speculative Delta planning without Gamma evidence and product
  direction decision.
- Replacing Alpha before Gamma proven.
- Replacing CVF_SESSION_MEMORY.md as canonical front door.
- Bypassing operator authorization gate at any step.
- Auto-promotion from one step to the next without explicit operator
  ACCEPT.

## Work Plan

### Step 2 Beta: Per-Tool Config Coverage Expansion

Gate: CLOSED_PASS_BOUNDED for active operator toolchain.

Sub-tranches:

- Beta-T1: Audit which AI coding tools the project must support
  (Gemini, Cursor, Aider, others identified by operator).
- Beta-T2: For each tool, add config file with same instruction
  pattern Alpha uses for CLAUDE.md and AGENTS.md.
- Beta-T3: Verify each tool's agent respects the mandatory startup
  acknowledgment after config added.

Estimated effort per tool: ~30-60 minutes (config file + test note).

Total Beta effort: depends on tool count. Typical 3-5 tools = 2-4
hours total work, spread across 1-2 sessions.

Acceptance criteria for Beta:

- One config file per supported tool committed.
- Each tool's startup behavior verified (manual test note or screen
  capture).
- No tool change breaks existing CLAUDE.md or AGENTS.md behavior.
- No runtime change, no provider change, no route change.
- Bounded to soft auto-load extension; same limitations as Alpha
  documented.

Beta produces evidence required for Step 3 Gamma:

- Which tools accept soft pattern reliably?
- Which tools require additional config (e.g., system prompt
  integration)?
- Does soft pattern scale to N tools without ceremony tax?

### Step 3 Gamma: cvf-mcp-server Build

Gate: Gamma-T1-T5 CLOSED_PASS_BOUNDED for local MCP server and local SDK-client
verification.

- Beta evidence available (or operator explicitly waives Beta
  prerequisite with reason recorded).
- Operator authorizes Gamma with fresh GC-018.

Sub-tranches:

- Gamma-T0: Existing MCP surface readiness audit and reuse/deconflict
  decision. CLOSED_PASS_BOUNDED on 2026-05-26.
- Gamma-T1: MCP server scaffold (TypeScript, dependencies, minimum
  tool registration). After Gamma-T0, default approach is reuse/adapt
  `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER` rather than create a new server tree.
  CLOSED_PASS_BOUNDED as part of Gamma-T1-T5.
- Gamma-T2: Core memory tools (`get_session_memory()`,
  `get_active_handoff()`, `get_session_state()`). CLOSED_PASS_BOUNDED as
  `cvf_get_session_memory`, `cvf_get_active_handoff`, and
  `cvf_get_session_state`, plus `cvf_get_startup_acknowledgment`.
- Gamma-T3: Governance tools (`get_rules(topic)`,
  `check_governance(action)`). CLOSED_PASS_BOUNDED as
  `cvf_get_governance_rules` and `cvf_check_governance_action`.
- Gamma-T4: Local deployment + client setup guides (Claude Code,
  Codex CLI, Gemini, others per Beta evidence). CLOSED_PASS_BOUNDED for local
  setup guide and generic stdio MCP config.
- Gamma-T5: Cross-tool verification (live test from each supported
  client). CLOSED_PASS_BOUNDED for local SDK-client stdio verification;
  external operator UI client auto-start remains operator-tested.

Estimated effort: multi-tranche project. Each sub-tranche ~weeks of
work depending on scope decisions made at GC-018 time.

Acceptance criteria for Gamma (overall):

- MCP server running locally with all 5 core tools exposed.
- At least 2 MCP-compatible clients (Claude Code + Codex CLI) verified
  calling tools at session start.
- Tool responses match repo state (read-after-write consistency).
- Server availability documented (start/stop procedure, health check).
- Audit log captures every tool call.
- No runtime change to existing CVF tranches.
- Deprecation plan for Alpha mandatory ack documented (Alpha retired
  only after Gamma proven, not as part of Gamma).

Gamma-T1-T5 closure evidence:

- GC-018:
  `docs/baselines/CVF_GC018_GAMMA_T1_T5_MCP_MEMORY_BOOTSTRAP_2026-05-26.md`.
- Completion:
  `docs/reviews/CVF_GAMMA_T1_T5_MCP_MEMORY_BOOTSTRAP_COMPLETION_2026-05-26.md`.
- Local setup:
  `docs/guides/CVF_GAMMA_MCP_SERVER_LOCAL_SETUP_2026-05-26.md`.
- Verification:
  `npm run test:run` PASS 17 files / 485 tests, `npm run build` PASS,
  `npm run verify:gamma` PASS with 14 tools and rawSecretPrinted=false.

Gamma decision point after T5:

- If cross-tool verification passes: Gamma complete; operator decides
  whether to retire Alpha mandatory ack.
- If cross-tool verification reveals gaps: bounded follow-up tranches,
  not scope expansion.
- If MCP standard insufficient for CVF needs: re-evaluate before
  Gamma-T6 or roll back to Beta-only.

### Step 4 Delta: Production Hardening

Gate: DEFERRED_DEMAND_GATED. Cannot dispatch until:

- Gamma proven (all Gamma sub-tranches CLOSED_PASS_BOUNDED).
- Operator decides CVF product direction (internal tool vs
  commercial product vs open source distribution).
- Operator authorizes Delta with fresh GC-018 referencing scale
  evidence.

Sub-tranches: defined only after Gamma proven and product direction
decided. Not pre-scoped here. Likely includes (subject to operator
decision):

- Server uptime SLA + monitoring
- Caching strategy
- Update push notifications
- Audit log integration with external systems
- Multi-tenant support (if CVF scales beyond operator's single use)
- Authentication layer
- Rate limiting
- Backup/disaster recovery

Estimated effort: weeks-months across multiple tranches. Not committed
in this roadmap.

Acceptance criteria for Delta: defined per sub-tranche at GC-018 time,
based on Gamma evidence and product direction decision.

## Sequencing Rationale

Why sequential not bundled:

1. **Evidence-driven design.** Beta provides multi-tool data needed
   to scope Gamma correctly. Gamma provides runtime data needed to
   scope Delta correctly. Bundling = speculation chain.

2. **Operator authority preservation.** Operator's defining role is
   per-step evaluation. Bundling removes evaluation gate between
   steps.

3. **Anti-patterns avoided.** AP4 (architectural commitment before
   evidence) and AP5 (convergence loop length as quality signal) from
   concept doc 2026-05-26 explicitly forbid speculative long-range
   architecture.

4. **Reversibility preserved.** Sequential gates allow rolling back
   any step without affecting later steps. Bundled = all-or-nothing.

5. **Operator throughput.** Smaller decisions = faster operator
   evaluation = faster overall progress despite serial sequence.

Wait periods between steps recommended:

- Beta → Gamma wait: 1-2 weeks operating with Beta. Long enough to
  observe multi-tool soft pattern behavior across typical session
  count. Short enough to maintain momentum.
- Gamma → Delta wait: indefinite. Wait until scale evidence justifies
  hardening investment. Operator may decide Gamma sufficient
  indefinitely.

## Acceptance Criteria

Roadmap-level acceptance (this document):

- Sequential gate model recorded explicitly.
- Each step's WORK_ORDER_READY / DEMAND_GATED / DEFERRED status
  documented.
- Bundling prohibition explicit in Non-Goals.
- Re-evaluation gates between steps documented.

Step-level acceptance criteria: defined per step above.

Roadmap closure: this roadmap is not closed by implementing all steps.
It remains active reference until cvf-mcp-server (Gamma) ships
successfully, at which point it transitions to historical record.

## Verification Or Evidence

This roadmap is documentation-only. No code, no live proof, no runtime
change.

Verification:

- Read concept doc
  `docs/concepts/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`
  for rules basis (Rules A1-A4, anti-patterns AP1-AP5).
- Read concept doc
  `docs/concepts/CVF_CROSS_AGENT_MEMORY_AND_AUTO_LOAD_ASSESSMENT_2026-05-26.md`
  for assessment basis (4 options analyzed).
- Verify Alpha shipped at commit `910043af` (`CLAUDE.md` Mandatory
  Startup Acknowledgment section).

Future implementation evidence per step requires its own GC-018,
focused tests when applicable, and live proof when runtime behavior
claimed.

## Claim Boundary

This roadmap does NOT claim:

- Implementation of Beta, Gamma, or Delta.
- Authorization to dispatch Beta, Gamma, or Delta.
- Speculative scope or design of Gamma or Delta beyond high-level
  description.
- cvf-mcp-server availability, hosting, or performance.
- Universal AI tool support.
- Production readiness.
- Public release readiness.
- Freeze posture changes.

The roadmap records the sequential progression and operator's
authorization model. Each step requires its own fresh GC-018 with
operator ACCEPT before implementation.

## Related Artifacts

Predecessor documents:

- `docs/concepts/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`
  (rules basis, anti-patterns AP1-AP5)
- `docs/concepts/CVF_CROSS_AGENT_MEMORY_AND_AUTO_LOAD_ASSESSMENT_2026-05-26.md`
  (assessment of 4 options)

Alpha implementation evidence:

- Commit `910043af` (Mandatory Startup Acknowledgment added to
  CLAUDE.md and AGENTS.md)
- `docs/baselines/CVF_GC018_ALPHA_MANDATORY_STARTUP_ACKNOWLEDGMENT_2026-05-26.md`

Cross-agent infrastructure (current state):

- `CVF_SESSION_MEMORY.md`
- `CLAUDE.md`
- `AGENTS.md`
- `AGENT_HANDOFF_V13_2026-05-25.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

Standards referenced:

- WC-4 Knowledge Absorption Blind-Spot Prevention Standard
  (`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`)
- F-1 Diminishing Returns Stop Rule (referenced in AGENTS.md)
- GC-018 Continuation Candidate Template
- GC-020 Handoff In-Place Update Rule

Companion rule formalization:

- `docs/concepts/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`
  amendment adding Rule BP1 (Bridge Implementation Pattern) — to be
  committed alongside this roadmap.

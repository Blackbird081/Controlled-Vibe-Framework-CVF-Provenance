# GC-018: W3 Tool MCP Database Action Taxonomy

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-24

Roadmap: `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`

Work Order: `docs/work_orders/CVF_WO_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_2026-05-24.md`

---

## Purpose

Authorize WC-3 Candidate 3 as W3: add a bounded, read-only action taxonomy for
tool, MCP, command, and database-facing operations so future CLI/MCP/API-key
surfaces can classify side effects, approval posture, trace requirements, and
diagnostic classes before any execution integration is opened.

## Scope / Target / Owner Boundary

In scope:

- `governance/contracts/tool-action-taxonomy.ts`
- `governance/contracts/tool-action-taxonomy.test.ts`
- W3 completion review, WC roadmap, session state, and handoff updates

Out of scope:

- runtime tool execution;
- MCP server/client bridge implementation;
- database driver or database mutation implementation;
- `/api/execute` route changes;
- provider behavior, model routing, or live provider semantics;
- governance evidence receipt envelope changes;
- auth/RBAC changes;
- public-sync or production-readiness claims;
- freeze release.

Owner surface: `governance/contracts` cross-channel governance contract helpers.

## Depth Audit

Depth score: 8/10.

Rationale:

- WC-3 ranks tool/MCP/database governance as Candidate 3 because CLI/MCP/API-key
  users need failures and side effects to be classified before retry, approval,
  or escalation.
- Existing `governance/contracts/cross-channel-guard-contract.ts` already owns
  canonical cross-channel phase/risk/decision vocabulary. W3 can add an
  adjacent taxonomy helper instead of inventing a runtime or policy engine.
- Existing `cvf-web` tool registry role policy is useful but too shallow for
  side-effect, transport, database, and MCP action classification.
- The highest risk is accidentally opening execution authority. W3 therefore
  authorizes only deterministic taxonomy/evaluation helpers and tests.

## Source / Predecessor Evidence

- WC roadmap:
  `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- WC-3 map:
  `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- WC-4 blind-spot standard:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Existing cross-channel contract:
  `governance/contracts/cross-channel-guard-contract.ts`
- Existing web tool registry and role guard:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/tool-registry-catalog.ts`
  and
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/tool-policy-guard.ts`

## Decision / Baseline / Proposed Tranche

Decision: continue with W3 as the third W-series implementation tranche.

Baseline: CVF has role-based web tool inventory and canonical guard types, but
no shared taxonomy for normalizing tool/MCP/database action side effects,
approval levels, trace requirements, or failure/diagnostic posture.

Proposed tranche:

- add a deterministic `cvf.toolActionTaxonomy.w3.v1` contract helper;
- normalize action kind, surface, side-effect class, transport, and database
  family into canonical risk and decision posture;
- emit secret-safe evaluation metadata with approval, trace, sandbox,
  mutation-capture, rollback, and diagnostic-class requirements;
- preserve a hard boundary that the helper classifies planned actions only and
  cannot execute tools, MCP calls, commands, or database operations.

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - `.private_reference/legacy/CVF ADD/CLI-Anything/` — 11 files
  - `.private_reference/legacy/CVF 16.5/OpenAgentd/` — 11 files
  - `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/` — 9 files
  - `.private_reference/legacy/CVF ADD/gridex/` — 9 files
  - `.private_reference/legacy/CVF ADD/cortex-hub/` — 11 files
  - active contract/tool surfaces under `governance/contracts/` and
    `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/`
- Prior absorption evidence resolved:
  - `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
  - `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
  - `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md`
  - `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md`
  - `docs/reviews/CVF_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_COMPLETION_2026-05-24.md`
  - `docs/reviews/CVF_CANONICAL_CLI_RUNTIME_GATEWAY_COMPLETION_2026-05-22.md`
  - `docs/reviews/CVF_D2_PROVIDER_CAPABILITY_MATRIX_COMPLETION_2026-05-22.md`
- Detailed source files used:
  - `.private_reference/legacy/CVF ADD/CLI-Anything/CVF_AGENT_NATIVE_TOOL_SURFACE_MODEL.md`
  - `.private_reference/legacy/CVF ADD/CLI-Anything/CVF_TOOL_SURFACE_POLICY_RULEBOOK.md`
  - `.private_reference/legacy/CVF ADD/CLI-Anything/CVF_SANDBOXED_TOOL_EXECUTION_PROFILE.md`
  - `.private_reference/legacy/CVF ADD/CLI-Anything/CVF_COMMAND_RUNTIME_TOOL_ADAPTER_SPEC.md`
  - `.private_reference/legacy/CVF ADD/CLI-Anything/CVF_TOOL_SURFACE_STRUCTURED_SPEC.md`
  - `.private_reference/legacy/CVF 16.5/OpenAgentd/CVF_MCP_TOOL_BOUNDARY_POLICY.md`
  - `.private_reference/legacy/CVF 16.5/OpenAgentd/CVF_LOCAL_SANDBOX_PERMISSION_POLICY.md`
  - `.private_reference/legacy/CVF 16.5/OpenAgentd/CVF_TOOL_CALL_TRACE_PROTOCOL.md`
  - `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/mcp-business-tool-contract.ts`
  - `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/mcp-business-risk-classifier.ts`
  - `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/mcp-business-approval-gate.ts`
  - `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/mcp-business-transport-policy.ts`
  - `.private_reference/legacy/CVF ADD/gridex/CVF_DATABASE_ACTION_MODEL.md`
  - `.private_reference/legacy/CVF ADD/gridex/CVF_DATABASE_POLICY_BINDING.md`
  - `.private_reference/legacy/CVF ADD/gridex/CVF_DATABASE_AUDIT_TRACE_MODEL.md`
  - `.private_reference/legacy/CVF ADD/cortex-hub/CVF_MCP_CORTEX_BRIDGE_SPEC.md`
  - `.private_reference/legacy/CVF ADD/cortex-hub/CVF_CORTEX_CAPABILITY_MATRIX.md`
  - `.private_reference/legacy/CVF ADD/cortex-hub/CVF_CORTEX_TRACE_AND_AUDIT_MODEL.md`
- Source families skipped:
  - provider method normalization: Candidate 5, not W3.
  - operational benchmark scorecard: Candidate 4, not W3.
  - external skill/model ingestion from Hugging Face or Hermes: demand-gated
    until action governance exists.
  - runtime database adapter implementation: explicitly deferred.
- File-level accepted value:
  - CLI-Anything: governed tool surfaces need identity, side-effect class,
    policy class, sandbox binding, traceability, rollback readiness, and
    separate install vs invoke policy.
  - OpenAgentd: MCP is a tool boundary, not a governance bypass; every MCP
    call needs permission check, DLP when needed, tool trace, and audit.
  - pancake-pos-mcp: business MCP actions need risk classification,
    approval-gate decisions, transport restrictions, and execution receipts.
  - gridex: database actions need normalized action families, review-before-run
    posture, environment zone policy, approval class, and trace.
  - cortex-hub: MCP/capability providers are interface bridges only; missing
    policy or trace is a hard stop.
- Owner-surface normalization:
  - shared taxonomy -> `governance/contracts/tool-action-taxonomy.ts`;
  - canonical risk/decision mapping -> existing cross-channel contract types;
  - proof -> focused `governance/contracts` tests;
  - future runtime use -> demand-gated follow-up only.
- Accept/defer/reject matrix:
  - ACCEPT_NOW: action side-effect taxonomy, approval posture, trace/sandbox
    flags, database family classification, and diagnostic class mapping.
  - ACCEPT_NOW: default-deny for unknown, privileged, untraced, or unscoped
    action requests.
  - ACCEPT_AS_OWNER_MAP: CVF web tool registry and future CLI/MCP surfaces may
    later consume the taxonomy after fresh work order.
  - DEFER_DEMAND_GATED: runtime tool invocation, MCP bridge execution, database
    adapter execution, UI policy readout, route integration, and public claims.
  - REJECT_DIRECT: direct external tool execution, direct MCP hub authority,
    direct database mutation, provider/tool bypass, and silent retries without
    diagnostic classification.
- Adversarial roles completed:
  - Implementer: a pure contract helper is the smallest bounded proof.
  - Skeptic/Auditor: source families are execution-heavy; W3 must not claim
    runtime enforcement from taxonomy tests.
  - Product/Operator Advocate: end users get a future path to "why was my
    CLI/MCP/API-key action blocked or approval-gated?" instead of `success=false`
    with no cause.
  - Safety/Boundary Owner: no action may execute from this tranche; high-risk
    mutations remain unavailable without later approval and runtime work.
- Thin proof target:
  - tests prove read-only actions classify as low-risk trace-required allow;
    workspace/database/external mutations escalate; destructive/privileged or
    unscoped actions block; unknown actions default-deny with an actionable
    diagnostic class.
- Blind-spot verdict: CLEAR

## Authorized Change

Implement W3 as a bounded cross-channel contract helper:

- create deterministic action taxonomy types and evaluator;
- map side-effect classes to canonical risk and decision posture;
- require trace for all accepted actions and mutation capture/rollback for
  mutation-capable actions;
- require sandbox/approval for mutation, install, external, privileged, MCP,
  and database operations as appropriate;
- classify unknown or under-specified actions as blocked with diagnostic class;
- keep runtime execution impossible.

## Evidence Plan

- `npm test -- tool-action-taxonomy.test.ts` in `governance/contracts`
- `python governance/compat/check_governed_file_size.py --enforce`
- markdown/session governance guards
- mandatory release gate if W3 closure asserts governance behavior beyond local
  taxonomy; otherwise local-contract boundary must be explicit.

## Acceptance Criteria

- [ ] Read-only local/tool/database inspection actions classify as trace-required
      low-risk allow or log-only posture.
- [ ] Workspace mutation, external mutation, install-capable, MCP, and database
      write/export/admin/recovery actions classify into approval/sandbox/trace
      posture.
- [ ] Destructive, privileged, unscoped, or unknown actions block or escalate
      deterministically.
- [ ] Every decision includes a secret-safe diagnostic class and user action.
- [ ] Tests prove no helper executes a tool, MCP call, command, or database
      operation.
- [ ] Focused contract tests PASS.
- [ ] Completion review filed and session/handoff updated.

## Claim Boundary

W3 may claim only deterministic local taxonomy/evaluation of planned
tool/MCP/command/database actions. It does not claim runtime enforcement,
live MCP execution, command execution, database execution, provider behavior,
receipt-envelope changes, public capability graduation, production readiness,
or freeze release.

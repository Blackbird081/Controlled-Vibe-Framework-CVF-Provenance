# CVF Work Order: W3 Tool MCP Database Action Taxonomy

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: work_order

Date: 2026-05-24

Tranche: W3

Roadmap: `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`

GC-018: `docs/baselines/CVF_GC018_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_2026-05-24.md`

---

## Purpose

Close WC-3 Candidate 3 with a bounded governance-contract proof: CVF should
classify planned tool, MCP, command, and database-facing actions before any
future runtime surface attempts to execute them.

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Orchestrator | Keep W3 scoped to taxonomy/contract helper and commit separately. |
| Legacy Source Extractor | Pull only action-taxonomy concepts that fit existing CVF owner surfaces. |
| Implementer | Add deterministic action taxonomy evaluator and focused tests. |
| QA | Run focused contract tests and docs/session guards. |
| Skeptic/Auditor | Reject runtime execution, MCP bridge, database adapter, and receipt-envelope expansion. |
| Product/Operator Advocate | Confirm classifications answer end-user "what failed/why blocked/what next" needs. |
| Safety/Boundary Owner | Confirm high-risk actions remain unavailable without fresh runtime authorization. |

## Authority Chain

- Operator instruction: continue through the roadmap in priority order and
  commit after each part.
- W2 closure:
  `docs/reviews/CVF_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_COMPLETION_2026-05-24.md`
- WC roadmap:
  `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- WC-3 map:
  `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- WC-4 standard:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- GC-018:
  `docs/baselines/CVF_GC018_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_2026-05-24.md`

## Scope / Target / Owner Boundary

Allowed files:

- `governance/contracts/tool-action-taxonomy.ts`
- `governance/contracts/tool-action-taxonomy.test.ts`
- W3 baseline, work order, completion review
- WC roadmap/session/handoff progress updates

Forbidden files/classes:

- `/api/execute` route and provider adapters;
- MCP server/client bridge implementation;
- database runtime adapter or database driver execution;
- `GovernanceEvidenceReceipt` envelope types;
- auth/RBAC;
- public-sync;
- hosted/production/freeze-release surfaces.

## Required First Reads

- `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- `docs/baselines/CVF_GC018_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_2026-05-24.md`
- `.private_reference/legacy/CVF ADD/CLI-Anything/CVF_AGENT_NATIVE_TOOL_SURFACE_MODEL.md`
- `.private_reference/legacy/CVF ADD/CLI-Anything/CVF_TOOL_SURFACE_POLICY_RULEBOOK.md`
- `.private_reference/legacy/CVF ADD/CLI-Anything/CVF_SANDBOXED_TOOL_EXECUTION_PROFILE.md`
- `.private_reference/legacy/CVF ADD/CLI-Anything/CVF_COMMAND_RUNTIME_TOOL_ADAPTER_SPEC.md`
- `.private_reference/legacy/CVF 16.5/OpenAgentd/CVF_MCP_TOOL_BOUNDARY_POLICY.md`
- `.private_reference/legacy/CVF 16.5/OpenAgentd/CVF_LOCAL_SANDBOX_PERMISSION_POLICY.md`
- `.private_reference/legacy/CVF 16.5/OpenAgentd/CVF_TOOL_CALL_TRACE_PROTOCOL.md`
- `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/mcp-business-tool-contract.ts`
- `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/mcp-business-risk-classifier.ts`
- `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/mcp-business-approval-gate.ts`
- `.private_reference/legacy/CVF ADD/gridex/CVF_DATABASE_ACTION_MODEL.md`
- `.private_reference/legacy/CVF ADD/gridex/CVF_DATABASE_POLICY_BINDING.md`
- `.private_reference/legacy/CVF ADD/gridex/CVF_DATABASE_AUDIT_TRACE_MODEL.md`
- `.private_reference/legacy/CVF ADD/cortex-hub/CVF_MCP_CORTEX_BRIDGE_SPEC.md`
- `.private_reference/legacy/CVF ADD/cortex-hub/CVF_CORTEX_CAPABILITY_MATRIX.md`
- `governance/contracts/cross-channel-guard-contract.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/tool-registry-catalog.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/tool-policy-guard.ts`

## Pre-Flight Checks

- Confirm W2 is closed pass bounded.
- Confirm W3 GC-018 includes the Knowledge Absorption Blind-Spot Control Block.
- Confirm implementation stays in `governance/contracts`.
- Confirm no runtime execution claim is made from local contract tests.
- Confirm any failed live/API proof, if later added, follows the V3 live-run
  diagnostic standard before rerun.

## Write Ownership

Implementation ownership:

- `governance/contracts/tool-action-taxonomy.ts`
- `governance/contracts/tool-action-taxonomy.test.ts`

Documentation ownership:

- W3 GC-018, work order, completion review
- WC roadmap status update
- active session state, front door, and handoff sync

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - `.private_reference/legacy/CVF ADD/CLI-Anything/`
  - `.private_reference/legacy/CVF 16.5/OpenAgentd/`
  - `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/`
  - `.private_reference/legacy/CVF ADD/gridex/`
  - `.private_reference/legacy/CVF ADD/cortex-hub/`
  - active `governance/contracts` and web tool registry files.
- Prior absorption evidence resolved:
  - WC-3 map
  - legacy spec absorption registry and blindspot audit
  - W1 and W2 closure packets
  - canonical CLI runtime gateway closure
  - D2 provider capability matrix closure
- Detailed source files used:
  - source files listed in Required First Reads.
- Source families skipped:
  - provider method normalization, operational benchmark scorecard,
    external model/skill ingestion, and runtime database adapter families.
- File-level accepted value:
  - tool side-effect declarations;
  - policy class and approval posture;
  - sandbox and trace requirements;
  - MCP boundary is not a bypass;
  - business/database mutations need review, approval, and trace;
  - missing policy or trace is a hard stop.
- Owner-surface normalization:
  - cross-channel governance contract helper under `governance/contracts`.
- Accept/defer/reject matrix:
  - ACCEPT_NOW: taxonomy, deterministic evaluator, diagnostic posture.
  - ACCEPT_AS_OWNER_MAP: future web/CLI/MCP/database runtime consumers.
  - DEFER_DEMAND_GATED: execution, bridge, adapter, route, UI, and public claim
    integrations.
  - REJECT_DIRECT: direct external tool/MCP/database authority and silent
    action retry without classified diagnostic posture.
- Adversarial roles completed:
  - Implementer: pure taxonomy helper is sufficient for W3.
  - Skeptic/Auditor: tests cannot prove runtime enforcement.
  - Product/Operator Advocate: classification gives users a future explanation
    path for blocked or failed actions.
  - Safety/Boundary Owner: high-risk mutations remain unavailable.
- Thin proof target:
  - focused contract tests cover read-only allow, mutation escalation, MCP
    transport risk, database action policy, destructive block, and unknown
    default-deny.
- Blind-spot verdict: CLEAR

## Execution Plan

1. Add `tool-action-taxonomy.ts` with action taxonomy types, defaults, and
   evaluator.
2. Add tests for read-only, local mutation, workspace mutation, MCP external
   mutation, database read/write/export/admin, destructive/privileged, and
   unknown actions.
3. Keep the helper side-effect free and free of runtime adapters.
4. Run focused contract tests.
5. Run governance compatibility/docs checks and release gate if closure makes
   a governance behavior claim beyond local taxonomy.
6. File completion review and update roadmap/session/handoff.
7. Commit W3 closure.

## Acceptance Criteria

- [ ] The helper exposes `cvf.toolActionTaxonomy.w3.v1`.
- [ ] Read-only actions evaluate as trace-required low-risk allow/log-only.
- [ ] Mutation-capable actions require sandbox/trace/mutation capture and
      approval posture.
- [ ] MCP/database/external actions receive stronger posture than local
      utility actions.
- [ ] Unknown or under-specified actions default-deny with actionable
      diagnostic fields.
- [ ] No runtime execution path exists in W3 code.
- [ ] Focused contract tests PASS.
- [ ] Completion review, roadmap, session state, and handoff are updated.

## Evidence Requirements

- Focused `governance/contracts` tests PASS.
- Markdown/docs/session guards PASS.
- Completion review records claim boundary and public catalog N/A unless a
  public-safe capability claim is explicitly added.

## Review Gate

Reject W3 pass if:

- implementation executes any tool, command, MCP call, or database action;
- implementation changes `/api/execute`, providers, auth/RBAC, or receipt
  envelope types;
- unknown or unscoped actions can be allowed;
- mutation actions do not require trace and approval/sandbox posture;
- completion claims live runtime behavior without live proof.

## Closure Checklist

- [ ] GC-018 and work order committed before implementation.
- [ ] Tool/MCP/database action taxonomy implemented.
- [ ] Focused contract tests PASS.
- [ ] Markdown/docs/session guards PASS.
- [ ] Completion review filed.
- [ ] WC roadmap/session/handoff updated.
- [ ] Final tranche commit created.

## Return Conditions

Return to orchestrator instead of closing if:

- useful Candidate 3 value requires runtime MCP/tool/database execution;
- taxonomy cannot be expressed without receipt-envelope changes;
- existing guard contract package cannot host the helper without broad
  refactoring;
- W3 would need public-sync or production-readiness claims.

## Operator Checkpoint

No additional operator checkpoint is required for local taxonomy W3. A new
checkpoint is required before runtime tool execution, MCP bridge wiring,
database adapter execution, route integration, UI policy readout, public-sync,
production claims, or freeze-release behavior.

## Claim Boundary

This work order authorizes only local taxonomy/evaluation for planned
tool/MCP/command/database actions. It does not authorize runtime enforcement,
live MCP execution, command execution, database execution, provider behavior,
public capability claims, production readiness, or freeze release.

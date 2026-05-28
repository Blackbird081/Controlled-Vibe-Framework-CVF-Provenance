# CVF W3 Tool MCP Database Action Taxonomy Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-05-24

---

## Purpose

Close W3 by adding a local cross-channel governance contract helper for planned
tool, MCP, command, and database-facing action classification without opening
runtime execution, MCP bridge wiring, or database mutation.

## Scope / Target / Owner Boundary

Target implementation:

- `governance/contracts/tool-action-taxonomy.ts`
- `governance/contracts/tool-action-taxonomy.test.ts`

Owner: Codex implementation under W3 work order.

Out of scope:

- runtime tool execution;
- MCP server/client bridge implementation;
- database runtime adapter or driver execution;
- `/api/execute` route changes;
- provider behavior;
- governance evidence receipt envelope changes;
- auth/RBAC;
- public-sync update;
- production readiness;
- freeze release.

## Evidence Trace

Evidence Trace Block:

- Claim: W3 source absorption used the detailed tool/MCP/database files from
  WC-3 Candidate 3, not only the WC-3 summary.
- Command:
  `Get-ChildItem -Recurse -File` for `CLI-Anything`, `OpenAgentd`,
  `pancake-pos-mcp`, `gridex`, and `cortex-hub`; plus `rg` for risk,
  approval, trace, sandbox, mutation, database, and MCP terms.
- Result: file counts confirmed as 11, 11, 9, 9, and 11; high-signal files
  identified and cited in the W3 GC-018 Control Block.
- Key path:
  `docs/baselines/CVF_GC018_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_2026-05-24.md`
- Verdict: EXISTS.
- Counter-evidence: sources contain runtime/adapter execution patterns; W3
  accepted only taxonomy and deferred runtime execution.

Evidence Trace Block:

- Claim: W3 implements deterministic local action taxonomy and does not execute
  tools, commands, MCP calls, or database operations.
- Command:
  `npm test -- tool-action-taxonomy.test.ts`
- Result: PASS, 1 file, 11 tests.
- Key path:
  `governance/contracts/tool-action-taxonomy.test.ts`
- Verdict: EXISTS.
- Counter-evidence: none; tests assert exported functions are only taxonomy
  version, evaluator, and runtime-execution false helper.

Evidence Trace Block:

- Claim: W3 did not regress existing cross-channel governance contracts.
- Command:
  `npm test` in `governance/contracts`
- Result: PASS, 3 files, 109 tests.
- Key path:
  `governance/contracts/cross-channel-guard-contract.test.ts`
- Verdict: EXISTS.
- Counter-evidence: no package main/export widening was performed.

Evidence Trace Block:

- Claim: repository-level live governance release gate remains healthy after
  W3.
- Command:
  `python scripts/run_cvf_release_gate_bundle.py --json`
- Result: PASS, 7/7 checks.
- Key path:
  `scripts/run_cvf_release_gate_bundle.py`
- Verdict: EXISTS.
- Counter-evidence: W3 itself still makes no live tool/MCP/database runtime
  claim.

## Source / Predecessor Evidence

Authorization:

- `docs/baselines/CVF_GC018_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_2026-05-24.md`
- `docs/work_orders/CVF_WO_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_2026-05-24.md`

Predecessors:

- `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_COMPLETION_2026-05-24.md`
- `docs/reviews/archive/CVF_CANONICAL_CLI_RUNTIME_GATEWAY_COMPLETION_2026-05-22.md`
- `docs/reviews/archive/CVF_D2_PROVIDER_CAPABILITY_MATRIX_COMPLETION_2026-05-22.md`

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - `.private_reference/legacy/CVF ADD/CLI-Anything/` — 11 files
  - `.private_reference/legacy/CVF 16.5/OpenAgentd/` — 11 files
  - `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/` — 9 files
  - `.private_reference/legacy/CVF ADD/gridex/` — 9 files
  - `.private_reference/legacy/CVF ADD/cortex-hub/` — 11 files
  - active `governance/contracts` and web tool registry files
- Prior absorption evidence resolved:
  - WC-3 map
  - legacy spec absorption registry and blindspot audit
  - W1 and W2 closure packets
  - canonical CLI runtime gateway closure
  - D2 provider capability matrix closure
- Detailed source files used:
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
- Source families skipped:
  - provider method normalization, operational benchmark scorecard,
    external model/skill ingestion, runtime database adapter implementation.
- File-level accepted value:
  - side-effect declarations;
  - approval and sandbox posture;
  - MCP is a governed tool boundary;
  - business/database mutations require review, approval, and trace;
  - missing policy or trace is a hard stop.
- Owner-surface normalization:
  - `governance/contracts/tool-action-taxonomy.ts`.
- Accept/defer/reject matrix:
  - `ACCEPT_NOW`: taxonomy, deterministic evaluator, diagnostic posture.
  - `ACCEPT_AS_OWNER_MAP`: future web/CLI/MCP/database consumers.
  - `DEFER_DEMAND_GATED`: execution, bridge, adapter, route, UI, public claim
    integrations.
  - `REJECT_DIRECT`: direct external tool/MCP/database authority and silent
    action retry without classified diagnostic posture.
- Adversarial roles completed:
  - Implementer: pure taxonomy helper is sufficient for W3.
  - Skeptic/Auditor: tests do not prove runtime enforcement and closure must
    not claim it.
  - Product/Operator Advocate: classifications create a future explanation path
    for blocked/approval-gated CLI/MCP/API-key actions.
  - Safety/Boundary Owner: all runtime execution remains unavailable.
- Thin proof target:
  - read-only allow, mutation escalation, MCP transport risk, database policy,
    destructive block, and unknown default-deny.
- Blind-spot verdict: CLEAR.

## Findings / Decisions

W3 adds `cvf.toolActionTaxonomy.w3.v1`, a deterministic evaluator that returns:

- canonical risk and decision posture;
- approval level;
- trace and audit-receipt requirements;
- sandbox, mutation-capture, and rollback posture;
- `runtimeExecutionAuthorized=false`;
- a secret-safe diagnostic class and user action.

Classification behavior:

- read-only local and database-read actions can classify as low-risk `ALLOW`
  when scoped and trace-bound;
- local mutations require review/sandbox/mutation-capture posture;
- workspace, external, MCP, install, database write/export actions escalate
  until required posture is satisfied;
- database schema/recovery/admin actions classify as critical approval posture;
- destructive and privileged actions block under W3 boundary;
- unknown or under-specified actions default-deny with actionable diagnostics.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Taxonomy mistaken for runtime enforcement | Output hard-codes `runtimeExecutionAuthorized=false` and no executor export exists |
| MCP becomes a governance bypass | MCP surface always requires scope, trace, and sandbox posture |
| Database read becomes too restrictive | Database read remains target-scoped and trace-bound but does not require sandbox |
| Mutation actions are allowed without trace | missing trace binding blocks before approval can matter |
| Destructive/privileged actions slip through taxonomy | W3 blocks them and requires a fresh runtime work order |

## Decision / Recommendation / Disposition

Disposition: `CLOSED_PASS_BOUNDED`.

Recommendation: Candidate 4 from WC-3, operational benchmark scorecard, becomes
the next ranked candidate. It remains demand-gated and must start with a fresh
GC-018/work order and WC-4 Control Block. It should consume existing evidence
logs and diagnostics, not open broad provider soak loops.

## Verification

- Focused contract tests:
  `npm test -- tool-action-taxonomy.test.ts`
  - PASS, 1 file, 11 tests.
- Full `governance/contracts` tests:
  `npm test`
  - PASS, 3 files, 109 tests.
- Live provider proof:
  `python scripts/run_cvf_release_gate_bundle.py --json`
  - PASS, 7/7.
  - W3 itself changes only local contract taxonomy and no live route/provider
    behavior.

## Public Catalog

Public catalog update: N/A.

Reason: W3 is a private cross-channel taxonomy helper. It does not add a public
capability surface, runtime execution path, or public-safe product claim.

## Tranche Closure Checklist

- [x] Public catalog updated OR explicitly N/A: N/A, no public capability
      added.
- [x] GC-020 handoff Current HEAD updated to this tranche's commit SHA: to be
      synced after commit.
- [x] Evidence Trace Block present for all significant claims (GC-046).
- [x] Legacy Spec Scan Block present OR explicitly N/A: covered by the
      Knowledge Absorption Blind-Spot Control Block.
- [x] Knowledge Absorption Blind-Spot Control Block present OR explicitly N/A:
      present.
- [x] Live-run diagnostics standard followed: release gate live proof PASS;
      no failed live/API run occurred and no rerun was performed after an
      unclear live failure.

## Claim Boundary

W3 claims only deterministic local taxonomy/evaluation for planned
tool/MCP/command/database actions. It does not claim runtime enforcement,
live MCP execution, command execution, database execution, provider behavior,
receipt-envelope changes, public capability graduation, production readiness,
or freeze release.

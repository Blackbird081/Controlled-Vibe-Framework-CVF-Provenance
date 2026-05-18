# CVF Legacy Concept Axis Matrix

Memory class: FULL_RECORD
Status: CORRECTION MATRIX AFTER CLAUDE FIVE-AXIS REBUTTAL

## Purpose

Provide the concept-axis, bidirectional trace that was missing from the first
Codex folder-axis absorption matrix.

This file corrects the structural defect identified in:

- `docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_CLAUDE_REBUTTAL_TO_CODEX_FIVE_AXIS_NONCOMPLIANCE_2026-05-18.md`

It traces each major legacy concept from source files to current CVF files, or
to the literal value `none` when no current CVF file implements that concept.

## Scope

Reviewed legacy scope remains limited to the four operator-approved folders:

- `.private_reference/legacy/CVF 16.5`
- `.private_reference/legacy/CVF 17.05`
- `.private_reference/legacy/CVF ADD`
- `.private_reference/legacy/CVF Edit`

No runtime implementation is authorized by this matrix.

## Source

Primary upstream artifacts:

- `docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_AUDIT_MATRIX_2026-05-18.md`
- `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`
- `docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_CLAUDE_REBUTTAL_2026-05-18.md`
- `docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_CLAUDE_REBUTTAL_TO_CODEX_FIVE_AXIS_NONCOMPLIANCE_2026-05-18.md`

## Methodology

Each row uses the six controlled dispositions required by the operator-approved
methodology:

| Disposition | Meaning |
|---|---|
| `absorbed` | current CVF has an implemented or canonical surface matching the concept |
| `partially_absorbed` | current CVF has pieces, but composition or enforcement is incomplete |
| `doc_only` | current CVF has doctrine/docs but no enforceable runtime binding |
| `not_absorbed` | no current CVF owner surface exists |
| `rejected_or_superseded` | concept is reference-only or intentionally replaced |
| `needs_gc018` | concept is ready for a future tranche but must not be implemented without GC-018 |

Severity values:

`blocker | high | medium | low | noise`

Path verification rule:

- Every concrete entry in `Current CVF files` must resolve with `Test-Path`.
- Rows whose disposition is about a public claim boundary rather than runtime
  implementation may append `[claim-boundary]` after the concrete file path.
- For absorbed guard rows, `Blocks` may describe what a violation would block;
  those rows are not claiming an unresolved implementation gap.

## Findings

Codex's first matrix was useful as a folder inventory, but not sufficient as an
absorption proof. The concept-axis matrix below is now the controlling review
view for Phase A freeze. The folder-axis matrix remains a companion inventory.

## Risk

Without this matrix, future agents can repeat the previous error: report that a
folder was reviewed while silently collapsing multiple concepts into one broad
row. This file reduces that risk by requiring both legacy source paths and
current CVF file paths per concept row.

## Concept Axis Matrix

### 1. Role

| Concept sub-item | Legacy source files | Current CVF files | Disposition | Severity | Blocks | Linked GAPs |
|---|---|---|---|---|---|---|
| Agent function role taxonomy | `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_ROLE_CATALOG.md`; `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_AGENT_ORCHESTRATOR_ROLE_ABSORPTION_GAP_CODEX_AUDIT_2026-05-17.md` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-axis.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-axis-adapter-map.ts` | `partially_absorbed` | high | full agent role governance; broad Phase 2.B runtime wire-up | `GAP-17.05-002`; `GAP-17.05-003`; `GAP-17.05-005` |
| Agent registry identity | `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_REGISTRY_SPEC.md` | `governance/toolkit/03_CONTROL/CVF_AGENT_REGISTRY.md`; `EXTENSIONS/CVF_ECO_v2.3_AGENT_IDENTITY/src/agent.registry.ts` | `partially_absorbed` | high | Role/Permission tranche | `GAP-17.05-002`; `GAP-17.05-003` |
| Agent adapter boundary | `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_ADAPTER_BOUNDARY.md` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-axis-adapter-map.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-handoff.ts` | `partially_absorbed` | medium | Role/Permission tranche | `GAP-17.05-002` |
| Agent handoff contract | `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_HANDOFF_CONTRACT.md` | `AGENT_HANDOFF_V9_2026-05-18.md`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-handoff.ts`; `governance/compat/check_agent_handoff_guard_compat.py` | `partially_absorbed` | high | handoff/runtime continuity claim; Role/Permission tranche | `GAP-17.05-002`; `GAP-17.05-003` |

### 2. Permission

| Concept sub-item | Legacy source files | Current CVF files | Disposition | Severity | Blocks | Linked GAPs |
|---|---|---|---|---|---|---|
| Per-role permission profile | `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_PERMISSION_PROFILE.md`; `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_ROLE_CATALOG.md` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/authority-gate.guard.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-axis.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-permission.contract.ts` | `partially_absorbed` | high | full role governance claim (runtime enforcement deferred) | `GAP-17.05-002`; `GAP-17.05-003`; `GAP-17.05-005`; `GAP-17.05-012` |
| Allowed outputs and deny rules | `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_ROLE_CATALOG.md` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-permission.contract.ts` (`RolePermissionOutputClass`, `RolePermissionDenyRuleId`) | `partially_absorbed` | high | runtime enforcement deferred to Phase E (E.2 role permission gate); full output-class enforcement not yet wired into execute path | `GAP-17.05-002`; `GAP-17.05-003` |
| Per-role risk policy | `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_RISK_POLICY.md` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/risk-engine.contract.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/risk-check.ts` | `partially_absorbed` | high | Role/Permission tranche | `GAP-17.05-002`; `GAP-17.05-003` |

### 3. Orchestrator

| Concept sub-item | Legacy source files | Current CVF files | Disposition | Severity | Blocks | Linked GAPs |
|---|---|---|---|---|---|---|
| ORCHESTRATOR role boundary | `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_AGENT_ORCHESTRATOR_ROLE_ABSORPTION_GAP_CODEX_AUDIT_2026-05-17.md`; `.private_reference/legacy/CVF ADD/Human System Harness/Thong_tin.md` | `docs/reviews/CVF_17_05_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-17.md`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/delegation.boundary.guard.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts` | `partially_absorbed` | high | runtime consumption for live ORCHESTRATOR enforcement | `GAP-17.05-001`; `GAP-17.05-003`; `GAP-17.05-005` |
| Orchestration rules contract | `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_ORCHESTRATION_RULES.md` | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/delegation.boundary.guard.contract.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sandbox-worker.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts` | `partially_absorbed` | high | runtime consumption of orchestration transition metadata | `GAP-17.05-001`; `GAP-17.05-003`; `GAP-17.05-013` |
| Reverse brief / solution bias guard | `.private_reference/legacy/CVF ADD/Human System Harness/Thong_tin.md`; `.private_reference/legacy/CVF Edit/Review CVF_1.md` | `governance/toolkit/05_OPERATION/CVF_AGENT_REVIEW_ANTI_COLLUSION_GUARD.md`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts` | `partially_absorbed` | medium | live delegation-path consumption | `GAP-17.05-001` |

### 4. Runtime

| Concept sub-item | Legacy source files | Current CVF files | Disposition | Severity | Blocks | Linked GAPs |
|---|---|---|---|---|---|---|
| State machine and failure transitions | `.private_reference/legacy/CVF Edit/De_xuat.md`; `.private_reference/legacy/CVF Edit/Failure Simulation cho CVF.md` | `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/state_enforcement/state.machine.validator.ts`; `EXTENSIONS/CVF_STARTER_TEMPLATE_REFERENCE/src/core/execution-state-machine.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` | `partially_absorbed` | high | runtime consumption/live recovery enforcement | `GAP-17.05-003`; `GAP-17.05-004`; `GAP-17.05-015` |
| Guard runtime enforcement | `.private_reference/legacy/CVF Edit/CVF_EDIT_ANALYSIS.md`; `.private_reference/legacy/CVF Edit/Review CVF_1.md` | `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/guard.runtime.engine.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-runtime-adapter.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` | `partially_absorbed` | high | live runtime consumption across product/provider/tool paths | `GAP-17.05-003`; `GAP-17.05-004`; `GAP-17.05-015` |
| Async worker ticket lifecycle | `.private_reference/legacy/CVF ADD/deepagents/Thong_tin.md`; `.private_reference/legacy/CVF ADD/Agent Harnesses/Thong_tin.md`; `.private_reference/legacy/CVF 16.5/OpenAgentd/Thong_tin.md` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sandbox-worker.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` | `partially_absorbed` | high | scheduler and runtime worker lifecycle consumption | `GAP-17.05-003`; `GAP-17.05-005`; `GAP-17.05-013` |

### 5. Memory

| Concept sub-item | Legacy source files | Current CVF files | Disposition | Severity | Blocks | Linked GAPs |
|---|---|---|---|---|---|---|
| Memory capture and retrieval policy | `.private_reference/legacy/CVF 16.5/agentmemory/Thong_tin.md`; `.private_reference/legacy/CVF ADD/cortex-hub/Thong_tin.md` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-tier.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts` | `partially_absorbed` | high | runtime memory policy consumption | `GAP-17.05-003`; `GAP-17.05-011`; `GAP-17.05-014` |
| Governed memory reinjection | `.private_reference/legacy/CVF 16.5/agentmemory/Thong_tin.md`; `.private_reference/legacy/CVF 16.5/tolaria/Thong_tin.md`; `.private_reference/legacy/CVF ADD/Workflow GoClaw/Thong_tin.md` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/w7.memory.record.contract.ts`; `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/continuity.checkpoint.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract.ts` | `partially_absorbed` | high | live reinjection enforcement; full Agent OS claim | `GAP-17.05-003`; `GAP-17.05-005`; `GAP-17.05-011` |
| Worker memory write restriction | `.private_reference/legacy/CVF ADD/deepagents/Thong_tin.md`; `.private_reference/legacy/CVF ADD/Hermes Agent/Thong_tin.md` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract.ts` | `partially_absorbed` | high | runtime write enforcement | `GAP-17.05-003`; `GAP-17.05-011`; `GAP-17.05-013` |

### 6. Provider

| Concept sub-item | Legacy source files | Current CVF files | Disposition | Severity | Blocks | Linked GAPs |
|---|---|---|---|---|---|---|
| Provider output contract | `.private_reference/legacy/CVF ADD/openrouter-cli.git/Thong_tin.md`; `.private_reference/legacy/CVF 16.5/free Claude Code/Thong_tin.md` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-output-contract.test.ts` | `partially_absorbed` | medium | Provider method tranche | none |
| Provider registry, quota, routing, fallback | `.private_reference/legacy/CVF 16.5/freellmapi/Thong_tin.md`; `.private_reference/legacy/CVF ADD/Hermes Agent/Thong_tin.md` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/quota-guard.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/provider-lane-status.ts` | `partially_absorbed` | medium | Provider method tranche | none |
| Stream/tool/JSON/vision/embedding/reasoning methods | `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md`; `.private_reference/legacy/CVF ADD/openrouter-cli.git/Thong_tin.md` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts` | `needs_gc018` | medium | Provider method tranche — demand-gated: no consuming vertical slice selected as of 2026-05-18; Tranche 4 not implemented | `GAP-17.05-009` |

### 7. Workflow

| Concept sub-item | Legacy source files | Current CVF files | Disposition | Severity | Blocks | Linked GAPs |
|---|---|---|---|---|---|---|
| Outcome to workflow to certified capability chain | `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md`; `.private_reference/legacy/CVF 17.05/CVF_EXTERNAL_CAPABILITY_INTAKE/CVF_CAPABILITY_WORKFLOW_COMPOSITION.md` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/phase2b-wireup.contract.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/phase2c-product-brief-slice.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` | `partially_absorbed` | high | generalized outcome-to-capability runtime consumption; external capability intake tranche | `GAP-17.05-003`; `GAP-17.05-004` |
| External capability lifecycle | `.private_reference/legacy/CVF 17.05/CVF_EXTERNAL_CAPABILITY_INTAKE/CVF_EXTERNAL_CAPABILITY_INTAKE_SPEC.md`; `.private_reference/legacy/CVF 17.05/CVF_EXTERNAL_CAPABILITY_INTAKE/CVF_CAPABILITY_CERTIFICATION_PROTOCOL.md` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/external-assets/register/route.ts` | `partially_absorbed` | high | external capability intake tranche | `GAP-17.05-003`; `GAP-17.05-012` |
| Change-spec adapter | `.private_reference/legacy/CVF 16.5/OpenSpec/Thong_tin.md` | `none` | `not_absorbed` | low | none | `GAP-17.05-014` |

### 8. Receipt

| Concept sub-item | Legacy source files | Current CVF files | Disposition | Severity | Blocks | Linked GAPs |
|---|---|---|---|---|---|---|
| Canonical receipt envelope | `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md`; `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_AUDIT_RECEIPT.md` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-envelope.contract.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | `partially_absorbed` | medium | Receipt compatibility; Role/Permission tranche | none |
| Per-agent audit receipt | `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_AUDIT_RECEIPT.md`; `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/Thong_tin.md` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-envelope.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-handoff.ts` | `needs_gc018` | medium | Tool/action governance tranche — deferred: no Phase D tranche covers per-agent/role audit receipt binding; requires separate GC-018 | none |
| Operational metric receipt integrity | `.private_reference/legacy/CVF 16.5/abtop/Thong_tin.md`; `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/operational-metrics.schema.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/phase3e-operational-emission.ts` | `absorbed` | low | none | `GAP-17.05-008`; `GAP-17.05-010` |

### 9. Benchmark

| Concept sub-item | Legacy source files | Current CVF files | Disposition | Severity | Blocks | Linked GAPs |
|---|---|---|---|---|---|---|
| Mandatory live governance proof | `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md`; `.private_reference/legacy/CVF Edit/CVF_EDIT_ANALYSIS.md` | `scripts/run_cvf_release_gate_bundle.py`; `docs/CVF_INCREMENTAL_TEST_LOG.md` | `absorbed` | low | violation would block public/release governance claims | `GAP-17.05-007` |
| Operational benchmark extension | `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md`; `.private_reference/legacy/CVF 16.5/abtop/Thong_tin.md` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/operational-metrics.schema.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/phase3e-operational-emission.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` | `partially_absorbed` | medium | live emission wiring, durable dashboard, and full observability plane | `GAP-17.05-008`; `GAP-17.05-010` |
| Deterministic failure simulation suite | `.private_reference/legacy/CVF Edit/Failure Simulation cho CVF.md`; `.private_reference/legacy/CVF Edit/Review CVF_1.md` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` | `partially_absorbed` | high | runtime failure simulation suite execution/live evidence | `GAP-17.05-003`; `GAP-17.05-015` |

### 10. UI / Noncoder

| Concept sub-item | Legacy source files | Current CVF files | Disposition | Severity | Blocks | Linked GAPs |
|---|---|---|---|---|---|---|
| Trusted form / product brief vertical slice | `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/phase2c-product-brief-slice.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | `absorbed` | medium | none for bounded slice | `GAP-17.05-006` |
| Deliverable pack evidence export | `.private_reference/legacy/CVF 16.5/md2html/Thong_tin.md`; `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/deliverable-pack.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` | `partially_absorbed` | medium | document artifact renderer claim | none |
| Database operator surface | `.private_reference/legacy/CVF ADD/gridex/Thong_tin.md` | `none` | `not_absorbed` | low | none | `GAP-17.05-012` |

### 11. Agent OS

| Concept sub-item | Legacy source files | Current CVF files | Disposition | Severity | Blocks | Linked GAPs |
|---|---|---|---|---|---|---|
| Complete Agent OS claim | `.private_reference/legacy/CVF Edit/CVF_EDIT_ANALYSIS.md`; `.private_reference/legacy/CVF ADD/Hermes Agent/Thong_tin.md`; `.private_reference/legacy/CVF ADD/deepagents/Thong_tin.md` | `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` `[claim-boundary]`; `ARCHITECTURE.md` `[claim-boundary]` | `rejected_or_superseded` | blocker | public catalog must not claim complete Agent OS | `GAP-17.05-003`; `GAP-17.05-015`; `GAP-17.05-016` |
| Product capability system composition | `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md`; `.private_reference/legacy/CVF 17.05/CVF_EXTERNAL_CAPABILITY_INTAKE/README.md` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/phase2b-wireup.contract.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/phase2c-product-brief-slice.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/phase3e-operational-emission.ts` | `partially_absorbed` | high | next legacy absorption roadmap | `GAP-17.05-003`; `GAP-17.05-005`; `GAP-17.05-016` |
| External skill/library marketplace claim | `.private_reference/legacy/CVF 17.05/CVF_EXTERNAL_CAPABILITY_INTAKE/CVF_ECC_MAPPING_GUIDE.md`; `.private_reference/legacy/CVF ADD/Hugging Face/Thong_tin.md` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts`; `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` `[claim-boundary]` | `rejected_or_superseded` | high | public catalog must not claim marketplace readiness | `GAP-17.05-003`; `GAP-17.05-016` |

## Delta Notes For Partial Rows

| Row | Absorbed | Not yet absorbed |
|---|---|---|
| 1.1 Agent function role taxonomy | role axis and adapter map exist | granular domain role IDs, per-role output constraints, and runtime permission binding |
| 1.2 Agent registry identity | registry docs and identity registry implementation exist | single runtime authority tying registry identity to role permission and receipts |
| 1.3 Agent adapter boundary | adapter map and handoff runtime exist | complete adapter conformance against every legacy agent boundary contract |
| 1.4 Agent handoff contract | active handoff file, guard checker, and runtime handoff helper exist | proof that all legacy handoff contract fields are enforced end to end |
| 2.3 Per-role risk policy | risk engine and route risk checks exist | per-role risk policy binding and role-specific denial outputs |
| 3.1 ORCHESTRATOR role boundary | authority-role delegation profile exists in guard contract | runtime scheduler and product execution path consumption |
| 3.2 Orchestration rules contract | delegation boundary, sandbox worker surfaces, typed overreach vocabulary, and worker-lane ticket shape exist | runtime worker-lane router and scheduler lifecycle |
| 3.3 Reverse brief / solution bias guard | review anti-collusion guard and ORCHESTRATOR overreach deny vocabulary exist | live delegation-path enforcement of reverse-brief behavior |
| 4.1 State machine and failure transitions | state validator, sample execution state machine, and runtime workflow failure vocabulary exist | live runtime consumption of the workflow contract and recovery enforcement |
| 4.2 Guard runtime enforcement | guard runtime engine, web adapter, and phase-bound guard enforcement metadata exist | unified enforcement across every product/runtime/provider/tool path |
| 4.3 Async worker ticket lifecycle | worker-lane ticket type, delegation receipt boundary, and runtime transition metadata exist | scheduler and runtime worker lifecycle execution |
| 5.1 Memory capture and retrieval policy | memory tier contract, memory continuity owner policy, and knowledge store exist | runtime consumption of the memory continuity contract across workers |
| 5.2 Governed memory reinjection | privacy-filtered reinjection policy and receipt requirement exist in guard contract | live runtime reinjection enforcement and provider-path proof |
| 5.3 Worker memory write restriction | worker ticket and memory continuity contract mark persistent/archive writes denied without ORCHESTRATOR delegation receipt | runtime write enforcement |
| 6.1 Provider output contract | JSON/NDJSON output contract and tests exist | first-class provider method coverage and broader CLI/job lifecycle semantics |
| 6.2 Provider registry, quota, routing, fallback | provider router, quota guard, and lane status exist | sticky sessions, health-driven fallback, and credential-vault semantics as one provider hub |
| 7.1 Outcome workflow chain | bounded Phase 2.B/2.C slice and runtime workflow transition metadata exist | general outcome-to-certified-capability runtime system |
| 7.2 External capability lifecycle | external asset registry and governance API exist | full certification, install-state, and authority binding runtime |
| 8.1 Canonical receipt envelope | receipt contract and gateway receipt exist | per-agent/role audit receipt binding |
| 9.2 Operational benchmark extension | schema, bounded emission pilot, and metadata-only workflow benchmark extension exist | durable dashboard, full observability plane, and cross-runtime live emission |
| 9.3 Deterministic failure simulation suite | runtime workflow contract models worker-overreach and memory-write-violation denial simulations | runtime failure simulation suite execution and live enforcement evidence |
| 10.2 Deliverable pack evidence export | deliverable pack, HTML export route, and artifact-export action class vocabulary exist | governed Markdown-to-HTML renderer as a reusable product runtime |
| 11.2 Product capability system composition | bounded 2.B/2.C/3.E chain exists | generalized system-wide product capability composition |

## Decision

This matrix supersedes the folder-axis matrix for absorption-proof purposes.
The folder-axis matrix remains useful as an inventory and orientation view.

Rows with `severity` equal to `blocker` or `high` require either a matching
ledger entry or an explicit rejection. Runtime work remains blocked until a
fresh GC-018 names the tranche and consuming slice.

Phase A freeze pointer: accepted at HEAD `ffae9346` by
`docs/reviews/CVF_LEGACY_ABSORPTION_PHASE_A_FREEZE_2026-05-18.md`.

## Recommendation

Use this matrix as the input to the upgraded gap ledger and to Phase D tranche
naming in the next roadmap. Do not freeze Phase A legacy knowledge mapping
until this matrix and the ledger crosswalk agree.

## Verification Run

Verification command:

```powershell
$paths = @(
  "AGENT_HANDOFF_V9_2026-05-18.md",
  "ARCHITECTURE.md",
  "docs/CVF_INCREMENTAL_TEST_LOG.md",
  "docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md",
  "docs/reviews/CVF_17_05_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-17.md",
  "EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/continuity.checkpoint.contract.ts",
  "EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/w7.memory.record.contract.ts",
  "EXTENSIONS/CVF_ECO_v2.3_AGENT_IDENTITY/src/agent.registry.ts",
  "EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/delegation.boundary.guard.contract.ts",
  "EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-tier.contract.ts",
  "EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/operational-metrics.schema.ts",
  "EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/phase2b-wireup.contract.ts",
  "EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-envelope.contract.ts",
  "EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/risk-engine.contract.ts",
  "EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-axis-adapter-map.ts",
  "EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-axis.contract.ts",
  "EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/authority-gate.guard.ts",
  "EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-handoff.ts",
  "EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts",
  "EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts",
  "EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-output-contract.test.ts",
  "EXTENSIONS/CVF_STARTER_TEMPLATE_REFERENCE/src/core/execution-state-machine.ts",
  "EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/guard.runtime.engine.ts",
  "EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/state_enforcement/state.machine.validator.ts",
  "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts",
  "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts",
  "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/external-assets/register/route.ts",
  "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.ts",
  "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/deliverable-pack.ts",
  "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-runtime-adapter.ts",
  "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts",
  "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/phase2c-product-brief-slice.ts",
  "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/phase3e-operational-emission.ts",
  "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/provider-lane-status.ts",
  "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/quota-guard.ts",
  "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/risk-check.ts",
  "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sandbox-worker.ts",
  "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts",
  "governance/compat/check_agent_handoff_guard_compat.py",
  "governance/toolkit/03_CONTROL/CVF_AGENT_REGISTRY.md",
  "governance/toolkit/05_OPERATION/CVF_AGENT_REVIEW_ANTI_COLLUSION_GUARD.md",
  "scripts/run_cvf_release_gate_bundle.py"
)
$paths | ForEach-Object { if (-not (Test-Path $_)) { "FAIL $_" } else { "PASS $_" } }
```

Result: PASS for every concrete current-CVF path listed above. Rows with
`Current CVF files` equal to `none` intentionally have no implementation path.

Ledger round-trip verification:

```powershell
$expected = @{
  "GAP-17.05-001" = @("3.1", "3.2", "3.3")
  "GAP-17.05-002" = @("1.1", "1.2", "1.3", "1.4", "2.1", "2.2", "2.3")
  "GAP-17.05-003" = "all high/blocker rows"
  "GAP-17.05-004" = @("4.1", "4.2", "7.1")
  "GAP-17.05-005" = @("1.1", "2.1", "3.1", "4.3", "5.2", "11.2")
  "GAP-17.05-006" = @("10.1")
  "GAP-17.05-007" = @("9.1")
  "GAP-17.05-008" = @("8.3", "9.2")
  "GAP-17.05-009" = @("6.3")
  "GAP-17.05-010" = @("8.3", "9.2")
  "GAP-17.05-011" = @("5.1", "5.2", "5.3")
  "GAP-17.05-012" = @("2.1", "7.2", "10.3")
  "GAP-17.05-013" = @("3.2", "4.3", "5.3")
  "GAP-17.05-014" = @("5.1", "7.3")
  "GAP-17.05-015" = @("4.1", "4.2", "9.3", "11.1")
  "GAP-17.05-016" = @("11.1", "11.2", "11.3")
}
```

Result: PASS - all 34 concept-axis matrix rows now have a `Linked GAPs`
cell; each concrete ledger crosswalk row maps back to the matrix; every
high/blocker row carries at least one linked GAP. `GAP-17.05-003` remains the
umbrella Phase A freeze gate and is listed on all high/blocker rows.

Legacy source spot-check:

| Checked row | Legacy source reread | Result |
|---|---|---|
| 1.4 Agent handoff contract | `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_HANDOFF_CONTRACT.md` | PASS - source requires structured handoff fields; current CVF has active handoff, runtime helper, and guard checker but not complete legacy-field enforcement |
| 2.1 Per-role permission profile | `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_PERMISSION_PROFILE.md` | PASS - source defines file/tool/execution/audit permission dimensions; current CVF lacks full per-role runtime binding |
| 5.1 Memory capture and retrieval policy | `.private_reference/legacy/CVF 16.5/agentmemory/Thong_tin.md` | PASS - source proposes governed memory gateway/retrieval/reinjection; current CVF has tier and store pieces only |
| 7.2 External capability lifecycle | `.private_reference/legacy/CVF 17.05/CVF_EXTERNAL_CAPABILITY_INTAKE/CVF_CAPABILITY_CERTIFICATION_PROTOCOL.md` | PASS - source requires certification inputs/status; current CVF has external asset governance pieces but not full certification runtime |
| 4.3 Async worker ticket lifecycle | `.private_reference/legacy/CVF ADD/Hermes Agent/Thong_tin.md` | PASS - source maps scheduler/subagent/sandbox patterns; current CVF has sandbox/delegation pieces but no canonical async ticket lifecycle |

## Claim Boundary

This artifact records a review correction. It does not authorize
implementation, does not change public claims, does not promote private legacy
material into public canon, and does not expand the reviewed folder scope.

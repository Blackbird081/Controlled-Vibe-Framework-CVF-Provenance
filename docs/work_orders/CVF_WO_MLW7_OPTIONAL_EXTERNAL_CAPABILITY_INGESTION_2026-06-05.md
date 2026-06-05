# CVF Work Order: MLW7 Optional External Capability Ingestion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-05

dispatchBaseHead: `2b1250c1`

executionBaseHead: `2b1250c1`

closureBaseHead: `2b1250c1`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Author MLW7 as a source-verified work order candidate for external capability
ingestion. MLW7 maps Hermes/HF/cortex/deepagents/external-provider patterns
into the existing external-asset governance surface without installing,
executing, registering authority, or publishing a marketplace claim.

## Agent Roles

| Role | Assignment |
| --- | --- |
| Orchestrator | Codex authoring packet and operator-dispatched executor |
| Worker | Codex self-execution under 2026-06-05 operator instruction |
| Reviewer / committer | Codex closure review and commit after focused gates |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator direction | 2026-06-05: after LO2, return to MLW7/MLW8 work-order authoring | ACCEPT |
| MLW7 GC-018 | `docs/baselines/CVF_GC018_MLW7_OPTIONAL_EXTERNAL_CAPABILITY_INGESTION_2026-06-05.md` | ACCEPT |
| T11 roadmap | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | ACCEPT |
| MLW0 source map | `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | ACCEPT |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope documentation, source-verification, and test
packet defects directly. Escalate before runtime execution, dependency install,
external repo ingestion, live proof, public-sync, secrets/quota use, destructive
actions, or claim-boundary expansion.

## Scope

Allowed implementation scope after 2026-06-05 operator dispatch:

- Add an intake-only external capability classification/admission mapping.
- Reuse existing external-asset governance source before adding any new surface.
- Add deterministic tests proving no install, execute, delegation approval, or
  client-side workflow-status bypass.
- Update docs/reviews for bounded closure.

Forbidden scope:

- Package/plugin/model/skill/MCP/repo installation.
- External capability execution.
- New dependencies, package files, lockfiles, provider calls, live proof,
  autonomous delegation, policy mutation, memory reinjection, public-sync,
  hosted readiness, production readiness, public readiness, or marketplace
  positioning.

Risk ceiling: R2 intake/proposal only.

## Required First Reads

| Required read | Reason | Status |
| --- | --- | --- |
| `docs/baselines/CVF_GC018_MLW7_OPTIONAL_EXTERNAL_CAPABILITY_INGESTION_2026-06-05.md` | MLW7 authority | READ |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | work-order quality rules | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts` | owner surface | SOURCE_VERIFIED |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/external-assets/register/route.ts` | server-side status derivation | SOURCE_VERIFIED |

## Pre-Flight Checks

| Check | Evidence | Status |
| --- | --- | --- |
| MLW7 GC-018 exists | baseline path above | PASS |
| Base head captured | `2b1250c1` | PASS |
| Source anchors searched | Source Verification Block | PASS |
| Runtime execution excluded | forbidden scope | PASS |

## Write Ownership

| Role | Owned paths |
| --- | --- |
| Worker | `src/lib/mlw7-external-capability-ingestion.ts` and focused test |
| Reviewer / committer | completion review and closure evidence |
| Forbidden | route wiring, dependency files, public-sync, live proof, package install, external execution |

## Execution Plan

1. Re-verify external-asset governance source.
2. Build intake-only classification/admission mapping.
3. Add deterministic no-install/no-execute/no-delegation tests.
4. Close with public-boundary and finding-learning disposition.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| MLW7 is planned as optional external capability ingestion | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | line 102 | `MLW7` | T11 roadmap | ACCEPT |
| MLW7 was deferred pending fresh GC-018 | `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | line 164 | `MLW7 Optional External Capability Ingestion` | MLW0 source map | ACCEPT |
| External asset governance request exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts` | line 73 | `ExternalAssetGovernanceRequest` | external asset governance module | ACCEPT |
| External asset workflow statuses exist | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts` | line 83 | `ExternalAssetWorkflowStatus` | external asset governance module | ACCEPT |
| External asset preparation function exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts` | lines 257-258 | `prepareExternalAssetGovernance` | external asset governance module | ACCEPT |
| Register route re-derives workflow status server-side | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/external-assets/register/route.ts` | lines 16, 68-76 | `workflowStatus` | external-assets register route | ACCEPT |
| Existing governance result blocks delegation by default | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts` | lines 410-411 | `blockedDelegationReasons` | external asset governance module | ACCEPT |

## New Doc-Only Fields

| New doc-only field | Purpose | Runtime claim blocked? |
| --- | --- | --- |
| `externalCapabilityCandidateClass` | candidate classification for design review | Yes |
| `admissionProfile` | source/provenance/risk/readiness proposal | Yes |
| `noInstallNoExecuteInvariant` | blocks scope inflation | Yes |

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Work-order mapping | Status |
| --- | --- | --- |
| Handle Hermes/HF/cortex/deepagents patterns after core stabilization | external capability candidate ledger | READY_FOR_REVIEW |
| Reuse existing external-asset governance surface | `prepareExternalAssetGovernance` owner | READY_FOR_REVIEW |
| Prevent marketplace/runtime execution overclaim | forbidden scope and no-execution invariant | READY_FOR_REVIEW |

## Execution Instructions

1. Re-read this work order and MLW7 GC-018.
2. Re-run source verification before edits.
3. Prefer an intake/classification helper over route or dependency changes.
4. Add focused deterministic tests for no-install/no-execute/no-delegation.
5. Stop before live proof, public-sync, dependency install, or external repo
   ingestion unless a separate operator authorization expands scope.

## Acceptance Criteria

| Criterion | Required before closure |
| --- | --- |
| Candidate ledger classifies accepted/deferred/rejected external capability signals | YES |
| Existing external-asset governance owner is reused or rejection is justified | YES |
| Tests prove no install/execute/delegation approval | YES |
| No public marketplace or capability catalog claim | YES |
| Public Export Disposition included | YES |

## Evidence Requirements

Closure evidence:

- source verification refreshed from current source;
- deterministic no-install/no-execute/no-delegation tests;
- changed-file diff proving no dependencies or public-sync;
- public export disposition and claim boundary.

## Review Gate

Reviewer must reject closure if MLW7 installs or executes external capability
content, adds dependencies without authorization, claims marketplace readiness,
or bypasses server-side external-asset governance.

## Closure Checklist

| Item | Status |
| --- | --- |
| Work order source-verified | PASS |
| Operator dispatch recorded | PASS |
| No runtime execution authorized | PASS |
| Focused tests passed | PASS |
| Public boundary present | PASS |

## Return Conditions

Return to Orchestrator if any follow-up implementation requires dependencies, external repo
content, provider calls, public-sync, runtime execution, new route authority, or
policy/delegation changes.

## Operator Checkpoint

Operator checkpoint is still required before dependency installation, external
repo ingestion, external capability execution, live proof, public-sync, route
wiring, or public marketplace/catalog claims.

## Closure Diff Gate

| Requirement | Final artifact | Disposition |
| --- | --- | --- |
| Candidate ledger classifies external capability signals | `mlw7-external-capability-ingestion.ts` | SATISFIED |
| Existing external-asset governance owner reused | helper imports `prepareExternalAssetGovernance` | SATISFIED |
| Tests prove no install/execute/delegation approval | `mlw7-external-capability-ingestion.test.ts` | SATISFIED |
| No dependency, route, public-sync, or live proof scope | changed-file evidence | SATISFIED |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | status `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MLW7_OPTIONAL_EXTERNAL_CAPABILITY_INGESTION_COMPLETION_2026-06-05.md` | reviewer artifact created | PASS |
| Roadmap state | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | MLW7 roadmap row remains source authority; no roadmap edit required | PASS |
| Registry JSON | N/A | no corpus/search registry update in MLW7 allowed scope | BLOCKED with reason |
| Registry Markdown | N/A | no corpus/search registry markdown update in MLW7 allowed scope | BLOCKED with reason |
| External evidence digest | N/A | no external evidence, external repo, package, or live provider consumed | N/A with reason |
| System loop interlock | N/A | no checker, route, or autonomous loop added | N/A with reason |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V15_2026-05-29.md` | updated after closure | PASS |

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason - this is a work-order authoring packet,
  not a fresh external capability corpus inventory.
- Corpus root: N/A with reason.
- Snapshot time: 2026-06-05 at base `2b1250c1`.
- Enumeration command: `rg --files --hidden --no-ignore docs/work_orders/CVF_WO_MLW7_OPTIONAL_EXTERNAL_CAPABILITY_INGESTION_2026-06-05.md`
- Manifest artifact or inline manifest: N/A with reason - authoring packet only.
- Manifest hash: N/A with reason.
- Processing ledger artifact or inline ledger: N/A with reason.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=0; ledger_terminal=0; exclusions=1; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: no external repo, package, model, skill, MCP, or legacy
  corpus rescan.
- Unreadable or unsupported files: none.
- Aggregation check: N/A with reason - no corpus aggregation performed.
- Drift check: PASS
- Output traceability: Source Verification Block.
- Adversarial verification: sampled marketplace/runtime scope inflation.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Knowledge System Reconciliation

- Knowledge task class: WORK_ORDER_AUTHORING.
- Source manifest: Source Verification Block in this file.
- Source manifest hash: N/A with reason - inline source verification.
- Enumeration safety: `rg --files --hidden --no-ignore docs/work_orders/CVF_WO_MLW7_OPTIONAL_EXTERNAL_CAPABILITY_INGESTION_2026-06-05.md EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/external-assets docs/baselines docs/reference docs/roadmaps`
- Intake registry or ledger: MLW7 GC-018 baseline and T11 roadmap.
- Authority assets: MLW7 GC-018 and external-asset governance source.
- Derived views: this work order.
- Semantic region ledger: EXTERNAL_ASSET_GOVERNANCE, REGISTER_ROUTE,
  MLW7_AUTHORING.
- Region reconciliation: assets=4; mapped=4; deferred=0; unmapped=0.
- Orphan or unmapped assets: none.
- Cross-region links: external capability signals route through existing
  external-asset governance before any future execution.
- Drift check: PASS
- Rebuildability check: PASS.
- Retrieval boundary: no runtime/readiness claim.
- Adversarial verification: no install, execute, delegation, or marketplace
  claim is authorized.
- Knowledge-map verdict: RECONCILED_VERIFIED

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| External capability ingestion can inflate into runtime/marketplace claims | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | WORK_ORDER_AUTHORED | no-install/no-execute invariant required |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

No public-sync or public marketplace claim is authorized.

## Claim Boundary

This artifact is a closed bounded work order for intake-only helper
implementation. It proves no package safety, execution safety, marketplace
readiness, live provider behavior, hosted readiness, production readiness,
public readiness, public-sync, or autonomous mutation.

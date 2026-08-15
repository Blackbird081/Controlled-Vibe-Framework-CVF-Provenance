# CVF GC-018 Baseline - CADP-AI-T5-R2A Shared Package-Root Multi-Surface Export Drift Proof Hardening

Memory class: governed-baseline

Status: DISPATCH_READY

docType: gc018_baseline

Batch ID: CADP-AI-T5-R2A

Date: 2026-08-15

Base HEAD: `ca1a408b1364995156c575d398a8ce99a256180d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one bounded checker-maintenance tranche that removes the disclosed
T5-R2 fixture-schema limitation: multiple CADP contract surfaces may cite the
same package-root file while contract-source ownership remains unique. Add
independent package-root export drift proof for T5-R2 without changing any
production TypeScript contract or opening authentication or transport runtime.

## Authorization

The operator instructed continuation after T5-R2 bounded acceptance. Source
review found no repository-owned external authentication verifier, so this
baseline routes the continuation to the already-recorded T5-R2 machine-gate
residual rather than inventing an authentication authority. The authority is
limited to the five-path checker/test/fixture/evidence manifest below.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id CADP-AI-T5-R2A --title "CADP AI T5 R2A Shared Package Root Multi Surface Export Drift Proof Hardening" --date 2026-08-15 --base ca1a408b1364995156c575d398a8ce99a256180d --commit-mode WORKER_MUST_NOT_COMMIT --dependency "CADP-AI-T5-R2 accepted bounded at ad76d7433" --include-worker-return-skeleton --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact five-path manifest, checker semantics, negative matrix, protected-path authorization, no-live boundary, reviewer conversion, and source verification were resolved |
| checkerReadAheadConfirmation | applicable dispatch, protected-path, trace, worker-return, Markdown, and CADP drift checker sources were read before authoring |
| docOnlyNewFields | `sharedPackageRootDisposition`; no runtime field is introduced |
| claimBoundary | dispatch baseline only; no checker change, runtime support, authentication, transport, or provider claim exists until worker execution and independent review |

## Dependency Release Evidence

| Dependency | Evidence | Release rule | Disposition |
|---|---|---|---|
| T5-R2 bounded adapter | `docs/reviews/CVF_CADP_AI_T5_R2_TRANSPORT_NEUTRAL_EXTERNAL_READOUT_ADAPTER_FOUNDATION_COMPLETION_2026-08-15.md`; material commit `ad76d7433` | reuse only the accepted package-root exports and disclosed residual | SATISFIED |
| residual registry finding | `docs/corpus-intelligence/registry/entries/cadp-ai-t5-r2-transport-neutral-adapter.json` finding `CADP-AI-T5-R2-F02` | resolve only shared-root fixture proof | SATISFIED |
| checker owner | `governance/compat/check_cadp_authority_boundary_drift.py` | preserve all existing violation codes and five-surface checks | SATISFIED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json`

Returned defects: 22, not truncated.

Disclosed defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021,
ADIF-0024, ADIF-0028, ADIF-0029, ADIF-0031, ADIF-0033, ADIF-0039,
ADIF-0043, ADIF-0044, ADIF-0045, ADIF-0049, ADIF-0051, ADIF-0052.

Dispatch impact: protected paths are exact and explicitly authorized; source
facts are verified; the worker cannot commit or widen into production/runtime;
reviewer and continuity ownership remain separate.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_cadp_authority_boundary_drift.py` |
| literalTokensReviewed | Status; Source Verification canonical columns; protected paths; operator authorization; rollback boundary; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition |
| gateRunPurpose | confirm source-derived dispatch evidence shape before protected checker maintenance |
| claimBoundary | gate conformance is not proof of implemented checker behavior or external runtime support |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| fixture loader uses one global path set | source fact | `governance/compat/check_cadp_authority_boundary_drift.py` | fixture loading near `seen_paths` | `load_fixture` | CADP drift checker | ACCEPT |
| package-root export is checked per surface | source fact | `governance/compat/check_cadp_authority_boundary_drift.py` | package-root branch | `check_surface` | CADP drift checker | ACCEPT |
| checker has focused unit-test owner | source fact | `governance/compat/test_check_cadp_authority_boundary_drift.py` | package-export tests | `TestPackageExportDrift` | checker tests | ACCEPT |
| T5-R1 owns shared root in fixture | source fact | `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json` | `T5R1_EXTERNAL_READOUT_FOUNDATION` | `packageRootPath` | CADP fixture | ACCEPT |
| T5-R2 root proof is absent | source fact | `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json` | `T5R2_EXTERNAL_READOUT_ADAPTER` | `requiredExportSymbols` | CADP fixture | ACCEPT |
| T5-R2 exports exist | source fact | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | CADP T5-R2 export block | `evaluateCadpExternalReadoutAdapter` | Guard Contract package root | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| planned packet paths | filename search found no T5-R2A packet | UNIQUE_PATHS |
| authentication owner | targeted Guard Contract search found shape-only identity and no external authentication verifier | BLOCKED_NOT_SELECTED |
| checker/test/fixture owner | direct source reads confirm one canonical checker family | UPDATE_EXISTING |
| same-token collision | no competing T5-R2A batch found in governed packet paths | CREATE_ONE_PACKET_PAIR |

## Scope

Allowed:

- distinguish unique contract-source ownership from shareable package-root references;
- retain schema coupling rules for root path, export module, and symbols;
- add focused regression tests for shared root and duplicate contract paths;
- update only the T5-R2 fixture package-root proof fields;
- reconcile the existing T5-R2 negative-proof plan and create the worker return.

Forbidden:

- production TypeScript, package barrels, authentication implementation,
  credentials, MCP/CLI/HTTP, provider or network actions, live tests, mutation,
  hook/CI wiring, public sync, deployment, production, session state, or commit;
- changing semantic CADP authority verdicts or weakening literal-false checks;
- adding a second checker owner or changing unrelated fixture surfaces.

## Planned Artifact Manifest

1. `governance/compat/check_cadp_authority_boundary_drift.py`
2. `governance/compat/test_check_cadp_authority_boundary_drift.py`
3. `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json`
4. `docs/reference/CVF_CADP_AI_T5_R2_TRANSPORT_NEUTRAL_ADAPTER_NEGATIVE_PROOF_PLAN_2026-08-15.md`
5. `docs/reviews/CVF_CADP_AI_T5_R2A_SHARED_PACKAGE_ROOT_MULTI_SURFACE_EXPORT_DRIFT_PROOF_HARDENING_WORKER_RETURN_2026-08-15.md`

## Adversarial Proof Matrix

| Case | Required result |
|---|---|
| two surfaces share one package root with distinct modules | fixture loads and each export block is independently checked |
| duplicate contract source path | `FIXTURE_SCHEMA_INVALID` remains fail-closed |
| missing T5-R2 export symbol | `PACKAGE_EXPORT_DRIFT` attributed to T5-R2 only |
| missing/empty export module or symbols | existing schema coupling rejects fixture |
| existing five surfaces | zero violations after fixture reconciliation |
| forbidden authority widening | existing false-field and forbidden-seam checks remain unchanged |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | CADP drift checker and fixture | local read-only static validation; no runtime authority | focused Python tests and checker output | checker only | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | T5-R2 package-root contract export | discoverability proof only; no invocation or auth | fixture/checker after worker review | no external adapter runtime | `CONTRACT_ONLY` |

## Core Guard Self-Protection Authorization

Protected paths:

- `governance/compat/check_cadp_authority_boundary_drift.py`
- `governance/compat/test_check_cadp_authority_boundary_drift.py`

Operator authorization: the operator instructed continuation after T5-R2
bounded closure; source verification routes that instruction to the disclosed
checker-schema residual and no broader path.

Authorized guard-maintenance scope: permit shared package-root references while
preserving unique contract-source ownership and every existing authority/seam
check.

Rollback boundary: revert the exact five worker paths as one material batch;
do not retain fixture fields that the reverted checker cannot load.

## Acceptance Criteria

- exactly five worker paths changed, staging empty, HEAD unchanged;
- duplicate contract paths still fail;
- duplicate package-root references are allowed and checked per surface;
- T5-R2 receives exact package-root module/symbol proof;
- focused checker tests and five-surface checker pass;
- worker-return fast gate passes after the last edit;
- no production/runtime/provider/live path changes.

## Evidence / Verification

- `python -m unittest governance.compat.test_check_cadp_authority_boundary_drift`
- `python governance/compat/check_cadp_authority_boundary_drift.py`
- `python governance/compat/run_worker_return_fast_gate.py`
- `git diff --check`
- exact HEAD/status/staging comparison.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/MCP/readiness claim |
| Chain map route | local checker residual only; no external artifact intake |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this baseline and paired work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | repository sources remain the only authority |

## Decision / Baseline

`AUTHORIZED_FOR_DISPATCH`

The paired work order may be dispatched after pre-dispatch review and commit.
Worker implementation remains no-commit and hermetic.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | future local CADP checker/test/fixture hardening |
| claimDisposition | CLAIM_REJECTED_NO_ACTION: baseline authoring is not implementation |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt exists |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: worker commands are planned but not executed by this baseline |
| invocationBoundary | local future checker execution only |
| interceptionBoundary | no runtime wrapper, transport, or agent interception |
| claimLanguage | protected checker-maintenance baseline only |
| forbiddenExpansion | no production, authentication, credentials, provider/live, mutation, public, deploy, production, or moratorium change |

## Claim Boundary

This baseline authorizes only shared package-root checker-schema hardening and
fixture proof. It does not authorize authentication, credentials, external
transport or invocation, provider/live behavior, mutation, public action,
deployment, production, or a moratorium lift.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance checker-maintenance dispatch; no public action is authorized.

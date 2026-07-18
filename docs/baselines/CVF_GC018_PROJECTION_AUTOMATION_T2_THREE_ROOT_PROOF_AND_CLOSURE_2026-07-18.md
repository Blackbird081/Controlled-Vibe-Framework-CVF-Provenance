# CVF GC-018 Projection Automation T2 Three-Root Proof And Closure Baseline

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-18

Batch ID: CVF-PROJECTION-AUTO-T2

Base head before packet authoring: `67aefb4eb`

## Purpose

Authorize the final roadmap tranche: a disposable provenance/public-sync/
cvf-web proof runner, one governed proof receipt, an operator guide, a final
closure audit, and a no-commit worker return.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-PROJECTION-AUTO-T2 --title "Projection Automation Three-Root Proof And Closure" --date 2026-07-18 --base 67aefb4eb --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | populated five-path scope, source verification, proof matrix, closure controls, and no-push boundary |
| checkerReadAheadConfirmation | dispatch-quality, structural, handoff, receipt, closure, public-disposition, and size checkers |
| docOnlyNewFields | T2 audit totals and guide examples only; proof receipt reuses the T1 schema |
| claimBoundary | final proof dispatch provenance only |

## Proposed Tranche / Decision

Proceed with T2 as proof/documentation only. Do not add an apply switch or run
against the real public-sync clone. Roadmap closure requires independent review.

## Target / Source

Target: the five worker paths in the paired work order. Sources: accepted T1
mapper, policy, focused tests, receipt schema, T1 completion review, and current
roadmap acceptance criteria.

## Scope / Target / Owner Boundary

T2 may create disposable temporary git roots, invoke the committed read-only
mapper, emit one governed proof receipt, document operator usage, reconcile T0
through T2, and delete only its own temp fixture. Real roots are read-only and
must not be used as proof targets. No apply/copy, public mutation, stage/commit/
push by worker, provider/network call, deployment, or production action.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| T1 accepted closure | `docs/reviews/CVF_PROJECTION_AUTOMATION_T1_COMPLETION_REVIEW_2026-07-18.md` | `aa699742b` | PASS |
| T1 handoff sync | active handoff marker | `67aefb4eb` | PASS |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| mapper exposes five parameters | EXISTS | `scripts/get_cvf_projection_map.ps1` | parameter block, lines 66-79 | `ReceiptOutputPath` | projection mapper CLI | ACCEPT |
| exact remote checks exist | RUNTIME_BEHAVIOR | `scripts/get_cvf_projection_map.ps1` | preflight block | `WRONG_PROVENANCE_REMOTE` | mapper root validation | ACCEPT |
| parity drift fails closed | RUNTIME_BEHAVIOR | `scripts/get_cvf_projection_map.ps1` | lines 533-538 | `POLICY_PARITY_FAILED` | mapper policy validation | ACCEPT |
| receipt target roots are forbidden | RUNTIME_BEHAVIOR | `scripts/get_cvf_projection_map.ps1` | lines 426-433 | `RECEIPT_TARGET_ROOT_FORBIDDEN` | mapper receipt boundary | ACCEPT |
| governed receipt schema exists | EXISTS | `docs/reference/CVF_PROJECTION_MAPPING_RECEIPT_SCHEMA_2026-07-18.md` | Top-Level Fields through No-Target-Write Claim | `receiptId` | receipt schema | ACCEPT |
| T1 suite supports governed receipt output | EXISTS | `scripts/test_get_cvf_projection_map.ps1` | parameter and final proof block | `GovernedReceiptPath` | focused test runner | ACCEPT |
| accepted T1 receipt has all parity MATCH | VALUE_SET | `docs/reviews/CVF_PROJECTION_AUTOMATION_T1_DRY_RUN_RECEIPT_2026-07-18.json` | `policyParity` | `mappedFiles` | accepted T1 receipt | ACCEPT |

## Design Control Gate

- fixture roots live under one unique temp parent and are deleted in `finally`;
- fixture origins use the exact policy URLs without performing network access;
- the current sync script is copied as read-only policy evidence into the
  disposable provenance fixture and committed there;
- proof runs mapper twice and compares receipt bytes/IDs;
- before/after file inventory and git status cover all three disposable roots;
- governed receipt output is outside every disposable root and has no BOM;
- operator guide defaults to stdout and requires clean validated roots;
- final audit reconciles roadmap AC-01 through AC-06 and T0/T1/T2 artifacts;
- no apply/copy branch, real target mutation, commit/push, or live/provider proof.

## Acceptance Criteria

- AC-01: disposable three-root proof exits zero and cleans its temp root.
- AC-02: repeated mapper receipts are byte-stable with the same receipt ID.
- AC-03: every parity key is `MATCH`; errors are empty; counts reconcile.
- AC-04: all three disposable root status/file inventories remain unchanged.
- AC-05: operator guide states exact safe command and review boundary.
- AC-06: final audit maps every roadmap criterion and declares public export.
- AC-07: real public-sync/cvf-web roots are never mutated or used as proof targets.

## Evidence / Verification

Use the T2 proof runner, governed receipt, exact temp cleanup evidence, T1
focused-suite regression, exact changed set, worker-fast/reviewer-fast,
phase autorun, file-size, and closure diff gates.

## Dual Agent Surface Matrix

| Surface | Interface | Authority/risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | local PowerShell proof CLI | disposable roots and receipt only | proof runner/receipt/audit | committed T1 mapper | ACCEPT |
| EXTERNAL_AGENT_CLI_MCP | operator guide command | no MCP/provider/remote authority | documented CLI boundary | same local mapper | DEFER_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`projection automation closure proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "projection automation closure proof" --role dispatcher --lifecycle-phase pre-dispatch --json`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Proposed Tranche / Decision; Evidence / Verification; Source Verification Block; Machine Closure Package; Acceptance Receipt Assertion Matrix; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation and evidence for T2 dispatch quality, not first discovery |
| claimBoundary | disposable closure proof only |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this baseline | `Status: DISPATCH_READY` | PASS |
| Work order status | paired T2 work order | `Status: DISPATCH_READY` | PASS |
| Completion or reviewer artifact | future T2 completion review | dependency-held | N/A with reason |
| Worker return | future T2 return | worker-owned | N/A with reason |
| Roadmap state | automation roadmap | `Status: T1_PASS_BOUNDED_T2_DISPATCH_READY` | PASS |
| Registry JSON | existing GC-051 coverage | aggregate drift checked | PASS |
| Registry Markdown | existing registry front door | no new family required | PASS |
| External evidence digest | repository-local evidence only | none | N/A with reason |
| System loop interlock | no loop owner changed | none | N/A with reason |
| Session continuity | protected surfaces | separate sync | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| parity | all MATCH | worker-owned | N/A with reason |
| errors | zero | worker-owned | N/A with reason |
| root delta | zero across three roots | worker-owned | N/A with reason |
| deterministic receipt | same bytes and ID | worker-owned | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T2 proof remains private and authorizes no public-sync action.

## Claim Boundary

This baseline authorizes only disposable proof and closure documentation. It
does not authorize apply/copy, real-root mutation, public commit/push,
provider/network calls, deployment, production, or public availability.

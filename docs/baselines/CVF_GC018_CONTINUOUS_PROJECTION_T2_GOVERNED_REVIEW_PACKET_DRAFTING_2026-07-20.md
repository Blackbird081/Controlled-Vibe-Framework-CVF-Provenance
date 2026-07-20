# CVF GC-018 Continuous Projection T2 Governed Review-Packet Drafting

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CVF-CONTINUOUS-PROJECTION-T2

Dispatch base head: `0ea461553`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Freeze the T1-accepted read-only drift receipt, its output schema, the
accepted mapper it wraps, and the roadmap-set T2 constraints before a worker
implements a read-only governed review-packet drafter that turns a drift
receipt into a review-required, uncommitted draft. This baseline releases a
bounded read-only implementation tranche only; no apply, copy, commit, push,
public-sync, provider, or real-root mutation authority is granted, and the
generated packet must itself remain a review-required draft that authorizes
nothing.

## Decision / Baseline / Proposed Tranche

Decision: release T2 after the T1 completion review
(`docs/reviews/CVF_CONTINUOUS_PROJECTION_T1_COMPLETION_REVIEW_2026-07-20.md`,
`REVIEWER_ACCEPTED_WITH_REPAIRS`) explicitly authorized only T2 packet
authoring and set the roadmap T2 content requirements. Baseline: the accepted
drift receipt `scripts/get_cvf_projection_drift_receipt.ps1` (implementation
commit `a394d635c`) and the accepted mapper it wraps remain read-only and
fail-closed; the receipt's 16-surface schema and `publicTargetState` split
are the frozen input. Proposed tranche: a new read-only review-packet
drafter script plus a focused deterministic proof suite, both authored by a
worker under `WORKER_MUST_NOT_COMMIT`, reviewed independently by the
reviewer/closer before any commit.

Operator implementation authorization: the initial 2026-07-20 instruction
authorized only T2 packet authoring. After independent review identified and
returned three packet findings, the operator explicitly instructed the reviewer
to repair those findings and transfer the accepted packet to Claude for T2
implementation. This releases only the exact three-output no-commit T2 worker
assignment after reviewer acceptance and dispatch/session-sync commits. T3-T4,
the real-root receipt run, and every mutation, public, provider/live, push,
deployment, and production lane remain parked.

## Reviewer Finding Carry-Forward

| Finding observed during packet review | Reviewer repair | Worker carry-forward |
|---|---|---|
| `DISPATCH_READY` lacked current implementation authority | fresh operator instruction recorded above | execute only after the reviewer dispatch/session-sync HEAD exists |
| intake and handoff route tokens disagreed | both now use `MULTI_AGENT_SINGLE_ROLE` | remain the no-commit implementation worker; do not collapse reviewer ownership |
| draft persistence, schema, and disposition-to-action semantics were ambiguous | stdout-only ordered JSON contract and fail-closed mapping are frozen below | implement the frozen mapping exactly; do not invent fields, actions, or a fourth persistent output |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-CONTINUOUS-PROJECTION-T2 --title "Continuous Projection Governed Review-Packet Drafting Baseline" --date 2026-07-20 --base 0ea461553 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | T1 dependency release, source verification, exact tranche scope, review-required-draft constraint, uncommitted-output boundary, closure ownership, and mutation boundary |
| checkerReadAheadConfirmation | dispatch-quality, handoff, worker-return, machine-closure, public-disposition, and file-size checkers |
| docOnlyNewFields | T2 draft-packet section names (`sourceFacts`, `affectedProjections`, `recommendedReviewerActions`, `publicProvenanceBoundary`, `evidence`, `draftStatus`) are documentation proposals until the worker implements them |
| claimBoundary | scaffold provenance does not prove runtime or execution behavior |

## Scope / Target / Owner Boundary

The worker may create only a new read-only review-packet drafter script and a
paired focused proof suite under `scripts/`, plus the paired T2 worker return
under `docs/reviews/`. The accepted drift receipt
`scripts/get_cvf_projection_drift_receipt.ps1`, its focused proof
`scripts/test_cvf_projection_drift_receipt.ps1`, the accepted mapper
`scripts/get_cvf_projection_map.ps1`, the policy
`scripts/cvf_projection_policy.json`, the other existing projection tests,
`scripts/cvf-public-sync.ps1`, the provenance root beyond the allowed new
paths, the sibling public-sync clone, cvf-web, registries, session files, and
the roadmap remain read-only. No apply/copy mode may be added to any script,
and the generated draft packet must never be committed or presented as a
reviewer decision.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T1 read-only drift receipt | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T1_COMPLETION_REVIEW_2026-07-20.md`; implementation commit `a394d635c` | reviewer accepted with repairs; 53/53 fixture proof; frozen receipt schema | PASS |
| projection mapper foundation | `docs/reviews/CVF_PROJECTION_AUTOMATION_T2_FINAL_CLOSURE_AUDIT_2026-07-18.md`; foundation commit `5df0c6f77` | accepted read-only three-root proof exists and is deterministic | PASS |
| current session release | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; sync commit `0ea461553` | next move authorizes T2 packet authoring only; implementation stays parked | PASS |

## Roadmap-Set T2 Constraints

The roadmap T2 tranche and the T1 completion review's Next Allowed Move
require the T2 packet to:

| Constraint | Source | Packet handling |
|---|---|---|
| list source facts, affected projections, recommended reviewer actions, public/provenance boundary, and evidence | roadmap T2 section; T1 completion Next Allowed Move | work order requires the drafter to emit exactly these five content groups from the drift receipt |
| keep generated output a review-required, uncommitted draft | roadmap T2 section; T1 completion Next Allowed Move | work order requires an explicit `draftStatus` of review-required and a claim that the draft authorizes no decision, plus a no-commit boundary on the drafter itself |
| no apply mode, no real-root run | roadmap Non-Goals; T1 completion Claim Boundary | work order forbids any apply/copy path and requires the proof suite to run against disposable fixtures and reused accepted receipts only, never the T4 real-root scan |

## Frozen T2 Draft Output Contract

The drafter accepts exactly one existing receipt through required parameter
`-ReceiptPath`. It reads that file and writes one JSON draft to stdout only.
It has no output-path, apply, copy, commit, or persistence parameter. Tests may
capture stdout inside their disposable temp directory; no generated draft is a
fourth worker output.

Top-level fields use this exact ordinal order:

1. `schemaVersion` = `1.0.0`
2. `draftStatus` = `REVIEW_REQUIRED_UNCOMMITTED`
3. `authorizesDecision` = `false`
4. `sourceFacts`
5. `affectedProjections`
6. `recommendedReviewerActions`
7. `publicProvenanceBoundary`
8. `evidence`
9. `claimBoundary`
10. `draftId`

The five roadmap content groups are fields 4-8. `affectedProjections` contains
rows whose `driftDisposition` is neither `CURRENT` nor
`NOT_APPLICABLE_WITH_REASON`, sorted ordinally by `surface`.
`recommendedReviewerActions` contains one same-order row per affected surface
using only this mapping:

| Input `driftDisposition` | Output `recommendedAction` |
|---|---|
| `MISSING_TARGET` | `REVIEW_MISSING_TARGET_NO_COPY_AUTHORIZED` |
| `STALE_TARGET` | `REVIEW_STALE_TARGET_DIFF_NO_APPLY_AUTHORIZED` |
| `SEMANTIC_REVIEW_REQUIRED` | `REVIEW_SEMANTIC_OWNER_AND_TARGET` |
| `SOURCE_AUTHORITY_BLOCKED` | `KEEP_BLOCKED_PENDING_SOURCE_AUTHORITY` |
| `AUDIENCE_PRESENTATION_RISK` | `REVIEW_AUDIENCE_PRESENTATION` |

The five content groups use these exact shapes and field orders:

| Group | Ordered fields |
|---|---|
| `sourceFacts` | `receiptId`, `receiptSchemaVersion`, `receiptRowCount`, `reconciliationMatch`, `rootsObserved`, `publicTargetState`, `noTargetWriteConfirmation` |
| each `affectedProjections` row | `surface`, `semanticOwner`, `projectionTarget`, `evidenceClass`, `audience`, `driftDisposition`, `sourceHash`, `targetHash`, `reviewerNote` |
| each `recommendedReviewerActions` row | `surface`, `driftDisposition`, `recommendedAction`, `reviewerNote`, `decisionAuthority` = `REVIEWER_ONLY` |
| `publicProvenanceBoundary` | `sourceAuthority` = `PROVENANCE_ROOT`, `observedTarget` = `PUBLIC_SYNC_ROOT`, `publicMutationAuthorized` = `false`, `applyOrCopyAuthorized` = `false`, `autoApproveAuthorized` = `false`, `persistence` = `STDOUT_ONLY_UNCOMMITTED` |
| `evidence` | `sourceReceiptId`, `mapperReceiptId`, `receiptNoTargetWriteConfirmation`, `receiptReconciliationMatch`, `affectedProjectionCount`, `actionCount` |

`claimBoundary` is the literal `DRAFT_ONLY_REVIEWER_DECISION_REQUIRED_NO_APPLY_COPY_COMMIT_PUBLIC_MUTATION`.
The input validator requires receipt fields `receiptId`, `schemaVersion`,
`rootsObserved`, `rows`, `publicTargetState`, `summary.rowCount`,
`summary.reconciliationMatch`, `mapperReceiptId`,
`noTargetWriteConfirmation`, and `errors`; exactly 16 rows; all nine row fields
listed above; an empty `errors` array; summary row count 16; and reconciliation
true.

`CURRENT` and `NOT_APPLICABLE_WITH_REASON` produce no action row. Any missing
required receipt field, failed reconciliation, row/action cardinality mismatch,
or unknown disposition fails nonzero with code
`UNSUPPORTED_OR_INVALID_DRIFT_RECEIPT`, writes one JSON diagnostic to stderr,
and emits no stdout success draft. `draftId` is
the uppercase SHA-256 of compact JSON for fields 1-9 encoded as UTF-8 without
BOM, so identical receipt content produces byte-identical output.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| drift receipt emits a 16-surface rows array | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, lines 663-680 | `rows` | drift receipt output schema | ACCEPT |
| drift receipt emits a tracked/ignored public split | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, line 671 | `publicTargetState` | drift receipt output schema | ACCEPT |
| drift receipt emits a reconciled disposition summary | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, lines 672-676 | `reconciliationMatch` | drift receipt output schema | ACCEPT |
| receipt schema version exists | VALUE_SET | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, line 664 | `schemaVersion` | drift receipt output schema | ACCEPT |
| observed roots exist | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, line 669 | `rootsObserved` | drift receipt output schema | ACCEPT |
| mapper receipt identity exists | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, line 677 | `mapperReceiptId` | drift receipt output schema | ACCEPT |
| successful receipt has an errors array | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, line 679 | `errors` | drift receipt output schema | ACCEPT |
| top-level receipt identity exists | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | final receipt assembly, lines 683-688 | `receiptId` | drift receipt output schema | ACCEPT |
| each row carries a reviewer note field | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | frozen contract rows, line 119 | `reviewerNote` | drift receipt row schema | ACCEPT |
| frozen contract owner exists | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | function, line 108 | `Get-FrozenT0ContractRows` | drift receipt frozen contract | ACCEPT |
| receipt is deterministic and fail-closed | RUNTIME_BEHAVIOR | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T1_COMPLETION_REVIEW_2026-07-20.md` | Independent Recomputed Evidence table | 53/53 fixture proof | T1 accepted implementation | ACCEPT |
| no-target-write confirmation string exists | LITERAL_INVARIANT | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, line 678 | `noTargetWriteConfirmation` | drift receipt output schema | ACCEPT |
| automatic semantic approval is forbidden | VALUE_SET | `scripts/cvf_projection_policy.json` | semanticReviewBoundary, lines 138-141 | `autoApproveForbidden` | projection policy schema | ACCEPT |

## New Doc-Only Fields

| Proposed item | Kind | Existing runtime status | T2 disposition |
|---|---|---|---|
| top-level draft fields and five content groups in Frozen T2 Draft Output Contract | ordered JSON schema | does not exist before T2 | worker implements exactly as new T2 output |
| `recommendedAction` and `decisionAuthority` | action-row fields | does not exist before T2 | worker implements only the frozen mapping |
| `UNSUPPORTED_OR_INVALID_DRIFT_RECEIPT` | diagnostic code | does not exist before T2 | worker implements fail-closed validation code |
| `draftId` hash profile | deterministic output identity | does not exist before T2 | worker implements uppercase SHA-256 over fields 1-9 |

## Evidence / Verification

Worker evidence must include direct source locations, the draft packet's five
content groups derived from a reused or fixture drift receipt, an explicit
review-required draft-status marker, deterministic draft output proof,
proof that the drafter reads a receipt without re-running the real-root
scan, exact diff, staged state, unchanged HEAD, worker-return fast gate, and
file-size results. No apply, copy, real-root mutation, committed draft, or
public action may be claimed.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`continuous projection T2 governed review-packet drafting`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "continuous projection T2 governed review-packet drafting" --role dispatcher --lifecycle-phase pre-dispatch --json`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Status; Dependency Release Evidence; Source Verification Block; ADIF Defect Registry Disclosure; Public Export Disposition; Claim Boundary |
| gateRunPurpose | validate T2 baseline dispatch shape and source evidence before authoring the paired work order |
| claimBoundary | checker compliance confirms packet structure only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance dispatch baseline; T2 authorizes no
public-sync export and the drafted review packet itself is a private,
review-required draft until a later reviewer decision.

## Claim Boundary

This reviewer-repaired baseline releases a bounded read-only review-packet
drafting implementation tranche under `WORKER_MUST_NOT_COMMIT`. It does not authorize
apply/copy implementation, semantic edits, real-root mutation, a committed
draft, commit, push, deployment, public-sync mutation, provider/live use,
production action, or unattended work. The worker implements read-only
receipt-to-draft transformation only; the reviewer/closer owns evidence
recomputation and any material commit.

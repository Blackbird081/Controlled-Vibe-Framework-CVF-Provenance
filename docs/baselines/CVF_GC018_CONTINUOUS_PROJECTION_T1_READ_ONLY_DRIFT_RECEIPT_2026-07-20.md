# CVF GC-018 Continuous Projection T1 Read-Only Drift Receipt

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS

Batch ID: CVF-CONTINUOUS-PROJECTION-T1

Dispatch base head: `c8f7bb9e7`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Freeze the T0-accepted three-root drift contract, the current read-only
projection mapper, its policy and proof seams, and the reviewer-set T1
release conditions before a worker implements a deterministic, read-only
drift receipt over the accepted contract. This baseline releases a bounded
read-only implementation tranche only; no apply, copy, commit, push,
public-sync, provider, or real-root mutation authority is granted.

## Decision / Baseline / Proposed Tranche

Decision: release T1 after the T0 completion review
(`docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_COMPLETION_REVIEW_2026-07-20.md`,
`REVIEWER_ACCEPTED_BOUNDED_WITH_REPAIRS`) explicitly authorized T1 packet
authoring and set three conditions the packet must resolve. Baseline: the
accepted mapper `scripts/get_cvf_projection_map.ps1` remains read-only and
fail-closed, and the T0 ledger's 16-row terminal contract is the frozen
input. Proposed tranche: a new read-only drift-receipt script plus a focused
deterministic proof suite, both authored by a worker under
`WORKER_MUST_NOT_COMMIT`, reviewed independently by the reviewer/closer before any commit.

Operator implementation authorization: the 2026-07-20 operator instruction
assigns this packet to the independent reviewer followed by the designated
worker step. That authorization becomes effective
only after the reviewer commits this packet and session continuity records the
final execution base. It does not widen the tranche or any mutation boundary.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-CONTINUOUS-PROJECTION-T1 --title "Continuous Projection Read-Only Drift Receipt Baseline" --date 2026-07-20 --base c8f7bb9e7 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | T0 dependency release, source verification, exact tranche scope, timeout-semantics resolution, six target-only file classification requirement, closure ownership, and mutation boundary |
| checkerReadAheadConfirmation | dispatch-quality, handoff, worker-return, machine-closure, public-disposition, and file-size checkers |
| docOnlyNewFields | T1 receipt schema fields (`driftDisposition`, `semanticOwner`, `projectionTarget`, `evidenceClass`, `audience`, `reviewerNote`) and proposed codes `RECEIPT_TIMEOUT_INCONCLUSIVE`, `AUDIENCE_EVIDENCE_MISSING` are documentation proposals until the worker implements them |
| claimBoundary | scaffold provenance does not prove runtime or execution behavior |

## Scope / Target / Owner Boundary

The worker may create only a new read-only drift-receipt script and a paired
focused proof suite under `scripts/`, plus the paired T1 worker return under
`docs/reviews/`. The accepted mapper `scripts/get_cvf_projection_map.ps1`,
the policy `scripts/cvf_projection_policy.json`, the existing focused test
`scripts/test_get_cvf_projection_map.ps1`, the three-root proof
`scripts/test_cvf_projection_three_root_proof.ps1`, `scripts/cvf-public-sync.ps1`,
the provenance root beyond the allowed new paths, the sibling public-sync
clone, cvf-web, registries, session files, and the roadmap remain read-only.
No apply/copy mode may be added to any script.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T0 three-root drift contract | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_COMPLETION_REVIEW_2026-07-20.md`; closure commit `d1cb8cba9` | reviewer accepted bounded with repairs; 16-row terminal contract frozen | PASS |
| projection mapper foundation | `docs/reviews/CVF_PROJECTION_AUTOMATION_T2_FINAL_CLOSURE_AUDIT_2026-07-18.md`; foundation commit `5df0c6f77` | accepted read-only three-root proof exists and is deterministic | PASS |
| current session release | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; sync commit `c8f7bb9e7` | next move authorizes T1 packet authoring only; implementation stays parked | PASS |

## Reviewer-Set T1 Conditions

The T0 completion review's Next Allowed Move requires the T1 packet to:

| Condition | Source | Packet handling |
|---|---|---|
| resolve bounded timeout semantics | T0 completion review Next Allowed Move | work order requires the worker to bound the recursive scan and define `RECEIPT_TIMEOUT_INCONCLUSIVE` behavior explicitly |
| classify the six target-only root files | T0 completion review Findings / Position; ledger row for `GOVERNANCE.md`, `PROVENANCE.md`, `PROVIDERS.md`, `CONTRIBUTING.md`, `COST_AND_QUOTA.md`, `CODEOWNERS` | work order requires the receipt to carry a `SOURCE_AUTHORITY_BLOCKED` disposition for these six rather than defaulting them to `CURRENT` |
| keep tracked public drift separate from ignored clone residue | T0 completion review Risk / Corrective Action; ledger negative-search row | work order requires the receipt to report tracked-versus-ignored counts as distinct fields, not a single filesystem count |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| mapper accepts three explicit roots plus optional receipt path | EXISTS | `scripts/get_cvf_projection_map.ps1` | parameter block, lines 65-80 | `ReceiptOutputPath` | mapper parameter contract | ACCEPT |
| candidate actions are classification labels only | LITERAL_INVARIANT | `scripts/get_cvf_projection_map.ps1` | description, lines 21-28 | `FLAG_SEMANTIC_REVIEW_CHANGED` | mapper action vocabulary | ACCEPT |
| policy parity inspection owner exists | EXISTS | `scripts/get_cvf_projection_map.ps1` | function, lines 249-328 | `Get-PolicyParityReport` | mapper policy parity read model | ACCEPT |
| cvf-web observation owner exists | EXISTS | `scripts/get_cvf_projection_map.ps1` | function, lines 330-376 | `Get-CvfWebObservation` | mapper Web observation read model | ACCEPT |
| deterministic receipt id and reconciliation exist | EXISTS | `scripts/get_cvf_projection_map.ps1` | receipt assembly, lines 558-576 | `reconciliationMatch` | mapper receipt schema | ACCEPT |
| no-target-write confirmation string exists | LITERAL_INVARIANT | `scripts/get_cvf_projection_map.ps1` | receipt assembly, line 571 | `noTargetWriteConfirmation` | mapper receipt schema | ACCEPT |
| automatic semantic approval is forbidden | VALUE_SET | `scripts/cvf_projection_policy.json` | semanticReviewBoundary, lines 138-141 | `autoApproveForbidden` | projection policy schema | ACCEPT |
| deterministic and negative proof seams exist | EXISTS | `scripts/test_get_cvf_projection_map.ps1` | assertions, lines 292, 309, 318, 441 | `provenance_remote_substring_spoof_rejected` | focused mapper proof suite | ACCEPT |
| frozen T0 terminal contract exists | EXISTS | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_THREE_ROOT_DRIFT_CONTRACT_LEDGER_2026-07-20.md` | Findings / Position terminal rows, 16-row table | Terminal Contract Rows | T0 accepted drift contract | ACCEPT |

## Evidence / Verification

Worker evidence must include direct source locations, current
root/remote/status observations, receipt determinism proof (byte-stable
repeated runs and stable receipt id), the tracked-versus-ignored separation,
the six target-only file classification, timeout-bounded behavior, exact
diff, staged state, unchanged HEAD, worker-return fast gate, and file-size
results. No apply, copy, real-root mutation, or public action may be claimed.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`continuous projection T1 read-only drift receipt implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "continuous projection T1 read-only drift receipt implementation" --role dispatcher --lifecycle-phase pre-dispatch --json`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Status; Dependency Release Evidence; Source Verification Block; ADIF Defect Registry Disclosure; Public Export Disposition; Claim Boundary |
| gateRunPurpose | validate T1 baseline dispatch shape and source evidence before authoring the paired work order |
| claimBoundary | checker compliance confirms packet structure only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance dispatch baseline; T1 authorizes no
public-sync export and the drift receipt itself is a private read-only
artifact until a later reviewer decision.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired T1 work order | `Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS` | PASS |
| Completion or reviewer artifact | paired T1 completion review | `Status: REVIEWER_ACCEPTED_WITH_REPAIRS` | PASS |
| Roadmap state | continuous-projection roadmap | `Status: T1_CLOSED_PASS_WITH_REVIEWER_REPAIRS_T2_PACKET_AUTHORING_NEXT` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated aggregate drift check remains clean; no entry change required | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | existing human registry remains unchanged; T1 adds no corpus record | PASS |
| External evidence digest | N/A with reason: repository-local sources and fixtures only | no imported evidence bundle | N/A with reason |
| System loop interlock | N/A with reason: no interlock owner changed | no mutation | N/A with reason |
| Session continuity | protected continuity surfaces | separate post-material closure sync | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| T1-ROW-COUNT | disposable-fixture receipt | `summary.rowCount` | `16` | `16` | PASS |
| T1-RECONCILIATION | disposable-fixture receipt | `summary.reconciliationMatch` | `true` | `true` | PASS |
| T1-SOURCE-BLOCK | disposable-fixture receipt | `rows[allowedRootFiles:target-only-six].driftDisposition` | `SOURCE_AUTHORITY_BLOCKED` | `SOURCE_AUTHORITY_BLOCKED` | PASS |
| T1-TIMEOUT | slow-mapper fixture error | `errors[0].code` | `RECEIPT_TIMEOUT_INCONCLUSIVE` | `RECEIPT_TIMEOUT_INCONCLUSIVE` | PASS |
| T1-PUBLIC-SPLIT | tracked/ignored fixture receipt | `publicTargetState` | distinct tracked and ignored arrays | 1 tracked and 1 git-confirmed ignored fixture path | PASS |

## Claim Boundary

This baseline is closed after the bounded read-only drift-receipt
implementation and independent review. It does not authorize apply/copy,
semantic edits, real-root mutation, push, deployment, public-sync mutation,
provider/live use, production action, or unattended work. The accepted result
is private fixture-proven receipt generation only.

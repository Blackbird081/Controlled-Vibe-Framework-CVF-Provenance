# CVF GC-018 Baseline - High-Risk Local Transaction Proof Foundation T2

Memory class: governed-dispatch-baseline

docType: baseline

Status: AUTHORIZED_FOR_DISPATCH

Batch ID: CVF-HRLTP-T2

Dispatch base head: `4952a0e3d3223f9ed7879d15512c897ea3222afe`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local orchestrator/reviewer

Reviewer owner: Local orchestrator/reviewer

Worker target: shared-workspace `INTERNAL_AGENT`

## Purpose

Authorize a forward-only extension of the existing HRLTP owner so a governed
packet cannot assign an actor an operation or observation that contradicts its
declared resource capability. The extension also binds crash-recovery ownership,
exact parent-versus-file deletion semantics, hermetic-versus-operational proof
ceilings, and the earliest pre-dispatch admission point.

## Authority And Learning Trigger

The operator directed Local to preserve the accepted G1-G4 learning and raise
the CVF foundation when useful. The accepted C0-R1 independent probe found that
an otherwise complete operational contract:

1. required Party C to inspect a response target its own rights did not permit;
2. described hard-termination residue without an authorized cleanup actor;
3. conflated parent-directory child-deletion authority with individual-file
   deletion authority; and
4. needed two further corrections because the first repair widened one
   cross-principal denial and dropped a directory-creation negative.

The existing independent probe and review-cost controls successfully contained
the defects and repair regressions. They do not replace the missing early
actor-capability feasibility admission. The selection audit owns the overlap
decision:
`docs/audits/CVF_HRLTP_T2_OPERATIONAL_ROLE_CAPABILITY_CONSISTENCY_SELECTION_2026-09-23.md`.

## Scope / Target / Owner Boundary

Target: the existing HRLTP standard/checker family and its current routing.

Owner: CVF governance control chain. The worker may alter only the protected
and reference paths named by the paired work order and must return without a
commit.

Boundary: static repository authoring admission only. No target transaction,
account, credential, ACL, source, alternate-principal process, provider, public
or deployment action is authorized.

## Architecture Decision

Extend HRLTP rather than creating a parallel standard. Add one closed
machine-readable consistency object whose relations are exact and enumerable:

- actors;
- resources;
- controlled operations;
- per-actor allowed and forbidden capabilities on each resource;
- required actions/observations with execution actor and evidence owner;
- recovery residue identity, cleanup actor/capability and unknown-artifact
  disposition;
- evidence mode and maximum claim ceiling.

Applicable relations must contain at least one actor, resource and required
action. Actor, resource and action identifiers and actor/resource capability
rows are unique. Evidence owners are known actors with the capability needed
to observe the named resource. Each operation is compatible with its resource
class, so a parent-directory child-delete operation cannot be attached to an
individual file resource.

The checker must reject an action whose operation is absent from the actor's
allowed capability set, present in its forbidden set, or assigned to an unknown
actor/resource. Recovery must be complete and internally consistent. Exact
Windows operation tokens distinguish parent child-deletion authority from
individual-file deletion authority. A normative design may carry a future
actual-token proof obligation with evidence state `PENDING` at a contract-only
ceiling. Operational-ready claims require completed operational evidence;
pending or hermetic evidence remains valid only at its declared lower ceiling.

The existing checker remains the sole machine owner. T2 extends its
applicability to current work orders that authorize either execution or a
normative operational contract design/amendment for a future high-risk local
transaction. Pure teaching examples and non-normative checker fixtures remain
excluded.

## Decision

Authorize the paired CVF-HRLTP-T2 work order for one no-commit INTERNAL_AGENT
implementation followed by a distinct Local independent probe and Local-owned
completion. No successor tranche or runtime authority follows automatically.

## Selected Tranche Manifest

The complete material tranche has nine paths with explicit role ownership:

| Path | Mutation owner | Required action |
|---|---|---|
| `docs/reference/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_STANDARD_2026-09-22.md` | worker | extend the canonical contract and applicability semantics |
| `governance/compat/check_high_risk_local_transaction_proof.py` | worker | enforce the closed feasibility and recovery relations |
| `governance/compat/test_check_high_risk_local_transaction_proof.py` | worker | add positive, adversarial and real-Git scope regressions |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | worker | update concise routing and required contract guidance |
| `docs/reference/guard_orientation/README.md` | worker | replace the stale nine-field/reviewer-fast-only orientation |
| `governance/compat/agent_autorun_command_catalog.py` | worker | bind the existing checker into common pre-dispatch autorun |
| `governance/compat/test_run_agent_autorun_workflow_gate.py` | worker | prove one common-catalog membership and pre-dispatch availability |
| `docs/reviews/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_FOUNDATION_T2_WORKER_RETURN_2026-09-23.md` | worker | return exact evidence, pending independent review and no commit |
| `docs/reviews/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_FOUNDATION_T2_COMPLETION_2026-09-23.md` | Local reviewer | record independent probe and terminal disposition |

Worker-owned manifest: the first eight paths only. The completion path is
required for material closure but is forbidden to the implementation worker.

## Required Evidence

- exact schema agreement among standard, checker, template and orientation;
- focused positive and adversarial tests for every new relation;
- tests proving normative design packets cannot use a documentation-only
  escape while pure examples remain non-applicable;
- tests distinguishing parent child-deletion from individual-file deletion;
- tests rejecting missing recovery owner, mismatched cleanup capability and
  permissive unknown-artifact handling;
- tests rejecting operational claims backed only by hermetic evidence;
- tests rejecting empty/duplicate identities, duplicate capability rows,
  incapable evidence owners and operation/resource-class mismatches;
- a positive contract-only normative design with pending actual-token proof,
  plus negatives that promote pending or hermetic proof to operational-ready;
- exactly one common autorun-catalog membership for the existing checker;
- worker-return fast-gate evidence, exact changed-set reconciliation, and
  independent probe pending for Local;
- reviewer completion with a distinct oracle before material closure.

## Acceptance Boundary

T2 is acceptable only if it strengthens forward-only dispatch admission and
does not reinterpret closed historical packets. Static PASS means the declared
relations are complete and internally consistent. It does not prove the
declared rights, operating-system state, runtime transaction, model behavior,
or independent-review judgment are true.

No duplicate checker, parallel transaction standard, new runtime wrapper, or
provider-specific policy may be introduced.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance-guard-authoring`, role=`INTERNAL_AGENT`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "governance-guard-authoring" --role INTERNAL_AGENT --lifecycle-phase implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No registered ADIF entry changes this bounded extension. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Source Verification Block; Core Guard Self-Protection Authorization; Gate-To-Role Closeability Contract; independent probe plan; Review-Dispatch Convergence Control; corpus manifest and verdict; Public Export Disposition |
| gateRunPurpose | confirmation after source read-ahead, not first discovery |
| claimBoundary | dispatch baseline shape only; implementation must read every changed owner before edit |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Existing HRLTP is the canonical owner and already defines the nine proof fields. | EXISTS | `docs/reference/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_STANDARD_2026-09-22.md` | Contract Shape; Evidence Semantics | HRLTP contract | HRLTP standard | ACCEPT |
| Existing checker validates exact keys and closed values but lacks actor-resource-operation feasibility. | EXISTS | `governance/compat/check_high_risk_local_transaction_proof.py` | `REQUIRED_FIELDS`; `validate_contract` | `REQUIRED_FIELDS`; `validate_contract` | HRLTP checker | ACCEPT |
| Focused test owner already covers contract shape, risk triggers and Git scopes. | EXISTS | `governance/compat/test_check_high_risk_local_transaction_proof.py` | `ContractTests`; `GitScopeTests` | HRLTP focused test classes | HRLTP tests | ACCEPT |
| Work-order template routes applicable work to HRLTP. | EXISTS | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | High-Risk Local Transaction Proof Routing | HRLTP routing | canonical work-order template | ACCEPT |
| Guard orientation currently states nine fields and reviewer-fast as earliest admission. | EXISTS | `docs/reference/guard_orientation/README.md` | Common Failure Patterns | HRLTP routing paragraph | guard orientation index | ACCEPT |
| Common autorun catalog does not currently contain HRLTP. | EXISTS | `governance/compat/agent_autorun_command_catalog.py` | `_common_commands` | `_common_commands` | autorun command catalog | ACCEPT |
| Current autorun test owner already verifies common-command membership for other controls. | EXISTS | `governance/compat/test_run_agent_autorun_workflow_gate.py` | common-command membership tests | `_common_commands` tests | autorun workflow tests | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| T2 dispatch artifact paths | all three planned dispatcher artifacts were absent before authoring | PASS |
| Parallel owner search | no active role-capability transaction admission standard or checker exists | PASS |
| Existing owner choice | HRLTP T1 is active and sufficient as the extension owner | PASS |
| Hook duplication | existing reviewer-fast, pre-commit and pre-push entries remain; T2 adds only missing common pre-dispatch autorun membership | PASS |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | current HRLTP standard/checker/tests, work-order template, guard orientation and autorun catalog/test |
| Runtime behavior claimed | N/A_WITH_REASON: this baseline authorizes static repository governance only |
| Helper/checker implementation claimed | NOT_IMPLEMENTED_YET: implementation is the next bounded phase |
| Provider/live proof claimed | N/A_WITH_REASON: no provider or live call |
| Public-sync claimed | N/A_WITH_REASON: deferred private-only |
| Freshness disposition | PASS for dispatch authority; no target-runtime safety claim |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded GC-018 dispatch source verification.
- Corpus root: nine named current-authority source groups in Source Verification Block and the paired selection audit.
- Snapshot time: 2026-09-23 dispatch authoring.
- Enumeration command: filesystem-backed direct `Get-Content -LiteralPath` reads plus targeted `rg -n` checks.
- Manifest artifact or inline manifest: the exact nine-path input ledger below.
- Manifest hash: N/A with reason: bounded direct-read dispatch authority uses an inline manifest, not a generated corpus artifact.
- Processing ledger artifact or inline ledger: the exact nine-path input ledger below.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=9; ledger_terminal=9; exclusions=0; unreadable=0; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: nine manifest groups reconcile to nine terminal direct-read groups.
- Drift check: current filesystem bytes read on 2026-09-23; no all-repository claim.
- Output traceability: selection finding maps to paired baseline, exact work order and nine-path tranche manifest.
- Adversarial verification: overlap audit tested duplicate-owner, late-review-only and documentation-only escape alternatives.
- Corpus verdict: COMPLETE_VERIFIED

| Input path | Terminal status |
|---|---|
| `docs/audits/CVF_HRLTP_T2_OPERATIONAL_ROLE_CAPABILITY_CONSISTENCY_SELECTION_2026-09-23.md` | READ |
| `docs/reviews/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_COMPLETION_2026-09-23.md` | READ |
| `docs/reference/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_STANDARD_2026-09-22.md` | READ |
| `governance/compat/check_high_risk_local_transaction_proof.py` | READ |
| `governance/compat/test_check_high_risk_local_transaction_proof.py` | READ |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `governance/compat/agent_autorun_command_catalog.py` | READ |
| `governance/compat/test_run_agent_autorun_workflow_gate.py` | READ |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Private repository standard/checker/template/orientation/autorun admission only. |
| claimDisposition | CLAIM_REJECTED: no target transaction or runtime enforcement is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | local repository commands only; no provider/live/public invocation |
| interceptionBoundary | static changed-work-order admission; no operating-system or runtime interception |
| claimLanguage | authorization baseline, not implemented behavior |
| forbiddenExpansion | no ACEL continuation, account, credential, source, runtime, public or deployment effect |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-HRLTP-T2 baseline authoring, 2026-09-23 |
| Working directory | repository root |
| Command or tool surface | governed reads, search, patch and local checks |
| Target paths | selection audit, this baseline and paired work order |
| Allowed scope source | active post-G1 architecture-reassessment next move and operator foundation-uplift instruction |
| Before status evidence | HEAD `4952a0e3d3223f9ed7879d15512c897ea3222afe`; no T2 artifacts |
| After status evidence | bounded T2 authority defined; no implementation execution |
| Diff evidence | exact three dispatcher paths before commit |
| Approval boundary | dispatch authorization only |
| Claim boundary | no protected implementation path changed by this baseline authoring step |
| Agent type | Local orchestrator/dispatcher |
| Invocation ID | `cvf-hrltp-t2-baseline-2026-09-23` |
| Expected manifest | three dispatch-authoring paths |
| Actual changed set | populated by Local before dispatch commit |
| Manifest delta | expected NONE |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance foundation; public export is separate.

## Claim Boundary

This baseline authorizes only the paired static governance implementation
tranche. It does not certify any principal capability, operating-system right,
transaction, source, provider/live behavior, deployment or production state.

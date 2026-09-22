# CVF HRLTP T2 Operational Role-Capability Consistency Selection

Memory class: governed-selection-audit

docType: audit

Status: SELECTED_FOR_DISPATCH_AUTHORING

Date: 2026-09-23

Decision owner: Local orchestrator/reviewer

## Purpose

Audit the accepted ACEL G1-G4 learning against current CVF controls and select
at most one bounded foundation tranche. The selected work must close a real
admission gap without duplicating independent review, review-cost control,
dispatch-quality source verification, or the existing high-risk transaction
proof owner.

## Target / Source

The bounded source set is:

1. `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` - `READ`;
2. `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` - `READ`;
3. `docs/reference/CVF_GATE_TO_ROLE_CLOSEABILITY_MACHINE_STANDARD.md` - `READ`;
4. `docs/reference/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_STANDARD_2026-09-22.md` - `READ`;
5. `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` - `READ`;
6. `governance/compat/check_high_risk_local_transaction_proof.py` - `READ`;
7. `governance/compat/check_independent_review_probe_admission.py` - `READ`;
8. `governance/compat/check_review_cost_control.py` - `READ`;
9. `governance/compat/check_work_order_dispatch_quality.py` - `READ`;
10. `docs/reviews/CVF_ACEL_G1_T3B_R2_ATOMIC_ROTATION_CONTRACT_CORRECTION_COMPLETION_2026-09-20.md` - `READ`;
11. `docs/reviews/CVF_ACEL_G1_T3C_C2_LOCAL_READABILITY_REPAIR_DECISION_2026-09-22.md` - `READ`;
12. `docs/reviews/CVF_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_COMPLETION_2026-09-22.md` - `READ`;
13. `docs/audits/CVF_ACEL_G1_T3D_C2_SOURCE_CREATION_READINESS_GAP_AUDIT_2026-09-23.md` - `READ`;
14. `docs/reviews/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_COMPLETION_2026-09-23.md` - `READ`.

## Scope / Methodology

The audit compared each recurring defect class with the earliest current
written rule, static admission check, independent review boundary, and hook
phase. It treated a later independent probe that caught a defect as effective
containment, but not as proof that dispatch-time prevention already exists.
It did not rerun accepted implementation suites or recreate closed tranche
work.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Repeated ambiguity should become a written rule, machine check, then the earliest applicable phase gate. | EXISTS | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | Escalation Ladder | rule/check/earliest-gate sequence | CVF learning philosophy | ACCEPT |
| Gate-to-role closeability validates declared responsibility topology, not operational reality. | EXISTS | `docs/reference/CVF_GATE_TO_ROLE_CLOSEABILITY_MACHINE_STANDARD.md` | Machine Enforcement | declared responsibility topology | closeability standard | ACCEPT |
| HRLTP already owns peer exclusion, failure injection, semantic security tuples, rollback exactness and final evidence binding. | EXISTS | `docs/reference/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_STANDARD_2026-09-22.md` | Contract Shape; Evidence Semantics | nine-field proof contract | HRLTP standard | ACCEPT |
| The current HRLTP checker validates nine exact fields but has no actor-resource-operation feasibility relation. | EXISTS | `governance/compat/check_high_risk_local_transaction_proof.py` | `REQUIRED_FIELDS`; `validate_contract` | `REQUIRED_FIELDS`; `validate_contract` | HRLTP checker | ACCEPT |
| Independent-probe admission validates evidence shape, integrity and separation rather than semantic sufficiency. | EXISTS | `governance/compat/check_independent_review_probe_admission.py` | module contract | `DeclarationScanner`; terminal probe bindings | independent-probe admission checker | ACCEPT |
| Review-cost control validates convergence fields and escalation, not semantic review quality. | EXISTS | `governance/compat/check_review_cost_control.py` | module contract | review-cost field contract | review-cost checker | ACCEPT |
| The accepted C0-R1 completion records the cross-principal read contradiction, missing hard-crash cleanup owner and delete-right conflation. | EXISTS | `docs/reviews/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_COMPLETION_2026-09-23.md` | Findings; Finding-To-Governance Learning Disposition | IP-01 through IP-03; machine-check candidates | accepted Local completion | ACCEPT |

## Findings / Position

Most G1-G4 findings are already governed or are deliberately left to a
separate runtime-specific evidence lane:

| Finding family | Existing owner | Disposition |
|---|---|---|
| ineffective negative test or same-oracle self-proof | independent-probe admission plus reviewer adversarial proof | NO_NEW_CONTROL |
| repeated repair turns and repair regressions | review-cost convergence, complete pre-repair dependency audit and targeted regression guard | NO_NEW_CONTROL |
| source facts, command signatures and canonical owner paths | dispatch-quality source verification | NO_NEW_CONTROL |
| peer exclusion, deterministic barriers, exception cleanup, semantic security rollback and frozen evidence | HRLTP T1 | EXTEND_EXISTING_OWNER_ONLY |
| actor assigned an action or observation its declared resource capability forbids | no current machine relation | SELECT_T2 |
| hard-crash residue without an authorized cleanup actor or unknown-artifact disposition | no complete current relation | SELECT_T2 |
| parent child-deletion authority conflated with individual-file deletion authority | no exact operation vocabulary in current admission | SELECT_T2 |

The precise missing control is not a new review system. It is a static
feasibility join inside the existing HRLTP owner:

`actor x resource x operation x declared capability x evidence owner`.

The join must be evaluated before implementation for both an executable
high-risk transaction and a normative design/amendment that binds a future
transaction. A documentation-only packet must not avoid the feasibility check
when its output is an active operational contract.

## Risk / Corrective Action

The principal risk is over-generalization. A broad semantic checker would
prescribe architecture, create false confidence, or duplicate reviewer
judgment. T2 therefore admits only closed structured declarations and exact
relations:

- every required action or observation maps to a declared allowed capability
  for the same actor and resource;
- a declared forbidden capability cannot simultaneously be required;
- recovery names the residue identity, cleanup actor, required cleanup
  capability and unknown-artifact disposition;
- Windows deletion semantics distinguish parent-directory child-deletion
  authority from an individual file's deletion authority;
- hermetic evidence cannot satisfy an operational real-principal proof field;
- machine PASS remains static authoring admission, not runtime truth.
- applicable relations must be non-empty; actor, resource and action IDs and
  actor/resource capability rows must be unique; evidence owners must be known
  and capable; operations must be compatible with their resource class;
- a normative design may declare actual-token proof `PENDING` only at a
  contract-only ceiling. Pending or hermetic evidence cannot promote an
  operational-ready claim.

## Decision / Disposition

Selected tranche: `CVF-HRLTP-T2`.

Selected route: extend the existing HRLTP standard, checker and focused tests;
update its current work-order-template and guard-orientation routing; add the
existing checker to the common pre-dispatch autorun catalog and prove that
membership with its current catalog test owner.

No new parallel standard, checker family, agent-role taxonomy, provider policy,
or runtime interception layer is selected.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| active operational contract can assign a principal an impossible or forbidden operation | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE_SELECTED | extend HRLTP with actor-resource-operation feasibility admission |
| hard-crash residue lacked a lawful cleanup owner and unknown-artifact rule | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE_SELECTED | add closed recovery-ownership fields and fail-closed relations |
| parent and individual-file deletion rights were conflated | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE_SELECTED | use exact controlled operation vocabulary and adversarial fixtures |
| independent review caught the defects and the correction regressions | REVIEW_REPAIR_REGRESSION | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | retain the existing independent-probe and review-cost controls without duplication |
| runtime/provider/cost learning applicability | RUNTIME_SIGNAL_GAP | COST_ECONOMICS_LEARNING | N/A_WITH_REASON | no provider invocation, live transaction, quota or per-model cost evidence belongs to this bounded static selection |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded governance-overlap selection audit.
- Corpus root: fourteen exact current-authority paths under Target / Source.
- Snapshot time: 2026-09-23 selection audit.
- Enumeration command: filesystem-backed direct `Get-Content -LiteralPath` reads plus targeted `rg -n` checks.
- Manifest artifact or inline manifest: numbered Target / Source list in this audit.
- Manifest hash: N/A with reason: bounded direct-read audit uses an inline manifest, not a generated corpus artifact.
- Processing ledger artifact or inline ledger: Source Verification Block and Findings / Position classification table.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=14; ledger_terminal=14; exclusions=0; unreadable=0; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: fourteen manifest paths reconcile one-to-one to fourteen terminal `READ` rows in the numbered Target / Source ledger.
- Drift check: current filesystem bytes were read on 2026-09-23; no historical completeness claim is made.
- Output traceability: three selected findings map to one paired baseline and one dispatch work order.
- Adversarial verification: tested no-op, duplicate-control and broad semantic-checker alternatives before selecting the narrow existing-owner extension.
- Corpus verdict: COMPLETE_VERIFIED

## Epistemic Process Block

| Field | Value |
|---|---|
| known | Current controls already own source verification, review convergence, independent-probe separation and nine-field transaction proof admission. |
| inferred | The repeated cross-principal contradictions share one missing machine relation: required operation versus declared capability and recovery owner. |
| unknown | Whether the future implementation can express every needed operation without an over-broad vocabulary; focused adversarial tests decide that. |
| validation | Paired GC-018 baseline, dispatch work order, focused checker tests and a distinct Local independent probe. |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer with read-only governance overlap audit |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-HRLTP-T2 selection, 2026-09-23 |
| Working directory | repository root |
| Command or tool surface | governed file reads, `rg`, line-level comparison and Git status |
| Target paths | the ten bounded source groups and this selection artifact |
| Allowed scope source | active handoff authorizes one bounded post-G1 foundation-learning selection |
| Before status evidence | HRLTP T1 active; G1-G4 findings accepted; no T2 artifact existed |
| After status evidence | one bounded extension selected; no implementation executed |
| Diff evidence | this audit plus paired baseline/work order only |
| Approval boundary | selection and dispatch authoring only |
| Claim boundary | no checker, hook, runtime, source, credential, provider, public or deployment mutation |
| Agent type | Local orchestrator/reviewer |
| Invocation ID | `cvf-hrltp-t2-selection-2026-09-23` |
| Expected manifest | exactly three dispatch-authoring artifacts |
| Actual changed set | populated by Local before dispatch commit |
| Manifest delta | expected NONE |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance selection; no public-sync artifact is in
scope.

## Claim Boundary

This audit selects one static, forward-only CVF foundation tranche. It does not
implement the control, certify any transaction, authorize ACEL continuation,
or open runtime, source, credential, provider/live, public or deployment work.

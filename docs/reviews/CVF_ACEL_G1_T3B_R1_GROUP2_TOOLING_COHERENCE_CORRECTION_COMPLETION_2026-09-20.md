# CVF ACEL G1 T3B R1 Group 2 Tooling Coherence Correction Completion Review

Memory class: governed-review

docType: review

Status: BLOCKED_WITH_REASON

Date: 2026-09-20

executionBaseHead: `12d2d0d7437db746e4c4c038cf88eb881e03c23d`

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_2026-09-20.md`

Reviewer: Local orchestrator/reviewer

independentProbeRequired: YES

independentProbeDisposition: FAIL_INDEPENDENT_PROBE

## Purpose

Review the returned five-path R1 tooling correction without recreating its
implementation. The review consumes the worker's valid evidence, checks only
the admitted ACL, per-version binding and supersession seams, and determines
whether Group 2 tooling is safe to commit or requires one consolidated
contract-level successor.

## Scope / Methodology

Role: Local orchestrator/reviewer. Phase: R1 completion review. Decision owner:
Local for acceptance, bounded reviewer repair, successor architecture and
commit. The shared-workspace worker remains an `INTERNAL_AGENT`; provider
identity supplies no authority.

The review reused the reported 48/48 spec-writer, 63/63 decision-writer and
47/47 Python results, then reran those suites once because the admitted
independent probe targeted the state-machine boundary those suites claimed to
prove. It also ran the worker-return fast gate once and executed an in-memory
PowerShell probe over the returned functions. No credential, `runas`, alternate
principal, real Group 2 path, provider, live, public or deployment action was
used.

## Target / Source

- R1 work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_2026-09-20.md`.
- R1 worker return: `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-20.md`.
- controlling Group 2 contract: `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`.
- returned decision writer: `scripts/acel_g1_approver_group2_decision_writer.ps1`.
- returned checker and tests: `governance/compat/check_acel_g1_verification_authority_spec.py`; `governance/compat/test_check_acel_g1_verification_authority_spec.py`.
- returned spec writer: `scripts/acel_g1_party_a_group2_spec_writer.ps1`.

## Findings / Position

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| T3B-R1-RV-1 | CRITICAL | The required supersession state is unreachable. Full-history replay rejects a newer `ACTIVATED` replacement while the old version remains active, but the R1 supersession guard requires that replacement already be active before it may supersede the old version. | ATOMIC_ROTATION_CONTRACT_REQUIRED |
| T3B-R1-RV-2 | HIGH | The closed `cvf.specDecisionEvent` schema has no replacement-version or replacement-hash fields. `-ReplacementSpecVersion` exists only as an invocation parameter and is discarded before the durable event is hashed/appended, so later verification cannot prove which newer version authorized the supersession. | DURABLE_REPLACEMENT_BINDING_REQUIRED |

The ACL correction, explicit Local/Approver read grants, per-version file
resolution, and per-version hash comparison are accepted as valid partial R1
work and must be preserved. They do not overcome the two supersession defects.

## Independent Probe Evidence

### Positive controls consumed

- spec writer self-test: 48/48 PASS, exit 0;
- decision writer self-test: 63/63 PASS, exit 0;
- Python checker tests: 47/47 PASS, exit 0;
- worker-return fast gate: COMPLIANT, exit 0;
- both real Group 2 paths remained absent.

### Decision-changing probe

The reviewer parsed only function/type definitions from the returned decision
writer into memory and constructed hash-linked v1/v2 events without writing a
file.

```text
PROBE_TWO_ACTIVE=REJECTED [DECISION_MULTIPLE_ACTIVE_VERSIONS] more than one specVersion is simultaneously ACTIVATED-without-SUPERSEDED: 1, 2
PROBE_OLD_ALREADY_SUPERSEDED=ACCEPTED active=2
```

The first result proves the work-order prerequisite "old active plus already
activated replacement" cannot pass the same replay used by real mode. The
second proves the R1 positive guard test accepts a history only after the old
version was already superseded, so it does not prove the proposed append.

### Durable-schema inspection

The controlling closed preimage contains only `decisionEventId`, `eventType`,
`specVersion`, `recomputedHashHex`, `approverId`, `decidedAt`, and
`priorEntryHashHex`. The real writer builds the appended record from those
fields and does not serialize `ReplacementSpecVersion`. Therefore an appended
`SUPERSEDED` event binds the old version/hash only.

## Root Cause / Responsibility

This is an orchestrator/contract defect, not merely worker non-compliance. The
T2F contract simultaneously requires:

1. a newer version to activate before the old version is superseded;
2. zero or one active version at every replay point; and
3. a durable supersession naming which version remains active.

Its closed event schema cannot represent item 3, while items 1 and 2 cannot
both hold in an append-only two-event sequence. The R1 work order repeated that
contradiction. The worker implemented the impossible acceptance contract and
its test selected an already-superseded history, masking the conflict.

## Selected Architecture Correction

Use one atomic rotation event rather than a transient two-active state:

- add required nullable `replacementSpecVersion` and
  `replacementRecomputedHashHex` fields to the closed event preimage;
- both fields are `null` for `APPROVED`, `REJECTED`, and ordinary `ACTIVATED`;
- for `SUPERSEDED`, both fields are non-null and bind a strictly greater,
  independently validated, `APPROVED` but not-yet-active replacement;
- applying that one event atomically removes the old version from the active
  set and adds the replacement, preserving exactly one active version;
- the replacement is thereafter considered activated by the atomic rotation
  and can itself be superseded later;
- an ordinary `ACTIVATED` event is valid only when no version is active.

No operational source exists, so the proposed schema can be corrected before
first establishment without migration or backward-compatibility debt.

## Risk / Corrective Action

Do not commit or execute the returned tooling. Dispatch one R2 correction that
updates the controlling T2F contract and the decision writer/checker/test
surfaces together, preserves the accepted ACL/per-version corrections, and
repairs the existing worker return. The spec writer is preserved byte-for-byte
and is not an R2 worker-owned path.

Required regressions:

1. `APPROVED(v1) -> ACTIVATED(v1) -> APPROVED(v2) -> SUPERSEDED(v1,replacement=v2)` passes and ends with only v2 active.
2. The same rotation with missing, equal/lower, unapproved, already-active,
   already-superseded, missing-file, wrong-hash or mismatched replacement fails.
3. Removing or mutating either durable replacement field invalidates the event
   preimage/digest or closed schema.
4. A standalone `ACTIVATED(v2)` while v1 is active still fails closed.

## Decision / Disposition

`REWORK_REQUIRED`.

T3B-RV-1, T3B-RV-2 and packet-shape portions of the earlier R1 are accepted
and reusable. T3B-RV-3 is not closed. Group 2 tooling remains unaccepted and
uncommitted. Real source creation, activation, consumer wiring, promotion and
candidate admission remain closed.

## Semantic Convergence Control

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3b-group2-source-creation-tooling-problem","chainMode":"SUCCESSOR","chainOrdinal":3,"predecessor":{"path":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_2026-09-20.md","sha256":"fb039baeb71106c9c4c86ffe626bdc3b50d7b6c0136ba8faf9cbcd28bb6b99e4"},"blockerDelta":{"prior":["acel_g1_group2_real_source_not_created","group2-tooling-r1-not-accepted"],"resolved":[],"retained":["acel_g1_group2_real_source_not_created","group2-tooling-r1-not-accepted"],"new":["unreachable-supersession-state","unbound-durable-replacement"],"reopened":["supersession-entry-gap"],"current":["acel_g1_group2_real_source_not_created","group2-tooling-r1-not-accepted","unreachable-supersession-state","unbound-durable-replacement","supersession-entry-gap"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":2,"nonDecreasingBlockerTransitions":1},"claims":[{"claimId":"ACEL-G1-T3B-R1-REVIEW","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/reviews/CVF_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_COMPLETION_2026-09-20.md"}],"requiredDisposition":"ROOT_CONTRACT_REQUIRED","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

## Review Cost And Diminishing Return Control

| Field | Value |
|---|---|
| reviewMode | EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION |
| evidenceReused | worker counts, exact five-path return, worker-return fast gate |
| rerunReason | admitted critical supersession probe contradicted the worker's positive test |
| expectedInformationGain | determine whether real-mode rotation is reachable and durably verifiable |
| observedInformationGain | unreachable state plus missing durable replacement binding confirmed |
| duplicateRerunDisposition | no additional broad rerun authorized |
| stopCondition | one consolidated R2 contract correction; no per-row repair loop |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| literalTokensReviewed | review heading families, exact status token, finding defect class, independent probe disposition, epistemic Comparison/Contradiction/Claim Update labels, corpus reconciliation scalar markers |
| gateRunPurpose | confirmation after authoring, not first discovery of required shape |
| claimBoundary | checker-shape evidence only; not proof of implementation acceptance |

## Finding-To-Governance Learning Disposition

- Defect class: `ORCHESTRATOR_PACKET_GAP`
- Learning lane: `GOVERNANCE_CONTROL_PLANE`
- Disposition: `RULE_EXISTS`
- Existing rule applied: contradictory acceptance conditions must be corrected
  at the earliest owning contract rather than patched only in implementation.
- Machine-check elevation: not yet justified as a generic checker; the R2
  regression suite becomes the earliest executable guard for this domain.

## Epistemic Process Block

### Expected Result / Prediction

R1 was expected to preserve one-active semantics while validating an already
activated replacement.

### Observed Result

The admitted probe rejected the necessary two-active pre-state, while the R1
positive replacement test passed only after the old version was already
superseded.

### Evidence Comparison

The observed function behavior contradicts both the R1 claim and the T2F
rotation prose; the closed event schema independently confirms there is no
durable replacement citation.

### Contradiction or Gap Disposition

Contract-level contradiction confirmed; route to one atomic-rotation R2.

### Claim Update

R1 is not complete. ACL and per-version binding fixes remain valid partial
evidence; supersession/rotation readiness is withdrawn.

## Corpus Completeness And Report Integrity

- Corpus task class: bounded named-source completion review.
- Corpus root: the R1 work order, return, controlling T2F contract and five returned outputs.
- Snapshot time: 2026-09-20 at review HEAD `12d2d0d74`.
- Enumeration command: filesystem-backed direct file reads of the named bounded set.
- Manifest artifact or inline manifest: paths listed under Target / Source plus the R1 work order's exact five-path manifest.
- Manifest hash: N/A with reason: bounded direct review uses the committed R1 manifest and creates no standalone corpus manifest.
- Processing ledger artifact or inline ledger: Target / Source and Independent Probe Evidence.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=all named review inputs; ledger_terminal=READ; exclusions=all paths outside this bounded review; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: all files outside the named bounded review.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate is generated.
- Drift check: worker-owned paths remained uncommitted and staging remained empty during review.
- Output traceability: Target / Source, Independent Probe Evidence and Agent Operation Trace Block identify every reviewed input and result.
- Adversarial verification: the in-memory two-active and already-superseded probes challenge the exact accepted supersession claim.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | ACEL-G1-T3B-R1 completion review, 2026-09-20 |
| Working directory | repository root |
| Command or tool surface | governed reads, focused suites, in-memory PowerShell function probe, apply_patch, governance gates and Git |
| Target paths | R1 return and five worker outputs; this reviewer-owned completion review |
| Allowed scope source | R1 work order Review Gate and standing Local reviewer/closer authority |
| Before status evidence | R1 return COMPLETE_PENDING_REVIEW; eighteen untracked paths; staging empty |
| After status evidence | R1 rejected for consolidated atomic-rotation contract correction |
| Diff evidence | exact status and staged manifest checked before any commit |
| Approval boundary | review, successor dispatch and bounded metadata repair only |
| Claim boundary | no real Group 2 source, principal execution, activation, admission, live/public/deployment effect |
| Agent type | Local reviewer/closer |
| Invocation ID | `acel-g1-t3b-r1-independent-review-20260920` |
| Expected manifest | this review plus later paired R2 baseline/work order |
| Actual changed set | reconciled before material commit |
| Manifest delta | pending dispatch construction |
| Deletion or rename disposition | none |

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: private provenance review and local tooling correction; no public
artifact or public-sync action is authorized.

## Claim Boundary

This review rejects R1 supersession readiness and selects a bounded atomic
rotation correction. It does not establish or activate Group 2, execute either
principal, promote a key, admit a candidate, wire a consumer, or authorize
provider/live/runtime/public/deployment behavior.

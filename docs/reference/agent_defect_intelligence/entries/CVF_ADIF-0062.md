# ADIF-0062 - Acceptance Chain Lacks A Machine-Readable Join

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0062
title: Acceptance chain lacks a machine-readable join
defectCategory: CLOSURE_EVIDENCE
defectClass: MACHINE_GATE_GAP
defectRole: ROOT_CAUSE
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Work-order authoring / dispatch; Worker execution (WORKER_MUST_NOT_COMMIT); Reviewer-return review; Closure / final acceptance
roles: dispatcher; worker; reviewer; closer; session-sync steward
lifecyclePhases: pre-dispatch; pre-implementation; worker-return; pre-closure
surfaceSelectors: governed work orders and their required artifact manifests; worker returns; Git changed sets; per-deliverable proof; terminal status fields; reviewer completion packets
detectionSignals: COMPLETE_PENDING_REVIEW while a mandatory deliverable is absent; expected manifest cannot be parsed; actual changed set is self-declared or disagrees with Git; proof is not bound to a requirement; component or shape gates pass while an end-to-end semantic probe fails; a late live chain run exposes a previously hidden join gap
enforcementLevel: PARTIAL_CHECK
checkerBindings: governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_worker_return_quality_gate.py; governance/compat/check_agent_operation_trace.py; governance/compat/run_worker_return_fast_gate.py
promotionState: MACHINE_HARDENING_REQUIRED
supersedes: NONE
lastVerifiedCommit: 532e49a72
roadmapSeedId: NONE
```

## Purpose

Record the system-level cause exposed by the RSE-T4-H1 return: CVF has
separate authority, required-deliverable, worker-return, Git, proof and status
surfaces, but no single machine-readable acceptance ledger joins them from the
dispatcher-owned requirement through independently observed completion to a
deterministic terminal status.

The worker's incorrect return is evidence of this gap, not its complete cause.
Local review caught the contradiction as a compensating control after the
available fast gates had passed.

## Scope / Applies To

Applies to delegated work whose acceptance depends on multiple mandatory
deliverables, bounded path manifests, proof artifacts or a terminal worker
status. It covers dispatch feasibility, worker-return admission, reviewer
acceptance and closure handoff.

It does not define the future ledger schema, authorize implementation, replace
semantic review, or claim every workflow needs the same proof depth. It
requires one traceable join appropriate to the task's risk and acceptance
contract.

## System Chain Root Cause

The affected chain is:

`governed requirement -> dispatch feasibility -> produced artifact ->
machine-observed actual state -> requirement-bound proof -> terminal status ->
review closure`

The current controls validate portions of that chain but do not share a
canonical requirement identity or one acceptance reducer. In the observed
case:

1. the work order named a mandatory deliverable, but no machine-owned ledger
   row required the return to resolve that deliverable;
2. the operation trace took its expected manifest from worker-authored prose;
3. the prose did not yield concrete paths, and the comparison had no effective
   expected set;
4. the return's manifest-delta wording was not semantically reconciled with
   Git's actual changed set;
5. the worker selected `COMPLETE_PENDING_REVIEW` even though a required
   deliverable was missing; and
6. structural fast gates passed before an independent Local probe exposed the
   false-negative behavior and status contradiction.

This is an oracle-separation defect: the actor being evaluated can currently
supply too much of the expected state, actual state and conclusion that the
machine checks then validate.

## Why The Gap Stayed Hidden

Earlier Local reviews manually rejected incorrect completion labels and
out-of-manifest changes, so human review masked the absence of an integrated
machine join. Later guards were added from individual incidents and primarily
checked document shape or known phrases. That improved specific cases without
proving the whole acceptance route.

The full chain was also not exercised continuously in a production-like
end-to-end path. Component checks and use-case fixes could therefore pass while
the joins between requirement, observed artifact, proof and status remained
dormant. The current failure is useful evidence: running the real chain made a
deeper control-plane gap visible early enough to harden the foundation.

## Bad Example

A work order requires a contract, tests and a template. The worker omits the
template, describes its expected manifest only as "the paths in the work
order," reports a partial changed set and selects `COMPLETE_PENDING_REVIEW`.
Independent checkers validate the return's headings and allowed status token,
but no machine row joins the missing template to Git truth and forces a blocked
status.

## Good Example

The dispatcher assigns a stable ID to every required deliverable. At return,
Git or another governed observer supplies the actual artifact set, every proof
references the relevant requirement ID, and one deterministic reducer derives
the terminal status. An absent artifact, unparseable expected manifest,
unbound proof or failed mandatory assertion makes the return
`BLOCKED_WITH_REASON`; the worker cannot override that result with prose.

## Canonical Sources

- `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0061.md`
- `docs/reviews/CVF_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_COMPLETION_2026-09-28.md`
- `docs/reviews/CVF_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_WORKER_RETURN_2026-09-28.md`
- `docs/reviews/evidence/rse-t4-h1-independent-probe-2026-09-28.json`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/check_worker_return_quality_gate.py`
- `governance/compat/check_agent_operation_trace.py`
- `governance/compat/run_worker_return_fast_gate.py`

## Remediation

1. Define a canonical machine-readable acceptance ledger whose row identity is
   owned at dispatch and joins `required deliverable -> actual artifact ->
   proof -> terminal result`.
2. Derive actual changed paths from Git or the governed execution surface; do
   not treat a worker-authored list as the acceptance oracle.
3. Fail closed when an expected manifest or required-deliverable reference is
   absent, ambiguous or unparseable.
4. Bind each proof record to an exact requirement ID and require an allowed
   disposition for every mandatory row.
5. Derive the worker-return terminal status with one deterministic reducer;
   any unresolved mandatory row must prevent a complete status.
6. Add pre-dispatch projected-mutation feasibility checks, including governed
   file-size and allowed-path consequences that can be known before execution.
7. Exercise the entire acceptance route with hostile end-to-end fixtures, not
   only component gates or examples matching prior incident wording.
8. Make `SYSTEM_CHAIN_ASSESSMENT_REQUIRED` the default first disposition for a
   novel or strange learning until all chain joins are demonstrated.
9. Place prevention at the earliest phase that owns the relevant fact while
   retaining independent reviewer evidence for semantic contradictions.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Required deliverables are not joined to actual artifacts, proof and status by one machine-readable record | `MACHINE_GATE_GAP`; `RULE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` | define the acceptance ledger and deterministic reducer | deferred to RSE-T4-H1-R1 foundation hardening |
| Expected and actual manifests can be supplied by the worker being evaluated | `ORCHESTRATOR_PACKET_GAP`; `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `STANDARD_UPDATED` | restore dispatcher and Git oracle separation | deferred to RSE-T4-H1-R1 foundation hardening |
| The gap remained latent while only components and prior use cases were checked | `PHASE_GATE_PLACEMENT_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` | add hostile end-to-end acceptance-chain proof at the earliest owned phases | deferred to RSE-T4-H1-R1 foundation hardening |
| An unusual return exposed a broader chain defect | `RULE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `STANDARD_UPDATED` | require chain-first assessment before a local-only repair classification | handled by the learning-philosophy update in this entry batch |

Runtime/provider/cost learning lane: `N/A_WITH_REASON` - this entry concerns
repository governance joins and worker-return acceptance. It makes no provider
quality, credential, quota, cost or production-runtime claim.

## Epistemic Process Block

### Expected Result / Prediction

The RSE-T4-H1 work order and worker-return fast gates were expected to reject a
complete status when a mandatory deliverable was absent or the reported
manifest disagreed with repository state.

### Evidence Comparison

The worker returned `COMPLETE_PENDING_REVIEW`; the available fast suite passed
69 of 69 checks. Independent Local review found the mandatory template absent,
found the claimed path counts inconsistent with Git, and produced four hostile
semantic cases that the implementation accepted incorrectly.

### Contradiction Or Gap Disposition

Reject the worker completion, preserve the evidence, and treat the incident as
an end-to-end acceptance-chain defect. Do not narrow the corrective tranche to
the four classifier predicates or to one prohibited status phrase.

### Claim Update

CVF has partial dispatch, trace and return-quality checks. It does not yet have
a machine-readable ledger that proves every mandatory deliverable reached an
actual artifact, valid proof and correctly reduced terminal status.

## ADIF Defect Registry Disclosure

ADIF-0061 owns the classifier-block/operator-escalation event that triggered
the tranche. It does not own the acceptance-chain failure exposed by the
returned implementation. Existing worker-return and operation-trace guards are
partial checker bindings, not an integrated ledger. ADIF-0062 therefore
records the distinct systemic gap without superseding ADIF-0061.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer acting as governance-learning owner |
| Provider or surface | private CVF workspace |
| Session or invocation | RSE-T4-H1 blocked closure and system learning capture, 2026-09-28 |
| Working directory | repository root |
| Command or tool surface | governed source reads, `rg`, Git inspection, independent probe evidence, `apply_patch`, focused governance gates |
| Target paths | this entry; `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` |
| Allowed scope source | operator instruction to record the missing acceptance ledger and apply chain-first assessment to future strange learning |
| Before status evidence | RSE-T4-H1 completion at `532e49a72` rejects a worker return after 69/69 fast gates and records the missing deliverable, Git mismatch and semantic false negatives |
| After status evidence | ADIF-0062 makes the systemic gap discoverable and the learning philosophy requires chain-first assessment; machine hardening remains pending |
| Diff evidence | material diff limited to this entry and the canonical learning philosophy update |
| Approval boundary | durable learning and corrective direction only; no ledger, checker, hook, runtime or provider behavior implemented |
| Claim boundary | one evidenced acceptance-chain gap and its bounded recurrence rule; no universal frequency or prevention claim |
| Agent type | reviewer/closer |
| Invocation ID | `adif-0062-acceptance-chain-join-20260928` |
| Expected manifest | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0062.md`; `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` |
| Actual changed set | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0062.md`; `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance-learning and corrective-foundation evidence; no
public-sync authority.

## Claim Boundary

This entry records a systemic acceptance-chain gap exposed by one governed
worker-return review and related historical compensating controls. It does not
claim that every CVF lane is affected, that all existing gates are ineffective,
or that the proposed ledger is implemented. Closure requires a separately
authorized corrective packet and end-to-end machine evidence.

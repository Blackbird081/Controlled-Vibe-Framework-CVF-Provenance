# ADIF-0061 - Tool Classifier Escalates Governed Edit To Operator

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0061
title: Tool classifier escalates governed edit to operator
defectCategory: GATE_TRIGGER_FRICTION
defectClass: RUNTIME_SIGNAL_GAP
defectRole: ROOT_CAUSE
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Work-order authoring / dispatch; Worker execution (WORKER_MUST_NOT_COMMIT); Reviewer-return review
roles: dispatcher; worker; reviewer
lifecyclePhases: pre-dispatch; pre-implementation; worker-return
surfaceSelectors: governed work orders that authorize long authority/permission prose edits; blocked-edit tool events; RSE operator-question routing; worker returns that record tool/classifier friction
detectionSignals: an edit to an allowed governed prose field is blocked as instruction poisoning or equivalent; the tool/runtime surfaces retry, skip, or stop choices directly to the operator; the active packet already assigns the technical decision to the worker or Local reviewer; the event is omitted from the worker return
enforcementLevel: GUIDANCE_ONLY
checkerBindings: NOT_APPLICABLE_WITH_REASON - no current checker validates tool/classifier-block recovery at dispatch time
promotionState: DESIGN_REVIEW_REQUIRED
supersedes: NONE
lastVerifiedCommit: ca2101e76
roadmapSeedId: NONE
```

## Purpose

Make a recurring operator-reported friction pattern discoverable: an external
tool or auto-mode classifier can block a legitimate governed prose edit and
surface a technical recovery choice to the operator even when the work order
and RSE rules already assign that decision elsewhere.

## Scope / Applies To

Applies to governed worker lanes that edit authority, permission, boundary or
policy-shaped prose through a tool/runtime classifier. It covers packet
preparation, bounded recovery routing, durable event capture and early local
diagnostics. It does not weaken a safety classifier, bypass a platform prompt,
authorize hidden retries, or claim repository governance can control external
UI behavior.

## Bad Example

A work order says technical contradictions return to Local but says nothing
about a blocked-edit classifier. The worker submits one large policy-shaped
replacement. Auto-mode labels it instruction poisoning and asks the operator
whether to retry, skip or stop. The operator becomes the accidental technical
dispatcher, and a later worker return omits the event.

## Good Example

The packet classifies tool/classifier blocks before execution, gives the worker
a bounded atomic-edit strategy where the runtime permits it, forbids converting
the event into a worker-authored operator question, and requires a secret-safe
event record. If the platform itself forces an operator UI, the return records
that runtime boundary without pretending the prompt was suppressed. Local then
decides whether one fresh packet or foundation repair is warranted.

## Canonical Sources

- `docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md`
- `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md`
- `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md`
- `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`
- `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`
- `docs/reviews/CVF_CVF_NCR_R1_S11_TEST_EVIDENCE_AUDIT_PRODUCTION_RUNTIME_COMPLETION_2026-09-28.md`

## Remediation

1. Define a Tool/Classifier Block Recovery Contract owned by the RSE lane.
2. Add the contract to the governed work-order template and dispatch scaffold
   when prose-bearing mutations can trigger tool classification.
3. Distinguish worker-authored escalation from a platform-forced UI event.
4. Require bounded atomic-edit preparation, an explicit retry ceiling when a
   retry is technically available to the worker, and `BLOCKED_WITH_REASON` to
   Local when recovery is unavailable or exhausted.
5. Require the worker return to record classifier, affected path/field,
   attempted recovery count, operator-prompt source and claim boundary.
6. Add a pre-dispatch/pre-implementation checker and hostile fixtures for an
   `Instruction Poisoning` blocked-edit event, while preserving the explicit
   limitation that CVF cannot suppress external safety UI.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Existing no-question prose does not define recovery for tool-level classifier blocks | `RUNTIME_SIGNAL_GAP`; `RULE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `STANDARD_UPDATED` | add the bounded recovery contract to RSE owner surfaces | deferred to foundation hardening |
| RSE-T3 detects missing jurisdiction blocks only at return time | `PHASE_GATE_PLACEMENT_GAP`; `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` | validate applicable dispatch packets before worker execution and cover hostile blocked-edit examples | deferred to foundation hardening |
| External UI may still force operator interaction after local controls pass | `RUNTIME_SIGNAL_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `RUNTIME_LEARNING_CANDIDATE` | record the event and maintain a non-suppression claim boundary | deferred; external runtime limitation |

Runtime/provider/cost learning lane: `N/A_WITH_REASON` - this entry concerns a
tool-control event. It records no provider model output, credential, quota,
cost or production execution evidence.

## Epistemic Process Block

### Expected Result / Prediction

An existing RSE no-question rule and an explicit S11 no-question contract were
expected to keep routine technical recovery out of the operator lane.

### Evidence Comparison

The worker did not author an operator question in the return, but the tool/UI
still surfaced retry, skip and stop choices to the operator after classifying
the allowed governed prose edit as instruction poisoning. The return-time RSE
diagnostic did not prevent or durably capture that event.

### Contradiction Or Gap Disposition

Keep RSE's authority classification, add an earlier tool/classifier recovery
contract and machine admission check, and preserve the external-runtime
non-suppression boundary.

### Claim Update

RSE question jurisdiction exists, but exact tool-classifier recovery and early
enforcement remain unimplemented.

## ADIF Defect Registry Disclosure

Existing RSE T1-T3 and ADIF-0057 were inspected. RSE owns question
jurisdiction; ADIF-0057 owns unreachable gate/role sequencing. Neither entry
owns the exact tool-classifier false-positive plus operator-escalation event,
so ADIF-0061 records that bounded pattern without replacing either owner.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer acting as governance-learning owner |
| Provider or surface | private CVF workspace; operator-reported blocked-edit UI |
| Session or invocation | NCR-R1/S11 review and learning capture, 2026-09-28 |
| Working directory | repository root |
| Command or tool surface | governed source reads, `rg`, worker-return review, `apply_patch`, focused governance gates |
| Target paths | this entry and the S11 completion review |
| Allowed scope source | operator instruction to park NCR after review and harden CVF foundation for the recurring error |
| Before status evidence | RSE no-question rules and return-time diagnostic existed, but no exact classifier-block recovery contract or dispatch-time enforcement existed |
| After status evidence | defect is durably discoverable; implementation remains pending a bounded hardening packet |
| Diff evidence | new entry plus S11 blocked completion in the material review diff |
| Approval boundary | learning record and hardening direction only; no platform bypass, provider call or feature successor |
| Claim boundary | operator-reported bounded runtime signal; no universal frequency, classifier defect or prevention claim |
| Agent type | reviewer/closer |
| Invocation ID | `adif-0061-tool-classifier-escalation-20260928` |
| Expected manifest | this entry and S11 completion review |
| Actual changed set | verified before material commit |
| Manifest delta | MATCH_PENDING_FINAL_STAGED_VERIFICATION |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance-learning evidence; no public-sync authority.

## Claim Boundary

This entry records one first governed capture of a pattern the operator reports
as recurrent. It establishes a bounded hardening target. It does not prove the
external classifier is universally wrong, disable safety checks, guarantee
prompt suppression, authorize automatic retry, or claim implementation.

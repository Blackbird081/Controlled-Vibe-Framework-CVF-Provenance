# ADIF-0048 - Session-Start State Misreported As Dispatch Provenance

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0048
title: Session-start state misreported as dispatch provenance
defectCategory: SOURCE_FIDELITY
defectClass: EVIDENCE_INTERPRETATION_ERROR
defectRole: worker
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Worker execution (WORKER_MUST_NOT_COMMIT); Reviewer-return review; Closure
roles: worker; reviewer; closer
lifecyclePhases: pre-implementation; pre-closure
surfaceSelectors: no-commit worker outputs, resumed verification sessions, executionBaseHead evidence, file-existence claims
detectionSignals: a later session says outputs were present at session start while the dispatch or original return says they were absent before authoring; re-verification language is presented as authoring provenance
enforcementLevel: GUIDANCE_ONLY
checkerBindings: NOT_APPLICABLE_WITH_REASON: session identity and file creation provenance are not reliably exposed to current repository-local gates
promotionState: DESIGN_REVIEW_REQUIRED
supersedes: NONE
lastVerifiedCommit: 848e67bad
roadmapSeedId: NONE
```

## Purpose

Prevent a resumed or second verification session from replacing the original
dispatch baseline merely because worker outputs already exist when that later
session begins.

## Scope / Applies To

Applies to no-commit worker returns, resumed agent sessions, verification-only
passes, and reviewer closure whenever file presence or absence is used to
establish authorship, changed-set scope, or execution-base fidelity.

## Bad Example

A second session opens after a first session created the allowed outputs,
observes those files at its own startup, and reports that they were already
present without distinguishing its session baseline from the dispatch and
original-authoring baseline.

## Good Example

Record both facts with explicit time scopes: "present when verification
session B began" and "absent at dispatch/session A pre-edit, then created by
session A." Treat session B as re-verification evidence, not as the authoring
return.

## Canonical Sources

- `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`,
  phase/base-head/changed-set/trace ownership.
- `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`,
  worker-return and changed-set evidence.
- `docs/reviews/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_WORKER_RETURN_2026-07-23.md`,
  executionBaseHead, pre-flight evidence, and reviewer-owned provenance
  reconciliation.

## Remediation

Bind every file-existence statement to a named phase and session. Preserve the
committed dispatch baseline and original pre-edit evidence. A later verifier
may confirm content and gates but must not silently replace the authoring
trace. If the two records conflict, the reviewer reconciles timestamps, Git
state, output content, and both session statements before closure.

## Epistemic Process Block

### Expected Result / Prediction

A second verification session should be able to confirm existing outputs
without changing who created them or when they first appeared.

### Evidence Comparison

The T2 dispatch reviewer confirmed both paths absent at committed dispatch.
The original worker return records both paths absent before edits and created
after `executionBaseHead=848e67bad`. A later message said both were present at
that later session's start and no content was modified. Filesystem creation
times after dispatch support the original authoring trace and are compatible
with later-session re-verification.

### Contradiction Or Gap Disposition

The statements used different session baselines. The reviewer retained the
original authoring trace and bounded the later statement to re-verification.

### Claim Update

"Present at session start" is meaningful only with a session/phase identity.
It does not prove presence at dispatch or identify the authoring session.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | independent reviewer/closer |
| Provider or surface | local private provenance workspace |
| Session or invocation | EAIC-KR-T2 reviewer closure, 2026-07-23 |
| Working directory | repository root |
| Command or tool surface | local file reads, filesystem metadata, Git status, repository search, apply_patch, and governance gates |
| Target paths | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0048.md`; entries README row; T2 worker return |
| Allowed scope source | operator instruction to review, repair findings, and record reusable tranche learning |
| Before status evidence | later verification-session statement conflated its own startup state with the dispatch/original-authoring baseline |
| After status evidence | worker return contains a reviewer reconciliation and this entry is indexed for resolver discovery |
| Diff evidence | T2 material closure changed set and reviewer gate output |
| Approval boundary | evidence and governance-learning repair only; no runtime, checker, provider, CLI/MCP, public, or process action |
| Claim boundary | defect record and guidance only; no automated session identification or provenance enforcement |
| Agent type | reviewer/closer |
| Invocation ID | `eaic-kr-t2-adif-0048-2026-07-23` |
| Expected manifest | ADIF-0048; entries README row; T2 worker-return repair |
| Actual changed set | ADIF-0048; entries README row; T2 worker-return repair within T2 closure |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance learning. No public-sync action is authorized.

## Claim Boundary

This entry records a session-baseline provenance defect and bounded reviewer
remediation. It does not identify hidden provider sessions, measure usage,
intercept agent behavior, or authorize CLI/MCP, runtime, checker, public, or
production work.

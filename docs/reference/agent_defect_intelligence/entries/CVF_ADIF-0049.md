# ADIF-0049 - Governed Command Signature Invented Without Help Verification

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0049
title: Governed command signature invented without help verification
defectCategory: SOURCE_FIDELITY
defectClass: EVIDENCE_INTERPRETATION_ERROR
defectRole: dispatcher
severity: MEDIUM
lifecycleState: ACTIVE
taskClasses: Work-order authoring / dispatch; Reviewer-return review; Closure
roles: dispatcher; worker; reviewer; closer
lifecyclePhases: pre-dispatch; pre-implementation; pre-closure
surfaceSelectors: governed work-order command blocks and local checker invocations
detectionSignals: a work order names a checker flag that the checker's current argument parser rejects; worker must inspect --help and remove or replace the flag
enforcementLevel: GUIDANCE_ONLY
checkerBindings: NOT_APPLICABLE_WITH_REASON: current gates execute applicable checkers but do not validate every command example against each target parser
promotionState: DESIGN_REVIEW_REQUIRED
supersedes: NONE
lastVerifiedCommit: b84055f59
roadmapSeedId: NONE
```

## Purpose

Prevent dispatch packets from inventing plausible-looking checker arguments
that are absent from the current command-line parser.

## Scope / Applies To

Applies when a governed baseline, work order, review, or closure packet gives
an exact repository-local command that a later agent is required to execute.
It is especially relevant when nearby checkers accept path arguments but the
named bundle runner discovers changed artifacts from Git state instead.

## Bad Example

Require
`python governance/compat/run_worker_return_fast_gate.py --path <return>`
because an individual checker accepts a path selector, without checking the
bundle runner's own parser.

## Good Example

Run the target command with `--help`, inspect its current parser or official
usage text, and record only supported arguments. For the current worker-return
bundle, use:

`python governance/compat/run_worker_return_fast_gate.py`

## Canonical Sources

- `governance/compat/run_worker_return_fast_gate.py`, current argument parser
  and changed-file discovery behavior.
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`, checker
  read-ahead and verification-command requirements.
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`,
  pre-write literal and checker discipline.
- `docs/reviews/CVF_EAIC_KR_T3_OWNER_ARCHITECTURE_AND_THREAT_MODEL_WORKER_RETURN_2026-07-23.md`,
  Worker Experience Retrospective.

## Remediation

Before dispatch, verify every mandatory exact command against the target
script's current `--help` output or parser source. Do not transfer flags from a
similarly named individual checker to a bundle runner. If a worker encounters
an unsupported documentation-only flag, record the mismatch, use the
source-verified supported command when this does not alter authority or scope,
and return the packet for reviewer repair.

## Epistemic Process Block

### Expected Result / Prediction

Checker read-ahead should make mandatory command examples executable as
written.

### Evidence Comparison

The T3 work order cited the correct bundle script but added `--path`. Direct
`--help` inspection showed that the bundle accepts only `--pytest-target`.
Running the bundle without `--path` completed 62/62 checks successfully.

### Contradiction Or Gap Disposition

The required command and current parser contradicted each other. The worker
preserved scope, recorded the mismatch, and used the supported zero-path
invocation. Reviewer closure corrected both work-order occurrences.

### Claim Update

Naming the correct checker file is not sufficient source verification for an
exact command. Mandatory arguments also require parser or `--help`
verification.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | independent reviewer/closer |
| Provider or surface | local private provenance workspace |
| Session or invocation | EAIC-KR-T3 reviewer closure, 2026-07-23 |
| Working directory | repository root |
| Command or tool surface | local file reads, `--help`, repository search, apply_patch, and governance gates |
| Target paths | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0049.md`; entries README; T3 work order |
| Allowed scope source | mandatory ADIF learning capture and reviewer-owned closure conversion |
| Before status evidence | committed T3 work order contained two unsupported `--path` examples |
| After status evidence | both examples use the supported bundle command and this entry is resolver-discoverable |
| Diff evidence | T3 reviewer closure changed set and gate output |
| Approval boundary | documentation and governance-learning repair only; no runtime, provider, CLI/MCP, public, or process action |
| Claim boundary | defect guidance only; no automatic command-signature checker is claimed |
| Agent type | reviewer/closer |
| Invocation ID | `eaic-kr-t3-adif-0049-2026-07-23` |
| Expected manifest | ADIF-0049; entries README row; T3 work-order command repair |
| Actual changed set | ADIF-0049; entries README row; T3 work-order command repair |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance learning. No public-sync action is authorized.

## Claim Boundary

This entry records one command-signature source-fidelity defect and bounded
remediation. It does not implement a checker, validate arbitrary commands,
invoke an agent, or authorize runtime, provider, CLI/MCP, public, or
production work.

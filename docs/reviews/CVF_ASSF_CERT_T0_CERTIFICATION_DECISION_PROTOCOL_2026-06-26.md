# CVF Review: ASSF-CERT-T0 Certification Decision Protocol

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: review

Batch ID: ASSF-CERT-T0

## Purpose

Define the bounded protocol for deciding certification evidence for
`cvf-dispatch-quality-reviewer`.

## Target / Source

Target package:
`docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json`.

## Scope / Methodology

The protocol classifies the decision as evidence approval, evidence hold, or
evidence rejection. It does not mutate source lifecycle fields.

## Findings / Position

Certification evidence may be approved only if the package acceptance evidence
is source-backed and the UAT evidence satisfies that acceptance evidence. Source
state update remains a separate lane.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| Evidence decision could be conflated with source mutation | Prevented: decision vocabulary separates evidence approval from source-state update |
| Missing UAT could allow certification | Prevented: protocol requires real UAT evidence |

## Decision / Recommendation

Protocol disposition:
`CERTIFICATION_DECISION_PROTOCOL_ACCEPTED`.

Allowed T2 outcomes:

- `CERTIFICATION_EVIDENCE_APPROVED_SOURCE_STATE_UPDATE_DEFERRED`
- `CERTIFICATION_EVIDENCE_HELD_WITH_REASON`
- `CERTIFICATION_EVIDENCE_REJECTED_WITH_REASON`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| lifecycle guard requires UAT before certification | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `certificationState` | ASSF lifecycle guard | LITERAL_INVARIANT | ACCEPT |
| package acceptance evidence is source-backed | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `acceptanceEvidence` | ASSF registry entry | VALUE_SET | ACCEPT |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator approval to run certification-decision roadmap |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this T0 protocol review |
| Disposition | no external material absorbed |
| Claim boundary | repository-local source evidence only |

## Epistemic Process Block

### Expected Result

A certification decision protocol should require real UAT evidence and keep
source-state mutation separate.

### Evidence Comparison

The lifecycle guard separates UAT and certification, and the package entry has
explicit lifecycle source fields.

### Contradiction Or Gap Disposition

No contradiction blocks the protocol. The source-state update gap is deferred
to T3 next-control.

### Claim Update

T0 establishes the decision vocabulary for T2.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance certification protocol; no public-sync
authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-CERT-T0 certification decision protocol |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- protocol only |
| receiptEvidence | CVF_RECEIPT_PRESENT - source-backed protocol review |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- T0 protocol disposition |
| invocationBoundary | governed local documentation review |
| interceptionBoundary | no provider, CLI, MCP, Web runtime, adapter, package execution, lifecycle source mutation, or certification source-state mutation |
| claimLanguage | defines evidence-decision protocol |
| forbiddenExpansion | no package instance, lifecycle mutation, registry-source mutation, generated-index mutation, resolver mutation, runtime, adapter, provider/live, public-sync, push, activation, readiness, or session-sync |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| ARAM-T0 | lifecycle guard | certification/UAT separation | present | present | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Agent type | single-agent multi-role |
| Provider or surface | local workspace |
| Session or invocation | ASSF-CERT-T0 protocol, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | source reads, apply_patch, gates |
| Target paths | ASSF-CERT material manifest |
| Allowed scope source | ASSF-CERT work order |
| Before status evidence | baseHead `aad3b819` |
| After status evidence | T0 review pending material commit |
| Diff evidence | `git diff --name-status`; autorun gates |
| Approval boundary | protocol only |
| Claim boundary | no lifecycle source mutation |
| Invocation ID | `assf-cert-t0-protocol-2026-06-26` |
| Expected manifest | ASSF-CERT material manifest |
| Actual changed set | ASSF-CERT material manifest |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_FOR_CODEX_2026-06-26.md` | work order closed bounded | PASS |
| Completion or reviewer artifact | this artifact | `CERTIFICATION_DECISION_PROTOCOL_ACCEPTED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_PACKAGE_CERTIFICATION_DECISION_ROADMAP_2026-06-26.md` | T0 row closed bounded | PASS |
| Registry JSON | N/A with reason: no registry JSON mutation is authorized | no corpus registry JSON in changed set | BLOCKED with reason: out of scope |
| Registry Markdown | N/A with reason: no registry Markdown mutation is authorized | no corpus registry Markdown mutation | BLOCKED with reason: out of scope |
| External evidence digest | N/A with reason: no external artifact is created | no external digest applies | N/A with reason |
| System loop interlock | this artifact | no runtime loop or provider call | PASS |
| Session continuity | N/A with reason: session-sync is separate after material closure | active session paths excluded | N/A with reason |

## Claim Boundary

This T0 review defines the decision protocol only.

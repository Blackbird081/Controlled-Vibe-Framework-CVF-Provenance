# CVF GC-018 Baseline - SOT3-T8 Refinery-To-Kernel Packet Binding Contract

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-13

Baseline ID: GC-018-SOT3-T8

## Purpose

Authorize one bounded contract tranche that gives Refinery ownership of the
canonical hash used to bind a released `RefineryPacket` to Kernel admission.

## Target / Source

Current Refinery packet type and exports, Kernel packet-reference/admission
types, the accepted T6 local helper, the SOT contract chain, and the open
system-chain GAP entry.

## Scope / Methodology

Define one versioned packet-hash profile, implement it in Refinery, export it,
prove field-stability and deterministic vectors, and migrate the T6 slice to
the owner API without changing trust evaluation or Flow behavior.

## Findings / Position

The existing T6 helper proves a viable bounded algorithm but is caller-owned.
Refinery produces `RefineryPacket`, so Refinery is the canonical producer of
its binding identity. Kernel remains a verifier of equality only.

## Risk / Corrective Action

Hashing an unstable object shape can create silent incompatibility. The profile
must name its included fields, canonicalization, digest format, version, and
published vectors; unknown or unsupported profiles must fail closed.

## Decision / Baseline / Proposed Tranche

DISPATCH_READY: one `WORKER_MUST_NOT_COMMIT` source/test/contract tranche.

## Evidence / Verification

Require focused Refinery tests, cross-package integration tests, typecheck,
deterministic vectors, mutation sensitivity, unsupported-value rejection, and
proof that Kernel admission still rejects a mismatched binding.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| T7 closeout | `docs/reviews/CVF_SOT3_T7_SEMANTIC_VALUE_AUDIT_CLOSEOUT_COMPLETION_2026-07-13.md` | `f017dc775` | ACCEPT |
| Open GAP | `docs/reference/system_chain/gaps/entries/sot3_refinery_kernel_packet_binding_hash_owner_unresolved.json` | `5d7318098` | ACCEPT |
| Operator checkpoint | current operator approval | 2026-07-13 | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Refinery packet has no binding hash | `EXTENSIONS/CVF_REFINERY/src/types/refinery-packet.ts` | `RefineryPacket` declaration | `RefineryPacket` | Refinery type contract | ACCEPT |
| Kernel packet reference requires content hash | `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/refinery-packet.ts` | `RefineryPacketRef` declaration | `content_hash` | `RefineryPacketRef` | ACCEPT |
| Kernel evaluation requires packet hash | `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts` | `EvaluateInput` declaration | `packetHash` | `EvaluateInput` | ACCEPT |
| Kernel admission compares packet and request hashes | `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/admission.ts` | admission equality branch | `admitRequest` | Kernel admission | ACCEPT |
| T6 has a caller-local whole-packet helper | `EXTENSIONS/CVF_SOT_THREE_LAYER_SLICE/src/evidence/packet-hash.ts` | `packetContentHash` function | `packetContentHash` | T6 integration helper | ACCEPT |
| Refinery public exports are controlled centrally | `EXTENSIONS/CVF_REFINERY/src/index.ts` | public export list | `RefineryPacket` | Refinery package entrypoint | ACCEPT |
| GAP close condition requires canonical algorithm and owner | `docs/reference/system_chain/gaps/entries/sot3_refinery_kernel_packet_binding_hash_owner_unresolved.json` | `closeCondition` | `closeCondition` | system-chain GAP record | ACCEPT |

## Acceptance Criteria

- Refinery owns and exports one versioned packet-binding hash profile.
- Canonicalization and included field set are explicit and deterministic.
- Published positive vector and mutation/unsupported-value negatives pass.
- T6 slice consumes the Refinery owner API and retains its accepted behavior.
- Kernel equality checks remain fail-closed and are not weakened.
- Contract/reference and GAP disposition are updated only with reviewer proof.
- No AI, agent, prompt, provider, network, database, activation, or public work.

## ADIF Defect Registry Disclosure

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 30 --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021,
ADIF-0024.

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

## Checker Source Read-Ahead Block

| Field | Disposition |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Source Verification Block; Dependency Release Evidence; Agent Handoff Contract Control Block; Public Export Disposition |
| gateRunPurpose | confirm source fidelity and dispatch shape after direct source review |
| claimBoundary | packet authoring does not prove implementation |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind gc018-baseline --batch-id SOT3-T8 --title "Refinery Kernel Packet Binding Contract" --date 2026-07-13 --base d04715b1c --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | GC-018 no-commit contract baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | authored from verified runtime and GAP sources |
| checkerReadAheadConfirmation | dispatch and source-fidelity guards |
| docOnlyNewFields | versioned packet-binding profile identifier |
| claimBoundary | baseline only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This baseline authorizes only the paired no-commit T8 worker execution after
pre-dispatch passes. It does not authorize activation, provider/live work,
public-sync, release, or production readiness.

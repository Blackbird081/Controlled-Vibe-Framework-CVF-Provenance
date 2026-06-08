# CVF GC-018 DSCP-T9 Local Pipeline Harness Baseline

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-08

---

## Authorization

Authorized by operator instruction 2026-06-08: close DSCP-T6/T7/T8, then audit
and select the next roadmap for Claude execution.

Selection audit:

`docs/audits/CVF_POST_DSCP_T8_NEXT_ROADMAP_AUDIT_2026-06-08.md`

## Decision

Decision: open DSCP-T9 as a local deterministic integration harness. Claude
must add focused tests that prove the closed DSCP-T6, DSCP-T7, DSCP-T8, T3
governed packer, and T4 governed receipt helper compose without leaking raw
content or bypassing governance evidence.

## Purpose

DSCP-T1 through DSCP-T8 established individual surfaces. T9 checks the
cross-surface path:

- scan descriptor helper;
- ECO multi-domain request adapter;
- governed context packer;
- LPF memory block adapter;
- governed retrieval receipt helper.

The harness is a drift detector and integration proof only.

## Predecessor Evidence

| Predecessor | Closure evidence | Disposition |
|---|---|---|
| DSCP-T6 scan descriptor runtime | `docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_COMPLETION_2026-06-08.md`; commit `13cc1505` | ACCEPT |
| DSCP-T7 ECO multi-domain pilot | `docs/reviews/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_COMPLETION_2026-06-08.md`; commit `958f8d2b` | ACCEPT |
| DSCP-T8 MKE1 cross-lane wire-in | `docs/reviews/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_COMPLETION_2026-06-08.md`; commit `e96aacaf` | ACCEPT |
| Parent DSCP roadmap T1-T8 closure | `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md`; commit `e96aacaf` | ACCEPT |

## Scope / Target / Owner Boundary

In scope:

- Create `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.local.pipeline.harness.test.ts`.
- Add only the GC-051 registry entry needed for the new harness test path.
- Create a worker return packet for DSCP-T9.

Out of scope:

- No runtime source modification unless the worker first returns
  `BLOCKED_SOURCE_NOT_FOUND` with exact source evidence.
- No provider call, live governance proof, external API key use, corpus
  ingestion, OCR, vector retrieval, PolicyLocal T12 authoring, public-sync,
  hosted readiness, production readiness, public readiness, or answer-quality
  claim.

## Source Verification Summary

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: `buildGovernedArtifactDescriptor` helper | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | lines 31-60 | `buildGovernedArtifactDescriptor` | `GovernedArtifactDescriptorInput` | ACCEPT |
| EXISTS: `GovernedContextPackerContract.pack` local packer | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` | lines 52-99 | `GovernedContextPackerContract` | `GovernedContextPackerContract.pack` | ACCEPT |
| LITERAL_INVARIANT: governed packer emits `rawContentReleased: false` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` | lines 84-94 | `rawContentReleased` | `GovernedContextPackageEvidence` | ACCEPT |
| LITERAL_INVARIANT: governed packer emits `canBypassGovernance: false` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` | lines 84-94 | `canBypassGovernance` | `GovernedContextPackageEvidence` | ACCEPT |
| EXISTS: `buildGovernedRetrievalReceipt` helper | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.retrieval.receipt.ts` | lines 30-56 | `buildGovernedRetrievalReceipt` | `GovernedRetrievalReceiptInput` | ACCEPT |
| LITERAL_INVARIANT: retrieval receipt emits `rawSourceReleased: false` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.retrieval.receipt.ts` | lines 52-55 | `rawSourceReleased` | `GovernedRetrievalReceipt` | ACCEPT |
| EXISTS: ECO request adapter | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/dscp.eco.adapter.ts` | lines 19-34 | `buildECOGovernedPackRequest` | `GovernedContextPackRequest` | ACCEPT |
| EXISTS: LPF package adapter | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.lpf.adapter.ts` | lines 42-62 | `buildLPFGovernedPackage` | `GovernedContextPackage` | ACCEPT |
| EXISTS: `RAGResult` source shape | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/types.ts` | lines 23-29 | `RAGResult` | ECO RAG types | ACCEPT |
| EXISTS: `MemoryContextBlock` source shape | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | lines 27-35 | `MemoryContextBlock` | `packageMemoryContext` | ACCEPT |

## Evidence / Verification

| Evidence | Required result |
|---|---|
| Source Verification Summary | all rows ACCEPT with existing source paths |
| Work-order dispatch quality | PASS before Claude execution |
| Focused harness test | PASS during worker execution |
| CPF package check | PASS during worker execution |
| GC-051 registry check | PASS after new test path registration |

## Acceptance Criteria

| Criterion | Gate |
|---|---|
| ECO path composes descriptor, adapter, packer, and receipt | focused vitest PASS |
| LPF path composes memory block, adapter, and receipt | focused vitest PASS |
| Blocked gate returns blocked package without source artifact leakage | focused vitest PASS |
| Receipt gates are derived from package evidence | focused vitest PASS |
| `rawContentReleased`, `canBypassGovernance`, and `rawSourceReleased` remain false | focused vitest PASS |
| New test path is covered in GC-051 | registry check PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T9_LOCAL_PIPELINE_HARNESS_FOR_CLAUDE_2026-06-08.md` | `Status: DISPATCHED` before worker return | READY |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_COMPLETION_2026-06-08.md` | reviewer-authored after worker return | PENDING |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_ROADMAP_2026-06-08.md` | `Status: DISPATCHED` before worker return | READY |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | new harness path covered during worker execution | PENDING |
| Session continuity | active handoff and state registry | reviewer sync after closure | PENDING |

## Claim Boundary

This baseline authorizes a local deterministic integration harness only. It
does not authorize runtime source changes, provider calls, live governance
proof, external keys, corpus ingestion, OCR, vector retrieval, PolicyLocal T12,
public-sync, hosted readiness, production readiness, public readiness, or
answer-quality claims.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; not public-synced.

# CVF GC-018 DSCP-T11 Profile-Aware Pipeline Harness Baseline

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-10

---

## Authorization

Authorized by operator instruction on 2026-06-10: prove that the DSCP-T10
domain profile metadata and gate keys pass through the existing local DSCP
descriptor, ECO/LPF package, and retrieval receipt surfaces without content
release or cross-profile bleed.

Active state:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

## Decision

Open DSCP-T11 as a bounded deterministic harness tranche.

T11 consumes the already closed T10 profile contract and the earlier DSCP
descriptor, ECO adapter, LPF adapter, packer, and receipt helpers. It does not
create a new runtime contract.

## Purpose

DSCP-T10 proved a domain-profile contract. DSCP-T11 proves the next local
pipeline step: profile metadata (`domainFamily`, `jurisdiction`, `moduleId`) and
gate keys (`ec02Gate`, `stabilityGate`) survive profile application, descriptor
construction, package creation, and retrieval receipt construction while raw
source or raw memory release remains blocked.

## Predecessor Evidence

| Predecessor | Closure evidence | Disposition |
|---|---|---|
| DSCP-T10 domain profile contract | `docs/reviews/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_COMPLETION_2026-06-10.md`; material commit `0afa8737` | ACCEPT |
| DSCP-T9 local pipeline harness | `docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_COMPLETION_2026-06-08.md`; material commit `5c90506a` | ACCEPT |
| DSCP-T8 LPF adapter | `docs/reviews/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_COMPLETION_2026-06-08.md`; closure commit `e96aacaf` | ACCEPT |
| DSCP-T7 ECO adapter | `docs/reviews/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_COMPLETION_2026-06-08.md`; closure commit `958f8d2b` | ACCEPT |
| DSCP-T6 descriptor helper | `docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_COMPLETION_2026-06-08.md`; closure commit `13cc1505` | ACCEPT |

## Scope / Target / Owner Boundary

In scope:

- Add one focused CPF vitest harness for profile-aware DSCP pipeline behavior.
- Verify legal-policy profile data through descriptor -> ECO pack -> receipt.
- Verify technical-project profile data through descriptor -> LPF package ->
  receipt.
- Verify `BLOCKED_UNTIL_*` boundary rules stop at profile application before
  descriptor/package/receipt creation.
- Verify no gate or metadata bleed between legal-policy and technical-project
  profiles.
- Register the new test path in GC-051 JSON and Markdown.
- Create a worker return packet.

Out of scope:

- No external `Policy_Local` workspace edits.
- No new source contract, web route, provider call, API key use, corpus
  ingestion, OCR, vector retrieval, semantic ranking, T12 authoring,
  public-sync, hosted readiness, production readiness, or public readiness.

## Source Verification Summary

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: domain-profile contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 23-46 | `DscpDomainProfile` | `DscpDomainProfile` | ACCEPT |
| RUNTIME_BEHAVIOR: profile application helper | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 92-173 | `applyDomainProfileToDescriptorInput` | `ApplyDomainProfileResult` | ACCEPT |
| EXISTS: descriptor metadata owner | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 48-50 | `metadata` | `GovernedArtifactDescriptor` | ACCEPT |
| EXISTS: custom gate owner | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 11-25 | `customGates` | `GovernanceGateSet` | ACCEPT |
| RUNTIME_BEHAVIOR: descriptor builder preserves metadata | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | lines 31-56 | `buildGovernedArtifactDescriptor` | `GovernedArtifactDescriptorResult` | ACCEPT |
| EXISTS: ECO pack request helper | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/dscp.eco.adapter.ts` | line 19 | `buildECOGovernedPackRequest` | `GovernedContextPackRequest` | ACCEPT |
| RUNTIME_BEHAVIOR: LPF package blocks raw content release | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.lpf.adapter.ts` | lines 42-52 | `buildLPFGovernedPackage` | `GovernedContextPackage` | ACCEPT |
| RUNTIME_BEHAVIOR: retrieval receipt blocks raw source release | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.retrieval.receipt.ts` | lines 30-52 | `buildGovernedRetrievalReceipt` | `GovernedRetrievalReceipt` | ACCEPT |

## Evidence / Verification

| Evidence | Required result |
|---|---|
| CPF package check | PASS |
| Focused DSCP-T11 vitest | PASS, 4/4 |
| Reviewer-fast gate | PASS |
| GC-051 registry coverage | PASS |
| Forbidden paths | none modified |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_FOR_CLAUDE_2026-06-10.md` | `Status: DISPATCHED` before closure | READY |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_COMPLETION_2026-06-10.md` | reviewer-authored after worker return | PENDING |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_ROADMAP_2026-06-10.md` | `Status: DISPATCHED` before closure | READY |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | DSCP-T11 test path covered | PENDING |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | DSCP-T11 quick lookup row | PENDING |
| Session continuity | active handoff and state registry | reviewer sync after closure | PENDING |

## Claim Boundary

This baseline authorizes only a local deterministic CPF test harness. It does
not claim provider behavior, live governance proof, retrieval quality, semantic
correctness, corpus ingestion, OCR, vector search, PolicyLocal T12 readiness,
current-law status, legal advice quality, public readiness, hosted readiness,
production readiness, public-sync, memory reinjection, high-risk promotion,
Learning Orchestrator runtime behavior, or autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; not public-synced.

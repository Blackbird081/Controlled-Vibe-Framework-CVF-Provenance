# CVF MKG2 Deferred Runtime Candidate Triage Roadmap

Memory class: FULL_RECORD

Status: REVIEW_READY

docType: roadmap

Date: 2026-06-01

## Purpose

Turn MKG1 deferred runtime/bridge/skill candidates into a clean planning lane
without reopening MKG1 or letting a worker improvise runtime scope.

## Authorization / Decision

Decision: operator dispatched the successor tranche on 2026-06-01 for bounded
documentation-only triage.

Authority:

- `docs/baselines/CVF_GC018_MKG2_DEFERRED_RUNTIME_CANDIDATE_TRIAGE_2026-06-01.md`
- `docs/reviews/CVF_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_COMPLETION_2026-06-01.md`
- `docs/audits/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_MANIFEST_2026-06-01.json`

## Scope

In scope:

- enumerate and classify the `21` MKG1 deferred assets;
- separate Cortex bridge/runtime, governed skill evolution, and graph
  implementation planning candidates;
- prepare source-verified future work packets;
- preserve doc-only boundary until a later explicit dispatch.

Out of scope:

- runtime source edits;
- live/provider proof;
- graph retrieval execution;
- Memory reinjection;
- skill mutation;
- public-sync or push.

## Non-Goals

- no implementation;
- no public readiness claim;
- no hosted or production readiness claim;
- no autonomous mutation;
- no use of Legacy source-family names as CVF owners.

## Work Plan

| Step | Requirement | Output | Status |
| --- | --- | --- | --- |
| M2.1 | Re-enumerate the 21 MKG1 deferred rows | deferred-candidate ledger | REVIEW_READY |
| M2.2 | Source-verify current runtime/graph/skill owners | Source Verification Block | REVIEW_READY |
| M2.3 | Split candidates into future roadmaps | candidate routing matrix | REVIEW_READY |
| M2.4 | Apply Worker Autonomy prompt standard | dispatch prompt block | REVIEW_READY |
| M2.5 | Run dispatch-quality and corpus guards | gate receipts | REVIEW_READY |

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Manifest backing | future packet cites manifest JSON and hash |
| Deferred asset count | `21/21` assets accounted for |
| Owner verification | no runtime owner claim without current source citation |
| Runtime boundary | no code/live/provider work in MKG2 planning |
| Worker autonomy | work order includes No-Question Rule before dispatch |

## Verification / Evidence

Required before dispatch:

```powershell
python scripts/build_legacy_rescan_c_manifest.py --check-only --expected-manifest-hash ae7fe05e016b7079a81002de60de1e1209112de59c8bee793e15e11557cae0ff
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
```

## Roadmap-To-Work-Order Trace

Draft work order:

`docs/work_orders/CVF_WO_MKG2_DEFERRED_RUNTIME_CANDIDATE_TRIAGE_2026-06-01.md`

Dispatch is active under the bounded MKG2 work order.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private dispatched roadmap only. No public-sync remote, public repository
commit, or public artifact path is included.

## Claim Boundary

MKG2 is a review-ready planning roadmap. It does not authorize implementation,
live proof, public-sync, provider use, runtime behavior, graph retrieval,
Memory reinjection, skill mutation, hosted readiness, production readiness, or
public readiness.

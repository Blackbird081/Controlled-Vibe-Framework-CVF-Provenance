# CVF CI2 Corpus Intelligence Enforcement And Product Readiness Roadmap

Memory class: FULL_RECORD

Status: T1_T2_CLOSED_T3_DISPATCH_READY

docType: roadmap

Date: 2026-06-02

GC-018: `docs/baselines/CVF_GC018_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_2026-06-02.md`

dispatchBaseHead: `73079521`

## Purpose

CI2 converts the completed CI1 corpus-intelligence chain and CSA1 standards
into an enforceable product-readiness path. The roadmap exists because LPCI
should not begin as a chatbot/UI exercise; it should begin only after corpus
inputs have deterministic hash, path, disposition, and index behavior.

## Authorization / Decision

Authorized by operator instruction on 2026-06-02 and
`docs/baselines/CVF_GC018_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_2026-06-02.md`.

Decision: dispatch CI2 as five ordered tranches. Do not begin LPCI runtime work
inside CI2.

## Scope / Target / Owner Boundary

Target: CVF corpus-intelligence governance and product-readiness intake.

Owner surface: CVF governance/control-plane documentation, structural checkers,
and machine-readable corpus-intelligence artifacts.

Corpus owners remain responsible for source truth, domain review, semantic
correctness, legal correctness, and currentness.

## Scope

In scope: NR-04 standard, NR-04/NR-05/NR-11 structural checkers, enforced index
model, pilot product-readiness pack, and LPCI product roadmap packet.

Out of scope: LPCI implementation, live proof, provider calls, embeddings,
vector store, UI/API work, public-sync, or new corpus scan without GC-051.

## Non-Goals

- do not implement LPCI chatbot runtime;
- do not answer legal/policy questions;
- do not create or populate a production retrieval index;
- do not claim semantic, legal, hosted, production, or public readiness;
- do not scan new corpora without explicit registration and work order scope.

## Current Runtime Freshness Verification

N/A with reason: CI2 dispatch artifacts make no current runtime behavior claim.
They state that LPCI runtime is outside scope and remains blocked until a
separate product roadmap authorizes implementation.

## Current State

| Layer | Evidence | State |
| --- | --- | --- |
| CI1 operational chain | `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | T1-T7 closed |
| NR-05 path standard | `docs/reference/CVF_CORPUS_PATH_NORMALIZATION_ALGORITHM_STANDARD_2026-06-02.md` | authored |
| NR-11 disposition merge rule | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | authored |
| NR-04 source hash standard | `docs/reference/CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md` | authored — CI2-T1 CLOSED_PASS_BOUNDED |
| NR-04/NR-05/NR-11 checkers | `docs/reviews/CVF_CI2_T2_PACKET_NORMALIZATION_CHECKERS_COMPLETION_2026-06-02.md` | implemented — CI2-T2 CLOSED_PASS_BOUNDED |
| LPCI product runtime | blocked by CI1-T7 | not authorized |

## Tranche Plan

| Tranche | Goal | Primary output | Status |
| --- | --- | --- | --- |
| CI2-T1 | NR-04 Source Hash Standard | `docs/reference/CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md` + readiness-template update | CLOSED_PASS_BOUNDED |
| CI2-T2 | Packet Normalization Checkers | checker scripts/tests for NR-04, NR-05, NR-11 + hook/autorun integration | CLOSED_PASS_BOUNDED |
| CI2-T3 | Enforced Cross-Corpus Index Model | versioned enforced index schema/model | DISPATCH_READY |
| CI2-T4 | Product Readiness Pilot Corpus Pack | pilot pack proving enforced fields can be consumed | HOLD_UNTIL_T3_PASS |
| CI2-T5 | LPCI Product Roadmap Packet | LPCI GC-018 + MVP roadmap proposal, no implementation | HOLD_UNTIL_T4_PASS |

## Dependency Lock

CI2 must run in order:

1. CI2-T1 closes the written NR-04 standard.
2. CI2-T2 implements machine checks only after the NR-04 standard exists and
   the CSA1 NR-05/NR-11 standards are cited.
3. CI2-T3 builds the enforced index model only after the checker behavior is
   known.
4. CI2-T4 creates a pilot product-readiness pack only after the enforced model
   exists.
5. CI2-T5 drafts the LPCI product packet only after T4 demonstrates product
   intake shape.

No worker may merge tranches or "continue ahead" to a later tranche in the same
work order.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order |
| --- | --- |
| Author source-hash standard before checker | `CVF_WO_CI2_T1_SOURCE_HASH_STANDARD_2026-06-02.md` |
| Implement structural enforcement | `CVF_WO_CI2_T2_PACKET_NORMALIZATION_CHECKERS_2026-06-02.md` |
| Normalize enforced index output | `CVF_WO_CI2_T3_ENFORCED_CROSS_CORPUS_INDEX_MODEL_2026-06-02.md` |
| Prove product-readiness packet | `CVF_WO_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK_2026-06-02.md` |
| Prepare LPCI product roadmap | `CVF_WO_CI2_T5_LPCI_PRODUCT_ROADMAP_PACKET_2026-06-02.md` |

## Work Plan

| Step | Requirement | Output | Status |
| --- | --- | --- | --- |
| C2.1 | Author NR-04 source hash standard | reference doc + template update | CLOSED_PASS_BOUNDED |
| C2.2 | Implement packet normalization checkers | scripts/tests/hook integration | CLOSED_PASS_BOUNDED |
| C2.3 | Publish enforced index model | JSON model + schema reference | DISPATCH_READY |
| C2.4 | Build pilot product-readiness pack | pilot JSON + reference explanation | HOLD_UNTIL_T3_PASS |
| C2.5 | Draft LPCI product roadmap packet | GC-018 + roadmap + future T1 WO | HOLD_UNTIL_T4_PASS |

## Acceptance Criteria

- CI2-T1 closes NR-04 written standard before checker implementation.
- CI2-T2 checkers pass tests and are integrated into governance gates.
- CI2-T3 produces a valid machine-readable enforced index model.
- CI2-T4 produces a pilot pack without inventing corpus evidence.
- CI2-T5 produces product roadmap artifacts only, with no runtime code.

## Verification / Evidence

CI2 dispatch verification:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base 65a0620f --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 65a0620f --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 65a0620f --head HEAD
```

CI2-T3 dispatch refresh verification uses the post-T2 head:

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 73079521 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 73079521 --head HEAD
```

## Gates

Every CI2 tranche must run:

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <baseHead> --head HEAD
git diff --check
git status --short
```

CI2-T2 additionally ran relevant unit tests and the local hook chain because it
edited governance checkers. CI2-T3 is doc/JSON model work and must not edit
checker code.

## Claim Boundary

CI2 provides standards, structural enforcement, index model, pilot pack, and
LPCI roadmap proposal. It does not implement LPCI runtime, prove legal answer
truth, run provider/live calls, build embeddings/vector stores, or claim public
readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: CI2 roadmap references internal GC-018 baselines, work order paths,
and CI1 corpus intelligence chain artifacts that are not public-sync exported.
Public-sync boundary: no CI2 artifact may be copied to the public-sync repo
until a separate public-sync authorization is obtained per the CVF public-sync
rule.

# CVF ERH Planning Review Codex Response

Memory class: FULL_RECORD

Status: DRAFT_REVIEW_RESPONSE

docType: review

Date: 2026-06-04

baseHead: `b5cf8882`

## Purpose

Answer the ERH planning review questions so a later agent can author the formal
ERH roadmap and work orders without guessing Codex's position.

## Target / Source

Target review:

`docs/assessments/CVF_ERH_PLANNING_REVIEW_FOR_CODEX_2026-06-04.md`

Source intake:

`docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md`

## Scope / Methodology

This response answers the seven Codex questions in the ERH planning review.
Method: read the target review, archived intake, current structural checker,
work-order quality checker, corpus registry standard, corpus registry state,
and relevant gate outputs. No runtime source, public-sync clone, provider call,
or live proof was modified or executed.

## Findings / Position

| Question | Codex response | Disposition |
| --- | --- | --- |
| B1 structural blocker | Operator clarified on 2026-06-04 that ERH is about public GitHub structure, README/catalog boundaries, and external-agent evaluation. If usage samples appear on a landing page, they are mock data for non-coder orientation only, not governance evidence. Do not ask for PASS and do not add an ad hoc checker suppression. Treat the file as retired local scratch/out-of-scope; if it ever enters a changed range, archive or bound it as `RETIRED_NOT_GITHUB_PUBLIC_EVIDENCE` with no public evidence claim. | OPERATOR_DECIDED_RETIRE |
| B2 registry blocker | Current registry check passes: `check_corpus_scan_registry.py --base b5cf8882 --head HEAD --enforce` reports 11 corpora and 0 violations. This appears resolved for `GOVERNANCE_PILOT_NO_LEGAL_CORPUS`; no broader same-field violation is currently detected. | RESOLVED_CURRENT |
| ERH-T1 split | Split public claim calibration into two parts: T1a private public-claim calibration packet; T1b public-sync README/catalog execution. ERH-F11 evaluation guide can live inside T1a as a section, but public execution must be separate because public-sync is a different repository boundary. | REFINE |
| ERH-T2 split | Split T2a route ledger and T2b CI hardening. Route ledger is read-only evidence analysis; CI workflow edits are higher risk and should not be bundled with ledger classification. | ACCEPT_SPLIT |
| ERH-T3 policySnapshotId | Docs-only is correct for this batch per operator decision. A minimal runtime fix such as persisted policy hash changes receipt semantics and should be a separate GC-018/runtime work order. | ACCEPT_DOCS_ONLY |
| ERH-T4 timing | Hold until T3 closes. The beta dependency decision depends on the documented production/posture boundary. It can be drafted earlier but should not close before T3. | HOLD_AFTER_T3 |
| Dangling links in intake | Yes. Because the 2026-06-03 roadmap/work-order paths are absent from the current worktree and the intake is archived, future ERH planning should either author fresh paths or mark the old links as `PENDING_AUTHORING` in a successor intake/addendum. Do not edit the archive casually unless the assigned task is archive correction. | ACCEPT |

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Treating docs-only claim calibration as runtime hardening | Keep ERH-T3 docs-only and open separate runtime work orders for policy versioning, durable store defaults, distributed rate limit, or signing/hash-chain implementation. |
| Public/provenance boundary breach | ERH public README/catalog work must be a public-sync work order executed from `Controlled-Vibe-Framework-CVF-public-sync`. |
| Route coverage overclaim | ERH-T2a must classify every API route and must not treat lexical hits as semantic governance proof. |
| Structural checker failure on this review | Add missing GC-045 sections to the review file before dispatch or commit. |

## Decision / Recommendation / Disposition

Recommended ERH sequence:

1. Clear/verify blockers: record B1 retired/out-of-scope and verify B2 registry pass.
2. ERH-T1a private public-claim calibration packet.
3. ERH-T2a route governance coverage ledger.
4. ERH-T3 evidence durability claim-boundary packet.
5. ERH-T2b CI hardening plan/work order.
6. ERH-T4 beta dependency decision after T3.
7. ERH-T1b public-sync README/catalog execution after private decisions are source-backed.

Recommendation: do not dispatch a formal ERH implementation tranche until a
fresh roadmap and work order are authored from this response. The archived
2026-06-03 intake is useful evidence, but its roadmap/work-order links are not
current live execution packets.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| ERH planning links point to absent current roadmap/work-order paths | DOCUMENTATION_GAP | DOCUMENTATION_ONLY_LEARNING | TEMPLATE_UPDATED_CANDIDATE | Future ERH roadmap must use fresh paths or `PENDING_AUTHORING` placeholders |
| B1 usage sample is not GitHub public evidence | OPERATOR_SCOPE_CLARITY_GAP | DOCUMENTATION_ONLY_LEARNING | OPERATOR_DECIDED | Landing-page mock content is allowed only as non-coder orientation; ERH remains focused on GitHub public structure and external-agent evaluation |
| ERH-T2 mixed read-only ledger with possible CI workflow edits | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | ROADMAP_REQUIRED | Split route ledger and CI hardening into separate tranches |
| Runtime-adjacent issues are intentionally docs-only in this response | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | No runtime/provider/cost proof is claimed; future runtime changes require separate GC-018/work order |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance response only. No public-sync remote, public commit,
or public artifact path evidence is included.

Next action: create a separate public-sync work order only after ERH private
claim calibration is source-backed.

## Claim Boundary

This response answers planning questions only. It does not implement ERH,
resolve public README/catalog content, run live governance proof, modify
runtime behavior, or close any external-review hardening finding.

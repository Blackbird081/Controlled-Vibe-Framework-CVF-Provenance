# CVF Customer Care seven-finding learning: per-output delivery truth

Memory class: governed-project-learning
Status: ACTIVE_REFERENCE
docType: reference
Date: 2026-10-13
parentFindingId: CCMA-OUTPUT-DELIVERY-TRUTH-20261013

## Purpose And Decision Boundary

Local reconciled the seven selected Customer-Care-Monitor runtime fixes at project revision `cdf5537e10c7a285f0f08d51753a749eac75abb8` with the private CVF Core at `b3d19eb36940848161ecc651d8961f5bcad42283`. This is a bounded source/review comparison and parent written-guidance update. It does not reopen the project fixes, assert whole-project coverage, run a provider or alter CVF runtime. Later project return and public documentation export are recorded separately below.

The reusable addition is a per-output delivery evidence contract: admission/claim, remote acceptance, durable outcome and result marker are separate facts. A caller may retry only an output proven failed; transport uncertainty or a failed outcome write must remain unresolved until reconciliation. An aggregate send status cannot substitute for the identity and persisted state of each output.

## Scope / Applies To

Applies to selected Core learning intake and to reviews of jobs that send to
multiple external outputs. It is a companion evidence guide under the existing
downstream profile owner. The prior hash-bound Build Learning Evidence Checklist
is left intact; this record and the new companion do not revise its historical
typed proof.

## Source Confidence And Scope

Source project remote: `https://github.com/CVF-Ecosystem/Customer-Care-Monitor.git`; branch `codex/cvf-portable-inheritance`. The current project HEAD and remote were read at the named revision; local worktree was clean. Selected raw file hashes and source/review locators are pinned in `docs/reviews/evidence/ccma-seven-finding-learning-source-20261013.json`. The three final Local review documents report bounded accepted source/tests; their historical execution results are ATTRIBUTED_SOURCE here. Local inspected selected current source regions for Messages lifetime and notification dispatch/transport, but did not rerun project tests, SMTP, browser, provider or MySQL. The manifest is a selected evidence set, not a complete repository scan.

## Five Parent Value Checks

| Check | Decision and evidence | Limit |
|---|---|---|
| Source confidence | The project revision, three final reviews and selected source paths have exact raw SHA-256 in the source manifest; observed Core owner text is read locally. | Project test counts/old-source kills remain attributed to the reviewers; no independent replay in Core. |
| Reusable mechanism | One logical job can dispatch to several outputs; acceptance and persistence can diverge per output. Unknown SMTP DATA or response/DB failure makes automatic replay unsafe. | The examples prove the need for a distinction, not exactly-once delivery or a general transport library. |
| Existing coverage | `CVF_BUILD_LEARNING_EVIDENCE_CHECKLIST.md` already separates returned outcome, stored status, terminal summary and checkpoint; provider-attempt and CAS owners cover adjacent concerns. | Existing terminal-write guidance does not explicitly ask for per-output remote acceptance, unknown versus proven failure, or retry eligibility by output identity. |
| Incremental value | Add a companion per-output checklist under the existing owner so reviewers can reject aggregate "sent" proof for mixed/uncertain attempts. | Written guidance only; prior hash-bound checklist remains unchanged, with no new mandatory phase or runtime behavior. |
| Bounded proof | R091 review binds explicit accepted/rejected/unknown transport cases, mixed output/reentry, persistence-failure and no second-send observations to retained project proof; the companion asks positive and negative review questions. | Core consumes the project review and source; no Core-run reproduction, live SMTP or delivery guarantee. |

## Seven-Finding Dedup And Routing

| CCMA finding | Parent route | Parent disposition |
|---|---|---|
| F01 reset target hierarchy | Actor and target authorization must be checked against current source state; existing permission/role owners apply. | `RULE_EXISTS`  -  project-specific hierarchy and MySQL locking stay in CCMA. |
| F02 dashboard and notification projection | Permission on returned payload as well as registered route; existing authority/claim owners apply. | `RULE_EXISTS`  -  no new universal permission matrix. |
| F03 refresh version race | One conditional state transition and checked affected count before emitting a successor; existing CAS/continuity owners apply. | `RULE_EXISTS`  -  no authentication library export. |
| F04 outbound per-output truth | Distinguish captured output identity, claim, remote acceptance/unknown/failure, durable outcome, marker and retry. | `TEMPLATE_UPDATED`  -  companion checklist under the existing evidence owner. |
| F05 SMTP cancellation | Bound blocking transport and retain owner until tail effect returns; existing deadline/cancellation principles apply. | `RULE_EXISTS`  -  no generic SMTP implementation claim. |
| F06 async selection lifetime | Response commits only for current tenant, selection intent and component lifetime, including A-B-A; existing run isolation/continuation principle applies. | `RULE_EXISTS`  -  CCMA UI implementation is an illustrative source case, not a new Core UI gate. |
| F07 batch bookkeeping/backoff | Error, parse/save failure and success share progress/accounting/backoff; cancellation bounds wait; existing attempt/terminal evidence owners apply. | `RULE_EXISTS`  -  no global retry policy inferred. |

These dispositions concern reusable Core controls, not whether the project fixes passed. The project reviews separately accept all seven within synthetic/local MySQL/loopback/UI limits. The Core comparison selects one incremental written control and does not infer that every application uses the same runtime topology.

## Selected Proof Questions For The Companion Checklist

Positive evidence packet: output A has a stable identity, explicit remote acceptance, committed receipt and marker; output B has a distinct identity and proven failure. A reentry skips A and may retry B within the declared policy. Review each output separately, including the resulting durable rows and affected counts.

Negative evidence packet: two send attempts return one ambiguous SMTP DATA result, while the aggregate job says "sent" or a failed receipt write leaves a sending row. The aggregate and the call return cannot prove delivery or safe retry for that output. Record UNKNOWN/reconciliation required; neither a blanket success marker nor an automatic second send is supported.

These are review oracles derived from selected source/review evidence, not newly executed Core runtime tests. The linked project tests reportedly cover these contrasts in disposable local fixtures; no independent Core rerun is claimed.

## Project Action And Feedback States

| Boundary | State | Evidence / next action |
|---|---|---|
| Project finding/action | RESOLVED_BOUNDED | R088/R090/R091 final reviews and project source at pinned revision; full product stage exits remain open. |
| Parent value decision | MERGE | One per-output companion under the existing Build Learning Evidence Checklist owner; six routes deduplicated as `RULE_EXISTS`. |
| Parent implementation | IMPLEMENTED_BOUNDED | Written companion checklist only after the selected changed-set and F2G gates pass. |
| Return delivery | RETURNED | Project record at `9ae219c67c7bf258c095a2acd76e969345110753`, remote branch readback and typed delivery receipt in `docs/reviews/evidence/ccma-seven-finding-delivery-receipt-20261013.json`. |
| Source-project application of parent control | APPLIED_BOUNDED_DOCUMENTATION_ONLY | Project learning record copies the guidance for future reviews; typed application receipt is `docs/reviews/evidence/ccma-seven-finding-application-receipt-20261013.json`. R091 code fixes predate this checklist. |

The later operator request authorized Local to return the guidance to the project and prepare a public-safe documentation export. Existing Facebook/Zalo OA checkpoints and product release limits are unchanged.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| F04 per-output acceptance versus durable marker | `RUNTIME_SIGNAL_GAP` | `GOVERNANCE_CONTROL_PLANE` | `TEMPLATE_UPDATED` | Use the companion checklist to demand identity-specific accepted/failed/unknown and persisted-state evidence before retry/closure claims. | Handled as bounded written guidance; no runtime gate. |
| F01/F02/F03/F05/F06/F07 existing mechanisms | `WORKER_EXECUTION_ERROR` at the source-project defect boundary; no demonstrated Core rule gap | `GOVERNANCE_CONTROL_PLANE` | `RULE_EXISTS` | Keep the existing permission, CAS, deadline, run-lifetime and attempt owners; reuse these examples only when a selected task needs them. | Parent dedup handled; product implementation remains CCMA-owned. |

Runtime/provider/cost learning: `N/A_WITH_REASON` for a new Learning Plane model or pricing signal. This intake contains no new provider response distribution, cost measurement, calibration or live customer data.

## Epistemic Process Block

Expected Result / Prediction: the recent seven fixes would mostly match existing Core owners, with one actionable evidence-guidance delta. Evidence Comparison: selected project reviews/source show per-output unknown and durable failure cases; the prior parent checklist covers terminal persistence but not this full output identity/retry matrix. Contradiction Or Gap Disposition: historical project tests are attributed and not rerun; unresolved real SMTP/browser/deployment layers remain open. Claim Update: a companion under the existing checklist owner adds one written review contract, not a new runtime safeguard or public product claim.

## Project Source Comparison Boundary

`PROJECT_TO_PARENT_COMPARISON`: the already available CVF-governed sibling
project is read at a pinned Git revision for selected use-case evidence. The
Project Learning Loop and F2G owners control this intake. The manifest records
exact selected paths, read depth and exclusions; the seven-finding ledger is
the bounded task boundary, not a claim that every project file was read.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/parent_learning_evidence.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `parentFindingId`; `TEMPLATE_UPDATED`; `RULE_EXISTS`; `RUNTIME_SIGNAL_GAP`; `GOVERNANCE_CONTROL_PLANE`; `control:`; `proof-positive:`; `proof-negative:`; `PROJECT_TO_PARENT_COMPARISON` |
| gateRunPurpose | Confirm the pre-read source pins, five value checks, typed parent lifecycle, exact changed paths and document structure; gates confirm prepared evidence rather than discover the finding. |
| claimBoundary | Passing static gates alone cannot establish agent comprehension, outbound exactly-once delivery or live provider behavior; documentary project adoption is separately evidenced by the typed loopback receipts. |

## Public Export Disposition

EXPORTED

Public-sync remote: `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`
Public-sync commit: `fa34ed49e56648acafe8b0388e48e0aa0523f007` (PR #11 squash merge; `origin/main` readback).
Public artifact paths: `docs/reference/downstream_gate_profile/CVF_PER_OUTPUT_DELIVERY_EVIDENCE_CHECKLIST.md`; `docs/reference/downstream_gate_profile/CVF_BUILD_LEARNING_EVIDENCE_CHECKLIST.md`.
Public checklist Git-blob SHA-256: `8b79097d726f9ba274a7a0be0f93e3e59c7723f4cb6703a128048cd6bf9d1baf` at the merged commit.
Public catalog paths: N/A with reason - the public change is a reference checklist and discoverability link, not a catalog entry.
Export scope: public-safe written guidance only. The private learning record, source manifest, typed loopback receipts and historical project evidence were not exported; CCMA retains its older pinned public Core and its own portable guidance copy.

## Claim Boundary

This record is a finite selected-use-case intake. It neither changes Customer Care code nor asserts that CVF governed its AI runtime. The parent companion, project documentation return and public-safe checklist are independently evidenced; no real SMTP, customer-delivery or runtime-governance proof follows.

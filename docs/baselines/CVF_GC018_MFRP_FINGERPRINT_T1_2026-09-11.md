# CVF GC-018 - Committed Evidence Fingerprint Contract

Memory class: governed-dispatch-baseline
docType: baseline
Status: CLOSED_PASS_BOUNDED
Date: 2026-09-11
Batch ID: MFRP-FINGERPRINT-T1
dispatchBaseHead: a6823f497
Commit mode: WORKER_MUST_NOT_COMMIT
Decision owner: operator explicit yes, 2026-09-11
Reviewer owner: Local reviewer/closer
Worker target: operator-selected internal VS Code worker

## Purpose

Authorize the fingerprint repair in docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_FINGERPRINT_T1_2026-09-11.md, with exactly eleven worker paths and independent review.

## Decision / Baseline

Preserve raw worktree/cache identity; add an integrity-covered committed Git-blob identity, strict compatibility and fail-closed collector handling. Full contract, complete hostile matrix and planned helper split are in the paired work order. No implementation has been performed.

## Current Runtime Freshness Verification

At a6823f497 the producer reads disk bytes and collector reads committed blobs; the additive binding remains proposed. See Source Verification Block for exact owner symbols. No runtime behavior or absence assessment beyond these deterministic source observations.

## Scope / Target / Owner Boundary

Ten worker paths named by the work order; same-workspace internal execution, no worker commit. Dispatcher owns only these two packets and separate continuity. No registry or hook/config edits.

## Acceptance Criteria

Canonical producer/validator/collector integration passes CRLF/LF, binary, dirty-state, malformed binding, legacy receipt and exact-range adversarial tests. Keep old measurements rejected and preserve raw-byte cache invalidation.

## Evidence / Verification

### Verified diagnostic

Attempt ATTEMPT-a4ec8bfaa9c112ca compared trusted material 3de0ba07ce213ce2e6fb5668b5d41f6fb663fab1 with disclosure a6823f497a2746ca496dbc196483baff14689850.
Read-only recomputation over the nine material paths produced:
- worktree bytes SHA-256: f3d5a50582a5bc594a79a66676a2e0b13e2520777a3c337c96dd1af1df197f54
- Git blob bytes SHA-256: 57ba3abdca179495fd537421a880e810b28a0ff95430e25dc76958259807fc26
- six raw differences; all nine match after CRLF-to-LF conversion; core.autocrlf=true.

This establishes representation mismatch for this named range only. Normalizing text is diagnostic, not the authorized hashing repair. The reviewer rejected the measurement, preserved the pending journal, and recoverably archived the marker as .cvf/runtime/mfrp-p4-shadow-canary/ADJUDICATED_REJECTED_OBSERVATION_2026-09-11_TPGR.json with SHA-256 56d22b53dc9587d4916c0b9a235b339d432ad80f9315b4250d5a02f7d3d8db98. No sample was promoted. Ignored runtime evidence is supporting diagnostic input only; current source and this operator-authorized packet control. This dispatch neither claims a permanent fix nor permits automatic marker deletion.


## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Producer fingerprints mutable disk bytes | LOCAL_SOURCE | governance/compat/run_agent_autorun_workflow_gate.py | fingerprint and receipt context | _worktree_fingerprint | P2 receipt producer | ACCEPT |
| Collector independently fingerprints committed blobs | LOCAL_SOURCE | governance/compat/mfrp_shadow_canary_autocollect.py | committed reconstruction | _reconstruct_fingerprint_from_commit | P4 collector | ACCEPT |
| Mismatch creates fail-closed marker | LOCAL_SOURCE | governance/compat/mfrp_shadow_canary_autocollect.py | receipt reconciliation | UNSAFE_FINGERPRINT_MISMATCH | P4 safety | ACCEPT |
| Digest and strict envelope owned centrally | LOCAL_SOURCE | governance/compat/agent_autorun_machine_verification.py | builder and validator | _validate_receipt_integrity | v3 canonical owner | ACCEPT |
| Readout delegates validation and retains raw changed-path identity | LOCAL_SOURCE | governance/compat/agent_automation_machine_verification_readout.py | read and build | read_receipt_readonly | AAF consumer | ACCEPT |
| Producer tests cover raw-byte drift | LOCAL_TEST | governance/compat/test_run_agent_autorun_workflow_gate.py | fingerprint regression | test_worktree_fingerprint_changes_with_file_content | cache tests | ACCEPT |
| Receipt tests preserve legacy rejection | LOCAL_TEST | governance/compat/test_agent_autorun_machine_verification.py | compatibility | test_unknown_schema_fails_closed | validator tests | ACCEPT |


## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_agent_handoff_boundary.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_task_governance_route.py; governance/compat/check_semantic_convergence_control.py; governance/compat/check_worker_return_quality_gate.py; governance/compat/check_review_cost_control.py |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; WORKER_MUST_NOT_COMMIT; closeabilityContractVersion; Self-declared worker-return artifact; Required Artifact Manifest |
| gateRunPurpose | confirm source-verified bounded dispatch and ownership, not discover implementation semantics |
| claimBoundary | dispatch evidence only; no implemented repair claim |


## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-FINGERPRINT-T1 --title "Committed Evidence Fingerprint Contract" --date 2026-09-11 --base a6823f497 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface INTERNAL_AGENT --stdout |
| generatedProfile | protected-governance-path; internal no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Reused governed role/closeability envelope, added separate immutable identity contract, exact eleven-path manifest and hostile proof matrix |
| checkerReadAheadConfirmation | sources named in Checker Source Read-Ahead Block read for field/enum requirements |
| docOnlyNewFields | committedEvidence proposed additive profile, not current machine behavior |
| claimBoundary | dispatch authoring only |


## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance-machine-hardening`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Resolver command: python governance/compat/run_adif_defect_resolver.py --task-class governance-machine-hardening --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling MEDIUM --json
Returned defect count: 0. Returned defects: NONE_RETURNED. Disclosed defectIds: none. Dispatch impact: no matching active resolver item; explicit contract and guard obligations remain.


## Core Guard Self-Protection Authorization

Operator authorization: explicit yes on 2026-09-11 to dispatch internal worker repair of the fingerprint contract and regression tests before any pilot.

Authorized guard-maintenance scope: only the eleven worker targets below; preserve raw cache invalidation, receipt integrity, full gate selection and P4 safety. Worker copies this block into its return. No hook/catalog/registry/config edits.

Protected worker paths:
- governance/compat/run_agent_autorun_workflow_gate.py
- governance/compat/agent_autorun_machine_verification.py
- governance/compat/mfrp_shadow_canary_autocollect.py
- governance/compat/committed_evidence_fingerprint.py
- governance/compat/test_run_agent_autorun_workflow_gate.py
- governance/compat/test_agent_autorun_machine_verification.py
- governance/compat/test_mfrp_shadow_canary_autocollect.py
- governance/compat/test_committed_evidence_fingerprint.py

Rollback boundary: only newly introduced fingerprint binding behavior and associated tests/reference. Never rewrite old receipts or journals, clear safety markers automatically, normalize the checkout, amend history, or restore unrelated work.


## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | P2 producer/validator, P4 collector | deterministic evidence only, no worker commit | source/test matrix | existing internal Python consumers | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | no new external consumer | no research or external invocation | operator authorization internal only | adapter absent and not authorized | N/A_WITH_REASON |


## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_FINGERPRINT_T1_2026-09-11.md | Status: CLOSED_PASS_BOUNDED | PASS |
| Completion or reviewer artifact | docs/reviews/CVF_MFRP_FINGERPRINT_T1_COMPLETION_2026-09-11.md | REVIEWER_ACCEPTED_BOUNDED | PASS |
| Roadmap state | standalone work order; no dedicated roadmap transition | no roadmap advancement | N/A with reason: standalone repair |
| Registry JSON | docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json | two reviewed source hashes; freshness CURRENT | PASS |
| Registry Markdown | docs/reference/review_cost_control/CVF_COMMITTED_EVIDENCE_FINGERPRINT_CONTRACT.md | implemented bounded profile, no corpus registry change | PASS |
| External evidence digest | completion Internal Cross-Check Evidence Digest | f92dd77d8b9c0e7fbe871e005e64a64585f5f56c8c597dbf0ec16ce2863f15e8; reported evidence only | PASS |
| System loop interlock | committedEvidence producer/validator/collector | legacy ineligible; unsafe declarations rejected; no sample promotion | PASS |
| Session continuity | CVF_SESSION_MEMORY.md; AGENT_HANDOFF_V60_2026-09-08.md | dedicated post-material continuity owned by Local closer | PASS - separate commit required |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| historical-drift | docs/reviews/CVF_MFRP_FINGERPRINT_T1_WORKER_RETURN_2026-09-11.md | committedEvidence | absent on semantic drift | absent in focused chain regression | PASS |
| malformed-binding | docs/reviews/CVF_MFRP_FINGERPRINT_T1_WORKER_RETURN_2026-09-11.md | committedEvidence | reject null/one-sided | focused validator/collector regressions pass | PASS |

These are recorded test assertions, not durable production runtime receipts.
No full release/provider proof or historical observation upgrade is claimed.

## Claim Boundary

Internal deterministic evidence-contract maintenance only. No runtime/governance-provider proof, pilot execution, absorption acceptance, public or deployment claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: internal repair and independent review only.

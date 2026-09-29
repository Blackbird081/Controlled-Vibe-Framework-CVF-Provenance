# ACEL G1 T3D C1-R2 Local Review

Memory class: governed-local-review

docType: review

Date: 2026-09-23

Status: REVIEWER_ACCEPTED_BOUNDED_CLOSURE_PENDING

## Purpose

Evaluate the returned five-path implementation, repair the orchestrator-owned manifest, and independently probe named safety contradictions. This review records the bounded terminal acceptance decision after three correction rounds.

## Target / Source

- Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_CORRECTION_2026-09-23.md`.
- Contract: `docs/audits/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md`.
- Return: `docs/reviews/CVF_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_WORKER_RETURN_2026-09-23.md`.
- Execution HEAD: `8537cdedb002323ee767313835811e4262ab2021`.
- Final return SHA256: `B263BFF7319EBA7BAA395C8BB3577B5B4BEE7B497CB992CC8C7709A078FA6C0D`.

Reviewed implementation SHA256 bindings (rechecked unchanged after review):

| Script | SHA256 |
|---|---|
| acel_g1_party_c_group4_registry_writer.ps1 | DF596D1E1F57D02FBE65C369506A325038B344DD95201F930DD0EDBE27781513 |
| acel_g1_party_b_group4_lookup_response_writer.ps1 | 49C8321B46CC1C0B409F29349D1D9145EADB360D035DCFA6FAABE951C03C1678 |
| acel_g1_group4_admin_recovery.ps1 | FFB359AD078783F64802EB29582F363066C38B5B5D6EA69FF6D8F34ED955C480 |
| acel_g1_group4_disposable_acl_probe.ps1 | 15D92E5C6E14AD3E2AF8B8D29FC759B233D64B90138EE7C58E6A6CE12953D0ED |

## Scope / Methodology

Local reviewer evaluated returned evidence and ran targeted counterexamples, not the full implementation suite again. The reason for rerun was missing reservation identity checks, rollback behavior and insufficient recovery ledger validation; expected information gain was whether these weaknesses produce unsafe observable effects. Ten bounded fixtures were proportionate to that risk.

Reproducible probe: `docs/reviews/evidence/cvf-acel-g1-t3d-c1-r2-local-probe-2026-09-23.ps1`. The executed copy was `.cvf/runtime/probes/g4-c1-r2-local-review.ps1`, invoked with `pwsh -NoProfile -NonInteractive -File` and the repository root argument. The probe AST-loads submitted function definitions, uses current-token TestPolicy and reviewer-owned disposable files. It does not run production entrypoints, impersonate Party B/C, or demonstrate production-principal authorization.

Fixtures were retained under `C:\Users\DELL\AppData\Local\Temp\cvf-g4-local-review-fec54a1decd34de3a2bd23178b5f1664`. Two deliberately created sentinel files were removed by the tested recovery function; no preexisting user files were targeted. Harness exit 0 means the experiment completed; its result was seven failed assertions, not a successful safety verdict.

## Findings

| Finding | Severity / owner | Evidence and corrective action |
|---|---|---|
| RV01 | Packet gap / orchestrator | Required Artifact Manifest lacked its machine-readable table; camelCase workerReturnPath did not satisfy the independent-probe checker's exact `Worker return path:` binding. Both repaired locally. Dispatch validation had been conditional on changed runtime paths, so an authoring-time PASS did not establish a usable returned-packet contract. |
| RV02 | High / worker | C `Assert-ReservedTarget` and B `Assert-ReservedZeroByte` accept hardlinked reservations; both transactions tolerate unknown siblings. Orphan-temp checks cover selected filename patterns rather than the complete permitted boundary. Enforce reservation identity/link-count and approved-boundary checks without granting additional cross-principal access. C CROSS-TARGET and B INIT-RACE test expectations also require reconciliation with the contract's identity-drift rejection. |
| RV03 | High / worker | C `Publish-RegistryTransaction` with RequireReservation and injected AfterMove failure throws but leaves the 17-byte published target. Its catch branch only removes published content when RequireReservation is false. Restore the contracted reservation state on failed publication and verify identity/security as well as content. |
| RV04 | High / worker | Recovery accepts an unverified minimal ledger and deletes its named file. A tempName containing `../` deletes a reviewer-owned sentinel outside the target directory. Validate leaf-only names, canonical containment, consistent ledger/schema/identity/security and termination evidence under the transaction guard before mutation. B creates temporary files before durable binding; ledger records lack complete prestate identity/security, and successful publication can record an empty temp name after clearing the variable. Bind before creation and preserve complete recovery evidence and verified poststate. |
| RV05 | Evidence gap / worker | The worker-owned disposable probe invokes writer selftests, and its hardlink fixture reports success without exercising writer rejection. This is not reviewer-independent negative-path proof. Return assertions that R2-01 through R2-09 are all MET are contradicted by Local results. Correct test oracles and coverage claims; add missing required return sections, rerun the required gate, then bind final evidence to the immutable final return. |

## Independent Probe Results

| Case | Required behavior satisfied | Observed result |
|---|---|---|
| c-positive | Yes | Publication succeeds; target length 17. |
| c-hardlink | No | No rejection; target length 17. |
| c-unknown-sibling | No | No rejection; target length 17. |
| c-post-replace-failure | No | ROLLBACK_INJECTED_AFTER_MOVE; target remains length 17 rather than zero. |
| b-positive | Yes | Transaction succeeds; target length zero. |
| b-hardlink | No | No rejection. |
| b-unknown-sibling | No | No rejection. |
| recovery-missing-binding-control | Yes | RECOVERY_LEDGER_BINDING_ABSENT; sentinel preserved. |
| recovery-unverified-binding | No | RECOVERY_RESIDUE_REMOVED_LEDGER_VERIFIED despite missing trustworthy binding; sentinel removed. |
| recovery-traversal-binding | No | Same reported success; sibling-directory sentinel removed through `../`. |

These are internal-primitive counterexamples, not proof that an unauthorized caller can bypass the production admin entrypoint. That limitation does not satisfy the recovery contract.

## Correction Return Review - Round 2

The returned correction resolves all seven original executable counterexamples: the reviewer reran the original ten-case probe and observed 10/10 required behaviors. That improvement is accepted as bounded evidence for RV02, RV03 and the originally sampled RV04 inputs. It does not close C1-R2 because the return itself discloses two contract requirements as open items, and source inspection found further direct contradictions.

| Finding | Severity / evidence | Required correction |
|---|---|---|
| RV06 | Critical. A new complete-looking but semantically unbound ledger row caused `Invoke-Recovery` to delete a reviewer-owned sentinel and report `RECOVERY_RESIDUE_REMOVED_LEDGER_VERIFIED`. The row used a non-contract schema, wrong targetName, invalid timestamp, no target identity, no prestate hash/security digest and no writer-termination proof. | Validate the exact schema and field semantics, targetName/path agreement, recorded phase sequence, captured target identity, expected prestate hashes/security digest, residue binding and independently confirmed writer termination. Ambiguous or missing proof must preserve the object. |
| RV07 | High. Party B creates capture/candidate temp files before its first ledger append (`Write-CopyOnWriteTransaction` lines 75-77; append path lines 92-94), contrary to R2-05. | Durably bind every recoverable temp name and required prestate before creating the temp; do not relabel a post-creation `TEMP_FLUSHED` row as precreation evidence. |
| RV08 | High. Both initialization writers clear `$temp` before constructing the `PUBLISHED` ledger row (Party C lines 418/423; Party B lines 82/83), producing an empty temp binding. This directly contradicts the worker return's `REVIEWED_NO_DEFECT_FOUND` statement. | Preserve an immutable transaction temp-name binding across all phases and assert the final ledger row is complete and phase-consistent. |
| RV09 | High. Recovery compares only target length, owner and protection flag. The return explicitly leaves content hash and complete ACE-vector poststate open, although C0-R1 and R2-05/R2-06 require exact prestate-or-complete-poststate and complete semantic security verification. | Capture and compare target bytes/hash, file identity, link count, attributes, owner, protection and complete semantic ACE vector; also verify the other target, parent and final residue inventory through the Local record boundary. |
| RV10 | Contract completeness. The tooling has no transaction-bound Local preflight authorization record or Local complete postflight corresponding to C0-R1. Writer-local checks are not a substitute. | Implement the existing contract's Local preflight/reference/postflight boundary within the permitted four-script architecture or return `BLOCKED_WITH_REASON` with the exact scope contradiction. Do not weaken the contract. |
| RV11 | Critical operability. `Assert-NoUnknownSiblings` permits only the writer's own target, so Party C rejects the required reserved `LOOKUP_RESPONSES.jsonl` and Party B rejects the required reserved `REGISTRY.json`. Both shared-parent positive probes fail with `UNKNOWN_RESIDUE_PRESENT`. | Model the exact closed two-name parent: allow both required reserved names while rejecting every other sibling. Use the Local authorization record for non-target invariance without disclosing or reading fields forbidden to the writer. |
| RV12 | High recovery-integrity defect. Round 2 fixed RV06-RV11, but recovery builds `otherBound` from raw, unvalidated rows belonging to other transaction IDs. A malformed two-field row whitelisted `unexpected.bin`; recovery removed the valid transaction's residue and returned `RECOVERY_RESIDUE_REMOVED_LEDGER_VERIFIED` while the unknown sibling remained. | Validate every ledger row before it can affect inventory policy; fully validate each other transaction before recognizing only its nonterminal bound residue. Any malformed/ambiguous other binding must block and preserve all artifacts. Final inventory must not silently treat an unvalidated name as authorized. |

Round-2 extended probe result: all 10 prior cases pass; three added contract cases fail. `c-shared-parent-positive` and `b-shared-parent-positive` reject the other required reservation, while `recovery-complete-but-unbound` deletes an unbound sentinel. Fixtures are under a reviewer-owned disposable `%TEMP%` root, use current-token TestPolicy, touch no production source and perform no Party B/C execution. The executed recovery deleted only the sentinel created for this test. Harness exit 0 means execution completed, not semantic PASS.

Correction round 2 subsequently resolved those three cases and the required gate passed. A fourteenth dependency probe then exposed RV12: 13/14 cases satisfied the required behavior; `recovery-malformed-other-binding-does-not-whitelist` failed. The primary transaction residue was removed, the unknown sibling remained, and recovery reported verified success. That result was the remaining acceptance blocker before correction round 3.

## Correction Return Review - Round 3 And Final Acceptance

The final narrow correction validates every other transaction binding before it can authorize a sibling residue. The Local reviewer reran the exact 14-case independent probe. All 14 cases satisfied their required behavior, including `recovery-malformed-other-binding-does-not-whitelist`, which now blocks on the malformed row and preserves both the valid transaction residue and the unknown sibling.

The final evidence bindings are the SHA256 values recorded above. The Local probe SHA256 is `543314F2698E9F26A86B8C4C72FF70932D05181B5BFB03FA8FA6BF80FBD81808`. This acceptance closes RV01-RV12 only for the declared hermetic current-token tooling boundary.

## Gate Evidence

After packet repair, command `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_CORRECTION_2026-09-23.md` exited 1. Independent-probe admission binding passed. Reviewer-fast reported four failing checks out of 69: semantic convergence/SCEC, operation trace, external knowledge intake and epistemic evidence. Worker-return quality selected zero eligible returns; that does not certify this return.

Command `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base c8b9a7bb459738ca7c7614dc3ba60093c42749f3 --head HEAD` exited 1 with three failures: SCEC, operation trace and external intake on the returned packet. Work-order dispatch quality passed. These runs preceded this review artifact; no claim is made that the final changed set passes all gates.

After the correction returns, the worker-return quality and independent-probe admission checks pass. The final combined worker-return fast gate exits 0; reviewer-fast reports 69/69 PASS; and `git diff --check` exits 0. The Local-owned review structural defects were repaired by the reviewer and are not attributed to the worker. Semantic acceptance is now established only for the bounded tooling claim.

## Risk / Corrective Action

Keep real Group 4 execution and downstream admission closed. Preserve the reservation contract, principal separation and no-commit boundary in the accepted implementation. Do not treat schema-only gates or current-token disposable fixtures as actual-principal proof. The real-parent Local preflight and ACL-protected ledger checkpoint remain operator-owned prerequisites for any later live source run.

## Expected Result / Prediction

The final correction should reject an unvalidated cross-transaction binding before mutation and preserve both the primary residue and unknown sibling.

## Evidence Comparison

The final evidence matches the prediction: the 14/14 independent probe passes, the exact worker-return fast gate passes, reviewer-fast is 69/69, and `git diff --check` passes. Earlier contradictory results remain recorded above as the repair history rather than current disposition.

## Contradiction Or Gap Disposition

RESOLVED_BOUNDED. RV01 remains recorded as an orchestrator-origin defect, not attributed to Claude. RV02-RV12 are resolved for the named hermetic cases. Untested actual-principal, real-parent and production ACL conditions remain unverified and are not implicitly passed.

## Claim Update

The reservation-compatible tooling correction is accepted for bounded hermetic use. No Group 4 establishment, actual-token authorization, admission, activation or consumer-wiring claim is added. The worker return remains separately attributable and unchanged by the reviewer.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| RV01 | ORCHESTRATOR_PACKET_GAP; PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Validate the dispatch manifest and exact return binding before worker execution, including a no-runtime-diff fixture. Record for foundation tranche; not implemented here. |
| RV02-RV04 | WORKER_EXECUTION_ERROR | RUNTIME_BEHAVIOR_LEARNING | RULE_EXISTS | Correct implementation against existing boundary contract and use adversarial fixtures before real execution. |
| RV05 | MACHINE_GATE_GAP; WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Detect zero-eligible-return false assurance and require negative-path assertions to invoke the protected operation. Promote only after bounded design review. |
| RV06-RV11 | WORKER_EXECUTION_ERROR | RUNTIME_BEHAVIOR_LEARNING | RULE_EXISTS | Correct against the existing C0-R1/R2-03/R2-05/R2-06 contract; add shared-parent, complete-binding and phase-order adversarial regressions before Local reruns the probe. |
| RV12 | WORKER_EXECUTION_ERROR | RUNTIME_BEHAVIOR_LEARNING | RULE_EXISTS | Validate cross-transaction ledger rows before using them to whitelist inventory; add the Local 14th case as a permanent regression. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_finding_to_governance_learning.py` |
| literalTokensReviewed | `Memory class`; `## Checker Source Read-Ahead Block`; `## External Knowledge Intake Routing`; required operation-trace labels; finding-learning fields |
| gateRunPurpose | confirm the already-inspected worker-return evidence and consolidated review structure; gate execution is not the first discovery mechanism |
| claimBoundary | structural gate evidence only; no semantic acceptance inferred from a gate pass |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/audits/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md` |
| Chain map route | N/A with reason: shared-workspace INTERNAL_AGENT correction and Local review only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | C0-R1 contract and C1-R2 work order |
| Disposition | local first-party verification only |
| Claim boundary | no external research, public-repository or provider authority claim |

## External/Local Coordination Binding

Role: `INTERNAL_AGENT` Local reviewer; phase: bounded returned-evidence review;
final technical decision owner: Local. No external research input was used.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Agent Operation Trace Block

- Actor: Local reviewer.
- Provider or surface: Codex shared workspace.
- Agent type: INTERNAL_AGENT; phase REVIEW; technical decision owner Local reviewer.
- Session or invocation: C1-R2 Local returned-evidence review, 2026-09-23.
- Invocation ID: local-g4-c1-r2-review-20260923.
- Working directory: `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF`.
- Command or tool surface: PowerShell read-only inspection, Python governance gates, pwsh disposable probe, apply_patch packet/evidence edits.
- Target paths: work order, this review, probe evidence; five worker outputs inspected unchanged.
- Allowed scope source: operator request to repair manifest and run gate plus independent probe.
- Before status evidence: two modified writer scripts and three new worker files; HEAD as recorded above.
- After status evidence: those five files retained plus reviewer work-order repair, this review and evidence probe; final Local probe 14/14 and worker-return/reviewer-fast gates PASS.
- Diff evidence: `git diff --check` and work-order diff; no worker implementation edits by reviewer.
- Approval boundary: bounded tooling accepted for Local closure; no real-principal execution, no live source mutation, no external provider call or agent dispatch.
- Claim boundary: bounded local review only.
- Expected manifest: worker five-path manifest plus three reviewer-owned packet/evidence paths identified above.
- Actual changed set: same eight repo paths; ignored local probe copy and disposable fixture directory are review execution aids.
- Manifest delta: three reviewer-owned additions/changes outside worker manifest, explicitly attributed to reviewer scope; no expansion of worker authority.
- Deletion or rename disposition: no repository deletion or rename.

## Decision / Disposition

REVIEWER_ACCEPTED_BOUNDED_CLOSURE_PENDING. RV01-RV12 are resolved within the declared hermetic tooling boundary. The independent probe passes 14/14; the worker-return fast gate is eligible for final packaging verification; and `git diff --check` passes. Local may create the material commit and then the separate continuity commit. Do not reopen the writers or extend this decision to actual Party B/C execution.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_CORRECTION_2026-09-23.md` | reviewer-accepted bounded status, real execution/closure anchors, exact manifest and closure checklist | PASS |
| Completion or reviewer artifact | this review | final bounded disposition, exact hashes, changed-set trace, probe and gate evidence, claim boundary | PASS |
| Roadmap state | N/A with reason: this correction is governed by its work order and C0-R1 contract; no roadmap row changes in this material batch | no roadmap mutation claimed | N/A with reason |
| Registry JSON | N/A with reason: no corpus scan, classification or readiness registry state changes | no registry mutation claimed | N/A with reason |
| Registry Markdown | N/A with reason: no GC-051 state changes | no registry mutation claimed | N/A with reason |
| External evidence digest | N/A with reason: no external evidence used | local first-party evidence only | N/A with reason |
| System loop interlock | N/A with reason: reusable findings are routed in Finding-To-Governance Learning Disposition for the later foundation tranche | no interlock registry mutation in this material batch | N/A with reason |
| Session continuity | `CVF_SESSION_MEMORY.md`, generated active state and `AGENT_HANDOFF_V63_2026-09-18.md` | separate GC-020 continuity commit after material SHA exists | BLOCKED |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

Private provenance evidence only. This document accepts the bounded tooling correction; it does not itself upgrade the CVF foundation, certify untested cases, establish live governance behavior, or authorize Party B/C execution.

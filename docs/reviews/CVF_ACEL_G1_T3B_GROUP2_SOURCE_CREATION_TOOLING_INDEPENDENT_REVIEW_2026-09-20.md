# CVF ACEL G1 T3B Group 2 Source-Creation Tooling Independent Review

Memory class: governed-review

docType: review

Status: REWORK_REQUIRED

Date: 2026-09-20

Batch ID: ACEL-G1-T3B-GROUP2-SOURCE-CREATION-TOOLING-REVIEW

Review base head: `b8d23fdd362322686b77c53dd2b11b5cb1e65d55`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Record Local's independent review of the five uncommitted T3B worker outputs,
separate the unrelated parked-path gate findings from defects in the returned
lane, and define one consolidated R1 correction. This review performs no
alternate-principal execution and creates no real Group 2 source.

## Target / Source

| Source | Identity / role |
|---|---|
| governing work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_2026-09-20.md`; SHA-256 `fc197fb73f0ddd3ae87f1c6b80f4f64be275481fdd8e2fb31bbef23f078f878b` |
| worker return | `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-20.md`; SHA-256 `95ae5cd5fce18ff115482da85475f21b880149387d6ac2990fddc57d8ee3c649` |
| Group 2 contract | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`; Source Group 2; Explicit Approval, Activation And Supersession |
| returned code | the two PowerShell writers and Python checker/test pair named by the work order's five-path manifest |
| OS facts | Party A SID ending 1006; Approver SID ending 1008; Local reviewer SID ending 1001; Approver is not a local Administrator; Local's non-elevated Administrators SID is deny-only |

## Scope / Methodology

Local consumed the worker's 42/42, 49/49 and 43/43 passing evidence, then
inspected only contract-sensitive seams that could invalidate those results:
cross-principal read access, per-version content binding, supersession entry,
full-history verification and return-gate readiness. Local reran the focused
tests and both hermetic writer suites once, inspected the exact DACL grants and
state-machine code, and ran the worker-return fast gate. No implementation was
recreated, no credential was requested and no real source path was written.

## Findings / Position

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| T3B-RV-1 | CRITICAL | Party A's writer hardens `SPEC_v1.json` to Party A plus `BUILTIN\Administrators`; the non-admin Approver receives no read grant, so the required decision writer cannot read the spec. The Local read grant is also ineffective in Local's ordinary non-elevated token because the Administrators SID is deny-only. | DACL_CONTRACT_CORRECTION_REQUIRED |
| T3B-RV-2 | CRITICAL | `validate_decision_history` compares every event, including v2, to the one v1 `spec_hash_hex`. The positive mixed-version test deliberately reuses v1's hash for v2. This accepts an uncited/nonexistent v2 binding and rejects a legitimate v2 with its own content hash. | PER_VERSION_SOURCE_BINDING_REQUIRED |
| T3B-RV-3 | HIGH | the real approver writer fixes both path and version to `SPEC_v1.json`/1 but exposes `SUPERSEDED`; it neither cites nor independently validates a newer version before superseding v1, contrary to the work order and T2F lifecycle. | SUPERSESSION_ENTRY_CORRECTION_REQUIRED |
| T3B-RV-4 | HIGH | the original work order misapplies `evidenceReadinessContract: REQUIRED_V1` to a bounded local tooling tranche with no audit/discovery-manifest artifact in its exact five-path manifest. The return then uses an invalid pseudo-binding and a multiline status not recognized for pending independent review. | DISPATCH_AND_RETURN_PACKET_CORRECTION_REQUIRED |

The worker's reported three older independent-probe findings are out-of-lane
parked-path debt and are not assigned to this worker. They do not erase the
four in-lane findings above.

## Risk / Corrective Action

Acceptance would produce tooling that passes hermetic tests but cannot execute
the Party A-to-Approver handoff, and a checker that does not cryptographically
bind mixed-version history to each cited immutable spec. One R1 correction
must repair all four findings together and add regression probes that would
fail on the returned implementation. No real Party A or Approver execution is
permitted during R1.

## Consolidated Correction Contract

1. Preserve the exact five-path worker manifest; modify no parked path.
2. Grant Approver SID `S-1-5-21-1644666849-912006174-747199667-1008`
   read-only access to each Party A-created spec while denying it write/delete/
   ownership/permission-change authority. Grant Local reviewer SID
   `S-1-5-21-1644666849-912006174-747199667-1001` explicit read-only access to
   both source files; do not rely only on a deny-only Administrators SID.
3. Resolve every decision event's `specVersion` to immutable
   `SPEC_v{n}.json`, strictly validate that record, recompute that version's
   decoded-content hash, and compare it to that event's `recomputedHashHex`.
   Missing, duplicate, malformed, path-escaped or mismatched version sources
   fail closed.
4. Real `SUPERSEDED` must require an explicit newer spec version, validate its
   independent file/hash, require that newer version's prior `APPROVED` and
   `ACTIVATED` events, require exactly one active old version, then append the
   supersession of the old version. It must never infer latest/largest.
5. Add regressions proving: Approver can read but not modify Party A's spec;
   Local ordinary-read SID is explicit; v2 with its own different valid hash
   passes full-history validation; v2 reusing v1 hash fails; missing `SPEC_v2`
   fails; v1 supersession without a validated active v2 fails.
6. The R1 work order supersedes the misapplied evidence-readiness requirement
   with an explicit not-applicable reason for this non-audit tranche. Bind the
   worker return to R1, use one exact recognized status, and remove the invalid
   pseudo-binding. Gate debt outside the five owned paths is disclosed
   separately and is not the return disposition.

## Decision / Disposition

`REWORK_REQUIRED`.

One consolidated internal R1 dispatch is authorized. The current five outputs
remain unaccepted and uncommitted. Group 2 source creation, approval,
activation, T3E wiring and candidate admission remain closed.

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3b-group2-source-creation-tooling-problem","chainMode":"SUCCESSOR","chainOrdinal":1,"predecessor":{"path":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_2026-09-20.md","sha256":"fc197fb73f0ddd3ae87f1c6b80f4f64be275481fdd8e2fb31bbef23f078f878b"},"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["acel_g1_group2_real_source_not_created","cross-principal-dacl-gap","per-version-binding-gap","supersession-entry-gap","worker-return-readiness-gap"],"reopened":[],"current":["acel_g1_group2_real_source_not_created","cross-principal-dacl-gap","per-version-binding-gap","supersession-entry-gap","worker-return-readiness-gap"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":1,"nonDecreasingBlockerTransitions":1},"claims":[{"claimId":"ACEL-G1-T3B-INDEPENDENT-REVIEW","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_INDEPENDENT_REVIEW_2026-09-20.md"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Finding-To-Governance Learning Disposition

- Defect class: `DISPATCH_AND_WORKER_CONTRACT_GAP`
- Learning lane: `GOVERNANCE_CONTROL_PLANE`
- Disposition: `RULE_EXISTS`
- Next control action: bind existing principal-separation, per-version source
  identity, reviewer-fast and supersession requirements directly into the R1
  acceptance probes. A new general CVF rule is not justified from this single
  tranche; recurrence after R1 would trigger machine-check elevation.

## Epistemic Process Block

### Expected Result / Prediction

Hermetic tests were expected to pass, but cross-principal ACL and mixed-version
binding were the most likely independent-review failure surfaces.

### Evidence Comparison

All returned unit/self-tests passed. Direct source inspection contradicted
their coverage: the ACL has no Approver grant and the mixed-version positive
test intentionally assigns v1's hash to v2. The worker-return fast gate also
failed on the current return's own evidence binding.

### Contradiction Or Gap Disposition

Passing worker tests are retained as useful evidence for unaffected behavior,
but they cannot support acceptance of the contradicted cross-principal and
per-version claims. Those claims are narrowed to `REWORK_REQUIRED`.

### Claim Update

The tooling is substantially implemented but is not operationally coherent or
review-ready. No real-source readiness claim is made.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_machine_closure_package.py` |
| literalTokensReviewed | governed review headings; defect/lane/disposition tokens; epistemic comparison/gap/update; trace fields; public disposition; machine closure rows |
| gateRunPurpose | preserve an evidence-backed consolidated rejection without duplicating implementation |
| claimBoundary | checker PASS validates packet shape only; it does not accept tooling or authorize real source execution |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | original T3B order plus this review | four consolidated findings; R1 supersedes current execution authority | PASS |
| Completion or reviewer artifact | this review | `REWORK_REQUIRED` | PASS |
| Roadmap state | existing ACEL roadmap/contract | no closure or successor tranche | N/A with reason |
| Registry JSON | N/A with reason: no real source exists | no mutation | N/A with reason |
| Registry Markdown | N/A with reason: no registry owner changes | no mutation | N/A with reason |
| External evidence digest | N/A with reason: local bounded review only | no external evidence | N/A with reason |
| System loop interlock | Group 2 real execution checkpoint | remains closed | PASS |
| Session continuity | active continuity surfaces | separate session-sync after R1 dispatch commit | PENDING_SEPARATE_SYNC |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF Local orchestrator/reviewer |
| Provider or surface | local private provenance repository |
| Session or invocation | ACEL G1 T3B independent review, 2026-09-20 |
| Working directory | repository root |
| Command or tool surface | governed reads, SHA-256, PowerShell/Python hermetic tests, OS account/group readout, worker-return fast gate, git |
| Target paths | five uncommitted T3B worker outputs and this review |
| Allowed scope source | operator authorized audit and worker dispatch; original committed T3B order assigns Local independent review |
| Before status evidence | HEAD `b8d23fdd362322686b77c53dd2b11b5cb1e65d55`; 13 parked paths plus exact five T3B outputs; staging empty |
| After status evidence | five worker outputs remain uncommitted; reviewer artifacts prepare one R1 dispatch; no parked path touched |
| Diff evidence | exact source lines, OS SID/group facts, 42/42, 49/49, 43/43 passes and worker-return fast failure reconciled |
| Approval boundary | review and corrective-dispatch preparation only |
| Claim boundary | no credentials, alternate-user execution, real source, activation, admission, provider/live/public/deploy effect |
| Agent type | independent Local reviewer/orchestrator |
| Invocation ID | `acel-g1-t3b-group2-tooling-independent-review-2026-09-20` |
| Expected manifest | this review plus paired R1 GC-018 baseline and work order |
| Actual changed set | this review plus paired R1 GC-018 baseline and work order |
| Manifest delta | MATCH after dispatch packet authoring |
| Deletion or rename disposition | none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private review and corrective dispatch; no public artifact is claimed.

## Claim Boundary

This review rejects the current T3B return and authorizes one bounded R1
correction only. It does not create or validate a real Group 2 source, use
credentials, run as Party A/Approver, establish activation, wire T3E, admit a
candidate or authorize provider/live/network/public/deployment effects.

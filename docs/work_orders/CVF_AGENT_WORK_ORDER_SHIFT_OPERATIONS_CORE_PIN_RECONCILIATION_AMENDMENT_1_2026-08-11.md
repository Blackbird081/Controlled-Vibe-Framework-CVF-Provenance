# CVF Agent Work Order - Shift Operations Core Pin Reconciliation Amendment 1

Status: DISPATCH_READY

Memory class: governed-work-order

Date: 2026-08-11

Batch ID: SOPR-CP1-A1

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: `0b835be3ff1ac1fbd1c95e365471887202d718b5`

dispatchBaseHead: `8428728dc039d5a1ccba816cbdd3fe8cba0ca4a3`

## Dispatch Prompt Envelope

DISPATCH STATUS: READY

Canonical packet: this Amendment 1 Work Order plus paired baseline and source
verification at their committed exact hashes.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: `0b835be3ff1ac1fbd1c95e365471887202d718b5`.

Current-time notes: target carries exact-10 pending worker output; hidden Core
is clean at local `origin/main` `2103a38f...`; no remote refresh is authorized.

Do-not-misread notes: this is a test/evidence repair, not runtime-security or
product authority.

Required first actions: verify target HEAD, staged zero, exact-10 dirty set,
all eleven preimages, hidden-Core equality and Amendment authority hashes.

Return contract: modify exact-2, finish at exact-11, run every required gate,
leave staged zero/HEAD unchanged, and return pending independent review or a
named blocked disposition.

Worker role: provider-neutral `REPAIR_WORKER`.

Target root: `shift-operations-workspace`.

Read this Amendment, its paired baseline and source-verification review, then
the parent SOPR-CP1 Work Order. Verify the exact dirty preimages before writing.
Repair only the JWT tamper fixture and the existing worker return. Run every
required check, leave staged zero and HEAD unchanged, and return
`COMPLETE_PENDING_INDEPENDENT_REVIEW` or a named blocked disposition.

## Purpose

Repair the deterministic-test blocker independently reproduced after the
original SOPR-CP1 worker return, without changing the accepted pin/continuity
semantics or opening a product/runtime lane.

## Scope / Methodology

Preserve the existing exact-10 pending diff. Modify one existing P4-A1 test so
its tampered JWT differs at the decoded signature-byte level, then correct and
extend the existing worker return. The repair worker writes exact-2 paths and
the final pending target manifest becomes exact-11.

## Findings / Position

The original test's final-character substitution may change the JWT text while
preserving decoded signature bytes. This is a test-fixture reliability defect,
not evidence of a runtime signature-verification bypass. Closure remains
blocked until AC-07 is reproducibly satisfied.

## Risk / Corrective Action

R2 test/evidence correction. Production/runtime source edits, waivers, hidden-
Core mutation, provider/live/network calls, or any twelfth target path are
forbidden.

## Authority Chain

1. Operator-delegated orchestrator/reviewer authority.
2. Parent baseline and Work Order for SOPR-CP1.
3. Independent review findings:
   `docs/reviews/CVF_SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_AMENDMENT_1_SOURCE_VERIFICATION_2026-08-11.md`.
4. Paired baseline amendment:
   `docs/baselines/CVF_GC018_SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_AMENDMENT_1_2026-08-11.md`.
5. This Amendment 1 Work Order at its committed exact SHA-256.

## Roles And Ownership

| Role | Responsibility |
|---|---|
| orchestrator/dispatcher | owns Amendment 1 source verification and authority commit |
| repair worker | writes only exact-2 repair paths; no stage or commit |
| independent reviewer/closer | recomputes all evidence and owns any target commit |
| session-sync steward | synchronizes Core only after repair dispatch/closure |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| taskClass | bounded no-commit test/evidence repair |
| risk | R2 |
| intakeSummary | repair one reproduced test-fixture blocker without runtime expansion |
| routeMode | `SINGLE_AGENT_SINGLE_ROLE` |
| selected route | `SINGLE_AGENT_SINGLE_ROLE`: one repair worker then independent reviewer |
| worker commit | FORBIDDEN |
| escalation | base/preimage mismatch, extra path, runtime change or external effect |

## Required First Reads

This Amendment; paired baseline/source review; parent Work Order; target
bootstrap/state/handoff; existing worker return; named test file; JWT token
decoder source; target AGENTS/manifest/policy. Use progressive reads only.

## Pre-Flight Checks

- target HEAD equals exact executionBaseHead;
- target staged set is empty;
- target dirty set is exact original SOPR-CP1 exact-10;
- all eleven preimages below match;
- hidden public Core remains clean with HEAD equal local `origin/main` at
  `2103a38fda01ee827e9fc6c3be38a824fa5d54ad`;
- private authority hashes match the committed Amendment 1 packet;
- no reviewer completion review exists in the target.

## Write Ownership

Repair worker owns only the exact-2 write set. Reviewer owns completion review,
closure conversion and target commit. Core session files are dispatcher-owned.

## Execution Plan

1. Rehydrate target repair context and verify authority/preimages.
2. Preserve nine pending paths byte-exact.
3. Replace ambiguous JWT text mutation with decoded-signature-byte mutation.
4. Correct and extend the existing worker return.
5. Run isolated stress, two full suites, original gates and exact-manifest checks.
6. Return unstaged and uncommitted for independent review.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| exact-10 gate failure outside scope must stop | `docs/baselines/CVF_GC018_SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_2026-08-11.md` | Stop Conditions | `Stop Conditions` | SOPR-CP1 | ACCEPT |
| final-character mutation is ambiguous | `docs/reviews/CVF_SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_AMENDMENT_1_SOURCE_VERIFICATION_2026-08-11.md` | normalized target evidence | `test_forged_or_tampered_credential_is_rejected_not_trusted` | P4-A1 test | ACCEPT |
| runtime decoder explicitly fixes HS256 | `docs/reviews/CVF_SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_AMENDMENT_1_SOURCE_VERIFICATION_2026-08-11.md` | normalized target evidence | `decode_access_token` | workspace API auth | ACCEPT |
| test-only exact-11 expansion | `docs/reviews/CVF_SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_AMENDMENT_1_SOURCE_VERIFICATION_2026-08-11.md` | Exact Target Snapshot | `Repair Worker Write Set` | Amendment 1 | ACCEPT |

## Exact Final Pending Manifest

1. `.cvf/manifest.json`
2. `AGENTS.md`
3. `knowledge/manifest.json`
4. `IMPLEMENTATION_STATUS.json`
5. `SESSION/ACTIVE_SESSION_STATE.json`
6. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
7. `SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
8. `SESSION/SESSION_MEMORY.md`
9. `SESSION/handoffs/CORE_PIN_RECONCILIATION_2026-08-11.md`
10. `docs/decisions/SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_WORKER_RETURN_2026-08-11.md`
11. `tests/cvf/test_p4a1_retrieval_authorization.py`

## Repair Worker Write Set

The worker may modify only:

1. `tests/cvf/test_p4a1_retrieval_authorization.py`
2. `docs/decisions/SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_WORKER_RETURN_2026-08-11.md`

The other nine pending files are protected retained outputs. Any byte drift in
them is a blocking mismatch.

## Fresh Dirty-Tree Preimage Authority

| Path | Required SHA-256 |
|---|---|
| `.cvf/manifest.json` | `4c3223abc51995337adf549a917de045d22d3d024c394d0db5fee4e3402eacec` |
| `AGENTS.md` | `e6d7b5307e03b8bab50879824a2d5f465ea8e4de92dbe6135ad3ffa46d637be9` |
| `knowledge/manifest.json` | `b35e9d63967cb3e62ea09632a91c3fc4fcc7c6e06e1c5c1fa85105e0720a1f86` |
| `IMPLEMENTATION_STATUS.json` | `0b92ba573663dbd8d91b6b449adb0f25b20d4c72657f9c9f8916e2e9bee49e35` |
| `SESSION/ACTIVE_SESSION_STATE.json` | `79d6b92329833824cee03d275f8dcc712d1625495b78d8896dd7c1bf2acb2c88` |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `53c83a466cf9cd02f8db41d8bf0f8f40ec2e88c7a62b7a6386ae44c896435075` |
| `SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `e68e3a8cf51f3b6eb43ea9e8c1e82c21454e7535fd6663de3e82eb165c92e4cd` |
| `SESSION/SESSION_MEMORY.md` | `e97c7e0901c51db3f70039e7f8e6fb6889e01ea36b721f827d1d81f6aea66d29` |
| `SESSION/handoffs/CORE_PIN_RECONCILIATION_2026-08-11.md` | `a894ec7855d02f193150574265bf17e75869c504f7fb8aa2391056324d5e765c` |
| `docs/decisions/SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_WORKER_RETURN_2026-08-11.md` | `eb4953ac28a484a7cbbcd6bc2f2f164036ba3675078e78d2584096a03cb8d843` |
| `tests/cvf/test_p4a1_retrieval_authorization.py` | `18a19ca48e64fa390ca68f09af05459667be25dddd763ad19039c415ea99c4e0` |

## Required Behavior

1. Preserve target HEAD and staged zero.
2. Decode only the JWT signature segment using base64url padding rules, flip a
   byte in the decoded signature, re-encode without padding, and rebuild the
   three-segment token.
3. Assert or otherwise make structurally evident that decoded signature bytes
   and token text differ; do not change production token verification.
4. Update the worker return to:
   - remove the false extra-hex-character statement;
   - replace the cross-test/clock hypothesis with the verified base64url
     fixture root cause;
   - cite Amendment 1 authority and exact test diff;
   - record ten isolated and two full-suite consecutive passes;
   - retain `COMPLETE_PENDING_INDEPENDENT_REVIEW` only if every gate passes.
5. Do not edit the nine retained pending paths.

## Required Artifact Manifest

Work-Order Fulfillment Manifest: exact rows below are required.

| Required output | Path | Required at handoff | State |
|---|---|---|---|
| deterministic test repair | `tests/cvf/test_p4a1_retrieval_authorization.py` | yes | MODIFY |
| corrected worker evidence | `docs/decisions/SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_WORKER_RETURN_2026-08-11.md` | yes | MODIFY |
| retained original pending output | other nine paths in exact final manifest | yes | BYTE_EXACT_PRESERVE |

## Scope Firewall Authorization

Allowed paths:

- Core dispatcher-owned packet paths:
  - `docs/reviews/CVF_SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_AMENDMENT_1_SOURCE_VERIFICATION_2026-08-11.md`
  - `docs/baselines/CVF_GC018_SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_AMENDMENT_1_2026-08-11.md`
  - `docs/work_orders/CVF_AGENT_WORK_ORDER_SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_AMENDMENT_1_2026-08-11.md`
- target repair worker paths:
  - `tests/cvf/test_p4a1_retrieval_authorization.py`
  - `docs/decisions/SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_WORKER_RETURN_2026-08-11.md`

Forbidden paths: every other Core/target/hidden-Core/workspace-root path and
all product/runtime/provider/live/public/push/deploy surfaces.

Operator authorization: explicit delegated orchestrator/reviewer decision
authority, applied after independent reviewer reproduction on 2026-08-11.

Rollback boundary: discard only the two repair-worker edits; preserve the
original exact-10 pending SOPR-CP1 diff and every committed repository state.

## Required Checks

From target root after the repair:

```powershell
1..10 | ForEach-Object { python -m pytest tests/cvf/test_p4a1_retrieval_authorization.py -q; if ($LASTEXITCODE -ne 0) { throw "isolated iteration failed" } }
python -m pytest tests/cvf -q
python -m pytest tests/cvf -q
python scripts/check_session_state.py
python scripts/check_project_knowledge.py
python scripts/testing/validate_repository.py
python scripts/check_file_size.py
powershell -NoProfile -ExecutionPolicy Bypass -File "..\.Controlled-Vibe-Framework-CVF\scripts\check_cvf_workspace_agent_enforcement.ps1" -ProjectPath "." -AllowOfflinePinnedCore
git diff --check
git status --short
git diff --name-status
git diff --cached --name-status
```

Also recompute SHA-256 for the nine protected retained paths and prove exact
equality with their Amendment 1 preimages.

## Verification Commands

The independent reviewer repeats the isolated stress, at least one full suite,
all local gates, exact-11 equality, final hashes, hidden-Core equality, staged
zero and unchanged HEAD. Component PASS cannot waive a semantic mismatch.

Core reviewer-fast command:
`python governance/compat/run_worker_return_fast_gate.py`.

## Acceptance Criteria

AC-A1-01 through AC-A1-08 are exactly those in the paired baseline amendment.
Any unresolved criterion returns a named blocked disposition.

## Worker Autonomy / No-Question Rule

Repair the exact two authorized files without asking again while authority,
preimages and scope match. Stop rather than infer permission for another path.

## Evidence Requirements

Record before/after hashes; decoded-byte mutation method; exact test diff;
isolated 10/10; full suites 2/2; original gates; exact-11; staged zero; HEAD
unchanged; hidden-Core unchanged; and zero provider/network/live calls.

## Review Gate

Worker may not self-approve. Independent reviewer recomputes every Amendment 1
criterion and owns closure conversion and any target commit.

## Closure Checklist

- [ ] Exact target and eleven dirty-tree preimages verified.
- [ ] Repair worker write set exact-2.
- [ ] Final pending target manifest exact-11.
- [ ] Decoded signature byte definitely changes.
- [ ] Isolated stress 10/10 and full suites 2/2 pass.
- [ ] Original gates and doctor pass within allowed warning.
- [ ] Worker return evidence corrected.
- [ ] Staged zero, no worker commit, zero external calls.

Unchecked items are intentional at dispatch and are not closure claims.

## Worker Return Packet Shape Contract

workerReturnPath:
`docs/decisions/SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_WORKER_RETURN_2026-08-11.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

scopeClassification: GOVERNANCE_TEST_EVIDENCE_REPAIR_ONLY_NO_COMMIT

requiredGate: target checks above plus
`python governance/compat/run_worker_return_fast_gate.py` from private Core.

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must include these always-required sections or terms:

- Purpose
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Claim Boundary
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- actual `executionBaseHead`
- actual `git status --short`

The worker return must include or explicitly mark `N/A with reason` or
`NOT_APPLICABLE_WITH_REASON` for:

- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

Omission is a blocking worker-return defect.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | `SINGLE_AGENT_SINGLE_ROLE` followed by independent reviewer/closer |
| rolePattern | repair worker -> reviewer/closer -> session-sync steward |
| phase | BUILD_REPAIR pending REVIEW |
| baseHeadFor(phase) | executionBaseHead=`0b835be3f`; closureBaseHead=reviewer captures |
| changedSetScope(phase) | worker write exact-2; final pending exact-11 |
| traceScope(phase, actor) | worker records repair diff; reviewer records closure range |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer only |
| crossBatchIsolation | no product/runtime/hidden-Core/other lane |
| nextMoveSurfaces | unchanged until independent acceptance |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | target `docs/decisions/SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_COMPLETION_REVIEW_2026-08-11.md` when accepted or rejected |
| reviewerOwnedClosurePaths | final pending exact-11 plus optional completion review |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

Reviewer converts pending review to exact final mode
`shift_operations_core_pin_reconciliation_closed_bounded_parked` only after
all original and Amendment 1 criteria pass.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | return contract; exact manifest; no-commit; scope firewall; reviewer conversion |
| gateRunPurpose | confirmation after source diagnosis, not first discovery |
| claimBoundary | Amendment 1 packet and test/evidence repair only |

## External Knowledge Intake Routing

Canonical chain map:
`docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`.

| Field | Value |
|---|---|
| Chain map | canonical chain map above |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | `BLOCKED_UNTIL_CVF_PROOF`; no runtime claim admitted |
| Matching local-view guard | `governance/compat/check_delta_execution_claim_boundary.py` |
| Owner surface | SOPR-CP1-A1 Work Order |
| Disposition | `NOT_APPLICABLE_WITH_REASON` |
| Claim boundary | no non-CVF input admitted as authority |

## Rescan Intelligence Hardening

Original source artifact: N/A with reason - no corpus source intake.
Predecessor intake artifact: N/A with reason - parent SOPR packet only.
Delta ledger status: NOT_APPLICABLE_WITH_REASON.
Routing matrix status: NOT_APPLICABLE_WITH_REASON.
Semantic sampling status: NOT_APPLICABLE_WITH_REASON.
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

### Original-Intake Delta Ledger

| Category | Disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | parent exact-10 retained |
| CHANGED_DISPOSITION | AC-07 moves to repair required |
| NEW_FINDING | base64url fixture ambiguity |
| REMOVED_OR_REJECTED | cross-test clock hypothesis rejected |

### Follow-Up Routing Matrix

| Lane | Disposition |
|---|---|
| DO_NOW | exact test/evidence repair |
| SEPARATE_RUNTIME_TRANCHE | N/A with reason: no runtime defect evidenced |
| STRATEGIC_OPERATOR_DECISION | N/A with reason: authority delegated |
| OUT_OF_SCOPE | production/runtime/product changes |
| RESOLVED_BY_DESIGN | deterministic decoded-byte flip |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| SOPR-A1-S1 | worker return Findings | cross-test interaction | reject or retain | isolated repeated failure | REJECT |
| SOPR-A1-S2 | JWT test fixture | token text changes | test validity | compare decoded signature bytes | REPAIR_REQUIRED |

## Corpus Completeness And Report Integrity

Corpus task class: N/A with reason - not a corpus task.
Corpus root: N/A with reason - none.
Snapshot time: 2026-08-11 dispatch.
Enumeration command: named-file reads only.
Manifest artifact or inline manifest: exact final pending manifest above.
Manifest hash: N/A with reason - no corpus manifest.
Processing ledger artifact or inline ledger: paired source verification.
Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
Reconciliation: N/A with reason - no corpus totals.
Unresolved files: none at dispatch beyond the named repair.
Declared exclusions: all unnamed paths.
Unreadable or unsupported files: none.
Aggregation check: N/A with reason - no aggregation.
Drift check: exact preimage hashes required.
Output traceability: Work Order to worker return and reviewer closure.
Adversarial verification: isolated stress and decoded-byte diagnostic.
- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this Work Order is not a corpus report.

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| defectClass | `WORKER_EXECUTION_ERROR` |
| lane | `GOVERNANCE_CONTROL_PLANE` |
| disposition | `RULE_EXISTS` |
| owner | repair worker then independent reviewer |
| rationale | existing fail-closed review and exact-scope rules caught the issue |

## Epistemic Process Block

| Field | Value |
|---|---|
| claim | fixture can preserve decoded bytes despite changed JWT text |
| evidence | isolated reproduction plus decoded-byte diagnostic |
| correction | flip a decoded signature byte then re-encode |
| boundary | no runtime bypass claim |

## Machine Closure Package

NOT_APPLICABLE_WITH_REASON: worker repair is pending independent closure.

## Provider Memory Authority Boundary

Provider-local memory is `NOT_CVF_SOURCE` and is neither read nor cited as
authority. All dispatch claims resolve through governed Core artifacts and
recomputed local evidence.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | orchestrator/reviewer/Work Order author |
| Provider or surface | private Core plus read-only downstream evidence |
| Session or invocation | `sopr-cp1-a1-dispatch-20260811` |
| Working directory | private Core root for authority authoring |
| Command or tool surface | local source reads, diagnostics, Markdown, gates, Git |
| Target paths | exact three Core packet paths at dispatch |
| Allowed scope source | operator delegation and independent review finding |
| Before status evidence | Core clean worktree; target intentionally carries exact-10 pending worker output, staged zero, and AC-07 intermittent fail |
| After status evidence | Amendment 1 exact-2 write/exact-11 final route ready |
| Diff evidence | Core pre-dispatch range |
| Approval boundary | test/evidence repair only |
| Claim boundary | no product/runtime/external effect |
| Agent type | orchestrator/reviewer |
| Invocation ID | `sopr-cp1-a1-dispatch-20260811` |
| Expected manifest | source review, baseline amendment, Work Order amendment |
| Actual changed set | resolved by pre-dispatch gate |
| Manifest delta | MATCH required before authority commit |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | deterministic JWT negative-test fixture and evidence correction |
| claimDisposition | CLAIM_REJECTED: no execution-control claim |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT; local tests/checkers only |
| actionEvidence | CLAIM_REJECTED_NO_ACTION; no runtime/provider action |
| invocationBoundary | local worker shell/Python test invocation |
| interceptionBoundary | no direct interception/proxy/runtime gate claim |
| claimLanguage | fixture reliability, not authentication bypass |
| forbiddenExpansion | product/runtime/provider/live/public/package/deploy/push |

## Worker Return

Return exactly one:

- `COMPLETE_PENDING_INDEPENDENT_REVIEW`
- `BLOCKED_BASE_OR_PREIMAGE_MISMATCH`
- `BLOCKED_FORBIDDEN_SCOPE_REQUIRED`
- `BLOCKED_WITH_REASON`

## ADIF Defect Registry Disclosure

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch`.

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defectIds: `ADIF-0001`, `ADIF-0002`, `ADIF-0014`, `ADIF-0015`,
`ADIF-0020`, `ADIF-0021`, `ADIF-0028`, `ADIF-0029`, `ADIF-0033`, `ADIF-0044`.

Dispatch impact: exact dirty manifest/preimages, provider-memory exclusion,
checker source read-ahead, no protected Core edit, and bounded test timeouts.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOPR-CP1-A1 --title "Shift Operations Core Pin Reconciliation Amendment 1" --date 2026-08-11 --base 8428728dc039d5a1ccba816cbdd3fe8cba0ca4a3 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit repair profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | exact dirty preimages, test root cause, exact-2 write set, exact-11 final set, checks and boundaries |
| checkerReadAheadConfirmation | applicable sources named above were read through direct gate diagnostics |
| docOnlyNewFields | repairWorkerWriteSet; exactFinalPendingManifest; decodedByteMutation |
| claimBoundary | dispatch authoring provenance only |

## Return-To-Orchestrator Conditions

Return immediately for base/preimage drift, non-exact dirty set, additional
path need, production/runtime edit need, external effect, new warning, or any
remaining gate failure.

## Execution Authority Waiver

operator.checkpoint.waiver: Amendment 1 exact-2 repair is authorized only from
the committed exact hash of this packet and paired baseline. Any target base,
scope, commit-mode or external-effect change requires fresh authority.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private repair dispatch; no public-sync authority.

## Claim Boundary

This Amendment authorizes only a deterministic test-fixture and evidence
repair. It does not accept the original worker return, waive AC-07, change
production/runtime code, or claim public, provider, deployment or production
readiness.

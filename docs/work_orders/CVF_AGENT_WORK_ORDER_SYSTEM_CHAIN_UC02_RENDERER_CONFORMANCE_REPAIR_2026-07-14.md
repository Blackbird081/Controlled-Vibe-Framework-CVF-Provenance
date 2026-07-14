# CVF Agent Work Order - System Chain UC-02 Renderer Conformance Repair

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Work Order ID: SCLP-UC02-R3

Date: 2026-07-14

dispatchBaseHead: `ef38f567e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: implementation worker; reviewer/closer remains separate.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_SYSTEM_CHAIN_UC02_RENDERER_CONFORMANCE_REPAIR_2026-07-14.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: capture executionBaseHead at start.

Current-time notes: UC-02 is already proven; this is provider-free renderer repair.

Do-not-misread notes: do not run UC-02, packet bootstrap, scenario commands, providers, or individual checker shortcuts.

Required first actions: read paired baseline, completion/GAP, three renderer owners, orchestration callers, and checker sources; capture clean base and run pre-implementation.

Return contract: `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` with exact changed set, tests, one regeneration call, zero UC-02/provider calls, gates, and unchanged HEAD.

## Purpose

Repair three source-verified Markdown renderers and regenerate their current
outputs without changing the accepted UC-02 proof.

## Authority Chain

1. `docs/reviews/CVF_SYSTEM_CHAIN_UC02_CURRENT_RERUN_COMPLETION_2026-07-14.md`
2. `docs/reference/system_chain/gaps/entries/phase_governance_generated_markdown_conformance.json`
3. paired GC-018
4. this work order

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | dispatcher role | source fidelity and dispatch |
| Worker | implementation worker | exact source/test/output manifest; no commit |
| Reviewer/closer | reviewer/closer role | review, GAP closure, commit, session sync |

## Required First Reads

Full-read this packet, paired baseline, UC-02 completion, renderer GAP, three
renderer sources, `baselines.py`, release gate, and four failing checker sources.

## Pre-Flight Checks

Capture `executionBaseHead`, require clean worktree, refresh every Source
Verification row, and pass pre-implementation. Repair allowed-scope machine
gate defects directly; stop for any additional source owner.

## Scope / Target / Owner Boundary

Writable source/test paths:

- `scripts/export_cvf_remediation_receipt_log.py`
- `scripts/runtime_evidence_manifest/manifest_builder.py`
- `scripts/export_cvf_release_packet.py`
- `governance/compat/test_system_chain_uc02_renderer_conformance.py`

Generated outputs are the 20 current files emitted by the existing release
gate: seven JSON/log pairs, one manifest JSON/log pair, and four packets. One
worker return is also writable. Everything else is read-only.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| shared family-log renderer | `scripts/export_cvf_remediation_receipt_log.py` | line 26 | `build_log` | remediation Markdown renderer | EXISTS | ACCEPT |
| family orchestration imports shared renderer | `scripts/runtime_evidence_manifest/baselines.py` | lines 7, 12-27 | `build_log`; `emit_family_baseline` | family baseline orchestration | RUNTIME_BEHAVIOR | ACCEPT |
| manifest-log renderer | `scripts/runtime_evidence_manifest/manifest_builder.py` | line 77 | `build_manifest_log` | manifest Markdown renderer | EXISTS | ACCEPT |
| packet renderer | `scripts/export_cvf_release_packet.py` | line 71 | `build_packet` | packet Markdown renderer | EXISTS | ACCEPT |
| packet defects are literal source values | `scripts/export_cvf_release_packet.py` | lines 55, 176, 181 | `_extract_latest_batch_title`; `build_packet` | packet renderer | VALUE_SET | ACCEPT |
| release gate is the regeneration owner | `scripts/run_cvf_runtime_evidence_release_gate.py` | line 35 | `main` | release-gate orchestration | RUNTIME_BEHAVIOR | ACCEPT |

## Current Runtime Freshness Verification

Fresh reads at `ef38f567e` confirm the three template owners. Wrapper/orchestrator
paths are not template owners and must not be edited unless source verification
returns `BLOCKED_SOURCE_NOT_FOUND` to reviewer.

## Negative Search And Collision Discipline

| Field | Evidence |
|---|---|
| Search roots | `scripts/`; `governance/compat/`; `docs/reviews/cvf_phase_governance/`; `docs/reference/system_chain/` |
| Search command | `rg -n "build_log|build_manifest_log|build_packet|Checker Source Read-Ahead Block|Verification Range|Acceptance Receipt Assertion Matrix" scripts governance/compat docs/reviews/cvf_phase_governance docs/reference/system_chain` |
| Coverage | runtime source, tests, governed docs, generated JSON/Markdown, and local GAP evidence; external evidence is N/A because this is a repository-source repair |
| Same-token collision result | the three renderer symbols have authoritative definitions plus known call/import occurrences; no fourth authoritative renderer occurrence was found at dispatch |
| Disposition | known call-site collisions are non-authoritative and not binding as template owners; an absent required source owner returns `BLOCKED_SOURCE_NOT_FOUND` |

## Execution Plan

1. Capture clean execution base and run pre-implementation.
2. Add focused tests that call all three renderer functions with temporary
   inputs and assert required structure, checker-read-ahead, ASCII, and no
   stale/empty range PASS claims.
3. Repair only the three renderer sources. Preserve evidence values and JSON.
4. Run focused tests and existing archive-path tests.
5. Invoke `python scripts/run_cvf_runtime_evidence_release_gate.py` once.
6. Run reviewer-fast/worker-return gates over regenerated outputs.
7. One retry is allowed only after a concrete source/test repair changes the
   expected output; never invoke UC-02.
8. Return without commit or stage.

## Planned Worker Fulfillment Manifest

| Group | Exact path / action |
|---|---|
| renderer source | `scripts/export_cvf_remediation_receipt_log.py` |
| renderer source | `scripts/runtime_evidence_manifest/manifest_builder.py` |
| renderer source | `scripts/export_cvf_release_packet.py` |
| focused test | `governance/compat/test_system_chain_uc02_renderer_conformance.py` |
| family output | `docs/reviews/cvf_phase_governance/CVF_W4_PHASE_GOVERNANCE_EVIDENCE_2026-03-07.json` |
| family output | `docs/reviews/cvf_phase_governance/CVF_W4_PHASE_GOVERNANCE_LOG_2026-03-07.md` |
| family output | `docs/reviews/cvf_phase_governance/CVF_W4_SKILL_GOVERNANCE_EVIDENCE_2026-03-07.json` |
| family output | `docs/reviews/cvf_phase_governance/CVF_W4_SKILL_GOVERNANCE_LOG_2026-03-07.md` |
| family output | `docs/reviews/cvf_phase_governance/CVF_W4_GOVERNANCE_ENGINE_EVIDENCE_2026-03-07.json` |
| family output | `docs/reviews/cvf_phase_governance/CVF_W4_GOVERNANCE_ENGINE_LOG_2026-03-07.md` |
| family output | `docs/reviews/cvf_phase_governance/CVF_W4_AGENT_PLATFORM_GOVERNANCE_EVIDENCE_2026-03-07.json` |
| family output | `docs/reviews/cvf_phase_governance/CVF_W4_AGENT_PLATFORM_GOVERNANCE_LOG_2026-03-07.md` |
| family output | `docs/reviews/cvf_phase_governance/CVF_W4_SAFETY_HARDENING_ROLLBACK_EVIDENCE_2026-03-07.json` |
| family output | `docs/reviews/cvf_phase_governance/CVF_W4_SAFETY_HARDENING_ROLLBACK_LOG_2026-03-07.md` |
| family output | `docs/reviews/cvf_phase_governance/CVF_W4_RUNTIME_ADAPTER_HUB_REMEDIATION_RECEIPTS_2026-03-07.json` |
| family output | `docs/reviews/cvf_phase_governance/CVF_W4_RUNTIME_ADAPTER_HUB_REMEDIATION_RECEIPT_LOG_2026-03-07.md` |
| family output | `docs/reviews/cvf_phase_governance/CVF_W4_SAFETY_RUNTIME_SESSION_EVIDENCE_2026-03-07.json` |
| family output | `docs/reviews/cvf_phase_governance/CVF_W4_SAFETY_RUNTIME_SESSION_LOG_2026-03-07.md` |
| manifest output | `docs/reviews/cvf_phase_governance/CVF_W4_MULTI_RUNTIME_EVIDENCE_MANIFEST_2026-03-07.json` |
| manifest output | `docs/reviews/cvf_phase_governance/CVF_W4_MULTI_RUNTIME_EVIDENCE_LOG_2026-03-07.md` |
| packet output | `docs/reviews/cvf_phase_governance/CVF_RELEASE_APPROVAL_PACKET_LOCAL_BASELINE_2026-03-07.md` |
| packet output | `docs/reviews/cvf_phase_governance/CVF_RELEASE_REVIEW_PACKET_PRODUCTION_CANDIDATE_2026-03-07.md` |
| packet output | `docs/reviews/cvf_phase_governance/CVF_INTERNAL_AUDIT_PACKET_2026-03-07.md` |
| packet output | `docs/reviews/cvf_phase_governance/CVF_ENTERPRISE_ONBOARDING_PACKET_2026-03-07.md` |
| worker return | `docs/reviews/CVF_SYSTEM_CHAIN_UC02_RENDERER_CONFORMANCE_REPAIR_WORKER_RETURN_2026-07-14.md` |

## Write Ownership

Worker owns only the manifest above and must not commit. Reviewer owns GAP,
coverage/roadmap confirmation, completion review, commit, and session sync.

## Dual Agent Surface Matrix

| Surface class | Interface | Authority/risk boundary | Required evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | local Python source/tests/release gate | exact manifest, no commit | tests, regenerated outputs, gates | existing local subprocess only | AUTHORIZED_BOUNDED |
| `EXTERNAL_AGENT_CLI_MCP` | N/A with reason: no external route | outside scope | zero invocation | no adapter implied | DEFERRED_NOT_REQUIRED |

## Acceptance Criteria

- All three renderer families pass focused structural and negative tests.
- Twelve Markdown outputs pass four named governance checkers.
- Release gate regenerates 20 outputs once; optional retry count no more than one.
- UC-02 proof-run/scenario/provider counts remain zero.
- No evidence value, semantic verdict, coverage, GAP, roadmap, or session edit.
- Worker-return fast gate passes and HEAD is unchanged.

## Evidence Requirements

- exact execution base and before/after `git status --short`;
- source diff for the three renderer owners and focused test;
- focused-test and existing archive-path-test command outputs;
- one release-gate invocation receipt and exact 20-output changed inventory;
- four checker results for all twelve Markdown outputs;
- explicit counts for release-gate retries, UC-02 calls, scenario events, and
  provider calls;
- worker-return fast-gate result and unchanged-HEAD proof.

## Verification Commands

```text
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python -m unittest governance.compat.test_system_chain_uc02_renderer_conformance
python -m unittest governance.compat.test_system_chain_uc02_archive_path_reconciliation
python scripts/run_cvf_runtime_evidence_release_gate.py
python governance/compat/run_worker_return_fast_gate.py --help
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
git rev-parse --short HEAD
```

The worker must read `--help` and use any required path/range arguments exposed
by the current worker-return gate; an individual checker is not a substitute.

## Review Gate

Reviewer independently verifies the exact changed set, reruns focused and
archive-path tests, validates all twelve Markdown outputs, confirms the call
counters, and runs pre-closure before changing GAP or session state.

## Fail Conditions

Fourth source owner, direct generated-output hand editing, checker weakening,
fabricated verification evidence, UC-02/provider call, unexpected path, second
retry, secret leakage, or stronger claim returns `BLOCKED_WITH_REASON`.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every acceptance criterion and the
worker-return fast gate pass with HEAD unchanged. Otherwise return
`BLOCKED_WITH_REASON` with the first classified blocker, safe diagnostics, and
no additional regeneration attempt beyond the authorized maximum.

## Closure Checklist

- [ ] Source ownership refreshed at execution base.
- [ ] Only the exact fulfillment manifest changed.
- [ ] Focused and archive-path tests passed.
- [ ] Twenty outputs regenerated through the release gate.
- [ ] Twelve Markdown outputs passed applicable checkers.
- [ ] UC-02, scenario-event, and provider-call counts are zero.
- [ ] Worker-return fast gate passed and HEAD stayed unchanged.
- [ ] Reviewer converted the no-commit return into governed closure.

## Worker Autonomy / No-Question Rule

Repair allowed-scope source/test/template defects directly. Do not ask whether
to repair machine-gate failures inside scope. Stop only at a forbidden boundary.

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Work-order control | Evidence |
|---|---|---|
| preserve accepted UC-02 | zero proof calls | command inventory |
| repair renderer GAP | exact three owners | source diff/tests |
| regenerate without scenario run | release gate only | 20 outputs |
| close learning loop | reviewer-owned GAP closure | completion review |

## Cost And Retry Control

UC-02 calls 0; scenario events 0; provider calls 0; release-gate calls 1 planned;
one diagnosed result-changing regeneration retry maximum.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit implementation worker then reviewer/closer |
| phase | renderer repair, regeneration, and worker return |
| baseHeadFor(phase) | dispatchBaseHead=`ef38f567e`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | exact Planned Worker Fulfillment Manifest |
| traceScope(phase, actor) | worker records source refresh, tests, regeneration calls, zero UC-02/provider calls, outputs, gates, diff, HEAD |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer commits |
| crossBatchIsolation | clean worktree confirmed at dispatch; all non-manifest paths read-only |
| nextMoveSurfaces | reviewer updates GAP/session only after accepted completion |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SYSTEM_CHAIN_UC02_RENDERER_CONFORMANCE_REPAIR_COMPLETION_2026-07-14.md` |
| reviewerOwnedClosurePaths | completion review; paired packet status; renderer GAP/index/README; session sources |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SYSTEM_CHAIN_UC02_RENDERER_CONFORMANCE_REPAIR_WORKER_RETURN_2026-07-14.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake route | system-chain renderer repair |
| canonical route mode | `SINGLE_AGENT_SINGLE_ROLE` |
| Selected role route | dispatcher -> no-commit worker -> reviewer/closer |
| scope classification | local source/test/regeneration repair |
| risk sensitivity | R1 provider-free |
| escalation condition | forbidden owner/path, UC-02/provider need, second retry |
| Dispatcher role | dispatcher role |
| Worker route | `WORKER_MUST_NOT_COMMIT` |
| Reviewer/closer route | after worker return |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | local runtime-generated evidence repair |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | three source-verified renderer owners |
| Disposition | CVF_SOURCE_VERIFIED_REPAIR |
| Claim boundary | no external authority or provider memory |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_SYSTEM_CHAIN_UC02_CURRENT_RERUN_COMPLETION_2026-07-14.md`

priorVerificationAnchor: material commit `9173af70b`

freshRecomputeRequired: yes; template ownership corrected before dispatch

unicodePathHandling: literal paths and UTF-8 readers; generated governed prose defaults ASCII

extractedTextAuthority: N/A with reason: no OCR/extraction input

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-repair`, role=`dispatcher`, lifecyclePhase=`dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class runtime-repair --role dispatcher --lifecycle-phase dispatch --surface-selector system-chain --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Commit Prompt Readiness

| Field | Value |
|---|---|
| workerCommitPrompt | FORBIDDEN |
| reviewerMaterialCommit | after accepted review only |
| sessionSyncCommit | separate following material closure |
| changedSetEvidence | manifest, diff/status, regeneration inventory |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `Source Verification Block`; `Current Runtime Freshness Verification`; `Planned Worker Fulfillment Manifest`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Public Export Disposition` |
| gateRunPurpose | confirmation after direct renderer-owner verification; not first discovery |
| claimBoundary | exact no-commit renderer repair |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` |
| generatedProfile | work-order full dispatch |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | source-verified manual authoring |
| checkerReadAheadConfirmation | checker sources/gotchas read first |
| docOnlyNewFields | N/A with reason: none |
| claimBoundary | dispatch only |

## Foundation Storage Layout Block

Existing renderer owners and phase-governance output root are reused. No new
stable package, registry, runtime owner, or public surface is created.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: internal private-provenance repair.

## Claim Boundary

Passing this repair proves generated Markdown conformance only. UC-02 remains
bounded by its retained receipt; no provider, production, public, scale,
certification, or user-value claim is added.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer role |
| Provider or surface | local private provenance repository |
| Session or invocation | SCLP-UC02-R3 dispatch, 2026-07-14 |
| Working directory | repository root |
| Command or tool surface | reads, rg, apply_patch, GAP generator, dispatch gates |
| Target paths | owner correction, paired baseline/work order |
| Allowed scope source | active session nextAllowedMove |
| Before status evidence | clean worktree at HEAD `ef38f567e` |
| After status evidence | source-verified dispatch packet |
| Diff evidence | dispatch diff before commit |
| Approval boundary | packet authoring and one no-commit worker |
| Claim boundary | no implementation, regeneration, UC-02, provider, public, or session edit |
| Agent type | dispatcher/reviewer |
| Invocation ID | system-chain-uc02-r3-work-order-2026-07-14 |
| Expected manifest | correction artifacts plus paired packet |
| Actual changed set | recomputed before commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Operator Checkpoint

N/A with reason: this dispatch requires no human decision. Any forbidden
boundary is returned with evidence under the stated return conditions.

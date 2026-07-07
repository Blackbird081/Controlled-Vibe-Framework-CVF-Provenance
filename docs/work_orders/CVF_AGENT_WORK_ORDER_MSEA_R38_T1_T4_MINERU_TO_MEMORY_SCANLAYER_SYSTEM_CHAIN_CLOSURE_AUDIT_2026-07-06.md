# CVF Agent Work Order - MSEA R38 T1-T4 MinerU To Memory ScanLayer System Chain Closure Audit

Memory class: governed-work-order

Status: CLOSED

Created: 2026-07-06

rawMemoryReleased: false

## Dispatch Prompt Envelope

dispatchId: MSEA-R38-T1-T4-MINERU-TO-MEMORY-SCANLAYER-SYSTEM-CHAIN-CLOSURE-AUDIT

route: WORKER_MUST_NOT_COMMIT

taskClass: System-chain audit / release-boundary decision

role: worker

dispatchBaseHead: `aeaadccf9`

executionBaseHead: WORKER_CAPTURE_AT_START

closureBaseHead: REVIEWER_SET_AT_CLOSURE

Commit mode: WORKER_MUST_NOT_COMMIT

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R38_T1_T4_MINERU_TO_MEMORY_SCANLAYER_SYSTEM_CHAIN_CLOSURE_AUDIT_2026-07-06.md`

Current-time notes: Artifact date is 2026-07-06. The provenance
workspace is clean at dispatch base `aeaadccf9`. R37 public catalog
hygiene has been pushed to the public repository and provenance branch,
leaving the next meaningful product question focused on whether the
MinerU output, memory, and scan-layer surfaces form a complete CVF
system or remain foundation-only.

Do-not-misread notes: This work order authorizes docs-only audit and
decision artifacts. It does not authorize source/test edits, runtime
wiring, MinerU runtime execution, provider/live proof, private/generated
content reads, memory/RAG writes, file-backed production persistence,
public-sync, use-case/legal workflow, extraction-truth claims, current-law
claims, worker commit, or push.

Required first actions: read this work order, the paired GC-018 baseline,
the mandatory startup and guard-orientation files named below, then
recompute source anchors from the cited current source and prior closed
artifacts before writing any R38 output.

Return contract: create the four required R38 reference artifacts and one
worker-return artifact, run the worker-return fast gate and pre-closure
quality checks, record exact command evidence including final
`git status --short --untracked-files=all`, disclose any provider-local or
IDE side-channel files, and stop for reviewer closure. Do not commit.

workerTargetPaths:

- `docs/reference/CVF_MSEA_R38_T1_MINERU_TO_MEMORY_SCANLAYER_CURRENT_CHAIN_MAP_2026-07-06.md`
- `docs/reference/CVF_MSEA_R38_T2_MINERU_TO_MEMORY_SCANLAYER_GAP_CLASSIFICATION_2026-07-06.md`
- `docs/reference/CVF_MSEA_R38_T3_MINERU_TO_MEMORY_SCANLAYER_MINIMAL_E2E_HARNESS_DECISION_2026-07-06.md`
- `docs/reference/CVF_MSEA_R38_T4_MINERU_TO_MEMORY_SCANLAYER_RELEASE_GATE_DECISION_2026-07-06.md`

workerReturnPath:

- `docs/reviews/CVF_MSEA_R38_T1_T4_MINERU_TO_MEMORY_SCANLAYER_SYSTEM_CHAIN_CLOSURE_AUDIT_WORKER_RETURN_2026-07-06.md`

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| intake summary | Operator asked for a T1-T4 work order after clarifying that the main concern is whether MinerU/Memory/scanlayer has become one coherent CVF system |
| scope classification | Docs-only system-chain audit and release-boundary decision |
| risk sensitivity | Medium: source facts span Python, TypeScript, scan-layer, memory candidate, and prior release-boundary artifacts; overclaiming production readiness is the primary risk |
| selected role route | routeMode: MULTI_AGENT_SINGLE_ROLE |
| role separation basis | Dispatcher authors this packet; one worker executes the four audit/decision tranches without commit; reviewer/closer owns closure conversion and commit |
| escalation condition | Return to orchestrator if source anchors conflict, if a held production lane appears to require actual runtime execution to classify, if private/generated content would need to be read, or if any artifact would imply use-case/legal/product-readiness claims |

## Worker Autonomy / No-Question Rule

The worker may proceed without asking wording or preference questions. The
worker must stop and return `BLOCKED_WITH_REASON` if the audit cannot
answer from current repository source and governed artifacts alone.

The worker must not open a broader product/use-case roadmap. If T4
recommends a future tranche, it must name the smallest source-verified next
packet, not execute it.

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Dispatcher | Authored this GC-018/source-verified R38 T1-T4 work order and paired baseline |
| Worker | Creates R38 T1-T4 reference artifacts and worker return; does not commit |
| Reviewer/closer | Reviews worker return, repairs only within scope if needed, runs closure gates, and owns material closure commit |
| Session-sync steward | Updates session surfaces when reviewer acceptance changes current mode or next allowed move |

## Purpose

Determine, with source verification and without use-case expansion, whether
the MinerU output chain, memory candidate chain, and scan-layer surfaces
currently form a complete CVF system or a bounded foundation/internal
system-chain that still needs one or more release gates.

## Authority Chain

| Authority | Role in R38 |
| --- | --- |
| Paired GC-018 baseline | Authorizes docs-only R38 T1-T4 audit and decision work |
| R33 T5 completion review | Establishes bounded internal system-chain readiness and keeps production/private/provider/use-case boundaries held |
| R34 T2 decision matrix | Stops the foundation lane until an operator names a priority and keeps production memory/RAG and persistence lanes held |
| R35 T2 capability snapshot | Classifies the MinerU chain as foundation-only, not production-usable |
| Current source surfaces | Provide direct runtime/source anchors for receipt writer, scan route, durable-store invocation candidate, memory/RAG candidate, route candidate, harness, and bridge |
| ADIF-0024 | Requires final evidence reruns and workspace hygiene disclosure |

## Roadmap-To-Work-Order Trace Matrix

| Driver | Work-order requirement | Disposition |
| --- | --- | --- |
| Operator request for T1-T4 | Dispatch one four-tranche packet, not an open-ended roadmap | SATISFIED_BY_THIS_PACKET |
| Operator concern about whether MinerU/Memory/scanlayer is a system | T1 maps current chain; T2 classifies gaps; T3 decides whether a minimal proof is still valuable; T4 selects next release gate | SATISFIED_BY_T1_T4 |
| Operator warning not to lurch into use case | Forbidden Scope excludes use-case/legal/extraction-truth/current-law workflow and T4 may only recommend a separately authorized future packet | SATISFIED_BY_BOUNDARY |
| R34/R35 foundation-only evidence | Worker must treat current MinerU chain as bounded unless source recomputation proves otherwise | SATISFIED_BY_SOURCE_VERIFICATION |

## Operator Checkpoint

No additional operator input is required for this dispatch. The operator's
current instruction authorizes authoring this T1-T4 work order only. A
future implementation, runtime proof, memory write, public-sync, or
use-case/legal lane still requires a fresh explicit operator-selected
packet.

## Pre-flight Checks

| Check | Required worker evidence |
| --- | --- |
| Worktree before edits | `git status --short --untracked-files=all` from the provenance workspace |
| Dispatch base capture | `git rev-parse --short HEAD` at worker start |
| Source-anchor recompute | Fresh `rg -n` or equivalent source reads for each runtime/source symbol cited in this packet |
| Path collision check | Confirm all five worker target paths do not already exist before writing |
| Provider-local hygiene | Inspect and disclose provider-local or IDE side-channel files; do not create or leave stray provider-local files |

## Write Ownership

| Surface | Owner |
| --- | --- |
| R38 T1-T4 reference artifacts | Worker may create |
| R38 worker return | Worker may create |
| Source files and tests | Not worker-owned |
| Session state, handoff, session memory | Not worker-owned in this worker phase |
| Public-sync clone or public catalog | Not worker-owned |
| Provider-local configuration or memory files | Not worker-owned; do not create, stage, or rely on them as authority |

## Required First Reads

Before writing any worker artifact, read:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- active handoff named by session state
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/baselines/CVF_GC018_MSEA_R38_T1_T4_MINERU_TO_MEMORY_SCANLAYER_SYSTEM_CHAIN_CLOSURE_AUDIT_2026-07-06.md`
- this work order
- `docs/reviews/CVF_MSEA_R33_T5_MINERU_INTERNAL_SYSTEM_CHAIN_COMPLETION_2026-07-05.md`
- `docs/reference/CVF_MSEA_R34_T2_MINERU_FOUNDATION_LANE_STOP_OR_NARROW_RELEASE_DECISION_MATRIX_2026-07-05.md`
- `docs/reference/CVF_MSEA_R35_T2_CVF_CURRENT_PRODUCT_CAPABILITY_SNAPSHOT_2026-07-05.md`
- current runtime/source files cited in the Source Verification Block

## Mission

Create a source-verified answer packet for the MinerU-to-memory/scanlayer
system status:

1. T1 maps the current chain and shows which links are source-backed,
   test/fixture-backed, internal-only, or held.
2. T2 classifies the remaining gaps by authority type and value.
3. T3 decides whether a minimal E2E harness/proof is still worth opening,
   without executing it.
4. T4 converts the audit into a release-gate recommendation and exact next
   allowed move.

## Allowed Scope

You may create only:

- `docs/reference/CVF_MSEA_R38_T1_MINERU_TO_MEMORY_SCANLAYER_CURRENT_CHAIN_MAP_2026-07-06.md`
- `docs/reference/CVF_MSEA_R38_T2_MINERU_TO_MEMORY_SCANLAYER_GAP_CLASSIFICATION_2026-07-06.md`
- `docs/reference/CVF_MSEA_R38_T3_MINERU_TO_MEMORY_SCANLAYER_MINIMAL_E2E_HARNESS_DECISION_2026-07-06.md`
- `docs/reference/CVF_MSEA_R38_T4_MINERU_TO_MEMORY_SCANLAYER_RELEASE_GATE_DECISION_2026-07-06.md`
- `docs/reviews/CVF_MSEA_R38_T1_T4_MINERU_TO_MEMORY_SCANLAYER_SYSTEM_CHAIN_CLOSURE_AUDIT_WORKER_RETURN_2026-07-06.md`

### T1 Requirements

T1 must include:

- a source-verified chain map from receipt writer to scan-layer surfaces,
  durable-store invocation candidate, memory/RAG route candidate,
  system-chain route candidate, internal harness, and Python receipt bridge;
- a status column using only `SOURCE_EXISTS`, `IMPLEMENTED_INTERNAL`,
  `FIXTURE_ONLY`, `HELD_NOT_RELEASED`, `SOURCE_MISSING_BLOCKER`, or
  `SCOPE_EXCLUDED`;
- a boundary column naming whether each link is production, foundation-only,
  internal-only, fixture-only, or held.

### T2 Requirements

T2 must include:

- a gap classification table with gap type, source evidence, authority
  needed, and value;
- separate rows for production memory/RAG route release, file-backed
  persistence, provider/live proof, scan-layer integration, private-output
  policy, public/runtime claim, and use-case/legal workflow;
- an explicit no-lane-deepening rule for low-value or use-case/legal gaps.

### T3 Requirements

T3 must decide exactly one of:

- `MINIMAL_E2E_HARNESS_PACKET_RECOMMENDED`
- `NO_ADDITIONAL_HARNESS_VALUE_STOP`
- `BLOCKED_PENDING_OPERATOR_RELEASE_LANE_SELECTION`

If a harness packet is recommended, T3 may specify only a future
source-verified proof design. It must not run tests, execute providers, read
private/generated output, or author source/test changes.

### T4 Requirements

T4 must decide exactly one of:

- `SYSTEM_FOUNDATION_COMPLETE_STOP`
- `NARROW_RELEASE_PROOF_WORK_ORDER_READY`
- `PRODUCTION_AUTHORITY_PACKET_REQUIRED`
- `USE_CASE_LANE_PARKED_NO_CURRENT_VALUE`
- `BLOCKED_SOURCE_CONFLICT`

T4 must include exact next-move text suitable for session surfaces after
reviewer closure. It must not claim production readiness unless a current
source-verified, accepted closure artifact already proves it.

## Forbidden Scope

Do not:

- edit source, tests, generated JSON aggregates, session state, active
  handoff, public-sync files, or provider-local files;
- run MinerU runtime, providers, browser proof, live governance proof,
  retrieval, vectorization, production durable-store invocation, or
  file-backed production persistence;
- read, quote, summarize, copy, import, stage, or commit private/generated
  MinerU output content;
- claim extraction accuracy, document truth, legal quality, current-law
  correctness, hosted readiness, public readiness, or production readiness;
- open or execute a use-case/legal workflow;
- create a public claim, public-sync batch, worker commit, or push.

## Execution Plan

1. Capture clean pre-flight status and base head.
2. Re-read all required first-read documents and current source anchors.
3. Create T1 chain map from direct source and accepted closure evidence.
4. Create T2 gap classification with held-lane authority and value.
5. Create T3 minimal harness decision without executing a harness.
6. Create T4 release-gate decision and next-move recommendation.
7. Create worker return with evidence, gate results, no-stray disclosure,
   and changed-file list.
8. Run required gates and stop for reviewer closure without committing.

## Evidence Requirements

Worker return must include:

- Roadmap-To-Work-Order Trace Matrix or direct operator-request trace;
- Source Verification Block for all source/runtime symbols and prior
  closure facts used;
- ADIF Defect Registry Disclosure;
- Checker Source Read-Ahead Block;
- Worker Output Quality Controls;
- Provider-Local Stray Artifact Control;
- Pylance Static-Analysis Diagnostic Boundary;
- Agent Operation Trace Block;
- Delta Execution Claim Boundary Control Block;
- Public Export Disposition;
- exact `git diff --name-status` and `git status --short --untracked-files=all`
  evidence after final edits.

## Verification Commands

Run from the provenance workspace after the worker artifacts are written:

```bash
python governance/compat/run_worker_return_fast_gate.py --path docs/reviews/CVF_MSEA_R38_T1_T4_MINERU_TO_MEMORY_SCANLAYER_SYSTEM_CHAIN_CLOSURE_AUDIT_WORKER_RETURN_2026-07-06.md
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <workerBaseHead> --head HEAD
git diff --name-status <workerBaseHead>..HEAD
git status --short --untracked-files=all
```

If any gate fails, repair within allowed scope and rerun the same command.
Do not substitute individual checker lists for the full worker-return gate.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate:

`python governance/compat/run_worker_return_fast_gate.py --path docs/reviews/CVF_MSEA_R38_T1_T4_MINERU_TO_MEMORY_SCANLAYER_SYSTEM_CHAIN_CLOSURE_AUDIT_WORKER_RETURN_2026-07-06.md`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required worker-return sections:

- Status
- Target / Source
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Worker Output Quality Controls
- Provider-Local Stray Artifact Control
- Pylance Static-Analysis Diagnostic Boundary
- Source Verification Block
- ADIF Defect Registry Disclosure
- Checker Source Read-Ahead Block
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- Return-To-Orchestrator

## Worker Output Quality Controls

| Control | Required evidence |
| --- | --- |
| Final command rerun | Rerun verification commands after the final edit, not before |
| Worktree hygiene | Include exact final `git status --short --untracked-files=all`; untracked provider-local or IDE side-channel files must be removed, ignored only if already intended by repo policy, or disclosed as BLOCKED |
| Stray provider-local prevention | Do not leave files such as provider settings, model-switch side effects, or agent-local memory files outside manifest/ignore policy |
| Static-analysis boundary | Because this is docs-only, record `N/A with reason`; if any source/test file appears in diff, stop and return BLOCKED |
| Negative edge cases | T1-T4 must explicitly reject production overclaim, use-case/legal expansion, private-output read, file-backed persistence, and provider/live proof |

## Provider-Local Stray Artifact Control

Provider-specific or IDE side-channel files are execution aids only. They
must not be cited as CVF authority, staged, committed, or left as stray
worktree artifacts. If model/provider switching creates a local settings
file, the worker must remove it or record a blocker instead of silently
leaving it behind.

## Pylance Static-Analysis Diagnostic Boundary

This work order is docs-only. Pylance diagnostics are not expected. If the
worker touches Python or TypeScript files, the worker must stop and return
`BLOCKED_SCOPE_EXPANSION`.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| T1-T4 artifacts exist | All four reference artifacts are created at the exact target paths |
| Worker return exists | Worker return created at the exact target path |
| Source verification | Runtime/source symbols and prior closure facts are freshly verified |
| Claim boundary | No production, public, provider/live, private-output, use-case/legal, or extraction-truth claim |
| Value focus | T4 names the smallest valuable next packet or a stop disposition |
| Hygiene | Final status shows only allowed R38 artifacts and no stray provider-local files |
| Gates | Worker-return fast gate and pre-closure autorun pass, or worker returns BLOCKED with exact failing command and reason |

## Review Gate

Reviewer must not accept the worker return if:

- any target artifact claims production readiness or public/runtime release;
- any source/test/runtime/session/public-sync/provider-local file was edited;
- T3 executes a harness instead of deciding whether a future harness packet is
  valuable;
- T4 opens a use-case/legal workflow or buries the next move in vague prose;
- final evidence is stale or does not include final `git status --short
  --untracked-files=all`.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver query:

`python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json`

Disclosed defectIds:

- ADIF-0001
- ADIF-0002
- ADIF-0014
- ADIF-0015
- ADIF-0020
- ADIF-0021
- ADIF-0007
- ADIF-0016
- ADIF-0017
- ADIF-0024
- ADIF-0006

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | Status: CLOSED; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Verification Commands; Worker Return Packet Shape Contract; Worker Output Quality Controls; Provider-Local Stray Artifact Control; Pylance Static-Analysis Diagnostic Boundary; ADIF Defect Registry Disclosure; Source Verification Block; New Doc-Only Fields; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition |
| gateRunPurpose | confirm R38 dispatch artifact shape after checker source read-ahead |
| claimBoundary | checker read-ahead evidence only; no runtime, provider/live, public-sync, private-output, source/test, memory write, or production route release |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Python MinerU receipt writer defines the metadata receipt object and durable memory write adapter candidate builder | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 96, 198, and 779 | `build_mineru_durable_memory_write_adapter_candidate` | MinerU receipt writer | EXISTS | ACCEPT |
| Scan-layer route decision source defines document scan signals and route decision function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | lines 40 and 71 | `decide_scan_route` | scan route decision module | EXISTS | ACCEPT |
| Scan outcome report source defines report output and file writer | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | lines 43 and 274 | `write_scan_outcome_report_files` | scan outcome report module | EXISTS | ACCEPT |
| Durable-store invocation source exposes an implemented bounded invocation function and a no-memory-write authorization token | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 27, 30, 37, and 105 | `invokeMineruDurableStoreWrite` | durable-store invocation candidate | EXISTS | ACCEPT |
| Memory/RAG route release source exposes a bounded candidate function and not-production-authorized token | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 30, 33, and 93 | `releaseMineruMemoryRagRouteCandidate` | memory/RAG route release candidate | EXISTS | ACCEPT |
| System-chain route candidate source restricts persistence mode to in-process-only and keeps production route not released | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 25, 28, 34, and 78 | `buildMineruSystemChainRouteCandidate` | system-chain route candidate | VALUE_SET | ACCEPT |
| Internal system-chain harness source defines a bounded pass token and records Python receipt bridge not wired by R33 | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-internal-system-chain-harness.ts` | lines 32, 38, and 126 | `runMineruInternalSystemChainHarness` | internal system-chain harness | VALUE_SET | ACCEPT |
| Python receipt bridge source defines fixture-only proof and a not-production-wired hold token | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-python-receipt-bridge.ts` | lines 25, 28, and 188 | `mapMineruPythonReceiptFixtureToDurableStoreInvocationInput` | Python receipt bridge | VALUE_SET | ACCEPT |
| R33 closed the internal system-chain readiness audit bounded and kept the Python receipt bridge separate | `docs/reviews/CVF_MSEA_R33_T5_MINERU_INTERNAL_SYSTEM_CHAIN_COMPLETION_2026-07-05.md` | lines 45-52 and 230 | `R33_INTERNAL_SYSTEM_CHAIN_HARNESS_PASS_BOUNDED_PUBLIC_SAFE_SNAPSHOT_READY` | R33 completion review | VALUE_SET | ACCEPT |
| R34-T2 selected stopping the foundation lane until an operator names a priority, and kept production memory/RAG and file-backed persistence held | `docs/reference/CVF_MSEA_R34_T2_MINERU_FOUNDATION_LANE_STOP_OR_NARROW_RELEASE_DECISION_MATRIX_2026-07-05.md` | lines 47, 55-56, and 219 | `MINERU_FOUNDATION_PLANE_STOP_HERE_PENDING_OPERATOR_NEW_INITIATIVE` | R34-T2 decision matrix | VALUE_SET | ACCEPT |
| R35-T2 classified the MinerU chain as foundation-only and not production-usable | `docs/reference/CVF_MSEA_R35_T2_CVF_CURRENT_PRODUCT_CAPABILITY_SNAPSHOT_2026-07-05.md` | lines 61-63, 73-74, and 212-215 | foundation-only MinerU chain | R35-T2 capability snapshot | VALUE_SET | ACCEPT |

## New Doc-Only Fields

| Field / token | Purpose | Runtime status |
| --- | --- | --- |
| `SOURCE_EXISTS` | R38 T1 status taxonomy for source surfaces that exist but are not release evidence | DOC_ONLY_NEW |
| `IMPLEMENTED_INTERNAL` | R38 T1 status taxonomy for internally implemented bounded links | DOC_ONLY_NEW |
| `FIXTURE_ONLY` | R38 T1 status taxonomy for proof or bridge surfaces limited to fixtures | DOC_ONLY_NEW |
| `HELD_NOT_RELEASED` | R38 T1/T2 status taxonomy for lanes with explicit hold tokens or missing authority | DOC_ONLY_NEW |
| `SOURCE_MISSING_BLOCKER` | R38 T1/T2 status taxonomy for a missing source authority that blocks a claim | DOC_ONLY_NEW |
| `SCOPE_EXCLUDED` | R38 T1/T2 status taxonomy for a lane excluded by this packet | DOC_ONLY_NEW |
| `MINIMAL_E2E_HARNESS_PACKET_RECOMMENDED` | T3 decision token for a future narrow proof packet | DOC_ONLY_NEW |
| `SYSTEM_FOUNDATION_COMPLETE_STOP` | T4 decision token for stopping because foundation status is already sufficiently known | DOC_ONLY_NEW |
| `NARROW_RELEASE_PROOF_WORK_ORDER_READY` | T4 decision token for a future narrow release-proof work order | DOC_ONLY_NEW |
| `PRODUCTION_AUTHORITY_PACKET_REQUIRED` | T4 decision token for a future authority packet before production release | DOC_ONLY_NEW |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_MSEA_R33_T5_MINERU_INTERNAL_SYSTEM_CHAIN_COMPLETION_2026-07-05.md`; `docs/reference/CVF_MSEA_R34_T2_MINERU_FOUNDATION_LANE_STOP_OR_NARROW_RELEASE_DECISION_MATRIX_2026-07-05.md`; `docs/reference/CVF_MSEA_R35_T2_CVF_CURRENT_PRODUCT_CAPABILITY_SNAPSHOT_2026-07-05.md`

priorVerificationAnchor: R33 bounded internal readiness, R34 stop decision,
and R35 foundation-only classification

recomputeReason: R38 must answer the operator's current system-chain
question from fresh source anchors instead of reusing prior summary wording.

unicodePathHandling: Use repository-relative literal paths and UTF-8-safe readers; do not normalize workspace root Unicode or quote absolute local paths in worker artifacts.

extractedTextAuthority: N/A with reason

freshRecomputeRequired: YES

## Negative Search And Collision Discipline

| Field | Requirement |
| --- | --- |
| exact search roots | Worker must search current source files and cited governed docs, not provider-local memory |
| exact search command or query | Record `rg -n` commands or equivalent exact structured queries used for source symbols and hold tokens |
| coverage across source/tests/docs/JSON/external evidence | Source and governed docs are required; tests may be read for context only; external evidence is not authorized |
| same-token collision result | If a decision token appears in unrelated docs, record it as a collision and do not treat it as authority |
| absent-versus-collision disposition | Use `SOURCE_MISSING_BLOCKER` for true missing source authority; use a collision note for non-authoritative occurrences |
| collision tokens already expected | `FIXTURE_ONLY`, `RAG`, and `CVF_MSEA_R38` may appear elsewhere in the repository and are not authority unless cited in a Source Verification row |

## Work-Order Fulfillment Manifest

| Required artifact | Owner | Status at dispatch |
| --- | --- | --- |
| `docs/reference/CVF_MSEA_R38_T1_MINERU_TO_MEMORY_SCANLAYER_CURRENT_CHAIN_MAP_2026-07-06.md` | Worker | TO_CREATE |
| `docs/reference/CVF_MSEA_R38_T2_MINERU_TO_MEMORY_SCANLAYER_GAP_CLASSIFICATION_2026-07-06.md` | Worker | TO_CREATE |
| `docs/reference/CVF_MSEA_R38_T3_MINERU_TO_MEMORY_SCANLAYER_MINIMAL_E2E_HARNESS_DECISION_2026-07-06.md` | Worker | TO_CREATE |
| `docs/reference/CVF_MSEA_R38_T4_MINERU_TO_MEMORY_SCANLAYER_RELEASE_GATE_DECISION_2026-07-06.md` | Worker | TO_CREATE |
| `docs/reviews/CVF_MSEA_R38_T1_T4_MINERU_TO_MEMORY_SCANLAYER_SYSTEM_CHAIN_CLOSURE_AUDIT_WORKER_RETURN_2026-07-06.md` | Worker | TO_CREATE |

## Agent Operation Trace Block

| Trace field | Value |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local repo authoring surface |
| Session or invocation | MSEA-R38-T1-T4 dispatch authoring |
| Working directory | repository root |
| Command or tool surface | `rg`; `Get-Content`; `python governance/compat/run_adif_defect_resolver.py`; `apply_patch`; `python governance/compat/run_agent_autorun_workflow_gate.py` |
| Target paths | paired R38 GC-018 baseline and this work order |
| Allowed scope source | operator request plus paired GC-018 baseline |
| Before status evidence | clean worktree Before status evidence: `git status --short --branch --untracked-files=all` returned clean before dispatch authoring |
| After status evidence | pending dispatch artifacts only until committed by dispatcher |
| Diff evidence | `git status --short --untracked-files=all` and pre-dispatch autorun range evidence |
| Approval boundary | dispatcher may author and commit dispatch artifacts only |
| Claim boundary | no runtime commands, provider calls, MinerU execution, memory writes, public-sync, or source/test edits are authorized by this dispatch |
| Agent type | dispatcher |
| Invocation ID | MSEA-R38-T1-T4-DISPATCH-AUTHORING-2026-07-06 |
| Expected manifest | two dispatch artifacts: paired R38 GC-018 baseline and this work order |
| Actual changed set | to be confirmed by final `git status --short --untracked-files=all` before commit |
| Manifest delta | expected only until final gate confirms no extra paths |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldTool | manual scaffold from current work-order template and R35/R36/R37 dispatch packet shape |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R38-T1-T4 --title "MinerU To Memory ScanLayer System Chain Closure Audit" --date 2026-07-06 --base aeaadccf9 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic no-commit docs-only worker dispatch |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| scaffoldSource | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; recent R35/R36/R37 work-order shapes |
| scaffoldReason | R38 needs a bounded audit/decision packet, not a runtime implementation packet |
| manualEditsAfterScaffold | Filled envelope, authority chain, source verification, T1-T4 requirements, ADIF disclosure, worker-quality controls, handoff controls, and claim boundary |
| docOnlyNewFields | listed in New Doc-Only Fields |
| checkerReadAheadConfirmation | Checker sources listed in Checker Source Read-Ahead Block were read before authoring |
| claimBoundary | Dispatch scaffold provenance only; no runtime, provider/live, public-sync, private-output, source/test, memory write, or production route release |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Disposition |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher-authored work order to single no-commit worker executing four sequential docs-only tranches, then reviewer closure conversion |
| phase | dispatch |
| baseHeadFor(phase) | `dispatchBaseHead=aeaadccf9`; `executionBaseHead=WORKER_CAPTURE_AT_START`; `closureBaseHead=REVIEWER_SET_AT_CLOSURE` |
| changedSetScope(phase) | dispatch changes are this work order and paired R38 GC-018 baseline; worker changes are limited to the four R38 reference artifacts and worker return |
| traceScope(phase, actor) | dispatcher records source verification, ADIF, checker read-ahead, worker-quality controls, and no-runtime boundary; worker records execution commands and changed files; reviewer records closure diff and commit steward results |
| commitOwner(phase) | dispatcher may commit dispatch artifacts; worker must not commit; reviewer/closer owns material closure commit; session-sync steward owns continuity commit if required |
| crossBatchIsolation | R38 must not modify source/tests, existing R28-R37 artifacts, session state, active handoff, public-sync files, provider-local files, IDE config, checker/hook files, or private/generated output |
| nextMoveSurfaces | unchanged by worker; reviewer updates next-move surfaces when acceptance changes them |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R38_T1_T4_MINERU_TO_MEMORY_SCANLAYER_SYSTEM_CHAIN_CLOSURE_AUDIT_COMPLETION_2026-07-06.md`

reviewerOwnedClosurePaths:

- `docs/reference/CVF_MSEA_R38_T1_MINERU_TO_MEMORY_SCANLAYER_CURRENT_CHAIN_MAP_2026-07-06.md`
- `docs/reference/CVF_MSEA_R38_T2_MINERU_TO_MEMORY_SCANLAYER_GAP_CLASSIFICATION_2026-07-06.md`
- `docs/reference/CVF_MSEA_R38_T3_MINERU_TO_MEMORY_SCANLAYER_MINIMAL_E2E_HARNESS_DECISION_2026-07-06.md`
- `docs/reference/CVF_MSEA_R38_T4_MINERU_TO_MEMORY_SCANLAYER_RELEASE_GATE_DECISION_2026-07-06.md`
- `docs/reviews/CVF_MSEA_R38_T1_T4_MINERU_TO_MEMORY_SCANLAYER_SYSTEM_CHAIN_CLOSURE_AUDIT_WORKER_RETURN_2026-07-06.md`
- `docs/reviews/CVF_MSEA_R38_T1_T4_MINERU_TO_MEMORY_SCANLAYER_SYSTEM_CHAIN_CLOSURE_AUDIT_COMPLETION_2026-07-06.md`

## Closure Checklist

| Item | Required closure state |
| --- | --- |
| All T1-T4 artifacts created | PASS or BLOCKED with reason |
| Worker return created | PASS or BLOCKED with reason |
| Worker Output Quality Controls complete | PASS or BLOCKED with reason |
| No source/test/runtime/session/public/provider-local edits | PASS |
| Closure diff gate | PASS |
| Commit steward | PASS before reviewer commit |
| Session surfaces | Updated when reviewer acceptance changes next allowed move |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: R38 is private provenance system-chain audit and decision work. It
does not change public catalog content and does not create public runtime,
production-readiness, or hosted-readiness claims.

## External Knowledge Intake Routing

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external source is absorbed; operator instruction is local work selection only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order |
| Disposition | N/A with reason: R38 uses current repository source and governed artifacts only |
| Claim boundary | no external repository, public-web, current-law, or copied-source claim |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | docs-only R38 system-chain audit dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, production route release, memory-store write, RAG, or provider behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: this dispatch authorizes docs-only audit artifacts |
| invocationBoundary | no MinerU runtime, private-output, provider/live, public-sync, file-backed production store, retrieval, vectorization, or production memory/RAG route invocation |
| interceptionBoundary | no direct interception, mandatory wrapper, provider routing, or runtime enforcement claim |
| claimLanguage | boundary language only: audit, classify, decide, recommend future packet |
| forbiddenExpansion | no runtime/provider/live/public/package/Web/MCP/model-router/use-case/private-output/production behavior without fresh source-verified authorization |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Storage surface touched | Governed docs dispatch artifacts only |
| Durable store invoked | No |
| Foundation storage claim | R38 dispatch creates no runtime storage, memory record, vector index, retrieval store, file-backed production persistence, or durable-store receipt |
| Layout disposition | R38 worker outputs remain in `docs/reference` and `docs/reviews`; no source/runtime storage layout mutation is authorized |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this work order | `Status: CLOSED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MSEA_R38_T1_T4_MINERU_TO_MEMORY_SCANLAYER_SYSTEM_CHAIN_CLOSURE_AUDIT_COMPLETION_2026-07-06.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A | N/A with reason: R38 is a standalone operator-requested system-chain audit packet, not a roadmap-derived closure | N/A with reason |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | `python governance/compat/generate_corpus_scan_registry.py --check` PASS during worker-return fast gate | PASS |
| Registry Markdown | changed corpus registry coverage | reviewer-fast changed corpus registry coverage PASS | PASS |
| External evidence digest | N/A | N/A with reason: no external evidence artifact, public-web source, or local external file was absorbed | N/A with reason |
| System loop interlock | R38 T1-T4 worker artifacts and completion review | `SYSTEM_FOUNDATION_COMPLETE_STOP`; no further audit-only tranche | PASS |
| Session continuity | session state, session memory, and active handoff | dedicated session-sync commit required after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
| --- | --- | --- |
| No runtime receipt is accepted by this dispatch closure | R38 remains docs-only and accepts no MinerU runtime, provider/live, memory-write, public-sync, or production route receipt | PASS |
| Worker return accepted only after reviewer closure | Completion review path named above records `CLOSED_PASS_BOUNDED` | PASS |

## Claim Boundary

This work order dispatches only docs-only R38 T1-T4 audit and decision
work. It does not authorize source/test edits, MinerU runtime execution,
private/generated content reads, memory/RAG writes, file-backed production
persistence, provider/live proof, public-sync, use-case/legal workflow,
extraction-truth claims, current-law claims, public readiness, production
readiness, worker commit, or push.

# CVF Agent Work Order - WOAS-R7 Checker-Safe Worker Return Skeleton Generation

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: WOAS-R7

Dispatch base head: `cce7eec3`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated worker role

Reviewer/closer: reviewer/closer role

Worker return path: `docs/reviews/CVF_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_WORKER_RETURN_2026-07-01.md`

## Dispatch Prompt Envelope

Role: delegated worker for WOAS-R7.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_2026-07-01.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-01; dispatch base head is
`cce7eec3`.

Do-not-misread notes: this packet authorizes only local worker-return skeleton
helper/test/reference hardening. It does not authorize checker relaxation,
runtime/provider/live proof, real outside-source intake, public-sync,
Web/UI/dashboard, MCP/CLI adapter behavior, package lifecycle mutation,
model-router work, action authority, automatic invocation, or
production-readiness claims.

Required first actions: read required startup files, guard orientation,
literal-format gotchas, this packet, the paired GC-018 baseline, the WOAS
scaffold standard, the worker-return quality gate source, the scaffold helper
source, the worker-return skeleton helper source, and all checker source listed
in the Checker Source Read-Ahead Block before writing any artifact.

Return contract: create the worker return artifact at
`docs/reviews/CVF_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_WORKER_RETURN_2026-07-01.md`,
run required gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Harden the generated worker-return skeleton so future delegated workers begin
from a machine-shaped artifact that does not immediately fail the current
worker-return quality gate. This tranche should turn the WOAS-R3 opt-in
skeleton into a checker-safe starting document, reducing latency and repeated
literal-shape repairs in worker returns.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION --title "Checker-Safe Worker Return Skeleton Generation" --date 2026-07-01 --base cce7eec3 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | protected-governance-path plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled worker mission, source verification, dependency release evidence, protected-path authorization, fulfillment manifest, acceptance criteria, fail conditions, verification commands, and claim boundaries; removed unresolved scaffold markers from dispatch-ready fields. |
| checkerReadAheadConfirmation | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| docOnlyNewFields | None for dispatch. Worker may document helper-output terminology in the existing WOAS scaffold standard if needed. |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Authority Chain

| Authority | Evidence |
| --- | --- |
| Operator instruction | Operator agreed to the WOAS-R7 tranche from session-sync commit `cce7eec3` and asked for a work order. |
| Active session front door | `CVF_SESSION_MEMORY.md` and active state at session-sync commit `cce7eec3` point to operator selection. |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_2026-07-01.md` |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` |
| WOAS scaffold standard | `docs/reference/work_order_authoring/CVF_WOAS_R1_DISPATCH_PACKET_AUTHORING_SCAFFOLD_STANDARD.md` |
| Worker-return quality standard | `docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md` |
| Active handoff | `AGENT_HANDOFF_V30_2026-07-01.md` |

## Agent Roles

| Role | Responsibility |
| --- | --- |
| dispatcher | Author this GC-018/work-order pair and run pre-dispatch gates. |
| worker | Execute only the allowed helper/test/reference scope and create the worker return without committing. |
| reviewer/closer | Review worker return, repair only allowed-scope closure defects if needed, and own material commit if accepted. |
| session-sync steward | Update active state and handoff only if reviewer/closer creates an accepted material commit. |

## Required First Reads

| Path | Required action |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V30_2026-07-01.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/reference/work_order_authoring/CVF_WOAS_R1_DISPATCH_PACKET_AUTHORING_SCAFFOLD_STANDARD.md` | READ |
| `docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md` | READ |
| `governance/compat/check_worker_return_quality_gate.py` | SOURCE_VERIFIED |
| `governance/compat/build_dispatch_packet_scaffold.py` | SOURCE_VERIFIED |
| `governance/compat/build_worker_return_skeleton_scaffold.py` | SOURCE_VERIFIED |
| Applicable checker files listed in this packet's Checker Source Read-Ahead Block | READ |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, forbidden-scope need,
or missing authority that makes completion impossible.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance helper and worker-return artifact authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "governance helper and worker-return artifact authoring" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No resolver entries were returned for this exact query. Worker must still record any new repeated non-obvious defect pattern in ADIF before closure if one is found. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_source_intake_decision_packet_preflight.py` |
| literalTokensReviewed | `## Dispatch Prompt Envelope`; `Role:`; `Canonical packet:`; `Commit mode:`; `executionBaseHead`; `Return contract:`; `## Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `Source Verification Block`; `Claimed item`; `Source file`; `Verified line/section`; `Verified path or symbol`; `Owning interface/function/schema`; `Disposition`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Core Guard Self-Protection Authorization`; `WORKER_MUST_NOT_COMMIT`; `Self-declared worker-return artifact: yes`; `PLACEHOLDER_MARKERS`; `REQUIRED_HEADINGS`; `READ_AHEAD_FIELDS`; `AOT_FIELDS`; `DELTA_FIELDS`; `EXTERNAL_INPUT_CANONICAL`; `WORKER_MUST_NOT_COMMIT honored`; `## Delta Execution Claim Boundary Control Block`; `CLAIM_REJECTED`; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION`; `## Public Export Disposition`; `DEFERRED_PRIVATE_ONLY`; `Agent Operation Trace Block` |
| gateRunPurpose | Confirmation evidence, not first discovery; checker source and literal tokens were read before this work order was authored. |
| claimBoundary | Read-ahead evidence for this dispatch packet only; worker must repeat read-ahead for its own changed artifacts before implementation. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session permits operator selection of a next governed lane from session-sync commit `cce7eec3`. | EXISTS | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| Dispatch scaffold helper imports the worker-return skeleton builder and exposes the opt-in flag. | EXISTS | `governance/compat/build_dispatch_packet_scaffold.py` | lines 32, 752, and 810-811 | `build_worker_return_skeleton`; `--include-worker-return-skeleton` | dispatch scaffold helper | ACCEPT |
| Worker-return skeleton helper owns generated worker-return text. | EXISTS | `governance/compat/build_worker_return_skeleton_scaffold.py` | line 7 | `build_worker_return_skeleton` | worker-return skeleton helper | ACCEPT |
| Current worker-return skeleton output still contains gate-banned scaffold markers. | VALUE_SET | `governance/compat/build_worker_return_skeleton_scaffold.py` | lines 24, 26, 36-39, 43-60, and 110-118 | `FILL_ME`; `WORKER_MUST_CAPTURE_AT_START` | worker-return skeleton helper | ACCEPT |
| Worker-return quality gate bans those scaffold markers in eligible worker returns. | LITERAL_INVARIANT | `governance/compat/check_worker_return_quality_gate.py` | line 38 and lines 229-233 | `PLACEHOLDER_MARKERS`; `REQUIRED_HEADINGS` | worker-return quality gate | ACCEPT |
| Worker-return quality gate requires table field sets and canonical external input text. | LITERAL_INVARIANT | `governance/compat/check_worker_return_quality_gate.py` | lines 61-102 and lines 245-267 | `READ_AHEAD_FIELDS`; `AOT_FIELDS`; `DELTA_FIELDS`; `EXTERNAL_INPUT_CANONICAL` | worker-return quality gate | ACCEPT |
| Worker-return quality gate requires the no-commit statement token. | LITERAL_INVARIANT | `governance/compat/check_worker_return_quality_gate.py` | lines 278-279 | `WORKER_MUST_NOT_COMMIT honored` | worker-return quality gate | ACCEPT |
| Dispatch scaffold provenance checker fails dispatch-ready artifacts retaining scaffold markers in the provenance block. | LITERAL_INVARIANT | `governance/compat/check_dispatch_scaffold_provenance.py` | lines 24-48 and 192-198 | `REQUIRED_HEADING`; `REQUIRED_FIELDS`; `PLACEHOLDER_TOKENS`; `VALID_SKELETON_STATUSES` | dispatch scaffold provenance checker | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for baseline | `Test-Path docs/baselines/CVF_GC018_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_2026-07-01.md` returned `False` before authoring | PASS |
| Path existence for work order | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_2026-07-01.md` returned `False` before authoring | PASS |
| Path existence for planned worker return | `Test-Path docs/reviews/CVF_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_WORKER_RETURN_2026-07-01.md` returned `False` before authoring | PASS |
| Token collision search | `rg -n "WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION|Checker-Safe Worker Return Skeleton Generation" docs/baselines docs/work_orders docs/reviews governance/compat` returned no matches before authoring | PASS |
| Collision decision | No existing WOAS-R7 packet, work order, or worker return was found. | PASS |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| WOAS-R3 worker-return skeleton scaffold | Material commit `38765baf`; opt-in worker-return skeleton path exists. | R7 may harden the existing skeleton output without adding a new behavior surface. | SATISFIED |
| WOAS-R4 worker-return quality gate | Material commit `e6a56718`; gate defines the machine shape to satisfy. | R7 must align skeleton output with this gate and focused tests. | SATISFIED |
| WOAS-R5 scaffold provenance gate | Material commit `2835b1b5`; dispatch-ready packets must carry scaffold provenance. | R7 dispatch includes scaffold provenance evidence and uses the helper as starting point. | SATISFIED |
| WOAS-R6 checklist parity | Material commit `1c74075c`; standard/checklist parity is closed. | R7 may now improve generated worker-return skeleton quality instead of adding another checklist prose patch. | SATISFIED |
| Current active mode | Active session state at session-sync commit `cce7eec3` records operator selection as the next move. | Dispatch may proceed only as bounded helper/test/reference work. | SATISFIED |

## Commit Mode And Base-Anchor Lifecycle

| Field | Value |
| --- | --- |
| dispatchBaseHead | `cce7eec3` |
| executionBaseHead | Worker must capture with `git rev-parse --short HEAD` before edits. |
| closureBaseHead | Reviewer/closer sets this when reviewing the uncommitted worker return. |
| commitMode | WORKER_MUST_NOT_COMMIT |
| workerCommitPermission | FORBIDDEN |
| reviewerCommitOwner | reviewer/closer role only if the worker return is accepted |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher-authored packet to one worker role, then reviewer/closer conversion |
| phase | dispatch-to-worker |
| baseHeadFor(phase) | dispatchBaseHead=`cce7eec3`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Worker may change only the Allowed scope paths listed in this work order. |
| traceScope(phase, actor) | Worker return must include Agent Operation Trace Block with expected manifest, actual changed set, and manifest delta. |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns any material commit if the worker return is accepted. |
| crossBatchIsolation | WOAS-R7 only; no KIOD, Web, package, public-sync, MCP/CLI, runtime/provider, model-router, or session-sync work. |
| nextMoveSurfaces | Worker must not update next-move surfaces; reviewer/closer owns session-sync if closure is accepted. |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_COMPLETION_2026-07-01.md` optional; prefer repairing evidence in the worker return unless a separate completion review is needed for checker shape. |
| reviewerOwnedClosurePaths | `docs/baselines/CVF_GC018_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_2026-07-01.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_2026-07-01.md`; optional completion review path above |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |

## Pre-Flight Checks

Worker must capture `executionBaseHead` with `git rev-parse --short HEAD`
before edits, run `git status --short`, and read the checker sources named in
this packet before writing the first changed artifact.

## Write Ownership

Worker owns only the allowed paths listed below and must leave all changes
uncommitted. Reviewer/closer owns acceptance, material commit, and any
session-sync.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| Intake summary | Operator request: continue from WOAS-R6 into the next tranche that further reduces worker authoring defects by improving helper-generated forms. |
| Scope classification | Bounded allowed scope: worker-return skeleton helper, focused tests, existing golden fixture, optional existing reference standard wording, and one worker return. |
| Risk sensitivity | Low runtime risk but medium governance-shape risk because protected `governance/compat/` paths are authorized. |
| Selected role route | routeMode=`SINGLE_AGENT_SINGLE_ROLE`; one worker executes, then reviewer/closer converts if accepted. |
| Role separation basis | Worker must not commit; reviewer/closer owns review, material commit, and any session-sync. |
| Escalation condition | Escalate with `BLOCKED_WITH_REASON` for forbidden scope, missing authority, source contradiction, or gate failure outside allowed-scope repair. |

## Allowed Scope

Allowed scope:

- `docs/reference/work_order_authoring/CVF_WOAS_R1_DISPATCH_PACKET_AUTHORING_SCAFFOLD_STANDARD.md`
- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `governance/compat/fixtures/woas_r3_worker_return_skeleton_golden.md`
- `governance/compat/test_check_worker_return_quality_gate.py`
- `docs/reviews/CVF_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_WORKER_RETURN_2026-07-01.md`

Reviewer-owned closure paths:

- `docs/baselines/CVF_GC018_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_2026-07-01.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_2026-07-01.md`
- `docs/reviews/CVF_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_COMPLETION_2026-07-01.md`

## Forbidden Scope

Forbidden scope:

- Do not change worker-return quality gate semantics or weaken checker enforcement.
- Do not edit hook catalogs, autorun wiring, pre-commit/pre-push wiring, or add a new blocking checker.
- Do not edit `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V30_2026-07-01.md`, or archived handoffs.
- Do not perform real outside-source intake, source import, source-mirror mutation, source absorption, or package candidate admission.
- Do not edit Web/UI/dashboard code, MCP/CLI adapter code, package lifecycle state, provider registry, model-router code, or public-sync clone.
- Do not make runtime/provider/live-proof, action-authority, automatic-invocation, public-readiness, or production-readiness claims.
- Do not change default non-skeleton helper output unless focused tests prove the intentional delta and the reviewer can inspect it easily.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: WOAS-R7 helper/test change only; no guard
catalog wiring, no new blocking checker semantics, and no relaxation of
existing worker-return quality checks.

Protected paths:

- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `governance/compat/fixtures/woas_r3_worker_return_skeleton_golden.md`
- `governance/compat/test_check_worker_return_quality_gate.py`

Operator authorization: operator instructed the dispatcher to create WOAS-R7
from session-sync commit `cce7eec3` and accepted the helper-first
quality improvement lane.

Rollback boundary: reviewer/closer may reject the uncommitted worker return;
no protected-path change is committed unless reviewer accepts the WOAS-R7
material batch.

| Protected path | Authorized worker action |
| --- | --- |
| `governance/compat/build_worker_return_skeleton_scaffold.py` | Replace gate-banned scaffold marker text in generated worker-return skeleton with safe fillable guidance and gate-safe default values. |
| `governance/compat/build_dispatch_packet_scaffold.py` | Adjust only if CLI integration needs a narrow update to call or expose the safer skeleton output. |
| `governance/compat/test_build_dispatch_packet_scaffold.py` | Add or update focused tests proving deterministic CLI output, golden fixture parity, and quality-gate-safe skeleton shape. |
| `governance/compat/fixtures/woas_r3_worker_return_skeleton_golden.md` | Update golden output for the safer skeleton if helper output changes. |
| `governance/compat/test_check_worker_return_quality_gate.py` | Add focused regression coverage proving generated skeleton output passes the current worker-return quality gate, if this is the cleanest test location. |

Authorization boundary: only the protected helper/test/fixture paths above are
authorized. Session state, active handoff, public-sync, runtime/provider/live,
Web/UI, package, MCP/CLI, model-router, and production behavior are not
authorized.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `governance/compat/build_worker_return_skeleton_scaffold.py` | Make the generated skeleton checker-safe by construction against current `check_worker_return_quality_gate.py` requirements. |
| `governance/compat/build_dispatch_packet_scaffold.py` | Preserve opt-in CLI behavior and default dispatch output; touch only if needed for safe skeleton integration. |
| `governance/compat/test_build_dispatch_packet_scaffold.py` | Add or update focused helper/golden tests for safe skeleton output. |
| `governance/compat/fixtures/woas_r3_worker_return_skeleton_golden.md` | Update deterministic golden fixture if helper output changes. |
| `governance/compat/test_check_worker_return_quality_gate.py` | Add quality-gate regression coverage if needed to prove generated skeleton eligibility and compliance. |
| `docs/reference/work_order_authoring/CVF_WOAS_R1_DISPATCH_PACKET_AUTHORING_SCAFFOLD_STANDARD.md` | Update only if helper contract wording needs to reflect checker-safe worker-return skeleton generation. |
| `docs/reviews/CVF_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_WORKER_RETURN_2026-07-01.md` | Create worker return with required sections and command evidence; leave uncommitted. |

## Execution Plan

| Step | Required action | Evidence |
| --- | --- | --- |
| 1 | Capture `executionBaseHead` with `git rev-parse --short HEAD`, run `git status --short`, and read the required checker/source files before editing. | Worker return command evidence and Checker Source Read-Ahead Block. |
| 2 | Inspect current generated worker-return skeleton output and compare it to `check_worker_return_quality_gate.py` required headings, fields, canonical tokens, and banned scaffold markers. | Focused notes in worker return plus test assertions. |
| 3 | Patch only the allowed helper/test/fixture/reference paths needed to make generated skeleton output quality-gate-safe by construction. | `git diff --name-status` and focused test evidence. |
| 4 | Run focused unit tests and worker-return fast gate. | Command Evidence section in worker return. |
| 5 | Return uncommitted `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`; do not update session state or commit. | No-Commit Statement and `git status --short` evidence. |

## Evidence Requirements

| Evidence item | Required shape |
| --- | --- |
| Before-state evidence | `executionBaseHead` and initial `git status --short` captured before edits. |
| Source read-ahead evidence | Worker return lists checker/source files read before implementation, including `check_worker_return_quality_gate.py` and helper sources. |
| Skeleton compliance evidence | Test or diagnostic output proves generated worker-return skeleton has no banned scaffold marker and includes required headings/fields/tokens. |
| Default-output boundary evidence | Test or diff evidence shows non-skeleton dispatch helper output was not broadened, or names the exact intentional delta. |
| No-commit evidence | Worker return states `WORKER_MUST_NOT_COMMIT honored` and shows no worker commit was made. |

## Review Gate

Reviewer/closer must reject or return the worker output if any of these are
true:

- worker changed files outside Allowed Scope without a source-backed reason;
- worker weakened checker semantics instead of fixing helper output;
- worker return contains unresolved worker-return quality gate violations;
- command evidence omits focused helper tests or worker-return fast gate;
- worker made runtime/provider/public/Web/MCP/package/model-router claims.

Reviewer/closer may accept only after verifying the worker return and changed
set against this packet, then owns material commit and session-sync if accepted.

## Closure Checklist

- [x] Dispatch packet includes source verification and dependency-release evidence.
- [x] Dispatch packet includes Core Guard Self-Protection Authorization for protected paths.
- [x] Dispatch packet includes Worker Return Packet Shape Contract and reviewer conversion.
- [x] Dispatch packet forbids worker commit and session-sync mutation.
- [ ] Reviewer/closer reviews worker return.
- [ ] Reviewer/closer runs closure gates on the accepted changed set.
- [ ] Reviewer/closer commits material batch if accepted.
- [ ] Reviewer/closer performs session-sync after accepted material commit.

## Operator Checkpoint

Operator checkpoint: worker may proceed under `WORKER_MUST_NOT_COMMIT` using
this dispatch packet. Operator intervention is required only if the worker
needs forbidden scope, checker relaxation, runtime/provider/live proof,
public-sync, UI/Web/MCP/package/model-router work, or another source authority
not present in this work order.

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Planned durable reference folder | `docs/reference/work_order_authoring/` only if narrow standard wording is needed. |
| Planned front door/index | Existing work-order-authoring reference surface; no new front door or index is authorized. |
| Date policy | No new dated standard is required by default; optional edit must stay in the existing WOAS scaffold standard path named in Allowed Scope. |
| Owner surface | `docs/reference/work_order_authoring/`; `governance/compat/` helper/test surface. |
| Claim boundary | Helper/test/reference storage layout only; no runtime, public-sync, package, Web, MCP, model-router, or production storage claim. |

## Worker Return Packet Shape Contract

Worker return must be created at
`docs/reviews/CVF_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_WORKER_RETURN_2026-07-01.md`
and include:

- `Status`
- `dispatchWorkOrder`
- `Purpose`
- `Scope / Methodology`
- `Findings / Position`
- `Risk / Corrective Action`
- `Claim Boundary`
- `Agent Operation Trace Block`
- `Delta Execution Claim Boundary Control Block`
- `Public Export Disposition`
- `executionBaseHead`
- `git status --short`
- changed files
- command evidence
- no-commit statement

Worker return must also include these conditional sections, each filled with
evidence or `N/A with reason` / `NOT_APPLICABLE_WITH_REASON`:

- `External Knowledge Intake Routing`
- `Rescan Intelligence Hardening`
- `Corpus Completeness And Report Integrity`
- `Finding-To-Governance Learning Disposition`
- `Epistemic Process Block`
- `Machine Closure Package`

## Required Artifact Manifest

| Path | Required at handoff | Disposition |
| --- | --- | --- |
| `docs/reviews/CVF_WOAS_R7_CHECKER_SAFE_WORKER_RETURN_SKELETON_GENERATION_WORKER_RETURN_2026-07-01.md` | YES | Must be created and left uncommitted with `Status: COMPLETE_PENDING_REVIEW` or `Status: BLOCKED_WITH_REASON`. |
| `governance/compat/build_worker_return_skeleton_scaffold.py` | YES if implementation succeeds | Must remove generated gate traps without changing unrelated helper behavior. |
| `governance/compat/test_build_dispatch_packet_scaffold.py` | YES if implementation succeeds | Must prove deterministic safe skeleton output. |
| `governance/compat/fixtures/woas_r3_worker_return_skeleton_golden.md` | YES if helper output changes | Must match updated generated skeleton exactly. |
| `governance/compat/test_check_worker_return_quality_gate.py` | OPTIONAL | Use if direct quality-gate regression coverage belongs there. |
| `docs/reference/work_order_authoring/CVF_WOAS_R1_DISPATCH_PACKET_AUTHORING_SCAFFOLD_STANDARD.md` | OPTIONAL | Use only for narrow contract wording. |

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | Generated worker-return skeleton contains every required heading and table field currently enforced by `check_worker_return_quality_gate.py`. |
| AC2 | Generated worker-return skeleton contains neither banned scaffold marker from `PLACEHOLDER_MARKERS` in eligible worker-return text. |
| AC3 | Generated skeleton uses the canonical external input type exactly and retains `WORKER_MUST_NOT_COMMIT honored` in the no-commit statement. |
| AC4 | Generated skeleton uses an execution-base capture instruction that does not make an eligible worker-return file fail before the worker fills it. |
| AC5 | Focused tests prove the helper output passes `check_worker_return_quality_gate.diagnose(...)` or an equivalent direct worker-return quality-gate assertion. |
| AC6 | Focused tests or golden fixture prove the CLI opt-in output remains deterministic and that default dispatch helper output is not broadened. |
| AC7 | Worker return itself passes the worker-return fast gate and records any self-repaired checker-shape defects. |

## Fail Conditions

| Condition | Required response |
| --- | --- |
| Worker needs to change worker-return quality gate semantics to pass the skeleton. | Return `BLOCKED_WITH_REASON`; R7 is helper-output hardening, not checker relaxation. |
| Worker needs runtime/provider/live proof, public-sync, Web/UI/dashboard, MCP/CLI adapter behavior, package lifecycle mutation, model-router work, action authority, automatic invocation, or production-readiness work. | Return `BLOCKED_WITH_REASON`; fresh source-verified authorization is required. |
| Helper output change would alter non-worker-return dispatch baseline/work-order defaults without focused regression proof. | Repair in allowed scope or return `BLOCKED_WITH_REASON` with exact diff evidence. |
| A focused test cannot assert skeleton quality without importing private checker internals. | Use a public diagnostic function if available, or invoke the checker in a temporary-file test; document the chosen evidence path. |
| Worker return cannot satisfy quality gate shape. | Repair in allowed scope before return or return `BLOCKED_WITH_REASON` with exact failing checker evidence. |

## Verification Commands

Worker must run at minimum:

```text
python -m unittest governance.compat.test_build_dispatch_packet_scaffold governance.compat.test_check_worker_return_quality_gate -v
python governance/compat/check_worker_return_quality_gate.py --base cce7eec3 --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_build_dispatch_packet_scaffold.py --pytest-target governance/compat/test_check_worker_return_quality_gate.py
python governance/compat/run_agent_automation_assist.py --base cce7eec3 --head HEAD --json --enforce
```

Worker should add or adjust direct commands if source changes require a
different focused test path. Gate runs are confirmation evidence, not first
discovery.

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | WOAS-R7 authorizes local helper/test/reference work only. |
| requiredFutureAction | If a later packet adds runtime or provider behavior, create a fresh source-verified work order and live-proof plan. |
| providerRegistryBoundary | N/A with reason: no provider registry mutation or provider routing claim. |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: WOAS-R7 does not ingest or classify outside source material. |
| Matching local-view guard | N/A with reason: no outside-source local-view guard is needed for helper/test hardening. |
| Owner surface | `docs/reference/work_order_authoring/`; `governance/compat/` |
| Disposition | NOT_APPLICABLE_WITH_REASON: local worker-return skeleton helper/test tranche only. |
| Claim boundary | No outside-source intake, absorption, source import, source-mirror mutation, or external-agent output conversion is authorized. |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- Reason: WOAS-R7 does not rescan external repositories or corpus material.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no corpus scan or report integrity claim is made.

## Finding-To-Governance Learning Disposition

| Field | Value |
| --- | --- |
| Defect class | N/A_WITH_REASON: no new repeated defect class is asserted by dispatch. |
| Learning lane | N/A_WITH_REASON: worker must add ADIF only if implementation exposes a new repeated non-obvious pattern. |
| Finding | Generated worker-return skeleton currently includes gate-banned scaffold markers; this work order routes the known issue to helper hardening. |
| Disposition | ADAPT_DOC_ONLY: bounded helper/test correction under existing WOAS lane. |
| Runtime/provider/cost lane | N/A_WITH_REASON: no runtime, provider, or cost lane affected. |
| Next control action | Worker implements helper/test hardening and returns uncommitted evidence. |

## Epistemic Process Block

- Epistemic Process Applicability: BOUNDED_GOVERNANCE_IMPLEMENTATION
- Expected result / prediction: If generated skeleton avoids banned scaffold markers and keeps required headings/fields, quality-gate diagnostics should be clean for the skeleton fixture.
- Evidence Comparison: Worker must compare helper output against focused tests and quality-gate diagnostics.
- Contradiction or gap disposition: Repair allowed helper/test scope or return `BLOCKED_WITH_REASON` if checker semantics would need to change.
- Claim update: No runtime or production claim; only generated-artifact shape can be claimed.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | WOAS-R7 checker-safe worker-return skeleton generation work order |
| claimDisposition | CLAIM_REJECTED: this packet makes no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, or universal governed-coding-control claim. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed by this dispatch. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed by this dispatch. |
| invocationBoundary | Manual local helper/checker/test invocation only after worker implementation. |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | Helper skeleton output and focused local checker/test evidence only. |
| forbiddenExpansion | Runtime/provider/live/public/package/Web/MCP/model-router behavior requires fresh source-verified authorization. |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | WOAS-R7 checker-safe worker-return skeleton generation, 2026-07-01 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | shell, scaffold helper stdout, apply_patch, pre-dispatch gates |
| Target paths | this work order; paired WOAS-R7 baseline |
| Allowed scope source | current operator instruction to create WOAS-R7 from session-sync commit `cce7eec3` |
| Before status evidence | HEAD `cce7eec3`; worktree clean before dispatch authoring |
| After status evidence | pending pre-dispatch verification before material dispatch commit |
| Diff evidence | `git diff --name-status` before dispatch commit |
| Approval boundary | dispatch packet authoring only |
| Claim boundary | no runtime/provider/public/source-import/Web/MCP/model-router claim |
| Agent type | dispatcher |
| Invocation ID | `woas-r7-dispatch-2026-07-01` |
| Expected manifest | paired WOAS-R7 baseline; this work order |
| Actual changed set | to be verified before dispatch commit |
| Manifest delta | TO_VERIFY_BEFORE_COMMIT |
| Deletion or rename disposition | N/A with reason: no deletion or rename planned |

## Machine Closure Package

NOT_APPLICABLE_WITH_REASON: this is a dispatch-ready work order, not a
closed-equivalent completion packet. Reviewer/closer owns closure packaging
after worker return review.

## Claim Boundary

This work order authorizes local helper/test/reference hardening only. It does
not authorize real outside-source intake, public-sync, Web/UI/dashboard,
MCP/CLI adapter behavior, package lifecycle mutation, provider registry work,
model-router work, runtime/live proof, action authority, automatic invocation,
checker relaxation, or production-readiness claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet only; no public-sync artifact is
authorized by WOAS-R7.

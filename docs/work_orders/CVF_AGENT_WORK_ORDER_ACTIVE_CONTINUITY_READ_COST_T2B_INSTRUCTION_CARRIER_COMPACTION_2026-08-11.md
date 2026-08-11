# CVF Agent Work Order - Active Continuity T2B Instruction Carrier Compaction

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-08-11

Batch ID: ACRC-T2B

Risk ceiling: R2

Dispatch base head: `178c5e7e169c936e285f484de5abd8dae2e06c07`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated implementation worker

Reviewer/closer: independent reviewer/closer

Worker return path:
`docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2B_WORKER_RETURN_2026-08-11.md`

## Dispatch Prompt Envelope

Role: implementation worker for ACRC-T2B.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_CONTINUITY_READ_COST_T2B_INSTRUCTION_CARRIER_COMPACTION_2026-08-11.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker captures current HEAD before edits.

Current-time notes: T2A is accepted and parked; T2B alone is authorized.

Do-not-misread notes: do not modify an existing downstream project, full
active-state history, runtime/provider behavior, public-sync, deployment, or
any sixteenth worker path.

Required first actions: use progressive startup; read bootstrap, compact front
door, active handoff, this Work Order, paired GC-018, source/binding matrix,
guard orientation and literal gotchas. Read only applicable checker source
before writing its governed output.

Return contract: create the exact worker return, run required gates, leave all
changes uncommitted, and return `COMPLETE_PENDING_INDEPENDENT_REVIEW` or
`BLOCKED`.

## Purpose

Archive and compact the three instruction carriers without losing a binding
rule or direct machine token, then add bounded machine enforcement so the
startup-cost regression cannot silently recur.

## Authority Chain

1. The active-continuity roadmap defines T2B after accepted T2A.
2. T2A material and continuity closure are committed.
3. The operator explicitly selected T2B on 2026-08-11.
4. The source/binding matrix accounts for all current AGENTS headings and
   carrier readers before rewrite.
5. The paired GC-018 and this Work Order authorize exact-15 only.

## Agent Roles

| Role | Ownership |
|---|---|
| dispatcher/source reviewer | authors and releases the governed packet |
| implementation worker | changes exact-15 and returns uncommitted evidence |
| independent reviewer/closer | recomputes evidence and owns material closure |
| session-sync steward | updates continuity only after review disposition |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake summary | compact three instruction carriers while preserving all canonical rules and machine bindings |
| Scope classification | bounded R2 governance-source/checker implementation, exact-15, no commit |
| Risk sensitivity | medium governance risk because lost literals can silently weaken future agent routing; zero runtime/provider/public risk in scope |
| Selected role route | dispatcher/source reviewer -> implementation worker -> independent reviewer/closer -> session-sync steward |
| Route mode | `MULTI_AGENT_MULTI_ROLE` |
| Escalation condition | return `BLOCKED` for exact-15 insufficiency, source contradiction, archive mismatch, forbidden-path need, external effect, or semantic loss |

Route this packet to one `IMPLEMENTATION_WORKER` after dispatch release. Keep
review and closure with an independent `REVIEWER`/`CLOSER`; keep continuity
mutation with `SESSION_SYNC_STEWARD`. No role may absorb T3 or downstream work.

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
2. `CVF_SESSION_MEMORY.md`
3. the active handoff named by the bootstrap/current state
4. this Work Order
5. the paired GC-018 baseline
6. the T2B source/binding matrix
7. `docs/reference/guard_orientation/README.md`
8. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`

Use the full active-state aggregate only as a targeted lookup for a missing or
contradictory current fact.

## Pre-Flight Checks

Confirm packet hashes, clean execution HEAD, staged zero, all three carrier
preimage hashes, exact-15 collision state, no existing worker path outside the
manifest, and pre-implementation autorun PASS before material edits.

## Write Ownership

The worker owns exact-15 only and must not commit. Dispatcher packet,
completion review, roadmap closure, active-state fragments, generated state,
front door and active handoff remain reviewer/closer or session-steward owned.

## Execution Plan

1. Preserve all three preimages byte-for-byte at the authorized archives.
2. Build the routing index from the accepted heading/reader matrix.
3. Compact the three active carriers without weakening direct bindings.
4. Add the checker, focused tests and five command-chain bindings.
5. Run the required local proof, author the return, and stop uncommitted.

## Dependency Release Evidence

| Dependency | Artifact/commit | Final disposition |
|---|---|---|
| T2A accepted | T2A completion review; `fd4d61e73` | SATISFIED |
| T2A parked continuity | `e95fc658f`; `178c5e7e1` | SATISFIED |
| T2B source map | `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2B_SOURCE_BINDING_MATRIX_2026-08-11.md` | SOURCE_MAP_ACCEPTED_FOR_DISPATCH |
| operator checkpoint | explicit T2B selection on 2026-08-11 | SATISFIED |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work Order owner | Required evidence | Disposition |
|---|---|---|---|
| compact root AGENTS | Required Behavior 2-4 | budget, markers, semantic routing | MAPPED |
| compact provider-local CLAUDE | Required Behavior 2-4 | `NOT_CVF_SOURCE`, budget, markers | MAPPED |
| compact downstream template | Required Behavior 5 | doctor and golden harness | MAPPED |
| preserve every binding rule | source map plus routing index | 38-heading coverage | MAPPED |
| archive superseded full carriers | Required Behavior 1 | raw byte/hash equality | MAPPED |
| source/binding matrix before rewrite | prerequisite source map | accepted source map path | MAPPED |
| machine prevention | Required Behavior 6 | checker, tests, five bindings | MAPPED |
| no T3/runtime/external expansion | Scope Firewall | exact-15/no-sixteenth | MAPPED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| T2B sequence and scope exist | `docs/roadmaps/CVF_ACTIVE_CONTINUITY_READ_COST_REDUCTION_ROADMAP_2026-08-10.md` | lines 199-218 | `T2B` | roadmap | ACCEPT |
| stop on lost owner/binding/budget | `docs/roadmaps/CVF_ACTIVE_CONTINUITY_READ_COST_REDUCTION_ROADMAP_2026-08-10.md` | lines 264-265 | `Stop T2B` | roadmap stop conditions | ACCEPT |
| all current headings/readers are mapped | `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2B_SOURCE_BINDING_MATRIX_2026-08-11.md` | heading and reader matrices | `AGENTS Heading Binding Matrix`; `Machine Reader Matrix` | accepted source map | ACCEPT |
| current carrier hashes/sizes | `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2B_SOURCE_BINDING_MATRIX_2026-08-11.md` | Current Source Facts | three source paths | accepted source map | ACCEPT |
| Core router literals | `governance/compat/check_active_session_state.py` | lines 59-60, 92-95, 656-704 | `AGENT_ROUTER_MARKERS`; `_classify` | active-session checker | ACCEPT |
| public-export AGENTS binding | `governance/compat/check_public_export_disposition.py` | lines 223-227 | `AGENTS_PATH` | public-export checker | ACCEPT |
| corpus completeness carrier bindings | `governance/compat/check_corpus_completeness_report_integrity.py` | binding validation function | `AGENTS_PATH`; `CLAUDE_PATH` | corpus completeness checker | ACCEPT |
| corpus reconciliation carrier bindings | `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` | binding validation function | `AGENTS_PATH`; `CLAUDE_PATH` | corpus reconciliation checker | ACCEPT |
| workspace state AGENTS literals | `governance/compat/check_agent_workspace_state.py` | marker map | `AGENTS_PATH` marker tuple | workspace state checker | ACCEPT |
| workspace skeleton AGENTS literals | `governance/compat/check_agent_workspace_skeleton.py` | marker map | `AGENTS_PATH` marker tuple | workspace skeleton checker | ACCEPT |
| workspace runtime AGENTS literals | `governance/compat/check_agent_workspace_runtime_boundary.py` | marker map | `AGENTS_PATH` marker tuple | workspace runtime-boundary checker | ACCEPT |
| hook catalog ownership | `governance/compat/local_governance_hook_catalog.py` | `HOOK_CHAINS` | phase catalog imports | local hook chain | ACCEPT |
| autorun catalog ownership | `governance/compat/agent_autorun_command_catalog.py` | `_common_commands` | `_common_commands` | autorun workflow | ACCEPT |
| documentation CI command surface | `.github/workflows/documentation-testing.yml` | Python governance checker steps | workflow steps | documentation CI | ACCEPT |
| template writer | `scripts/new-cvf-workspace.ps1` | lines 343-413 | `$agentsTemplatePath` | downstream bootstrap writer | ACCEPT |
| downstream doctor contract | `scripts/check_cvf_workspace_agent_enforcement.ps1` | lines 407-440 | `requiredRoleTokens`; `rehydrationTokens` | workspace doctor | ACCEPT |
| golden carrier contract | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | lines 63-69 | `Test-CvfCarrierContent` | golden harness | ACCEPT |

## New Doc-Only Fields

| Field | Owner | Purpose |
|---|---|---|
| `carrierBudget` | new routing index | declare T2B line/byte limits |
| `preimageSha256` | new routing index | bind each byte-identical archive |
| `bindingClass` | new routing index | distinguish canonical route from direct literal |

## Exact Worker Changed Set

Use this one literal manifest for every scope comparison:

1. `AGENTS.md`
2. `CLAUDE.md`
3. `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`
4. `docs/reference/archive/AGENTS_FULL_PRE_T2B_2026-08-11.md`
5. `docs/reference/archive/CLAUDE_FULL_PRE_T2B_2026-08-11.md`
6. `docs/reference/archive/CVF_DOWNSTREAM_AGENTS_TEMPLATE_FULL_PRE_T2B_2026-08-11.md`
7. `docs/reference/CVF_AGENT_INSTRUCTION_CARRIER_ROUTING_INDEX_2026-08-11.md`
8. `governance/compat/check_agent_instruction_carriers.py`
9. `governance/compat/test_check_agent_instruction_carriers.py`
10. `governance/compat/agent_autorun_command_catalog.py`
11. `governance/compat/local_governance_hook_catalog_pre_commit.py`
12. `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
13. `governance/compat/local_governance_hook_catalog_pre_push.py`
14. `.github/workflows/documentation-testing.yml`
15. `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2B_WORKER_RETURN_2026-08-11.md`

Expected manifest: exact 15 paths above.

Any sixteenth worker path is forbidden.

## Scope Firewall Authorization

Allowed paths:

- `AGENTS.md`
- `CLAUDE.md`
- `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`
- `docs/reference/archive/AGENTS_FULL_PRE_T2B_2026-08-11.md`
- `docs/reference/archive/CLAUDE_FULL_PRE_T2B_2026-08-11.md`
- `docs/reference/archive/CVF_DOWNSTREAM_AGENTS_TEMPLATE_FULL_PRE_T2B_2026-08-11.md`
- `docs/reference/CVF_AGENT_INSTRUCTION_CARRIER_ROUTING_INDEX_2026-08-11.md`
- `governance/compat/check_agent_instruction_carriers.py`
- `governance/compat/test_check_agent_instruction_carriers.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `.github/workflows/documentation-testing.yml`
- `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2B_WORKER_RETURN_2026-08-11.md`
- `docs/roadmaps/CVF_ACTIVE_CONTINUITY_READ_COST_REDUCTION_ROADMAP_2026-08-10.md`
- `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2B_SOURCE_BINDING_MATRIX_2026-08-11.md`
- `docs/baselines/CVF_GC018_ACTIVE_CONTINUITY_READ_COST_T2B_INSTRUCTION_CARRIER_COMPACTION_2026-08-11.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_CONTINUITY_READ_COST_T2B_INSTRUCTION_CARRIER_COMPACTION_2026-08-11.md`

Dispatcher-owned and reviewer-owned paths outside worker exact-15:

- active-continuity roadmap;
- T2B source/binding matrix;
- paired GC-018 and this Work Order;
- later completion review and session-sync surfaces.

Forbidden paths:

- any existing downstream repository, including shift-operations-workspace;
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` or its source fragments;
- current front door or active handoff;
- public-sync clone, public remote, deployment or runtime/product source;
- broad refactor of existing checkers/readers;
- any archive deletion or history rewrite.

Operator authorization: explicit T2B selection on 2026-08-11.

Rollback boundary: revert exact-15 as one material batch if independent review
rejects the implementation; preserve the three preimage archives.

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | N/A with reason: T2B compacts instruction carriers and does not build an agent-interaction workspace |
| Contract source | archive-qualified canonical-contract exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | N/A with reason: no workspace state or storage is added |
| Handoff fields | existing Agent Handoff Contract Control Block only |
| State ownership | unchanged; no workspace aggregate or source fragment mutation |
| Guard owner | `governance/compat/check_agent_workspace_design.py` |
| Build boundary | no workspace runtime source, provider proof, public-sync, or registry edits |

Canonical design source:
`docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`.

## Required Behavior

### 1. Preserve preimages

Copy raw bytes before rewriting. The three archive hashes must equal:

| Source/archive family | Required SHA-256 |
|---|---|
| AGENTS | `24395f0fbab0e68ca416f500ab76118e01d368d506016c58c0a2ec1e31daf73a` |
| CLAUDE | `5d918333045b248beb1d3acbe9fb984da45298cf5348abe0a107593ee0c8c7c1` |
| downstream template | `7f545fa243754cd3066f3b4264959f4b7f9bd3fa2f348bd1b99cc21483e34a74` |

Archives are historical evidence and `NOT_ACTIVE_AUTHORITY`.

### 2. Create canonical routing index

Create the exact index path from the manifest. It must carry the four approved
budgets, all 38 current AGENTS level-two heading names, canonical owners,
binding classes, direct machine-reader tokens, preimage hashes, archive paths,
and a claim boundary. It must be ASCII and within 300 lines/32,768 bytes.

### 3. Compact AGENTS

Keep a short progressive startup router, startup acknowledgment, canonical
authority hierarchy, task-class routing table, direct checker bindings, live
proof and repository/public boundaries, and a pointer to the routing index.
Retain the exact active V58 pointer. Do not duplicate historical narrative.

Target: at most 220 lines and 20,480 bytes.

### 4. Compact CLAUDE

Keep provider-operating guidance only, state explicitly that `CLAUDE.md` is
`NOT_CVF_SOURCE`, route governance facts to canonical CVF surfaces, preserve
the active front-door/state markers and two corpus-checker path bindings, and
retain short command/repository/public-sync pointers without duplicated
architecture history.

Target: at most 160 lines and 16,384 bytes.

### 5. Compact downstream template

Keep substitution tokens, progressive bootstrap-first startup, exact phase chain,
seven role tokens, mandatory rehydration tokens, live-proof/workspace/risk
boundaries, one governance-latency heading and all five golden-harness phrases,
at most 12 first-read paths, handoff closure, evidence bridge and override
refusal. Do not mutate any generated/existing downstream project.

Target: at most 180 lines and 20,480 bytes.

### 6. Add machine checker and wiring

The new checker must:

- read files with strict UTF-8 and convert missing/unreadable/malformed input
  into safe violations;
- enforce N/N+1 line and byte limits for all four active/index surfaces;
- validate the three archive hashes and source-family paths;
- verify every mapped AGENTS heading is present exactly once in the routing
  index;
- verify all direct Core and downstream literal tokens;
- reject unconditional full-state/history read mandates using the existing
  active-continuity wording helper or equivalent source-verified behavior;
- verify its own binding in autorun, pre-commit, reviewer-fast, pre-push and
  documentation CI; and
- expose `--enforce` and `--json` without network or external calls.

Add focused deterministic tests for every positive and negative class. Do not
weaken existing checkers to make the compact carriers pass.

### 7. Return uncommitted

Author the worker return at path 15, run the full return gate, leave HEAD
unchanged and staged zero, and stop for independent review.

## Direct Literal Preservation Contract

At minimum the compact carriers must retain every direct literal named in the
accepted source/binding matrix. For downstream, this includes:

- `INTAKE -> DESIGN -> SPEC -> WORK_ORDER -> BUILD -> REVIEW -> FREEZE`;
- `ORCHESTRATOR`, `SPEC_AUTHOR`, `WORK_ORDER_AUTHOR`,
  `IMPLEMENTATION_WORKER`, `REVIEWER`, `CLOSER`, `SESSION_SYNC_STEWARD`;
- `Mandatory Continuity Rehydration`, `new or resumed chat/session`,
  `new tranche or work order`, `Do not rely on chat history`,
  `BLOCKED_CONTINUITY_DRIFT`;
- `### Governance Latency and Approval Continuity`, `dependent same-scope repairs`,
  `real boundary change`, `consolidated review of relevant records`,
  `REVIEW_COST_ESCALATION_REQUIRED`, and `avoidable operator wait`.

## Core Guard Self-Protection Authorization

Protected paths:

- `AGENTS.md`
- `CLAUDE.md`
- `governance/compat/check_agent_instruction_carriers.py`
- `governance/compat/test_check_agent_instruction_carriers.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `.github/workflows/documentation-testing.yml`

Operator authorization: explicit T2B selection on 2026-08-11 after accepted
T2A closure.

Authorized guard-maintenance scope: exact-15 archive, carrier compaction,
routing index, checker/test, five gate bindings, and worker return only.

Rollback boundary: revert exact-15 together if rejected; preserve the three
preimage archives and do not change T3/downstream/public/runtime surfaces.

The worker return must reproduce this block and list every protected path it
actually changes so closure preflight can validate the uncommitted result.

## Near-Threshold Maintainability Plan

No new Python file may exceed 300 lines. If the checker or focused test would
exceed 300 lines, return `BLOCKED_SIZE_SCOPE`; do not compress semantics or add
a sixteenth path. Existing hook/autorun catalogs receive only one command row
each. All active Markdown targets must meet the approved budgets.

## Verification Commands

Run at minimum:

1. `python -m pytest governance/compat/test_check_agent_instruction_carriers.py -q`
2. `python governance/compat/check_agent_instruction_carriers.py --enforce --json`
3. `python governance/compat/check_active_session_state.py --enforce --json`
4. the three agent-workspace checkers and the public/corpus binding checkers;
5. `powershell -ExecutionPolicy Bypass -File scripts/test_cvf_golden_downstream_bootstrap.ps1`;
6. governed file-size, Python-size, encoding and archive-hygiene gates;
7. `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` before material evidence;
8. `python governance/compat/run_worker_return_fast_gate.py`;
9. exact-15 status/name-status, secret scan, `git diff --check`, HEAD and
   staged-zero audit.

Do not run live release, provider, browser, server, Docker, database,
deployment, public-sync, push, or downstream mutation commands.

## Acceptance Criteria

- AC-01: three byte-identical archives match all pinned hashes.
- AC-02: AGENTS is at most 220 lines/20,480 bytes.
- AC-03: CLAUDE is at most 160 lines/16,384 bytes and `NOT_CVF_SOURCE`.
- AC-04: downstream template is at most 180 lines/20,480 bytes and retains all
  substitution tokens, doctor and golden-harness literals.
- AC-05: routing index is at most 300 lines/32,768 bytes and covers all 38
  source headings exactly once.
- AC-06: every existing direct checker binding remains satisfied without
  weakening an existing reader.
- AC-07: new checker handles all positive/N+1/drift/malformed/unreadable cases
  deterministically and fail closed.
- AC-08: autorun, all three local hook catalogs and documentation CI run the
  new checker.
- AC-09: active-session, workspace, corpus, public-export and golden downstream
  tests/gates pass.
- AC-10: exact-15/no-sixteenth, unchanged worker HEAD, staged zero, worker no
  commit, and zero external-effect calls are proven.

## Worker Autonomy / No-Question Rule

Repair allowed-scope failures directly after reading the failing checker
source. Return to orchestrator only for source contradiction, missing
authority, exact-15 insufficiency, archive mismatch, size-scope impossibility,
or a required forbidden-path change.

## Evidence Requirements

Provide command-backed archive hashes/raw equality, carrier budgets, all 38
heading routes, direct-token bindings, N/N+1 cases, exact-15 status/diff,
focused and golden-harness results, unchanged worker HEAD, staged zero, and
zero provider/network/live/downstream/public/commit/push calls.

## Review Gate

An independent reviewer must inspect source semantics, recompute every archive
and budget, run adversarial checker probes plus required gates, verify exact-15
and no weakening, then issue PASS or CHANGES_REQUIRED before any closure commit.

## Closure Checklist

- [x] Exact worker scope and forbidden expansion are explicit.
- [x] Every roadmap requirement maps to an owner and evidence class.
- [x] Current source claims use allowed source-verification dispositions.
- [x] Worker return, independent review and session-sync ownership are bound.
- [x] T3, downstream migration and external effects remain parked.

## Worker Return Packet Shape Contract

workerReturnPath:
`docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2B_WORKER_RETURN_2026-08-11.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must contain executionBaseHead, exact-15 expected/actual/delta,
AC-01 through AC-10, archive hashes, before/after budgets, 38-heading coverage,
direct-binding proof, focused/golden/local gates, worker HEAD/staged state,
no-commit and zero-call accounting.

## Worker Output Checker Read-Ahead Mandate

Before writing the routing index, checker, tests, or worker return, read the
applicable structural, encoding, file-size, binding, trace and worker-return
checker sources. Use exact real headings only, not checklist strings prefixed
with heading syntax.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Binding |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher/source reviewer, separate no-commit implementation worker, independent reviewer/closer, session-sync steward |
| phase | `T2B_DISPATCH`, `T2B_BUILD`, `T2B_REVIEW`, `T2B_CLOSURE_OR_BLOCK` |
| baseHeadFor(phase) | `dispatchBaseHead=178c5e7e169c936e285f484de5abd8dae2e06c07`; worker captures executionBaseHead; reviewer captures closureBaseHead |
| changedSetScope(phase) | dispatcher packet paths are separate; worker exact-15; reviewer closure paths separate |
| traceScope(phase, actor) | dispatcher maps/authorizes; worker proves exact-15; reviewer recomputes semantic and machine evidence |
| commitOwner(phase) | independent reviewer/closer only after PASS |
| crossBatchIsolation | T3, downstream mutation and all external/runtime lanes remain parked |
| nextMoveSurfaces | dispatch steward activates T2B only; worker stops pending review; closer parks or advances after review |

Designated closer: `INDEPENDENT_REVIEWER_CLOSER`.

## Reviewer Closure Conversion

- completionReviewPath:
  `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2B_COMPLETION_REVIEW_2026-08-11.md`
- reviewerOwnedClosurePaths: completion review, accepted material commit,
  roadmap closure, current-authority/session sync and handoff anchor
- closureOwner: independent reviewer/closer
- workerCommitPermission: `FORBIDDEN`

## Work-Order Fulfillment Manifest

| Requirement | Owning output | Worker evidence |
|---|---|---|
| archives | three archive paths | raw equality and hashes |
| binding preservation | routing index plus compact carriers | heading/token matrix |
| recurrence prevention | checker/tests and five bindings | focused tests and catalog scan |
| downstream inheritance | compact template | golden bootstrap harness |
| scope/no effects | worker return | exact manifest and zero-call counts |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | root AGENTS plus canonical routing index | repository-local R2 instruction routing | source map, archives, checker/tests | local filesystem reads | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | provider-local CLAUDE and generated downstream AGENTS | no CLI/MCP invocation or provider authority | provider boundary and local golden harness | no runtime adapter | `N/A_WITH_REASON` |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing root carriers, reference/archive, governance compatibility and command catalogs |
| Storage decision | reuse existing layout; add three archives, one routing index, one checker/test and one return |
| Existing aggregate impact | none |
| Generated state impact | none during worker build |
| Durable governance boundary | active carriers route; archives preserve evidence; index owns compact binding map |

## Commit Mode And Base-Anchor Lifecycle

| Field | Binding |
|---|---|
| commitMode | `WORKER_MUST_NOT_COMMIT` |
| dispatchBaseHead | `178c5e7e169c936e285f484de5abd8dae2e06c07` |
| executionBaseHead | worker captures post-dispatch clean HEAD |
| closureBaseHead | reviewer captures after worker return |
| commitOwner | independent reviewer/closer only |
| stale-anchor action | return `BLOCKED`; do not infer authority from chat/provider memory |

## Negative Search And Collision Discipline

All proposed baseline, Work Order, routing-index, checker, test, archive and
worker-return paths were absent at dispatch base. The worker must repeat path
collision and exact preimage-hash checks before writing.

## Provider Memory Authority Boundary

`CLAUDE.md`, provider-local memories, IDE summaries and chat history are
`NOT_CVF_SOURCE`. Facts used for implementation or review must be reverified
against this packet, the paired baseline, source map, canonical references,
current source, or command evidence.

## Legacy Absorption Coverage Index Disposition

N/A with reason: T2B changes instruction routing and does not add, scan,
classify, absorb, or claim legacy corpus knowledge.

rawMemoryReleased=false

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | governed worker dispatch -> uncommitted return -> independent CVF source review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T2B source map and Work Order |
| Disposition | NOT_APPLICABLE_WITH_REASON: worker delegation is not knowledge absorption |
| Claim boundary | no external source/provider/corpus/public intake or authority promotion |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACRC-T2B --title "Active Continuity Instruction Carrier Compaction" --date 2026-08-11 --base 178c5e7e169c936e285f484de5abd8dae2e06c07 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact source map, archive/budget/literal/checker/wiring/role boundaries |
| checkerReadAheadConfirmation | dispatch, structure, protected-path, handoff, trace, binding, file-size and worker-return sources read |
| docOnlyNewFields | `carrierBudget`; `preimageSha256`; `bindingClass` |
| claimBoundary | dispatch provenance only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defectIds: NONE_RETURNED

Returned defects: NONE_RETURNED

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json`

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_closure_packaging_preflight.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_active_session_state.py`; `governance/compat/check_agent_workspace_state.py`; `governance/compat/check_agent_workspace_skeleton.py`; `governance/compat/check_agent_workspace_runtime_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_python_automation_size.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `MULTI_AGENT_MULTI_ROLE`; `WORKER_RETURN_FULL_GATE_V1`; `Core Guard Self-Protection Authorization`; `Expected manifest`; `Actual changed set`; `Manifest delta`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | source-backed confirmation before worker dispatch |
| claimBoundary | exact-15 dispatch and output form only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/work-order author |
| Provider or surface | local private CVF Core workspace |
| Session or invocation | ACRC-T2B dispatch authoring, 2026-08-11 |
| Working directory | repository root at `178c5e7e1` |
| Command or tool surface | progressive reads, source search, hashes/sizes, scaffold and patch authoring |
| Target paths | roadmap, source map, paired baseline and this Work Order |
| Allowed scope source | explicit operator T2B selection and accepted roadmap |
| Before status evidence | clean worktree at HEAD `178c5e7e1`; staged zero |
| After status evidence | exact four dispatcher paths before commit |
| Diff evidence | status/name-status and dispatch gates |
| Approval boundary | exact-15 no-commit dispatch only |
| Claim boundary | no worker implementation, downstream mutation, external call, commit, or push |
| Agent type | dispatcher/work-order author |
| Invocation ID | `active-continuity-read-cost-t2b-dispatch-2026-08-11` |
| Expected manifest | roadmap, source map, baseline, Work Order |
| Actual changed set | same four dispatcher paths before commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: dispatcher deletes or renames nothing |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | repository-local instruction-carrier compaction and structural checking |
| claimDisposition | N/A with reason: no runtime execution-control claim |
| receiptEvidence | N/A with reason: no runtime receipt is produced |
| actionEvidence | N/A with reason: local source/test/archive evidence only; no runtime action claim |
| invocationBoundary | local shell and Python/PowerShell test execution |
| interceptionBoundary | no IDE, provider, network, external-service or runtime interception |
| claimLanguage | bounded startup instruction routing and recurrence prevention |
| forbiddenExpansion | T3, existing downstream mutation, provider/live, public-sync, push, deploy or production |

## Worker Return

Return exactly `COMPLETE_PENDING_INDEPENDENT_REVIEW` or `BLOCKED` and stop.
Do not commit.

## Return-To-Orchestrator Conditions

Return `BLOCKED` for source contradiction, archive mismatch, missing canonical
owner, exact-15 insufficiency, N/N+1 proof impossibility, protected-path need
outside scope, external/secret/quota requirement, or destructive action.

## Execution Authority Waiver

operator.checkpoint.waiver: exact-15 T2B execution is authorized only after
this packet and paired baseline pass pre-dispatch and the active session routes
the worker to their exact hashes. Fresh operator authority is required for any
scope expansion, T3, existing downstream mutation, external effect, commit-mode
change, public sync, push or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T2B modifies private provenance carriers and future-project template
source only. Public projection requires a later separate public-sync batch.

## Claim Boundary

T2B may produce compact Core/provider/downstream instruction carriers,
byte-identical archives, a canonical routing index, and repository-local
machine enforcement. It does not migrate shift-operations or any other
existing project, change runtime/provider behavior, call a service, deploy,
publish, push, or prove production readiness.

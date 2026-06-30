# CVF Agent Work Order - KIOD-R5 Packet-Blocked Pilot

Memory class: FULL_RECORD

Status: HOLD_PENDING_OPERATOR_SOURCE_SELECTION

Date: 2026-06-30

docType: work_order

dispatchBaseHead: fad6e44c

executionBaseHead: HOLD_PENDING_OPERATOR_SOURCE_SELECTION

closureBaseHead: HOLD_PENDING_OPERATOR_SOURCE_SELECTION

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker after release only. Reviewer/closer remains separate.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R5_PACKET_BLOCKED_PILOT_2026-06-30.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: record with `git rev-parse --short HEAD` only after this
work order is released from hold.

Current-time notes: KIOD-R4 is closed with decision token
`PACKET_BLOCK_REQUIRED_NOW`; KIOD-R5 is held because the operator has not yet
selected the exact next source repo/folder.

Do-not-misread notes: do not execute this work order while status is
`HOLD_PENDING_OPERATOR_SOURCE_SELECTION`; do not let the worker choose the
source target; do not implement a checker; do not import source material into
CVF; do not create runtime, provider, MCP/CLI adapter, dashboard, public-sync,
generated aggregate, package activation, or production-readiness behavior; do
not commit from worker mode.

Required first actions: after operator source selection and dispatcher release,
read this work order, the paired GC-018 baseline, KIOD-R1, KIOD-R2, KIOD-R3,
KIOD-R4 completion, Guard Orientation Index, and literal-format gotchas; record
executionBaseHead; inspect `git status --short`; then produce only the worker
return artifact requested below.

Return contract: while held, no worker return is authorized. After release, the
worker returns one uncommitted `COMPLETE_PENDING_REVIEW` artifact under
`docs/reviews/` and does not commit.

## Paired Baseline

`docs/baselines/CVF_GC018_KIOD_R5_PACKET_BLOCKED_NEXT_REPO_FOLDER_PILOT_2026-06-30.md`

## Scope

Allowed scope: preserve the corrected KIOD-R5 hold packet, source-selection
gate, source verification, release instructions, and future worker-return
shape.

Forbidden scope: worker execution, agent-selected source target, checker
implementation, direct source import, runtime/provider behavior, MCP/CLI
adapter behavior, dashboard/Web work, public-sync, generated aggregate edits,
package lifecycle mutation, automatic invocation, action authority, or
production-readiness claims.

## Hold Gate

| Gate | Current value | Required release evidence |
| --- | --- | --- |
| sourceSelectionEvidence | not recorded | operator names exactly one source repo URL, local source mirror, or folder path |
| worker execution | not authorized | release edit changes this section and reruns pre-dispatch gates |
| source-target choice | operator-owned | worker must not infer or choose the target |

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Dispatcher | Codex/reviewer before release | keep packet held until source target is explicit |
| Future worker | operator-selected agent after release | produce uncommitted worker return only |
| Reviewer/closer | Codex/reviewer after worker return | accept, reject, repair, and commit accepted material |

## Purpose

Hold the KIOD-R5 worker packet until the source target is explicit. KIOD-R5
will pilot packet-blocked source intake only after the operator selects one
repo/folder. The released pilot must require `Negative-search evidence` before
accepting any novelty candidate, owner-missing row, or new-owner proposal.

## Authority Chain

| Authority | Source path | Verified line/section | Disposition |
| --- | --- | --- | --- |
| KIOD-T0 roadmap | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | lines 5, 33, 36, 91 | ACCEPT |
| KIOD-R4 completion | `docs/reviews/CVF_KIOD_R4_NEGATIVE_SEARCH_EVIDENCE_DECISION_COMPLETION_2026-06-30.md` | lines 24, 70-78, 186, 295 | ACCEPT |
| KIOD-R1 taxonomy | `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md` | lines 50-53, 61 | ACCEPT |
| KIOD-R2 pre-scan packet | `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md` | lines 37, 40, 46, 51, 62 | ACCEPT |
| KIOD-R3 routing matrix | `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | lines 34, 37, 45, 54 | ACCEPT |
| Agent handoff contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | lines 243-249 | ACCEPT |

## Required First Reads

Release-time worker must read:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- active handoff named by the state registry
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- this work order and paired baseline
- KIOD-R1, KIOD-R2, KIOD-R3, and KIOD-R4 completion artifacts named in the
  Authority Chain

## Pre-Flight Checks

This work order is not executable while held.

Release-time dispatcher must run:

- `git rev-parse --short HEAD`
- `git status --short`
- `python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD`

## Write Ownership

Future worker may write only the release-authorized worker-return artifact under
`docs/reviews/`. Worker must not commit.

Reviewer/closer owns completion review, accepted edits, session sync, and
commits after worker return.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| KIOD-R5 is proposed as the next packet-blocked pilot | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | line 91 | `KIOD-R5` | KIOD-T0 roadmap row | ACCEPT |
| KIOD-R5 must wait for operator-selected repo/folder | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | line 91 | `operator-selected repo/folder` | KIOD-T0 roadmap row | ACCEPT |
| KIOD-R4 selected packet-block enforcement now | `docs/reviews/CVF_KIOD_R4_NEGATIVE_SEARCH_EVIDENCE_DECISION_COMPLETION_2026-06-30.md` | line 24 | `PACKET_BLOCK_REQUIRED_NOW` | KIOD-R4 completion decision | ACCEPT |
| KIOD-R4 routes future omitted negative-search evidence to KIOD-R5 | `docs/reviews/CVF_KIOD_R4_NEGATIVE_SEARCH_EVIDENCE_DECISION_COMPLETION_2026-06-30.md` | lines 70-78 | `Negative-search evidence` | KIOD-R4 risk routing | ACCEPT |
| R1 requires stopping when negative search evidence is absent | `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md` | line 52 | `negative search evidence` | KIOD-R1 owner surface checklist | ACCEPT |
| R2 says novelty candidates are invalid when negative-search evidence is absent | `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md` | line 40 | `Novelty candidates` | KIOD-R2 packet fields | ACCEPT |
| R3 NEW_FINDING requires negative-search commands and candidate owner decision | `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | line 34 | `NEW_FINDING` | KIOD-R3 routing matrix | ACCEPT |
| WORKER_MUST_NOT_COMMIT split needs reviewer closure conversion | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | lines 243-249 | `Reviewer Closure Conversion` | Agent handoff contract | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query:
`python governance/compat/run_adif_defect_resolver.py --task-class knowledge-intake-overlap-discipline --role dispatcher --lifecycle-phase pre-dispatch`

Returned defects: NONE_RETURNED

Resolver query: taskClass=`knowledge-intake-overlap-discipline`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

## Agent Handoff Contract Control Block

| Field | Value |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher holds packet; future worker returns uncommitted artifact; reviewer/closer owns acceptance and commit |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=fad6e44c; executionBaseHead=HOLD_PENDING_OPERATOR_SOURCE_SELECTION; closureBaseHead=HOLD_PENDING_OPERATOR_SOURCE_SELECTION |
| changedSetScope(phase) | held packet files now; future worker return after release; reviewer closure artifacts after return |
| traceScope(phase, actor) | dispatcher records held-packet trace; future worker records execution trace; reviewer records closure trace |
| commitOwner(phase) | dispatcher/reviewer for held packet; nobody during WORKER_MUST_NOT_COMMIT execution; reviewer/closer for closure |
| crossBatchIsolation | no R1, R2, R3, R4, runtime, Web, public-sync, generated aggregate, or package activation changes |
| nextMoveSurfaces | after this hold packet, operator must select the exact source repo/folder before dispatch |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_KIOD_R5_PACKET_BLOCKED_PILOT_COMPLETION_2026-06-30.md`

reviewerOwnedClosurePaths:
`docs/reviews/CVF_KIOD_R5_PACKET_BLOCKED_PILOT_WORKER_RETURN_2026-06-30.md`;
`docs/reviews/CVF_KIOD_R5_PACKET_BLOCKED_PILOT_COMPLETION_2026-06-30.md`

## External Knowledge Intake Routing

External knowledge intake routing: REQUIRED

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> root/folder lifecycle classification plus absorption map when retained -> CVF owner surface disposition -> governed work order before implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | `docs/reference/external_agent_review/`; `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` |
| Disposition | HOLD_PENDING_OPERATOR_SOURCE_SELECTION |
| Claim boundary | held packet only; no source absorption or implementation claim |

## Execution Plan

No worker execution is allowed while held.

After source selection and release, the worker must:

1. read the required files;
2. record executionBaseHead and clean or dirty status;
3. inspect only the selected source target;
4. produce a worker return with source-target evidence, negative-search
   evidence, overlap/novelty classification, and claim boundary;
5. stop without committing.

## Future Release Instructions

When the operator selects a source target, update this work order before worker
dispatch with:

- `sourceSelectionEvidence`: exact repo URL, mirror path, or folder path.
- `sourceTargetReadPlan`: exact first-read files, folders, or mirror commit.
- `Negative-search evidence`: literal commands or queries that search CVF owner
  surfaces before accepting novelty or owner-missing rows. Example command
  shape: `rg -n --fixed-strings "<candidate term>" docs governance CVF_SESSION`.
- `Overlap And Novelty Classification`: at least one row using KIOD-R3
  dispositions such as `CONFIRMED_EXISTING`, `ENRICH_EXISTING`, `NEW_FINDING`,
  `REJECT_DIRECT_IMPORT`, `NO_NEW_VALUE`, or `OWNER_SURFACE_NOT_FOUND`.

## Evidence Requirements

Held packet evidence:

- current status remains `HOLD_PENDING_OPERATOR_SOURCE_SELECTION`;
- source target is not selected;
- worker execution is not authorized.

Release-time worker evidence:

- exact selected source target;
- command-backed source read evidence;
- `Negative-search evidence` commands or queries;
- `Overlap And Novelty Classification` table;
- `git status --short` before and after worker changes.

## Acceptance Criteria

- The artifact remains held until source selection is explicit.
- A released worker packet cannot accept novelty or owner-missing rows without
  negative-search evidence.
- Worker output must remain uncommitted until reviewer/closer acceptance.

## Review Gate

Reviewer must reject any worker return that omits the selected source target,
omits negative-search evidence, lets the worker choose the target, or claims
runtime/checker/adapter/public/production behavior.

## Closure Checklist

- [x] HOLD status recorded with source-selection blocker.
- [x] ADIF disclosure recorded.
- [x] AHB control block and reviewer closure conversion recorded.
- [x] Dual-agent matrix recorded.
- [x] Forbidden scope recorded.
- [ ] Release source target selected by operator.
- [ ] Release pre-dispatch gates run after source selection.

## Return-To-Orchestrator Conditions

Return to orchestrator if the source target is absent, the operator selection
is ambiguous, the worker tries to select the target, or a required source owner
cannot be verified.

## Operator Checkpoint

Operator checkpoint required: name exactly one source repo URL, local source
mirror, or folder path for KIOD-R5 before worker dispatch.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-30 KIOD-R5 hold-packet repair after rejected Claude draft |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, governance checkers |
| Target paths | `docs/baselines/CVF_GC018_KIOD_R5_PACKET_BLOCKED_NEXT_REPO_FOLDER_PILOT_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R5_PACKET_BLOCKED_PILOT_2026-06-30.md` |
| Allowed scope source | operator request to inspect and handle poor Claude work order |
| Before status evidence | Claude draft had staged scope creep and untracked KIOD-R5 packet files; scope creep restored to HEAD before packet repair |
| After status evidence | pending checker rerun after repair |
| Diff evidence | `git diff -- docs/baselines/CVF_GC018_KIOD_R5_PACKET_BLOCKED_NEXT_REPO_FOLDER_PILOT_2026-06-30.md docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R5_PACKET_BLOCKED_PILOT_2026-06-30.md` |
| Approval boundary | repair KIOD-R5 packet only; do not execute worker pilot |
| Claim boundary | held documentation packet only; no runtime, checker, adapter, public-sync, source import, or production claim |
| Agent type | reviewer/dispatcher repair |
| Invocation ID | local Codex session 2026-06-30 |
| Expected manifest | `docs/baselines/CVF_GC018_KIOD_R5_PACKET_BLOCKED_NEXT_REPO_FOLDER_PILOT_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R5_PACKET_BLOCKED_PILOT_2026-06-30.md` |
| Actual changed set | `docs/baselines/CVF_GC018_KIOD_R5_PACKET_BLOCKED_NEXT_REPO_FOLDER_PILOT_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R5_PACKET_BLOCKED_PILOT_2026-06-30.md` |
| Manifest delta | N/A with reason: expected and actual changed sets match |

## Dual Agent Surface Matrix

| Consumer | Surface owner | Allowed use | Evidence or reason | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | future KIOD-R5 worker after release | may produce a documentation-only source-intake packet and worker return | KIOD-R1 through KIOD-R4 authority chain and this held work order | no commit, runtime, source import, checker, or production claim | HOLD_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future external adapter | no CLI/MCP ingress, execution, mutation, raw source release, or public behavior | no adapter is implemented or authorized here | separate GC-018/source-verified adapter packet required | DEFERRED_WITH_REASON |

## Forbidden Scope

- No checker implementation for negative-search evidence.
- No direct source import into CVF.
- No runtime, provider, MCP/CLI adapter, dashboard, public-sync, generated
  aggregate, package lifecycle mutation, automatic invocation, action authority,
  or production-readiness claim.
- No edits to KIOD-R1, KIOD-R2, KIOD-R3, KIOD-R4, or KIOD-T0 during held packet
  correction.

## Verification Plan

Current held-packet verification:

- `python governance/compat/check_work_order_dispatch_quality.py --base fad6e44c --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base fad6e44c --head HEAD`

Release verification after source selection:

- rerun both commands above on the release range;
- run any focused checker named by the release edit;
- capture `git diff --name-status` and `git status --short`.

## Claim Boundary

This work order is not dispatch-ready. It is a corrected hold packet that
prevents worker execution until source selection is explicit and packet-block
fields are release-edited with source evidence.

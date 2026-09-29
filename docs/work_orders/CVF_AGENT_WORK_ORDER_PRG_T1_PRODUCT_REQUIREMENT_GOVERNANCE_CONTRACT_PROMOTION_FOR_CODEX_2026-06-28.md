# CVF Agent Work Order - PRG-T1 Product Requirement Governance Contract Promotion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-28

Batch ID: PRG-T1

dispatchBaseHead: 67250e04

executionBaseHead: 67250e04

closureBaseHead: 67250e04

Commit mode: `WORKER_MAY_COMMIT_AFTER_REVIEWER_CLOSURE`

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role dispatcher/worker/reviewer/closer.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_PRG_T1_PRODUCT_REQUIREMENT_GOVERNANCE_CONTRACT_PROMOTION_FOR_CODEX_2026-06-28.md`

Commit mode: `WORKER_MAY_COMMIT_AFTER_REVIEWER_CLOSURE`.

Current-time notes: current date is 2026-06-28. PRG-T0 committed at
`efb45892` and accepted the operator-provided package as a T1 hardening seed.

Do-not-misread notes: reuse the folder's useful substance by adapting it into
CVF form. Do not copy external AGPL code, do not promote the root package
folder directly, do not implement validators, and do not bypass SPEC or Work
Order.

Required first actions: read session front door/state/handoff, guard
orientation, literal-format gotchas, external knowledge chain map, PRG-T0
roadmap, and the package protocol files cited in the Source Verification Block.

## Purpose

Execute PRG-T1 by promoting selected operator-provided package content into a
CVF-owned Product Requirement Governance reference front door and contract.

## Authority Chain

| Authority | Path or source | Disposition |
|---|---|---|
| Operator instruction | current chat approval to proceed and reuse package material by editing into CVF form | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup source read |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | startup source read |
| Active handoff | `AGENT_HANDOFF_V25_2026-06-28.md` | startup source read |
| PRG-T0 roadmap | `docs/roadmaps/CVF_PRG_T0_PRODUCT_SPEC_EXTERNAL_PACKAGE_ABSORPTION_ROADMAP_2026-06-28.md` | authorizes PRG-T1 GC-018/work order route |
| PRG-T1 GC-018 | `docs/baselines/CVF_GC018_PRG_T1_PRODUCT_REQUIREMENT_GOVERNANCE_CONTRACT_PROMOTION_2026-06-28.md` | this work order's baseline |

## Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Dispatcher | Codex | source-verify T1 scope |
| Worker | Codex | create adapted reference docs only |
| Reviewer/closer | Codex | run gates, repair allowed-scope doc defects, and commit material |
| Session-sync steward | Codex | update session surfaces only if needed after material commit |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex acts as dispatcher, worker, reviewer/closer, and later session-sync steward only if continuity changes |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC if needed |
| baseHeadFor(phase) | `dispatchBaseHead=67250e04`; `executionBaseHead=67250e04`; `closureBaseHead=67250e04` |
| changedSetScope(phase) | material phase may create only PRG-T1 baseline, work order, completion review, README, and contract |
| traceScope(phase, actor) | completion review records command evidence, changed set, and claim boundary |
| commitOwner(phase) | Codex owns material commit; session-sync commit is separate if needed |
| crossBatchIsolation | no runtime/source/checker/test/public-sync/session-state changes in material commit |
| nextMoveSurfaces | update only after material commit if current mode or next allowed move changes |
| closer designation | Codex reviewer/closer |

## Scope / Methodology

In scope:

- create `docs/reference/product_requirement_governance/README.md`;
- create `docs/reference/product_requirement_governance/CVF_PRG_PRODUCT_REQUIREMENT_CONTRACT.md`;
- create this work order, the PRG-T1 GC-018 baseline, and completion review;
- adapt useful content from the operator-provided folder into CVF form;
- run dispatch and closure gates.

Out of scope:

- validator source, fixtures, tests, generated registries, hooks, UI, runtime,
  provider/live proof, public-sync, package activation, certification, adapter
  implementation, and copied external code.

## Required First Reads

| Source | Reason |
|---|---|
| `CVF_SESSION_MEMORY.md` | active front-door state |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | compact current mode and next move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | canonical active state |
| `AGENT_HANDOFF_V25_2026-06-28.md` | active handoff |
| `docs/reference/guard_orientation/README.md` | task guard map |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | literal-format prevention |
| `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | external material routing |
| `docs/roadmaps/CVF_PRG_T0_PRODUCT_SPEC_EXTERNAL_PACKAGE_ABSORPTION_ROADMAP_2026-06-28.md` | PRG-T1 authority |
| package protocol files named in Source Verification Block | adaptation inputs |

## Pre-Flight Checks

| Command | Required result |
|---|---|
| `git rev-parse --short HEAD` | `67250e04` at dispatch start |
| `git status --short` | clean or only PRG-T1 material paths after authoring |
| `python -c "from governance.compat.run_adif_defect_resolver import resolve_defect_packet; print(resolve_defect_packet(task_class='work-order-authoring', role='dispatch-author', lifecycle_phase='dispatch').to_dict())"` | zero returned ADIF defects for disclosed query |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path created | `docs/reference/product_requirement_governance/` |
| Front door | `docs/reference/product_requirement_governance/README.md` |
| Primary contract | `docs/reference/product_requirement_governance/CVF_PRG_PRODUCT_REQUIREMENT_CONTRACT.md` |
| Storage class | governed reference documentation |
| Generated aggregate | N/A with reason: PRG-T1 creates no generated JSON aggregate |
| Registry owner | N/A with reason: registry design is deferred to a later PRG validator/traceability tranche |
| Public surface | DEFERRED_PRIVATE_ONLY |
| Boundary | no runtime validator, package instance, adapter, public-sync, or generated registry is created |

## Current Runtime Freshness Verification

| Field | Evidence |
|---|---|
| Runtime/source path changed | N/A with reason: PRG-T1 allowed scope is governed documentation only |
| Verification command | `git diff --name-status 67250e04..HEAD` |
| Expected changed set | PRG-T1 baseline, work order, completion review, reference README, and reference contract only |
| Runtime claim boundary | PRG-T1 makes only an absence boundary: no validator/source/runtime behavior is implemented by this tranche |
| Required next action for runtime work | fresh GC-018, source-verified work order, fixtures/tests, and applicable live-proof rules when governance behavior is claimed |

## Write Ownership

Allowed material paths:

- `docs/reference/product_requirement_governance/README.md`
- `docs/reference/product_requirement_governance/CVF_PRG_PRODUCT_REQUIREMENT_CONTRACT.md`
- `docs/baselines/CVF_GC018_PRG_T1_PRODUCT_REQUIREMENT_GOVERNANCE_CONTRACT_PROMOTION_2026-06-28.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_PRG_T1_PRODUCT_REQUIREMENT_GOVERNANCE_CONTRACT_PROMOTION_FOR_CODEX_2026-06-28.md`
- `docs/reviews/CVF_PRG_T1_PRODUCT_REQUIREMENT_GOVERNANCE_CONTRACT_PROMOTION_COMPLETION_2026-06-28.md`

Forbidden paths: runtime/source/checker/test files, generated aggregates,
active session state, active handoff, front door, public-sync clone, external
repo source, and the root package folder.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| PRG-T0 selected PRG-T1 contract/validator foundation route | `docs/roadmaps/CVF_PRG_T0_PRODUCT_SPEC_EXTERNAL_PACKAGE_ABSORPTION_ROADMAP_2026-06-28.md` | lines 187-195 | `AUTHOR_PRG_T1_GC018_FOR_PACKAGE_PROMOTION_AND_VALIDATOR_FOUNDATION` | PRG-T0 roadmap | LITERAL_INVARIANT | ACCEPT |
| Direct AGPL code copy is rejected | `docs/roadmaps/CVF_PRG_T0_PRODUCT_SPEC_EXTERNAL_PACKAGE_ABSORPTION_ROADMAP_2026-06-28.md` | lines 121, 162, 211 | `REJECT_DIRECT_CODE_COPY` | PRG-T0 roadmap | LITERAL_INVARIANT | ACCEPT |
| PRG-T0 audited product hierarchy, metadata, deterministic validation, no-silent-reversal, read-only critique, and handoff primitives | `docs/roadmaps/CVF_PRG_T0_PRODUCT_SPEC_EXTERNAL_PACKAGE_ABSORPTION_ROADMAP_2026-06-28.md` | Package Content Audit Matrix; Absorption Classification | `Package Content Audit Matrix`; `Absorption Classification` | PRG-T0 roadmap | LITERAL_INVARIANT | ACCEPT |
| PRG-T0 selected frontmatter governance, deterministic validation, no-silent-reversal, read-only reviewer lane, and product-spec-to-work-order boundary as absorb/adapt content | `docs/roadmaps/CVF_PRG_T0_PRODUCT_SPEC_EXTERNAL_PACKAGE_ABSORPTION_ROADMAP_2026-06-28.md` | lines 159-160 | `Absorb now as doctrine`; `Adapt into CVF` | PRG-T0 roadmap | VALUE_SET | ACCEPT |
| PRG-T0 recorded the future owner surface for PRG promotion | `docs/roadmaps/CVF_PRG_T0_PRODUCT_SPEC_EXTERNAL_PACKAGE_ABSORPTION_ROADMAP_2026-06-28.md` | line 93 | `docs/reference/product_requirement_governance/` | PRG-T0 roadmap | LITERAL_INVARIANT | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatch-author`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator-provided package -> PRG-T0 roadmap -> PRG-T1 CVF reference contract |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/product_requirement_governance/` |
| Disposition | ADAPT selected package primitives into CVF-owned reference contract |
| Claim boundary | external package content remains advisory until adapted into CVF-owned docs |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order action | Disposition |
|---|---|---|
| Promote selected package value through GC-018/work order | create PRG-T1 baseline and this work order | SATISFIED |
| Use package material where valuable | adapt selected package protocols into PRG contract | SATISFIED |
| Keep root package unpromoted | leave root package as ignored external input | SATISFIED |
| Preserve clean-room license boundary | no external code copied | SATISFIED |
| Defer validator implementation | contract records validator foundation boundary | SATISFIED |

## Execution Plan

| Step | Action | Disposition |
|---|---|---|
| T1.1 | read PRG-T0 and package source protocols | COMPLETE |
| T1.2 | create PRG reference folder front door | COMPLETE |
| T1.3 | create adapted PRG product requirement contract | COMPLETE |
| T1.4 | create completion review | COMPLETE |
| T1.5 | run dispatch/closure gates and commit material docs | REQUIRED |

## Evidence Requirements

Evidence must include source verification against PRG-T0, the adapted contract's
Source Conversion Matrix, External Knowledge Intake Routing, Dual Agent Surface
Matrix, public export disposition, closure command table, and final git status.

## Review Gate

Codex reviewer/closer must run structural completeness, external-intake routing,
dispatch-quality, autorun pre-implementation, commit steward, and diff hygiene
before material commit. Any allowed-scope documentation defect must be repaired
and rerun.

## Closure Checklist

- [x] PRG reference front door exists.
- [x] PRG contract exists.
- [x] Source Conversion Matrix exists.
- [x] External Knowledge Intake Routing exists.
- [x] Dual Agent Surface Matrix exists.
- [x] Public Export Disposition is private-only.
- [x] Validator implementation remains deferred.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if gates require runtime/source/checker/test
mutation, generated registry mutation, public-sync, provider/live proof,
adapter work, root package promotion, or copied external source code.

## Operator Checkpoint

N/A with reason: the operator approved PRG-T1 and explicitly instructed reuse
of valuable folder content after editing into CVF form. No additional
checkpoint is required for documentation-only contract promotion.

## Work-Order Fulfillment Manifest

| Artifact | Owner | Status |
|---|---|---|
| `docs/reference/product_requirement_governance/README.md` | Codex | CREATED |
| `docs/reference/product_requirement_governance/CVF_PRG_PRODUCT_REQUIREMENT_CONTRACT.md` | Codex | CREATED |
| `docs/baselines/CVF_GC018_PRG_T1_PRODUCT_REQUIREMENT_GOVERNANCE_CONTRACT_PROMOTION_2026-06-28.md` | Codex | CREATED |
| this work order | Codex | CREATED |
| `docs/reviews/CVF_PRG_T1_PRODUCT_REQUIREMENT_GOVERNANCE_CONTRACT_PROMOTION_COMPLETION_2026-06-28.md` | Codex | CREATED |

## Required Artifact Manifest

| Artifact | Required state | Status |
|---|---|---|
| `docs/reference/product_requirement_governance/README.md` | reference folder front door exists and is bounded | PASS |
| `docs/reference/product_requirement_governance/CVF_PRG_PRODUCT_REQUIREMENT_CONTRACT.md` | adapted PRG contract exists and preserves claim boundary | PASS |
| `docs/baselines/CVF_GC018_PRG_T1_PRODUCT_REQUIREMENT_GOVERNANCE_CONTRACT_PROMOTION_2026-06-28.md` | GC-018 baseline records source verification and T1 boundary | PASS |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_PRG_T1_PRODUCT_REQUIREMENT_GOVERNANCE_CONTRACT_PROMOTION_FOR_CODEX_2026-06-28.md` | work order records execution plan and closure scope | PASS |
| `docs/reviews/CVF_PRG_T1_PRODUCT_REQUIREMENT_GOVERNANCE_CONTRACT_PROMOTION_COMPLETION_2026-06-28.md` | completion review records acceptance and evidence | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | `docs/reference/product_requirement_governance/` | internal agents may use the reference for drafting and review guidance only | created README and contract | N/A with reason: no runtime adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future PRG readout or adapter candidate | no external agent interface is created | deferred in this work order | separate GC-018/source-verified adapter or public-sync work required | `DEFERRED_WITH_REASON` |

## Worker Autonomy / No-Question Rule

Codex may repair allowed-scope documentation, heading, and gate-shape defects
without pausing for approval. Stop if repair would require runtime/source
mutation, public-sync, provider/live proof, adapter work, package activation,
certification, or root package promotion.

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| PRG reference owner surface exists | README file created |
| Adapted PRG contract exists | contract file created |
| Package material is reused with CVF form | Source Conversion Matrix in contract |
| SPEC and Work Order remain mandatory | contract handoff sections |
| Validator implementation remains deferred | Validator Foundation Boundary |
| Public/export/adapter posture remains bounded | Public Export Disposition and Dual Agent Surface Matrix |

## Verification / Evidence

| Command | Required result |
|---|---|
| `python governance/compat/check_markdown_structural_completeness.py --base 67250e04 --head HEAD --enforce` | PASS |
| `python governance/compat/check_external_knowledge_intake_routing.py --base 67250e04 --head HEAD --enforce` | PASS |
| `python governance/compat/check_work_order_dispatch_quality.py --base 67250e04 --head HEAD --enforce` | PASS |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 67250e04 --head HEAD --serial` | PASS |
| `git diff --check` | PASS |

## Fail Conditions

Block if PRG-T1 copies AGPL implementation code, promotes the root package
folder directly, creates validators/fixtures/source/tests, claims runtime or
public behavior, creates external adapter support, changes session state in the
material commit, or allows product requirements to bypass SPEC and Work Order.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance reference promotion only.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_PRG_T0_PRODUCT_SPEC_EXTERNAL_PACKAGE_ABSORPTION_ROADMAP_2026-06-28.md` | `AUTHOR_PRG_T1_GC018_FOR_PACKAGE_PROMOTION_AND_VALIDATOR_FOUNDATION` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_PRG_T1_PRODUCT_REQUIREMENT_GOVERNANCE_CONTRACT_PROMOTION_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Reference front door | `docs/reference/product_requirement_governance/README.md` | `Status: ACTIVE_REFERENCE` | PASS |
| Reference contract | `docs/reference/product_requirement_governance/CVF_PRG_PRODUCT_REQUIREMENT_CONTRACT.md` | `Status: ACTIVE_REFERENCE` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_PRG_T1_PRODUCT_REQUIREMENT_GOVERNANCE_CONTRACT_PROMOTION_COMPLETION_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason | no registry JSON authorized by PRG-T1 | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no registry Markdown authorized by PRG-T1 | BLOCKED with reason |
| External evidence digest | N/A with reason | external package audit evidence is recorded in PRG-T0 | N/A with reason |
| System loop interlock | this file | no loop, queue, daemon, runtime, generated aggregate, or automatic activation created | PASS |
| Session continuity | N/A with reason | material reference promotion does not change active mode; handoff marker for PRG-T0 was already synced at `67250e04` | N/A with reason |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher/worker/reviewer/closer |
| Provider or surface | local workspace |
| Session or invocation | PRG-T1 product requirement governance contract promotion, 2026-06-28 |
| Working directory | repository root |
| Command or tool surface | source reads, package reads, apply_patch, governance gates |
| Target paths | PRG-T1 baseline, work order, completion review, README, and contract |
| Allowed scope source | operator approval after PRG-T0 commit `efb45892` |
| Before status evidence | `dispatchBaseHead=67250e04` |
| After status evidence | material docs ready for commit after gates |
| Diff evidence | `git diff --name-status 67250e04..HEAD` |
| Approval boundary | documentation-contract promotion only |
| Claim boundary | no runtime validator, generated registry, public-sync, provider/live proof, adapter, package certification, or Build authorization |
| Agent type | single-agent multi-role |
| Invocation ID | `cvf-prg-t1-product-requirement-contract-promotion-2026-06-28` |
| Expected manifest | PRG-T1 baseline, work order, completion review, README, contract |
| Actual changed set | PRG-T1 baseline, work order, completion review, README, contract |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This work order closes documentation-contract promotion only. It does not
implement validators, generated registries, runtime behavior, provider/live
proof, public-sync, package activation, certification, external adapters, or
direct Build authorization from product requirements.

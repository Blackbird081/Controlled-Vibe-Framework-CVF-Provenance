# CVF GC-018 PRG-T1 Product Requirement Governance Contract Promotion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018_baseline

Date: 2026-06-28

Batch ID: PRG-T1

Commit mode: WORKER_MAY_COMMIT_AFTER_REVIEWER_CLOSURE

dispatchBaseHead: 67250e04

executionBaseHead: 67250e04

closureBaseHead: 67250e04

## Purpose

Authorize PRG-T1 to promote selected content from the operator-provided
`CVF_Product_Requirement_Governance/` package into a CVF-owned reference
contract under `docs/reference/product_requirement_governance/`.

This baseline follows the PRG-T0 decision to use the package as a hardening
seed. T1 is documentation-contract promotion only. Validator source, tests,
fixtures, generated registries, runtime behavior, public-sync, adapters, and
package certification remain out of scope.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | current chat approval to proceed and reuse package content by editing into CVF form | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup source read before material work |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | startup source read before material work |
| Active handoff | `AGENT_HANDOFF_V25_2026-06-28.md` | startup source read before material work |
| PRG-T0 roadmap | `docs/roadmaps/CVF_PRG_T0_PRODUCT_SPEC_EXTERNAL_PACKAGE_ABSORPTION_ROADMAP_2026-06-28.md` | selected `AUTHOR_PRG_T1_GC018_FOR_PACKAGE_PROMOTION_AND_VALIDATOR_FOUNDATION` |
| External knowledge chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | external material remains advisory until promoted |
| Operator-provided package | `CVF_Product_Requirement_Governance/` | external input, not CVF authority |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| PRG-T0 accepted the package as a T1 seed requiring hardening | `docs/roadmaps/CVF_PRG_T0_PRODUCT_SPEC_EXTERNAL_PACKAGE_ABSORPTION_ROADMAP_2026-06-28.md` | line 25; lines 187-195 | `ACCEPT_PACKAGE_AS_T1_SEED_WITH_HARDENING_REQUIRED`; `AUTHOR_PRG_T1_GC018_FOR_PACKAGE_PROMOTION_AND_VALIDATOR_FOUNDATION` | PRG-T0 roadmap | LITERAL_INVARIANT | ACCEPT |
| PRG-T0 requires clean-room AGPL boundary | `docs/roadmaps/CVF_PRG_T0_PRODUCT_SPEC_EXTERNAL_PACKAGE_ABSORPTION_ROADMAP_2026-06-28.md` | lines 121, 162, 211 | `REJECT_DIRECT_CODE_COPY` | PRG-T0 roadmap | LITERAL_INVARIANT | ACCEPT |
| Product hierarchy, metadata, deterministic validation, no-silent-reversal, read-only critique, and handoff primitives were audited in PRG-T0 | `docs/roadmaps/CVF_PRG_T0_PRODUCT_SPEC_EXTERNAL_PACKAGE_ABSORPTION_ROADMAP_2026-06-28.md` | Package Content Audit Matrix; Absorption Classification | `Package Content Audit Matrix`; `Absorption Classification` | PRG-T0 roadmap | LITERAL_INVARIANT | ACCEPT |
| PRG-T0 selected frontmatter governance, deterministic validation, no-silent-reversal, read-only reviewer lane, and product-spec-to-work-order boundary as absorb/adapt content | `docs/roadmaps/CVF_PRG_T0_PRODUCT_SPEC_EXTERNAL_PACKAGE_ABSORPTION_ROADMAP_2026-06-28.md` | lines 159-160 | `Absorb now as doctrine`; `Adapt into CVF` | PRG-T0 roadmap | VALUE_SET | ACCEPT |
| PRG-T0 recorded the selected owner surface for future PRG promotion | `docs/roadmaps/CVF_PRG_T0_PRODUCT_SPEC_EXTERNAL_PACKAGE_ABSORPTION_ROADMAP_2026-06-28.md` | line 93 | `docs/reference/product_requirement_governance/` | PRG-T0 roadmap | LITERAL_INVARIANT | ACCEPT |
| External material is advisory until mapped and promoted | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | Central Core; Mandatory Chain | `CVF remains the source of truth` | external knowledge chain map | LITERAL_INVARIANT | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatch-author`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Decision / Baseline / Proposed Tranche

Decision: close PRG-T1 as documentation-contract promotion.

Baseline: the PRG-T0 roadmap and operator-provided package are the inputs. The
CVF-owned output is the reference front door plus contract under
`docs/reference/product_requirement_governance/`.

Proposed tranche output: active PRG reference folder, adapted PRG product
requirement contract, paired work order, and completion review. No validator,
fixture, runtime, generated registry, adapter, public-sync, or package
certification is authorized.

## Evidence / Verification

Dispatch and closure evidence must come from source verification, structural
completeness, external-intake routing, dispatch-quality, autorun, commit
steward, diff hygiene, and the completion review's final command table.

## Current Runtime Freshness Verification

| Field | Evidence |
|---|---|
| Runtime/source path changed | N/A with reason: PRG-T1 allowed scope is governed documentation only |
| Verification command | `git diff --name-status 67250e04..HEAD` |
| Expected changed set | PRG-T1 baseline, work order, completion review, reference README, and reference contract only |
| Runtime claim boundary | PRG-T1 makes only an absence boundary: no validator/source/runtime behavior is implemented by this tranche |
| Required next action for runtime work | fresh GC-018, source-verified work order, fixtures/tests, and applicable live-proof rules when governance behavior is claimed |

## Continuation Decision

| Field | Disposition |
|---|---|
| Selected tranche | PRG-T1 product requirement governance contract promotion |
| Closure status | CLOSED_PASS_BOUNDED |
| Worker commit authority | WORKER_MAY_COMMIT_AFTER_REVIEWER_CLOSURE |
| Reviewer closer | Codex single-agent multi-role |
| Reason for single-agent closure | documentation-only promotion with source verification, no runtime/source mutation, no provider/live proof, no public-sync |
| Next tranche blocked | PRG-T2 validator fixtures/checker foundation remains parked until PRG-T1 closure |

## Roadmap-To-Work-Order Trace Matrix

| PRG-T0 requirement | PRG-T1 action | Disposition |
|---|---|---|
| Decide final governed placement for package value | create `docs/reference/product_requirement_governance/` | SATISFIED |
| Add absorption map and provenance block | add Source Conversion Matrix and External Knowledge Intake Routing | SATISFIED |
| Normalize status and field vocabulary | convert package terms into CVF contract language and boundaries | SATISFIED_BOUNDED |
| Create fixtures and validator | defer to later PRG-T2 | DEFERRED_WITH_REASON |
| Avoid AGPL code copy | documentation adaptation only | SATISFIED |
| Preserve SPEC and Work Order route | contract states product requirements cannot bypass SPEC or Work Order | SATISFIED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | `docs/reference/product_requirement_governance/` | internal agents may use the contract as documentation guidance only | PRG-T1 reference files and completion review | N/A with reason: no internal runtime adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future PRG public-safe or adapter readout | no external interface, MCP tool, CLI command, or public package behavior is created | deferred in this baseline | separate GC-018/source-verified work order required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator-provided package -> PRG-T0 roadmap -> PRG-T1 CVF reference contract |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/product_requirement_governance/` |
| Disposition | ADAPT selected package primitives into CVF-owned reference contract |
| Claim boundary | package content remains external input; PRG-T1 owns only adapted reference documentation |

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| T1.1 | Create PRG reference front door | `docs/reference/product_requirement_governance/README.md` |
| T1.2 | Create adapted PRG contract | `docs/reference/product_requirement_governance/CVF_PRG_PRODUCT_REQUIREMENT_CONTRACT.md` |
| T1.3 | Create paired work order and completion review | PRG-T1 work order and completion review |
| T1.4 | Run dispatch/closure gates | command evidence in completion review |
| T1.5 | Commit material docs only | material commit after gates pass |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Selected package content is adapted rather than copied wholesale | Source Conversion Matrix |
| CVF owner surface exists | `docs/reference/product_requirement_governance/README.md` |
| PRG contract exists | `CVF_PRG_PRODUCT_REQUIREMENT_CONTRACT.md` |
| SPEC and Work Order remain mandatory route | contract handoff sections |
| Validator implementation remains deferred | Validator Foundation Boundary |
| External/public/adapter posture is explicit | Dual Agent Surface Matrix and Public Export Disposition |

## Fail Conditions

Fail or block PRG-T1 if the change copies AGPL implementation code, treats the
root package folder as canonical, creates runtime validators or fixtures,
claims public/provider/live behavior, creates external adapter support, bypasses
SPEC/Work Order, or omits source verification for reused package primitives.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance reference promotion only. No public-sync artifact is
authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_PRG_T0_PRODUCT_SPEC_EXTERNAL_PACKAGE_ABSORPTION_ROADMAP_2026-06-28.md` | `Status: ROADMAP_READY_FOR_OPERATOR_APPROVAL` and selected PRG-T1 next move | PASS |
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_PRG_T1_PRODUCT_REQUIREMENT_GOVERNANCE_CONTRACT_PROMOTION_FOR_CODEX_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Reference front door | `docs/reference/product_requirement_governance/README.md` | `Status: ACTIVE_REFERENCE` | PASS |
| Reference contract | `docs/reference/product_requirement_governance/CVF_PRG_PRODUCT_REQUIREMENT_CONTRACT.md` | `Status: ACTIVE_REFERENCE` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_PRG_T1_PRODUCT_REQUIREMENT_GOVERNANCE_CONTRACT_PROMOTION_COMPLETION_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason | no registry JSON authorized by PRG-T1 | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no registry Markdown authorized by PRG-T1 | BLOCKED with reason |
| External evidence digest | N/A with reason | external package was already audited by PRG-T0; no new digest artifact in T1 | N/A with reason |
| System loop interlock | this file | no loop, queue, daemon, runtime, generated aggregate, or automatic activation created | PASS |
| Session continuity | N/A with reason | material reference promotion does not change active mode; handoff marker for PRG-T0 was already synced at `67250e04` | N/A with reason |

## Claim Boundary

PRG-T1 promotes a documentation contract only. It does not implement validators,
fixtures, generated registries, runtime behavior, provider/live proof,
public-sync, package activation, certification, external adapters, or direct
Build authorization from product requirements.

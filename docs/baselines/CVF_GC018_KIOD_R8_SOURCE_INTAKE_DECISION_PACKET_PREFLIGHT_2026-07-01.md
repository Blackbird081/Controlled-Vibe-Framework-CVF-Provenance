# CVF GC-018 Baseline - KIOD-R8 Source Intake Decision Packet Preflight

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_BOUNDED

Batch ID: KIOD-R8

Dispatch base head: d77d5f52

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: Codex

Worker target: delegated external agent

## Purpose

Create a bounded guard foundation for future repo/folder knowledge-intake work:
an explicit source-intake decision packet standard plus a preflight checker that
blocks worker dispatch when the packet omits owner-surface, pre-scan, overlap,
negative-search, value-conversion, and claim-boundary decisions.

This baseline is a governance-foundation tranche only. It does not absorb
`EverMind-AI/EverOS`, `colbymchenry/codegraph`, or any other outside source.

## Scope

| Scope item | Disposition |
| --- | --- |
| Standard for source-intake decision packets | REQUIRED |
| Range-aware preflight checker | REQUIRED |
| Focused checker tests | REQUIRED |
| Autorun and local hook catalog wiring | REQUIRED |
| Worker return artifact | REQUIRED |
| Real repo/folder absorption pilot | FORBIDDEN_IN_THIS_TRANCHE |
| Runtime, package, Web, MCP, CLI, model-gateway, public-sync, or provider-live behavior | FORBIDDEN_IN_THIS_TRANCHE |

## Decision

| Decision item | Disposition |
| --- | --- |
| Dispatch KIOD-R8 | APPROVED_FOR_WORKER_DISPATCH |
| Worker commit authority | WORKER_MUST_NOT_COMMIT |
| Reviewer closure conversion | REQUIRED |
| Future source-intake pilot | REQUIRES_SEPARATE_SELECTION |

## Evidence

| Evidence item | Current value |
| --- | --- |
| Dispatch base | d77d5f52 |
| ADIF resolver | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch` returned zero candidates. |
| Collision search | R8 token search returned only synthetic R7 checker test fixture lines. |
| Planned paths | Planned R8 baseline, work order, standard, and checker paths did not already exist. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF-specific defect rows are required for this baseline. The worker must still read applicable checkers before writing any governed artifact. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `## Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `## External Knowledge Intake Routing`; `## Source Verification Block`; `## ADIF Defect Registry Disclosure`; `Reviewer Closure Conversion`; `Source intake decision packet: REQUIRED` |
| gateRunPurpose | Pre-dispatch confirmation evidence, not first discovery. |
| claimBoundary | This block records checker read-ahead for the GC-018 baseline only; worker implementation must repeat read-ahead before writing governed artifacts. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| KIOD owner-surface taxonomy is the existing source for owner surface selection. | EXISTS | `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md` | lines 30-55 | `Owner Surface Taxonomy` | KIOD-R1 taxonomy standard | ACCEPT |
| KIOD pre-scan packets are the existing source for bounded source intake before absorption. | EXISTS | `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md` | lines 30-57 | `Required Pre-Scan Packet` | KIOD-R2 pre-scan standard | ACCEPT |
| KIOD overlap routing dispositions already include owner-not-found and no-new-value cases. | VALUE_SET | `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | lines 28-37 | `CONFIRMED_EXISTING; ENRICH_EXISTING; NEW_FINDING; REJECT_DIRECT_IMPORT; NO_NEW_VALUE; OWNER_SURFACE_NOT_FOUND` | KIOD-R3 overlap routing matrix | ACCEPT |
| Outside-source intake artifacts already have required core block fields and disposition taxonomy. | EXISTS | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | lines 102-145 | `## External Absorption Core` | External Absorption Core Standard | ACCEPT |
| Value-conversion matrix columns and lane tokens are already source-defined. | VALUE_SET | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | lines 160-181 | `DOCTRINE_ADAPTED; PACKAGE_CANDIDATE; RUNTIME_CANDIDATE; CHECKER_CANDIDATE; REJECT_DIRECT_IMPORT; NO_PACKAGE_OR_RUNTIME_VALUE` | External Absorption Core Standard | ACCEPT |
| Overlap classification columns and disposition tokens are already source-defined. | VALUE_SET | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | lines 195-223 | `CONFIRMED_EXISTING; ENRICH_EXISTING; NEW_FINDING; REJECT_DIRECT_IMPORT; NO_NEW_VALUE; OWNER_SURFACE_NOT_FOUND` | External Absorption Core Standard | ACCEPT |
| Intake routing guard already defines required routing fields and allowed input-type values. | EXISTS | `governance/compat/check_external_knowledge_intake_routing.py` | constants near lines 22-52 | `REQUIRED_FIELDS; ALLOWED_INPUT_TYPES` | `check_external_knowledge_intake_routing.py` | ACCEPT |
| Checker read-ahead block field names are machine-checked. | VALUE_SET | `governance/compat/check_governed_artifact_checker_read_ahead.py` | constants near lines 20-39 | `applicableCheckersRead; literalTokensReviewed; gateRunPurpose; claimBoundary` | `check_governed_artifact_checker_read_ahead.py` | ACCEPT |
| WORKER_MUST_NOT_COMMIT dispatch packets require reviewer closure conversion. | EXISTS | `governance/compat/check_agent_handoff_boundary.py` | constants and validation around lines 38-54 and 305-320 | `Reviewer Closure Conversion` | `check_agent_handoff_boundary.py` | ACCEPT |
| Work orders can authorize guarded checker/catalog edits through Core Guard Self-Protection Authorization. | EXISTS | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | lines 742-756 | `Core Guard Self-Protection Authorization` | Work order template | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| R8 token collision search | `rg -n "KIOD-R8|SOURCE_INTAKE_DECISION_PACKET|Source Intake Decision Packet|Absorption Decision Packet" docs governance CVF_SESSION AGENTS.md` returned only synthetic R7 checker test fixture lines. | ACCEPT |
| Planned path existence | `Test-Path` returned `False` for the planned baseline, work order, standard, and checker paths. | ACCEPT |
| Existing overlap decision | No existing source-intake decision packet standard or checker is present. | ACCEPT |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | `external knowledge intake routing guard implementation` |
| Chain map route | Guard-foundation work for source-intake routing and decision discipline. |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/external_agent_review/` and `governance/compat/` |
| Disposition | GOVERNANCE_GUARD_FOUNDATION_ONLY |
| Claim boundary | This baseline authorizes a preflight guard for future source-intake dispatch packets. It does not authorize absorbing any outside source in this tranche. |

## Planned Worker Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/external_agent_review/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_STANDARD.md` | Create standard with exact packet shape, marker, required fields, lane tokens, and claim boundary. |
| `governance/compat/check_source_intake_decision_packet_preflight.py` | Create range-aware checker with `--base`, `--head`, and `--enforce`. |
| `governance/compat/test_source_intake_decision_packet_preflight.py` | Create focused pass/fail tests. |
| `governance/compat/agent_autorun_command_catalog.py` | Wire checker into autorun catalog. |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | Wire checker into reviewer-fast catalog. |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | Wire checker into pre-commit catalog. |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | Wire checker into pre-push catalog. |
| `docs/reviews/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_WORKER_RETURN_2026-07-01.md` | Worker return with command evidence and no commit. |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| GC-018 status | This baseline | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_2026-07-01.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_WORKER_RETURN_2026-07-01.md` | `Status: COMPLETE_PENDING_REVIEW`; accepted by reviewer/closer after repair | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_COMPLETION_2026-07-01.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason | no dedicated KIOD-R8 roadmap file is changed | N/A with reason |
| Registry JSON | N/A | no GC-051 or generated registry JSON mutation is authorized by this governance-checker preflight tranche | BLOCKED with reason: separate registry mutation work order required |
| Registry Markdown | N/A | no corpus or scan registry Markdown mutation is authorized by this governance-checker preflight tranche | BLOCKED with reason: separate registry mutation work order required |
| External evidence digest | N/A with reason | no outside-source evidence digest is produced | N/A with reason |
| System loop interlock | N/A with reason | no system loop interlock registry is changed | N/A with reason |
| Session continuity | active session surfaces | update after material commit in separate session-sync batch | PASS |

## Claim Boundary

This GC-018 baseline authorizes KIOD-R8 dispatch only. It does not claim that
future repo/folder absorption is complete, that any source package is ready for
runtime use, or that any provider/live governance behavior has been proven.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: KIOD-R8 is private provenance governance-foundation work. Public-sync is
outside this tranche.

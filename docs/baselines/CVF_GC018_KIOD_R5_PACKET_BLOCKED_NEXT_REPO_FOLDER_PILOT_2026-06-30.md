# CVF GC-018 - KIOD-R5 Packet-Blocked Next Repo/Folder Pilot

Memory class: FULL_RECORD

Status: HOLD_PENDING_OPERATOR_SOURCE_SELECTION

Date: 2026-06-30

docType: baseline

dispatchBaseHead: fad6e44c

Batch ID: KIOD-R5

## Purpose

Prepare the KIOD-R5 packet-blocked pilot boundary without dispatching a worker
before the operator selects the exact source repository or source folder.

KIOD-R5 exists because KIOD-R4 accepted `PACKET_BLOCK_REQUIRED_NOW`: the next
source-intake pilot must carry mandatory `Negative-search evidence` before any
novelty candidate, owner-missing row, or new-owner proposal is accepted.

This baseline is intentionally held. It does not authorize a worker to choose
the source target, run a scan, add a checker, import source material, create a
runtime, create an MCP/CLI adapter, build UI/dashboard surfaces, run provider
proof, public-sync, mutate generated aggregates, create package activation, or
claim production readiness.

## Scope

Allowed scope: record the KIOD-R5 hold boundary, source-selection gate, source
verification, and release criteria for the future packet-blocked pilot.

Forbidden scope: worker execution, source selection by an agent, checker
implementation, runtime/provider behavior, MCP/CLI adapter behavior, Web/UI,
public-sync, source import, generated aggregate edits, package lifecycle
mutation, or production-readiness claims.

## Baseline Decision

Decision: keep KIOD-R5 in `HOLD_PENDING_OPERATOR_SOURCE_SELECTION` until the
operator names exactly one source repository URL, local source mirror, or
folder path.

## Hold Gate

| Gate | Current value | Required release evidence |
| --- | --- | --- |
| Source repo/folder | not selected in this artifact | operator names exactly one source repo URL, local source mirror, or folder path |
| Source selection owner | operator | worker must not infer or choose the source target |
| Dispatch status | HOLD_PENDING_OPERATOR_SOURCE_SELECTION | may move only after sourceSelectionEvidence is recorded in the paired work order |
| Worker authority | none yet | dispatch requires a refreshed source-verified work order and pre-dispatch gate run |

## Authority Chain

| Authority | Source path | Verified line/section | Disposition |
| --- | --- | --- | --- |
| KIOD-T0 roadmap | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | lines 5, 33, 36, 91 | ACCEPT |
| KIOD-R4 decision | `docs/reviews/CVF_KIOD_R4_NEGATIVE_SEARCH_EVIDENCE_DECISION_COMPLETION_2026-06-30.md` | lines 24, 70-78, 186, 295 | ACCEPT |
| KIOD-R1 owner surface taxonomy | `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md` | lines 50-53, 61 | ACCEPT |
| KIOD-R2 pre-scan packet | `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md` | lines 37, 40, 46, 51, 62 | ACCEPT |
| KIOD-R3 routing matrix | `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | lines 34, 37, 45, 54 | ACCEPT |
| Dual-agent accounting | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | lines 45, 53-54, 117 | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| KIOD-R5 is the next roadmap lane | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | line 36 | `AUTHOR_KIOD_R5_GC018_FOR_PACKET_BLOCKED_NEXT_REPO_FOLDER_PILOT` | KIOD-T0 roadmap status | ACCEPT |
| KIOD-R5 applies to the next operator-selected repo/folder | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | line 91 | `operator-selected repo/folder` | KIOD-R5 roadmap row | ACCEPT |
| KIOD-R4 selected packet-block enforcement | `docs/reviews/CVF_KIOD_R4_NEGATIVE_SEARCH_EVIDENCE_DECISION_COMPLETION_2026-06-30.md` | line 24 | `PACKET_BLOCK_REQUIRED_NOW` | KIOD-R4 completion decision | ACCEPT |
| Negative-search evidence must precede owner-missing acceptance | `docs/reviews/CVF_KIOD_R4_NEGATIVE_SEARCH_EVIDENCE_DECISION_COMPLETION_2026-06-30.md` | lines 70-78 | `Negative-search evidence` | KIOD-R4 completion risk routing | ACCEPT |
| R1 stops when negative search evidence is absent | `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md` | line 52 | `negative search evidence` | KIOD-R1 owner surface checklist | ACCEPT |
| R2 novelty candidates need negative-search evidence | `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md` | line 40 | `Novelty candidates` | KIOD-R2 pre-scan packet standard | ACCEPT |
| R3 NEW_FINDING requires negative-search commands | `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | line 34 | `NEW_FINDING` | KIOD-R3 routing matrix | ACCEPT |
| Owner surface not found is a routeable disposition | `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | line 37 | `OWNER_SURFACE_NOT_FOUND` | KIOD-R3 routing matrix | ACCEPT |
| Both internal and external agent surfaces must be accounted | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | lines 45, 53-54, 117 | `INTERNAL_AGENT`; `EXTERNAL_AGENT_CLI_MCP` | Dual Agent Surface Matrix | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query:
`python governance/compat/run_adif_defect_resolver.py --task-class knowledge-intake-overlap-discipline --role dispatcher --lifecycle-phase pre-dispatch`

Returned defects: NONE_RETURNED

Resolver query: taskClass=`knowledge-intake-overlap-discipline`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

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

## Negative Search And Collision Discipline

The held packet names `OWNER_SURFACE_NOT_FOUND` only as a KIOD-R1/R2/R3
routeable disposition. It does not assert that any current source target lacks
an owner surface.

Release must add concrete negative-search commands or queries for the selected
source target before any novelty candidate, owner-missing row, or new-owner
proposal is accepted.

Search roots for release-time negative search: `docs`, `governance`,
`CVF_SESSION`, and selected source-target evidence.

Search command or structured query shape:
`rg -n --fixed-strings "<candidate term>" docs governance CVF_SESSION`

Coverage: release-time searches must cover source, tests when relevant, docs,
JSON/state records, and external evidence paths when they exist.

Same-token collision result: `CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD` is a
same-token occurrence in existing CVF references, not an absent claim.

Same-token collision result: `KIOD` is a same-token occurrence in existing CVF
KIOD artifacts, not an absent claim.

Same-token collision result: `NEW_FINDING` is a same-token occurrence in KIOD-R3
and overlap discipline surfaces, not an absent claim.

Same-token collision result: `OWNER_SURFACE_NOT_FOUND` is a same-token
occurrence in KIOD-R1/R2/R3 and overlap discipline surfaces, not an absent
claim.

Absent-versus-collision disposition: these tokens are binding KIOD vocabulary
and must not be interpreted as evidence that a selected source target has no
owner surface.

## Dual Agent Surface Matrix

| Consumer | Surface owner | Allowed use | Evidence or reason | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | future KIOD-R5 worker after operator source selection | may read this held packet as planning context only | this baseline and paired held work order | no execution, scan, commit, source import, or checker authority before release | HOLD_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future external adapter | no CLI/MCP ingress, execution, mutation, raw source release, or public behavior | no adapter is authorized by KIOD-R5 | separate GC-018/source-verified adapter work order required | DEFERRED_WITH_REASON |

## Release Criteria

Before this baseline can become dispatch-ready:

- The operator must name exactly one source repo URL, local source mirror, or
  folder path.
- The paired work order must record `sourceSelectionEvidence` with that exact
  target.
- The paired work order must include a concrete negative-search command plan
  against CVF owner surfaces.
- The dispatcher must rerun pre-dispatch gates on a real `--base` and `--head`
  range after the release edit.

## Evidence Verification

Held-packet verification commands:

- `python governance/compat/check_work_order_dispatch_quality.py --base fad6e44c --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base fad6e44c --head HEAD`

## Claim Boundary

This artifact is a held planning baseline only. It authorizes no worker scan,
checker implementation, runtime/provider behavior, MCP/CLI adapter, dashboard,
public-sync, source import, generated aggregate edit, automatic invocation,
action authority, package lifecycle mutation, or production-readiness claim.

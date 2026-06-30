# CVF GC-018 - KIOD-R5 Packet-Blocked Next Repo/Folder Pilot

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-30

docType: baseline

dispatchBaseHead: 49a0dd74

Batch ID: KIOD-R5

## Purpose

Authorize the KIOD-R5 packet-blocked pilot after the operator selected the
exact source repository and local source folder.

KIOD-R5 exists because KIOD-R4 accepted `PACKET_BLOCK_REQUIRED_NOW`: the next
source-intake pilot must carry mandatory `Negative-search evidence` before any
novelty candidate, owner-missing row, or new-owner proposal is accepted.

This baseline authorizes a documentation-only worker scan of the selected
source target. It does not authorize a worker to choose a different source
target, add a checker, import source material, create a runtime, create an
MCP/CLI adapter, build UI/dashboard surfaces, run provider proof, public-sync,
mutate generated aggregates, create package activation, or claim production
readiness.

## Scope

Allowed scope: dispatch the KIOD-R5 worker to inspect the selected EverOS
Controlled Memory Index Store source folder, compare it against existing CVF
EverOS T0-T5 owner surfaces, and return an uncommitted worker-return artifact.

Forbidden scope: worker execution, source selection by an agent, checker
implementation, runtime/provider behavior, MCP/CLI adapter behavior, Web/UI,
public-sync, source import, generated aggregate edits, package lifecycle
mutation, or production-readiness claims.

## Baseline Decision

Decision: release KIOD-R5 from hold because the operator selected
`https://github.com/EverMind-AI/EverOS.git` and the local source folder
`.private_reference/legacy/CVF 28.06/CVF Controlled Memory Index Store`.

Upstream repository HEAD was verified with
`git ls-remote https://github.com/EverMind-AI/EverOS.git HEAD` as
`0341f1230fef170d28d83c4295ab9d93570b0f2d`. The selected folder is a local
operator-provided package, not a folder present at the upstream repo root.

## Hold Gate

| Gate | Current value | Required release evidence |
| --- | --- | --- |
| Source repo/folder | `https://github.com/EverMind-AI/EverOS.git`; `.private_reference/legacy/CVF 28.06/CVF Controlled Memory Index Store` | satisfied by operator selection and command-backed verification |
| Source selection owner | operator | worker must not infer or choose a different source target |
| Dispatch status | DISPATCH_READY | worker may execute only this packet as `WORKER_MUST_NOT_COMMIT` |
| Worker authority | documentation-only scan and worker return | no source import, runtime, checker, or adapter implementation |

## Authority Chain

| Authority | Source path | Verified line/section | Disposition |
| --- | --- | --- | --- |
| KIOD-T0 roadmap | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | lines 5, 33, 36, 91 | ACCEPT |
| KIOD-R4 decision | `docs/reviews/CVF_KIOD_R4_NEGATIVE_SEARCH_EVIDENCE_DECISION_COMPLETION_2026-06-30.md` | lines 24, 70-78, 186, 295 | ACCEPT |
| KIOD-R1 owner surface taxonomy | `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md` | lines 50-53, 61 | ACCEPT |
| KIOD-R2 pre-scan packet | `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md` | lines 37, 40, 46, 51, 62 | ACCEPT |
| KIOD-R3 routing matrix | `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | lines 34, 37, 45, 54 | ACCEPT |
| Dual-agent accounting | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | lines 45, 53-54, 117 | ACCEPT |
| EverOS prior lane closure | `docs/reviews/CVF_EVEROS_T5_REMAINING_VALUE_AUDIT_AND_LANE_CLOSEOUT_2026-06-28.md` | lines 17-23, 80, 86-101, 187 | ACCEPT |
| EverOS source-selection history | `docs/roadmaps/CVF_EVEROS_T0_EXTERNAL_MEMORY_FOUNDATION_ABSORPTION_ROADMAP_2026-06-28.md` | lines 78-80, 121, 189-191 | ACCEPT |

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
| EverOS lane is already closed with no immediate next tranche | `docs/reviews/CVF_EVEROS_T5_REMAINING_VALUE_AUDIT_AND_LANE_CLOSEOUT_2026-06-28.md` | lines 21-23, 80, 120 | `CLOSE_EVEROS_ABSORPTION_LANE_NO_NEXT_TRANCHE` | EVEROS-T5 closeout | ACCEPT |
| Operator-provided package was previously advisory input | `docs/roadmaps/CVF_EVEROS_T0_EXTERNAL_MEMORY_FOUNDATION_ABSORPTION_ROADMAP_2026-06-28.md` | lines 78-80, 121 | `CVF Controlled Memory Index Store` | EVEROS-T0 roadmap | ACCEPT |

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
| Disposition | DISPATCH_READY |
| Claim boundary | selected-source worker scan only; no source import or implementation claim |

## Negative Search And Collision Discipline

The held packet names `OWNER_SURFACE_NOT_FOUND` only as a KIOD-R1/R2/R3
routeable disposition. It does not assert that any current source target lacks
an owner surface.

Worker must run concrete negative-search commands or queries for the selected
source target before any novelty candidate, owner-missing row, or new-owner
proposal is accepted.

Search roots for release-time negative search: `docs`, `governance`,
`CVF_SESSION`, and selected source-target evidence.

Search command or structured query shape:
`rg -n --fixed-strings "<candidate term>" docs governance CVF_SESSION`

Required selected-target queries include:

- `rg -n --fixed-strings "Controlled Memory Index Store" docs governance CVF_SESSION`
- `rg -n --fixed-strings "Memory Index Claim Boundary" docs governance CVF_SESSION`
- `rg -n --fixed-strings "Retrieval Receipt Contract" docs governance CVF_SESSION`
- `rg -n --fixed-strings "Memory Read Write Gate" docs governance CVF_SESSION`
- `rg -n --fixed-strings "SQLite Ledger Schema" docs governance CVF_SESSION`
- `rg -n --fixed-strings "LanceDB Vector Index" docs governance CVF_SESSION`
- `rg -n --fixed-strings "Index Rebuild And Recovery" docs governance CVF_SESSION`

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
| `INTERNAL_AGENT` | KIOD-R5 worker | may read the selected local source folder and produce an uncommitted worker return | this baseline and paired work order | no commit, source import, runtime, checker, adapter, or production claim | DISPATCH_READY_DOC_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future external adapter | no CLI/MCP ingress, execution, mutation, raw source release, or public behavior | no adapter is authorized by KIOD-R5 | separate GC-018/source-verified adapter work order required | DEFERRED_WITH_REASON |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| EverOS Controlled Memory Index Store local package | `docs/roadmaps/CVF_EVEROS_T0_EXTERNAL_MEMORY_FOUNDATION_ABSORPTION_ROADMAP_2026-06-28.md`; `docs/reviews/CVF_EVEROS_T5_REMAINING_VALUE_AUDIT_AND_LANE_CLOSEOUT_2026-06-28.md` | ENRICH_EXISTING | possible memory-index claim-boundary delta must be proven by full read and negative-search evidence | worker must classify each file or group; no direct import |

## External Absorption Core

External absorption core: REQUIRED

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/legacy/CVF 28.06/CVF Controlled Memory Index Store`; upstream context `https://github.com/EverMind-AI/EverOS.git` at `0341f1230fef170d28d83c4295ab9d93570b0f2d` |
| Enumeration command | `Get-ChildItem -LiteralPath '.private_reference/legacy/CVF 28.06/CVF Controlled Memory Index Store' -Recurse -File` |
| Manifest artifact or inline manifest | inline table below; paired work order `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R5_PACKET_BLOCKED_PILOT_2026-06-30.md` section Source Target Read Plan; worker return must include complete 26-file manifest |
| Processing ledger artifact or inline ledger | inline table below; worker return `docs/reviews/CVF_KIOD_R5_PACKET_BLOCKED_PILOT_WORKER_RETURN_2026-06-30.md` must include per-file processing ledger with terminal statuses |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/roadmaps/CVF_EVEROS_T0_EXTERNAL_MEMORY_FOUNDATION_ABSORPTION_ROADMAP_2026-06-28.md`; `docs/reviews/CVF_EVEROS_T5_REMAINING_VALUE_AUDIT_AND_LANE_CLOSEOUT_2026-06-28.md`; `governance/compat/check_memory_access_claim.py`; new owner proposals require negative-search evidence |
| Unresolved items | worker must report unresolved count; dispatch target has 26 files to account |
| Completion claim boundary | dispatch baseline only; no absorption closure, runtime, provider, package activation, source import, public-sync, or production claim |

Inline dispatch manifest:

| Source group | Count | Status |
| --- | --- | --- |
| `.private_reference/legacy/CVF 28.06/CVF Controlled Memory Index Store` | 26 | SELECTED_FOR_WORKER_READ |

Inline dispatch ledger:

| Source group | Terminal status at dispatch | Count |
| --- | --- | --- |
| selected local folder | DEFERRED | 26 |

## Mandatory Blind-Spot Control Block

| Gate | Evidence |
| --- | --- |
| Gate 1: absorption source enumerated | dispatch enumeration found 26 files under selected local folder |
| Gate 2: all files listed | worker return must list all 26 selected-source files |
| Gate 3: each file has terminal status | worker return must assign terminal status to every file or group |
| Gate 4: reconciliation passes | reviewer must compare manifest count and ledger terminal count |
| Gate 5: adapted/deferred items traced | worker must trace any adapted/deferred item to CVF owner surface or blocker |
| Blind-spot verdict | CLEAR_FOR_DISPATCH_ONLY_WITH_WORKER_FULL_MANIFEST_REQUIRED |

## Corpus Completeness And Report Integrity

- Corpus task class: SELECTED_EXTERNAL_FOLDER_WORKER_DISPATCH
- Corpus root: `.private_reference/legacy/CVF 28.06/CVF Controlled Memory Index Store`
- Snapshot time: 2026-06-30 dispatcher verification
- Enumeration command: `Get-ChildItem -LiteralPath '.private_reference/legacy/CVF 28.06/CVF Controlled Memory Index Store' -Recurse -File`
- Manifest artifact or inline manifest: inline table below; paired work order `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R5_PACKET_BLOCKED_PILOT_2026-06-30.md` section Source Target Read Plan; worker return must include complete manifest
- Manifest hash: NOT_APPLICABLE_WITH_REASON: dispatch records file count and path target only; worker computes any required hash after full read
- Processing ledger artifact or inline ledger: inline table below; worker return `docs/reviews/CVF_KIOD_R5_PACKET_BLOCKED_PILOT_WORKER_RETURN_2026-06-30.md` required
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE
- Reconciliation: manifest=26; ledger_terminal=26; exclusions=0; unresolved=0 required before reviewer acceptance
- Unresolved files: 0 required before reviewer acceptance; dispatch has 26 pending worker-read files
- Declared exclusions: none at dispatch
- Unreadable or unsupported files: worker must report
- Aggregation check: worker return must sum statuses to manifest count
- Drift check: worker records current `git status --short` and source target evidence
- Output traceability: worker maps any value to existing EverOS T0-T5 owner surfaces or `OWNER_SURFACE_NOT_FOUND`
- Adversarial verification: duplicate EverOS T0-T5 material must be marked `CONFIRMED_EXISTING` or `NO_NEW_VALUE`
- Corpus verdict: PARTIAL - dispatch authorizes worker corpus read; no absorption closure claim is made here

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| Selected local Controlled Memory Index Store folder | possible memory-index and receipt-boundary deltas | DOCTRINE_ADAPTED | existing EverOS T0-T5 owner surfaces unless negative search proves a gap | worker classifies; reviewer decides whether doctrine enrichment is needed | no runtime, vector store, SQLite, checker, adapter, or direct import |
| Reusable memory-index operating pattern | possible future package or skill contract only if full read proves reusable agent-facing value | PACKAGE_CANDIDATE | conditional future package lane only after reviewer acceptance | no package work in KIOD-R5; return candidate evidence only | no package activation, registry mutation, or package body read |
| EverOS runtime/server/vector/database material | implementation-shaped source material | RUNTIME_CANDIDATE | T5 rejected or deferred runtime-shaped lanes | record as deferred/rejected with concrete reopen condition if value remains | no runtime/provider behavior |
| Memory-index claim-boundary checker concept | possible checker candidate from bundled checker/test pair | CHECKER_CANDIDATE | future checker work order only if reviewer accepts gap evidence | no checker implementation in KIOD-R5 | no guard wiring or hook mutation |
| Source implementation files and generated artifacts | external source code must not be copied into CVF | REJECT_DIRECT_IMPORT | CVF-owned rewrite only through future governed work | reject direct import | no direct import |
| Duplicates of EverOS T0-T5 absorbed doctrine | already absorbed value | NO_PACKAGE_OR_RUNTIME_VALUE | existing EverOS T0-T5 artifacts | record as duplicate with negative-search evidence | no new lane |

## Release Criteria

Dispatch release criteria:

- The operator selected exactly one source repo and local source folder.
- The paired work order records `sourceSelectionEvidence` with that exact
  target.
- The paired work order includes a concrete negative-search command plan
  against CVF owner surfaces.
- The dispatcher reruns pre-dispatch gates on a real `--base` and `--head`
  range after this release edit.

## Evidence Verification

Held-packet verification commands:

- `python governance/compat/check_work_order_dispatch_quality.py --base 49a0dd74 --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 49a0dd74 --head HEAD`

## Claim Boundary

This artifact is a held planning baseline only. It authorizes no worker scan,
checker implementation, runtime/provider behavior, MCP/CLI adapter, dashboard,
public-sync, source import, generated aggregate edit, automatic invocation,
action authority, package lifecycle mutation, or production-readiness claim.

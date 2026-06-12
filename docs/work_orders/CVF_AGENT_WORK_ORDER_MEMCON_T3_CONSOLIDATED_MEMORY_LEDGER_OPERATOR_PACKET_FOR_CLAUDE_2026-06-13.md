# CVF Agent Work Order - MEMCON-T3 Consolidated Memory Ledger And Operator Packet

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-06-13

Owner: Codex

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `c454921a`

executionBaseHead: `c454921a`

closureBaseHead: `WORKER_MUST_NOT_SET`

sourceAuthority:
`docs/baselines/CVF_GC018_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_2026-06-13.md`

rawMemoryReleased=false

completionReviewPath:
`docs/reviews/CVF_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:
`docs/reviews/CVF_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_COMPLETION_2026-06-13.md`;
`CVF_SESSION/ACTIVE_SESSION_STATE.json`;
`CVF_SESSION/state/**`;
`CVF_SESSION_MEMORY.md`;
`AGENT_HANDOFF_V18_2026-06-12.md`

GC-018:
`docs/baselines/CVF_GC018_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_2026-06-13.md`

Parent roadmap:
`docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`

## Purpose

Create the MEMCON-T3 documentation artifacts that make memory consolidation
operator-visible before any retrieval-pack integration work begins.

Claude must define a consolidated memory ledger contract, a Markdown-first
operator-visible review packet structure, and bounded fixtures that prove the
packet renders active, stale, conflicted, pruned or rejected, and
time-ambiguous memory entries as distinct categories.

This tranche is documentation-first and fixture-only. It does not implement
runtime memory behavior, storage, retrieval packaging, provider/API calls,
OCR, Policy_Local mutation, public-sync, or raw memory release.

## Authority Chain

| Authority | Path / evidence | Disposition |
| --- | --- | --- |
| Operator request | operator asked Codex to create a Claude work order for continued MEMCON work | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V18_2026-06-12.md` | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | ACCEPT |
| T1a MEMCON standard | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | ACCEPT |
| T1b schema appendix | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | ACCEPT |
| T2 checker | `governance/compat/check_memory_consolidation_artifact_quality.py` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_2026-06-13.md` | ACCEPT |

## Agent Roles

| Role | Agent | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | dispatches work order and baseline only |
| Worker | Claude | creates allowed-scope artifacts and returns uncommitted |
| Reviewer / closer | Codex | reviews, fixes only reviewer-owned issues, runs closure gates, commits |

## Intake Role Routing Decision

Intake summary: operator asked Codex to create the next work order for Claude
after MEMCON-T2 closed.

Scope classification: bounded documentation and fixture design for the memory
consolidation workflow chain.

Risk sensitivity: medium governance risk because the artifact shapes later
memory retrieval packaging, but this work order authorizes no runtime behavior,
provider/API proof, public-sync, secret handling, legal claim, production
claim, or readiness claim.

Selected route mode: MULTI_AGENT_MULTI_ROLE.

Role separation basis: Claude acts as implementation worker under
`WORKER_MUST_NOT_COMMIT`; Codex remains reviewer, closer, and committer.

Escalation condition: return to Codex if implementation requires forbidden
paths, runtime memory behavior, generated JSON aggregate architecture, external
workspace mutation, Policy_Local mutation, provider/API proof, public-sync,
operator evidence, or a wider claim boundary.

Reason: T3 creates governance-facing memory artifacts that later tranches may
consume. Multi-agent separation keeps worker drafting separate from reviewer
closure and session-state authority.

## Required First Reads

Claude must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V18_2026-06-12.md`
4. `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`
5. `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md`
6. `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md`
7. `governance/compat/check_memory_consolidation_artifact_quality.py`
8. this work order

## Startup Acknowledgment Required

Claude must begin with:

`Startup acknowledged: current mode=memcon_t3_consolidated_memory_ledger_operator_packet_dispatched; active handoff=AGENT_HANDOFF_V18_2026-06-12.md; work order=MEMCON-T3; next allowed move=Claude creates allowed-scope MEMCON-T3 artifacts under WORKER_MUST_NOT_COMMIT and returns uncommitted; parked checkpoint=Policy_Local PL-S1, EC/T12, DEP2/Redis/receipt-anchor remain parked.`

## Commit Mode And Base-Anchor Lifecycle

| Anchor | Value | Owner | Disposition |
| --- | --- | --- | --- |
| dispatchBaseHead | `c454921a` | Codex | ACCEPT |
| executionBaseHead | `c454921a` | Claude | ACCEPT |
| closureBaseHead | `WORKER_MUST_NOT_SET` | Codex reviewer | ACCEPT |
| Commit mode | `WORKER_MUST_NOT_COMMIT` | Codex | ACCEPT |

Claude must not commit. Claude must record the worker-return base/head and
`git status --short` output in the worker-return packet.

## Dependency Release Evidence

| Dependency | Required evidence | Disposition |
| --- | --- | --- |
| MEMCON-T1a standard closure | material commit `84a46b62`; standard path `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | ACCEPT |
| MEMCON-T1b schema closure | material commit `f94d2fbd`; schema path `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | ACCEPT |
| MEMCON-T2 checker closure | material commit `f83aa7d8`; session sync `c454921a`; checker path `governance/compat/check_memory_consolidation_artifact_quality.py` | ACCEPT |
| Fresh MEMCON-T3 baseline | `docs/baselines/CVF_GC018_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_2026-06-13.md` | ACCEPT |

## Current Runtime Freshness Verification

This tranche does not implement runtime memory. Claude must refresh the
documentation and checker anchors before editing:

```powershell
rg -n "MEMCON-T3 Detail|Operator-Visible Memory Review Packet|rawMemoryReleased|sourceAuthority" docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md
rg -n "OperatorMemoryReviewPacket Field Table|Promotion And Blocking Rules|publicExportDisposition|rawMemoryReleased" docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md
rg -n "MEMCON_MARKERS|SOURCE_AUTHORITY_MARKERS|OPERATOR_PACKET_REQUIRED_SECTIONS|RETRIEVAL_BOUNDARY_MARKER" governance/compat/check_memory_consolidation_artifact_quality.py
```

## Pre-Flight Checks

Claude must run these before editing:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base c454921a --head HEAD
```

If the pre-implementation gate fails only on allowed-scope artifacts, Claude
must repair and rerun under the Worker Autonomy rule. If the failure is outside
allowed scope, Claude must return to Codex.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| T3 deliverable is the consolidated memory ledger and Markdown-first operator packet | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | `MEMCON-T3 Detail` | `MEMCON-T3` | MEMCON roadmap | ACCEPT |
| T3 requires sample fixtures for active, stale, conflicted, pruned, and time-ambiguous memories | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | `MEMCON-T3 Detail` | `sample fixtures` | MEMCON roadmap | ACCEPT |
| JSON or generated aggregate ledger is conditional on append-heavy need | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | `MEMCON-T3 Detail` | `JSON` | MEMCON roadmap | ACCEPT |
| Operator-visible packet must be Markdown-first | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | `Operator-Visible Memory Review Packet` | `Operator-Visible Memory Review Packet` | MEMCON T1a standard | ACCEPT |
| Operator packet must expose active, candidate, conflict, stale, temporal ambiguity, pruning, preview, action, and claim-boundary sections | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | `Operator-Visible Memory Review Packet` | `Operator-Visible Memory Review Packet` | MEMCON T1a standard | ACCEPT |
| Retrieval-facing memory output must keep raw release false | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | `Retrieval Eligibility Rule` | `rawMemoryReleased` | MEMCON T1a standard | ACCEPT |
| Consolidated records require source authority | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | `ConsolidatedMemoryRecord Field Table` | `sourceAuthority` | ConsolidatedMemoryRecord | ACCEPT |
| OperatorMemoryReviewPacket fields are source-defined | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | `OperatorMemoryReviewPacket Field Table` | `OperatorMemoryReviewPacket` | MEMCON T1b schema appendix | ACCEPT |
| OperatorMemoryReviewPacket includes public export disposition | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | `OperatorMemoryReviewPacket Field Table` | `publicExportDisposition` | OperatorMemoryReviewPacket | ACCEPT |
| Source authority must be non-empty for promotion | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | `Promotion And Blocking Rules` | `sourceAuthority` | MEMCON T1b schema appendix | ACCEPT |
| Every retrieval-facing shape carries raw release false | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | `Promotion And Blocking Rules` | `rawMemoryReleased` | MEMCON T1b schema appendix | ACCEPT |
| T2 checker requires source authority markers on changed MEMCON artifacts | `governance/compat/check_memory_consolidation_artifact_quality.py` | constants and validator rules | `SOURCE_AUTHORITY_MARKERS` | MEMCON artifact quality checker | ACCEPT |
| T2 checker requires operator packet sections on changed MEMCON review packets | `governance/compat/check_memory_consolidation_artifact_quality.py` | constants and validator rules | `OPERATOR_PACKET_REQUIRED_SECTIONS` | MEMCON artifact quality checker | ACCEPT |
| T2 checker requires retrieval boundary marker on retrieval-facing changed MEMCON artifacts | `governance/compat/check_memory_consolidation_artifact_quality.py` | constants and validator rules | `RETRIEVAL_BOUNDARY_MARKER` | MEMCON artifact quality checker | ACCEPT |
| Generated JSON aggregates require source layout and deterministic generator | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | generated aggregate requirements | `generator` | JSON generated aggregate discipline standard | ACCEPT |

## Evidence Reuse And Encoding Plan

Claude may reuse the source anchors listed above without reprinting long
quoted passages. All new prose must default to ASCII. If a source excerpt
contains non-ASCII characters, Claude must either paraphrase in ASCII or record
the explicit evidence-quote exception in the worker-return packet.

## New Files To Create

| Path | Required content |
| --- | --- |
| `docs/reference/CVF_MEMORY_CONSOLIDATION_LEDGER_OPERATOR_PACKET_CONTRACT_2026-06-13.md` | Markdown-first ledger and operator packet contract |
| `docs/reviews/CVF_MEMCON_T3_OPERATOR_MEMORY_REVIEW_PACKET_SAMPLE_2026-06-13.md` | bounded sample packet proving distinct memory categories |
| `docs/reviews/CVF_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_WORKER_RETURN_2026-06-13.md` | worker return packet with proof manifest |

## Allowed Implementation Scope

Claude may modify:

- `docs/reference/CVF_MEMORY_CONSOLIDATION_LEDGER_OPERATOR_PACKET_CONTRACT_2026-06-13.md`
- `docs/reviews/CVF_MEMCON_T3_OPERATOR_MEMORY_REVIEW_PACKET_SAMPLE_2026-06-13.md`
- `docs/reviews/CVF_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_WORKER_RETURN_2026-06-13.md`
- this work order only for worker-return status evidence if needed
- parent roadmap row only to mark worker-return status, not final closure

Claude must not modify:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/**`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`
- `EXTENSIONS/`
- Policy_Local or any external workspace
- public-sync
- provider key files
- generated JSON aggregates unless Claude returns a scoped generator/source
  layout recommendation for Codex review

## Allowed / Forbidden Scope

Allowed scope is exactly the paths listed in `Allowed Implementation Scope`.
Forbidden scope is exactly the paths and behaviors listed under `Claude must
not modify` plus the non-goals in the claim boundary.

## Write Ownership

Claude owns worker implementation changes only until return:

- T3 contract document;
- T3 sample operator packet;
- T3 worker-return packet;
- optional status evidence inside this work order or parent roadmap row.

Codex owns closure conversion:

- completion review path;
- session state, handoff, and front-door sync;
- final roadmap closure status;
- commits.

## Execution Plan

1. Read the required first-read files and record the startup acknowledgment.
2. Run the pre-flight commands from this work order.
3. Draft the reference contract with ledger fields, category rendering rules,
   operator actions, retrieval preview boundary, and claim boundary.
4. Draft the sample operator review packet with one bounded fixture row for
   each required category.
5. Draft the worker-return packet with changed-file evidence, proof results,
   fulfillment manifest, and no-commit statement.
6. Run the Required Proof Manifest commands.
7. Leave artifacts uncommitted and return to Codex.

## Evidence Requirements

Claude must provide:

- changed-file evidence from `git status --short`;
- command evidence for the pre-implementation gate, MEMCON checker,
  reviewer-fast, and pre-commit;
- file evidence for the contract, sample packet, and worker return;
- explicit `N/A with reason` for runtime, live proof, public-sync, JSON
  aggregate, provider/API, OCR, and Policy_Local evidence;
- statement that no commit was created by Claude.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Contract artifact | Created at the required reference path |
| Sample packet artifact | Created at the required review path |
| Worker-return artifact | Created at the required review path |
| Required sample categories | Active, new candidate, conflict, stale, pruned/rejected, and temporal ambiguity are distinct |
| Source authority | Every durable memory-like record has non-empty source authority or is blocked |
| Raw release boundary | Retrieval-facing sections include `rawMemoryReleased=false` |
| Public export disposition | Changed MEMCON review artifacts include a valid disposition |
| JSON aggregate boundary | No hand-edited large JSON aggregate is created |
| Worker commit boundary | Claude returns uncommitted artifacts |

## Worker Autonomy / No-Question Rule

Worker-Autonomy / No-Question Rule: any governance gate failure within allowed
scope must be repaired and rerun by Claude without asking the operator. Claude
must return to Codex only when repair would exceed allowed scope, touch
forbidden paths, alter the claim boundary, consume provider/API quota, mutate
external workspaces, or require operator evidence.

## Required Artifact Content

The contract document must include:

- ledger purpose and authority chain;
- `MemoryCandidate` and `ConsolidatedMemoryRecord` usage boundaries;
- record status categories for active, new candidate, conflicted,
  stale/outdated, pruned/rejected, and temporal ambiguity blocks;
- source-authority requirements;
- conflict and staleness rendering rules;
- temporal ambiguity rendering rule;
- retrieval preview boundary with `rawMemoryReleased=false`;
- operator action table;
- claim boundary;
- Public Export Disposition.

The sample review packet must include these exact operator-visible sections:

- Active Consolidated Memories
- New Candidate Memories
- Conflicts Requiring Decision
- Stale Or Outdated Memories
- Pruned Or Rejected Noise
- Temporal Ambiguity Blocks
- Retrieval-Eligible Pack Preview
- Operator Actions Required
- Claim Boundary
- Public Export Disposition

The sample packet must contain at least one bounded fixture row for each of:

- active memory;
- new candidate memory;
- conflicted memory;
- stale or outdated memory;
- pruned or rejected noise;
- temporal ambiguity block.

Every retrieval-facing section must include `rawMemoryReleased=false`.

## JSON Aggregate Boundary

Default route: do not create JSON aggregates in T3.

If Claude determines a JSON ledger is required, Claude must stop short of
hand-editing a large aggregate and return a design note naming:

- compact source directory;
- generator path;
- drift-check command;
- owner of generated aggregate closure.

Codex will decide whether to open a separate generated-aggregate work order.

## Required Proof Manifest Atomic Literal Discipline

Each Required Proof Manifest row below contains one command literal only.
Claude must keep new proof rows atomic.

## Required Proof Manifest

| Proof item | Command literal | Required result |
| --- | --- | --- |
| Worktree start state | `git status --short` | records actual worker start state |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base c454921a --head HEAD` | PASS or source-scoped return |
| MEMCON checker | `python governance/compat/check_memory_consolidation_artifact_quality.py --base c454921a --head HEAD --enforce` | PASS |
| Reviewer-fast early filter | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS |
| Pre-commit hook chain | `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit` | PASS |
| Worker return state | `git status --short` | lists uncommitted worker artifacts |

## Required Artifact Manifest

| Artifact | Owner | Required state at worker return |
| --- | --- | --- |
| `docs/reference/CVF_MEMORY_CONSOLIDATION_LEDGER_OPERATOR_PACKET_CONTRACT_2026-06-13.md` | Claude | created or updated |
| `docs/reviews/CVF_MEMCON_T3_OPERATOR_MEMORY_REVIEW_PACKET_SAMPLE_2026-06-13.md` | Claude | created or updated |
| `docs/reviews/CVF_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_WORKER_RETURN_2026-06-13.md` | Claude | created or updated |
| `docs/reviews/CVF_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_COMPLETION_2026-06-13.md` | Codex | reviewer-owned closure artifact |

## Work-Order Fulfillment Manifest

Claude must include this table in the worker-return packet:

| Requirement | Evidence path or command | Worker disposition |
| --- | --- | --- |
| Contract document created | path and summary | PASS or BLOCKED |
| Sample packet created | path and summary | PASS or BLOCKED |
| Distinct category fixtures present | path and category list | PASS or BLOCKED |
| rawMemoryReleased boundary present | command or file evidence | PASS or BLOCKED |
| MEMCON checker run | command result | PASS or BLOCKED |
| reviewer-fast run | command result | PASS or BLOCKED |
| pre-commit run | command result | PASS or BLOCKED |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Evidence expected |
| --- | --- | --- |
| Markdown review packet for operator inspection | create sample review packet with required sections | `docs/reviews/CVF_MEMCON_T3_OPERATOR_MEMORY_REVIEW_PACKET_SAMPLE_2026-06-13.md` |
| Ledger and packet contract | create reference contract document | `docs/reference/CVF_MEMORY_CONSOLIDATION_LEDGER_OPERATOR_PACKET_CONTRACT_2026-06-13.md` |
| Active fixture | sample packet active row | sample review packet |
| Stale fixture | sample packet stale/outdated row | sample review packet |
| Conflicted fixture | sample packet conflict row | sample review packet |
| Pruned fixture | sample packet pruned/rejected row | sample review packet |
| Time-ambiguous fixture | sample packet temporal ambiguity block row | sample review packet |
| JSON aggregate discipline | keep default Markdown-first route or return source-layout recommendation | worker-return packet |

## Worker Return Packet Requirements

Claude must return uncommitted artifacts and include:

- startup acknowledgment;
- base/head anchors;
- changed file list;
- Required Proof Manifest results;
- Work-Order Fulfillment Manifest;
- unresolved issues, if any;
- explicit statement that Claude did not commit;
- claim boundary;
- Public Export Disposition.

## Review Gate

Codex must not close this work order until reviewer gates pass on the actual
worker-return range and the worker-return packet records the uncommitted
artifact state.

## Reviewer Closure Conversion

Codex owns reviewer closure. Codex may add the completion review path, update
session state/front door/handoff, update final roadmap closure status, and
commit only after closure gates pass.

## Machine Closure Package

Worker-return evidence must be machine-checkable:

- `git diff --name-status` or equivalent changed-file evidence;
- `git status --short` showing worker-return state;
- MEMCON checker output;
- reviewer-fast output;
- pre-commit output;
- explicit `N/A with reason` for runtime, live proof, public-sync, JSON
  aggregate, and provider/API evidence.

## Closure Checklist

| Closure item | Owner | Required disposition |
| --- | --- | --- |
| Worker-return packet complete | Claude | PASS or BLOCKED |
| MEMCON checker evidence present | Claude | PASS or BLOCKED |
| Reviewer-fast evidence present | Claude | PASS or BLOCKED |
| Pre-commit evidence present | Claude | PASS or BLOCKED |
| Completion review authored | Codex | reviewer-owned |
| Session state/front door/handoff synced | Codex | reviewer-owned |
| Final commit created | Codex | reviewer-owned |

## Return-To-Orchestrator Conditions

Claude must return to Codex rather than widening scope if any condition appears:

- generated JSON aggregate becomes necessary;
- runtime memory behavior changes are needed;
- retrieval integration is needed;
- Policy_Local or external workspace changes are needed;
- provider/API proof or secrets are needed;
- public-sync is needed;
- session state or active handoff changes are needed;
- operator evidence is needed;
- a governance gate fails outside allowed scope.

## Operator Checkpoint

No operator checkpoint is required for Claude to execute the allowed-scope T3
documentation and fixture work. Operator checkpoint is required before
Policy_Local PL-S1, EC activation, retrieval integration, public-sync,
provider/API proof, T12 unlock, high-risk promotion, memory reinjection, or
autonomous mutation.

## Export Surface Decision

This is private provenance work. Do not copy artifacts to public-sync and do
not make a public catalog claim from T3.

## Claim Boundary

This work order authorizes documentation and fixture design for MEMCON-T3 only.
It does not claim runtime memory implementation, storage, retrieval behavior,
semantic memory correctness, production readiness, public readiness, live
governance behavior, provider/API proof, OCR, Policy_Local mutation, EC
activation, corpus ingestion, T12 unlock, memory reinjection, high-risk
promotion, or autonomous mutation.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

No public-sync artifact exists for this private dispatch. Public export is a
separate authorization path.

## Dispatch Packet Authoring Learning Promotion

This work order carries forward the current CVF dispatch controls: source
verification before worker execution, dependency release evidence, worker
autonomy for allowed-scope gate failures, atomic proof rows, reviewer-owned
closure for `WORKER_MUST_NOT_COMMIT`, and explicit generated-aggregate
boundary handling.

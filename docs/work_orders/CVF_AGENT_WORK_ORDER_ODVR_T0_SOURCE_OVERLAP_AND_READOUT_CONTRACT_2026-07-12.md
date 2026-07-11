# CVF Agent Work Order - ODVR-T0 Source Overlap And Readout Contract

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-07-12

Batch ID: ODVR-T0-DISPATCH

dispatchBaseHead: `933f7a420`

executionBaseHead: `c691e4fe4`

closureBaseHead: `c691e4fe4`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: independent reviewer

## Dispatch Prompt Envelope

Role: delegated worker for ODVR-T0.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ODVR_T0_SOURCE_OVERLAP_AND_READOUT_CONTRACT_2026-07-12.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture exact HEAD before any edit and record it in the
worker return.

Current-time notes: artifact date is 2026-07-12; source and overlap claims must
be refreshed at execution start.

Do-not-misread notes: this is a docs/schema overlap decision, not permission to
build a composer, CLI, UI, dashboard, provider integration, or truth store. Do
not spawn subagents, commit, change session state, or touch public-sync.

Required first actions: complete startup reads, capture HEAD/status, read the
paired baseline and checker sources, run the named ADIF query, then independently
source-verify all four existing owner families before editing.

Return contract: create the named worker return, run required verification,
leave all changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Produce the source/overlap inventory, field authority map, freshness and
contradiction semantics, and JSON contract that decide whether ODVR-T1 has a
non-duplicate implementation target.

## Authority Chain

1. `AGENTS.md` and active session front doors.
2. Paired GC-018 baseline and this work order.
3. ODVR roadmap at material commit `7c6f13ab8`.
4. Current generated active-session owner and current runtime/read-model source.
5. Canonical AHB and agent-workspace contracts.
6. Completion reviews and state entries as bounded evidence, never substitutes
   for current runtime source when source exists.

## Agent Roles

- delegated worker: source verification, overlap classification, contract/schema
  authoring, validation, and worker return; no commit.
- independent reviewer: designated closer, allowed-scope repair owner,
  material commit owner, and closure decision owner.
- session-sync steward: separate post-closure phase only.

## Scope / Target / Owner Boundary

### Allowed deliverables

- `docs/reference/operator_decision_value_readout/README.md`
- `docs/reference/operator_decision_value_readout/CVF_ODVR_T0_SOURCE_OVERLAP_AND_READOUT_CONTRACT.md`
- `docs/reference/operator_decision_value_readout/CVF_ODVR_T0_READOUT_SCHEMA.json`
- `docs/reviews/CVF_ODVR_T0_SOURCE_OVERLAP_AND_READOUT_CONTRACT_WORKER_RETURN_2026-07-12.md`

### Forbidden scope

No runtime composer, Python/TypeScript implementation, executable CLI, Web/UI,
dashboard, route wiring, provider/API call, live proof, mutable/generated state,
queue, registry, checker/hook/CI wiring, session front-door change, roadmap
mutation, public-sync, outside-source intake, or ODVR-T1/T2 work.

## Write Ownership

Worker may change exactly the four allowed deliverables. Existing source,
roadmap, baseline, work order, governance, and session files are read-only. Any
required fifth path returns to orchestrator.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| ODVR roadmap authorization | `7c6f13ab8`; roadmap `Status: PROPOSED`; `Next Allowed Move` names T0 packet | SATISFIED |
| Session routing | `933f7a420`; generated bootstrap names ODVR-T0 packet authoring | SATISFIED |
| Existing owner availability | all paths and symbols in paired Source Verification Block exist at dispatch source audit | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ODVR-T0 --title "Operator Decision And Value Readout Source Overlap And Contract" --date 2026-07-12 --base 933f7a420 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SATISFIED: ODVR roadmap PROPOSED at material commit 7c6f13ab8 and session routing current at 933f7a420" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced all placeholders with ODVR-T0 source-backed controls |
| checkerReadAheadConfirmation | named checker sources read before authoring |
| docOnlyNewFields | proposed ODVR fields must be listed in a separate New Doc-Only Fields table and schema |
| claimBoundary | dispatch provenance only |

## Required First Reads

Read the mandatory startup sequence, guard orientation, literal gotchas,
repository boundary, paired baseline, this work order, ODVR roadmap, active AHB
ratification, agent-workspace front door/topology contract, active-session
generator, MAO-T7 evidence readout, MLW-NRD1 decision readout, Web Workspace
server read model, local workspace projection closure entry, MAO-LIVE roadmap,
commit-steward standard, and all checker sources named below.

## Pre-Flight Checks

Capture `git rev-parse --short HEAD` and `git status --short`. Confirm the four
allowed paths and that HEAD equals the committed dispatch HEAD supplied by the
orchestrator. Run `Test-Path` and `rg` for every planned artifact/symbol. Stop on
an unexpected collision or dirty unrelated path.

## Worker Autonomy / No-Question Rule

Repair allowed-scope validation failures directly by reading the failing
contract/checker. Return only for source contradiction, forbidden-path need,
existing full-owner discovery, or missing canonical authority.

## Source Verification Block

Use the paired baseline table as the starting inventory, then independently
re-run all searches. The contract output must classify each proposed readout
field as `REUSE`, `COMPOSE`, `OMIT`, or `BLOCKED_SOURCE_NOT_FOUND`, name its
canonical owner, and provide direct source evidence. Existing-source claims use
only `ACCEPT`, `REJECT`, or `BLOCKED_SOURCE_NOT_FOUND` in their source table.

New ODVR field names are doc-only proposals. List them separately with type,
required/optional status, source derivation, freshness rule, and contradiction
behavior; do not represent them as existing runtime fields.

## Negative Search And Collision Discipline

Search repo-wide for `ODVR`, `Decision And Value Readout`, every proposed field,
the three planned material paths, and semantically equivalent operator summary
contracts. Record exact commands and terminal dispositions. A full existing
owner triggers the roadmap stop rule.

### Pre-Dispatch Negative Search Evidence

| Field | Evidence |
|---|---|
| Exact search command or query | `rg -n -i --glob '*.ts' --glob '*.tsx' --glob '*.py' --glob '*.md' --glob '*.json' --glob '*.jsonl' -- '<term>' EXTENSIONS docs CVF_SESSION governance .private_reference` |
| Exact search roots | `EXTENSIONS`; `docs`; `CVF_SESSION`; `governance`; `.private_reference` |
| Coverage | runtime source, tests, governed docs, JSON/generated state, and private external-evidence history |
| `ODVR` collision result | authoritative occurrences exist in the ODVR roadmap and current session-routing artifacts; runtime-owner status remains a separate semantic disposition |
| `Decision And Value Readout` collision result | exact-token result classified `REQUIRES_SEMANTIC_OWNER_REVIEW`; semantic owner searches control the disposition |
| `REUSE` collision result | many unrelated docs/state occurrences; classification vocabulary only, not an existing ODVR field |
| `COMPOSE` collision result | unrelated docs/state occurrences plus current roadmap prose; classification vocabulary only |
| `OMIT` collision result | unrelated docs/state occurrences; classification vocabulary only |
| Planned path collision result | `CLEAR_FOR_PLANNED_NEW_PATH` at dispatch; worker refreshes `Test-Path` before editing |
| Same-token disposition | every collision is recorded as authoritative ODVR routing, narrower semantic owner, or unrelated occurrence; no bare token absence is treated as semantic absence |

## Current Runtime Freshness Verification

Refresh all Source Verification rows at execution start. Inspect actual exports
and consumers for MAO-T7, MLW-NRD1, and the Web Workspace read model. Verify the
generated active-session source layout rather than hand-editing or treating the
aggregate as an authoring source. No implementation absence claim may rely only
on filename search; include semantic token and symbol searches.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture-contract`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Worker rerun command: `python governance/compat/run_adif_defect_resolver.py --task-class architecture-contract --role dispatcher --lifecycle-phase pre-dispatch --surface-selector docs/reference --risk-ceiling HIGH --max-results 20 --json`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_workspace_design.py`; `governance/compat/check_agent_workspace_runtime_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch status; source verification; AHB block; workspace block; reviewer closure conversion; worker return shape |
| gateRunPurpose | confirmation and evidence after source-backed authoring; not first discovery |
| claimBoundary | packet compatibility only |

## Intake Role Routing Decision

Selected route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: `worker-no-commit split`

Intake summary: bounded documentation/schema source and overlap decision.

Scope classification: DOCS_SCHEMA_CONTRACT_ONLY.

Risk sensitivity: MEDIUM because a false ownership decision would create a
duplicate truth surface or misroute later implementation.

Escalation condition: source contradiction, full existing owner, forbidden
path, or unresolved canonical field authority.

## Agent Handoff Contract Control Block

Contract source: canonical contract, not archived handoff authority:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker-no-commit split |
| phase | EXECUTION |
| baseHeadFor(phase) | executionBaseHead captured by worker at start |
| changedSetScope(phase) | exactly four allowed deliverables |
| traceScope(phase, actor) | delegated worker trace covers only worker changed set |
| commitOwner(phase) | nobody during execution; independent reviewer at CLOSURE |
| crossBatchIsolation | one batch in a clean worktree; unrelated changes block execution |
| Before status evidence | clean worktree at committed dispatch HEAD |
| nextMoveSurfaces | worker must not edit; session-sync steward owns after reviewer decision |

## Agent Workspace Design Control Block

Contract sources: canonical contract, not archived handoff authority:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`;
`docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`;
and `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`.

| Field | Value |
|---|---|
| Workspace purpose | analyze existing read-model overlap only; no workspace build |
| Contract source | active AHB and workspace topology contracts |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | N/A with reason: no state or runtime storage created |
| Handoff fields | route, rolePattern, phase, base heads, changed set, trace, commit owner |
| State ownership | generated active session state remains canonical; workspace and ODVR remain read-only projections |
| Guard owner | existing workspace design and runtime-boundary guards |
| Build boundary | docs/schema only; no runtime source, UI, runtime queue, generated state, provider proof, public-sync, or registry edits |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_ODVR_T0_SOURCE_OVERLAP_AND_READOUT_CONTRACT_COMPLETION_2026-07-12.md`

reviewerOwnedClosurePaths: completion review, allowed repairs to worker outputs,
baseline/work-order closure conversion, roadmap T0 disposition if supported,
material commit, and separate session-sync paths after material closure.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap T0 requirement | Work-order instruction | Evidence output |
|---|---|---|
| source and overlap inventory | inspect all four owner families and semantic collisions | T0 contract owner/overlap tables |
| field-level authority map | classify every proposed result field | T0 contract field map |
| freshness rules | define source and aggregate freshness deterministically | contract plus JSON Schema fixtures |
| contradiction rules | fail closed and retain both source anchors | contract plus contradiction fixtures |
| JSON contract | define doc-only proposed shape without implementation claim | JSON Schema |
| representative fixtures | include current, stale, missing-source, and contradicted examples as schema examples | contract/schema examples |
| duplicate-owner stop rule | recommend stop if a full owner exists | worker return terminal recommendation |

## Work-Order Fulfillment Manifest

Exactly four worker-owned outputs: three material reference/schema artifacts and
one worker return. No optional files.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Worker return must state `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`,
executionBaseHead, exact changed paths, overlap verdict, source-verification
summary, commands/results, unresolved dissent, claim boundary, and explicit
`WORKER_MUST_NOT_COMMIT` confirmation.

## Execution Plan

1. Refresh current-source and semantic collision searches.
2. Inventory the active-session, MAO-T7, MLW-NRD1, and Web Workspace owners.
3. Classify each required ODVR result field and record reuse/compose/omit/block.
4. Define source anchor, freshness, missing-source, and contradiction semantics.
5. Write JSON Schema and representative current/stale/missing/contradicted examples.
6. Validate cross-document references and return the no-commit worker packet.

## Verification Commands

- JSON parse and Draft schema self-validation with available local tooling.
- repo-wide `rg` and `Test-Path` searches recorded in evidence.
- `python governance/compat/check_agent_workspace_runtime_boundary.py --enforce`
- `python governance/compat/check_governed_file_size.py --enforce`
- `git diff --check`
- `python governance/compat/run_worker_return_fast_gate.py`
- pre-implementation autorun gate on the real execution range.

## Acceptance Criteria

- Exactly three material outputs and one worker return exist, with no extra path.
- Every existing owner/symbol is independently source-verified.
- Every proposed field has one canonical source or a blocking disposition.
- The contract distinguishes implementation success from value proof.
- `CURRENT`, `STALE`, and `CONTRADICTED` are deterministic and testable.
- Contradictions preserve both source anchors and never choose silently.
- Missing mandatory sources fail closed.
- The JSON Schema validates all representative positive and negative examples.
- The output explicitly proves reuse/composition need or recommends stopping.
- No runtime/UI/provider/state/public/external-intake mutation or claim occurs.

## Evidence Requirements

Command-backed source searches, overlap matrix, schema validation, exact
changed-set proof, gate results, and explicit N/A with reason for non-applicable
proof.

## Negative And Fail-Condition Scan

Fail on duplicate truth ownership, UI or provider-local memory as authority,
silent source precedence, inferred free-prose verdict, mutable readout behavior,
guessed existing field, missing source anchor, implementation code, any changed
path outside the manifest, or a claim that T0 proves operator-friction value.

## Review Gate

The independent reviewer reruns source and collision searches, recomputes field
classifications, validates schema examples and negative cases, classifies any
dissent, repairs only allowed scope, and alone decides acceptance and commit.

## Closure Checklist

- [x] Exactly four worker outputs reviewed.
- [x] Every source fact and proposed field classified.
- [x] Schema and representative examples validated.
- [x] Duplicate-owner stop rule resolved.
- [x] No forbidden path or implementation claim present.
- [x] Worker return fast gate passes.
- [x] Reviewer authors completion review and owns material commit.

## Return-To-Orchestrator Conditions

Return only for source contradiction, an existing full canonical owner, missing
canonical authority, required forbidden path, or a field-semantics choice that
materially changes the roadmap beyond its authorized composition boundary.

## Operator Checkpoint

N/A with reason: operator explicitly authorized creation of this work order; no
runtime, public, or external-source checkpoint is crossed.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated worker |
| Provider or surface | local private provenance repository |
| Session or invocation | ODVR-T0 execution |
| Working directory | repository root |
| Command or tool surface | read/search/edit/local validation only |
| Target paths | four allowed deliverables |
| Allowed scope source | this work order and paired GC-018 |
| Before status evidence | clean worktree at executionBaseHead |
| After status evidence | uncommitted worker outputs plus return |
| Diff evidence | `git status --short` and `git diff --name-status` |
| Approval boundary | no commit; reviewer acceptance required |
| Claim boundary | T0 docs/schema overlap decision only |
| Agent type | worker |
| Invocation ID | odvr-t0-delegated-worker-2026-07-12 |
| Expected manifest | four allowed deliverables |
| Actual changed set | worker records at return |
| Manifest delta | worker records MATCH or BLOCKED |
| Deletion or rename disposition | N/A with reason: none authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance ODVR-T0 contract/schema work.

Next action: retain privately pending independent review.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation root | `docs/reference/operator_decision_value_readout/` |
| Stable front door | `docs/reference/operator_decision_value_readout/README.md` |
| Durable source files | overlap/contract Markdown and JSON Schema |
| Generated aggregate | N/A with reason: T0 creates no generated aggregate |
| Generator/checker | N/A with reason: no generator or checker authorized |
| Index update | README indexes the two sibling T0 artifacts |
| Public boundary | provenance only; no public-sync |

## Claim Boundary

This work order authorizes a delegated worker to produce ODVR-T0 documentation,
JSON Schema, representative doc examples, and a worker return without committing.
It does not authorize implementation, composer, CLI, UI, provider/live proof,
state mutation, automatic decision, public-sync, outside-source absorption,
ODVR-T1/T2, or production readiness.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: this tranche compares internal CVF owner surfaces;
it does not ingest, enumerate, map, or absorb an outside corpus.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no source corpus, mirror
  manifest, processing ledger, or completeness claim is part of the
  fulfillment manifest.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION

No outside source target is selected or consumed. Any later source-mirror lane
requires a separate operator-selected packet.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this artifact | `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | ODVR-T0 completion review | `REVIEWER_ACCEPTED_AFTER_REPAIR` | PASS |
| Roadmap state | ODVR roadmap | `PROPOSED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated aggregate check PASS; no ODVR entry required | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | current companion retained | PASS |
| External evidence digest | N/A with reason: internal CVF sources only | no external digest | N/A with reason |
| System loop interlock | current R91/ASC evidence | CURRENT | PASS |
| Session continuity | separate session-sync after material commit | pending separate batch | N/A with reason |

# CVF Agent Work Order - LSC-T1 Signal Ledger Source Layout And De-Dup Contract

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-20

docType: work_order

dispatchBaseHead: 90b06fa0

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_FOR_WORKER_2026-06-20.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: confirm with `git rev-parse --short HEAD` at worker start.

Current-time notes: LSC-T1 is a documentation/reference and JSON-template
contract tranche only. It follows LSC-T0 roadmap approval and second-round
advisory review with no blocking findings. N4 and N5 from round 2 are in scope:
exact AAF-to-intake severity mapping and `disposition`/`captureState`
source-of-truth handling.

Do-not-misread notes: do not build a ledger store, generator, drift checker,
helper readout, CLI/MCP adapter, runtime bridge, provider route, public-sync
artifact, or source implementation. Do not edit `EXTENSIONS/**`; cite it as
source only. Do not reopen AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7, or MLW8.

Required first actions: read this work order, read the LSC-T1 GC-018 baseline,
read the LSC-T0 roadmap, read the Codex classification, read both advisory
rebuttals, read the source files named in the Source Verification Block, confirm
actual `executionBaseHead`, and inspect current `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with only the required
uncommitted artifacts, actual `executionBaseHead`, actual `git status --short`,
source inventory, scan-depth ledger, focused gate evidence, and no commit. If
blocked, return `BLOCKED_WITH_REASON` and name the exact source or gate.

The worker-return artifact must include either the structured
`WORKER_EXPERIENCE_RETRO` block or the exact asserting
`WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` line.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two roles across phases: dispatcher creates packet; worker authors reference/template/return artifacts; reviewer/closer reviews and commits if accepted |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=90b06fa0`; `executionBaseHead` confirmed by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending LSC-T1 artifacts; one reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix LSC-T1 with AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7/8, runtime/provider/live, MCP, public-sync, queue/daemon, or direct-interception work |
| Before status evidence | dispatch base `90b06fa0`; current dispatch changed set intentionally includes LSC-T0 advisory/classification/roadmap artifacts plus this LSC-T1 packet |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_COMPLETION_2026-06-20.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; accepted reference front door; accepted contract; accepted JSON template; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer role |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | LSC-T0 roadmap plus classified round-1 and round-2 advisory rebuttals |
| Intake role | worker authors bounded reference/template/return artifacts |
| Reviewer role | reviewer/closer validates source fidelity, gate results, claim boundary, and commit eligibility |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; no runtime/source implementation |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if runtime/source/test/MCP/provider/live/public-sync/session-sync/parked-lane expansion is required |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index requirement | NOT_APPLICABLE_WITH_REASON |
| Reason | LSC-T1 is derived from current LSC roadmap/rebuttal artifacts and current Learning Plane/AAF source files, not a raw `.private_reference/legacy` corpus scan or LHW wave. |
| Coverage evidence used instead | LSC-T0 roadmap, Codex classification, round-1 and round-2 advisory rebuttals, Learning Signal Intake Bridge, AAF-T5 checker, worker-experience standard, and JSON generated aggregate discipline. |

## Purpose

Create the LSC-T1 source-layout and de-dup contract so CVF can capture learning
signals from worker friction, finding disposition, and future Learning Plane
projections without creating a second learning-signal core.

Success means future workers can read one contract and know:

- which fields are owned by `LearningSignalIntakeRecord`;
- which LSC extension fields are allowed;
- how `WORKER_EXPERIENCE_RETRO` maps to a signal or no-entry;
- how `rootCauseGroupId` is deterministically derived;
- how projections avoid double-counting the same root cause;
- how JSON source files and a generated Markdown index should be laid out in a
  future implementation tranche.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Dispatcher | dispatch author role |
| Worker | documentation/reference author role |
| Reviewer | review role after worker return |
| Closer | closer role after acceptance |
| Session-sync steward | session-sync steward role if session-sync is required |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-20 approval to continue into LSC-T1 after round-2 approve | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| LSC-T1 GC-018 | `docs/baselines/CVF_GC018_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_2026-06-20.md` | ACCEPT |
| LSC-T0 roadmap | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | ACCEPT |
| Codex classification | `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CODEX_CLASSIFICATION_2026-06-20.md` | ACCEPT |
| Round-1 advisory rebuttal | `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_2026-06-20.md` | ADVISORY_INPUT_CLASSIFIED |
| Round-2 advisory rebuttal | `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_ROUND2_2026-06-20.md` | ADVISORY_INPUT_ACCEPTED |
| Learning Signal Intake Bridge | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | SOURCE_AUTHORITY |
| Worker-experience checker | `governance/compat/check_worker_experience_retrospective.py` | SOURCE_AUTHORITY_FOR_AAF_TOKEN_ENUMS |
| Worker-experience standard | `docs/reference/worker_experience_retrospective/README.md` | SOURCE_AUTHORITY_FOR_AAF_TOKEN_SHAPE |
| JSON generated aggregate discipline | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | ACCEPT |
| External knowledge absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/learning_signal_chain/README.md`;
- create `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_2026-06-20.md`;
- create `docs/reference/learning_signal_chain/CVF_LEARNING_SIGNAL_LEDGER_ENTRY_TEMPLATE.json`;
- create `docs/reviews/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_WORKER_RETURN_2026-06-20.md`;
- define documentation-only field mappings from LSC event/template fields to
  `LearningSignalIntakeInput` and `LearningSignalIntakeRecord`;
- define deterministic `rootCauseGroupId` derivation rules;
- define projection de-dup between AAF-T5 token, Finding-To-Governance row, MLW3
  candidate, and future CLI/MCP event projection;
- define exact AAF-T5 `frictionLevel` to intake `severity` or no-entry mapping;
- define `disposition` as governed source of truth and `captureState` as
  derived/advisory, or define a strict allowed-pairs table and conflict rule;
- define JSON source plus generated Markdown index discipline for a future
  implementation tranche.

Forbidden scope:

- no edits to `EXTENSIONS/**`, `governance/compat/**`, tests, scripts, MCP,
  web UI, session state, active handoff, root startup routers, `.github/**`,
  dependency manifests, public-sync, or closed predecessor artifacts;
- no actual ledger source directory, generated aggregate, generator, checker,
  helper readout, runtime bridge, CLI/MCP adapter, provider/live proof,
  dependency install, queue/daemon, watcher, wrapper/proxy enforcement, direct
  IDE/shell/git/filesystem interception, arbitrary command execution, or
  EDIT/COMMIT execution;
- no public catalog update, public/production/release readiness, full-hook
  equivalence, cost optimization, speed claim, or universal
  governed-coding-control claim;
- no reopening of AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7, or MLW8.

Risk ceiling: R1 documentation/reference and JSON-template contract.

## Execution Plan

1. Confirm `executionBaseHead` and current `git status --short`.
2. Read all Required First Reads and record a source inventory in the worker
   return.
3. Create the Learning Signal Chain reference front door.
4. Create the LSC-T1 contract with all required content sections.
5. Create the JSON entry template and validate it as valid JSON.
6. Create the worker-return artifact with the required packet shape and
   worker-experience token.
7. Run required helper/gate commands and record results.

## Evidence Requirements

The worker-return artifact must record:

- actual `executionBaseHead`;
- actual `git status --short`;
- source inventory and scan-depth ledger;
- changed-path list;
- JSON validation command and result;
- required gate commands and results;
- explicit statement that no source/runtime/test/session/public-sync paths were
  edited;
- exact claim boundary and public export disposition.

## Acceptance Criteria

The worker return is acceptable only if:

- all Required Deliverables exist and no unauthorized paths are changed;
- the contract binds to `LearningSignalIntakeInput` /
  `LearningSignalIntakeRecord` instead of creating a parallel core;
- the AAF-T5 mapping table includes exact no-entry handling for the NA token and
  `frictionLevel=NONE`;
- `disposition` is the governed source of truth or an allowed-pairs table gives
  a deterministic conflict rule;
- `rootCauseGroupId` is deterministic and ledger-owned;
- JSON source plus generated Markdown index discipline is clearly stated;
- parked lanes remain parked;
- required gates pass or any failure is classified as `BLOCKED_WITH_REASON`.

## Review Gate

The reviewer/closer must run reviewer-fast or a stricter applicable gate before
accepting the worker return. Acceptance requires checking source fidelity,
changed-set scope, JSON validity, public/provenance boundary, external-intake
routing, finding-to-governance disposition, Delta boundary N/A, and the worker
return packet shape.

## Closure Checklist

- [ ] Required deliverables exist.
- [ ] No forbidden paths changed.
- [ ] JSON template validates.
- [ ] Source Verification claims remain current.
- [ ] N4 severity/no-entry mapping is present.
- [ ] N5 disposition/captureState authority rule is present.
- [ ] Worker-return packet includes required sections and token.
- [ ] Reviewer-fast or stricter gate passes.
- [ ] Commit ownership remains reviewer/closer only.
- [ ] Session-sync is performed only if mode or next-move surfaces change.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all Required Deliverables are created
and required gate evidence is recorded. Return `BLOCKED_WITH_REASON` if the task
requires forbidden paths, runtime/source/test implementation, provider/live
proof, public-sync, session-sync during worker execution, dependency install,
destructive actions, or parked-lane reopening.

## Operator Checkpoint

Allowed-scope corrections are handled under the Worker Autonomy rule above.
Fresh operator authorization is required before any runtime/source/test
implementation, generator or drift-checker build, CLI/MCP adapter,
provider/live proof, public-sync, session-sync during worker execution, or
reopening of AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7, or MLW8.

## Required First Reads

The worker must read these before editing:

- `docs/baselines/CVF_GC018_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_2026-06-20.md`
- `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`
- `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CODEX_CLASSIFICATION_2026-06-20.md`
- `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_2026-06-20.md`
- `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_ROUND2_2026-06-20.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts`
- `governance/compat/check_worker_experience_retrospective.py`
- `docs/reference/worker_experience_retrospective/README.md`
- `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`
- `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`

## Pre-Flight Checks

Before implementation, the worker must run or record:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 90b06fa0 --head HEAD
```

If the worktree contains unrelated dirty paths, the worker must preserve them
and avoid editing outside Required Deliverables.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/reference/learning_signal_chain/README.md` | worker | create |
| `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_2026-06-20.md` | worker | create |
| `docs/reference/learning_signal_chain/CVF_LEARNING_SIGNAL_LEDGER_ENTRY_TEMPLATE.json` | worker | create as template only |
| `docs/reviews/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_WORKER_RETURN_2026-06-20.md` | worker | create |
| Any other path | Not worker-owned | forbidden unless a revised work order authorizes it |

## Worker Autonomy / No-Question Rule

The worker must repair and rerun machine-check or packet-shape failures inside
Allowed scope. The worker must stop and return `BLOCKED_WITH_REASON` only if a
needed action would exceed Allowed scope, alter the claim boundary, require
runtime/source/test edits, provider/live proof, public-sync, secrets/quota,
dependency install, destructive actions, AAF-T6/T7/CGE-T3/ACE-R1/MLW7/MLW8
scope, or any forbidden path.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | stable reference front door plus dated contract and JSON template under `docs/reference/learning_signal_chain/` |
| Storage decision | create a folder-scoped reference surface so future LSC tranches can add generated source layout/generator/checker without crowding root reference files |
| Existing aggregate impact | none in LSC-T1 |
| Generated state impact | none in LSC-T1; future generated Markdown index and drift checker require a separate tranche |
| Durable governance boundary | LSC-T1 defines layout and template only; it does not create an active ledger store |
| Index/readout boundary | Markdown index is future generated readout only and not a source of truth |

## Required Deliverables

The worker must leave exactly these uncommitted artifact changes:

- `docs/reference/learning_signal_chain/README.md`
- `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_2026-06-20.md`
- `docs/reference/learning_signal_chain/CVF_LEARNING_SIGNAL_LEDGER_ENTRY_TEMPLATE.json`
- `docs/reviews/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_WORKER_RETURN_2026-06-20.md`

## Contract Content Requirements

The LSC-T1 contract must include these sections:

- Purpose
- Source Authority
- Non-Authority Inputs
- Existing Intake Field Ownership
- LSC Extension Field Ownership
- AAF-T5 Token To Intake Mapping
- Severity Mapping Table
- Disposition And Capture-State Authority Rule
- Root-Cause Group ID Derivation
- Projection De-Dup Rule
- JSON Source Layout
- Generated Markdown Index Rule
- CLI/MCP Minimal Payload Boundary
- Parking Ledger For AAF-T6/T7, CGE-T3, ACE-R1, MLW7/8
- Public Export Disposition
- Delta Execution Claim Boundary Control Block
- Claim Boundary

## Required AAF-T5 Mapping Rule

The contract must define this exact baseline mapping unless source verification
finds a stronger current CVF owner rule and records it:

| AAF-T5 `frictionLevel` | Intake result |
|---|---|
| `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` exact no-friction assertion | no signal entry |
| `NONE` | no signal entry |
| `LOW` | `severity=low` |
| `MEDIUM` | `severity=medium` |
| `HIGH` | `severity=high` |
| `BLOCKING` | `severity=critical` |

The contract must state that no-friction returns do not produce ledger entries,
because counting them would pollute de-dup metrics.

## Required Disposition/Capture-State Rule

The contract must make `disposition` the governed source of truth. `captureState`
must be derived/advisory unless the contract defines an allowed-pairs table and
explicit conflict rule. If an entry has conflicting values, the conflict must be
classified as invalid or recomputed from `disposition`; it must not silently
prefer `captureState` over `disposition`.

## Required Root-Cause And Projection Rules

The contract must define `rootCauseGroupId` as ledger-owned and deterministically
derivable from stable fields, not hand-assigned by each projection.

Minimum required projection rule:

| Projection | Rule |
|---|---|
| AAF-T5 token | capture source for worker friction |
| Finding-To-Governance row | disposition view of the same root cause |
| MLW3 candidate | proposal/evidence view of the same root cause |
| CLI/MCP event | external-agent capture view of the same root cause |

When projections refer to the same root cause, they must share one
`rootCauseGroupId` and not create separate counts.

## Required JSON Template Rule

The JSON template must:

- separate existing intake-owned fields from LSC extension fields;
- keep `autonomousMutationAuthorized` false;
- include placeholders only where the work order clearly marks them doc-only;
- include `sourceProjection`, `rootCauseGroupId`, `captureState`, and
  `repeatRisk` as LSC extension fields;
- include a comment-free valid JSON shape or record explanatory metadata in
  JSON fields, not comments;
- not claim to be an active runtime schema or generated aggregate.

## Generated Aggregate Discipline

The contract must decide:

- JSON source files are the future source of truth for ledger entries;
- a Markdown-readable index is generated/readout only and must not be edited by
  hand once a generator exists;
- generator and drift checker implementation are future LSC work, not LSC-T1
  worker scope.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order requirement |
|---|---|
| LSC-T1 binds to `LearningSignalIntakeRecord` | Source Verification Block and contract content requirements |
| LSC-T1 defines de-dup/root-cause grouping | Required Root-Cause And Projection Rules |
| N4 exact AAF-to-intake severity mapping | Required AAF-T5 Mapping Rule |
| N5 disposition/captureState authority | Required Disposition/Capture-State Rule |
| JSON source plus generated Markdown index | Generated Aggregate Discipline |
| Keep parked lanes parked | Forbidden scope and parking ledger requirement |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| LSC-T0 defines LSC-T1 as signal-ledger source layout and de-dup contract | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 252, 312-315 | `LSC-T1`; `rootCauseGroupId`; `LearningSignalIntakeRecord` | LSC-T0 roadmap | ACCEPT |
| LSC-T0 requires existing intake extension instead of a parallel record | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 148-165, 240 | `LearningSignalIntakeInput`; `LearningSignalIntakeRecord`; existing intake extension | LSC-T0 roadmap | ACCEPT |
| Round-2 review approves LSC-T1 dispatch with N4/N5 folded in | `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_ROUND2_2026-06-20.md` | lines 86, 199-204 | `APPROVE_NO_BLOCKING_FINDINGS`; N4; N5 | advisory rebuttal round 2 | ACCEPT |
| Round-2 review requires exact AAF-to-intake severity mapping | `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_ROUND2_2026-06-20.md` | lines 129-136 | `frictionLevel`; `severity`; no-entry | advisory rebuttal round 2 | ACCEPT |
| Round-2 review requires disposition/captureState authority rule | `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_ROUND2_2026-06-20.md` | lines 139-145 | `captureState`; `disposition` | advisory rebuttal round 2 | ACCEPT |
| Learning Signal Intake Bridge owns lane, defect class, severity, disposition, input, record, and mutation invariant | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | lines 11-68, 123-173 | `LearningSignalLane`; `LearningSignalDefectClass`; `LearningSignalSeverity`; `LearningSignalDisposition`; `LearningSignalIntakeInput`; `LearningSignalIntakeRecord`; `autonomousMutationAuthorized` | LPF intake bridge | ACCEPT |
| AAF-T5 checker owns worker retro token names and friction levels | `governance/compat/check_worker_experience_retrospective.py` | lines 34-56, 176-200, 273-275 | `WORKER_EXPERIENCE_RETRO`; `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON`; `FRICTION_LEVELS` | worker-experience checker | ACCEPT |
| Worker-experience standard owns token syntax and exact NA assertion | `docs/reference/worker_experience_retrospective/README.md` | lines 47-68 | `WORKER_EXPERIENCE_RETRO`; `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` | worker-experience standard | ACCEPT |
| Future ledger aggregate should use generated source layout and drift check | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | lines 24-29, 31-43, 71-82 | future ledger/manifest aggregate; generator; drift checker | JSON generated aggregate discipline | ACCEPT |
| External-agent returned outputs require classification before governed action | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | lines 35-42, 44-62, 70-78 | external-agent returned output route | external knowledge absorption chain map | ACCEPT |

## Work-Order Fulfillment Manifest

| Required artifact | Required content | Worker disposition |
|---|---|---|
| `docs/reference/learning_signal_chain/README.md` | stable front door pointing to LSC-T1 contract and future chain surfaces | create |
| `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_2026-06-20.md` | source layout, de-dup, mapping, generated-index, claim boundary | create |
| `docs/reference/learning_signal_chain/CVF_LEARNING_SIGNAL_LEDGER_ENTRY_TEMPLATE.json` | valid JSON template aligned to intake and LSC extension fields | create |
| `docs/reviews/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_WORKER_RETURN_2026-06-20.md` | worker return with evidence and token | create |

## Worker Return Packet Shape Contract

The worker-return artifact must include these sections or exact N/A-with-reason
dispositions where listed:

| Packet item | Worker-return disposition |
|---|---|
| Purpose section | MUST_INCLUDE |
| Scope / Methodology section | MUST_INCLUDE |
| Findings / Position section | MUST_INCLUDE |
| Risk / Corrective Action section | MUST_INCLUDE |
| Work-Order Fulfillment Manifest section | MUST_INCLUDE |
| Source Inventory or equivalent source ledger | MUST_INCLUDE |
| Agent Operation Trace Block section | MUST_INCLUDE |
| Delta Execution Claim Boundary Control Block section | MUST_INCLUDE |
| External Knowledge Intake Routing section | MUST_INCLUDE_OR_NA_WITH_REASON |
| Rescan Intelligence Hardening section | MUST_INCLUDE_OR_NA_WITH_REASON |
| Corpus Completeness And Report Integrity section | MUST_INCLUDE_OR_NA_WITH_REASON |
| Finding-To-Governance Learning Disposition section | MUST_INCLUDE |
| Epistemic Process Block section | MUST_INCLUDE_OR_EPISTEMIC_PROCESS_NA_WITH_REASON |
| Machine Closure Package section | MUST_INCLUDE_OR_NA_WITH_REASON; worker must not mark closure |
| Public Export Disposition section | MUST_INCLUDE |
| Claim Boundary section | MUST_INCLUDE |
| `executionBaseHead` | exact value from `git rev-parse --short HEAD` |
| `git status --short` | exact output after worker changes |
| Worker-experience token | structured `WORKER_EXPERIENCE_RETRO` or exact asserting `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` |

Conditional sections must not be omitted silently. If not applicable, the worker
must include the section with `N/A with reason` or
`NOT_APPLICABLE_WITH_REASON`, and state why it is not applicable to this
docs/template-only tranche.

## Test And Gate Requirements

The worker must run or record:

```powershell
python governance/compat/run_agent_automation_assist.py --base 90b06fa0 --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py
```

The worker should also validate the JSON template with a repo-local parser or
PowerShell/Node/Python JSON parse command and record the exact command.

## Rescan Intelligence Hardening

- Original source artifact: `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`.
- Predecessor intake artifact: `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_ROUND2_2026-06-20.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because round-2 N4/N5 were promoted from advisory findings into LSC-T1 dispatch requirements.
- Routing matrix status: `DO_NOW` for LSC-T1 source-layout/de-dup contract; `SEPARATE_RUNTIME_TRANCHE` for generator/checker/helper/CLI/MCP/runtime work; `STRATEGIC_OPERATOR_DECISION` for later lane ordering; `OUT_OF_SCOPE` for provider/live/public-sync/direct-interception/readiness claims; `RESOLVED_BY_DESIGN` for round-1 parallel-core risk folded into intake-bridge binding.
- Semantic sampling status: sampled N4, N5, and root-cause de-dup owner rule against current source verification.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | LSC remains capture-fast, promotion-slow, and proposal-only. |
| CHANGED_DISPOSITION | N4/N5 moved from advisory refinements into LSC-T1 work-order requirements. |
| NEW_FINDING | AAF `frictionLevel=NONE` and exact NA assertion must create no signal entry. |
| REMOVED_OR_REJECTED | Runtime/provider/live/public-sync/direct-interception scope remains rejected for LSC-T1. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | LSC-T1 documentation/reference and JSON-template contract. |
| SEPARATE_RUNTIME_TRANCHE | generator, drift checker, helper readout, CLI/MCP adapter, runtime bridge. |
| STRATEGIC_OPERATOR_DECISION | ordering of AAF-T6/T7, CGE-T3, ACE-R1, MLW7/8 after LSC-T1. |
| OUT_OF_SCOPE | provider/live, public-sync, direct interception, readiness, universal control. |
| RESOLVED_BY_DESIGN | no parallel learning-signal record; extend or map to existing intake bridge. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| LSC-T1-S1 | round-2 N4 | no-friction AAF returns should not create signal entries | mapped into required severity table | prevents empty no-friction returns from polluting de-dup counts | PASS |
| LSC-T1-S2 | round-2 N5 | `disposition` and `captureState` can conflict | mapped into source-of-truth rule | prevents derived state from overriding governed disposition | PASS |
| LSC-T1-S3 | LSC-T0 de-dup | projections must share one root cause | mapped into rootCauseGroupId requirement | prevents AAF/Finding/MLW projections from triple-counting | PASS |

## Corpus Completeness And Report Integrity

- Corpus task class: NOT_APPLICABLE_WITH_REASON - LSC-T1 is a bounded documentation/reference and JSON-template contract, not a corpus enumeration or legacy scan.
- Corpus root: NOT_APPLICABLE_WITH_REASON - no corpus root is assigned.
- Snapshot time: NOT_APPLICABLE_WITH_REASON - no corpus snapshot is taken.
- Enumeration command: filesystem-backed direct file reads listed in Source Verification Block and Required First Reads; no corpus enumeration command is authorized.
- Manifest artifact or inline manifest: inline Source Verification Block above.
- Manifest hash: NOT_APPLICABLE_WITH_REASON - no corpus manifest hash is created.
- Processing ledger artifact or inline ledger: inline Source Verification Block and Work-Order Fulfillment Manifest above.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline Source Verification Block; ledger_terminal=READ for named source rows; exclusions=corpus enumeration and legacy scan surfaces are out of scope; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: corpus scan, legacy source-family enumeration, public-sync copy, runtime/provider/live proof, and parked lanes.
- Unreadable or unsupported files: 0.
- Aggregation check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate is created.
- Drift check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate or generated corpus registry is changed.
- Output traceability: Required Deliverables and Source Verification Block define all worker output traceability.
- Adversarial verification: reviewer/closer must run reviewer-fast or stricter applicable gate before acceptance.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output to finding classification to governed work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | LSC-T1 signal-ledger source-layout and de-dup contract |
| Disposition | ADAPT as CVF-owned Learning Signal Chain contract |
| Claim boundary | advisory inputs become authority only through Codex classification, GC-018, and this work order |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LSC-T1 signal-ledger contract work order only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | documentation/reference and JSON-template authoring only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | source-layout contract, de-dup rule, schema template, and generated-index decision only |
| forbiddenExpansion | wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| LSC must not create a parallel record beside `LearningSignalIntakeRecord` | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | worker contract must bind to existing intake bridge | handled by this work order |
| AAF-to-intake severity mapping needs exact no-entry and blocking rules | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | worker contract must define mapping table | handled by this work order |
| `captureState` can drift from governed `disposition` | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | worker contract must define source-of-truth rule | handled by this work order |
| Runtime/provider/cost applicability for this work order | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed by this work order | handled |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order for Learning Signal Chain contract work.
No public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Commit Prompt Readiness

| Field | Disposition |
|---|---|
| Worker commit mode | `WORKER_MUST_NOT_COMMIT` |
| Worker return token | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| Reviewer commit owner | reviewer/closer role after accepted worker return |
| Material commit scope | LSC-T1 required deliverables only |
| Session-sync | reviewer/closer only if mode or next-move surfaces change |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author role |
| Provider or surface | local workspace |
| Session or invocation | LSC-T1 dispatch authoring, 2026-06-20 |
| Working directory | repository root |
| Command or tool surface | `apply_patch` file edits plus governance checks |
| Target paths | `docs/baselines/CVF_GC018_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_FOR_WORKER_2026-06-20.md`; LSC-T0 roadmap/review/classification artifacts |
| Allowed scope source | operator instruction for LSC-T1 after round-2 rebuttal; LSC-T0 roadmap; Codex classification |
| Before status evidence | clean worktree at committed base `90b06fa0`; current uncommitted dispatch batch records all changed paths explicitly |
| After status evidence | LSC-T1 GC-018 and work order created; LSC-T0 roadmap/classification/rebuttal artifacts updated for dispatch incorporation |
| Diff evidence | `git status --short` and dispatch gates on range `90b06fa0..HEAD` |
| Approval boundary | operator authorized LSC-T1 dispatch; no worker implementation or commit by worker |
| Claim boundary | dispatch authoring only; no runtime/source/test/session/public-sync implementation |
| Agent type | dispatcher role |
| Invocation ID | `lsc-t1-dispatch-authoring-2026-06-20` |
| Expected manifest | LSC-T0 roadmap, round-1 rebuttal, round-2 rebuttal, Codex classification, LSC-T1 GC-018, LSC-T1 work order |
| Actual changed set | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`; `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_2026-06-20.md`; `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_ROUND2_2026-06-20.md`; `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CODEX_CLASSIFICATION_2026-06-20.md`; `docs/baselines/CVF_GC018_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_FOR_WORKER_2026-06-20.md` |
| Manifest delta | MATCH |

## Claim Boundary

This work order authorizes only LSC-T1 documentation/reference and JSON-template
contract artifacts. It does not implement a ledger store, generator, drift
checker, helper readout, runtime Learning Plane mutation, provider/live proof,
CLI/MCP adapter behavior, public-sync, direct IDE/shell/git/filesystem
interception, wrapper/proxy enforcement, queue/daemon, watcher, readiness, cost
optimization, full-hook equivalence, or universal governed-coding control.

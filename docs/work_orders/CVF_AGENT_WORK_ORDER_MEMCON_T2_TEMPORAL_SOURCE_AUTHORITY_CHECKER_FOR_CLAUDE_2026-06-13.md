# CVF Agent Work Order - MEMCON-T2 Temporal Ambiguity And Source-Authority Checker

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-13

Owner: Codex

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `3f4ddda6`

executionBaseHead: `3f4ddda6`

closureBaseHead: `f3da4134`

sourceAuthority:
`docs/reviews/CVF_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_COMPLETION_2026-06-13.md`

rawMemoryReleased=false

completionReviewPath:
`docs/reviews/CVF_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_COMPLETION_2026-06-13.md`

GC-018:
`docs/baselines/CVF_GC018_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_2026-06-13.md`

Parent roadmap:
`docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`

## Purpose

Implement the first MEMCON machine checker so future memory-consolidation
artifacts fail early when they contain unresolved temporal ambiguity, missing
source authority, missing conflict/staleness fields, missing retrieval boundary,
raw-memory release claims, or missing operator-visible review sections.

## Authority Chain

| Authority | Path / evidence | Disposition |
| --- | --- | --- |
| Operator request | operator asked Codex to create a Claude work order | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V18_2026-06-12.md` | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | ACCEPT |
| T1b schema appendix | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_2026-06-13.md` | ACCEPT |

## Agent Roles

| Role | Agent | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | dispatches only |
| Worker | Claude | implements allowed-scope artifacts and returns uncommitted |
| Reviewer / closer | Codex | reviews, fixes if in reviewer scope, commits only after gates |

## Intake Role Routing Decision

Intake summary: operator asked Codex to create a Claude work order for
MEMCON-T2 after MEMCON-T1b closed.

Scope classification: bounded governance checker implementation.

Risk sensitivity: medium control-plane risk because the tranche changes local
hook behavior, but no runtime memory, provider/API, public-sync, or external
workspace mutation is authorized.

Selected route mode: MULTI_AGENT_MULTI_ROLE.

Role separation basis: Claude implements allowed-scope checker artifacts under
`WORKER_MUST_NOT_COMMIT`; Codex reviews, converts closure artifacts, updates
session continuity, and commits.

Escalation condition: return to Codex if implementation requires forbidden
paths, runtime memory behavior, Policy_Local mutation, provider/API proof,
public-sync, external workspace access, or operator evidence.

Reason: T2 changes governance checker behavior and hook placement. Claude is
assigned as worker under `WORKER_MUST_NOT_COMMIT`; Codex keeps reviewer and
committer authority so implementation, review, and closure evidence are
separated.

## Required First Reads

Claude must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V18_2026-06-12.md`
4. `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`
5. `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md`
6. `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md`
7. `governance/compat/run_local_governance_hook_chain.py`

## Startup Acknowledgment Required

Claude must begin with:

`Startup acknowledged: current mode=memcon_t2_temporal_source_authority_checker_dispatched; active handoff=AGENT_HANDOFF_V18_2026-06-12.md; work order=MEMCON-T2; next allowed move=Claude executes WORKER_MUST_NOT_COMMIT and returns uncommitted artifacts; parked checkpoint=Policy_Local PL-S1, EC/T12, DEP2/Redis/receipt-anchor remain parked.`

## Dependency Release Evidence

| Dependency | Required evidence | Disposition |
| --- | --- | --- |
| MEMCON-T1a closure | material commit `84a46b62` | SATISFIED |
| MEMCON-T1b schema closure | material commit `f94d2fbd`; session sync `3f4ddda6` | SATISFIED |
| Fresh T2 authority | GC-018 and this work order | SATISFIED |

## Current Runtime Freshness Verification

This tranche is a governance checker implementation. It must not infer runtime
memory behavior from docs. Before editing, Claude must run or re-run these
source checks:

```powershell
rg -n "MEMCON-T2|Temporal ambiguity|source-authority|raw transcript release" docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md
rg -n "Machine-Check Handoff Notes For MEMCON-T2|source-authority|TIME_AMBIGUOUS_BLOCKED|rawMemoryReleased" docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md
rg -n "REVIEWER_FAST_CHECKS|pre-commit|check_memory_governance_compat" governance/compat/run_local_governance_hook_chain.py
```

## Pre-Flight Checks

Claude must run these before editing:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 3f4ddda6 --head HEAD
```

If the pre-implementation gate fails only on allowed-scope artifacts, Claude
must fix and rerun under the Worker Autonomy rule. If it fails outside allowed
scope, return to Codex.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| T2 checker scope exists in roadmap | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | `MEMCON-T2 Detail` | `MEMCON-T2` | MEMCON roadmap | ACCEPT |
| T2 must check source authority | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | `Machine-Check Handoff Notes For MEMCON-T2` | `sourceAuthority` | MEMCON schema appendix | ACCEPT |
| T2 must check temporal ambiguity | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | `Machine-Check Handoff Notes For MEMCON-T2` | `TIME_AMBIGUOUS_BLOCKED` | MEMCON schema appendix | ACCEPT |
| T2 must check raw release invariant | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | `Machine-Check Handoff Notes For MEMCON-T2` | `rawMemoryReleased` | MEMCON schema appendix | ACCEPT |
| T2 must respect T1a temporal normalization rule | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | `Temporal Normalization Rule` | `temporalNormalizationStatus` | MEMCON T1a standard | ACCEPT |
| T2 must respect T1a retrieval boundary | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | `Retrieval Eligibility Rule` | `rawMemoryReleased` | MEMCON T1a standard | ACCEPT |
| Reviewer-fast hook list exists | `governance/compat/run_local_governance_hook_chain.py` | lines 24-71 | `REVIEWER_FAST_CHECKS` | local hook runner | ACCEPT |
| Pre-commit hook list exists | `governance/compat/run_local_governance_hook_chain.py` | lines 79-181 | `pre-commit` | local hook runner | ACCEPT |
| Existing checker pattern exists | `governance/compat/check_rescan_intelligence_hardening.py` | constants, CLI, validator pattern | `REPO_ROOT` | rescan intelligence checker | ACCEPT |

## New Files To Create

| Path | Required content |
| --- | --- |
| `governance/compat/check_memory_consolidation_artifact_quality.py` | deterministic checker with CLI `--base`, `--head`, and `--enforce` support |
| `governance/compat/test_check_memory_consolidation_artifact_quality.py` | focused positive and negative tests |
| `docs/reviews/CVF_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_WORKER_RETURN_2026-06-13.md` | worker return packet |

## Allowed Implementation Scope

Claude may modify:

- `governance/compat/check_memory_consolidation_artifact_quality.py`
- `governance/compat/test_check_memory_consolidation_artifact_quality.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `docs/reviews/CVF_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_WORKER_RETURN_2026-06-13.md`
- this work order only for worker return/status evidence if needed
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

## Allowed / Forbidden Scope

Allowed scope is exactly the paths listed in `Allowed Implementation Scope`.
Forbidden scope is exactly the paths and behaviors listed under `Claude must
not modify` plus the non-goals in the claim boundary.

## Write Ownership

Claude owns worker implementation changes only until return:

- new checker;
- focused checker tests;
- hook-list placement in `run_local_governance_hook_chain.py`;
- worker-return packet;
- optional status evidence inside this work order or parent roadmap row.

Codex owns closure conversion:

- completion review path;
- session state, handoff, and front-door sync;
- final roadmap closure status;
- commits.

## Worker Autonomy / No-Question Rule

Worker-Autonomy / No-Question Rule: any governance gate failure within allowed
scope must be repaired and rerun by Claude without asking the operator. Claude
must return to Codex only when repair would exceed allowed scope, touch
forbidden paths, alter claim boundary, consume provider/API quota, mutate
external workspaces, or require operator evidence.

## Checker Requirements

The checker must inspect changed active MEMCON memory-consolidation artifacts,
not every historical document. Applicable files are active governed Markdown
under `docs/reference/`, `docs/reviews/`, `docs/roadmaps/`, `docs/baselines/`,
and `docs/work_orders/` that include one or more MEMCON markers:

- `MemorySignal`
- `MemoryCandidate`
- `ConsolidatedMemoryRecord`
- `OperatorMemoryReviewPacket`
- `MemoryRetrievalPackInput`
- `MEMCON`
- `memory consolidation`

The checker must fail applicable artifacts when:

- source-authority field or section is missing;
- durable/retrieval-facing memory text contains unresolved relative-date
  phrases without explicit quote handling;
- `TIME_AMBIGUOUS_BLOCKED` is promoted as retrieval-eligible or consolidated;
- `rawMemoryReleased=true` appears;
- retrieval-facing sections omit `rawMemoryReleased=false`;
- operator-visible packet sections omit conflict, stale/outdated, temporal
  ambiguity, pruning/rejection, or operator action visibility when the artifact
  is a review packet;
- public export disposition is missing from changed MEMCON review packets.

Relative-date examples must include:

- `today`
- `yesterday`
- `tomorrow`
- `last week`
- `recently`
- `earlier`
- `this month`
- `three months ago`
- Vietnamese-facing equivalents when the artifact declares Vietnamese-facing
  text, such as `hom nay`, `hom qua`, `tuan truoc`, `gan day`, and `thang nay`
  in ASCII transliteration.

Allowed quote handling:

- quoted source evidence may retain relative phrases only when the artifact
  explicitly marks the phrase as source quote/evidence and states it is not the
  durable normalized memory value.

## Hook Placement Requirements

Add the checker to:

- `reviewer-fast`;
- `pre-commit`.

Do not add it to unrelated public-sync or provider-specific paths.

## Execution Plan

1. Perform first reads and pre-flight checks.
2. Implement the checker with deterministic file selection and CLI support.
3. Add focused positive and negative tests.
4. Wire the checker into reviewer-fast and pre-commit hook lists.
5. Run focused tests, reviewer-fast, and pre-commit.
6. Produce the worker return packet and leave all artifacts uncommitted for
   Codex review.

## Evidence Requirements

Claude must provide command-backed evidence for:

- focused unittest result;
- reviewer-fast result;
- pre-commit result;
- changed files list;
- `WORKER_MUST_NOT_COMMIT observed`;
- any guard findings and whether each is a CVF foundation learning candidate.

## Acceptance Criteria

T2 worker return is acceptable only if:

- the checker exists at the authorized path;
- tests cover missing source authority, unresolved relative dates,
  `TIME_AMBIGUOUS_BLOCKED` promotion, raw-memory release, retrieval boundary,
  and operator-visible review packet gaps;
- reviewer-fast and pre-commit include the checker and pass;
- no forbidden path is modified;
- no runtime memory, provider/API, Policy_Local, public-sync, storage, OCR, or
  retrieval claim is made.

## Required Proof Manifest

| Proof item | Required command / evidence | Required literal |
| --- | --- | --- |
| Focused checker tests | `python -m unittest governance.compat.test_check_memory_consolidation_artifact_quality` | `OK` |
| Reviewer-fast | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | `All reviewer-fast governance checks passed` |
| Pre-commit | `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit` | `All pre-commit governance checks passed` |
| Worktree status | `git status --short` | worker artifacts staged or uncommitted; no commit |

## Required Artifact Manifest

| Artifact | Required status | Closure evidence |
| --- | --- | --- |
| `governance/compat/check_memory_consolidation_artifact_quality.py` | created | checker source present |
| `governance/compat/test_check_memory_consolidation_artifact_quality.py` | created | focused unittest file present |
| `governance/compat/run_local_governance_hook_chain.py` | updated | reviewer-fast and pre-commit hook entries present |
| `docs/reviews/CVF_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_WORKER_RETURN_2026-06-13.md` | created | `WORKER_MUST_NOT_COMMIT observed` |
| `docs/reviews/CVF_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_COMPLETION_2026-06-13.md` | created by Codex | `Status: CLOSED_PASS_BOUNDED` |

## Work-Order Fulfillment Manifest

| Fulfillment item | Worker evidence required | Reviewer disposition owner |
| --- | --- | --- |
| Checker created | changed file list includes `governance/compat/check_memory_consolidation_artifact_quality.py` | Codex |
| Focused tests created | changed file list includes `governance/compat/test_check_memory_consolidation_artifact_quality.py` | Codex |
| Hook placement complete | diff shows checker in reviewer-fast and pre-commit | Codex |
| Focused tests pass | command output contains `OK` | Codex |
| Reviewer-fast passes | command output contains `All reviewer-fast governance checks passed` | Codex |
| Pre-commit passes | command output contains `All pre-commit governance checks passed` | Codex |
| No commit by worker | worker packet states `WORKER_MUST_NOT_COMMIT observed` and `git status --short` shows uncommitted/staged artifacts | Codex |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order requirement | Evidence expected from worker |
| --- | --- | --- |
| required source authority fields | checker failure when source authority is missing | focused negative test |
| forbidden durable relative-date phrases unless normalized | checker failure for unresolved relative-date phrases | focused negative test |
| missing conflict or staleness fields | checker failure for incomplete operator review packet | focused negative test |
| missing retrieval boundary | checker failure for missing retrieval boundary/raw release marker | focused negative test |
| raw transcript release marker | checker failure for `rawMemoryReleased=true` | focused negative test |
| missing operator-visible review section | checker failure for missing operator-visible sections | focused negative test |

## Worker Return Packet Requirements

Claude must return uncommitted artifacts and include:

- execution base head;
- changed files list;
- implementation summary;
- focused test result;
- reviewer-fast result;
- pre-commit result;
- any findings and whether they indicate CVF foundation learning;
- exact claim boundary;
- confirmation: `WORKER_MUST_NOT_COMMIT observed`.

## Review Gate

Codex must run reviewer-fast before accepting the packet, inspect the diff, fix
reviewer-owned closure-only artifacts if needed, then run pre-closure on the
committed closure range before marking T2 closed.

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_COMPLETION_2026-06-13.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/**`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

Reviewer closure conversion must not be performed by Claude.

## Closure Checklist

- [x] Claude worker return received with `WORKER_MUST_NOT_COMMIT observed`.
- [x] Codex reviewer-fast passes on returned artifacts.
- [x] Codex verifies changed files are inside allowed scope or reviewer-owned
      closure scope.
- [x] Completion review is created by Codex.
- [x] Pre-closure autorun passes on the committed closure range.
- [x] Session state, session memory, and active handoff are updated by Codex.
- [x] T2 is marked `CLOSED_PASS_BOUNDED` only after committed evidence exists.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 | `docs/baselines/CVF_GC018_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_COMPLETION_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_WORKER_RETURN_2026-06-13.md` | `WORKER_MUST_NOT_COMMIT observed` | PASS |
| Roadmap state | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | `Status: MEMCON_T2_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason | no GC-051 registry update authorized for MEMCON-T2 checker closure | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no GC-051 registry update authorized for MEMCON-T2 checker closure | BLOCKED with reason |
| Checker source | `governance/compat/check_memory_consolidation_artifact_quality.py` | file exists | PASS |
| Focused tests | `governance/compat/test_check_memory_consolidation_artifact_quality.py` | unittest PASS | PASS |
| Hook placement | `governance/compat/run_local_governance_hook_chain.py` | reviewer-fast and pre-commit entries exist | PASS |
| External evidence digest | N/A with reason | no external corpus/provider evidence used | N/A with reason |
| System loop interlock | N/A with reason | no runtime loop mutation authorized | N/A with reason |
| Session continuity | active state/front door/handoff | separate session-sync commit follows material closure when required | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
| --- | --- | --- | --- |
| Receipt generation | N/A with reason - deterministic checker closure only | no runtime receipt generated | PASS |
| Query execution | N/A with reason - no retrieval/query runtime authorized | no query route changed or executed | PASS |
| Provider/API proof | N/A with reason - provider/API proof forbidden | no provider/API call used | PASS |
| rawMemoryReleased | `false` | `rawMemoryReleased=false` in closure artifacts | PASS |

## Return-To-Orchestrator Conditions

Return without implementation if:

- a runtime memory implementation becomes necessary;
- source verification contradicts the schema appendix;
- hook placement requires broad refactor;
- tests require provider/API, Policy_Local, public-sync, storage, OCR, or
  external workspace access;
- any forbidden path must be touched.

## Operator Checkpoint

No operator checkpoint is needed during T2 unless scope expands. Codex will
review the uncommitted worker return and decide closure, fixes, or next
roadmap.

## Claim Boundary

This work order authorizes only a deterministic governance checker and focused
tests for MEMCON artifacts. It does not authorize runtime memory storage,
retrieval behavior, cross-agent memory consistency, operator UI, Policy_Local
mutation, EC activation, T12 unlock, provider/API proof, public-sync export,
production/public readiness, memory reinjection, high-risk promotion, or
autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Memory Plane checker dispatch; public-sync is not authorized.

# CVF Agent Work Order - Active Continuity Read Cost T3 Shift Operations Application

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED

Date: 2026-08-11

Batch ID: ACRC-T3

Core dispatch base head: `4c3d63d1563531f01c0b96cbb720abd2a1b20c5f`

Target repository: `shift-operations-workspace`

Target execution base head: `b62271d42150da68d4fb80983cd56260ee11cee1`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: implementation worker for ACRC-T3 in `shift-operations-workspace`.

Canonical packet: this Work Order plus
`docs/baselines/CVF_GC018_ACTIVE_CONTINUITY_READ_COST_T3_SHIFT_OPERATIONS_APPLICATION_2026-08-11.md`
from the private CVF provenance repository.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: exact target commit
`b62271d42150da68d4fb80983cd56260ee11cee1`.

Current-time notes: P4-A1 is accepted, stopped, and parked; T3 is the only
released downstream lane.

Do-not-misread notes: this is continuity-only work. It does not authorize
product/runtime work, the stale `.cvf/manifest.json` `cvfCoreCommit` repair,
provider/live proof, public sync, push, deployment, or any commit.

Required first actions: work from the target repository root; perform its
First-Request Protocol and declaration; read the baseline and this packet;
verify exact HEAD, clean status, and every pinned preimage; run the target
preimplementation checks before writing.

Return contract: create the target worker return, run all required gates, leave
changes unstaged and uncommitted, and return `COMPLETE_PENDING_INDEPENDENT_REVIEW`
or `BLOCKED_WITH_REASON`.

Worker: provider-neutral implementation worker.

Reviewer/closer: independent reviewer/closer.

Worker return path: target repository decision artifact named
`ACTIVE_CONTINUITY_READ_COST_T3_WORKER_RETURN_2026-08-11.md`.

## Purpose

Implement roadmap T3 by introducing progressive downstream continuity routing,
compacting current carriers, archiving displaced history byte-for-byte,
rotating to current accepted P4-A1 authority, and adding fail-closed local
checks without changing any product behavior.

## Authority Chain

1. Operator continuation and delegated orchestrator/reviewer authority.
2. Active-continuity roadmap T3.
3. Paired GC-018 baseline and its fresh protected-preimage release.
4. This exact Work Order.
5. Accepted downstream P4-A1 closure truth as read-only predecessor authority.

Provider-local memory, chat summaries, and `CLAUDE.md` are not CVF authority.

## Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| ORCHESTRATOR / WORK_ORDER_AUTHOR | dispatcher | authority, exact scope, hashes, dispatch |
| IMPLEMENTATION_WORKER | delegated worker | exact-14 downstream changes, tests, worker return, no commit |
| REVIEWER / CLOSER / COMMIT_STEWARD | independent reviewer | recompute, review, repair decision, target commit if accepted |
| SESSION_SYNC_STEWARD | session-sync steward after material acceptance | synchronize Core roadmap/session separately |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| Task class | downstream governance-continuity compaction |
| Risk ceiling | R2 |
| Route mode | `MULTI_AGENT_MULTI_ROLE` |
| Escalation condition | exact base/hash contradiction, archive mismatch, forbidden-scope need, external effect, or irreparable in-scope gate failure |

Intake summary: one R2 continuity-only migration from a stopped accepted P4-A1
state; exact base, paths, hashes, roles, evidence, and no-commit ownership are
fully bounded before BUILD.

## Required First Reads

| Source | Required action |
|---|---|
| target `AGENTS.md` | FULL_READ |
| target `.cvf/manifest.json` and `.cvf/policy.json` | FULL_READ |
| target canonical session-memory carrier | FULL_READ before compaction |
| target canonical active-session state | FULL_READ before compaction |
| target current P4-A1 closure handoff | FULL_READ |
| target implementation-status source | FULL_READ |
| target documentation index and business roadmap named by its manifest | FULL_READ |
| paired GC-018 baseline | FULL_READ |
| this Work Order | FULL_READ |
| target session-state checker and focused mirror-drift test | FULL_READ |

## Pre-Flight Checks

1. `git rev-parse HEAD` equals the exact target execution base.
2. `git status --short` is empty.
3. Recompute every existing-path SHA-256 from the paired baseline; all must
   match exactly.
4. Confirm both future archive paths, bootstrap path, successor handoff, and
   worker return path do not exist.
5. Run `python scripts/check_session_state.py`,
   `python scripts/check_project_knowledge.py`, and the focused mirror test.
6. Run the workspace doctor without live-readiness mode. Its bounded legacy
   catalog warning and stale core-pin note are accepted pre-existing notes;
   any new failure blocks.

## Dependency Release Evidence

| Dependency | Release evidence | Disposition |
|---|---|---|
| accepted predecessor | target closure commit `ffe1c5b500f2f27f4166ded97423c4fc76354c67` and independent review hash `d56b835d9c72ec706fc3b8d293aaf85a147ecd6f62c20cfa1afc29baed52ef22` | ACCEPT |
| T2B foundation | accepted material commit `575f8f991fa0446756aea53515ec128c252c5168` | ACCEPT |
| operator checkpoint | fresh selection on 2026-08-11 under delegated decision authority | ACCEPT |
| target base | clean `b62271d42150da68d4fb80983cd56260ee11cee1` observed before dispatch | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap T3 requirement | Work Order implementation | Acceptance |
|---|---|---|
| add downstream bootstrap read model | create canonical compact projection; route AGENTS to it | AC-03, AC-06 |
| compact session memory | archive preimage, replace active file with current pointers | AC-02, AC-04 |
| reduce 251-path list to at most 12 | edit canonical state and validate count/existence | AC-05 |
| move historical reads and blocked narrative | byte-exact state archive plus explicit history pointers | AC-02, AC-05 |
| rotate handoff | create successor bound to accepted P4-A1 closure | AC-07, AC-08 |
| update mirror and Project Knowledge pin atomically | mirror sync plus only implementation-status source-pin refresh | AC-07, AC-09 |
| governance continuity only | exact path firewall and zero product/external effects | AC-10, AC-11 |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T3 requires bootstrap model | VALUE_SET | `docs/roadmaps/CVF_ACTIVE_CONTINUITY_READ_COST_REDUCTION_ROADMAP_2026-08-10.md` | T3 section | `T3` | active-continuity roadmap | ACCEPT |
| T3 requires at most 12 current reads | LITERAL_INVARIANT | `docs/roadmaps/CVF_ACTIVE_CONTINUITY_READ_COST_REDUCTION_ROADMAP_2026-08-10.md` | T3 section | `required_reads` | active-continuity roadmap | ACCEPT |
| downstream canonical state path | VALUE_SET | canonical downstream manifest at exact target execution base | canonicalContinuityPaths | `activeState` | downstream manifest | ACCEPT |
| current state read-list field | EXISTS | canonical downstream state at exact target execution base | line 8 | `required_reads` | canonical session state | ACCEPT |
| current state active-handoff field | VALUE_SET | canonical downstream state at exact target execution base | lines 5-6 | `active_handoff` | canonical session state | ACCEPT |
| mirror checker mapping | RUNTIME_BEHAVIOR | canonical downstream checker source at exact target execution base | `_MIRROR_FIELD_MAP`; `verify_mirror_drift` | `verify_mirror_drift` | session-state checker | ACCEPT |
| Knowledge implementation-status pin | VALUE_SET | canonical downstream Knowledge manifest at exact target execution base | project-context sourcePins | `sourcePins` | Project Knowledge manifest | ACCEPT |
| P4-A1 accepted closure identity | VALUE_SET | canonical downstream active handoff at exact target execution base | Closure Identity and Exact Accepted Authority | `Closure HEAD` | downstream active handoff | ACCEPT |

## New Doc-Only Fields

| Field | Owner | Purpose |
|---|---|---|
| `history_index` | canonical downstream state | pointers to byte-exact pre-T3 archives |
| bootstrap `historyIndex` | compact projection | pointer-only archive discovery |

Bootstrap projection fields other than the two rows above mirror existing
canonical values and are not new product/runtime fields.

## Exact Worker Changed Set

The worker may change exactly these 14 target-relative paths and no others:

1. `AGENTS.md`
2. `.cvf/manifest.json`
3. `SESSION/SESSION_MEMORY.md`
4. `SESSION/archive/SESSION_MEMORY_PRE_T3_2026-08-11.md`
5. `SESSION/ACTIVE_SESSION_STATE.json`
6. `SESSION/archive/ACTIVE_SESSION_STATE_PRE_T3_2026-08-11.json`
7. `SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
8. `SESSION/handoffs/T3_ACTIVE_CONTINUITY_READ_COST_2026-08-11.md`
9. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
10. `IMPLEMENTATION_STATUS.json`
11. `knowledge/manifest.json`
12. `scripts/check_session_state.py`
13. `tests/cvf/test_session_state_mirror_drift.py`
14. `docs/decisions/ACTIVE_CONTINUITY_READ_COST_T3_WORKER_RETURN_2026-08-11.md`

## Fresh Preimage Authority

| Existing path | Required SHA-256 before first write |
|---|---|
| `AGENTS.md` | `a29efc0f7a79d659a8982ec5f391b0bbcd9d588891299658ce894e15d0b9e7a0` |
| `.cvf/manifest.json` | `617bb281aea622790c30b2e65204f7fa7b4d3a5923b8ca3a0995daa051fa1867` |
| `SESSION/SESSION_MEMORY.md` | `45b2adb1c45cbe57cb17724bcbbdcaf753835a21a608c76b5f585ffd3396363f` |
| `SESSION/ACTIVE_SESSION_STATE.json` | `cb93adf42361d6c71ece3b5e63a9c568d22b78a65ec668c0c1523f49c4f68b6d` |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `ee66ead77e5b86dbcca996325d330c25da3a2886bf79911051fc5da031ba4275` |
| `IMPLEMENTATION_STATUS.json` | `afab67dfd75b65e74c49d24e2de2721c0dcbd72d910fb52712375ca1b31b1ee1` |
| `knowledge/manifest.json` | `66c4ec986be52bf08ecdb273a4a4ed50ff0db9f75a2ef301de5ef104de65c9b3` |
| `scripts/check_session_state.py` | `cc7310ec63a398fb18a7749c81ef3eb985828d3047bca496ad913f9009bdc56d` |
| `tests/cvf/test_session_state_mirror_drift.py` | `eaa94510ab949a055eba31538c3b6698c23c95320f04bc99a021444c42f2285b` |
| current P4-A1 handoff, read-only | `e1be2f314959e0c05e4877e88c81361e3678e3d88df526654c6786cf25b4ae96` |

Any mismatch is `BLOCKED_ARCHIVE_OR_AUTHORITY_MISMATCH`; do not select newer
bytes or alter the packet locally.

## Write Ownership

Worker owns exact-14 unstaged material only. Reviewer owns review repairs,
completion decision, staging, target commit, and subsequent Core closure sync.

## Execution Plan

1. Capture target preflight evidence and hashes.
2. Byte-copy the two active carrier preimages to their archive paths; verify
   archive hashes before changing active files.
3. Create the compact bootstrap JSON and successor handoff.
4. Compact session memory and canonical state. Preserve accepted P4-A1 facts;
   set the new T3 mode and bounded next move.
5. Update AGENTS progressive routing and add the bootstrap path to manifest
   requiredDocs without changing the core commit pin.
6. Synchronize compatibility mirror and implementation status.
7. Recompute SHA-256 for the changed implementation status and update only its
   Project Knowledge source pin plus the required review date.
8. Extend checker/test coverage and repair exact-scope failures.
9. Create the worker return, run all gates, prove exact-14/staged-zero/no
   commit, and stop for independent review.

## Required Behavior

- Bootstrap is valid UTF-8 JSON, at most 4096 bytes, and includes
  `schemaVersion`, `canonicalSource`, `currentMode`, `activeHandoff`,
  `nextAllowedMove`, `parkedOperatorCheckpoint`, `requiredReads`,
  `historyIndex`, and `updatedAt`.
- `AGENTS.md` follows the accepted compact downstream template semantics but
  adapts canonical paths to this project's retained `SESSION/` topology.
- Default startup reads bootstrap first; full canonical state and history are
  targeted lookups only when compact current authority is missing or conflicts.
- Active memory contains only current pointers and bounded claim/next-move
  facts. Historical prose remains byte-preserved in its archive.
- Canonical `required_reads` and bootstrap `requiredReads` contain the same
  existing current paths, no duplicates, and no more than 12 entries.
- Canonical state contains explicit pointers to both pre-T3 archives.
- Successor handoff cites P4-A1 closure `ffe1c5b500f2f27f4166ded97423c4fc76354c67`,
  exact36 `298143d71478993e1c14ab4c20ca8490c1f8e21f`, and independent review
  `d56b835d9c72ec706fc3b8d293aaf85a147ecd6f62c20cfa1afc29baed52ef22`
  with findings/waivers `NONE/NONE`.
- The stale core pin remains unchanged and is recorded as a separate parked
  reconciliation lane, not silently repaired in T3.
- No provider, live, secret, product, public, deployment, push, or commit
  action occurs.

## Scope Firewall Authorization

Downstream worker protected-path authority is limited to the exact-14. The
worker may make content repairs within those target paths without asking again,
including formatting, JSON ordering, checker literals, and focused test
adjustments. Adding another downstream path, changing commit mode, changing
target base, or crossing an external-effect boundary requires return to the
orchestrator. The Core reviewer/closer additionally owns the exact repository-
local closure paths listed below under the packet's Reviewer Closure Conversion
and the operator's delegated authority.

Allowed paths:

- `docs/baselines/CVF_GC018_ACTIVE_CONTINUITY_READ_COST_T3_SHIFT_OPERATIONS_APPLICATION_2026-08-11.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_CONTINUITY_READ_COST_T3_SHIFT_OPERATIONS_APPLICATION_2026-08-11.md`
- `docs/roadmaps/CVF_ACTIVE_CONTINUITY_READ_COST_REDUCTION_ROADMAP_2026-08-10.md`
- `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T3_COMPLETION_REVIEW_2026-08-11.md`
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0052.md`
- `docs/reference/agent_defect_intelligence/entries/README.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V59_2026-08-11.md`

Forbidden paths:

- `AGENTS.md`
- `CLAUDE.md`
- unlisted `CVF_SESSION/` paths
- `governance/compat/`

Every other unlisted Core path and every unlisted target path is also
forbidden, including product runtime, core-pin reconciliation,
provider/live/public/deploy/push surfaces.

Operator authorization: continuation on 2026-08-11 under explicit delegated
orchestrator/reviewer decision authority.

Rollback boundary: discard only the uncommitted exact-14 worker diff; preserve
accepted P4-A1 commits and all other downstream/Core history.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: perform the separately committed Core
session/front-door synchronization required after accepted ACRC-T3 material
closure; update no guard implementation or policy.

Protected paths:

- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V59_2026-08-11.md`

Operator authorization: 2026-08-11 operator delegated full orchestrator and
reviewer closure authority and instructed continuation after the worker return.

Rollback boundary: revert only the ACRC-T3 Core material closure and its
immediately following session-sync commit; preserve target commit `0b835be3f`
and every unrelated Core/downstream history entry.

## Near-Threshold Maintainability Plan

The active 375-line memory and 1372-line state are not compressed in place to
retain history. Their exact bytes are archived; active memory becomes a compact
pointer record, while the state removes the 251-entry startup list and long
blocked narrative from active routing. The full state remains canonical but is
no longer a default startup read.

## Required Checks

Run from the target repository root. Use the target's existing Python and
PowerShell conventions.

```powershell
python scripts/check_session_state.py
python -m pytest tests/cvf/test_session_state_mirror_drift.py -q
python scripts/check_project_knowledge.py
python scripts/testing/validate_repository.py
python scripts/check_file_size.py
powershell -ExecutionPolicy Bypass -File "..\.Controlled-Vibe-Framework-CVF\scripts\check_cvf_workspace_agent_enforcement.ps1" -ProjectPath "." -AllowOfflinePinnedCore
git diff --check
git status --short
git diff --name-status
```

Also run existing targeted Knowledge tests invoked or named by
`scripts/check_project_knowledge.py`. Do not run live readiness or a provider
release bundle because this tranche asserts no AI-governance behavior.

## Verification Commands

Worker runs the target-local command block in Required Checks. The independent
Core reviewer also runs:

```powershell
python governance/compat/run_worker_return_fast_gate.py
```

This Core command validates the returned packet shape and does not substitute
for any target-local implementation check.

## Acceptance Criteria

- AC-01 through AC-11 are exactly those in the paired baseline.
- Every checklist item must be resolved as PASS or N/A with reason; any
  unresolved item produces `BLOCKED_WITH_REASON`.
- Final changed set is exact-14, staged count is zero, and HEAD remains the
  execution base.

## Worker Autonomy / No-Question Rule

Repair allowed-scope failures directly after reading the failing checker/test.
Return only for a real authority contradiction, forbidden-path need, external
effect, or missing dependency that makes exact-scope completion impossible.

## Evidence Requirements

Record commands and exact outputs/counts without secrets; before/after hashes;
archive equality; bootstrap/memory byte sizes; required-read counts; changed
set; staged-zero; HEAD; no-commit; and zero disallowed calls.

## Review Gate

Worker may not self-approve. Independent reviewer recomputes every acceptance
criterion and decides repair, acceptance, target commit, and Core closure sync.

## Closure Checklist

- [x] Exact base, clean status, and preimages verified.
- [x] Archives are byte-identical and retained.
- [x] Bootstrap/memory/read budgets pass.
- [x] Progressive routing and current-authority consistency pass.
- [x] Mirror and all transitively affected Project Knowledge pins are atomic
  and exact after bounded reviewer reconciliation.
- [x] Worker exact-14, staged-zero, no-commit, and zero-disallowed-call evidence
  pass; reviewer closure is an independently recorded exact-15.
- [x] All required local gates pass.
- [x] Worker return is complete and independently reviewed.

All items were recomputed by the independent reviewer before the target commit.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/decisions/ACTIVE_CONTINUITY_READ_COST_T3_WORKER_RETURN_2026-08-11.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

scopeClassification: DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT

requiredGate: target local checks listed in Required Checks

Core reviewer confirmation gate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

publicSyncDisposition: FORBIDDEN

liveRuntimeDisposition: FORBIDDEN

checkerMutationDisposition: FORBIDDEN

workerSelfSelection: FORBIDDEN

The return must include Target / Source, Status, startup declaration, source
inventory, preimage/archive evidence, changed files, gate evidence, first-run
and final-run results, git status, no-commit statement, trace, findings,
claim boundary, and exact return disposition.

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return, inspect target checker/test conventions that
apply to `docs/decisions` artifacts and the exact fields expected by this Work
Order. Do not copy a Core `docs/reviews` skeleton blindly into the downstream
project.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | ORCHESTRATOR/WORK_ORDER_AUTHOR -> IMPLEMENTATION_WORKER -> independent REVIEWER/CLOSER/COMMIT_STEWARD -> SESSION_SYNC_STEWARD |
| phase | WORK_ORDER to BUILD to REVIEW to FREEZE |
| baseHeadFor(phase) | dispatchBaseHead=`4c3d63d1563531f01c0b96cbb720abd2a1b20c5f`; executionBaseHead=`b62271d42150da68d4fb80983cd56260ee11cee1`; closureBaseHead=reviewer captures target execution base |
| changedSetScope(phase) | worker exact-14 target paths; reviewer repairs remain explicitly recorded; Core closure sync is separate |
| traceScope(phase, actor) | worker records all target reads/writes/checks; reviewer records independent recomputation and commit; sync steward records Core-only continuity |
| commitOwner(phase) | worker forbidden; independent reviewer/commit steward owns target commit; Core commit steward owns later separate Core sync |
| crossBatchIsolation | no product, core-pin, public, provider, live, deploy, push, or other roadmap tranche may be batched |
| nextMoveSurfaces | worker updates target current carriers; reviewer converts target closure; Core session sync occurs only after accepted target material commit |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | target `docs/decisions/ACTIVE_CONTINUITY_READ_COST_T3_COMPLETION_REVIEW_2026-08-11.md` |
| reviewerOwnedClosurePaths | target completion review plus allowed-scope repairs and target continuity finalization; later Core roadmap/session closure is a separate commit |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| exact-14 target paths | implement or create exactly as specified |
| two archive paths | byte-copy pinned preimages before active compaction |
| worker return | create complete evidence packet and stop uncommitted |
| completion review | N/A with reason: reviewer-owned and must not be created by worker |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: paired GC-018 baseline and accepted P4-A1 closure

priorVerificationAnchor: exact hashes and commits named in this packet

freshRecomputeRequired: every target preimage, archive digest, gate, and final
changed-set fact

unicodePathHandling: use literal Windows paths and UTF-8-safe readers; authored
artifacts remain ASCII except existing user-facing or protocol data preserved
byte-for-byte

extractedTextAuthority: direct repository bytes and command output only

## Commit Mode And Base-Anchor Lifecycle

Worker begins and ends at exact target HEAD
`b62271d42150da68d4fb80983cd56260ee11cee1`, staged zero, no commit. If HEAD
changes, stop. Reviewer sets closure base from that target commit and owns any
accepted target commit. The later Core closure commit is never part of worker
scope.

## Negative Search And Collision Discipline

Before writing, confirm the four new target paths do not exist and search for
the T3 batch ID and successor handoff name. A collision or existing partial T3
artifact blocks; do not overwrite or merge unknown bytes.

## Legacy Absorption Coverage Index Disposition

| Field | Value |
|---|---|
| Coverage index | NOT_APPLICABLE_WITH_REASON: T3 archives already governed downstream continuity bytes and does not absorb an external or legacy source corpus |
| New coverage item | N/A with reason: no external source, package, or knowledge corpus is ingested |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent returned output |
| Chain map route | governed Core dispatch -> uncommitted downstream return -> independent source review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired T3 baseline and this Work Order |
| Disposition | NOT_APPLICABLE_WITH_REASON: cross-repository execution is not external knowledge absorption |
| Claim boundary | no external source/provider/corpus/public intake or authority promotion |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| stable active front door | canonical downstream bootstrap under `SESSION/` |
| canonical source | existing canonical active state remains unchanged in ownership |
| archive ownership | two dated byte-exact pre-T3 carriers under target `SESSION/archive/` |
| index/discovery | canonical `history_index` and compact bootstrap `historyIndex` point to both archives |
| date policy | archive names carry the dispatch date; active bootstrap remains stable and undated |
| claim boundary | storage/routing only; no runtime memory, RAG, provider, or product persistence claim |

## Provider Memory Authority Boundary

Provider-specific memory is operating guidance only. All implementation facts
must be verified from target repository bytes or the canonical Core packet.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACR-T3 --title "Active Continuity Read Cost T3 Shift Operations Application" --date 2026-08-11 --base b62271d42150da68d4fb80983cd56260ee11cee1 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact cross-repository scope, hashes, checks, and handoff lifecycle |
| checkerReadAheadConfirmation | dispatch-quality, ADIF, handoff, lifecycle, packet authority/encoding, and file-size shapes reviewed |
| docOnlyNewFields | `history_index`; bootstrap `historyIndex` |
| claimBoundary | dispatch packet only; no runtime/provider/live/public behavior claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`downstream-continuity-compaction`, role=`work-order-author`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class downstream-continuity-compaction --role work-order-author --lifecycle-phase pre-dispatch --surface-selector SESSION --risk-ceiling MEDIUM --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no extra defect ID returned; pinned preimages and fail-closed archive controls remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch-ready status; no-commit token; Source Verification columns; roadmap trace; evidence-reuse scalars; handoff and reviewer fields; worker-return terms; public export token |
| gateRunPurpose | confirmation and dispatch evidence, not first discovery |
| claimBoundary | artifact-shape review only; downstream behavior requires worker and reviewer evidence |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator/work-order author |
| Provider or surface | local Core plus read-only downstream inspection |
| Session or invocation | ACRC-T3 dispatch, 2026-08-11 |
| Working directory | private Core for packet; downstream root for read-only verification |
| Command or tool surface | file reads, Git/hash, workspace doctor, resolver, scaffold, apply_patch |
| Target paths | paired baseline, this Work Order, roadmap dispatch status |
| Allowed scope source | operator continuation and roadmap T3 |
| Before status evidence | Core clean worktree and downstream clean worktree at the exact heads named above |
| After status evidence | exact no-commit T3 dispatch packet |
| Diff evidence | pre-dispatch changed-set and autorun output |
| Approval boundary | exact-14 downstream continuity migration only |
| Claim boundary | no product/runtime/provider/live/public/deploy/push claim |
| Agent type | orchestrator/work-order author |
| Invocation ID | `acrc-t3-work-order-2026-08-11` |
| Expected manifest | paired baseline; this Work Order; roadmap dispatch status |
| Actual changed set | resolved by pre-dispatch gate |
| Manifest delta | must match before dispatch commit |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | repository-local continuity files and deterministic validation |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT; local file hashes and test/validator outputs only |
| actionEvidence | CLAIM_REJECTED_NO_ACTION; no runtime action, continuity file mutation only |
| invocationBoundary | worker manually invokes target-local deterministic commands |
| interceptionBoundary | no direct interception, proxy, runtime gate, or coding-agent control claim |
| claimLanguage | compact progressive startup routing and fail-closed local consistency checks |
| forbiddenExpansion | runtime/provider/live/public/package/Web/MCP/model-router, product, deploy, push, and core-pin work remain parked |

## Worker Return

Return exactly one of:

- `COMPLETE_PENDING_INDEPENDENT_REVIEW`
- `BLOCKED_ARCHIVE_OR_AUTHORITY_MISMATCH`
- `BLOCKED_FORBIDDEN_SCOPE_REQUIRED`
- `BLOCKED_WITH_REASON`

Final worker disposition: `COMPLETE_PENDING_INDEPENDENT_REVIEW`.
Final reviewer disposition: `REVIEWER_ACCEPTED`.

## Closure Record

- Target closure commit:
  `0b835be3ff1ac1fbd1c95e365471887202d718b5`.
- Target worker return SHA-256:
  `b4bfb93418b7179ef7db98b85aef077101309077f850fc77ff71d15daf5e971f`.
- Target completion review SHA-256:
  `fb55e9ee55f225e68cd40b33afc8b7205a99ab561022bc25f20720e9c23dd85c`.
- Core evidence digest:
  `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T3_COMPLETION_REVIEW_2026-08-11.md`.
- Reviewer findings: the dispatched exact scope omitted two transitively
  affected Project Knowledge pins, and AC-07 named a new mode without pinning
  its required post-T3 literal. Both were repaired under the packet's
  Reviewer Closure Conversion authority and recorded as ADIF-0052.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work Order status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Paired baseline status | `docs/baselines/CVF_GC018_ACTIVE_CONTINUITY_READ_COST_T3_SHIFT_OPERATIONS_APPLICATION_2026-08-11.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | target `docs/decisions/ACTIVE_CONTINUITY_READ_COST_T3_WORKER_RETURN_2026-08-11.md` | SHA-256 `b4bfb93418b7179ef7db98b85aef077101309077f850fc77ff71d15daf5e971f`; worker made no commit | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T3_COMPLETION_REVIEW_2026-08-11.md` | `Status: REVIEWER_ACCEPTED` | PASS |
| Target material commit | sibling private target | `0b835be3ff1ac1fbd1c95e365471887202d718b5` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ACTIVE_CONTINUITY_READ_COST_REDUCTION_ROADMAP_2026-08-10.md` | `Status: T1_T2A_T2B_T3_PASS` | PASS |
| Registry JSON | no corpus registry source edit required | N/A | BLOCKED with reason: no corpus scan or registry mutation authorized |
| Registry Markdown | no corpus registry Markdown edit required | N/A | BLOCKED with reason: no corpus scan or registry mutation authorized |
| External evidence digest | `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T3_COMPLETION_REVIEW_2026-08-11.md` | SHA-256 `10da21b1fd1dcb98ea638650f79a78913e38b20eba27b83b55482bd7949cdee7`; target evidence normalized without promoting target authority | PASS |
| System loop interlock | no system-loop registry mutation in scope | `governance/compat/check_system_loop_interlock.py` via autorun | PASS |
| Runtime/provider/live evidence | N/A | no runtime/provider/live behavior authorized | N/A with reason |
| Public-sync evidence | N/A | no public-sync authorized | N/A with reason |
| Session continuity | active Core front door/state/handoff | separate session-sync follows material closure | N/A with reason |

## Return-To-Orchestrator Conditions

Return immediately for target base drift, any preimage mismatch, active
worker/reviewer contradiction, archive inequality, required fifteenth path,
core-pin or product change need, external-effect need, or gate defect that
cannot be repaired within exact scope.

## Execution Authority Waiver

operator.checkpoint.waiver: exact-14 T3 execution is authorized only from the
committed exact hash of this packet and paired baseline. Fresh authority is
required for scope/base/commit-mode/external-effect/public/push/deploy changes.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private downstream continuity migration; no public-sync artifact or
authority exists in this tranche.

## Claim Boundary

This Work Order authorizes only an uncommitted, exact-14 downstream continuity
migration and evidence return. It does not claim agent comprehension, universal
auto-load, runtime governance, provider behavior, product capability, public
availability, deployment, release, push, or production readiness.

# CVF GC-018 Baseline - Active Continuity Read Cost T3 Shift Operations Application

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_BOUNDED

Date: 2026-08-11

Batch ID: ACRC-T3

Core dispatch base head: `4c3d63d1563531f01c0b96cbb720abd2a1b20c5f`

Downstream execution base head: `b62271d42150da68d4fb80983cd56260ee11cee1`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator-delegated orchestrator/reviewer

Reviewer owner: independent reviewer/closer

Worker target: provider-neutral implementation worker in shift-operations-workspace

## Purpose

Release the roadmap T3 entry condition and authorize one bounded downstream
continuity migration. The migration adds a compact bootstrap front door,
removes historical startup fan-out, preserves every displaced byte in governed
archives, and leaves all product and external-effect lanes parked.

## Authorization

The operator selected continuation and delegated full orchestrator/reviewer
decision authority on 2026-08-11. The P4-A1 implementation and independent
review are stopped at accepted local closure commit
`ffe1c5b500f2f27f4166ded97423c4fc76354c67`; the current downstream HEAD is
clean at `b62271d42150da68d4fb80983cd56260ee11cee1`. This baseline freshly
releases only the exact protected paths listed below.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| T2B accepted | `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2B_COMPLETION_REVIEW_2026-08-11.md`; material commit `575f8f991fa0446756aea53515ec128c252c5168` | ACCEPT |
| P4-A1 worker stopped | downstream active handoff records exact36 BUILD `298143d71478993e1c14ab4c20ca8490c1f8e21f` and closure `ffe1c5b500f2f27f4166ded97423c4fc76354c67` | ACCEPT |
| Independent review stopped | downstream active state records `REPAIR_5_TEST_SPLIT_REVIEW_PASS` at `d56b835d9c72ec706fc3b8d293aaf85a147ecd6f62c20cfa1afc29baed52ef22`, findings/waivers `NONE/NONE` | ACCEPT |
| Fresh operator selection | operator message `tiep tuc` on 2026-08-11 under previously delegated decision authority | ACCEPT |
| Protected carrier release | exact paths and SHA-256 values in this baseline and paired Work Order | ACCEPT |

## Scope

One continuity-only change in the sibling downstream repository
`shift-operations-workspace`: progressive startup routing, compact current
state, byte-exact archival of displaced history, a rotated handoff, mirror
sync, Project Knowledge source-pin refresh, and focused machine enforcement.

## Non-Goals

No P4-A, P4-A2, application/runtime source, API/UI, provider, model, RAG,
vector index, audit write, persistence, deployment, public sync, push, secret
read, live proof, or CVF-core manifest-pin reconciliation is authorized.

## Design Control Gate

The implementation must preserve the canonical `SESSION/` topology. The new
bootstrap model is a compact projection, not a replacement source of truth.
`SESSION/ACTIVE_SESSION_STATE.json` remains canonical;
`CVF_SESSION/ACTIVE_SESSION_STATE.json` remains a compatibility mirror.
Displaced history must be copied byte-for-byte before active files are
compacted.

## Baseline Decision

Authorize the paired exact-14 no-commit Work Order. Stop on target HEAD drift,
preimage mismatch, active worker/reviewer evidence, archive mismatch,
forbidden-path need, provider/network/live need beyond the already completed
read-only workspace doctor, or semantic loss.

## Approved Budgets

| Surface | Ceiling |
|---|---:|
| `SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | 4096 bytes |
| `SESSION/SESSION_MEMORY.md` | 4096 bytes |
| canonical `required_reads` | at most 12 entries |
| bootstrap `requiredReads` | at most 12 entries |

## Exact Worker Scope

| Target-relative path | Action |
|---|---|
| `AGENTS.md` | UPDATE progressive downstream routing using the accepted compact template semantics |
| `.cvf/manifest.json` | UPDATE requiredDocs with the canonical bootstrap path only; leave `cvfCoreCommit` unchanged |
| `SESSION/SESSION_MEMORY.md` | UPDATE to compact current pointers only |
| `SESSION/archive/SESSION_MEMORY_PRE_T3_2026-08-11.md` | CREATE byte-exact preimage archive |
| `SESSION/ACTIVE_SESSION_STATE.json` | UPDATE current continuity, at-most-12 reads, bounded current blocks, and history pointers |
| `SESSION/archive/ACTIVE_SESSION_STATE_PRE_T3_2026-08-11.json` | CREATE byte-exact preimage archive |
| `SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | CREATE compact current projection |
| `SESSION/handoffs/T3_ACTIVE_CONTINUITY_READ_COST_2026-08-11.md` | CREATE active T3 handoff anchored to accepted P4-A1 authority |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | UPDATE compatibility mirror atomically |
| `IMPLEMENTATION_STATUS.json` | UPDATE continuity-only T3 status and boundary |
| `knowledge/manifest.json` | UPDATE only the `IMPLEMENTATION_STATUS.json` source pin and review date required by that source change |
| `scripts/check_session_state.py` | UPDATE bootstrap, read-count, archive-pointer, budget, and mirror checks |
| `tests/cvf/test_session_state_mirror_drift.py` | UPDATE focused positive and fail-closed coverage |
| `docs/decisions/ACTIVE_CONTINUITY_READ_COST_T3_WORKER_RETURN_2026-08-11.md` | CREATE worker return |

## Fresh Protected Preimages

All values were recomputed in the downstream repository at clean HEAD
`b62271d42150da68d4fb80983cd56260ee11cee1` on 2026-08-11.

| Path | SHA-256 |
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
| current P4-A1 handoff, read-only authority | `e1be2f314959e0c05e4877e88c81361e3678e3d88df526654c6786cf25b4ae96` |

## Required Behavior

1. Verify downstream HEAD, clean status, and every existing-path preimage
   before the first write.
2. Archive the two superseded active carriers byte-for-byte and prove SHA-256
   equality with their pinned preimages.
3. Route startup through the new bootstrap first, then compact memory, active
   handoff, implementation truth, and index; full state/history is targeted
   only when current facts are missing or contradictory.
4. Reduce `required_reads` from 251 to no more than 12 current paths and move
   the prior list plus prior blocked narrative under the state preimage archive
   and explicit history pointers.
5. Rotate the active handoff without changing accepted P4-A1 closure truth.
6. Keep canonical state, compatibility mirror, bootstrap, memory, handoff, and
   implementation status mutually consistent.
7. Refresh the Project Knowledge pin for `IMPLEMENTATION_STATUS.json` in the
   same changed set. Do not change unrelated pins.
8. Extend local checks so missing/drifted/oversized bootstrap, more than 12
   reads, missing archives, and mirror drift fail closed.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| roadmap owns T3 application | VALUE_SET | `docs/roadmaps/CVF_ACTIVE_CONTINUITY_READ_COST_REDUCTION_ROADMAP_2026-08-10.md` | T3 section | `T3` | active continuity roadmap | ACCEPT |
| downstream state owns required read list | EXISTS | canonical downstream source at exact target execution base | state line 8 | `required_reads` | canonical downstream session state | ACCEPT |
| current list has 251 entries | VALUE_SET | canonical downstream source at exact target execution base | state `required_reads` array | `required_reads` | canonical downstream session state | ACCEPT |
| compatibility mirror mapping exists | RUNTIME_BEHAVIOR | canonical downstream checker source at exact target execution base | `_MIRROR_FIELD_MAP`; `verify_mirror_drift` | `verify_mirror_drift` | session-state checker | ACCEPT |
| Project Knowledge pins implementation status | VALUE_SET | canonical downstream Knowledge manifest at exact target execution base | project-context sourcePins | `sourcePins` | Project Knowledge manifest | ACCEPT |
| accepted P4-A1 authority is parked | VALUE_SET | canonical downstream active handoff at exact target execution base | Closure Identity; Next Governed Move | `Closure HEAD` | downstream active handoff | ACCEPT |

## Stop Conditions

- Any downstream existing-path hash differs from the table above.
- Downstream HEAD is not the exact execution base or the worktree is dirty.
- Archive bytes do not match the two pinned preimages.
- More than the exact-14 paths are needed.
- The implementation changes the core pin or any product/runtime surface.
- Any live/provider/public/push/deploy/destructive action becomes necessary.
- Any gate failure cannot be repaired inside exact scope.

## Acceptance Criteria

- AC-01: exact downstream base, clean status, and all preimages pass.
- AC-02: both archives are byte-identical to their preimages.
- AC-03: bootstrap exists, is valid JSON, is at most 4096 bytes, and matches
  current canonical state fields.
- AC-04: active memory is at most 4096 bytes and contains current pointers,
  not chronological history.
- AC-05: canonical and bootstrap read lists each contain at most 12 current
  paths and every path exists.
- AC-06: AGENTS routes progressively and does not require default full-history
  reading.
- AC-07: new handoff, canonical state, mirror, bootstrap, memory, and status
  agree on mode, handoff, next move, and parked boundaries.
- AC-08: P4-A1 accepted hashes and `NONE/NONE` truth are preserved.
- AC-09: only the implementation-status Project Knowledge pin changes for
  source drift; all unrelated pins remain exact.
- AC-10: focused session tests, project Knowledge checker, repository
  validator, file-size check, workspace doctor, diff check, secret scan, and
  exact changed-set checks pass without provider/live calls.
- AC-11: worker return is complete and the worker leaves staged zero and makes
  no commit.

## Review Gate

Independent reviewer must recompute hashes, archive equality, changed set,
budgets, read counts, mirror/bootstrap projections, Knowledge pins, and every
command result before accepting or committing.

Review completed on 2026-08-11. The reviewer accepted the bounded continuity
migration at downstream commit
`0b835be3ff1ac1fbd1c95e365471887202d718b5`, after correcting the post-T3
closure mode and reconciling all three transitively affected Project Knowledge
pins. The repo-local evidence digest is
`docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T3_COMPLETION_REVIEW_2026-08-11.md`.

## Required Evidence

First-run and final-run gate outputs; `git status --short`; `git diff
--name-status`; preimage and archive hashes; byte sizes; read counts; focused
test counts; zero provider/live/network-after-doctor/secret/public/push calls;
and no-commit evidence.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work Order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_CONTINUITY_READ_COST_T3_SHIFT_OPERATIONS_APPLICATION_2026-08-11.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | target `docs/decisions/ACTIVE_CONTINUITY_READ_COST_T3_WORKER_RETURN_2026-08-11.md` | SHA-256 `b4bfb93418b7179ef7db98b85aef077101309077f850fc77ff71d15daf5e971f`; independently accepted | PASS |
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

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent returned output |
| Chain map route | returned output -> raw target capture -> normalized Core completion review -> baseline closure |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; target-local deterministic verification |
| Owner surface | `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T3_COMPLETION_REVIEW_2026-08-11.md` |
| Disposition | ADAPT as bounded execution evidence; retain Core-governed authority |
| Claim boundary | sibling target artifacts are evidence only; no external or provider-local source is promoted |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACR-T3 --title "Active Continuity Read Cost T3 Shift Operations Application" --date 2026-08-11 --base b62271d42150da68d4fb80983cd56260ee11cee1 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced every placeholder with verified cross-repository T3 authority, scope, hashes, and evidence |
| checkerReadAheadConfirmation | dispatch-quality, ADIF disclosure, handoff-boundary, lifecycle-hygiene, packet-authority/encoding, and file-size checker shapes reviewed |
| docOnlyNewFields | downstream bootstrap fields `schemaVersion`, `canonicalSource`, `currentMode`, `activeHandoff`, `nextAllowedMove`, `parkedOperatorCheckpoint`, `requiredReads`, `historyIndex`, `updatedAt` |
| claimBoundary | dispatch authoring only; no runtime/provider/live/public behavior claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`downstream-continuity-compaction`, role=`work-order-author`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class downstream-continuity-compaction --role work-order-author --lifecycle-phase pre-dispatch --surface-selector SESSION --risk-ceiling MEDIUM --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no additional defect-specific control was returned; existing archive, hash, literal-shape, and no-commit controls remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification columns; ADIF query line; Agent Handoff fields; Reviewer Closure fields; Public Export token |
| gateRunPurpose | confirm packet compliance and record evidence before dispatch |
| claimBoundary | checker read-ahead covers artifact shape only; downstream behavior still requires worker evidence and independent review |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator/work-order author |
| Provider or surface | local Core and read-only downstream workspace inspection |
| Session or invocation | ACRC-T3 packet authoring, 2026-08-11 |
| Working directory | private provenance repository; downstream inspected read-only |
| Command or tool surface | local file reads, Git status/hash, workspace doctor, resolver, scaffold, apply_patch |
| Target paths | this baseline and paired Work Order |
| Allowed scope source | operator continuation plus accepted roadmap T3 |
| Before status evidence | Core clean at `4c3d63d1563531f01c0b96cbb720abd2a1b20c5f`; downstream clean at `b62271d42150da68d4fb80983cd56260ee11cee1` |
| After status evidence | fresh exact-path release and no-commit packet |
| Diff evidence | pre-dispatch Git diff and autorun gate |
| Approval boundary | packet authoring and exact downstream continuity migration only |
| Claim boundary | no product/runtime/provider/live/public/deploy/push claim |
| Agent type | orchestrator/work-order author |
| Invocation ID | `acrc-t3-dispatch-authoring-2026-08-11` |
| Expected manifest | this baseline; paired Work Order; roadmap dispatch status |
| Actual changed set | resolved before dispatch commit |
| Manifest delta | pending pre-dispatch verification |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T3 targets a private downstream continuity system; no public artifact
or public-sync action is authorized.

## Claim Boundary

This baseline authorizes a local downstream continuity migration only. It does
not prove agent comprehension, universal auto-load, runtime governance,
provider behavior, product capability, public availability, deployment,
release, push, or production readiness.

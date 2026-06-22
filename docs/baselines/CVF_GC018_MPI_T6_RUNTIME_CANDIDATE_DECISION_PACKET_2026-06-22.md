# CVF GC-018 - MPI-T6 Runtime Candidate Decision Packet

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-22

docType: gc018_baseline

dispatchBaseHead: dc329a99

Batch ID: MPI-T6

Text Encoding Exception: this packet uses ASCII-only prose; no exception
content is required.

## Purpose

Answer the single question the Phase 2 roadmap parked for MPI-T6: whether
the MPI lane should now expand its own scope to build runtime memory access,
vector/durable store integration, external-agent MCP read tooling, or
route-side federation. Per the roadmap's own MPI-T6 section, this packet is
a decision packet only - it must not implement any runtime. The recommended
answer is **DEFER**, bounded to the MPI lane's own changed set, with the
conditions under which a future operator could reopen the question.

This packet is the second authoring attempt. The first attempt (superseded,
not retained as authority here) made an unsupported exhaustive-directory
claim about `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/` and treated
the negative `canReinject` flag state as a repo-wide invariant. Both errors
are corrected below using actual source refresh against pre-existing, non-MPI
runtime surfaces.

## Decision / Baseline / Proposed Tranche

Decision: DEFER, bounded to the MPI lane's own future work orders.

Baseline: MPI-T2 through MPI-T5 closed evidence shows the MPI lane's own
bounded contract/helper/checker additions have not produced a runtime gap,
a blocked operator-stated requirement, or an unresolved overclaim within
that lane's own changed set. This decision does not assert that no runtime
memory route exists anywhere in the repository - pre-existing, non-MPI
surfaces with runtime read/write behavior are documented in the Source
Refresh Table below and are explicitly out of scope for this decision.

Proposed tranche: none. This is a decision record, not a dispatch.

## Operator Authorization

The operator selected MPI-T6 on 2026-06-22 after MPI-T5 closed bounded
(material commit `97e7f9fc`, session syncs `2f28f4d3` and `8534621c`). The
operator separately authorized a review-gate hardening tranche
(`docs/baselines/CVF_GC018_MPI_T6_REVIEW_GATE_HARDENING_2026-06-22.md`, see
Authority Chain row below for its terminal status) that used this packet's
first authoring attempt as a regression fixture; that hardening tranche's
four named defect classes are addressed in this revision. The operator then
instructed: act as packet author (not runtime worker), correct the two named
artifacts only, do not edit checkers, source-refresh the named pre-existing
surfaces, and return this packet pending review without committing. The latest
operator instruction authorizes Codex reviewer correction, closure, and a
private commit before starting the next roadmap.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction (2026-06-22, author revision) | correct MPI-T6 packet author errors; source-refresh named runtime surfaces; no checker edits; return without author commit | ACCEPT |
| Operator instruction (2026-06-22, reviewer closure) | fix remaining findings and commit cleanly before the next roadmap | ACCEPT |
| Phase 2 roadmap | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md`, `## MPI-T6 Runtime Candidate Decision Packet` | ACCEPT |
| Parent MPI roadmap | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | ACCEPT |
| MPI-T5 closure | `docs/reviews/CVF_MPI_T5_MEMORY_ACCESS_CLAIM_CHECKER_COMPLETION_2026-06-22.md` (terminal disposition: closed bounded pass) | ACCEPT |
| MPI-T4 closure | `docs/reviews/CVF_MPI_T4_FEDERATED_MEMORY_READ_HELPER_WORKER_RETURN_2026-06-22.md` (`Status: ACCEPTED_BY_REVIEWER`) | ACCEPT |
| MPI-T3 contract | `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md` | SOURCE_AUTHORITY_FOR_EXTERNAL_READ_BOUNDARY (MPI lane only) |
| MPI-T2 contract | `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md` | SOURCE_AUTHORITY_FOR_REGISTRY_PROJECTION_BOUNDARY (MPI lane only) |
| Memory Plane front door | `docs/reference/CVF_MEMORY_PLANE_MAP.md` | SOURCE_AUTHORITY_FOR_OVERALL_BOUNDARY |
| Review gate hardening baseline | `docs/baselines/CVF_GC018_MPI_T6_REVIEW_GATE_HARDENING_2026-06-22.md` (terminal disposition: closed bounded pass) | ACCEPT - defines the four defect classes this revision must avoid |
| AskUserQuestion role selection (prior session turn) | operator selected "Claude authors GC-018 decision packet directly" | NOT_CVF_SOURCE - provider-local interaction tool output; recorded for continuity only, not cited as CVF authority |

Provider-specific memory, CLAUDE.md, and MEMORY.md are not CVF authority for
this decision and are not cited as ACCEPT rows above. Runtime claims in this
packet were refreshed against current source as of `dc329a99`.

## Dependency Release Evidence

| Dependency | Evidence | Status |
|---|---|---|
| MPI-T5 closure | material commit `97e7f9fc`; session syncs `2f28f4d3`/`8534621c`; review decision `ACCEPTED_BY_REVIEWER and CLOSED_PASS_BOUNDED` | RELEASED |
| Review gate hardening closure | `docs/baselines/CVF_GC018_MPI_T6_REVIEW_GATE_HARDENING_2026-06-22.md`, `Status: CLOSED_PASS_BOUNDED` | RELEASED |
| Operator decision | explicit MPI-T6 selection on 2026-06-22, with explicit packet-author role and a named correction instruction for this revision | RELEASED |
| Source refresh | Source Refresh Table below cites current, non-enumerated, spot-verified source paths and their commit history | RELEASED |
| Dispatch base | committed HEAD `dc329a99` before this revision; worktree carried the two files this packet's own scope authorizes | RELEASED |

## Scope And Owner Boundary

Allowed scope: this decision packet, plus the closure-state lines in the
Phase 2 roadmap recording MPI-T6's drafted, pending-review status.

Forbidden scope: any runtime, route, vector/durable store, CLI/MCP adapter,
provider/live, registry write, checker, or public-sync change. This packet
implements nothing and authorizes nothing beyond its own decision record. No
edit to any `governance/compat/*.py` file is in scope for this packet (the
review-gate hardening tranche already made the only authorized checker
edits, under its own separate GC-018).

Risk ceiling: R0 - a documentation-only decision record. No source, test,
hook, or autorun file is touched by this packet.

## Source Refresh Table

This table replaces the prior exhaustive-directory claim with spot-verified,
non-exhaustive evidence. No row in this table asserts that a directory
contains only the named files; each row verifies the named file's existence,
content, and commit history only.

| Question | Verified evidence | Commit/path evidence | Disposition |
|---|---|---|---|
| Does a pre-existing durable memory read/write route exist outside the MPI lane? | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts` defines `evaluateDurableMemoryRoute` (read) and `evaluateDurableMemoryWrite` (write) against a file-backed store from `cvf-learning-plane-foundation` | added in `3da15a40` and later modified in `5a920a4c`; both commits are outside the MPI-T2 through MPI-T5 changed set (MPI-T2 `468ca3be`, MPI-T4 `28373d14`, MPI-T5 `97e7f9fc`) | YES, pre-existing, not MPI |
| Does a pre-existing API route expose memory readout over HTTP? | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` exports `POST`, requires session cookie or service token, calls `buildMemoryRuntimeReadout` | introduced in `2ebc0b92`, outside the MPI changed set | YES, pre-existing, not MPI |
| Does a pre-existing API route expose durable memory write over HTTP? | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.ts` exports `POST`, requires session cookie or service token, calls `createFileBackedDurableMemoryStore(...).write` | introduced in `bf4dd9c3`, outside the MPI changed set | YES, pre-existing, not MPI |
| Does a pre-existing reinjection path exist where the `canReinject` policy flag can be affirmatively set? | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts`, `evaluateAifMemoryReinjection`: returns `status: 'allowed'` only when both the `canReinject` and `actorAuthorized` policy flags are affirmatively set, after excluding items with a raw payload field, a blocked lifecycle state, or a low provenance score | introduced in `9b1615b8`, outside the MPI changed set | YES, pre-existing, policy-gated, not MPI; the negative `canReinject` flag state is not a repo-wide invariant |
| Are these pre-existing surfaces referenced from request paths? | repository search for `evaluateDurableMemoryRoute`, `evaluateAifMemoryReinjection`, and `buildMemoryRuntimeReadout` under `src/app` includes `app/api/execute/route.ts`, `app/api/execute/route-memory-advisory.ts`, and `app/api/memory/readout/route.ts` | verified at `dc329a99`: execute route call sites at lines 669/671; advisory readout at line 116; memory readout route at line 177 | YES, named request-path references exist; this row does not claim an exhaustive route inventory |
| Does the MPI lane's own changed set (MPI-T2 through MPI-T5) add or modify the named durable/reinjection/memory-route paths above? | none of `468ca3be`, `28373d14`, or `97e7f9fc` changes the named durable-memory, AIF reinjection, or memory API route paths | committed name-status checks for the three MPI commits return no matching path | NO - the named path sets are disjoint |
| Has the MPI lane's own checker (MPI-T5) found a violation in the MPI lane's own closed artifacts? | MPI-T5 completion review Findings/Position: checker self-run passes over the closure range; no violation reported against MPI-T2/T3/T4 artifacts | `docs/reviews/CVF_MPI_T5_MEMORY_ACCESS_CLAIM_CHECKER_COMPLETION_2026-06-22.md`, `## Findings / Position` | NO violation within MPI lane scope |
| Does the current cited authority ask the MPI lane itself to build a new runtime route, vector store, or external-agent MCP read? | the Phase 2 roadmap keeps those builds outside its authorization, and the current operator correction instruction requests packet repair/review only | roadmap `## Non-Goals` and this packet's `## Operator Authorization`; this row does not claim an exhaustive search of operator history | NO CURRENT REQUIREMENT IN THE CITED AUTHORITY |

## Decision

**DEFER, bounded to the MPI lane's own future work orders.** Do not
authorize the MPI lane to build a new runtime memory access route,
vector/durable store integration, external-agent MCP read tooling, or
route-side federation at this time.

This decision does not evaluate, approve, restrict, or pass judgment on the
pre-existing `durable-memory-route.ts`, `aif-memory-reinjection.ts`, or
`app/api/memory/*` surfaces. Those surfaces were built and wired by a
separate, earlier lane (commits `3da15a40`, `5a920a4c`, `9b1615b8`,
`2ebc0b92`, `bf4dd9c3`) before MPI-T2 opened, already exist independent of
any MPI decision, and are not modified, extended, or constrained by this
packet.

Rationale, bounded to what the evidence above supports: within the MPI
lane's own changed set, MPI-T2 through MPI-T5 have not produced an instance
of a runtime gap, a blocked product requirement, or an overclaim that
MPI-T5's checker could not already catch. Expanding the MPI lane's own
scope into runtime/vector/durable work now would be speculative against a
requirement that has not arisen in that lane. This rationale does not extend
to, and should not be read as a judgment on, whether the separate
pre-existing durable/reinjection/route surfaces are sufficient, correct, or
complete - that is outside this packet's Source Refresh Table and outside
the MPI lane's authority.

## Reopen Conditions

This decision may be reopened only when at least one of the following
becomes true, each requiring a fresh operator decision and a fresh GC-018
per the roadmap's own MPI-T6 closing paragraph:

1. an operator-stated product requirement explicitly needs the MPI lane
   itself to add a live runtime memory read, vector/durable store query, or
   external-agent MCP/CLI read that neither the MPI lane's own
   contract/helper layer nor the separate pre-existing durable/reinjection
   surfaces already satisfy;
2. MPI-T5's checker repeatedly flags real overclaim attempts within the MPI
   lane that trace back to an actual missing MPI-lane capability rather than
   a wording error;
3. an external integration partner requires the MPI lane specifically (as
   opposed to the existing pre-existing memory routes) to expose live
   MCP/CLI memory read access as a contractual or platform-compatibility
   requirement.

Any future runtime work triggered by one of these conditions still requires:
fresh operator decision, fresh GC-018, full source verification, live/
provider proof when governance behavior is claimed, public/provenance
boundary review, and explicit secrets/quota handling if applicable - per the
roadmap's own MPI-T6 paragraph, unchanged by this decision.

## Current Runtime Freshness Verification

| Claim | Current evidence | Disposition |
|---|---|---|
| MPI-T2/T3/T4/T5 boundaries are the live source of truth for the MPI lane's own scope | current contract/helper/checker files cited in Authority Chain, verified at `dc329a99` | ACCEPT |
| Pre-existing durable/reinjection/route surfaces exist outside the MPI lane | Source Refresh Table above, spot-verified by file read and `git log`, not by exhaustive directory enumeration | ACCEPT |
| Route wiring within the MPI lane | N/A with reason: forbidden by this baseline; the MPI lane itself has not wired a route | N/A_WITH_REASON |
| Provider/live proof | N/A with reason: no provider behavior is changed or claimed | N/A_WITH_REASON |
| Public sync | N/A with reason: private provenance decision record only; no public artifact is pending | N/A_WITH_REASON |

## Evidence / Verification

Decision verification uses current source reads of the named pre-existing
surfaces, path-specific commit-history
checks confirming disjoint lanes, the MPI-T5 completion review's self-run
result, the review-gate hardening baseline's four named defect classes, and
git log/status evidence. No new test, checker, or runtime artifact is
created or required for a decision-only packet. No exhaustive directory
listing is claimed or required.

## Acceptance And Fail Conditions

Accept this decision packet when the Source Refresh Table cites only
spot-verified, non-exhaustive evidence with commit-history support, the
Decision section states an unambiguous answer bounded to the MPI lane's own
scope, the Reopen Conditions are concrete and checkable, no exhaustive
directory or repo-wide invariant claim is made, and no implementation,
route, or runtime artifact is created.

This packet fails if it is later found to have implemented any runtime
behavior, created any route, vector/durable store, or CLI/MCP adapter,
claimed an exhaustive directory listing, claimed a repo-wide invariant that
the Source Refresh Table itself contradicts, or omitted the Machine Closure
Package required for a closed-equivalent disposition.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision record; no public artifact or public
claim is authorized or pending for this packet or for the Phase 2 roadmap's
MPI-T2 through MPI-T6 tranches.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current source proof and work-order source-verification boundary |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; memory-access claim checker |
| Owner surface | this MPI-T6 GC-018 baseline |
| Disposition | DEFER as a decision record; no absorption into runtime |
| Claim boundary | external/provider memory is not authority; current CVF source controls; AskUserQuestion tool output is NOT_CVF_SOURCE and is not cited as authority above |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MPI-T6 decision-only packet, bounded to the MPI lane's own scope |
| claimDisposition | N/A with reason: no Delta execution-control behavior is implemented or claimed |
| receiptEvidence | N/A with reason: no Delta receipt |
| actionEvidence | N/A with reason: decision packet creates no runtime action evidence |
| claimLanguage | MPI-T6 decision record only; defers MPI-lane runtime expansion; does not evaluate pre-existing non-MPI surfaces |
| forbiddenExpansion | route/schema/auth changes, runtime memory access, vector/durable store integration, CLI/MCP adapter, provider/live, public-sync, checker edits, wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |
| invocationBoundary | none; this is a read-only decision record with no invocation surface |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or route interception |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: decision-only packet has no implementation work order. | N/A with reason | N/A with reason |
| Completion or reviewer artifact | `docs/reviews/CVF_MPI_T6_RUNTIME_CANDIDATE_DECISION_PACKET_COMPLETION_2026-06-22.md` | `Status: CLOSED_PASS_BOUNDED`; `ACCEPTED_BY_REVIEWER` | PASS |
| Roadmap state | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | `Status: MPI_T6_DECIDED_DEFER_PHASE2_FULLY_DECIDED_PRIVATE_ONLY` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | unchanged; generated aggregate drift check is required before commit | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | unchanged; no MPI-T6 registry row is required for a decision-only packet | PASS |
| External evidence digest | N/A with reason: no external evidence is consumed. | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no runtime/system loop is changed by this decision packet. | N/A with reason | N/A with reason |
| Session continuity | active state/front door/handoff | reviewer-owned session sync follows the material closure commit in a separate continuity commit | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt or query acceptance | N/A with reason: MPI-T6 creates no runtime request, receipt, query, or acceptance behavior | N/A with reason |
| Decision value | `DEFER` | PASS |
| Runtime implementation | none in the MPI-T6 changed set | PASS |
| Provider/live proof | N/A with reason: no provider or governance runtime behavior is asserted | N/A with reason |
| Public export | `DEFERRED_PRIVATE_ONLY` | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | decision-packet author (not runtime worker; corrected per operator instruction in this revision) |
| Provider or surface | local workspace |
| Session or invocation | MPI-T6 packet correction, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | source reads, path-specific git history, repository search, reviewer-fast, autorun gates, git commit |
| Target paths | this GC-018 decision packet; roadmap closure-state and residue lines |
| Allowed scope source | operator instruction: correct the two named artifacts only; no checker edits; no commit |
| Before status evidence | committed HEAD `dc329a99`; worktree carried exactly the two files this packet's own scope authorizes (this baseline and the roadmap) |
| After status evidence | reviewer completion, material commit, then separate session-sync commit |
| Diff evidence | `git diff --name-status`, committed material range, and clean final worktree |
| Approval boundary | decision record only; no worker execution turn required or authorized |
| Claim boundary | no route, write, adapter, provider/live, public-sync, checker, or session behavior beyond this decision record and the roadmap closure-state lines |
| Agent type | packet author followed by Codex reviewer/closer |
| Invocation ID | `mpi-t6-runtime-candidate-decision-2026-06-22` |
| Expected manifest | decision packet, Phase 2 roadmap, reviewer completion |
| Actual changed set | decision packet, Phase 2 roadmap, reviewer completion |
| Manifest delta | MATCH |

## Claim Boundary

This baseline records only a DEFER recommendation against the MPI-T6
question, bounded to whether the MPI lane's own future work orders should
expand into runtime/vector/durable work. It does not authorize, implement,
or claim any runtime memory access, vector/durable store integration,
external-agent MCP read tooling, route-side federation, or any other
behavior change. It does not claim that `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/
cvf-web/src/lib/` or any other directory contains only a fixed set of files,
and it does not claim that the negative `canReinject` or `rawMemoryReleased`
flag states are repo-wide invariants - both are scoped to the MPI lane's own
changed set only, and the Source Refresh Table documents a real,
pre-existing, policy-gated path outside that lane where the `canReinject`
policy flag can be affirmatively set under the named exclusion conditions.
This packet is `CLOSED_PASS_BOUNDED` after reviewer correction and acceptance.
The decision remains DEFER and private-only; later runtime work still requires
the Reopen Conditions plus fresh operator authorization and GC-018.

# CVF AHB-T2 Agent Handoff Contract Ratification

Memory class: FULL_RECORD

Status: ACTIVE_RATIFIED

docType: reference

Date: 2026-06-16

Batch ID: AHB-T2

Worker: Claude (contract author, WORKER_MUST_NOT_COMMIT)

Reviewer: Codex (reviewer/closer)

rawMemoryReleased: false

executionBaseHead: cc84e772

EPISTEMIC_PROCESS_NA_WITH_REASON: This is a governance contract-ratification
packet. No model behavior prediction is required. All source facts are verified
against governed artifacts named in the Required First-Read Ledger.

---

## Purpose

Ratify the CVF Agent Handoff Contract as the Central Core for handoff
semantics. This packet converts the AHB-T1 proposed model into bounded contract
decisions that future local views may cite, while leaving machine enforcement,
workspace design, runtime edits, provider proof, and public-sync out of scope.

## Scope / Applies-To

This document is the AHB-T2 ratification packet for the CVF Agent Handoff
Contract. It turns the AHB-T1 proposed model (section D of the audit) into
governed contract decisions by deciding each contract field, reconciling MA1,
dispatch envelope, commit steward, AOT trace, and session-sync next-move surfaces
under one vocabulary, absorbing the closed AOT-T3 rule as a derived AOT input,
and explicitly deciding cross-batch isolation and C3 three-or-more-agent
semantics.

This packet applies to all CVF governed batches across all four first-class role
configurations:

- C1: one-agent-many-roles
- C2: two-agent author-then-execute
- C3: three-or-more-agent chain
- C4: worker-no-commit author/reviewer split

It does not implement any machine check, wire any gate, build the agent-interaction
workspace, edit runtime/source/test files, edit interlock registries, run any
live/provider proof, or public-sync.

## Required First-Read Ledger

| Read ID | File | Evidence used |
|---|---|---|
| R1 | `docs/baselines/CVF_GC018_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | authorization, scope, AC1-AC7, forbidden actions |
| R2 | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB tranche sequence, AHB-T2 purpose, CCLV/Central Core posture |
| R3 | `docs/audits/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_2026-06-16.md` | proposed contract model D.1/D.2, gap ledger, surface inventory |
| R4 | `docs/reviews/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_CODEX_REBUTTAL_2026-06-16.md` | Codex critique: crossBatchIsolation mechanism open, C3 semantics required |
| R5 | `docs/reviews/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_COMPLETION_2026-06-16.md` | bounded closure decisions and follow-up routing |
| R6 | `docs/reviews/CVF_AHB_T1A_FINDING_CLEANUP_COMPLETION_2026-06-16.md` | audit-filename classification fix, canonical defect-class vocabulary |
| R7 | `docs/reviews/CVF_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_COMPLETION_2026-06-16.md` | closed AOT-T3 dispatch-manifest scope rule (B12) |
| R8 | `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md` | required envelope fields: Role, Canonical packet, Commit mode, executionBaseHead, Return contract |
| R9 | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | mode-to-phase table, Commit Split Rule, Single-Agent Multi-Role Rule, WORKER_MUST_NOT_COMMIT Rule |
| R10 | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | Required Agent Operation Trace Block, Expected Manifest And Manifest Delta |
| R11 | `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | MA1 Role Assignment, Role Output Schema, Dissent And Review Ledger |
| R12 | `docs/reference/CVF_NEXT_MOVE_FRESHNESS_CHECKER_STANDARD_2026-06-16.md` | the four active next-move surfaces |
| R13 | `AGENTS.md` | active-handoff registry resolution, successor-handoff rule |

## Pre-Flight Evidence

| Check | Evidence | Disposition |
|---|---|---|
| HEAD at authoring start | `cc84e772` (session-sync commit after AHB-T2 dispatch commit `4b78355f`) | PASS |
| Worktree clean | `git status --short` (empty output) | PASS |
| Dispatch committed | `4b78355f Dispatch AHB-T2 handoff contract ratification`; sync `cc84e772` | PASS |
| Negative search | `rg -n "Agent Handoff Contract\|handoff contract\|crossBatchIsolation\|AHB-T2" docs` (42 files) | predecessor/dispatch inputs only; no same-purpose ratified contract |
| Same-purpose collision | no prior unified AHB-T2 ratification packet found under `docs/reference/`; AHB-T1 audit and Codex rebuttal are predecessor inputs, not collisions | PASS |

## Source Authority

| Source artifact | Verified section | Relevant authority | Disposition |
|---|---|---|---|
| `docs/audits/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_2026-06-16.md` | `## D. Proposed Agent Handoff Contract Model` (D.1, D.2) | proposed field set and surface mapping | ACCEPT as input to ratification |
| `docs/reviews/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_CODEX_REBUTTAL_2026-06-16.md` | `## 5. Condition Delta`; `## 2. Agree / Disagree Findings` | Codex conditions: crossBatchIsolation mechanism open; C3 semantics required | ACCEPT as binding ratification constraint |
| `docs/reviews/CVF_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_COMPLETION_2026-06-16.md` | `## Findings / Position` | B12 dispatch-manifest scope rule: dispatch trace = dispatch changed set only | ACCEPT as closed AOT input |
| `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md` | `## Required Fields` | Role, Canonical packet, Commit mode, executionBaseHead, Return contract | ACCEPT |
| `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | `## Commit Split Rule`; `## WORKER_MUST_NOT_COMMIT Rule`; `## Single-Agent Multi-Role Rule` | phase->changed-set split and commit ownership | ACCEPT |
| `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | `## Required Agent Operation Trace Block`; `### Expected Manifest And Manifest Delta (AOT-T2-C01)` | trace-scope and changed-set attribution fields | ACCEPT |
| `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | `## 4. Role Assignment`; `## 6. Role Output Schema`; `## 7. Dissent And Review Ledger` | N-plus-agent role/dissent predecessor vocabulary (archived; reconciled not superseded) | ACCEPT |
| `docs/reference/CVF_NEXT_MOVE_FRESHNESS_CHECKER_STANDARD_2026-06-16.md` | `## Current Surfaces` | the four active next-move surfaces | ACCEPT |
| `governance/compat/check_work_order_dispatch_quality.py` | `ROLE_ROUTING_MODES` | exactly four canonical route modes | ACCEPT (B13 verification) |

## Ratified Contract Field Set

Each field is decided as RATIFIED, RATIFIED_WITH_BOUNDARY, or DEFERRED_WITH_REASON.

### CF-01: `route`

Decision: RATIFIED

The canonical route value for a governed batch is exactly one of the four tokens:
`SINGLE_AGENT_SINGLE_ROLE`, `SINGLE_AGENT_MULTI_ROLE`, `MULTI_AGENT_SINGLE_ROLE`,
`MULTI_AGENT_MULTI_ROLE`. This is the route selected for this dispatch. It is not
a description of historical role configurations or a vocabulary catalog entry.

Source: `check_work_order_dispatch_quality.py` `ROLE_ROUTING_MODES`; B13 (verified
in AHB-T1 audit section C).

### CF-02: `rolePattern`

Decision: RATIFIED

The `rolePattern` field names the actor-to-role assignment under the selected
route. It resolves the B13/B15 ambiguity: when a document catalogs role
configurations for study (as an audit subject), the literal route-mode tokens
appear in prose or quoted form and do not trigger route-selection gate checks.
Only the `## Intake Role Routing Decision` section's selected value is the active
`route`; everything else is vocabulary metadata.

Named patterns (descriptive, not additional route tokens):

- one-agent-many-roles: one agent holds dispatch-author, executor, reviewer, and
  closer roles across phases; each role change is stated in the artifact with a
  fresh base-head per phase.
- author-then-executor: one agent authors dispatch artifacts; a second agent
  executes and closes.
- three-or-more-agent chain: three or more agents hold distinct roles; MA1 role
  assignment vocabulary applies; AHB-T3 must specify per-actor trace scope and
  commit ownership for this pattern (see CF-07 and the C3 section below).
- worker-no-commit split: one agent authors under WORKER_MUST_NOT_COMMIT; a
  separate reviewer/closer commits accepted material and authors the completion
  review.

Source: AHB-T1 audit D.1; MA1 Role Assignment; B13/B15 verification.

### CF-03: `phase`

Decision: RATIFIED

The four canonical phases for a governed batch are:

1. DISPATCH_AUTHORING: the dispatching actor authors the roadmap, GC-018, work
   order, and dispatch envelope for a worker.
2. EXECUTION: the worker actor (or the executing role in one-agent-many-roles)
   performs the authorized work and returns or commits.
3. CLOSURE: the reviewer/closer actor authors the completion review, commits
   accepted material, and updates roadmap/GC-018 status.
4. SESSION_SYNC: any actor with the steward `session-sync` role updates active
   next-move surfaces (CVF_SESSION_MEMORY.md, ACTIVE_SESSION_STATE.json, active
   handoff, active handoff startup acknowledgment) to reflect the new state.

Source: steward mode-to-phase table in
`docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`.

### CF-04: `baseHeadFor(phase)`

Decision: RATIFIED

Each phase is anchored to a distinct base head:

| Phase | Base-head field | Meaning |
|---|---|---|
| DISPATCH_AUTHORING | `dispatchBaseHead` | HEAD at the start of dispatch authoring |
| EXECUTION | `executionBaseHead` | HEAD after the dispatch commit(s), before the worker begins |
| CLOSURE | `closureBaseHead` | HEAD at the start of closure authoring (usually the execution commit HEAD) |
| SESSION_SYNC | N/A (no material changed set) | session-sync commit uses the material/closure commit as its prior |

These three base-head fields (dispatchBaseHead, executionBaseHead,
closureBaseHead) are canonical. Work orders must state all three when applicable.
Single-field reuse across phases is allowed only when a phase has no independent
commit boundary (e.g., closureBaseHead equals executionBaseHead when the worker
does not commit).

Source: AHB-T1 gap AHB-G3; work-order template base-head fields observed across
PLCS/AHB/AOT tranches.

### CF-05: `changedSetScope(phase)`

Decision: RATIFIED

The changed set for each phase is bounded to that phase's artifacts only:

- DISPATCH_AUTHORING: only the dispatch batch artifacts (GC-018, work order,
  roadmap status update, dispatch envelope). Future execution deliverables listed
  in `## Write Ownership` do not appear in the dispatch trace manifest (B12 rule,
  absorbed from AOT-T3).
- EXECUTION: only the worker-owned files listed in `## Write Ownership` for this
  batch. The dispatch artifacts already committed are not re-listed.
- CLOSURE: only the reviewer-owned closure paths listed in `## Reviewer Closure
  Conversion` (completionReviewPath, reviewerOwnedClosurePaths). Worker execution
  files are re-listed only if the reviewer amends them with allowed repairs.
- SESSION_SYNC: only the session state/front-door/handoff continuity files. No
  material artifacts.

A trace block's `Expected manifest` and `Actual changed set` must list only the
files changed by the actor in that phase; they must not cross phase boundaries.

Source: Commit Split Rule; Dispatch Manifest Scope Discipline (B12/AOT-T3
completion); AHB-T1 gap AHB-G2.

### CF-06: `traceScope(phase, actor)`

Decision: RATIFIED

Each phase and actor combination requires exactly one Agent Operation Trace Block
that describes that actor's work in that phase:

- The DISPATCH_AUTHORING trace block is authored by the dispatching actor and
  covers only the dispatch changed set.
- The EXECUTION trace block is authored by the worker actor and covers only the
  worker changed set (or the uncommitted worker artifacts in a
  WORKER_MUST_NOT_COMMIT split).
- The CLOSURE trace block is authored by the reviewer/closer and covers only the
  closure changed set.
- The SESSION_SYNC trace block is authored by the session-syncing actor and covers
  only the session-sync changed set.

When a single agent holds multiple roles (one-agent-many-roles), it authors
multiple trace blocks - one per phase - rather than one combined block. Each
trace block captures the base head, changed set, and approval boundary for that
phase only.

A trace-bearing reference file that is re-edited by a second actor (gap AHB-G5)
must update its trace block to reflect the second actor's changed set, not the
first actor's original manifest. The re-editor owns the updated trace block.

Source: AOT trace standard Required Agent Operation Trace Block; AHB-T1 gap
AHB-G5; B12/AOT-T3 completion.

### CF-07: `commitOwner(phase)`

Decision: RATIFIED

| Phase | Who commits | Rule |
|---|---|---|
| DISPATCH_AUTHORING | the dispatching actor | standard material commit |
| EXECUTION (WORKER_MAY_COMMIT) | the worker actor | commits its own execution material |
| EXECUTION (WORKER_MUST_NOT_COMMIT) | nobody; HEAD unchanged | worker returns uncommitted artifacts |
| CLOSURE | the reviewer/closer actor | commits all accepted material; owns completionReviewPath and reviewerOwnedClosurePaths |
| SESSION_SYNC | the syncing actor | commits only session continuity files |

For WORKER_MUST_NOT_COMMIT splits (C4), the work order must include a
`## Reviewer Closure Conversion` section with `completionReviewPath` and
`reviewerOwnedClosurePaths` tokens. This is the B14 rule, now ratified as a
contract requirement for C4.

For C3 three-or-more-agent chains: a single actor must be designated as the
closer. If no explicit designation exists in the MA1 role assignment, the
committing actor defaults to the last actor in the chain who holds the reviewer
or closer role. AHB-T3 must specify per-actor commit-ownership when N-plus-agent
chains do not have an explicit closer designation.

Source: steward WORKER_MUST_NOT_COMMIT Rule; Reviewer Closure Conversion (B14
verification); AHB-T1 gap AHB-G4.

### CF-08: `crossBatchIsolation`

Decision: RATIFIED_WITH_BOUNDARY

The ratified rule: one committed or uncommitted dispatch batch per worktree at any
given time. A second dispatch batch must not begin authoring or execution in the
same worktree while the first batch has uncommitted artifacts.

Ratified mechanism: worktree discipline (one-batch-per-worktree at a time).
Before beginning a new dispatch batch, the current worktree must either be clean
(all prior batch artifacts committed) or the new batch must be deferred. The AOT
trace block records `Before status evidence` as a clean-worktree statement; this
is now a contract invariant, not merely a convention.

Boundary: the workspace isolation mechanism (a future dedicated agent-interaction
workspace) is OUT_OF_SCOPE for this ratification. The workspace is AHB-Tn scope.
The queue discipline (how a parked second batch is re-queued after the first
commits) is DEFERRED to AHB-T3, which must specify whether the mechanism is a
queue file, a session-state entry, or a workspace-level signal.

Codex rebuttal noted bounded dissent on mechanism selection (rebuttal finding 2).
The ratified rule is the invariant (one-batch-per-clean-worktree); the
enforcement mechanism is AHB-T3 scope.

Source: AHB-T1 gap AHB-G1; Codex rebuttal finding 2 (mechanism left open);
existing Before-status-evidence convention in AOT trace standard.

### CF-09: `nextMoveSurfaces`

Decision: RATIFIED

The four active next-move surfaces that must be kept consistent at SESSION_SYNC
are:

1. `CVF_SESSION/ACTIVE_SESSION_STATE.json` top-level `nextAllowedMove`
2. `CVF_SESSION_MEMORY.md` section `## Next Allowed Move`
3. the active handoff section `## Next Allowed Move`
4. the active handoff startup acknowledgment

After any material closure commit, the syncing actor must update all four surfaces
to reflect the new allowed move. The Next-Move Freshness Checker enforces this at
the machine level. No active next-move surface may instruct dispatch or execution
of a target that the active session state already records as
`CLOSED_PASS_BOUNDED`.

Source: `docs/reference/CVF_NEXT_MOVE_FRESHNESS_CHECKER_STANDARD_2026-06-16.md`
`## Current Surfaces`; AHB-T1 audit section A inventory row for next-move surfaces.

## Surface Reconciliation Matrix

All AHB-T1 inventoried surfaces are reconciled below. No surface is orphaned.

| Inventory surface (from AHB-T1 section A) | Contract field(s) | Reconciliation verdict |
|---|---|---|
| Dispatch Prompt Envelope (Role, Canonical packet, Commit mode, executionBaseHead, Return contract, Current-time notes, Do-not-misread notes, Required first actions) | CF-01 `route`, CF-02 `rolePattern`, CF-07 `commitOwner(DISPATCH)`, CF-04 `baseHeadFor(EXECUTION)`, return contract | RECONCILED: envelope is the DISPATCH_AUTHORING phase's handoff surface for actor identity, base-head, and commit-ownership intent |
| Steward mode-to-phase table (dispatch, implementation, reviewer-return, closure, push, session-sync, handoff-sync) | CF-03 `phase`, CF-04 `baseHeadFor(phase)` | RECONCILED: steward modes map to the four contract phases; push is a pre-SESSION_SYNC optional phase |
| Commit Split Rule (material / session-sync / handoff-sync separation) | CF-05 `changedSetScope(phase)`, CF-07 `commitOwner(phase)` | RECONCILED: split rule defines the changed-set scope per phase; it is now derivable from CF-05 |
| Single-Agent Multi-Role Rule | CF-02 `rolePattern` (one-agent-many-roles pattern), CF-06 `traceScope(phase, actor)` | RECONCILED: one-agent-many-roles is a named role pattern under C1; per-phase evidence separation is CF-06 |
| WORKER_MUST_NOT_COMMIT Rule | CF-07 `commitOwner(EXECUTION)` for C4 | RECONCILED: rule is now the C4 execution commit-owner constraint |
| Agent Operation Trace Block (Actor, Agent type, Invocation ID, Expected manifest, Actual changed set, Manifest delta) | CF-06 `traceScope(phase, actor)`, CF-05 `changedSetScope(phase)` | RECONCILED: trace block is the per-phase-per-actor evidence record |
| Expected Manifest And Manifest Delta (AOT-T2-C01) | CF-05 `changedSetScope(phase)` | RECONCILED: manifest delta computation derives from the phase's changed-set scope |
| Dispatch Manifest Scope Discipline (B12) | CF-05 `changedSetScope(DISPATCH)`, CF-06 `traceScope(DISPATCH)` | RECONCILED: absorbed as AOT-T3 closed input (see AOT-T3 Absorption section) |
| Boundary-Prose Trigger Discipline (B11/B15 class) | CF-02 `rolePattern` vocabulary distinction | RECONCILED: selected route value (CF-01) vs cataloged vocabulary are distinguished by context; B15 is the specific instance |
| Route mode tokens (4 canonical) | CF-01 `route` | RECONCILED: the four tokens are the CF-01 enum |
| dispatchBaseHead / executionBaseHead / closureBaseHead header fields | CF-04 `baseHeadFor(phase)` | RECONCILED: three fields map to three phases; now a contract invariant |
| Reviewer Closure Conversion (completionReviewPath, reviewerOwnedClosurePaths) | CF-07 `commitOwner(CLOSURE)` for C4 | RECONCILED: B14 is ratified as a contract requirement for C4 CLOSURE phase |
| MA1 Role Assignment, Role Output Schema, Dissent And Review Ledger (archived) | CF-02 `rolePattern`, CF-07 `commitOwner` for C3 | RECONCILED: MA1 is predecessor vocabulary for C3; it is reconciled not superseded; AHB-T3 will formalize per-actor trace/commit rules |
| 4 next-move surfaces | CF-09 `nextMoveSurfaces` | RECONCILED |
| Front-door startup order and current state (CVF_SESSION_MEMORY.md) | CF-09 `nextMoveSurfaces` (SESSION_SYNC binding) | RECONCILED: front-door is the human-readable surface of the CF-09 SESSION_SYNC invariant |
| Active-handoff registry resolution + successor rule (AGENTS.md) | CF-09 `nextMoveSurfaces` | RECONCILED: AGENTS.md governs which handoff is authoritative at SESSION_SYNC |
| Archived ADR: agent handoff contract relationship | predecessor conceptual framing | RECONCILED as predecessor; this packet supersedes it as the ratified contract |
| Agent role assignment matrix | CF-02 `rolePattern` | RECONCILED: role assignment matrix provides the role-to-actor vocabulary that rolePattern draws from |

**Reconciliation verdict: all 18 inventory surfaces are reconciled with no orphan.**

## AOT-T3 Absorption

AOT-T3 (`CLOSED_PASS_BOUNDED` at material commit `08659a5d`) delivered the B12
machine-check rule:

> A dispatch work-order trace `Expected manifest` that lists future execution
> deliverables (paths that belong to the EXECUTION or CLOSURE phase, not the
> DISPATCH_AUTHORING phase) fails with `DISPATCH_SCOPE_VIOLATION`.

This rule is absorbed into the contract as part of CF-05
`changedSetScope(DISPATCH)` and CF-06 `traceScope(DISPATCH)`:

- CF-05 ratifies that DISPATCH_AUTHORING changed-set scope is limited to dispatch
  batch artifacts only.
- CF-06 ratifies that the DISPATCH_AUTHORING trace block describes only the
  dispatch actor's work.

AOT-T3 is not reopened by this ratification. It is a derived check of CF-05 and
CF-06 that was delivered before the contract was ratified. AHB-T3 must ensure its
unified handoff-boundary machine check does not duplicate the AOT-T3 check but
may cite it as a sub-rule.

Source: `docs/reviews/CVF_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_COMPLETION_2026-06-16.md`.

## Cross-Batch Isolation Decision

Gap source: AHB-G1 (no current surface owns cross-batch isolation).

Decision: RATIFIED_WITH_BOUNDARY (see CF-08).

Ratified rule: one committed-or-uncommitted dispatch batch per worktree at any
time. Before beginning a second dispatch batch in the same worktree, the first
batch must either be fully committed (worktree clean) or the second batch must be
deferred via the active session state.

Ratified enforcement surface: the `Before status evidence` row of the Agent
Operation Trace Block is now a contract invariant. The dispatch actor must state
clean worktree as a pre-condition before beginning a new dispatch batch.

Deferred: the queue discipline mechanism and the physical enforcement model (e.g.,
a queue file, a session-state `parkedBatches` entry, or a future workspace
isolation service) are OUT_OF_SCOPE for AHB-T2. AHB-T3 must specify the
enforcement mechanism.

Codex rebuttal bounded dissent acknowledged: the mechanism (one-batch-per-worktree
hard invariant vs queue discipline vs workspace isolation) was left open by design.
This ratification takes the conservative position: one-batch-per-clean-worktree as
a synchronous discipline. The future workspace will enforce this physically (see
AHB-T1 section F); until then, worktree clean is the enforcement signal.

Concrete example at authoring time: AOT-T3 GC-018 was staged alongside the
in-flight PLCS-T3 worktree and had to be removed and queued. Under this ratified
rule, the correct action was to wait until the PLCS-T3 worktree was committed
before beginning AOT-T3 dispatch authoring. The session state `parkedBatches` or
equivalent mechanism to record the deferred batch is AHB-T3 scope.

## C3 Three-Or-More-Agent Semantics

Gap source: AHB-G4 (no rule assigns trace-scope, commit ownership, or closer
identity per actor in a 3-plus-agent chain).

Decision: RATIFIED_WITH_BOUNDARY

### C3 trace scope

Each actor in a three-or-more-agent chain must author its own trace block for its
own phase. The MA1 Role Output Schema (archived) defines that each role actor
delivers to the `## 6. Role Output Schema`; this is now reconciled as each role
actor owning a trace block (CF-06) for its delivery phase.

When the same batch spans multiple actors across multiple phases, the trace blocks
accumulate in the completion review or final work artifact. No single actor
rewrites another actor's trace block; each actor owns its own phase's block.

### C3 commit ownership

A single closer must be designated in the MA1 Role Assignment or equivalent work
order section before the batch begins execution. If the closer is not designated:

- default rule: the actor holding the integration/review role (MA1 section 7
  Dissent And Review Ledger) is the closer.
- if multiple actors hold review roles, the dispatcher designates one before
  dispatch.

This designation is the C3 equivalent of CF-07's `commitOwner(CLOSURE)`.

### C3 closer identity

The closer is the actor who authors the completion review and commits the accepted
material at CLOSURE phase. The closer may be distinct from all execution actors.
For the current two-actor CVF standard (Claude/Codex), the closer is always the
reviewer/critic actor in a worker-no-commit split. For three-or-more actors, the
work order must name the closer explicitly before dispatch.

### C3 boundary

The C3 per-actor trace-scope and commit-ownership rules are RATIFIED here as
canonical intent. AHB-T3 must formalize the machine-checkable version of these
rules (e.g., that a work order with N agents has N trace blocks and one designated
closer). The current machine checks enforce C4 (WORKER_MUST_NOT_COMMIT with
Reviewer Closure Conversion) but do not enumerate per-actor trace blocks in C3
chains. That enumeration is AHB-T3 scope.

Source: MA1 Role Assignment/Output Schema/Dissent sections; AHB-T1 audit matrix
C3 rows; Codex rebuttal finding 3.

## AHB-T3 Implementation Boundary

AHB-T3 may implement:

- a unified handoff-boundary machine check that verifies all nine CF fields in
  this contract for any governed work order, with appropriate per-configuration
  rules;
- C3 per-actor trace-block enumeration check;
- `crossBatchIsolation` queue discipline enforcement (e.g., checking that no
  second batch begins before the first is committed);
- a check that all three base-head fields (dispatchBaseHead, executionBaseHead,
  closureBaseHead) are present and non-empty in dispatch-ready work orders.

AHB-T3 must not:

- weaken or remove the AOT-T3 `DISPATCH_SCOPE_VIOLATION` check;
- replace the existing Commit Split Rule or WORKER_MUST_NOT_COMMIT enforcement;
- implement the agent-interaction workspace (AHB-Tn scope);
- open a registry edit or runtime mutation without a fresh GC-018.

AHB-Tn (workspace design) must derive its isolation model from CF-08
`crossBatchIsolation` so the workspace enforces the same invariant physically
that the current worktree discipline enforces procedurally.

## Claim Boundary

This packet ratifies nine contract fields (CF-01 through CF-09) for the CVF Agent
Handoff Contract. It does not:

- implement any checker or gate;
- wire any autorun or hook-chain script;
- build the agent-interaction workspace;
- edit runtime/source/test/registry files;
- run any live provider proof;
- public-sync or make public catalog changes;
- change active session state;
- claim production, public, or live governance readiness.

The ratified contract becomes the Central Core for handoff semantics. Per-batch
dispatch envelopes, trace blocks, commit steward records, and session-sync surfaces
are Local Views that must cite this contract going forward. The Central Core + Local
View posture is inherited from the PLCS Standing Operating Rule as noted in the AHB
roadmap.

Contract enforcement and machine-check formalization are AHB-T3 scope, requiring a
fresh GC-018 and operator authorization before dispatch.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance contract. No public-sync batch is authorized.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `RULE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `CONTRACT_RATIFIED`; `STANDARD_CANDIDATE` for AHB-T3 machine check |
| Next control action | Codex reviews this packet; if accepted, AHB-T3 machine-check implementation requires fresh GC-018 and operator authorization |
| Worker blame | `N/A_WITH_REASON`: the nine contract fields address shared handoff-boundary semantics across all role configurations, not individual worker fault |

## Rescan Intelligence Hardening

- Original source artifact: AHB-T1 audit and proposed model (section D.1/D.2).
- Predecessor intake artifact: AHB roadmap, AHB-T1 completion, AHB-T1A cleanup,
  Codex rebuttal, AOT-T3 completion.
- Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS.
- Routing matrix status: AHB-T2 ratification DO_NOW; AHB-T3 and workspace remain
  SEPARATE_RUNTIME_TRANCHE or STRATEGIC_OPERATOR_DECISION.
- Semantic sampling status: bounded adversarial samples below.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Dispatch disposition |
|---|---|
| `UNCHANGED_FROM_INTAKE` | the nine proposed fields from AHB-T1 D.1 are carried forward with ratification decisions |
| `CHANGED_DISPOSITION` | AOT-T3 moved from parked candidate to closed-input absorbed as CF-05/CF-06 sub-rule |
| `NEW_FINDING` | none in ratification packet; crossBatchIsolation mechanism and C3 machine-check are deferred to AHB-T3 |
| `REMOVED_OR_REJECTED` | workspace build, registry edits, and checker implementation remain out of scope |

### Follow-Up Routing Matrix

| Lane | Applies to | Rationale |
|---|---|---|
| RESOLVED_BY_DESIGN | AHB-T2 ratification | this packet |
| RESOLVED_BY_DESIGN | AOT-T3 dispatch-manifest scope absorption | absorbed as CF-05/CF-06 sub-rule |
| SEPARATE_RUNTIME_TRANCHE | AHB-T3 unified machine check | requires fresh GC-018 and operator authorization |
| SEPARATE_RUNTIME_TRANCHE | agent-interaction workspace (AHB-Tn) | requires ratified CF-08 and fresh GC-018 |
| STRATEGIC_OPERATOR_DECISION | AHB-T3 dispatch authorization | operator decision after Codex acceptance of this packet |
| OUT_OF_SCOPE | runtime/provider/public-sync/registry/live proof | explicitly forbidden by GC-018 |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AHB-T2-S1 | CF-08 crossBatchIsolation | one-batch-per-clean-worktree is the ratified invariant | mechanism left to AHB-T3 | Could this be read as requiring workspace isolation now? | PASS_BOUNDARY - workspace build is explicitly AHB-Tn scope; only worktree discipline is ratified |
| AHB-T2-S2 | C3 semantics | closer designation required before dispatch | C3 is weakest coverage | Could C3 chains skip closer designation? | PASS_BOUNDARY - ratified rule requires explicit designation or default rule; AHB-T3 must machine-check this |
| AHB-T2-S3 | AOT-T3 absorption | B12 absorbed as CF-05/CF-06 sub-rule | closed input, not reopened | Could AHB-T3 duplicate the AOT-T3 check? | PASS_BOUNDARY - AHB-T3 boundary explicitly forbids duplicating or removing the AOT-T3 check |
| AHB-T2-S4 | CF-06 trace re-edit | re-editor owns updated trace block | AHB-G5 gap | Could a second actor avoid updating the trace block? | PASS_BOUNDARY - contract ratifies the re-editor owns the trace update; machine check is AHB-T3 scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude (AHB-T2 contract author, WORKER_MUST_NOT_COMMIT) |
| Provider or surface | Claude Code local workspace |
| Session or invocation | 2026-06-16 AHB-T2 ratification authoring; base `cc84e772` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, Write, Grep, Bash (git read-only) |
| Target paths | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_WORKER_RETURN_2026-06-16.md` |
| Allowed scope source | AHB-T2 work order + GC-018 (operator instruction 2026-06-16); Codex dispatch commit `4b78355f` |
| Before status evidence | HEAD `cc84e772`; clean worktree |
| After status evidence | ratification packet and worker return authored; HEAD unchanged (worker no-commit) |
| Diff evidence | `git status --short` shows two untracked docs only |
| Approval boundary | contract ratification packet and worker return only; no checker/runtime/registry/provider/public mutation |
| Claim boundary | repo-local ratification only; no enforcement, machine-check, workspace build, or runtime claim |
| Agent type | Claude |
| Invocation ID | `ahb-t2-ratification-authoring-claude-2026-06-16` |
| Expected manifest | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_WORKER_RETURN_2026-06-16.md` |
| Actual changed set | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_WORKER_RETURN_2026-06-16.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

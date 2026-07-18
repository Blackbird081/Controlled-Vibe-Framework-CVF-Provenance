# CVF Web Inheritance T3P2 - Evidence And Liveness Availability Decision

Memory class: governed-worker-decision

Status: ACCEPTED_BY_REVIEWER_WITH_REPAIR

Batch ID: CVF-WEB-INHERITANCE-T3P2

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: `a63625bd7`

## Target / Source

Target: select a truthful, value-backed availability route for an MAO
evidence and liveness Web projection before T3B scope is authored, per the
CVF Web Capability Inheritance And Operator Projection Roadmap's T3 tranche
family.

Source of decision: direct read of
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts`,
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/lifecycle.controller.contract.ts`,
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts`,
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts`,
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.operator.projection.ts`,
`docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md`,
and the accepted T3A and T3P1 completion reviews.

## Purpose

Decide from current source how, or whether, cvf-web may safely project MAO
evidence, milestones, heartbeat, timeout, and recency state, now that T3P1
has delivered a working, tested run-discovery/replay seam over durable task
events.

## Scope / Methodology

Read the required startup surfaces, guard orientation, literal-format
gotchas checklist, the T3P2 work order, the paired baseline, the roadmap's
T3P2 row, the accepted T3A and T3P1 reviews, and every file in the work
order's Source Verification Block before writing. Refreshed every negative
search directly at this execution head rather than reusing T3A's prior
findings, since T3P1 changed the durable run store's capabilities in the
interim. Separated all four required liveness/readout dimensions (heartbeat,
timeout/task state, evidence milestones, recency) before scoring Web
suitability for any of them, completed the terminal availability matrix, and
directly evaluated `DURABLE_EVIDENCE_SUBSTRATE_REQUIRED` as the alternative
route before selecting the final `availabilityDisposition`.

## Refreshed Negative Searches

```
grep -rn "retention|Retention|reconstructLedger|resumeLedger|rehydrate" EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/*.ts
=> every hit is either a comment referencing the contract's Storage And
   Retention Decision, or `evaluateRetention`/`MaoRetentionDecision`/
   `MaoRetentionPolicyInput` in evidence.readout.contract.ts; zero
   `reconstructLedger`, `resumeLedger`, or `rehydrate` hit anywhere

grep -rn "heartbeat" EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts
=> zero hits (the durable run store has no heartbeat concept at all)
```

`evaluateRetention` exists but is a pure classifier over a caller-supplied
`MaoEvidenceRecord` (`RETAIN` / `RETAIN_WITHIN_CLOSURE_WINDOW` /
`ELIGIBLE_FOR_EXPIRY`); it never deletes, persists, or reconstructs a record,
and it presupposes the record it classifies already exists somewhere durable
to classify - which nothing in this codebase currently provides for evidence
records specifically (see the evidence-replay row below).

## Required Availability Matrix

| Required dimension | Current owner | Verified contract | Gap | Web availability |
|---|---|---|---|---|
| retention | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` lines 322-358 (`evaluateRetention`, `MaoRetentionDecision`) | pure classifier: `RETAIN` while the batch is open, `RETAIN_WITHIN_CLOSURE_WINDOW` inside the closure window after closure, `ELIGIBLE_FOR_EXPIRY` after the window elapses; never deletes anything itself | this classifies retention *policy* for a record the caller already holds; it does not persist or reconstruct any record, so it has nothing durable to operate on for evidence specifically | `NOT_AVAILABLE_WITHOUT_PERSISTENCE_OWNER` |
| reconstruction (evidence) | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` lines 158-233 (`MaoEvidenceLedger`) | `private readonly records: MaoEvidenceRecord[]` held only in the constructing process's memory; no file, database, or reconstruction function anywhere in the file | evidence records do not survive process restart; there is no `resumeLedger`-style function, unlike the durable run store's file-backed `resumeRun`/`listRunIds` | `NOT_AVAILABLE_NO_PERSISTENCE` |
| reconstruction (run events/task state) | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` (`MaoFileRunStore.resumeRun`, `.listRunIds`, both accepted in T3P1) | pure, replayable reads: `resumeRun` replays every persisted event through a fresh `MaoEventLedger` with full schema/authority/sequence validation; `listRunIds` discovers valid run identities with the same full validation and zero partial results | none for this dimension; T3P1 closed the discovery gap the T3A decision identified | `AVAILABLE_TODAY` |
| evidence caller | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.operator.projection.ts` lines 68-79 (`MaoOperationalOperatorProjectionInput.ledger: MaoEvidenceLedger`) | the operator projection builder requires a caller-supplied, already-populated `MaoEvidenceLedger` instance; it does not construct or load one itself | representative and live-value pilot source functions construct process-local ledgers, but no cvf-web caller or durable reconstruction path exists; a Web server process restarting would have an empty ledger with no way to recover prior records | `NO_WEB_CALLER_AND_NO_RECOVERY_PATH` |
| milestone availability | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` lines 388-473 (`milestoneForReceiptKind`, `projectWorkspaceMilestones`) | maps `GRAPH`/`ROLE_RESOLUTION`/`INTEGRATION`/terminal `OUTPUT`\|`REVIEW` receipts to milestone kinds; explicitly excludes `INVOCATION` receipts ("no per-heartbeat mirroring"); pure function over an `MaoEvidenceLedger`'s records | inherits the evidence-ledger persistence gap directly: a milestone list generated from an empty post-restart ledger would silently under-report history with no error signal | `NOT_AVAILABLE_NO_PERSISTENCE` |
| heartbeat | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/lifecycle.controller.contract.ts` lines 240-268 (`MaoLifecycleController.heartbeatRecords`, `.heartbeat()`, `.isHeartbeatStale()`) | `private readonly heartbeatRecords: Map<string, MaoHeartbeatRecord>` held only in the constructing controller instance's memory; refreshed search confirms zero heartbeat reference anywhere in `durable.run.store.ts` | heartbeat state has no persistence owner at all and is explicitly excluded from the milestone projection by design ("no per-heartbeat mirroring"), not merely by omission | `NOT_AVAILABLE_BY_DESIGN` |
| timeout / task state | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` lines 392-428 (`recordTimeout`) | writes exactly one durable `TIMEOUT_DETECTED`/`timed_out` event via `this.store.appendEvent` the first time a ceiling is strictly exceeded, idempotency-keyed on `${taskId}:${startedAt}` plus `"TIMEOUT_DETECTED"`; a repeated call after the milestone exists fails closed with `ALREADY_TERMINAL` rather than duplicating; task state itself comes from `buildReadModel` over the same durable event history | none for this dimension: the timeout milestone is durable, idempotent, and replayable through the same `resumeRun`/`listRunIds` seam as any other task event | `AVAILABLE_TODAY` |
| recency | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` lines 371-386 (`classifyReadoutFreshness`) | computes `CURRENT`/`STALE`/`NO_EVIDENCE_YET` purely from a caller-supplied `evaluatedAt` versus the evidence readout's `lastRecordedAt` under a caller-supplied `staleAfterMs`; not an independent heartbeat or process-liveness signal | inherits the evidence-ledger persistence gap; a freshness classification computed from an empty post-restart ledger would always read `NO_EVIDENCE_YET` regardless of real activity, which is misleading if presented as "system freshness" rather than "evidence recency" | `AVAILABLE_ONLY_AS_EVENT_RECENCY_NOT_EVIDENCE_RECENCY` |
| privacy | `MaoTaskGraph`/`MaoEventLedgerEntry` fields (`durable.run.store.ts`, `event.ledger.contract.ts`) versus `MaoEvidenceRecord.safeFields` (`evidence.readout.contract.ts`) | run/task-state fields (`taskId`, `state`, `terminalOutcome`, `lastEventId`, `lastSequence`, milestone kinds) are structurally plain identifiers and enums with no secret shape; evidence's `safeFields` is a caller-controlled redaction result, not a fixed allowlist | none for the durable event/task-state dimension this decision releases; the evidence-privacy gap the T3A decision already flagged remains unresolved and is simply not released by this narrower route | `SAFE_FOR_RELEASED_DIMENSION_ONLY` |
| operator value | roadmap T3 row (`docs/roadmaps/CVF_WEB_CAPABILITY_INHERITANCE_AND_OPERATOR_PROJECTION_ROADMAP_2026-07-18.md`) plus T3P1 acceptance | a durable, replayable, restart-safe run/task/timeout view is real, immediately provable operator value; it requires no new persistence work because T3P1 already delivered the discovery/replay seam | releasing only this dimension for T3B, while evidence/milestones/heartbeat stay explicitly parked, matches accepted current source capability without inventing anything | `REAL_VALUE_AVAILABLE_TODAY_FOR_NARROWED_SCOPE` |
| next owner | N/A for the released dimension (T3P1 already closed it); a persistence owner is the explicit prerequisite for the parked dimensions | N/A | evidence-ledger and heartbeat persistence remain unowned by any current source file | `PARKED_PENDING_FUTURE_PERSISTENCE_DECISION` |

All 11 rows are terminal. None records a blended or provisional
disposition.

## Reviewer Correction

The worker's original evidence-caller row said no source caller outside tests
constructed an `MaoEvidenceLedger`. Independent search found two process-local
pilot callers: `runWorkerPhase` in `representative.pilot.contract.ts` and
`runMaoLane` in `live.provider.value.pilot.ts`. The row is repaired to the
source-accurate boundary: those pilots do construct ephemeral ledgers, while
cvf-web has no caller and no source owner can reconstruct evidence after a
restart. This correction does not change the selected disposition or T3B
release boundary.

## Findings / Position

- **T3P1 changed the picture materially since T3A.** At T3A, the entire
  run/task-state dimension was blocked on missing run discovery. T3P1's
  accepted `MaoFileRunStore.listRunIds` and pre-existing `resumeRun` now give
  a Web caller a safe way to both discover which runs exist and replay their
  full event history read-only, with fail-closed validation and no partial
  results. This closes the run-discovery gap entirely for the durable
  event/task-state/timeout dimension.
- **Evidence and heartbeat remain unavailable for the same structural
  reason identified at T3A: no persistence.** `MaoEvidenceLedger` is
  `private readonly records` in the constructing process's memory only;
  `MaoLifecycleController.heartbeatRecords` is a `Map` in the constructing
  controller instance's memory only. Neither has a file, database, or
  reconstruction function anywhere in the codebase. A refreshed search
  found `evaluateRetention`, which was not present in the T3A audit's
  finding set, but it is a pure retention-policy classifier over an
  already-held record, not a persistence or reconstruction mechanism - it
  does not change the underlying gap.
- **Timeout detection is genuinely durable, not merely evidence-adjacent.**
  `recordTimeout` in `operational.worker.launcher.ts` writes a real
  `TIMEOUT_DETECTED` event through `MaoFileRunStore.appendEvent`, the same
  durable, idempotent, replayable event ledger that task state and run
  discovery already use. This is why timeout/task state is `AVAILABLE_TODAY`
  while heartbeat is `NOT_AVAILABLE_BY_DESIGN`: they are structurally
  different mechanisms (a durable milestone event versus a process-local
  heartbeat map), not two views of the same gap.
- **Recency must be worded precisely.** `classifyReadoutFreshness` measures
  evidence recency, which is blocked on the same persistence gap as
  evidence itself. However, a distinct and available recency concept exists
  for durable events: the `occurredAt`/`createdAtUtc` timestamps already
  present on every replayed `MaoEventLedgerEntry` can support an
  "event recency" readout without needing the evidence ledger at all. This
  decision releases only that narrower event-recency concept, never
  "evidence recency" or "system freshness" as a whole.
- **`DURABLE_EVIDENCE_SUBSTRATE_REQUIRED` was directly evaluated and
  rejected as the sole route.** A full block would be true to the letter of
  "evidence isn't durable yet," but it would discard the real, immediately
  provable operator value that T3P1 already unlocked for run/task/timeout
  state. Blocking all of T3B until evidence/heartbeat persistence exists
  would leave a already-closed-by-T3P1 capability parked for no source
  reason.
- **`EXPLICIT_IN_PROCESS_EVIDENCE_ROUTE` was directly evaluated and
  rejected.** Presenting in-process-only evidence as an operator-visible Web
  section, even with a visible caveat, risks the same false-inheritance
  reading the T3A decision warned against: an operator refreshing the page
  after any server restart would see evidence silently reset to empty with
  no explanation tied to the caveat, which is not "visibly operator-safe" in
  practice even if the words are present on first load.

## availabilityDisposition

`BOUNDED_DURABLE_EVENT_ONLY_WEB_ROUTE`

Rationale: durable event/task-state/timeout value is real and available
today because T3P1 closed the run-discovery gap that blocked it at T3A.
Evidence milestones and heartbeat are explicitly and structurally excluded
from this route because neither has any persistence owner in current
source; releasing them would either require guessing a new persistence
mechanism (forbidden by this packet's scope) or presenting a misleading
process-lifetime-only view. `DURABLE_EVIDENCE_SUBSTRATE_REQUIRED` is
rejected because it would block real, already-available value.
`EXPLICIT_IN_PROCESS_EVIDENCE_ROUTE` is rejected because an in-process-only
evidence section cannot be made visibly operator-safe against a silent
post-restart reset. `DEFER_T3_WITH_REASON` is rejected because there is no
reason to defer the durable event/task-state/timeout dimension, which has
no outstanding gap.

## claimableLivenessDimensions

- **Task/run state** (`buildReadModel` over `resumeRun`'s replayed events):
  `taskId`, `state`, `terminalOutcome`, `lastEventId`, `lastSequence` -
  `AVAILABLE_TODAY`, durable and replayable.
- **Timeout milestones** (`TIMEOUT_DETECTED` events from `recordTimeout`):
  durable, idempotent, replayable exactly like any other task event -
  `AVAILABLE_TODAY`.
- **Run discovery** (`listRunIds`): safe enumeration of valid run identities
  - `AVAILABLE_TODAY`, accepted in T3P1.
- **Event recency** (derived from replayed `MaoEventLedgerEntry.occurredAt`
  timestamps, not `classifyReadoutFreshness`): `AVAILABLE_TODAY` as a
  distinct, narrower concept from evidence recency.
- **Heartbeat**: `NOT_AVAILABLE_BY_DESIGN`. Never claimable through this
  route; the contract itself excludes per-heartbeat mirroring from any
  workspace/Web projection.
- **Evidence milestones and evidence recency**
  (`classifyReadoutFreshness`, `projectWorkspaceMilestones`,
  `MaoEvidenceRecord`): `NOT_AVAILABLE_WITHOUT_PERSISTENCE_OWNER`. Not
  claimable until a durable evidence-ledger persistence owner exists.

## requiredNextOwner

N/A with reason: no new owner is required to release the durable
event/task-state/timeout dimension named above; `MaoFileRunStore`
(`resumeRun`, `listRunIds`, and the existing `appendEvent`/`recordTimeout`
write path) already owns everything this route needs, and T3P1 already
closed the one prerequisite (discovery) this route depended on.

For the explicitly parked evidence/heartbeat dimension, a future persistence
owner would need to be proposed and source-verified in a dedicated GC-018 and
work order before any T3B expansion into that dimension; no such owner
exists in current source, and this decision does not invent one.

## t3bReleaseBoundary

Released to T3B: a read-only Web projection of durable run/task state
(`buildReadModel` output over `resumeRun`), timeout milestones
(`TIMEOUT_DETECTED` events), run discovery (`listRunIds`), and event
recency (derived from replayed event timestamps, not
`classifyReadoutFreshness`). T3B must define its own explicit Web-side
allowlist over these fields (mirroring the T2 `Sot3ActivationEvidenceReadoutEntry`
precedent) rather than passing any raw MAO type through unchanged, and must
follow the same `AVAILABLE`/`EMPTY`/`UNAVAILABLE` server-read-model pattern
already accepted for T2 and used by the existing `runtime-modules` page.

Excluded from T3B: evidence records, evidence-derived milestones
(`projectWorkspaceMilestones`), evidence recency
(`classifyReadoutFreshness`), heartbeat state, and any "live worker" or
"active process" claim. None of these may appear in a T3B Web surface under
any label, including a caveated or read-only one, until a durable
persistence owner for the evidence ledger and/or heartbeat state is
separately proposed, source-verified, and authorized.

## Risk / Corrective Action

No corrective action was required; every row resolved from current source
without a source contradiction, execution-head mismatch, or need to edit a
forbidden path. The principal risk this decision manages is a false or
overbroad evidence/liveness claim: without the explicit dimension-by-
dimension separation above, a future T3B implementer could read
`evaluateRetention`'s existence and mistakenly conclude evidence persistence
already exists, or could conflate durable timeout events with evidence
milestones because both ultimately derive from the same "receipt" vocabulary
in the runtime foundation contract. Both risks are closed here by keeping
run/task/timeout state (durable, released) structurally separate from
evidence/heartbeat (in-memory only, excluded) in every finding and matrix
row.

## Finding-To-Governance Learning Disposition

N/A_WITH_REASON: no repeated or non-obvious governance-gate defect pattern
was discovered while authoring this decision; the ADIF resolver query for
`taskClass=architecture, role=worker, lifecyclePhase=pre-implementation`
returned zero defects.

## Epistemic Process Block

Expected Result / Prediction: T3P1's accepted `listRunIds`/`resumeRun` seam
would make durable run/task/timeout state safely Web-projectable today,
while evidence and heartbeat would remain blocked by the same in-memory-only
persistence gap identified at T3A, since neither `MaoEvidenceLedger` nor
`MaoLifecycleController.heartbeatRecords` gained any new persistence owner
between T3A and this tranche.

Evidence Comparison Requirement: confirmed directly. `resumeRun` and
`listRunIds` are unchanged in their read/replay/discovery guarantees and are
now accepted (T3P1 completion review). `MaoEvidenceLedger` still declares
only `private readonly records: MaoEvidenceRecord[]` with zero persistence
function anywhere in `evidence.readout.contract.ts`.
`MaoLifecycleController.heartbeatRecords` still declares only a
constructor-scoped `Map`. The one new finding not present in T3A's audit,
`evaluateRetention`, was directly read and confirmed to be a pure
classifier over an already-held record, not a persistence mechanism,
so it does not contradict the prediction.

Contradiction Handling Requirement: no contradiction was found. The
prediction is confirmed as stated; the availability matrix records the
`evaluateRetention` finding as a refinement/clarification (retention policy
exists, but nothing durable exists for it to classify for evidence
specifically), not a reversal.

Claim Update Requirement: Claim confirmed and narrowed to an exact
dimension boundary. The T3A blanket `SPLIT_T3B_PREREQUISITE_OWNER_REQUIRED`
verdict is now split further: the run-discovery prerequisite it named is
closed (T3P1), so the durable event/task-state/timeout dimension is
released to T3B under `BOUNDED_DURABLE_EVENT_ONLY_WEB_ROUTE`, while the
evidence/heartbeat dimension remains blocked pending a separate persistence
decision this packet does not authorize.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_equivalence_claim_evidence.py` |
| literalTokensReviewed | checker-read-ahead section field names (`applicableCheckersRead`, `literalTokensReviewed`, `gateRunPurpose`, `claimBoundary`); trace-block required label set (`Actor`, `Provider or surface`, `Session or invocation`, `Working directory`, `Command or tool surface`, `Target paths`, `Allowed scope source`, `Before status evidence`, `After status evidence`, `Diff evidence`, `Approval boundary`, `Claim boundary`, `Agent type`, `Invocation ID`, `Expected manifest`, `Actual changed set`, `Manifest delta`); target/source heading group |
| gateRunPurpose | evidence confirmation run after direct checker-source read, applying the per-output checker-read-ahead lesson learned during T3A |
| claimBoundary | structural conformance does not replace implementation review |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated source-audit worker |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-WEB-INHERITANCE-T3P2 no-commit worker execution, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | Read, Write, Bash (grep/search), governance gate scripts |
| Target paths | `docs/reviews/CVF_WEB_INHERITANCE_T3P2_EVIDENCE_AND_LIVENESS_AVAILABILITY_DECISION_2026-07-18.md`; `docs/reviews/CVF_WEB_INHERITANCE_T3P2_WORKER_RETURN_2026-07-18.md` |
| Allowed scope source | dispatched work order `CVF_AGENT_WORK_ORDER_CVF_WEB_INHERITANCE_T3P2_EVIDENCE_AND_LIVENESS_AVAILABILITY_DECISION_2026-07-18.md` |
| Before status evidence | clean worktree at `a63625bd7`; no T3P2 decision or worker return existed |
| After status evidence | this decision artifact exists with all 11 terminal matrix rows and one selected `availabilityDisposition`; worker return records evidence |
| Diff evidence | `git diff --name-status` shows no modified tracked path; `git status --short --untracked-files=all` shows exactly two untracked new paths |
| Approval boundary | T3P2 documentation-only evidence/liveness availability decision dispatch only |
| Claim boundary | no persistence, Web, execution, provider/live, public, push, or production mutation |
| Agent type | delegated source-audit worker |
| Invocation ID | `cvf-web-inheritance-t3p2-worker-2026-07-18` |
| Expected manifest | `docs/reviews/CVF_WEB_INHERITANCE_T3P2_EVIDENCE_AND_LIVENESS_AVAILABILITY_DECISION_2026-07-18.md`; `docs/reviews/CVF_WEB_INHERITANCE_T3P2_WORKER_RETURN_2026-07-18.md` |
| Actual changed set | `docs/reviews/CVF_WEB_INHERITANCE_T3P2_EVIDENCE_AND_LIVENESS_AVAILABILITY_DECISION_2026-07-18.md`; `docs/reviews/CVF_WEB_INHERITANCE_T3P2_WORKER_RETURN_2026-07-18.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred in this tranche |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance T3P2 no-commit worker execution; no public-sync action.

## Claim Boundary

This decision authorizes no implementation, persistence, runtime, source,
test, page, provider/live, public, push, release, or production mutation. It
records one terminal `availabilityDisposition`
(`BOUNDED_DURABLE_EVENT_ONLY_WEB_ROUTE`), an exact `claimableLivenessDimensions`
boundary, `requiredNextOwner: N/A with reason` for the released dimension,
and an exact `t3bReleaseBoundary` for a future, separately authorized T3B
packet. Independent reviewer/closer recomputation of every source seam and
negative search, and any roadmap release or closure commit, remain pending
and out of scope for this artifact.

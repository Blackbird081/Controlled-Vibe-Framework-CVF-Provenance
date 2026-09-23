# Multi-Agent Control Value Retrospective - Local Rebuttal

Memory class: review-response
Status: LOCAL_ANALYSIS_RESPONSE_CANDIDATE
Date: 2026-09-23
Decision owner: Local orchestrator/reviewer
Reviewed repository HEAD: `85f2d834df06c78998d6b2593fc43d1673311835`

## Purpose

Consolidate the operator-relayed cross-provider critique into reusable agent
lessons and testable CVF improvement candidates. This is a discussion artifact,
not a work order or a completion review. The operator will relay it to the
responding reviewer; no agent invocation is requested by this artifact.

## Target / Source

- Response: `docs/reviews/CVF_MULTI_AGENT_CONTROL_VALUE_RETROSPECTIVE_CROSS_PROVIDER_RESPONSE_2026-09-23.md`.
- Observation: `docs/reviews/evidence/cvf-multi-agent-control-value-retrospective-2026-09-23.json`.
- Bounded technical evidence: `docs/reviews/CVF_AUTORUN_ACTIVE_WORK_ORDER_LANE_BINDING_R1_COMPLETION_2026-09-23.md`.
- Current parked-path authority: `AGENT_HANDOFF_V63_2026-09-18.md` and `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.

## Scope / Methodology

Read the response in full and inspect selected owner/checker sections. Recompute
the bounded Git diff statistics. No implementation replay or complete session
audit was performed. The response is advisory input from a shared-workspace
reader; a different provider does not change repository authority or create an
organizationally independent reviewer. No source corpus was imported.

## Findings / Position

The strongest correction to the initial retrospective is accepted: orchestration
cost includes CVF packet, continuity and evidence-maintenance overhead. Changing
model selection alone cannot remove that overhead. The Local orchestrator owns
the omitted dependency and its integration decisions; a worker correctly stopping
at its manifest boundary is not evidence of worker incompetence.

| Item | Disposition | Reason and amendment |
|---|---|---|
| R-01 | ACCEPT_WITH_AMENDMENT | Reduce packaging through existing task-proportional routing. Its Profiles And Minimums already define P1_LIGHT and P3_ELEVATED. Canonical checker/hook/authority changes remain P3 regardless of line count; the autorun repair is not a valid low-risk micro-repair example. Document-line share is a cost signal, not a measured time share. |
| R-02 | ACCEPT | Mutable pin targets create avoidable maintenance. Candidate: retain an immutable dispatch snapshot and separately record closure status. Preserve exact-byte provenance and authority checks; do not merely omit status fields from hashing without a versioned canonicalization contract. |
| R-03 | ACCEPT_WITH_AMENDMENT | The thirteen paths are explicitly parked with preservation authority. Determine ownership and terminal disposition before any movement or commitment. Read-only review or isolation may help, but 'cheapest improvement' is unmeasured. A clean isolated worktree must not be used to conceal required shared-workspace diagnostics. |
| R-04 | ACCEPT_WITH_AMENDMENT | Preserve the telemetry failure, but reject the present fail-open classification. Collector post-commit exit 0 is intentional. Its code records an unsafe marker and excludes failed collection; next pre-commit is the blocking boundary. Whether this particular attempt followed every step still needs its journal/marker evidence. |
| R-05 | ACCEPT_WITH_AMENDMENT | Pre-dispatch dependency discovery is useful. Require a disposition for each known dependent owner, not automatic inclusion of every dependent file in worker write scope. Reviewer-owned repair, immutable reference and explicit blocker are distinct valid routes. |
| R-06 | ACCEPT_WITH_AMENDMENT | Build a bounded event timeline if it changes the improvement priority. Commit intervals are elapsed proxies containing possible idle/operator/parallel time. They cannot allocate Worked seconds or quota precisely to implementation versus packaging. |
| R-07 | ACCEPT | Reuse existing fields and mechanically derive available data. No delegation packet is needed when delegation is disabled. Any new requirement must name the repeated manual step it removes or risk it prevents. |
| R-08 | ACCEPT_WITH_AMENDMENT | A read-only reviewer from another provider is a possible risk-triggered option. Provider diversity is neither guaranteed independence nor proven lowest cost. Separate fixtures, adversarial assertions and bounded review scope determine its evidential value. No automatic invocation is authorized. |

### Concrete owner and checker answers

1. Packet proportionality: `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md`, Profiles And Minimums and TPGR-T0 Legacy Full-Gate Interlock. T0 requires the full legacy bundle; the standard makes selective execution conditional on later equivalence evidence. This inspection does not establish the current acceptance status of every later TPGR tranche.
2. Packet role separation: `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` and `governance/compat/check_work_order_dispatch_quality.py` own worker/closer boundaries. A merged file must not allow a worker to author its own acceptance. A packet merger cannot be declared compatible without examining all affected shape consumers.
3. Hash binding: `governance/compat/check_semantic_convergence_control.py`, predecessor verification and `_repo_predecessor_hash_resolver`; `governance/compat/check_independent_review_probe_admission.py`, `bind_evidence`, requires a regular file and recomputed SHA-256. A snapshot route needs compatible consumers and negative tests for stale/substituted snapshots.
4. Freshness: `governance/compat/check_system_chain_map_freshness.py` checks recorded source fingerprints against bytes. That is drift detection; this targeted inspection has not established whether another existing owner already supplies complete reverse-dependency dispatch planning. Do not infer repository-wide absence.
5. Collector: `governance/compat/mfrp_shadow_canary_autocollect.py`, `generate_current_receipt` failure handling and `main`, distinguish unsafe collection from commit completion. Inspect the actual failed attempt before promoting an incident finding.

### Evidence corrections requested from the responding reviewer

- Clarify the statement that commands ran at HEAD `622bc4b0f`, versus target HEAD `85f2d834d`. Separate the command's explicit commit range from the workspace snapshot used for parked-file observations.
- Give the exact command, timezone, endpoints and classification rule behind 64 commits / 26 sync / 12 fix. Subject heuristics are useful but remain heuristic.
- Retain 10h26m13s = 37,573 seconds as operator-reported Worked. Preserve 'one week of Codex quota' as an operator report without a numeric currency/token allocation. Neither is a verified per-model meter.
- Treat +1854/-59 across 18 files as reproduced for `git diff --shortstat 3403a1f13^ 85f2d834d`. Do not convert line counts into a causal estimate of wasted compute.

## Risk / Corrective Action

The next response should consolidate disagreements rather than add another
unbounded standards proposal. For R-01 through R-08, return only changed
dispositions, source-backed corrections and unresolved decision-changing gaps.
Do not repeat implementation or launch live experiments to answer this critique.

Proposed improvement order: first resolve measurement boundaries and parked-path
ownership; then compare existing-owner options for immutable provenance and
proportional packaging; then admit only the minimum dependency/telemetry changes
that measurably remove repeated work. This is a candidate order, not authority
to move files, weaken gates or reopen paused implementation.

## Agent Learning And Future Acceptance Evidence

| Lesson | Observable behavior for a future bounded task | Failure signal |
|---|---|---|
| Optimize accepted outcome | Record elapsed proxy, accepted scope, rework and operator interventions together | More passing checks cited as sufficient evidence of productivity |
| Strength does not repair a bad contract | Identify dependency owners and the hard uncertainty before choosing effort | Strongest model selected merely because the role is reviewer |
| Delegation has integration cost | Name a disjoint deliverable, a usable oracle and expected benefit | Added agent duplicates root reading or leaves all integration serial |
| Control resources as well as authority | Use a declared parent budget and preserve unavailable usage as unknown | Internal helpers implicitly treated as free |
| Preserve valid work | Consume returned evidence unless a named contradiction justifies rerun | Broad replay with no expected information gain |
| Governance must earn its cost | Compare manual steps/artifacts before and after a candidate change | New mandatory fields without removed work or demonstrated risk reduction |
| Keep review claims precise | Distinguish self-review, separate actor, separate oracle and provider diversity | A different role/model label used as proof of independence |

Success criteria for a future improvement: fewer repeated manual steps and repair
rounds on comparable natural tasks, while preserving rejection of unauthorized
writes, evidence substitution and self-approval. Record difficulty and differences;
do not claim causal superiority from a single sample. No expensive replay is
requested. Both provider critiques remain evidence inputs, not automatic policy.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Purpose; Scope / Target / Owner Boundary; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; claimBoundary |
| gateRunPurpose | Local closer confirmation of candidate evidence shape, not first discovery of semantic findings. |
| claimBoundary | Targeted checker inspection supports named binding claims; no full governance behavior claim. |

## Agent Operation Trace Block

Actor: Local orchestrator/reviewer. Surface: shared private workspace.
Authorization: operator requested a persisted rebuttal and future learning evidence.
Action: targeted reads and creation of this response only.
Diff evidence: exact added response file; original critique and observation retained.
No commit, agent invocation, account action or source creation performed.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Rejoinder Adjudication - 2026-09-23

Read in full:
`docs/reviews/CVF_MULTI_AGENT_CONTROL_VALUE_RETROSPECTIVE_CROSS_PROVIDER_REJOINDER_2026-09-23.md`.
The responding reviewer accepts R-01 through R-08 and corrects its stale HEAD
and fail-open claims. These corrections are accepted. The discussion has
converged on the lessons; further model-ranking debate adds no supported value.

### P4-C1 safety marker adjudication

Local reviewer/closer decision: REJECT_FAILED_OBSERVATION_AND_ARCHIVE_MARKER.
The unresolved marker's SHA-256 before movement is
`d74f3b070e11b02bb8ba8b6c523d3e4ca85ee023dfae361e3e7e6cb6d59ff93f`.
Its code is `UNSAFE_AUTORUN_RECEIPT_GENERATION_FAILED` and its detail identifies
an unauthorized material/session range mixture. `git show --format= --name-only
ee81deeeb` confirms three protected state paths alongside implementation and
review artifacts in that one commit. The pending P4-C1 journal preserves the
failed outcome at disclosure commit `85f2d834d`; no replacement PASS receipt or
sample is claimed. Pre-commit marker blocking therefore served its purpose.
The marker is preserved byte-for-byte as
`.cvf/runtime/mfrp-p4-shadow-canary/ADJUDICATED_REJECTED_OBSERVATION_2026-09-23_AUTORUN_R1_MIXED_COMMIT.json`.
Only the unresolved runtime location is cleared after this decision. The
historical mixed commit and its failed observation remain rejected; this
adjudication authorizes no retroactive collector pass or hook bypass.

### Newly verified findings

- G-2 is CONFIRMED at current HEAD: in
  `governance/compat/run_agent_commit_steward_preflight.py`, `build_path_plan`
  unions `_range_paths(base, head)` with `_status_paths()`. `_has_agent_operation_trace`
  and `_has_exact_mixed_atomicity_authorization` read current filesystem text.
  `governance/compat/run_agent_autorun_workflow_gate.py`, `_range_shape_preflight`,
  calls this plan while describing its result as committed-range evidence.
  Both path scope and content snapshot can therefore depend on mutable worktree
  state. This establishes a mismatch at this caller, not that all steward
  worktree-aware uses are wrong.
- G-1 recurrence is plausible, but eight equal root causes are not established
  by a shared error string. Only the current marker and relevant code were
  independently inspected here; the eight-event classification remains the
  responding reviewer's reported runtime observation.
- C-1's proposed repair is NOT ACCEPTED AS SPECIFIED for the current incident.
  `mfrp_shadow_canary_autocollect.py::generate_current_receipt` already uses
  the trusted commit's single parent as base and the trusted commit as head;
  it explicitly excludes the disclosure commit. `git show --format= --name-only
  ee81deeeb` confirms the material commit itself includes bootstrap, aggregate
  and core session state alongside implementation and review files. Splitting
  successive material/sync commits cannot remove this intra-commit mixture.
- The current `UNRESOLVED_SAFETY_MARKER.json` was read directly and confirms
  receipt-generation failure plus the next-pre-commit blocking boundary. The
  marker was not cleared. No failed observation was enrolled or relabeled PASS
  by this review. A marker alone does not prove execution of the next hook.
- G-3 is accepted as a limitation of the cited T0 contract. No repository-wide
  determination of later TPGR acceptance is claimed by this targeted review.

### Corrected improvement candidate

First separate committed-evidence analysis from pending-worktree planning at
the caller boundary. Preserve the existing pending-worktree checks where they
are intended. Committed evidence must use both paths and content from its
declared Git snapshot, including trace and atomicity authorization content.

Candidate acceptance probes:

1. Adding an unrelated untracked trace document cannot change a committed-range verdict.
2. Editing/deleting a tracked trace or authorization document in the worktree cannot change that historical verdict.
3. A single commit with an unauthorized material/session mixture remains rejected.
4. An authorized atomic mixture must satisfy the existing exact-manifest contract using committed evidence; no blanket exclusion is allowed.
5. Pending-worktree planning still sees unauthorized pending changes.
6. Missing/substituted receipt evidence remains rejected.

Before changing range selection, classify each reported recurrence against its
actual base/head, committed paths, and authorization. Distinguish genuine mixed
commits, worktree contamination, authorized atomic companions and multi-commit
range selection. Marker adjudication is separate from fixing those causes.

### Additional agent lessons

- Refresh HEAD at measurement time in a shared workspace; retain explicit endpoints.
- A repeated diagnostic is evidence of recurrence, not proof of one root cause.
- Validate a proposed fix against the actual call path before accepting it.
- A historical evidence check must not silently depend on mutable filesystem bytes.
- Local closure owns the mixed-commit decision. The collector's refusal is not
  automatically a collector defect, even when its diagnostics contain unrelated paths.

No additional provider response is needed to accept these lessons. The useful
next technical work is the bounded recurrence classification and a compatible
snapshot-scope design, before any guard implementation. This records an
improvement candidate, not a new dispatch or a completed foundation upgrade.

## Claim Boundary

Candidate analysis only. This response does not establish a new guard, complete
a CVF foundation upgrade, enroll a P4 sample, prove model ranking or authorize
subagents. Further implementation must preserve current source and authority
boundaries. The operator's no-subagent instruction remains controlling.

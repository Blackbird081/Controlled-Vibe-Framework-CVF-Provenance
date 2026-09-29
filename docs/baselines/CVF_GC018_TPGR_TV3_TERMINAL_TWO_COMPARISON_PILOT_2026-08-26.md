# CVF GC-018 Baseline - TPGR-TV3 Terminal Two-Comparison Pilot

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-26

Batch ID: TPGR-TV3

Dispatch base head: `4403175d13a6d743441ace2d90ffc4f53c5e4f84`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: delegated worker role

## Purpose

Run exactly two repository-local retrospective comparisons to measure whether
the TV2 shadow decision would have avoided false stop or false continuation
against accepted CVF decisions. Produce one terminal recommendation without
editing implementation owners or opening a successor.

## Scope / Target / Owner Boundary

| Comparison | Accepted evidence | TV3 question |
| --- | --- | --- |
| remediation | EAFR-R11 admitted exactly one consolidated R12 repair for a source-backed P1 with unknown economics | would the shadow rule preserve the serious repair while preventing an open-ended successor chain? |
| absorption/project boundary | MCP-KAR-T2 stopped four schema candidates because no current owner or consumer existed | would the common value fields prevent a false continuation without claiming that TPGR is activated for absorption? |

The second row is comparison-only. The TPGR standard still requires a separate
accepted class design before a `trancheValue` record is declared for absorption
or app/project delivery.

## Proposed Tranche / Decision

Admit TV3 as the final comparison-only tranche with exactly one worker-return
file. Decision: `CONTINUE_HIGH_VALUE` under the explicit terminal cap and
operator approval; no implementation or successor authority follows.

## Tranche Admission And Cost Envelope

| Field | Value |
| --- | --- |
| outcomeConsumer | dispatchers and reviewers deciding whether the value gate deserves retention |
| severity | P2 terminal evidence tranche; comparison A contains historical P1 evidence |
| findingEvidenceState | HISTORICAL_BOUNDED |
| rootCauseIdentity | independent terminal calibration gap; no implementation defect asserted |
| marginalValue | decide retain/close versus park without another implementation tranche |
| valueEvidenceState | HISTORICAL_BOUNDED |
| workerTime | projected 20 minutes maximum |
| reviewerTime | projected 15 minutes maximum |
| latency | one worker round trip plus one reviewer pass |
| tokenOrQuotaUsage | bounded documentary analysis; no provider API quota |
| providerCallCost | UNKNOWN; calls forbidden, never represented as zero |
| opportunityCost | displaces no P0/P1 repair and ends at TV3 |
| consolidationKey | TPGR_TV3_TERMINAL_COMPARISON |
| stopCondition | stop after two comparisons and one terminal recommendation |
| successorAuthority | roadmap cap 3, current ordinal 3, no TV4 |
| decisionReason | TV2 is accepted and two historical decisions provide bounded calibration value |
| reviewerIdentity | independent reviewer/closer after worker return |
| freshness | captured 2026-08-26; fixed committed evidence, no external refresh |
| overrideAppealEvidence | NONE |

Value disposition: `CONTINUE_HIGH_VALUE` for TV3 only. This decision is
non-authoritative shadow evidence for the worker pass and cannot relax the
P3 route or full legacy bundle.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| TV2 independent acceptance | `docs/reviews/CVF_TPGR_TV2_TRANCHE_VALUE_ADMISSION_SHADOW_IMPLEMENTATION_WORKER_RETURN_2026-08-26.md`; material `227f3d950` | accepted implementation plus fresh operator value decision | SATISFIED |
| two bounded comparison sources | accepted EAFR-R11 and MCP-KAR-T2 worker returns | each source exists, is committed, and carries a terminal decision | SATISFIED |
| TV3 value | operator agreed to the terminal two-comparison pass | no owner edit, no external effect, no TV4 | SATISFIED |

## Acceptance Criteria

- exactly two comparisons and no third case;
- each row separates accepted historical outcome, projected TV2 result,
  false-stop risk, false-continue risk, and match/mismatch disposition;
- comparison A is executed through the current pure router with trusted
  authority resolved from the worker's committed execution HEAD;
- comparison B remains documentary because absorption/app/project activation
  is not authorized;
- terminal economics label every cost dimension without inventing savings;
- exactly one recommendation: `CLOSE_ROADMAP_BOUNDED` or
  `PARK_EVIDENCE_COLLECTION`;
- no source, test, schema, standard, template, router, checker, registry,
  roadmap, session, or handoff edit by the worker;
- no provider, network, credential, build, package, public, deploy, or push.

## Verification / Evidence

Run the task-route gate, pre-dispatch autorun bundle, worker-return fast gate,
exact hash recomputation and Git status/staging checks named in the work order.
Only the independent reviewer may convert the worker recommendation to roadmap
closure.

## Stop Conditions

Stop and return `BLOCKED_WITH_REASON` if either accepted source is missing or
hash-drifted, authority cannot resolve from the committed execution HEAD, a
third comparison becomes necessary, or a code/owner edit is required. Unknown
economics cannot be upgraded to observed savings. No TV4 may be proposed.

## Planned Worker Fulfillment Manifest

Exactly one new file:
`docs/reviews/CVF_TPGR_TV3_TERMINAL_TWO_COMPARISON_PILOT_WORKER_RETURN_2026-08-26.md`.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-TV3 --title "Terminal Two-Comparison Pilot And Roadmap Disposition" --date 2026-08-26 --base 4403175d13a6d743441ace2d90ffc4f53c5e4f84 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "TPGR-TV2 accepted at 227f3d950" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic worker dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | terminal comparison scope, exact sources, value envelope and one-file manifest |
| checkerReadAheadConfirmation | dispatch, prompt, read-ahead, structural, trace, route and worker-return checkers read |
| docOnlyNewFields | comparison result table and terminal economics projection only |
| claimBoundary | dispatch provenance only; no runtime or external behavior claim |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Source Verification columns; Dispatch Prompt fields; read-ahead fields; trace labels; baseline structural groups; route manifest keys; worker-return markers and required section names |
| gateRunPurpose | confirm the already-derived packet shape before pre-dispatch, not discover requirements through gate failures |
| claimBoundary | structural conformance does not prove comparison semantics or authorize closure |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| TV3 is capped terminal work | GOVERNANCE_RULE | `docs/roadmaps/CVF_TPGR_TRANCHE_VALUE_ADMISSION_GOVERNANCE_ROADMAP_2026-08-26.md` | Work Plan And Successor Cap | Hard successor cap | TPGR-TV roadmap | ACCEPT |
| TV2 shadow implementation is accepted | REVIEW_EVIDENCE | `docs/reviews/CVF_TPGR_TV2_TRANCHE_VALUE_ADMISSION_SHADOW_IMPLEMENTATION_WORKER_RETURN_2026-08-26.md` | Independent Reviewer Addendum | ACCEPT_WITH_IN_SCOPE_REPAIR | TV2 review | ACCEPT |
| source-backed P1 received one consolidated repair | REVIEW_EVIDENCE | `docs/reviews/CVF_EAFR_R11_FINAL_RECONCILIATION_TRANCHE_VALUE_AND_RFR_DECISION_WORKER_RETURN_2026-08-26.md` | Epistemic Process Block | consolidated successor | EAFR-R11 review | ACCEPT |
| absent consumer stopped absorption candidate | REVIEW_EVIDENCE | `docs/reviews/CVF_MCP_KAR_T2_SCHEMA_CONSUMER_OWNER_VALUE_DECISION_WORKER_RETURN_2026-08-23.md` | Decision / Disposition | STOP_NO_NAMED_CONSUMER | MCP-KAR-T2 review | ACCEPT |
| current decision evaluator is pure and authority-bound | SOURCE_BEHAVIOR | `governance/compat/route_task_governance.py` | evaluate_tranche_value | evaluate_tranche_value | TPGR router | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: 22; not truncated. All IDs are disclosed in the paired work
order; their dispatch impact is exact source evidence, bounded scope, checker
read-ahead, one-file worker ownership, no-commit return and split closure.

Disclosed defectIds: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015,
ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private terminal comparison dispatch; no public artifacts change.

## Claim Boundary

This baseline authorizes one local, comparison-only TV3 worker return. It does
not close the roadmap by itself, activate absorption/project use, modify any
owner, authorize live proof, weaken the risk floor, resume TPGR-R9, or create
TV4.

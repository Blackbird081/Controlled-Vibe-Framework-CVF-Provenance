# CVF GC-018 - KIOD-R7 Dispatch Packet Lifecycle Hygiene

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-07-01

docType: baseline

dispatchBaseHead: b743c085

Batch ID: KIOD-R7

## Purpose

Authorize a bounded governance hardening tranche for stale dispatch-packet
lifecycle hygiene.

The immediate defect class is not a knowledge-source import defect. It is a CVF
process defect: after a governed lane closes, old or draft `DISPATCH_READY`
packets for the same lane can remain in the repo or worktree and look
executable even when active session state, active handoff, and closure evidence
say the lane is already closed or superseded. This creates avoidable overlap,
wrong-role execution, and stale-base confusion for future workers.

This baseline authorizes one worker to implement a conservative checker,
standard, focused tests, and local hook/autorun wiring. It does not authorize
runtime behavior, provider/live proof, public-sync, dashboard/UI work, source
import, package activation, model routing, automatic invocation, or production
readiness claims.

## Scope

Allowed scope: create a CVF-owned dispatch-packet lifecycle hygiene standard,
implement a conservative checker for changed governed dispatch artifacts, add
focused tests, wire the checker into local governance catalogs, and return an
uncommitted worker-return artifact.

Forbidden scope: runtime/provider behavior, live/API proof, source import from
external repositories, public-sync, Web/UI/dashboard changes, MCP/CLI adapter
implementation, generated package index mutation, package lifecycle promotion,
session-state or active-handoff edits by the worker, broad dispatch-quality
refactor, or closure of any KIOD-R6 deferred candidate.

## Baseline Decision

Decision: dispatch KIOD-R7 now because KIOD-R6 closed bounded at material
commit `8b89fc64`, the active handoff records only operator selection as the
next move, and the review of discarded R6 draft packets exposed a repeatable
pre-dispatch hygiene gap.

The tranche is intentionally small: checker plus standard plus tests plus
catalog wiring. The checker must be conservative and changed-range aware. It
must reject only clear stale dispatch-lifecycle contradictions and clear
provider-specific normative role assignment in dispatch artifacts.

## Authority Chain

| Authority | Source path | Verified line/section | Disposition |
| --- | --- | --- | --- |
| Active startup state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | lines 3-5 | ACCEPT |
| Active handoff KIOD-R6 closure | `AGENT_HANDOFF_V30_2026-07-01.md` | lines 52-75, 172-183 | ACCEPT |
| Guard orientation work-order/checker guidance | `docs/reference/guard_orientation/README.md` | lines 79-82, 89, 115 | ACCEPT |
| Dispatch quality checker source | `governance/compat/check_work_order_dispatch_quality.py` | lines 69-84, 202 | ACCEPT |
| Checker read-ahead checker source | `governance/compat/check_governed_artifact_checker_read_ahead.py` | lines 22-36, 153-214 | ACCEPT |
| Agent handoff contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | lines 107-108, 243-249, 292-307 | ACCEPT |
| Tranche commit choreography | `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | lines 58-68, 230-238, 277-281 | ACCEPT |
| Dual-agent accounting | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | lines 30-41, 45-54, 115-123 | ACCEPT |
| Core guard self-protection | `docs/reference/guard_orientation/README.md` | lines 89, 102 | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Current mode is KIOD-R6 accepted pending next lane selection | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | line 3 | `currentMode` | active session bootstrap read model | VALUE_SET | ACCEPT |
| Active handoff is V30 | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | line 4 | `activeHandoff` | active session bootstrap read model | VALUE_SET | ACCEPT |
| KIOD-R6 closed at material commit `8b89fc64` | `AGENT_HANDOFF_V30_2026-07-01.md` | lines 52-75 | `KIOD-R6 Memory Foundation Enrichment Closure` | active handoff | VALUE_SET | ACCEPT |
| Active next move is operator selection after KIOD-R6 closure | `AGENT_HANDOFF_V30_2026-07-01.md` | lines 172-183 | `Next Allowed Move` | active handoff | VALUE_SET | ACCEPT |
| Work-order authoring requires checker read-ahead and source verification | `docs/reference/guard_orientation/README.md` | line 79 | `Work-order authoring / dispatch` | guard orientation index | LITERAL_INVARIANT | ACCEPT |
| Worker execution under `WORKER_MUST_NOT_COMMIT` must leave artifacts uncommitted | `docs/reference/guard_orientation/README.md` | line 80 | `WORKER_MUST_NOT_COMMIT` | guard orientation index | LITERAL_INVARIANT | ACCEPT |
| Guard/checker maintenance needs Core Guard Self-Protection Authorization | `docs/reference/guard_orientation/README.md` | lines 89, 102 | `Core Guard Self-Protection Authorization` | guard orientation index | LITERAL_INVARIANT | ACCEPT |
| Dispatch-quality checker defines required source-verification columns | `governance/compat/check_work_order_dispatch_quality.py` | line 202 | `REQUIRED_SOURCE_COLUMNS` | dispatch quality checker | EXISTS | ACCEPT |
| Checker read-ahead block fields are machine-checked | `governance/compat/check_governed_artifact_checker_read_ahead.py` | lines 22-36 | `REQUIRED_HEADING`; `REQUIRED_FIELDS`; `CHECKER_PATH_RE` | checker read-ahead guard | EXISTS | ACCEPT |
| C4 handoff route needs Reviewer Closure Conversion | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | lines 243-249 | `Reviewer Closure Conversion` | agent handoff contract | LITERAL_INVARIANT | ACCEPT |
| Stale dispatch bases and stale `DISPATCH_READY` residue are known closure defects | `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | lines 58-68, 230-238 | `DISPATCH_READY` | tranche commit choreography standard | LITERAL_INVARIANT | ACCEPT |
| Dual-agent surface matrix must account for internal and external consumers | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | lines 30-41, 45-54 | `INTERNAL_AGENT`; `EXTERNAL_AGENT_CLI_MCP` | dual-agent accounting standard | LITERAL_INVARIANT | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query:
`python governance/compat/run_adif_defect_resolver.py --task-class governance_checker_maintenance --role dispatcher --lifecycle-phase pre-dispatch --json`

Returned defects: NONE_RETURNED

Resolver query: taskClass=`governance_checker_maintenance`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | `## Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `## ADIF Defect Registry Disclosure`; `Resolver query: taskClass=`; `Returned defects: NONE_RETURNED`; `REQUIRED_SOURCE_COLUMNS`; `WORKER_MUST_NOT_COMMIT`; `Core Guard Self-Protection Authorization`; `Dual Agent Surface Matrix` |
| gateRunPurpose | confirmation/evidence only after checker constants and literal tokens were read before writing this baseline |
| claimBoundary | This block proves only read-ahead discipline for this baseline; it does not prove the future KIOD-R7 checker works until worker implementation and tests pass. |

## Negative Search And Collision Discipline

The worker must search for existing dispatch-lifecycle hygiene owner surfaces
before creating the new standard or checker. Minimum searches:

- `rg -n --fixed-strings "dispatch packet lifecycle" docs governance CVF_SESSION`
- `rg -n --fixed-strings "stale DISPATCH_READY" docs governance CVF_SESSION`
- `rg -n --fixed-strings "provider-specific normative role" docs governance CVF_SESSION`
- `rg -n --fixed-strings "WORKER_MUST_NOT_COMMIT" docs/reference governance/compat`
- `rg -n --fixed-strings "Core Guard Self-Protection Authorization" docs/reference governance/compat`

If an existing owner surface already covers the exact behavior, the worker must
enrich that surface instead of creating a duplicate standard and must record the
decision in the worker return.

## Core Guard Self-Protection Authorization

Authorization reason: KIOD-R7 is explicitly a guard-maintenance tranche. The
operator authorized the next roadmap/work-order lane to prevent repeated
dispatch lifecycle defects.

Authorized guard-maintenance scope: create one dispatch lifecycle hygiene
checker, one focused test module, one standard, and local hook/autorun wiring.

Operator authorization: operator asked to write the next work order after
selecting the dispatch lifecycle hygiene roadmap value.

Protected paths authorized for worker mutation:

- `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`
- `governance/compat/test_dispatch_packet_lifecycle_hygiene.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`

Protected paths mentioned but not authorized for worker mutation:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V30_2026-07-01.md`

Authorized non-protected paths:

- `docs/reference/external_agent_review/CVF_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_STANDARD.md`
- `docs/reviews/CVF_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_WORKER_RETURN_2026-07-01.md`

Rollback boundary: revert only KIOD-R7 files and KIOD-R7 catalog entries. Do not
revert KIOD-R6 material commit `8b89fc64`, V30 session sync, or unrelated
governance entries.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | KIOD-R7 checker, standard, tests, and local governance catalogs | may inspect changed governed dispatch artifacts and session/handoff text; no runtime or provider behavior | this GC-018, paired work order, future worker return, focused tests | internal governance checker only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | external worker consuming work order text | may execute the packet as a worker and return uncommitted evidence; no external adapter or MCP behavior is implemented | this GC-018 and paired work order | adapter implementation is out of scope and requires separate GC-018 | DEFERRED_WITH_REASON |

## Proposed Deliverables

| Path | Purpose | Disposition |
| --- | --- | --- |
| `docs/reference/external_agent_review/CVF_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_STANDARD.md` | canonical doc for stale dispatch packet lifecycle hygiene | CREATE |
| `governance/compat/check_dispatch_packet_lifecycle_hygiene.py` | changed-range checker for stale dispatch lifecycle contradictions and provider-specific normative role assignment | CREATE |
| `governance/compat/test_dispatch_packet_lifecycle_hygiene.py` | focused checker tests with stale KIOD-style dispatch fixtures | CREATE |
| `governance/compat/agent_autorun_command_catalog.py` | autorun catalog wiring | EDIT |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | pre-commit hook catalog wiring | EDIT |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | pre-push hook catalog wiring | EDIT |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | reviewer-fast hook catalog wiring | EDIT |
| `docs/reviews/CVF_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_WORKER_RETURN_2026-07-01.md` | worker return with implementation evidence | CREATE |

## Acceptance Criteria

- The checker is changed-range aware and has `--base`, `--head`, and `--enforce`
  behavior consistent with existing `governance/compat/check_*.py` patterns.
- The checker blocks changed dispatch-ready governed artifacts when they cite a
  root-level active handoff that is no longer active.
- The checker blocks changed dispatch-ready governed artifacts when the same
  lane key is clearly recorded as closed in active session/handoff/front-door
  sources.
- The checker blocks clear provider-specific normative worker assignment in
  dispatch artifacts while allowing provider names in evidence/history text
  outside normative role assignment surfaces.
- The checker does not scan or fail unchanged historical artifacts.
- The worker return records negative-search evidence, checker read-ahead,
  source verification, tests, `git status --short`, and claim boundary.

## Review Gate

Reviewer must reject the worker return if the worker:

- commits changes;
- changes session state or active handoff;
- implements runtime/provider behavior or public-sync;
- broadens the checker to fail unrelated historical artifacts;
- omits focused tests for stale handoff, closed-lane stale dispatch, and
  provider-specific normative role assignment;
- omits Core Guard Self-Protection Authorization coverage for protected files;
- claims production behavior, external adapter support, or live governance
  proof.

## Closure Boundary

Closure is reviewer-owned. This baseline remains a dispatch authority packet
until a reviewer accepts the worker return, commits material changes, and then
updates session-sync surfaces separately if current mode or next allowed move
changes.

## Evidence Requirements

Dispatcher evidence before execution:

- checker read-ahead gate: PASS
- ADIF disclosure gate: PASS
- markdown structural gate: PASS after this section is present
- dispatch-quality gate: PASS after paired work order literal terms are present
- pre-dispatch autorun: required before claiming dispatch complete

Worker evidence after execution is defined in the paired work order and must be
recorded in the worker return.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| GC-018 status | `docs/baselines/CVF_GC018_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_2026-07-01.md` | `Status: CLOSED_PASS_BOUNDED` after reviewer acceptance | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_2026-07-01.md` | `Status: CLOSED_PASS_BOUNDED` after reviewer acceptance | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_COMPLETION_2026-07-01.md` | reviewer closure artifact records acceptance and gate evidence | PASS |
| Worker return | `docs/reviews/CVF_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_WORKER_RETURN_2026-07-01.md` | `Status: COMPLETE_PENDING_REVIEW`; accepted by reviewer/closer | PASS |
| Roadmap state | N/A with reason | no dedicated KIOD-R7 roadmap file is changed by this closure; lane selected directly after KIOD-R6 closure | N/A with reason |
| Registry JSON | N/A with reason | no corpus, scan, package, or generated registry JSON is changed by KIOD-R7 | BLOCKED with reason: not applicable to this non-corpus governance checker closure |
| Registry Markdown | N/A with reason | no corpus or scan registry Markdown is changed by KIOD-R7 | BLOCKED with reason: not applicable to this non-corpus governance checker closure |
| External evidence digest | N/A with reason | KIOD-R7 consumes no external source repository and produces no external evidence digest | N/A with reason |
| System loop interlock | N/A with reason | no system loop interlock registry is changed by KIOD-R7 | N/A with reason |
| Public export | N/A with reason | KIOD-R7 is private provenance governance hardening; public-sync requires separate authorization | N/A with reason |
| Runtime/provider proof | N/A with reason | no runtime/provider/live governance behavior is claimed by this tranche | N/A with reason |
| Session continuity | active session surfaces | reviewer/closer updates after material commit in separate session-sync batch | PASS |

## Claim Boundary

KIOD-R7 is closed as a bounded governance checker tranche after reviewer
acceptance. It does not authorize runtime/provider/public/Web/package behavior.

Public Export Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening only; no public-sync batch is
authorized by KIOD-R7.

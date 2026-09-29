# CVF GC-018 Baseline - DARA T2B Operator-Authorized Internal Recovery

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-09-07

Batch ID: DARA-T2B-OPERATOR-AUTHORIZED-INTERNAL-RECOVERY

Dispatch base head: 0ba931bb1073afef3b4e5c376fc9161548c759b0

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator; dispatch author: orchestrator; worker target: internal agent; reviewer/closer: reviewer/closer role.

providerExecutionAuthority: FORBIDDEN

## Purpose

Open one fail-closed internal recovery assignment for the rejected DARA-T2
candidate. The assignment repairs the complete committed R3 finding set inside
the existing exact 14-path implementation manifest, preserves the predecessor
review and cost history, and creates no third external invocation.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id DARA-T2B-OPERATOR-AUTHORIZED-INTERNAL-RECOVERY --title "DARA T2B Operator-Authorized Internal Recovery" --date 2026-09-07 --base 0ba931bb1073afef3b4e5c376fc9161548c759b0 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --cumulative-external-invocation-count 2 --external-invocation-ceiling 2 --stdout` |
| generatedProfile | protected-governance-path plus no-commit internal-worker profile |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | authored from the committed template and accepted DARA packet because the current helper working tree is part of the rejected candidate under recovery |
| checkerReadAheadConfirmation | dispatch, convergence, source, protected-path, handoff, return, trace, size, and public guards |
| docOnlyNewFields | recovery route, transport boundary, predecessor telemetry, and exact internal-only stop rule |
| claimBoundary | scaffold provenance only; no implementation, surface reclassification, or acceptance claim |

## Decision / Baseline / Proposed Tranche

Recovery route: `OPERATOR_AUTHORIZED_INTERNAL_RECOVERY`

Transport disposition: `OPERATOR_MANUAL_COPY_PASTE`

Dispatch surface: `INTERNAL_AGENT`

Predecessor review round: 3

Predecessor external invocation count: 2

Predecessor external invocation ceiling: 2

Operator-reported elapsed time: 200 minutes

Token or subscription-quota usage: `NOT_AVAILABLE_WITH_REASON: operator did not measure exact quota usage`

The committed final review at `ceadf2c3ff8d5e42d37d974a5ba8c1413b617ccb`
proves two new critical fail-open root causes and three dependent evidence
manifestations. The operator authorized this internal recovery route on
2026-09-07, kept the current agent in the orchestrator/reviewer role,
prohibited it from using an external-worker CLI, and retained manual
worker-packet relay.

This is a new parent assignment created from new independent critical evidence.
It is not an automatic DARA rework round 3 and does not erase or reset the
predecessor telemetry.

## Consumer And Transport Boundary

Manual copy/paste is only a transport method. The recipient must stop with
`BLOCKED_SURFACE_MISMATCH` before editing if execution crosses an independent
provider, account, credential, process, durable-action, or external authority
boundary. This baseline does not classify a manually contacted external model
as an internal agent and does not raise the external ceiling above 2/2.

## Authorized Scope

- Repair DARA-T2-R3-01, DARA-T2-R3-02, and DARA-T2-R3-03 as one dependency
  closure.
- Reuse one immutable semantic-review identity validator for the required
  architecture matrix and accepted-design echo branches.
- Resolve each declared trust locator against the cited authority bytes.
- Constrain every rollback path to the work order's exact writable manifest.
- Apply private/archive authority rejection to trust, canonical-owner, and
  canonical-authority path classes.
- Add discoverable negative tests for every repaired predicate and update the
  existing worker return with only real test identities and truthful results.

## Forbidden Scope

No new implementation path, new worker-return file, exception-registry change,
MFRP collector/readout/receipt change, roadmap edit by the worker, ADIF edit,
session or handoff edit, WP-ARCH-003 edit, runtime/provider/live call,
credential access, public sync, deployment, commit, push, DARA-T3 opening, or
automatic successor is authorized.

## Dependency Release Evidence

| Dependency | Evidence | Release rule | Disposition |
|---|---|---|---|
| final DARA-T2 rejection | `docs/reviews/CVF_DARA_T2_R2_FINAL_IMPLEMENTATION_COMPLETION_REVIEW_2026-09-07.md`; commit `ceadf2c3ff8d5e42d37d974a5ba8c1413b617ccb`; SHA-256 `c879896888a1595b1b1850d21f0aa09a9eecd8b6924f1085e3df487bd792fa6e` | complete finding set and escalation boundary are immutable | ACCEPT |
| accepted root contract | `docs/assessments/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_2026-09-07.md`; commit `203e9e6f7bc63873da008284688f7b533f65fbf9` | R1-02/R1-03 semantics remain controlling | ACCEPT |
| R2 scope amendment | `docs/assessments/CVF_DARA_T2_R2_ROOT_CONTRACT_COMPLETION_AMENDMENT_2026-09-07.md`; commit `f0c5dc61d2300eec36dcfc499aed2ca6e0d4363a` | exact 14-path manifest and base-debt rule remain controlling | ACCEPT |
| operator recovery authority | operator instruction dated 2026-09-07, recorded in this baseline and DARA roadmap | internal-only recovery route; no external ceiling increase | ACCEPT |
| MFRP P4-C1 | `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION_2026-09-02.md`; activation `b9bdba712` | reviewer consumes returned evidence and avoids duplicate reruns | ACCEPT |

## Exact Worker Changed-Set Manifest

1. `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
2. `docs/reference/CVF_ARCHITECTURE_READINESS_ADMISSION_STANDARD_2026-09-07.md`
3. `governance/compat/build_dispatch_packet_scaffold.py`
4. `governance/compat/build_dispatch_packet_architecture_readiness.py`
5. `governance/compat/build_worker_return_skeleton_scaffold.py`
6. `governance/compat/check_work_order_dispatch_quality.py`
7. `governance/compat/check_work_order_dispatch_quality_range.py`
8. `governance/compat/check_work_order_dispatch_quality_source.py`
9. `governance/compat/run_worker_return_scaffold.py`
10. `governance/compat/test_build_dispatch_packet_scaffold.py`
11. `governance/compat/test_check_work_order_dispatch_quality_architecture_readiness.py`
12. `governance/compat/test_run_worker_return_scaffold.py`
13. `governance/compat/check_work_order_dispatch_quality_architecture_schema.py`
14. `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_WORKER_RETURN_2026-09-06.md`

The cleanup-only path `governance/compat/test_check_work_order_dispatch_quality.py`
must remain byte-identical to the worker execution base and absent from the
final diff.

## Acceptance Matrix

| ID | Required outcome |
|---|---|
| IR-01 | accepted-design echo uses the same immutable commit, ancestor, committed-path, committed-byte SHA, digest, and criterion validation as the required architecture route |
| IR-02 | fabricated commit, non-ancestor commit, wrong review path, wrong file SHA, arbitrary digest, and missing criterion each fail closed in the echo route |
| IR-03 | each trust locator must resolve in normalized cited authority bytes; nonresolving locator fails closed |
| IR-04 | each rollback path must be repo-relative and contained in the exact worker writable manifest; `AGENTS.md` fails closed |
| IR-05 | private, archive, and legacy-private paths fail closed when used as trust source, canonical owner, or canonical authority |
| IR-06 | tests use discoverable real symbols and cover every negative case in IR-02 through IR-05 |
| IR-07 | the worker return removes nonexistent test names and maps each PASS claim to an actual test identity and command result |
| IR-08 | focused tests, both scaffold routes, size guards, worker-return fast gate, and pre-implementation gate pass after the last material edit |
| IR-09 | final worker diff equals the exact 14 paths; cleanup-only path is absent; parked WP hashes remain unchanged |
| IR-10 | worker makes zero external/provider/live calls, zero commits, and opens no successor tranche |

## Reviewer Non-Duplication Boundary

The reviewer consumes the returned command results and exact manifest. A
focused rerun is allowed only for a named contradiction, with the claim,
expected information gain, and cost reason recorded. No per-row review or
broad duplicate suite is admitted. One terminal review decides acceptance or
returns `BLOCK_INTERNAL_RECOVERY_EVIDENCE` without creating another automatic
repair loop.

## Verification And Evidence Plan

Before worker relay, run the pre-dispatch gate against the staged dispatch
artifacts. At worker handoff, require exact manifest reconciliation, focused
tests after the final edit, both size guards, the worker-return fast gate,
automation assist, pre-implementation, `git diff --check`, empty staging, and
before/after parked-file hashes. These checks prove bounded packet and local
candidate evidence only; the reviewer retains semantic acceptance authority.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024,
ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json` |
| Returned defect count | 22 |
| Disclosed defectIds | all IDs listed above |
| Dispatch impact | preserve source identity, route truth, protected-path authority, exact manifest, real test names, pending-return freshness, and commit separation |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_python_automation_size.py` |
| literalTokensReviewed | dispatch status, INITIAL convergence values, internal surface values, protected paths, source table columns, pending return, trace labels, public disposition |
| gateRunPurpose | confirm this bounded internal-recovery authorization after the complete finding set and path manifest were frozen; not first discovery |
| claimBoundary | structural conformance does not prove implementation correctness or reclassify an external recipient as internal |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| complete R3 finding set | committed review evidence | `docs/reviews/CVF_DARA_T2_R2_FINAL_IMPLEMENTATION_COMPLETION_REVIEW_2026-09-07.md` | Findings / Position | DARA-T2-R3-01 through DARA-T2-R3-03 | DARA reviewer | ACCEPT |
| internal/external consumer boundary | active standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule | INTERNAL_AGENT | dual-agent accounting | ACCEPT |
| round-three escalation and successor authority | active standard | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | Round-Three Escalation Rule; Same-Scope Authority Continuity | REVIEW_COST_ESCALATION_REQUIRED | Review Cost | ACCEPT |
| reviewer evidence-reuse boundary | active standard | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | Universal Discovery And Active Measurement Binding | reviewerWorkBoundary | Review Cost and MFRP | ACCEPT |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: repair only the DARA candidate on the
protected implementation and test paths in the exact worker manifest.

Protected paths:

- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/build_dispatch_packet_architecture_readiness.py`
- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/check_work_order_dispatch_quality_range.py`
- `governance/compat/check_work_order_dispatch_quality_source.py`
- `governance/compat/run_worker_return_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `governance/compat/test_check_work_order_dispatch_quality_architecture_readiness.py`
- `governance/compat/test_run_worker_return_scaffold.py`
- `governance/compat/check_work_order_dispatch_quality_architecture_schema.py`

Operator authorization: on 2026-09-07 the operator explicitly opened
`OPERATOR_AUTHORIZED_INTERNAL_RECOVERY`, prohibited orchestrator use of an
external-worker CLI, retained the current agent as orchestrator/reviewer, and reserved manual worker
packet relay to the operator.

Rollback boundary: revert only the DARA-T2B worker edits if rejected. Preserve
all committed DARA design, amendments, reviews, P4-C1 evidence, continuity, and
the two parked WP-ARCH-003 files.

Not authorized: external invocation 3, new path, exception increase, MFRP or
session mutation, runtime/provider/live/public action, worker commit, or push.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact local DARA 14-path candidate under this baseline and paired work order | no commit, no external effect, exact protected-path authorization | committed R3 review plus targeted tests and pending worker return | internal repository editing only; manual prompt relay does not widen authority | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no worker execution authorized in DARA-T2B | predecessor ceiling remains 2/2; any independent provider/account boundary blocks | DARA final review and this explicit exclusion | no CLI/MCP/adapter/provider call; no transport-based reclassification | N/A_WITH_REASON |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator/reviewer |
| Provider or surface | local private CVF workspace |
| Session or invocation | DARA-T2B internal-recovery baseline authoring, 2026-09-07 |
| Working directory | repository root |
| Command or tool surface | governed reads, ADIF resolver, `rg`, `apply_patch`, local gates, git |
| Target paths | this baseline, paired work order, DARA roadmap |
| Allowed scope source | operator instruction dated 2026-09-07 |
| Before status evidence | HEAD `0ba931bb1073afef3b4e5c376fc9161548c759b0`; DARA candidate remains 14 uncommitted paths; two parked WP files remain excluded |
| After status evidence | recovery authorization artifacts only; worker candidate not edited by orchestrator |
| Diff evidence | `git diff --name-status`; `git status --short --untracked-files=all` |
| Approval boundary | internal recovery dispatch authoring and later independent review only |
| Claim boundary | no worker repair, provider/live call, external ceiling increase, acceptance, or production claim |
| Agent type | orchestrator/reviewer |
| Invocation ID | `dara-t2b-operator-authorized-internal-recovery-dispatch-2026-09-07` |
| Expected manifest | DARA roadmap, this baseline, paired work order |
| Actual changed set | same three orchestrator-owned paths; pre-existing worker and WP paths remain unstaged |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private recovery authorization; no public-sync authority.

## Claim Boundary

This baseline authorizes one internal, no-commit recovery assignment. It does
not repair or accept DARA-T2, change the external count or ceiling, authorize a
manual external-model call, resume WP-ARCH-003, open DARA-T3, modify runtime,
invoke a provider, publish, deploy, or claim production readiness.

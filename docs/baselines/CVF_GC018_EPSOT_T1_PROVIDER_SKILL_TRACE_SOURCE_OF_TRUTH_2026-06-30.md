# CVF GC-018 EPSOT-T1 Provider Skill Trace Source Of Truth

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: gc018_baseline

baseHead: `09a753ea`

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | add a bounded CVF source-of-truth trace guard for provider-owned external skill consumption claims |
| Baseline | AGSK-R7 closed with runtime package work separate from provider-owned skill runtime control |
| Proposed tranche | EPSOT-T1 standard, checker, tests, and catalog wiring |
| Execution route | Codex direct implementation with reviewer-owned commit |
| Closure posture | CLOSED_PASS_BOUNDED after focused tests and governance gates |

## Purpose

Authorize a bounded CVF source-of-truth trace guard for provider-owned external
skill surfaces. The tranche records the authority boundary, adds a machine
checker, wires it into local governance catalogs, and closes with focused test
evidence.

## Scope / Methodology

Allowed scope:

- Add the external provider skill source-of-truth standard.
- Add a forward-only changed-Markdown checker and focused regression tests.
- Wire the checker into reviewer-fast, pre-commit, and autorun command
  catalogs.
- Add matching work order and completion review records.

Forbidden scope:

- No provider runtime interception.
- No CLI/MCP adapter implementation.
- No package activation or ACTIVE resolver change.
- No public-sync.
- No live provider proof claim.

## ADIF Defect Registry Disclosure

Resolver command:

`python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase implementation --surface-selector governance/compat --risk-ceiling HIGH --max-results 20`

Returned defects: NONE_RETURNED

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: EPSOT-T1 checker, tests, catalog wiring,
standard, work order, baseline, and completion review only.

Protected paths:

- `governance/compat/check_external_provider_skill_usage_trace.py`
- `governance/compat/test_check_external_provider_skill_usage_trace.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/agent_autorun_command_catalog.py`

Operator authorization: the operator approved building a source-of-truth
mechanism so provider-owned external skill surfaces leave traceable evidence
when their output is consumed in CVF.

Rollback boundary: revert only EPSOT-T1 material and later session-sync records;
do not revert AGSK-R7 package-promotion material or unrelated runtime package
state.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Reviewer-fast catalog is a list of named local checks | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | `REVIEWER_FAST_CHECKS` declaration | `REVIEWER_FAST_CHECKS` | local governance hook catalog | EXISTS | ACCEPT |
| Pre-commit catalog is a list of named local checks | `governance/compat/local_governance_hook_catalog_pre_commit.py` | `PRE_COMMIT_CHECKS` declaration | `PRE_COMMIT_CHECKS` | local governance hook catalog | EXISTS | ACCEPT |
| Autorun catalog supports ranged checker commands | `governance/compat/agent_autorun_command_catalog.py` | `_range_command` and `_common_commands` | `_range_command` | agent autorun command catalog | EXISTS | ACCEPT |
| Existing changed-Markdown checker pattern uses applicable prefixes | `governance/compat/check_memory_access_claim.py` | `APPLICABLE_PREFIXES` | `APPLICABLE_PREFIXES` | memory access claim checker | EXISTS | ACCEPT |
| Existing changed-Markdown checker pattern supports ranged CLI flags | `governance/compat/check_memory_access_claim.py` | argument parser flags | `--base`, `--head`, `--enforce` | memory access claim checker CLI | EXISTS | ACCEPT |
| Provider skill trace table is new policy vocabulary | `docs/reference/CVF_EXTERNAL_PROVIDER_SKILL_SOURCE_OF_TRUTH_STANDARD_2026-06-30.md` | Required External Provider Skill Usage Trace | `External Provider Skill Usage Trace` | EPSOT-T1 standard | DOC_ONLY_NEW | ACCEPT |

## Evidence / Verification

| Evidence | Required or observed result |
|---|---|
| Checker compile | `python -m py_compile governance/compat/check_external_provider_skill_usage_trace.py` PASS |
| Focused regression | `python -m unittest governance.compat.test_check_external_provider_skill_usage_trace` PASS |
| Trace guard | committed-range rerun required before material closure |
| Reviewer-fast | rerun required after artifact repairs |
| Live proof | NOT_RUN_WITH_REASON: no provider or live governance behavior is claimed |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | governance hook catalogs and analogous changed-Markdown checker |
| Runtime behavior claimed | N/A_WITH_REASON: no runtime behavior is claimed |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - source supports static trace guard wiring only |

## New Doc-Only Fields

| Field | Owner | Disposition |
|---|---|---|
| `Usage disposition` | EPSOT-T1 standard | DOC_ONLY_NEW |
| `Provider skill name` | EPSOT-T1 standard | DOC_ONLY_NEW |
| `Provider owner` | EPSOT-T1 standard | DOC_ONLY_NEW |
| `Invocation context` | EPSOT-T1 standard | DOC_ONLY_NEW |
| `Output consumed by CVF` | EPSOT-T1 standard | DOC_ONLY_NEW |
| `CVF source-of-truth promotion path` | EPSOT-T1 standard | DOC_ONLY_NEW |
| `Evidence artifact` | EPSOT-T1 standard | DOC_ONLY_NEW |
| `Authority boundary` | EPSOT-T1 standard | DOC_ONLY_NEW |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no provider-owned skill surface was consumed for this baseline |
| Provider owner | N/A with reason: no provider-owned skill surface was consumed for this baseline |
| Invocation context | N/A with reason: local repository authoring only |
| Output consumed by CVF | N/A with reason: no provider-owned skill output was consumed |
| CVF source-of-truth promotion path | N/A with reason: this baseline is governed source evidence |
| Evidence artifact | `docs/baselines/CVF_GC018_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md` |
| Authority boundary | no provider output; provider output would be not CVF canonical authority |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | EPSOT-T1 baseline authoring, 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | repository reads, apply_patch, local checker/test authoring |
| Target paths | EPSOT-T1 baseline, work order, completion review, standard, checker, test, and catalogs |
| Allowed scope source | operator request and this GC-018 baseline |
| Before status evidence | base `09a753ea` |
| After status evidence | EPSOT-T1 material staged for closure gates |
| Diff evidence | `git diff --name-status` before closure |
| Approval boundary | bounded trace guard only |
| Claim boundary | no provider runtime, adapter, live, public, activation, or package-promotion claim |
| Agent type | Codex |
| Invocation ID | `epsot-t1-gc018-2026-06-30` |
| Expected manifest | `docs/reference/CVF_EXTERNAL_PROVIDER_SKILL_SOURCE_OF_TRUTH_STANDARD_2026-06-30.md`; `docs/baselines/CVF_GC018_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md`; `docs/reviews/CVF_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_COMPLETION_2026-06-30.md`; `governance/compat/check_external_provider_skill_usage_trace.py`; `governance/compat/test_check_external_provider_skill_usage_trace.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/agent_autorun_command_catalog.py` |
| Actual changed set | `docs/reference/CVF_EXTERNAL_PROVIDER_SKILL_SOURCE_OF_TRUTH_STANDARD_2026-06-30.md`; `docs/baselines/CVF_GC018_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md`; `docs/reviews/CVF_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_COMPLETION_2026-06-30.md`; `governance/compat/check_external_provider_skill_usage_trace.py`; `governance/compat/test_check_external_provider_skill_usage_trace.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/agent_autorun_command_catalog.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: operator-directed governance guard tranche, not a roadmap status edit | N/A with reason | PASS |
| Registry JSON | N/A with reason: no registry JSON mutation | N/A with reason | PASS |
| Registry Markdown | N/A with reason: no registry Markdown mutation | N/A with reason | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no runtime loop or system-loop mutation | N/A with reason | PASS |
| Session continuity | N/A with reason: material baseline does not update session state; session-sync follows material commit | N/A with reason | PASS |
| Focused tests | checker compile and unittest | PASS before final gate sweep | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening; no public-sync authorization.

## Claim Boundary

EPSOT-T1 authorizes static trace enforcement in CVF governed artifacts only. It
does not authorize provider-side audit access, external runtime interception,
adapter implementation, active resolver behavior, package activation, web UI,
public-sync, push, or live governance proof.

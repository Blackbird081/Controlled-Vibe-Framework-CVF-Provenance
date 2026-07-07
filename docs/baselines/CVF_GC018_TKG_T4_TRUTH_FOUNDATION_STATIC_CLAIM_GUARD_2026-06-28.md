# CVF GC-018 TKG-T4 Truth Foundation Static Claim Guard

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018_baseline

Date: 2026-06-28

Owner: Codex

rawMemoryReleased: false

## Purpose

Implement the bounded static truth-foundation claim guard selected by TKG-T3.

Decision: `IMPLEMENT_TKG_T4_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD`.

## Decision / Baseline / Proposed Tranche

Decision: `IMPLEMENT_TKG_T4_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD`.

Baseline: TKG-T3 selected a bounded local static checker and deferred
repo-wide provenance-label enforcement.

Proposed next tranche: `TKG-T5 Remaining Value Audit And Lane Closeout`.

## Scope / Target / Owner Boundary

Allowed material scope:

- add `governance/compat/check_truth_foundation_claim_guard.py`;
- add focused unit coverage for the checker;
- wire the checker into autorun, reviewer-fast, pre-commit, and pre-push
  command catalogs;
- file this GC-018 baseline and matching completion review.

Forbidden material scope:

- no runtime/provider/live behavior;
- no MCP gateway, hypervisor, CLI adapter, package activation, certification,
  generated aggregate, public-sync export, evidence database, obligation
  registry, or MPI-T6 runtime;
- no direct import of upstream AGT or Truth Kernel package code;
- no repo-wide provenance-label enforcement.

## Source Authority

| Source | Path | Role |
|---|---|---|
| TKG-T1 contract | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | truth foundation doctrine |
| TKG-T2 matrix | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_OWNER_SURFACE_RECONCILIATION_MATRIX.md` | owner-surface reconciliation |
| TKG-T3 roadmap | `docs/roadmaps/CVF_TKG_T3_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD_PLAN_ROADMAP_2026-06-28.md` | checker envelope and boundaries |
| Memory claim checker | `governance/compat/check_memory_access_claim.py` | changed-path checker pattern |
| Autorun catalog | `governance/compat/agent_autorun_command_catalog.py` | workflow gate wiring |
| Local hook catalogs | `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py` | local hook wiring |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| TKG-T3 selected T4 checker implementation | `docs/roadmaps/CVF_TKG_T3_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD_PLAN_ROADMAP_2026-06-28.md` | Decision; T4 Checker Envelope | `TKG_T4_STATIC_TRUTH_FOUNDATION_CLAIM_GUARD_IMPLEMENTATION` | TKG-T3 roadmap | VALUE_SET | ACCEPT |
| TKG-T1 supplies integrity, LLM, external-input, and provenance doctrine | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | Integrity Is Not Truth; LLM Output Is Not Self-Trusting; Source Authority Rule | `cvf.truthFoundation.sourceProvenanceVerification.tkgT1.v1` | truth foundation contract | VALUE_SET | ACCEPT |
| TKG-T2 selects claim-language guard as higher value than runtime/package import | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_OWNER_SURFACE_RECONCILIATION_MATRIX.md` | T2 Decision; Gap And Candidate Matrix | `RECOMMEND_TKG_T3_PLAN` | TKG-T2 reconciliation matrix | VALUE_SET | ACCEPT |
| Memory claim checker provides reusable changed-path static checker structure | `governance/compat/check_memory_access_claim.py` | `_get_changed_name_status`; `_get_worktree_name_status`; `_classify`; `main` | `_classify` | memory access claim checker | RUNTIME_BEHAVIOR | ACCEPT |
| Autorun catalog owns range command binding | `governance/compat/agent_autorun_command_catalog.py` | `_range_command`; `_common_commands` | `_common_commands` | agent autorun command catalog | RUNTIME_BEHAVIOR | ACCEPT |
| Reviewer-fast hook catalog owns reviewer-fast local command list | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | `REVIEWER_FAST_CHECKS` | `REVIEWER_FAST_CHECKS` | reviewer-fast hook catalog | VALUE_SET | ACCEPT |
| Pre-commit hook catalog owns pre-commit local command list | `governance/compat/local_governance_hook_catalog_pre_commit.py` | `PRE_COMMIT_CHECKS` | `PRE_COMMIT_CHECKS` | pre-commit hook catalog | VALUE_SET | ACCEPT |
| Pre-push hook catalog owns pre-push local command list | `governance/compat/local_governance_hook_catalog_pre_push.py` | `PRE_PUSH_CHECKS` | `PRE_PUSH_CHECKS` | pre-push hook catalog | VALUE_SET | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0006

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add and wire one bounded static
truth-foundation claim guard plus focused tests.

Protected paths:

- `governance/compat/check_truth_foundation_claim_guard.py`
- `governance/compat/test_check_truth_foundation_claim_guard.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`

Operator authorization: the operator instructed Codex to continue through the
remaining TKG roadmap after TKG-T3 selected this checker.

Rollback boundary: if TKG-T4 is rejected, revert only this checker, tests,
catalog wiring, TKG-T4 baseline, and TKG-T4 completion review. Do not revert
TKG-T3 material commit `5ee0765c`, TKG-T3 handoff sync commit `230b923b`, or
earlier TKG/FPC/PRG/EverOS commits.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | TKG-T1 contract, TKG-T2 matrix, TKG-T3 roadmap, memory checker pattern, autorun catalog, local hook catalogs |
| Runtime behavior claimed | N/A_WITH_REASON: checker validates local governed Markdown only |
| Live/provider proof claimed | N/A_WITH_REASON: no live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized or performed |
| Freshness disposition | PASS - current source evidence supports static checker implementation only |

## Acceptance Criteria

| ID | Criterion | Disposition |
|---|---|---|
| AC1 | checker detects bounded integrity-boundary overclaim language | PASS |
| AC2 | checker detects bounded LLM/reviewer verification overclaim language | PASS |
| AC3 | checker detects bounded external-input authority overclaim language | PASS |
| AC4 | checker ignores marked discussion-only planning sections | PASS |
| AC5 | focused tests cover positive, negative, CLI, JSON, archive, and read-only cases | PASS |
| AC6 | checker is wired into autorun, reviewer-fast, pre-commit, and pre-push catalogs | PASS |
| AC7 | runtime/provider/public/package/MCP behavior remains out of scope | PASS |

## Evidence / Verification

| Evidence item | Command or artifact | Required result |
|---|---|---|
| focused unit tests | `python -m unittest governance.compat.test_check_truth_foundation_claim_guard` | PASS |
| checker over current T4 range | `python governance/compat/check_truth_foundation_claim_guard.py --base 230b923b --head HEAD --enforce` | PASS |
| autorun gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 230b923b --head HEAD` | PASS before commit |
| commit steward | `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 230b923b --head HEAD --enforce` | PASS before commit |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | External repo or copied folder -> Root/folder lifecycle classification plus absorption map when retained -> CVF-owned reference contract -> ABSORB, ADAPT, DEFER, REJECT, or BLOCK |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline |
| Disposition | ADAPT TKG-T3 checker plan into local static checker implementation |
| Claim boundary | external sources remain inputs; TKG-T4 creates no runtime, provider/live, public-sync, adapter, package, MCP, or Truth Kernel package behavior |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | TKG-T4 local static truth-foundation claim guard |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime receipt or execution-control behavior is claimed |
| actionEvidence | ACTION_EVIDENCE_PRESENT - checker, tests, catalog wiring, and governance gate evidence |
| invocationBoundary | local governed checker and documentation authoring |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, adapter, or package interception claim |
| claimLanguage | local static Markdown checker only |
| forbiddenExpansion | no runtime, provider/live proof, public-sync, adapter, package activation, certification, MCP gateway, hypervisor, evidence database, obligation registry, generated aggregate, or MPI-T6 runtime |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local workspace |
| Session or invocation | `tkg-t4-truth-foundation-static-claim-guard-2026-06-28` |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, Get-Content, apply_patch, unittest, governance gates |
| Target paths | TKG-T4 checker, tests, command catalogs, this baseline, and completion review |
| Allowed scope source | TKG-T3 roadmap and operator instruction to continue through the roadmap |
| Before status evidence | baseHead `230b923b`; worktree clean before T4 patch |
| After status evidence | checker, tests, wiring, baseline, and completion review added |
| Diff evidence | `git diff --name-status 230b923b..HEAD` |
| Approval boundary | local static checker and hook/catalog wiring only |
| Claim boundary | no runtime, provider/live, public-sync, generated aggregate, adapter, package activation, certification, MCP gateway, hypervisor, circuit breaker, evidence database, obligation registry runtime, SOT index runtime, verifier service, or Truth Kernel package import |
| Agent type | single-agent dispatcher/implementer/reviewer/closer |
| Invocation ID | `tkg-t4-static-claim-guard-2026-06-28` |
| Expected manifest | `docs/baselines/CVF_GC018_TKG_T4_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD_2026-06-28.md`; `docs/reviews/CVF_TKG_T4_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD_COMPLETION_2026-06-28.md`; `governance/compat/check_truth_foundation_claim_guard.py`; `governance/compat/test_check_truth_foundation_claim_guard.py`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py` |
| Actual changed set | `docs/baselines/CVF_GC018_TKG_T4_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD_2026-06-28.md`; `docs/reviews/CVF_TKG_T4_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD_COMPLETION_2026-06-28.md`; `governance/compat/check_truth_foundation_claim_guard.py`; `governance/compat/test_check_truth_foundation_claim_guard.py`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this tranche |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_TKG_T3_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD_PLAN_ROADMAP_2026-06-28.md` | TKG-T4 row selected | PASS |
| Work order status | N/A with reason: direct single-agent checker tranche | N/A with reason | N/A with reason |
| Completion or reviewer artifact | `docs/reviews/CVF_TKG_T4_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD_COMPLETION_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Checker implementation | `governance/compat/check_truth_foundation_claim_guard.py` | focused command PASS | PASS |
| Checker tests | `governance/compat/test_check_truth_foundation_claim_guard.py` | focused unittest PASS | PASS |
| Gate wiring | command catalogs | autorun, reviewer-fast, pre-commit, and pre-push entries present | PASS |
| Registry JSON | BLOCKED with reason: no registry JSON mutation is authorized | no registry path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown mutation is authorized | no registry path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: TKG-T4 consumes CVF-owned TKG-T1 through TKG-T3 surfaces | no new external digest imported | N/A with reason |
| System loop interlock | N/A with reason: no runtime loop/interlock surface changed | Claim Boundary | N/A with reason |
| Public sync | N/A with reason: no public-sync is authorized | no public paths changed | N/A with reason |
| Runtime/live proof | N/A with reason: no runtime/provider governance behavior is claimed | no live run required | N/A with reason |
| Session continuity | active handoff marker planned after material commit | separate handoff-sync commit required | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| TKG-T4-Q1 | checker command | N/A with reason: command output | checker passes over T4 range | PASS after remediation | PASS |
| TKG-T4-Q2 | focused tests | N/A with reason: unittest output | tests pass | PASS after remediation | PASS |
| TKG-T4-Q3 | command catalogs | N/A with reason: source diff | four catalog entries present | present | PASS |
| TKG-T4-Q4 | Claim Boundary | N/A with reason: Markdown section | no runtime/provider/public/package behavior claimed | boundary section present | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance local governance checker. Public export requires a
separate public-sync decision.

## Claim Boundary

TKG-T4 implements and wires a local static Markdown checker only. It does not
authorize or claim AGT runtime governance, Truth Kernel runtime, MCP gateway
interception, hypervisor execution rings, circuit breakers, evidence database,
obligation registry runtime, SOT index runtime, independent verifier service,
provider/live proof, public-sync export, CLI/MCP adapter, package activation,
certification, generated aggregate, or production/hosted readiness.

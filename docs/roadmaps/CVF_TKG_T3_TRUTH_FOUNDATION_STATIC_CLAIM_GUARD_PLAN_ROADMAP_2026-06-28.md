# CVF TKG-T3 Truth Foundation Static Claim Guard Plan Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-28

Batch ID: TKG-T3

External knowledge intake routing: REQUIRED

## Purpose

Decide whether the truth foundation doctrine absorbed through TKG-T0, TKG-T1,
and TKG-T2 is ready for a small static claim guard.

Decision:
`AUTHOR_TKG_T4_GC018_FOR_STATIC_TRUTH_FOUNDATION_CLAIM_GUARD`

Recommended next:
`TKG_T4_STATIC_TRUTH_FOUNDATION_CLAIM_GUARD_IMPLEMENTATION`

## Authorization / Decision

Operator authorization: the operator instructed Codex to continue through the
remaining TKG roadmap after TKG-T2.

TKG-T3 authorizes only a future GC-018 and checker implementation tranche. It
does not itself implement a checker, wire a hook, import AGT or Truth Kernel
runtime code, run a provider/live proof, create an evidence database, create an
obligation registry, open a public-sync batch, or claim production governance
behavior.

## Non-Goals

This roadmap does not:

- implement `governance/compat/check_truth_foundation_claim_guard.py`;
- add tests or hook/catalog wiring;
- edit runtime, provider, CLI/MCP, adapter, package, generated aggregate, or
  public-sync behavior;
- run provider/live proof or consume API keys;
- promote upstream AGT or `CVF_Truth_Kernel_Patch/` as CVF authority;
- require repo-wide provenance labels.

## Scope / Target / Owner Boundary

In scope:

- translate TKG-T2 checker candidates into a bounded static-checker plan;
- select which claim classes have enough value and low enough noise for TKG-T4;
- record which candidate should stay advisory;
- preserve existing CVF owner surfaces as the authority for evidence,
  workflow, release truth, and TruthScore behavior.

Out of scope:

- runtime/provider/live behavior;
- MCP gateway, hypervisor, kill switch, quarantine, circuit breaker, CLI
  adapter, package activation, certification, generated aggregate, or MPI-T6
  runtime;
- direct import of upstream AGT code or `CVF_Truth_Kernel_Patch/` code;
- public-sync export;
- repo-wide provenance-label retrofit.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| TKG-T0 selected truth-kernel doctrine seed and parked runtime work | `docs/roadmaps/CVF_TKG_T0_AGENT_GOVERNANCE_TRUTH_KERNEL_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | Proposed Roadmap; Claim Boundary | `TKG-T3` | TKG-T0 roadmap | VALUE_SET | ACCEPT |
| TKG-T1 owns source authority, integrity, LLM, provenance label, and movement doctrine | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | Source Authority Rule; Integrity Is Not Truth; LLM Output Is Not Self-Trusting; Provenance Label Contract | `cvf.truthFoundation.sourceProvenanceVerification.tkgT1.v1` | truth foundation contract | VALUE_SET | ACCEPT |
| TKG-T2 recommends a static claim-guard plan before any checker | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_OWNER_SURFACE_RECONCILIATION_MATRIX.md` | T2 Decision; Candidate Matrix section | `TKG-T3 Truth Foundation Static Claim Guard Plan` | TKG-T2 reconciliation matrix | VALUE_SET | ACCEPT |
| TKG-T2 defers checker implementation until TKG-T3 plus fresh GC-018 | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_OWNER_SURFACE_RECONCILIATION_MATRIX.md` | Candidate Matrix section | `TKG-T4 Static checker implementation` | TKG-T2 reconciliation matrix | VALUE_SET | ACCEPT |
| Existing equivalence guard covers copy/equivalence claims near paths | `governance/compat/check_equivalence_claim_evidence.py` | checker docstring; `EQUIVALENCE_PHRASES` | `check_text` | equivalence claim evidence checker | EXISTS | ACCEPT |
| Existing Delta guard covers execution-control claim boundary sections | `governance/compat/check_delta_execution_claim_boundary.py` | `REQUIRED_SECTION`; `check_text` | `check_text` | Delta execution claim boundary checker | EXISTS | ACCEPT |
| Existing memory claim guard covers derived-view and memory authority overclaims | `governance/compat/check_memory_access_claim.py` | checker docstring; `CLAIM_RULES`; `diagnose_memory_access_claims` | `CLAIM_RULES` | memory access claim checker | EXISTS | ACCEPT |
| Autorun workflow control requires gate failure repair instead of handwritten pass claims | `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | Failure policy | agent autorun workflow control standard | autorun governance standard | EXISTS | ACCEPT |
| Agent execution SOP requires evidence proportional to the claim | `docs/reference/CVF_AGENT_EXECUTION_WORKFLOW_SOP_2026-05-19.md` | Evidence must be proportional to the claim | agent execution SOP | execution workflow standard | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | TKG-T1 contract, TKG-T2 matrix, existing equivalence, Delta, and memory claim guards |
| Runtime behavior claimed | N/A_WITH_REASON: this roadmap changes no runtime, route, CLI/MCP, adapter, provider, public, or MPI-T6 behavior |
| Live/provider proof claimed | N/A_WITH_REASON: no live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized or performed |
| Freshness disposition | PASS - current source evidence supports a checker plan only |

## Candidate Claim Classes

| Candidate | T3 decision | Reason | T4 handling |
|---|---|---|---|
| Integrity artifact overclaimed as semantic truth | IMPLEMENT | receipts, hashes, approvals, and commits are frequent in closure and dispatch prose | add static phrase guard with guardrail exclusions |
| LLM or reviewer prose used as sole verifier for hard claims | IMPLEMENT | hard-claim verification needs source, command, receipt, test, or accountable authorization evidence | add static phrase guard with hard-claim context terms |
| External input treated as CVF authority without CVF owner surface | IMPLEMENT | external-absorption lanes repeatedly risk promoting source inputs too quickly | add static phrase guard for external repo, copied folder, patch, or provider-memory authority language |
| Important truth-foundation claim missing provenance label | DEFER | TKG labels are new doc-only vocabulary and retroactive repo-wide enforcement would be noisy | keep advisory in TKG-T4 review, not machine failure |

## T4 Checker Envelope

TKG-T4 should implement one conservative checker:

`governance/compat/check_truth_foundation_claim_guard.py`

The checker should scan changed governed Markdown under:

- `docs/baselines/`
- governed work-order Markdown files
- `docs/reviews/`
- `docs/reference/`
- `docs/roadmaps/`

The checker should skip archived paths and should support:

- `--base`
- `--head`
- `--enforce`
- `--json`

Required focused tests:

- invalid integrity-as-truth language fails;
- valid integrity-boundary language passes;
- invalid LLM/reviewer-as-sole-verifier language fails;
- valid reviewer-risk language passes;
- invalid external-input-as-CVF-authority language fails;
- valid external-input-advisory language passes;
- archived files are ignored.

## Guard Behavior Discussion

Discussion-only disposition: META_DISCUSSION_ONLY

The future checker must not fail this roadmap merely because this roadmap names
the claim classes it plans to prevent. TKG-T4 should include guardrail terms or
a discussion-section exclusion so planning prose can describe invalid examples
without becoming a false positive.

## Design Control Gate

| Control | Required disposition | Verdict |
|---|---|---|
| CVF authority | T4 must cite TKG-T1 and TKG-T2, not external inputs alone | PASS |
| Checker scope | T4 checks only bounded claim-language classes | PASS |
| Label enforcement | provenance-label missing remains advisory until a concrete owner surface exists | PASS |
| Runtime boundary | runtime/provider/live/public/package/MCP behavior stays out of scope | PASS |
| Fresh implementation authority | T4 requires fresh GC-018 before checker implementation | PASS |

## Work Plan

| Step | Output | Stop condition |
|---|---|---|
| Classify T2 candidates | Candidate Claim Classes | any candidate needs runtime or repo-wide retrofit |
| Select T4 envelope | T4 Checker Envelope | checker would duplicate existing equivalence, Delta, or memory guards |
| Park noisy candidate | Rejected Or Deferred Candidates | provenance labels become mandatory without owner-surface adoption |
| Close T3 | Machine Closure Package | missing source verification or public/runtime boundary |

## Verification / Evidence

| Evidence item | Command or artifact | Required result |
|---|---|---|
| TKG-T1 contract | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | source/provenance/verification doctrine exists |
| TKG-T2 matrix | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_OWNER_SURFACE_RECONCILIATION_MATRIX.md` | T3 plan is recommended and T4 is deferred |
| Structural/gate checks | governance gates over base `19ac0faf` and `HEAD` | PASS before material commit |

## Rejected Or Deferred Candidates

| Candidate | Disposition | Reopen condition |
|---|---|---|
| repo-wide provenance-label required-field gate | DEFERRED_WITH_REOPEN_CONDITION | reopen only after at least one TKG-owned artifact family adopts labels and source-verifies label applicability |
| evidence record schema/checker | DEFERRED_WITH_REOPEN_CONDITION | reopen only when a concrete evidence packet needs TKG evidence fields |
| obligation registry or runtime | REJECTED_FOR_THIS_CHAIN | reopen only with explicit operator runtime requirement and fresh GC-018 |
| AGT MCP gateway, hypervisor, or Truth Kernel package import | REJECTED_FOR_THIS_CHAIN | reopen only with explicit runtime/operator requirement, source verification, tests, and live proof plan |

## Roadmap Sequence

| Tranche | Status | Objective | Boundary |
|---|---|---|---|
| TKG-T0 | CLOSED_PASS_BOUNDED | audit AGT and Truth Kernel patch and select doctrine seed | documentation-only |
| TKG-T1 | CLOSED_PASS_BOUNDED | author CVF-owned source/provenance/verification contract | no checker/runtime/import |
| TKG-T2 | CLOSED_PASS_BOUNDED | reconcile TKG fields against existing owner surfaces | no checker/runtime/import |
| TKG-T3 | CLOSED_PASS_BOUNDED | decide the static checker envelope | no checker implementation |
| TKG-T4 | RECOMMENDED_NEXT | implement bounded static claim guard with GC-018, tests, and hook/catalog wiring if source-verified | no runtime/provider/live/public/package behavior |
| TKG-T5 | PARKED_AFTER_T4 | close remaining TKG absorption value and record reopen conditions | requires TKG-T4 closure |

## Acceptance Criteria

| ID | Criterion | Disposition |
|---|---|---|
| AC1 | T3 does not implement a checker or runtime behavior | PASS |
| AC2 | T3 selects only bounded, low-noise claim classes for T4 | PASS |
| AC3 | provenance-label missing enforcement is deferred with a concrete reopen condition | PASS |
| AC4 | T4 requires fresh GC-018 before checker implementation | PASS |
| AC5 | public-sync, provider/live proof, adapters, packages, MCP, and MPI-T6 remain out of scope | PASS |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | External repo or copied folder -> Root/folder lifecycle classification plus absorption map when retained -> CVF-owned reference contract -> ABSORB, ADAPT, DEFER, REJECT, or BLOCK |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/roadmaps/CVF_TKG_T3_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD_PLAN_ROADMAP_2026-06-28.md` |
| Disposition | ADAPT TKG-T2 candidate findings into a bounded TKG-T4 static-checker plan |
| Claim boundary | external sources remain inputs; TKG-T3 creates no runtime, provider/live, public-sync, adapter, package, MCP, or checker behavior |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | this roadmap | may use for TKG-T4 GC-018 and checker scoping | Source Verification Block and Candidate Claim Classes | N/A with reason: documentation-only roadmap | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future public-safe or adapter readout | no external interface, MCP tool, CLI command, package, or public behavior is created | Claim Boundary | separate GC-018/source-verified work order required | `DEFERRED_WITH_REASON` |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| truth-foundation overclaim language has enough repeated absorption-lane risk for a bounded guard | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | TKG-T4 GC-018 and static checker |
| provenance-label enforcement is too broad without an adopted artifact family | RULE_GAP | DOCUMENTATION_ONLY_LEARNING | DESIGN_REVIEW_REQUIRED | keep label enforcement advisory until a concrete owner surface exists |

Runtime/provider/cost learning lane: N/A_WITH_REASON - local documentation
planning only.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | TKG-T3 static truth foundation claim-guard plan |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime receipt or execution-control behavior is claimed |
| actionEvidence | ACTION_EVIDENCE_PRESENT - TKG-T3 roadmap created from TKG-T1 and TKG-T2 source-verified references |
| invocationBoundary | local governed documentation authoring |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, adapter, or package interception claim |
| claimLanguage | roadmap and future-checker scoping language only |
| forbiddenExpansion | no runtime, provider/live proof, public-sync, adapter, package activation, certification, MCP gateway, hypervisor, evidence database, obligation registry, generated aggregate, or MPI-T6 runtime |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance truth-foundation checker planning. Public wording
requires a separate public-sync decision.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local workspace |
| Session or invocation | `tkg-t3-truth-foundation-static-claim-guard-plan-2026-06-28` |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, Get-Content, apply_patch, governance gates |
| Target paths | `docs/roadmaps/CVF_TKG_T3_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD_PLAN_ROADMAP_2026-06-28.md` |
| Allowed scope source | operator approved continuing the TKG roadmap after TKG-T2 |
| Before status evidence | baseHead `19ac0faf`; worktree clean before patch |
| After status evidence | TKG-T3 roadmap added |
| Diff evidence | `git diff --name-status 19ac0faf..HEAD` |
| Approval boundary | documentation-only checker-plan roadmap |
| Claim boundary | no runtime, provider/live, public-sync, generated aggregate, checker implementation, adapter, package activation, certification, MCP gateway, hypervisor, circuit breaker, evidence database, obligation registry runtime, SOT index runtime, verifier service, or Truth Kernel package import |
| Agent type | single-agent dispatcher/implementer/reviewer/closer |
| Invocation ID | `tkg-t3-static-claim-guard-plan-2026-06-28` |
| Expected manifest | `docs/roadmaps/CVF_TKG_T3_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD_PLAN_ROADMAP_2026-06-28.md` |
| Actual changed set | `docs/roadmaps/CVF_TKG_T3_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD_PLAN_ROADMAP_2026-06-28.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this tranche |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Completion or reviewer artifact | `docs/roadmaps/CVF_TKG_T3_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD_PLAN_ROADMAP_2026-06-28.md` | this closed roadmap acts as the single-agent T3 closure artifact | PASS |
| Roadmap artifact | `docs/roadmaps/CVF_TKG_T3_TRUTH_FOUNDATION_STATIC_CLAIM_GUARD_PLAN_ROADMAP_2026-06-28.md` | this roadmap | PASS |
| Work order status | no worker-dispatch work order in TKG-T3 | single-agent roadmap plan | N/A with reason |
| Roadmap state | this roadmap | Status: CLOSED_PASS_BOUNDED | PASS |
| Registry JSON | no registry JSON mutation authorized | changed set excludes registry JSON | BLOCKED with reason: TKG-T3 is documentation-only |
| Registry Markdown | no registry Markdown mutation authorized | changed set excludes registry Markdown | BLOCKED with reason: TKG-T3 is documentation-only |
| External evidence digest | N/A with reason: TKG-T3 consumes TKG-T1 and TKG-T2 CVF-owned references, not a new external digest | no new external artifact imported | N/A with reason |
| System loop interlock | N/A with reason: no runtime loop/interlock surface changed | Claim Boundary | N/A with reason |
| Session continuity | active handoff marker planned after material commit | separate handoff-sync commit required | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| TKG-T3-Q1 | this roadmap | N/A with reason: Markdown artifact | TKG-T4 selected as next implementation candidate | `TKG_T4_STATIC_TRUTH_FOUNDATION_CLAIM_GUARD_IMPLEMENTATION` | PASS |
| TKG-T3-Q2 | Candidate Claim Classes | N/A with reason: Markdown table | three claim classes selected for implementation | integrity, LLM/reviewer, and external-input authority classes selected | PASS |
| TKG-T3-Q3 | Rejected Or Deferred Candidates | N/A with reason: Markdown table | provenance-label missing enforcement deferred | DEFERRED_WITH_REOPEN_CONDITION | PASS |
| TKG-T3-Q4 | Claim Boundary | N/A with reason: Markdown section | no runtime/provider/public/package/checker behavior claimed | boundary section present | PASS |

## Claim Boundary

TKG-T3 is a static-checker planning roadmap only. It does not implement or
authorize AGT runtime governance, Truth Kernel runtime, MCP gateway
interception, hypervisor execution rings, circuit breakers, evidence database,
obligation registry runtime, SOT index runtime, independent verifier service,
provider/live proof, public-sync export, CLI/MCP adapter, package activation,
certification, generated aggregate, hook wiring, checker mutation, or
production/hosted readiness.

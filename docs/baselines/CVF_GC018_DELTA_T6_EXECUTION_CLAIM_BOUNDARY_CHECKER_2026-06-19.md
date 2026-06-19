# CVF GC-018 - Delta-T6 Execution Claim Boundary Checker

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-19

Owner: Codex

Execution route: SINGLE_AGENT_MULTI_ROLE

Base head: `1092829b`

## Purpose

Authorize a bounded governance-control tranche using Delta-T5 closure artifact
`docs/reviews/CVF_DELTA_T5_EXECUTION_CONTROL_CAPABILITY_ROADMAP_COMPLETION_2026-06-19.md`
at material/closure commit `97a634c2`.
Delta-T6 promotes the Delta-T5 no-receipt/no-claim rule into an early machine
guard: changed governed Markdown artifacts that make broad execution-control,
agent-coding-control, mandatory-wrapper, direct-interception, or universal
governed-coding claims must include explicit receipt/action evidence or reject
the claim boundary.

This tranche does not authorize runtime execution control, direct IDE/shell/git/
filesystem interception, new MCP tools, provider/live calls, public-sync,
queues, daemons, CVF Web action execution, wrapper/proxy enforcement, or
universal governed-coding claims.

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
| --- | --- |
| Decision | Dispatch a bounded machine guard for execution-control claim boundaries |
| Proposed tranche | Delta-T6 Execution Claim Boundary Checker |
| Base head | `1092829b` |
| Worker / reviewer / closer | Codex across phase-separated roles |
| Route | `SINGLE_AGENT_MULTI_ROLE` |
| Upstream evidence | Delta-T5 roadmap and completion review |
| Later tranche | Receipt-to-execution evidence auditor, wrapper/proxy enforcement, direct interception, EDIT/COMMIT, provider/live, public-sync, and universal governed-coding control remain separate authorization |

## Scope / Target / Owner Boundary

Allowed scope:

- add one range-aware governance checker for changed governed Markdown
  artifacts;
- trigger only when a changed artifact explicitly makes or dispatches broad
  execution-control, governed-coding-control, mandatory-wrapper, direct-
  interception, or universal enforcement claims;
- require a `Delta Execution Claim Boundary Control Block` with non-empty rows;
- require receipt/action evidence rows to state proof, explicit rejection, or
  `N/A with reason`;
- add focused tests for valid bounded claim, rejected claim, missing block,
  missing evidence, and unrelated-doc non-applicability;
- wire the checker into reviewer-fast, pre-commit, pre-push, and autorun common
  gates;
- add completion review and evidence JSON.

Forbidden scope:

- no MCP/runtime source mutation except governance checker code;
- no new Delta execution profile, no launcher behavior change, no approval
  runtime policy change, no Model Gateway behavior change;
- no provider/live proof, public-sync, queue, daemon, CVF Web action execution,
  external repo import, broad legacy scan, or readiness claim;
- no claim that this guard intercepts direct IDE, shell, git, filesystem, or
  agent tool actions.

Risk ceiling: governance-control R1. The guard is repo-local, range-aware, and
forward-only.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | `MACHINE_GUARD_ONLY`: no runtime enforcement added |
| claimDisposition | future applicable artifacts must state `CLAIM_REJECTED`, `BOUNDED_CLAIM_WITH_EVIDENCE`, or `N/A with reason` |
| receiptEvidence | future applicable artifacts must state `CVF_RECEIPT_PRESENT`, `CLAIM_REJECTED_NO_RECEIPT`, or `N/A with reason` |
| actionEvidence | future applicable artifacts must state `ACTION_EVIDENCE_PRESENT`, `CLAIM_REJECTED_NO_ACTION`, or `N/A with reason` |
| invocationBoundary | future applicable artifacts must state whether invocation is mandatory, cooperating-only, or `N/A with reason` |
| interceptionBoundary | future applicable artifacts must reject direct IDE/shell/git/filesystem interception unless separately authorized |
| claimLanguage | future applicable artifacts must avoid universal governed-coding control language unless receipt/action proof exists |
| forbiddenExpansion | this tranche forbids runtime profile expansion, EDIT/COMMIT execution, arbitrary commands, provider/live, public-sync, queue, daemon, and direct interception |

## Delta Mutating Profile Boundary Control Block

| Field | Disposition |
| --- | --- |
| profileScope | `MACHINE_GUARD_ONLY`: no new runtime profile |
| fixedTargetPolicy | N/A with reason: this tranche checks broad execution-control claim language, not mutation targets |
| approvalEvidenceSource | N/A with reason: this tranche does not add approval-backed mutation |
| callerPathInput | N/A with reason: checker-only artifact; no caller path input |
| commandAuthority | N/A with reason: no runtime command authority added |
| receiptChain | N/A with reason: this tranche checks future claim evidence, not runtime execution |
| claimBoundary | no universal governed-coding or direct interception claim |
| forbiddenExpansion | runtime profiles, EDIT/COMMIT execution, provider/live, public-sync, queue, daemon, and direct interception remain parked |

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Delta-T5 defines a no-receipt/no-claim rule for governed-coding control. | LITERAL_INVARIANT | `docs/roadmaps/CVF_DELTA_EXECUTION_CONTROL_CAPABILITY_ROADMAP_2026-06-19.md` | lines 108-121 | `No-Receipt No-Claim Rule` | Delta-T5 roadmap | ACCEPT |
| Delta-T5 defines broad claim language boundaries for Delta overall and runtime enforcement claims. | LITERAL_INVARIANT | `docs/roadmaps/CVF_DELTA_EXECUTION_CONTROL_CAPABILITY_ROADMAP_2026-06-19.md` | lines 123-146 | `Claim Language Boundary` | Delta-T5 roadmap | ACCEPT |
| Delta-T5 recommends Delta-T6 as a high-value machine guard candidate. | LITERAL_INVARIANT | `docs/roadmaps/CVF_DELTA_EXECUTION_CONTROL_CAPABILITY_ROADMAP_2026-06-19.md` | line 162 | `Delta-T6 Execution Claim Boundary Checker` | Delta-T5 roadmap next tranche table | ACCEPT |
| Delta-T5 completion records Delta-T6 as a machine-check candidate for execution-control claims lacking receipt/action evidence. | LITERAL_INVARIANT | `docs/reviews/CVF_DELTA_T5_EXECUTION_CONTROL_CAPABILITY_ROADMAP_COMPLETION_2026-06-19.md` | lines 120-123 | `Finding-To-Governance Learning Disposition` | Delta-T5 completion review | ACCEPT |
| Existing Delta-T4B checker provides the range-aware changed-governed-Markdown checker pattern. | EXISTS | `governance/compat/check_delta_mutating_profile_boundary.py` | lines 81-129 and 275-304 | `_get_changed_paths`; `check_text`; `main` | Delta mutating profile boundary checker | ACCEPT |
| Existing Delta-T4B tests provide the import-and-check_text focused unittest pattern. | EXISTS | `governance/compat/test_check_delta_mutating_profile_boundary.py` | lines 1-134 | `DeltaMutatingProfileBoundaryTests` | Delta mutating profile boundary tests | ACCEPT |
| Local hook chain currently registers a Delta checker in reviewer-fast, pre-commit, and pre-push lanes. | EXISTS | `governance/compat/run_local_governance_hook_chain.py` | lines 102-103, 264-265, and 458-459 | `REVIEWER_FAST_CHECKS`; `HOOK_CHAINS` | local governance hook chain | ACCEPT |
| Autorun common commands currently register a Delta checker. | EXISTS | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 165-166 | `_common_commands` | autorun workflow gate | ACCEPT |

## New Doc-Only Fields

| New item | Required value or shape | Purpose |
| --- | --- | --- |
| `Delta Execution Claim Boundary Control Block` | governed Markdown section with required row labels | future execution-control claim declaration |
| `claimScope` | non-empty row | state guard-only or runtime-enforcement scope |
| `claimDisposition` | `CLAIM_REJECTED`, `BOUNDED_CLAIM_WITH_EVIDENCE`, or `N/A with reason` | prevent silent universal claims |
| `receiptEvidence` | `CVF_RECEIPT_PRESENT`, `CLAIM_REJECTED_NO_RECEIPT`, or `N/A with reason` | bind governed-coding claims to receipt evidence |
| `actionEvidence` | `ACTION_EVIDENCE_PRESENT`, `CLAIM_REJECTED_NO_ACTION`, or `N/A with reason` | bind governed-coding claims to action evidence |
| `invocationBoundary` | non-empty row | distinguish mandatory from cooperating-only invocation |
| `interceptionBoundary` | non-empty row | reject direct interception unless separately authorized |
| `claimLanguage` | non-empty row | constrain broad control language |
| `forbiddenExpansion` | non-empty row | state parked expansion classes |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | Runtime/MCP/control claim must cite current proof, work-order source verification, and local-view guard before implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; proposed `governance/compat/check_delta_execution_claim_boundary.py` |
| Owner surface | Delta-T6 GC-018 and work order |
| Disposition | `DO_NOW` for guard-only machine enforcement; `BLOCKED_UNTIL_CVF_PROOF` for runtime enforcement expansion |
| Claim boundary | no runtime/provider/live/public-sync/direct interception/universal governed-coding control claim |

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | A new checker fails applicable changed governed Markdown artifacts that omit the Delta execution-claim control block. |
| AC2 | The checker requires all control-block rows to be non-empty. |
| AC3 | The checker rejects receipt/action evidence rows unless they state proof, explicit rejection, or `N/A with reason`. |
| AC4 | The checker ignores unrelated governed Markdown artifacts. |
| AC5 | Focused tests cover positive, negative, missing-field, evidence-boundary, and non-applicable cases. |
| AC6 | The checker is wired into reviewer-fast, pre-commit, pre-push, and autorun common gates. |
| AC7 | Completion evidence records no runtime/provider/live/public/direct-interception/universal-control claim. |

## Evidence / Verification

Required evidence:

- focused unittest or pytest for the new checker;
- `python governance/compat/run_worker_return_fast_gate.py --pytest-target <new-test>`;
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <implementationBaseHead> --head HEAD`;
- commit-steward preflight for implementation and closure;
- exact changed-set evidence and completion review.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance guard. Public-sync is not authorized.

## Claim Boundary

Delta-T6 may prove only that changed governed artifacts about broad execution
control or governed-coding control must carry bounded claim evidence. It does
not prove runtime interception, mandatory wrapper use, provider behavior,
hosted readiness, public readiness, production readiness, wrapper/proxy
enforcement, or universal governed-coding control.

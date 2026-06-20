# CVF GC-018 - AAF-T5 Worker Experience Retrospective Capture Foundation

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-20

docType: baseline

dispatchBaseHead: 8f8bc2d5

Batch ID: AAF-T5

## Purpose

Authorize AAF-T5 as a bounded governance/helper foundation tranche that captures
worker friction proactively at worker return time.

AAF-T5 responds to an operator-identified blind spot: CVF has an error-to-
governance learning loop when an agent fails a guard, but it lacks a proactive
worker-experience channel for runs that pass gates while still exposing useful
latency, helper, source-discovery, worktree, keyword-trap, or enum/token
friction.

AAF-T5 must create a stable standard, checker, tests, and helper/hook wiring for
worker-experience retrospective tokens. It must not implement the Guard
Orientation Read-Receipt Gate, helper/index drift hardening, provider/runtime
behavior, public-sync, or direct interception.

## Operator Authorization

The operator accepted the roadmap direction and asked Codex to write the work
order after the external worker response returned uncommitted. The operator also
explicitly framed this as a governance uplift: the issue is not merely to learn
a lesson, but to add automation/helper support so future noncoder operators and
external agents do not repeat avoidable latency.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-20 request to finalize T5/T6/T7 and open AAF-T5 | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| AAF-T4 completion | `docs/reviews/CVF_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_COMPLETION_2026-06-20.md` | ACCEPT |
| Worker-experience proposal | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_FOR_CODEX_2026-06-20.md` | ADVISORY_INPUT_ACCEPTED |
| Codex rebuttal | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CODEX_REBUTTAL_2026-06-20.md` | CLASSIFICATION_INPUT |
| Returned advisory response | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md` | ADVISORY_INPUT_ACCEPTED |
| Codex classification | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_T5_T6_T7_CODEX_CLASSIFICATION_2026-06-20.md` | ACCEPT |
| AAF helper | `governance/compat/run_agent_automation_assist.py` | ACCEPT |
| Commit steward | `governance/compat/run_agent_commit_steward_preflight.py` | ACCEPT |
| Worker-return fast gate | `governance/compat/run_worker_return_fast_gate.py` | ACCEPT |
| Local hook chain | `governance/compat/run_local_governance_hook_chain.py` | ACCEPT |

Provider-specific memory and private chat history are not CVF source authority.
The returned external-agent packets are advisory inputs only until absorbed by
this Codex classification and the paired work order.

## Scope / Owner Boundary

Allowed worker scope:

- create a stable standard/front door under
  `docs/reference/worker_experience_retrospective/README.md`;
- create `governance/compat/check_worker_experience_retrospective.py`;
- create `governance/compat/test_check_worker_experience_retrospective.py`;
- update `governance/compat/run_agent_automation_assist.py` to detect missing
  or malformed worker-experience tokens earlier;
- update `governance/compat/test_run_agent_automation_assist.py` for the helper
  changes;
- wire the checker into `governance/compat/run_local_governance_hook_chain.py`
  for reviewer-fast, pre-commit, and pre-push lanes;
- update `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` only to
  route worker-experience retrospective lookup to the new standard;
- create the AAF-T5 worker-return artifact.

Forbidden worker scope:

- no edits to closed AAF-T1/T2/T3/T4 artifacts;
- no edits to session state, active handoff, session memory, root startup
  files, or generated session aggregates;
- no AAF-T6 Guard Orientation Read-Receipt Gate implementation;
- no AAF-T7 helper/index drift hardening for `push` beyond recording the
  experience enum and preserving current helper behavior;
- no runtime/provider/live proof, provider calls, secrets/quota use, dependency
  install, public-sync, MCP execution, CVF Web action, queue/daemon, watcher,
  wrapper/proxy enforcement, direct IDE/shell/git/filesystem interception,
  arbitrary command execution, EDIT/COMMIT execution, production/public/release
  readiness, full-hook equivalence, speed claim, cost-optimization claim, or
  universal governed-coding-control claim.

Risk ceiling: R2 governance helper and checker foundation. The worker may edit
checker/helper source and focused tests, but no product runtime.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with these owned
artifacts changed or created:

- `docs/reference/worker_experience_retrospective/README.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `governance/compat/check_worker_experience_retrospective.py`
- `governance/compat/test_check_worker_experience_retrospective.py`
- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `docs/reviews/CVF_AAF_T5_WORKER_EXPERIENCE_RETROSPECTIVE_CAPTURE_FOUNDATION_WORKER_RETURN_2026-06-20.md`

No other worker-owned file is authorized unless the work order is revised.

## Decision / Baseline / Proposed Tranche

Baseline decision: AAF-T5 is ready for worker dispatch as a bounded
worker-experience retrospective capture foundation.

Proposed tranche: `AAF-T5 Worker Experience Retrospective Capture Foundation`.

Tranche owner split: the dispatch author creates this GC-018, classification,
and paired work order; the worker implements the standard, checker, helper
diagnostics, hook wiring, focused tests, and worker return without committing;
the reviewer/closer reviews, repairs only within allowed scope if needed,
commits accepted material, and session-syncs only after material closure.

Baseline evidence:

- Current dispatch base is `8f8bc2d5`.
- AAF-T4 is closed and its continuity recommends AAF-T5, but AAF-T4's old
  wording was read-receipt first.
- The operator and returned advisory chain changed the AAF-T5 target to
  worker-experience capture first, with read receipt deferred to AAF-T6.
- Existing helper and hook surfaces are present and source-verified.

## Source / Predecessor Evidence

| Source | Evidence | Disposition |
|---|---|---|
| AAF-T4 completion | lines 69-72, 102-103, 118 identify read receipt as voluntary and machine-check candidate | ACCEPT |
| Codex classification | T5/T6/T7 split and final enum/token shape | ACCEPT |
| Returned advisory response | lines 69, 74, 91, 99-116, 125-144, and 153 name enum additions, NA token, push drift, worker-return marker, and worked-example value | ACCEPT |
| AAF helper source | read-only helper boundary and worker-return detection hooks | ACCEPT |
| Commit steward source | `push` belongs to steward, not worker-facing helper T5 scope | ACCEPT_DEFER_TO_AAF_T7 |
| Local hook chain source | reviewer-fast, pre-commit, and pre-push lanes exist for checker wiring | ACCEPT |

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `8f8bc2d5`.
- `git status --short` showed only the three uncommitted worker-experience
  advisory files, plus the recurring Windows global git-ignore permission
  warning.
- Source verification used direct file reads and `rg -n` lookups against
  current repository files.

Required pre-dispatch verification before commit:

```powershell
python governance/compat/run_agent_automation_assist.py --base 8f8bc2d5 --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 8f8bc2d5 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 8f8bc2d5 --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 8f8bc2d5 --head HEAD --enforce
```

## Required Standard And Token Shape

The new reference standard must define eligible worker-return artifacts and the
required token forms.

Structured retrospective form:

```text
WORKER_EXPERIENCE_RETRO:
frictionLevel: NONE|LOW|MEDIUM|HIGH|BLOCKING
frictionType: NONE|GATE_SURPRISE|SCOPE_AMBIGUITY|SOURCE_DISCOVERY|WORKTREE_CONTAMINATION|HELPER_GAP|LATENCY|KEYWORD_TRAP|ENUM_OR_TOKEN_MISMATCH|OTHER
observedStep: short text
preventiveControlCandidate: NONE|INDEX_UPDATE|HELPER_DIAGNOSTIC|CHECKER|WORK_ORDER_TEMPLATE|STANDARD_UPDATE|DEFER
```

No-friction escape hatch:

```text
WORKER_EXPERIENCE_RETRO_NA_WITH_REASON: no friction beyond normal gates; no gate surprise, no helper gap, no worktree contamination this return
```

The checker must reject bare placeholder NA forms. The accepted NA form must
assert no friction beyond normal gates.

## Checker Behavior

The checker must:

- apply only to eligible worker-return artifacts;
- accept `Self-declared worker-return artifact: yes` as an explicit marker;
- otherwise require both `Status: COMPLETE_PENDING_REVIEW` or
  `Status: BLOCKED_WITH_REASON` and a `Responds to work order:` line;
- exclude `docType: review_context`, completion reviews, reference standards,
  baselines, work orders, session-sync files, and advisory classification
  packets;
- accept exactly one of the structured retrospective or asserting NA forms;
- validate enum values exactly;
- require non-empty `observedStep` for structured retrospective form;
- report path-specific errors that tell the worker which token or enum failed;
- provide an `--enforce` mode suitable for hook integration.

The helper must surface missing or malformed tokens as early diagnostics, while
remaining read-only.

## Claim Boundary

AAF-T5 may claim only a worker-experience retrospective capture standard,
checker, helper diagnostic, tests, and hook wiring for worker-return artifacts.
It must not claim guard-orientation read receipt enforcement, automated provider
selection, runtime provider routing, provider/live behavior, public readiness,
production readiness, release readiness, direct interception, wrapper/proxy
enforcement, queue/daemon execution, cost optimization, full-hook equivalence,
or universal governed-coding control.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output to finding classification to governed work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | worker-experience retrospective standard and checker |
| Disposition | ADAPT as CVF-owned governance helper foundation |
| Claim boundary | advisory inputs become authority only through this baseline, Codex classification, and paired work order |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T5 worker-experience retrospective capture dispatch only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | worker-return artifact text and deterministic local checks only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | retrospective capture standard, checker, helper diagnostic, tests, hook wiring |
| forbiddenExpansion | read-receipt gate, automated provider selection, runtime routing, provider/live proof, wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain parked |

## Rescan Intelligence Hardening

- Original source artifact: operator worker-experience blind-spot finding and
  returned advisory response.
- Predecessor intake artifact:
  `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md`.
- Predecessor intake artifacts: the three worker-experience advisory/rebuttal
  packets named in Authority Chain.
- Delta ledger status: `CHANGED_DISPOSITION` because AAF-T5 pivots from
  read-receipt gate first to worker-experience capture first.
- Routing matrix status:
  - `DO_NOW`: AAF-T5 worker-experience capture foundation.
  - `RESOLVED_BY_DESIGN`: keep T5 as capture sensor while T6/T7 remain separate.
  - `DEFER`: AAF-T6 guard orientation read-receipt gate.
  - `DEFER`: AAF-T7 helper/index friction hardening.
  - `SEPARATE_RUNTIME_TRANCHE`: runtime/provider/live/MCP/direct-interception scope.
  - `OUT_OF_SCOPE`: runtime/provider/live/public-sync/direct interception.
- Semantic sampling status: `PARTIAL_TARGETED`, limited to advisory packets and
  source surfaces named in this baseline.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | AAF-T4 read receipt remains voluntary until a future AAF-T6 gate. |
| CHANGED_DISPOSITION | AAF-T5 becomes worker-experience capture first, not read-receipt first. |
| NEW_FINDING | Passing worker returns need a structured friction capture token. |
| REMOVED_OR_REJECTED | Provider/runtime/live/public-sync/direct-interception scope remains rejected. |

### Follow-Up Routing Matrix

| Lane | Disposition |
|---|---|
| DO_NOW | Create worker-experience retrospective standard, checker, helper diagnostics, tests, and hook wiring. |
| DEFER | AAF-T6 Guard Orientation Read-Receipt Gate. |
| DEFER | AAF-T7 helper/index hardening for U findings and `push` drift. |
| STRATEGIC_OPERATOR_DECISION | CGE-T3 and ACE-R1 remain parked. |
| OUT_OF_SCOPE | Production readiness, public release readiness, provider/runtime execution, universal governed-coding-control claim. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AAF-T5-RS1 | Operator finding | worker pass can hide friction | DO_NOW | Could reviewer questioning be enough? | PASS_MACHINE_CHANNEL_REQUIRED |
| AAF-T5-RS2 | Returned advisory Q2 | KEYWORD_TRAP and ENUM_OR_TOKEN_MISMATCH recur | DO_NOW enum | Could enum growth be deferred? | PASS_BOUND_ENUM_INCLUDED |
| AAF-T5-RS3 | Returned advisory Q4 | `push` drift exists | DEFER AAF-T7 | Could AAF-T5 fix helper mode drift now? | PASS_SCOPE_DEFERRED |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Control-plane disposition | Earliest phase target |
|---|---|---|---|
| Worker pass can hide useful friction | MACHINE_GATE_GAP | MACHINE_CHECK_AUTHORIZED | reviewer-fast |
| Worker no-friction claim needs a falsifiable form | TEMPLATE_GAP | STANDARD_AUTHORIZED | worker return |
| Advisory packets can discuss worker returns without being worker returns | CHECKER_SCOPE_RISK | SELF_DECLARATION_AUTHORIZED | checker matching |
| Helper should surface missing token early | LATENCY_GAP | HELPER_DIAGNOSTIC_AUTHORIZED | AAF helper |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: AAF-T5 is private provenance governance-helper foundation work. Public
export requires separate public-sync authorization and remote verification.

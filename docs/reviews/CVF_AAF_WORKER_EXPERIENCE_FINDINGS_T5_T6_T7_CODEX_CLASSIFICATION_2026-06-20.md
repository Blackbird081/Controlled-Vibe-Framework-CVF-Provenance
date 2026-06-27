# CVF AAF Worker Experience Findings T5 T6 T7 Codex Classification

Memory class: FULL_RECORD

Status: CLASSIFIED_DISPATCH_AAF_T5

docType: review_context

Date: 2026-06-20

Classification owner: Codex reviewer/orchestrator role

Input packets:

- `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_FOR_CODEX_2026-06-20.md`
- `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CODEX_REBUTTAL_2026-06-20.md`
- `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md`

EPISTEMIC_PROCESS_NA_WITH_REASON: classification of returned advisory packets
only. This packet makes no runtime, provider, public-sync, live-proof,
readiness, or universal governed-coding-control claim.

## Purpose

Finalize the AAF-T5/T6/T7 split after the operator identified a real governance
blind spot: CVF learns from agent errors after a guard failure, but it does not
proactively capture worker friction when a worker passes all gates.

The finding is accepted. A worker can return `COMPLETE_PENDING_REVIEW`, pass the
structural gates, and still have suffered preventable friction that would never
enter the governance learning loop unless the operator or reviewer asks.

## Target / Source

Target: AAF worker-experience advisory chain and AAF-T5 dispatch decision.

Source: the three input packets named above, AAF-T4 closure evidence, and the
source files in the Source Verification Block.

## Scope / Target / Owner Boundary

Scope: classify the advisory chain and open the correct AAF-T5 dispatch lane.

Owner boundary: Codex owns classification and dispatch authoring. The worker
owns implementation only after dispatch. This packet does not edit closed
artifacts or implement code.

## Scope / Methodology

Methodology: compare operator finding, proposal, Codex rebuttal, returned
advisory response, AAF-T4 closure, helper source, commit steward, and local hook
chain. Then classify which findings belong in AAF-T5, AAF-T6, AAF-T7, or
out-of-scope lanes.

## Findings / Position

Position: AAF-T5 must capture worker experience first. AAF-T6 and AAF-T7 remain
separate. The enum additions `KEYWORD_TRAP` and `ENUM_OR_TOKEN_MISMATCH` are
accepted for T5.

## Risk / Corrective Action

Risk: merging read receipt, helper drift, and experience capture into one
tranche would blur the control boundary.

Corrective action: dispatch AAF-T5 only as the retrospective capture foundation
and record T6/T7 as deferred lanes.

## Classification Decision

| Tranche | Decision | Scope |
|---|---|---|
| AAF-T5 | DISPATCH_NOW | Worker Experience Retrospective Capture Foundation |
| AAF-T6 | DEFER_SEPARATE_TRANCHE | Guard Orientation Read-Receipt Gate |
| AAF-T7 | DEFER_SEPARATE_TRANCHE | Helper/index friction hardening for U findings |

AAF-T5 is the sensor layer. It creates a required worker-return token channel
for friction capture and an explicit no-friction escape hatch. AAF-T5 must land
before the read-receipt gate because the experience channel is how CVF decides
which worker-facing controls deserve promotion.

AAF-T6 remains the right place to turn guard orientation reading into a hard
artifact-level gate. AAF-T5 may mention that read-receipt friction is a possible
retrospective signal, but it must not implement or claim the read-receipt gate.

AAF-T7 remains the right place to harden helper/index drift such as the helper
mode vocabulary and `push` exclusion. AAF-T5 may include enum values that record
those experiences, but it must not implement the T7 code fixes.

## Final Worker Experience Token Shape

Eligible worker-return artifacts must include exactly one of the two forms
below.

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

The no-friction form is accepted for every eligible return, but only in its
asserting form. It must be falsifiable in review and cannot be reduced to a bare
placeholder.

## Eligible Artifact Boundary

AAF-T5 should key on self-declared worker-return artifacts, not every changed
file in a dirty worktree.

Eligible worker-return detection should accept either:

- explicit `Self-declared worker-return artifact: yes`; or
- a file with `Status: COMPLETE_PENDING_REVIEW` or `Status: BLOCKED_WITH_REASON`
  and a `Responds to work order:` line.

The worker should exclude `docType: review_context`, completion reviews,
reference standards, baselines, work orders, session-sync files, and advisory
classification packets. This prevents the retrospective gate from false-firing
on packets that discuss worker returns without being a worker return.

## Required Absorption Table

| Finding | Disposition | Absorbed into |
|---|---|---|
| Worker pass gates can still hide useful friction | ACCEPT | AAF-T5 required worker-experience token |
| Read receipt is valuable but different from experience capture | ACCEPT_SPLIT | AAF-T6 |
| KEYWORD_TRAP recurred as a friction class | ACCEPT | AAF-T5 enum |
| ENUM_OR_TOKEN_MISMATCH recurred as a friction class | ACCEPT | AAF-T5 enum |
| Helper/steward `push` vocabulary drift exists | ACCEPT_DEFER | AAF-T7 |
| Helper should fail early where possible | ACCEPT_DEFER | AAF-T7 and future helper diagnostics |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Proposal status is advisory and returned for Codex classification | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_FOR_CODEX_2026-06-20.md` | line 5 | `Status` | advisory proposal | ACCEPT |
| Codex rebuttal proposed `WORKER_EXPERIENCE_RETRO` | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CODEX_REBUTTAL_2026-06-20.md` | line 84 | `WORKER_EXPERIENCE_RETRO` | Codex rebuttal | ACCEPT |
| Codex rebuttal proposed `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CODEX_REBUTTAL_2026-06-20.md` | lines 94, 164-165 | `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` | Codex rebuttal | ACCEPT |
| Returned rebuttal response accepted T5/T6/T7 split | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md` | lines 28-34, 162 | tranche split | advisory response | ACCEPT |
| Returned rebuttal response recommended KEYWORD_TRAP and ENUM_OR_TOKEN_MISMATCH | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md` | lines 69, 74, 165 | `KEYWORD_TRAP`; `ENUM_OR_TOKEN_MISMATCH` | advisory response | ACCEPT |
| Returned rebuttal response proposed asserting NA token | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md` | line 91 | `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` | advisory response | ACCEPT |
| Returned rebuttal response source-checked `push` drift | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md` | lines 99-116, 167 | `push` | advisory response | ACCEPT |
| AAF-T4 closure says read receipt remains voluntary | `docs/reviews/CVF_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_COMPLETION_2026-06-20.md` | lines 69-72, 102-103, 118 | read-receipt gate candidate | AAF-T4 completion | ACCEPT |
| Helper is read-only and must not push or mutate state | `governance/compat/run_agent_automation_assist.py` | line 11 | read-only helper boundary | AAF helper | ACCEPT |
| Helper has mode vocabulary and worker-return pattern to extend | `governance/compat/run_agent_automation_assist.py` | lines 142, 161, 419, 670 | `ALLOWED_MODES`; `_WORKER_RETURN_RE` | AAF helper | ACCEPT |
| Commit steward supports push while helper omits it | `governance/compat/run_agent_commit_steward_preflight.py` | lines 200, 273, 317 | `push` | commit steward preflight | ACCEPT |
| Worker-return fast gate runs reviewer-fast and accepts focused pytest targets | `governance/compat/run_worker_return_fast_gate.py` | lines 46-47, 84 | `--pytest-target` | worker-return fast gate | ACCEPT |
| Local hook chain supports reviewer-fast, pre-commit, and pre-push lanes | `governance/compat/run_local_governance_hook_chain.py` | lines 24, 151, 155, 159, 384 | hook chains | local governance hook chain | ACCEPT |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output to atomic finding classification to CVF disposition to governed work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | worker-return packet shape and AAF helper |
| Disposition | ADAPT into CVF-owned AAF-T5 dispatch |
| Claim boundary | advisory packets remain inputs only; Codex classification and work order control implementation |

## Finding-To-Governance Learning Disposition

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Runtime/provider/cost learning lane: `N/A_WITH_REASON` - this classification
does not change runtime, provider, live, cost, token-budget, or public-sync
behavior.

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Worker friction can be invisible when all gates pass | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | AAF-T5 creates checker and helper diagnostic | handled by dispatch |
| No-friction path can become reflexive if token is too weak | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_ADDED | AAF-T5 standard defines exact asserting NA token | handled by dispatch |
| Worker-return detection can false-fire on advisory packets | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | AAF-T5 checker uses self-declared worker-return boundary | handled by dispatch |
| Helper/steward mode drift is real but not T5 scope | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | AAF-T7 helper/index friction hardening | deferred |
| Runtime/provider/cost applicability | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Rescan Intelligence Hardening

- Original source artifact: operator finding plus returned advisory/rebuttal
  packets.
- Predecessor intake artifact:
  `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because the original read-receipt
  candidate is split into T5 sensor layer, T6 read-receipt gate, and T7 helper
  hardening.
- Routing matrix status:
  - `DO_NOW`: dispatch AAF-T5 worker-experience capture.
  - `RESOLVED_BY_DESIGN`: keep T5 as sensor layer and defer read receipt/helper drift.
  - `DEFER`: AAF-T6 read-receipt gate.
  - `DEFER`: AAF-T7 helper/index hardening.
  - `SEPARATE_RUNTIME_TRANCHE`: runtime/provider/live/MCP/direct-interception scope.
  - `STRATEGIC_OPERATOR_DECISION`: CGE-T3 and ACE-R1 remain parked.
  - `OUT_OF_SCOPE`: runtime/provider/live/public-sync/direct interception.
- Semantic sampling status: targeted to the three advisory packets and source
  files named above.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | Worker-experience friction remains governance-control-plane evidence. |
| CHANGED_DISPOSITION | AAF-T5 changes from read-receipt first to worker-experience capture first. |
| NEW_FINDING | Worker-return packets need explicit experience token or falsifiable no-friction assertion. |
| REMOVED_OR_REJECTED | Runtime/provider/live/public-sync/direct-interception scope remains rejected. |

### Follow-Up Routing Matrix

| Lane | Disposition |
|---|---|
| DO_NOW | AAF-T5 Worker Experience Retrospective Capture Foundation. |
| RESOLVED_BY_DESIGN | Keep T5 as a capture sensor and defer read receipt/helper drift. |
| DEFER | AAF-T6 Guard Orientation Read-Receipt Gate. |
| SEPARATE_RUNTIME_TRANCHE | Runtime/provider/live/MCP/direct-interception work requires separate authorization. |
| STRATEGIC_OPERATOR_DECISION | CGE-T3 and ACE-R1 remain parked. |
| OUT_OF_SCOPE | Public readiness, production readiness, universal governed-coding control. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AAF-T5-CLS-RS1 | Returned advisory Q2 | KEYWORD_TRAP is frequent | DO_NOW enum | Could it be folded into GATE_SURPRISE? | PASS_EXPLICIT_ENUM_ACCEPTED |
| AAF-T5-CLS-RS2 | Returned advisory Q4 | `push` drift exists | DEFER AAF-T7 | Could T5 fix helper modes? | PASS_SCOPE_DEFERRED |
| AAF-T5-CLS-RS3 | Operator finding | worker pass can hide friction | DO_NOW checker | Could reviewer questioning be enough? | PASS_MACHINE_CHANNEL_REQUIRED |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T5 classification and dispatch routing only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | local documentation/source classification only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | worker-experience capture classification only |
| forbiddenExpansion | read-receipt enforcement, runtime/provider/live, public-sync, direct interception, queue/daemon, readiness, and universal control remain parked |

## Agent Operation Trace Block

| Field | Value |
|---|---|
| Actor | Codex reviewer/orchestrator role |
| Provider or surface | local workspace |
| Session or invocation | current Codex session |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | local file reads, `rg`, governance gates, `apply_patch` |
| Target paths | this classification packet |
| Allowed scope source | operator instruction and AAF-T5 dispatch authoring |
| Before status evidence | dispatch base `8f8bc2d5` with advisory files uncommitted |
| After status evidence | classification created for AAF-T5 dispatch |
| Diff evidence | `git diff --check` required before commit |
| Approval boundary | classification and dispatch only; no implementation |
| Claim boundary | no runtime/provider/live/public-sync/direct-interception claim |
| Agent type | reviewer/orchestrator |
| Invocation ID | local-session-2026-06-20-aaf-t5-dispatch |
| Expected manifest | this classification; AAF-T5 baseline; AAF-T5 work order; three advisory input files |
| Actual changed set | checked by git status and autorun gates before commit |
| Manifest delta | none expected beyond AAF-T5 dispatch/advisory packet normalization |

## Claim Boundary

This classification may claim only that the worker-experience blind spot has
been accepted and routed into AAF-T5 dispatch, with T6 and T7 separated. It does
not implement a checker, modify helper code, close any tranche, prove runtime
behavior, authorize provider/live calls, public-sync, direct interception,
wrapper/proxy enforcement, queue/daemon execution, readiness, or universal
governed-coding control.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance classification for a governed dispatch packet. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

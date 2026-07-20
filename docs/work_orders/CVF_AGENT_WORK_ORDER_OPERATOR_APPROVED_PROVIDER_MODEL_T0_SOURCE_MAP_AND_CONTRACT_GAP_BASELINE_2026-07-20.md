# CVF Agent Work Order - Operator-Approved Provider Model T0 Source Map And Contract Gap Baseline

Memory class: governed-worker-dispatch

Status: REVIEWER_ACCEPTED_DISPATCH_READY_WITH_REPAIRS

Batch ID: OPM-AIR-T0

Dispatch base head: 683543e49

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: worker role (operator-assigned current worker: Claude)

Reviewer/closer: reviewer/closer role (operator-assigned current reviewer/closer: Codex)

Worker return path: `docs/reviews/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_T0_WORKER_RETURN_2026-07-20.md`

## Dispatch Prompt Envelope

Role: delegated worker for CVF-OPM-AIR T0, acting under `WORKER_MUST_NOT_COMMIT`.

Canonical packet: this work order, paired with
`docs/baselines/CVF_GC018_OPERATOR_APPROVED_PROVIDER_MODEL_T0_SOURCE_MAP_AND_CONTRACT_GAP_BASELINE_2026-07-20.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: reviewer supplies the final committed dispatch/session-sync
HEAD in the worker prompt; worker captures it with `git rev-parse --short HEAD`
and requires an exact match before the first edit.

Current-time notes: artifact date is 2026-07-20; the dispatch base head is
`683543e49`; the worker must re-verify the worktree is clean before starting.

Do-not-misread notes: this work order does not authorize T1-T5 implementation
of any roadmap contract field, does not authorize any credential use or
provider call, does not authorize public-sync, push, or deployment, and does
not authorize the worker to commit. The worker inspects current source and
existing secret-safe session metadata only; it must not expose prompts,
responses, credentials, or provider-private payloads in any output.

Required first actions: read `CVF_SESSION_MEMORY.md`,
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, the active handoff, guard
orientation, the literal-format gotchas reference, this work order, the
paired GC-018 baseline in full, and every checker source listed in the
Checker Source Read-Ahead Block below before writing any output artifact.

Return contract: create exactly the three authorized output artifacts, run
the required gates, leave all changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Execute CVF-OPM-AIR T0: produce a source-verified contract-gap ledger, an
operator usage-measurement baseline, and a worker return, each strictly
inside the boundaries the paired GC-018 baseline already establishes. This
tranche is documentation and source-inspection only. It does not implement
any Group A-D field, does not use a credential, does not call a provider, and
does not run live proof.

## Scope / Target / Owner Boundary

Target: exactly the three no-commit worker outputs under `docs/reviews/`
named in this work order. Owner: this work order and the paired GC-018
baseline own the CVF-OPM-AIR T0 dispatch lane; full Allowed/Forbidden detail
is in `4. Scope` below.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id OPM-AIR-T0 --title "Operator-Approved Provider Model T0 Source Map And Contract Gap Baseline" --date 2026-07-20 --base 683543e49 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold placeholder file names with the operator-directed exact baseline/work-order/worker-return paths; resolved every scaffold placeholder field; added the full Roadmap-to-Work-Order Trace Matrix, System Loop Interlock Routing, and Operator Checkpoint sections the generic scaffold leaves as stubs |
| checkerReadAheadConfirmation | see Checker Source Read-Ahead Block below |
| docOnlyNewFields | none introduced by this work order beyond those already listed `DOC_ONLY_NEW` in the paired GC-018 Contract Gap Reconciliation Matrix |
| claimBoundary | dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Source Verification Block; Checker Source Read-Ahead Block; External Knowledge Intake Routing; Foundation Storage Layout Block; Reviewer Closure Conversion; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm reviewer-repaired packet structure and source boundaries as evidence before implementation dispatch |
| claimBoundary | checker compliance confirms packet shape only; it does not prove worker execution or provider behavior |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| durableFoundationChange | NO |
| existingOwnerReuse | current Model Gateway registry, capability, routing, quota, receipt, credential, fallback, and execution owners are read-only inputs |
| newDurableOwner | N/A with reason: T0 produces dated review evidence only |
| indexOrFrontDoorImpact | N/A with reason: no foundation owner or stable front door is added, split, moved, or refactored |
| generatedAggregateImpact | N/A with reason: no generated aggregate changes |
| claimBoundary | dated T0 evidence does not become a new runtime or foundation owner |

## 1. Mission

Dispatch a no-commit worker to produce three source-verified,
documentation-only artifacts for CVF-OPM-AIR T0: a contract-gap ledger that
carries the GC-018 Contract Gap Reconciliation Matrix forward into a
reviewable finding ledger, an operator usage-measurement baseline that
applies the GC-018 measurement-class boundary to a real deduplicated Claude
CLI JSONL extraction, and a worker return that records evidence, gate
results, and an after-tranche findings/learning report. Success means all
three artifacts exist, are internally consistent with the GC-018 baseline,
pass the worker-return fast gate, and remain uncommitted for reviewer
acceptance.

## 2. Authority Chain

- Operator instruction: CVF-OPM-AIR T0 dispatch prompt, 2026-07-20
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Decision pack / review authority: `AGENT_HANDOFF_V49_2026-07-20.md`,
  `CVF-OPM-AIR T0 Packet Authoring Authorization` section
- Roadmap: `docs/roadmaps/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_ASSIGNMENT_AND_INVOCATION_RECEIPT_ROADMAP_2026-07-20.md`
- Roadmap design-control gate: roadmap `Design Control Gate` section
- Spec / contract / machine-readable semantics: N/A with reason: T0 has no
  machine-readable schema of its own; it produces documentation artifacts only
- GC-018 requirement: already filed at
  `docs/baselines/CVF_GC018_OPERATOR_APPROVED_PROVIDER_MODEL_T0_SOURCE_MAP_AND_CONTRACT_GAP_BASELINE_2026-07-20.md`
- Active handoff: `AGENT_HANDOFF_V49_2026-07-20.md`

Authority boundary: this work order does not authorize work outside this
authority chain. If any authority artifact conflicts with this work order,
the worker must stop and return to the reviewer/closer before implementation.

## 3. Agent Roles

- Orchestrator / dispatcher: dispatch author (operator-assigned: Claude, this
  authoring turn)
- Implementer: worker (operator-assigned: Claude, after reviewer acceptance)
- Reviewer: reviewer/closer (operator-assigned: Codex)
- Operator approval required for: any T1-T5 implementation dispatch, any
  credential use or provider call, any public-sync, push, or deployment
  action, and any release of a `HOLD_*` prerequisite

## 4. Scope

Allowed scope:

- read current source under `EXTENSIONS/CVF_MODEL_GATEWAY/src/` and any
  adjacent file needed to verify a claim already made in the GC-018 baseline;
- read existing secret-safe CVF session/handoff/roadmap metadata;
- read local Claude CLI JSONL usage logs already present on the operator's
  machine, extracting only token-count and timing fields, never prompt or
  response text;
- create exactly the three authorized output artifacts listed below;
- run the listed governance gates and repair allowed-scope failures.

Forbidden scope:

- editing any file under `EXTENSIONS/CVF_MODEL_GATEWAY/`, `governance/compat/`,
  `CVF_SESSION/**`, or any `AGENT_HANDOFF*.md`;
- using any credential, API key, or account-subscription session;
- calling any provider, running any live proof, or invoking any CLI/MCP
  execution surface beyond local read-only inspection;
- creating any file other than the three authorized outputs;
- committing any change;
- public-sync, push, or deployment;
- copying raw prompt text, raw response text, or any credential value into an
  output artifact.

Risk ceiling:

- R0 (Safe)

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Worker execution (WORKER_MUST_NOT_COMMIT)`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects (`--max-results 50`, `--json`; see command output below):

| defectId | One-line avoidance note for this dispatch |
| --- | --- |
| ADIF-0001 | The contract-gap ledger cites only files this worker directly reads; no exhaustive-directory claim is made without listing the actual files read |
| ADIF-0002 | No provider-local memory file is cited as CVF source authority in any of the three outputs |
| ADIF-0006 | Source Verification `Verified path or symbol` cells in the worker's outputs must be bare symbols, never value/type annotations |
| ADIF-0014 | Corpus Completeness, Rescan Intelligence, and Mandatory Blind-Spot Control blocks are required in each output with explicit dispositions, not silence |
| ADIF-0020 | Worker must read applicable checker source for each output's `docType` before writing the first section, per the Worker Output Checker Read-Ahead Mandate below |
| ADIF-0021 | No applicability-marker string for another guard family is used loosely in the three worker outputs; each conditional section uses the guard's own safe vocabulary |
| ADIF-0007 | Gate-marker vocabulary is used only in its literal phase-gate sense in the three worker outputs, not as unrelated boundary prose |
| ADIF-0022 | Worker must avoid literal evidence-row false positives (bare directory-path substrings, quoted real headings, proximity trigger phrases) in the three outputs |
| ADIF-0023 | Worker must derive each output's required checker shape from checker source directly, per the Worker Output Checker Read-Ahead Mandate below, not assume the dispatch packet checklist alone is sufficient |
| ADIF-0024 | Worker must rerun every required command after the last edit and record actual results, not stale placeholder values |
| ADIF-0039 | Worker Return Packet Shape Contract below names `run_worker_return_fast_gate.py` explicitly |

## 5. Required First Reads

Before creating any output artifact, read:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V49_2026-07-20.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/roadmaps/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_ASSIGNMENT_AND_INVOCATION_RECEIPT_ROADMAP_2026-07-20.md`
- `docs/baselines/CVF_GC018_OPERATOR_APPROVED_PROVIDER_MODEL_T0_SOURCE_MAP_AND_CONTRACT_GAP_BASELINE_2026-07-20.md`
- this work order
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`
- `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`
- `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`

## 6. Pre-Flight Checks

Commands to run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_adif_defect_registry_disclosure.py --base <executionBaseHead> --head HEAD --enforce
```

Expected results:

- HEAD exactly matches the reviewer-supplied `executionBaseHead` and
  `git status --short` is empty before the worker adds its three outputs;
- pre-implementation autorun gate PASS on the same range;
- dispatch-quality and ADIF-disclosure gates PASS.

If a pre-flight check fails, the worker stops and records the failed command
and result. The worker must not continue past a failed autorun phase gate.

Mandatory Gate-Failure Remediation Protocol: allowed-scope failures (missing
`N/A with reason`, stale closure residue, source-verification corrections,
routine guard failures inside this work order's Allowed scope) are mandatory
remediation, not operator-preference questions. Escalation is reserved for
remediation that would exceed Allowed scope, change claim boundary, release a
`HOLD_*` prerequisite, open public-sync, run live/provider proof, consume
secrets/quota, touch a forbidden path, or perform a destructive action.

Staging and checker-source rule: before running any staged-index check,
stage the intended file set with `git add <paths>`. Working-tree-aware gates
may be used for pending worker artifacts before staging; record that status
as pending, not clean closure.

## 6A. Source-Fidelity Pass

### Source Verification Block

The paired GC-018 baseline already carries a full Source Verification Block
covering `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`,
`provider-capability-registry.ts`, `dynamic-model-registry-contract.ts`,
`routing-policy.ts`, `quota-ledger.ts`, `gateway-receipt.ts`,
`credential-boundary.ts`, `fallback-policy.ts`,
`unified-gateway-interface-contract.ts`, and
`provider-execution-bridge.ts`, plus the archived live-run diagnostic
standard and the CVF-OPM-AIR roadmap. The worker must re-verify every ACCEPT
row against current HEAD immediately before citing it in the contract-gap
ledger, since source may have drifted between dispatch and execution.

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Gateway response exposes provider/model identity and token usage | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | `GatewayExecuteResponse` interface | `model`; `usage` | unified gateway interface contract | ACCEPT |

Provider-local Claude JSONL is `NOT_CVF_SOURCE` and is excluded from this
Source Verification Block. Its `message.id` and nested usage fields are
secret-safe operational measurement inputs only; their observed presence does
not establish a canonical CVF runtime contract.

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | YES (the GC-018 Contract Gap Reconciliation Matrix states which Group A-D fields are absent from current Model Gateway runtime) |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | WORKER_MUST_RECOMPUTE_AT_EXECUTION |
| reason | source may drift between this dispatch-authoring turn and worker execution; the worker must re-open every file in the GC-018 Source Verification Block and confirm each cited symbol still exists at the worker's own `executionBaseHead` before citing it in the contract-gap ledger |
| requiredFutureAction | worker records any drift found in the contract-gap ledger's own Current Runtime Freshness Verification section, using the same EXISTS/VALUE_SET/LITERAL_INVARIANT/RUNTIME_BEHAVIOR/DOC_ONLY_NEW vocabulary |

## Evidence Reuse And Encoding Plan

| Field | Value |
| --- | --- |
| verificationMode | RECOMPUTE_REQUIRED |
| priorVerificationArtifact | N/A with reason: `verificationMode` is `RECOMPUTE_REQUIRED` |
| priorVerificationAnchor | N/A with reason: `verificationMode` is `RECOMPUTE_REQUIRED` |
| recomputeReason | the GC-018 baseline's Source Verification Block was authored at `683543e49`; the worker executes at a later `executionBaseHead` and must recompute against current source rather than reuse a stale prior verification |
| freshRecomputeRequired | YES |
| unicodePathHandling | N/A with reason: this tranche reads only ASCII-named repository source paths and local CLI JSONL fields; no Unicode-path or extracted-text evidence class applies |
| extractedTextAuthority | N/A with reason |

Scalar field restatement (required by the field-line parser in addition to
the table above):

verificationMode: RECOMPUTE_REQUIRED
priorVerificationArtifact: N/A with reason
priorVerificationAnchor: N/A with reason
recomputeReason: the GC-018 baseline Source Verification Block was authored at dispatch base head 683543e49; the worker executes at a later executionBaseHead and must recompute directly against current source rather than reuse a stale prior verification
freshRecomputeRequired: YES
unicodePathHandling: N/A with reason - every path read in this tranche is a literal ASCII repository path read directly with a UTF-8-safe reader; no Unicode-path or extracted-text evidence class applies
extractedTextAuthority: N/A with reason

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| Produce a fresh GC-018 that maps every proposed field to an existing owner, an extension seam, or a doc-only proposal | already satisfied by the paired GC-018 baseline | GC-018 `Contract Gap Reconciliation Matrix` | manual review against roadmap Groups A-D | PASS |
| Reconcile Model Gateway, control plane, execution plane, agent handoff, live diagnostics, and receipt-envelope owners | already satisfied by the paired GC-018 baseline | GC-018 `Source Verification Block` | direct source read | PASS |
| Explicitly reject duplicate registry, bridge, credential, and receipt owners | already satisfied by the paired GC-018 baseline | GC-018 `Baseline Decision` | manual review | PASS |
| Packet must include the operator usage snapshot measurement boundary | already satisfied by the paired GC-018 baseline | GC-018 `Operator Usage Baseline Snapshot And Measurement Classification` | manual review | PASS |
| Packet must include exact CLI usage extraction and deduplication requirements | already satisfied by the paired GC-018 baseline; applied by the worker | GC-018 `Deduplicated Claude CLI JSONL Measurement Requirement`; worker output 2 (usage measurement baseline) | worker deduplicates by unique `message.id` | PENDING_WORKER_EXECUTION |
| Packet must include the five-stage role sequence | already satisfied by the paired GC-018 baseline | GC-018 `Role Sequence` | manual review | PASS |
| Packet must include after-tranche finding/learning reporting | this section, 9. Evidence Requirements, 10. Acceptance Criteria | worker output 3 (worker return) `Reviewer Findings Repaired` and `Learning Candidates For Operator Review` sections | worker-return fast gate plus manual reviewer read | PENDING_WORKER_EXECUTION |
| T0 must not implement, credential-use, provider-call, or public-sync | 4. Scope Forbidden scope | all three outputs | `git diff --name-status`; `git status --short` | PENDING_WORKER_EXECUTION |
| T1 cannot dispatch until T0 closes and names extension seams | already satisfied by the paired GC-018 baseline | GC-018 `Baseline Decision` | manual review; T1 dispatch is a separate future packet | PASS |

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside this work order's Allowed scope: reading files named by this work
order, running `git status`, `git diff`, `git rev-parse`, manifest/hash
checks, and the listed governance gates; documentation-format remediation
inside Allowed scope; required evidence-block completion inside Allowed
scope; repeated guard execution after allowed-scope remediation.

Escalation is reserved for actions that would exceed Allowed scope, edit any
source or governance file, run live/provider proof, use secrets/quota,
public-sync, push/publish, change risk or claim boundary, release a `HOLD_*`
prerequisite, touch a forbidden path, or perform a destructive action. If a
machine gate fails inside Allowed scope, the worker repairs and reruns rather
than asking whether to fix it.

## 6C.1 System Loop Interlock Routing

- Upstream loop and output artifact: this CVF-OPM-AIR T0 tranche; output is
  the contract-gap ledger (worker output 1) carrying forward the GC-018
  Contract Gap Reconciliation Matrix.
- Downstream loop and input artifact: a future CVF-OPM-AIR T1 (Approval And
  Assignment Contract) GC-018 baseline and work order, which must consume the
  contract-gap ledger's `DOC_ONLY_NEW` and `EXTENSION_SEAM` rows as its own
  Source Verification input.
- Machine-readable registry, finding packet, or intake path: worker output 1
  itself (`docs/reviews/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_T0_SOURCE_MAP_AND_CONTRACT_GAP_LEDGER_2026-07-20.md`)
  is the finding packet for this loop; there is no separate corpus scan
  registry entry because this tranche is not a corpus scan.
- Routing rule for deferred or blocked findings: every `DOC_ONLY_NEW` row
  routes to T1 or T2 schema design; every `EXTENSION_SEAM` row routes to T1 or
  T2 composition design; no row is dropped without a disposition.
- Claim boundary that blocks autonomous mutation: this routing does not
  create T1 runtime, does not authorize T1 dispatch, and does not itself
  satisfy T1's own required fresh GC-018 and source-verified work order.

## 6D. Pending Artifact Evidence Finality

If the worker leaves the three output artifacts uncommitted for review, it
must not claim `git status --short` is clean. It must record the actual
pending status: exactly three new untracked files under `docs/reviews/`.
The dispatch packet must already be committed before execution. Pending
artifacts must not cite `--base HEAD~1 --head HEAD` or another committed-only
range as proof for themselves.

Commit Mode And Base-Anchor Lifecycle: `dispatchBaseHead=683543e49`;
`executionBaseHead` captured by the worker at start; `closureBaseHead` set by
the reviewer/closer after accepted commit.

Worker Pending-Return Gate: the worker records the worker-return fast gate
result and `git status --short` at `COMPLETE_PENDING_REVIEW` time; the
reviewer/closer owns the committed-range `pre-closure` gate afterward.

Reviewer Closure Conversion Block: see the dedicated section below.

## 6E. Self-Reported Gate Evidence Consistency

If the worker records a governance gate result, it must match the actual
last-run state. If a required gate fails inside Allowed scope, the worker
repairs and reruns before handoff. If the failure cannot be repaired inside
Allowed scope, the worker sets its return to `BLOCKED_WITH_REASON` and names
the return action instead of leaving a non-blocked artifact with a
self-reported failure. The worker updates the recorded Governance Gates Run
result after any repair, before returning the artifact.

## 6E.1 Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this work order | closed-equivalent status only after reviewer/closer closure; no stale residue | N/A with reason: `REVIEWER_ACCEPTED_DISPATCH_READY_WITH_REPAIRS` is dispatch state, not closure |
| Completion or reviewer artifact | worker output 3 (worker return) | final disposition, changed-file evidence, claim boundary, gate evidence | PENDING_WORKER_EXECUTION |
| Roadmap state | `docs/roadmaps/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_ASSIGNMENT_AND_INVOCATION_RECEIPT_ROADMAP_2026-07-20.md` | tranche row final status; roadmap Status remains `T0_PACKET_AUTHORING_AUTHORIZED` until reviewer/closer updates it after commit | N/A with reason: roadmap status update is reviewer/closer-owned after commit |
| Registry JSON | N/A with reason: T0 performs no corpus scan and touches no registry | N/A | N/A with reason |
| Registry Markdown | N/A with reason: T0 performs no corpus scan and touches no registry | N/A | N/A with reason |
| External evidence digest | worker output 2 (usage measurement baseline) | deduplicated CLI JSONL record count, measurement class, generated time, privacy boundary | PENDING_WORKER_EXECUTION |
| System loop interlock | this work order, `6C.1 System Loop Interlock Routing` | upstream/downstream loop, routing rule, mutation boundary | PASS |
| Session continuity | `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, active handoff | mode, next allowed move, handoff HEAD or accepted parent marker | N/A with reason: session continuity update is reviewer/closer-owned after accepted commit |

## 6F. Commit Choreography

Governed per `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`.
The worker does not commit. The reviewer/closer commits the material artifacts
(this work order, the GC-018 baseline, and the three accepted worker outputs)
first, then performs a separate session-sync commit only if mode, next
allowed move, or handoff status changes as a result of this tranche.

### 6F. Near-Threshold Owner Maintainability Plan

N/A with reason: this work order adds no source inside a registered owner
domain; it produces documentation artifacts only.

## 6G. Work-Order Fulfillment Manifest

### Planned Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `docs/reviews/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_T0_SOURCE_MAP_AND_CONTRACT_GAP_LEDGER_2026-07-20.md` | Yes | carries the GC-018 Contract Gap Reconciliation Matrix forward into a reviewable finding ledger with Finding-To-Governance disposition |
| `docs/reviews/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_T0_USAGE_MEASUREMENT_BASELINE_2026-07-20.md` | Yes | applies the GC-018 measurement-class boundary to a real deduplicated Claude CLI JSONL extraction |
| `docs/reviews/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_T0_WORKER_RETURN_2026-07-20.md` | Yes | worker-return packet with evidence, gate results, Reviewer Findings Repaired, and Learning Candidates For Operator Review |

### Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `EXTENSIONS/CVF_MODEL_GATEWAY/**` | T0 is documentation and source-inspection only; no runtime edit is authorized |
| `governance/compat/**` | no checker/guard change is authorized by this work order |
| `CVF_SESSION/**` | session-state mutation is reviewer/closer-owned after accepted commit |
| `AGENT_HANDOFF*.md` | handoff mutation is reviewer/closer-owned after accepted commit |

### Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
| --- | --- | --- | --- |
| `docs/reviews/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_T0_SOURCE_MAP_AND_CONTRACT_GAP_LEDGER_2026-07-20.md` | ABSENT | ABSENT (verified `test -f`, `NOT_EXISTS`) | N/A |
| `docs/reviews/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_T0_USAGE_MEASUREMENT_BASELINE_2026-07-20.md` | ABSENT | ABSENT (verified `test -f`, `NOT_EXISTS`) | N/A |
| `docs/reviews/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_T0_WORKER_RETURN_2026-07-20.md` | ABSENT | ABSENT (verified `test -f`, `NOT_EXISTS`) | N/A |

### Pre-Existing Dirty Path Exemptions

N/A with reason: `git status --short` was clean at dispatch base head
`683543e49` before this work order and its paired GC-018 baseline were
created; no pre-existing dirty path requires exemption.

### Planned Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| worker-return fast gate pass | worker output 3 | `COMPLETE_PENDING_REVIEW` | Yes |
| deduplication by unique message.id | worker output 2 | `message.id` | Yes |
| no raw credential/prompt/response text | all three outputs | N/A with reason: this is a negative/absence proof, not a positive literal | Yes |

## 7. Write Ownership

Owned files or modules:

- `docs/reviews/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_T0_SOURCE_MAP_AND_CONTRACT_GAP_LEDGER_2026-07-20.md`
- `docs/reviews/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_T0_USAGE_MEASUREMENT_BASELINE_2026-07-20.md`
- `docs/reviews/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_T0_WORKER_RETURN_2026-07-20.md`

Forbidden paths:

- everything named in the Forbidden Path Manifest above

Write mode: create-only.

Any file outside ownership requires an updated work order or operator
approval. If the closure diff shows files outside Allowed scope, the worker
must stop and return to the reviewer/closer.

## 7A. Protected-Path Authorization Carrier

N/A with reason: this work order authorizes no `governance/compat/*.py`
checker, no `CVF_SESSION/**` state/handoff file, no `CVF_SESSION_MEMORY.md`
edit, and no `AGENT_HANDOFF*.md` edit. No Core Guard Self-Protection
Authorization block is required.

## 8. Execution Plan

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`; compare it
   exactly with the reviewer-supplied final dispatch/session-sync HEAD and
   confirm `git status --short` is empty. Validation: command output recorded.
   Stop condition: HEAD mismatch or any dirty path.
2. Read every file in `5. Required First Reads` in full.
   Validation: worker return `Source Inventory` table lists each path with a
   `READ` or `FULL_READ` action token. Stop condition: any required read is
   skipped.
3. Re-verify every `ACCEPT` row in the GC-018 Source Verification Block
   against current HEAD.
   Validation: no drift found, or drift explicitly recorded. Stop condition:
   a cited symbol no longer exists at current HEAD and is not corrected.
4. Author the contract-gap ledger (worker output 1), carrying the GC-018
   Contract Gap Reconciliation Matrix forward with a
   `Finding-To-Governance Learning Disposition` section per field group.
   Validation: `check_markdown_structural_completeness.py` review-type
   headings present. Stop condition: any Group A-D field is missing a
   disposition.
5. Extract deduplicated Claude CLI JSONL usage by unique `message.id` from
   exact session basenames `fe820583-4b33-480e-b9d3-14451324dc23.jsonl` and
   `3788ceeb-8aac-415b-a2c9-6e7dc1b01edf.jsonl`, without copying
   prompt or response text, and author the usage-measurement baseline
   (worker output 2) using the GC-018 measurement-class vocabulary.
   Validation: per-`message.id` `input_tokens`, `cache_creation_input_tokens`,
   `cache_read_input_tokens`, `output_tokens` recorded; unique API response
   count computed from distinct `message.id`, not raw JSONL line count. Mark
   JSONL `NOT_CVF_SOURCE`; record the packet-author diagnostic
   `CALLER_TIMEOUT_CHILD_CONTINUED_REVIEWER_STOPPED`. Stop
   condition: local JSONL is unavailable; record
   `NOT_AVAILABLE_WITH_REASON` for that measurement class instead of
   fabricating a value.
6. Author the worker return (worker output 3) with evidence, gate results,
   `Reviewer Findings Repaired`, and `Learning Candidates For Operator
   Review` sections.
   Validation: worker-return fast gate PASS. Stop condition: fast gate fails
   outside Allowed scope.
7. Run the Verification Commands in `9. Evidence Requirements` and repair any
   allowed-scope failure.
   Validation: commands recorded with actual results. Stop condition: a
   failure outside Allowed scope remains after one repair attempt.
8. Return `COMPLETE_PENDING_REVIEW` with `git status --short` showing the
   three new untracked files, or `BLOCKED_WITH_REASON` naming the blocker.

## 8A. Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
| --- | --- | --- | --- |
| Scope boundary | roadmap `Scope / Target / Owner Boundary` | `4. Scope` mirrors the roadmap's T0 in-scope/out-of-scope split | PASS |
| Non-goals | roadmap `Non-Goals` | `4. Scope` Forbidden scope excludes default-provider, replacement-owner, and live-proof actions | PASS |
| Lane split | roadmap `Work Plan` T0 row | this work order executes only T0; T1-T5 remain parked | PASS |
| Dependency/source-verification plan | roadmap `Source Verification Block` | `6A. Source-Fidelity Pass` requires re-verification against current HEAD | PASS |
| Claim boundary | roadmap `Claim Boundary` | this work order's `Claim Boundary` section below inherits the same no-implementation, no-credential, no-provider-call boundary | PASS |
| Acceptance criteria | roadmap `Acceptance Criteria` | `10. Acceptance Criteria` below traces each roadmap checkbox | PASS |
| Verification/evidence | roadmap `Verification Strategy` | `9. Evidence Requirements` below | PASS |
| Dispatch-readiness decision | roadmap `Tranche Release Rules` | T0 has no predecessor tranche; T1 remains gated on this T0 closing | PASS |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatch author (operator-assigned current actor: Claude) |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-OPM-AIR T0 packet authoring, 2026-07-20 |
| Working directory | repository root |
| Command or tool surface | direct source reads, repository search, governed file writes, governance gates |
| Target paths | this work order; the paired GC-018 baseline |
| Allowed scope source | `AGENT_HANDOFF_V49_2026-07-20.md` `CVF-OPM-AIR T0 Packet Authoring Authorization` section |
| Before status evidence | clean worktree at `683543e49` |
| After status evidence | two new untracked governed files; no other path changed |
| Diff evidence | `git status --short` showing exactly two untracked paths |
| Approval boundary | dispatch-authoring only |
| Claim boundary | repo-local trace only; no runtime, provider, live, public-sync, push, or production claim |
| Agent type | dispatch author |
| Invocation ID | `cvf-opm-air-t0-work-order-authoring-2026-07-20` |
| Expected manifest | this work order; the paired GC-018 baseline |
| Actual changed set | this work order; the paired GC-018 baseline |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this batch |

## 8C. Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: applying the GC-018 measurement-class boundary
to a real local Claude CLI JSONL extraction will find at least one qualifying
session record, since the operator was actively running this exact T0 packet
authoring session with the CLI in the foreground.

Evidence Comparison Requirement: worker return compares the actual JSONL
extraction result (record found and deduplicated, or absent with reason)
against this prediction.

Contradiction Handling Requirement: if no local JSONL record is found, the
worker return must record `NOT_AVAILABLE_WITH_REASON` for the
`CLI_USAGE_EXACT_ACCOUNT_QUOTA_UNKNOWN` class and state a Contradiction Or Gap
Disposition explaining why, rather than substituting an estimate.

Claim Update Requirement: worker return records whether the measurement
prediction was confirmed, revised, narrowed, or invalidated.

## 9. Evidence Requirements

Required evidence:

- `git status --short` before and after worker execution;
- worker-return fast gate result;
- Evidence Trace Block for the JSONL deduplication claim;
- complete Agent Operation Trace Block in the worker return.

Evidence Trace Block requirements:

- Claim: local Claude CLI JSONL usage logs were extracted and deduplicated by
  unique `message.id`.
- Command: worker records the exact extraction command used.
- Result: unique API response count and per-`message.id` token fields.
- Key path: local log path class (not raw path if it would expose
  operator-machine-specific personal data beyond what is already CVF-safe).
- Verdict: `EXISTS`, `ABSENT`, or `PARTIAL`.

Base-anchor evidence:

- `dispatchBaseHead`: `683543e49`
- `executionBaseHead`: captured by the worker at start
- `closureBaseHead`: N/A - pending review
- Commit mode: `WORKER_MUST_NOT_COMMIT`
- Pending-artifact component gates: worker-return fast gate;
  pre-implementation autorun gate on the worker's own changed set
- Worker Pending-Return Gate table: recorded in the worker return
- Worker-return fast gate:
  `python governance/compat/run_worker_return_fast_gate.py`
- Committed-range `pre-closure`: N/A - pending review

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## 10. Acceptance Criteria

- [ ] Contract-gap ledger carries forward every Group A-D field disposition
  from the GC-018 baseline with a Finding-To-Governance Learning Disposition
- [ ] Usage-measurement baseline deduplicates by unique `message.id` and uses
  only the five GC-018 measurement classes, with no cross-class conversion
- [ ] Worker return includes `Reviewer Findings Repaired` and `Learning
  Candidates For Operator Review` sections
- [ ] All three outputs remain uncommitted; worker did not commit
- [ ] No credential, provider call, live proof, or public-sync action occurred

Fail conditions:

- [ ] any output presents a `DOC_ONLY_NEW` field as existing runtime
- [ ] any output converts an `OPERATOR_UI_SNAPSHOT` or
  `SUBSCRIPTION_LIMIT_EVENT_ONLY` value into a token count or dollar figure
  without a source-backed conversion rule
- [ ] any output contains raw prompt text, raw response text, or a credential
  value
- [ ] the worker commits any change

Closure is blocked if any fail condition is present.

## 11. Review Gate

Implementation may proceed only after:

- GC-018 filed (already satisfied by the paired baseline)
- `pre-dispatch` autorun gate passed before dispatch
- `pre-implementation` autorun gate passed before material edits

Closure may proceed only after:

- reviewer/closer no-blocking objection
- `pre-closure` autorun gate passed and result recorded

For `WORKER_MUST_NOT_COMMIT` mode, worker handoff is not closure. The
reviewer/closer approves disposition, commits the reviewed owned diff, and
runs the committed-range `pre-closure` gate before changing status to a
closed-equivalent value.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_T0_WORKER_RETURN_2026-07-20.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, section names
are written without the heading prefix. Reserve actual markdown heading
syntax for real sections so structural checkers do not treat this checklist
as the artifact section body.

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for
that file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| contract-gap ledger under `docs/reviews/` | derive the five review heading groups (target/source, scope/methodology, findings/position, risk/corrective action, decision/recommendation/disposition), plus a Finding-To-Governance Learning Disposition section since it carries a table whose first practical column is a per-field finding |
| usage-measurement baseline under `docs/reviews/` | derive the five review heading groups; include the Deduplicated Claude CLI JSONL Measurement Requirement fields and measurement-class vocabulary exactly as named in the GC-018 baseline |
| worker return under `docs/reviews/` | derive exact review headings, worker-return quality terms, trace labels, Delta boundary labels, and no-commit evidence shape; include Reviewer Findings Repaired and Learning Candidates For Operator Review sections named by this work order |

Literal-shape reminders: do not list required headings as backticked `## ...`
strings before the real section; write source-not-found disposition spelling
instead of the exact blocked enum in any `literalTokensReviewed` field; avoid
`after ... closure` wording unless a dependency-release row cites the
accepted artifact path and commit.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | roadmap-author role transitions to reviewer role, then to reviewer/closer role; dispatch-author role transitions to worker role under `WORKER_MUST_NOT_COMMIT` only after the reviewer role accepts the dispatch |
| phase | pre-implementation through worker `COMPLETE_PENDING_REVIEW` |
| baseHeadFor(phase) | dispatchBaseHead=683543e49; executionBaseHead=reviewer-supplied committed dispatch/session-sync HEAD verified by worker; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exactly the three authorized `docs/reviews/` outputs; no other path |
| traceScope(phase, actor) | worker's Agent Operation Trace Block in the worker return covers only the three outputs it creates |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns the material commit after acceptance |
| crossBatchIsolation | this batch does not touch Continuous Projection, MAO, SOT3, or any other active lane |
| nextMoveSurfaces | `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, and `AGENT_HANDOFF_V49_2026-07-20.md` are reviewer/closer-owned after accepted commit; the worker does not edit them |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_T0_COMPLETION_REVIEW_2026-07-20.md` |
| reviewerOwnedClosurePaths | paired baseline; this work order; roadmap; completion review; separate session continuity sync |
| closureOwner | reviewer/closer role (operator-assigned current actor: Codex) |
| workerCommitPermission | FORBIDDEN |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | CVF-OPM-AIR T0 documentation and source-inspection tranche only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: source verification is bounded to the files directly read and cited in the GC-018 baseline and this work order |
| receiptEvidence | N/A with reason: this tranche produces no runtime receipt envelope |
| actionEvidence | N/A with reason: no runtime action is executed; evidence is `git status`/`git diff` and direct file reads only |
| invocationBoundary | governed local document authoring and read-only source inspection; no broader claim |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | this work order dispatches a no-commit worker to author three documentation artifacts; it does not execute, deploy, or invoke any provider |
| forbiddenExpansion | no runtime edit, credential use, provider call, live proof, public-sync, push, or deployment is authorized by this work order |

## Operator Checkpoint

Operator involvement is required before: any T1-T5 implementation dispatch
for a roadmap contract group; any credential use or provider call under this
or any successor packet; any public-sync, push, or deployment action; release
of any future `HOLD_*` prerequisite; or if source-fidelity re-verification
during worker execution finds a conflict that would require a duplicate
registry, bridge, credential, or receipt owner. Operator silence is not a
waiver for any of these conditions.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | NOT_APPLICABLE_WITH_REASON: T0 verifies repository-local source and measures provider-local usage metadata without absorbing it as CVF authority |
| Matching local-view guard | N/A with reason: repository source is re-read directly; JSONL remains `NOT_CVF_SOURCE` operational evidence |
| Owner surface | paired baseline, this work order, and T0 usage-measurement output |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | no prompt, response, credential, provider-private payload, or external semantic claim is promoted |

## Intake Role Routing Decision

Route mode: MULTI_AGENT_MULTI_ROLE.

Intake summary: this tranche originates from an explicit operator request
recorded in `AGENT_HANDOFF_V49_2026-07-20.md`, not from an unscoped raw
request; the operator directed the exact five-stage role sequence and the
three output paths this work order authorizes.

Scope classification: bounded scope, allowed scope limited to exactly three
new `docs/reviews/` files; blast radius is documentation-only with zero
changed paths under `EXTENSIONS/CVF_MODEL_GATEWAY/` or `governance/compat/`.

Risk sensitivity: risk ceiling R0; this tranche performs no public-sync, no
provider call, no live invocation, no secret access, and makes no production
or public-readiness claim.

Escalation condition: any conflict, source-verification blocker, or scope
question routes to the Operator Checkpoint section below, which names when
operator involvement is required; a failed allowed-scope gate is repaired and
rerun rather than escalated, per the Worker Autonomy / No-Question Rule.

Codex authors and owns the CVF-OPM-AIR roadmap, then acts as reviewer for
this packet, then acts as reviewer/closer after worker execution. Claude
authors this dispatch packet, then acts as worker under
`WORKER_MUST_NOT_COMMIT` only after Codex accepts and commits the dispatch.
No single agent self-authorizes its own move to the next role; each
transition requires the prior role's accepted, committed artifact.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this work order does not absorb, reopen, or
implement knowledge from any legacy source folder, archived absorption
packet, or the legacy absorption coverage index. It composes current
`EXTENSIONS/CVF_MODEL_GATEWAY/src/` source directly read in this session and
the operator-approved CVF-OPM-AIR roadmap. It mentions Model Gateway,
control-plane, execution-plane, and Agent Operation Trace vocabulary only in
the ordinary sense of the current provider-neutral roadmap and this work
order's own required trace block, not as legacy-coverage scope.

## 12. Closure Checklist

- [ ] All acceptance criteria satisfied or explicitly marked N/A with reason
- [ ] Required tests or evidence commands run
- [ ] Autorun `pre-closure` gate passed:
  `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <closureBaseHead> --head HEAD`
- [ ] Commit mode recorded as `WORKER_MUST_NOT_COMMIT`
- [ ] `dispatchBaseHead`, `executionBaseHead`, and closure-stage base evidence
  recorded without treating a stale dispatch anchor as current worker proof
- [ ] For `WORKER_MUST_NOT_COMMIT`, pending handoff used a non-closed status,
  recorded actual `git status --short`, and left committed-range
  `pre-closure` to the reviewer/closer
- [ ] For `WORKER_MUST_NOT_COMMIT`, Worker Pending-Return Gate results are
  recorded and remaining failures are explicitly `BLOCKED`, `N/A with
  reason`, or `FAIL_EXPECTED_PENDING_FINALITY`
- [ ] For `WORKER_MUST_NOT_COMMIT`, worker-return fast gate result is
  recorded
- [ ] Agent Operation Trace Block is present and complete
- [ ] Closure gate uses a non-empty committed diff range after reviewer/closer
  commit, not an identical base-equals-head invocation
- [ ] Changed-file set is inside this work order's Allowed scope
- [ ] Roadmap-to-work-order trace matrix final statuses are PASS or N/A with
  reason after worker execution
- [ ] No open checkbox residue remains after reviewer/closer closure
- [ ] Public catalog N/A with reason (private, unreleased roadmap)
- [ ] Public/provenance repository boundary checked; no public path touched
- [ ] GC-020 handoff updated with current HEAD after reviewer/closer commit
- [ ] Active session front door and state registry updated by the
  reviewer/closer if mode, next allowed move, or handoff status changes

## 13. Return-To-Orchestrator Conditions

Return to the reviewer/closer without continuing if:

- pre-flight fails outside Allowed scope;
- any autorun phase gate fails outside Allowed scope or cannot be repaired
  inside this work order;
- source-fidelity re-verification finds a missing path, invented symbol, or
  unverified role/template mapping;
- local Claude CLI JSONL usage logs are unavailable and no
  `NOT_AVAILABLE_WITH_REASON` disposition can be safely recorded without
  guessing;
- scope conflict is discovered;
- implementation would exceed the R0 risk ceiling;
- public/provenance boundary is unclear.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private dispatch packet for an unreleased provider-neutral
control-plane roadmap. It contains no public-safe implementation or release
evidence and authorizes no public-sync mutation.

## Claim Boundary

This reviewer-repaired and accepted work order authorizes only the CVF-OPM-AIR T0 no-commit worker
execution: creation of exactly the three named `docs/reviews/` outputs from
direct source inspection and existing secret-safe session metadata, with no
runtime edit, credential use, provider call, live proof, public-sync, push,
or deployment. It does not authorize T1-T5 implementation of any roadmap
contract field. It authorizes implementation only after the reviewer commits
this exact dispatch and session-sync anchor; it does not claim T0 closure.

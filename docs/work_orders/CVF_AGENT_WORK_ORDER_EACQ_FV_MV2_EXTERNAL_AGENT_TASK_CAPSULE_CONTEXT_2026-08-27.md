# CVF Agent Work Order - EACQ-FV MV-2 External Agent Task Capsule Context

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Work order ID: EACQ-FV-MV2

Batch ID: EACQ-FV-MV2

Dispatch base head: `22644e47e118bd88bf0d004cb74819fd2956c061`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated bounded implementation worker

Reviewer/closer: designated internal orchestrator/reviewer

Worker return path: `docs/reviews/CVF_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_WORKER_RETURN_2026-08-27.md`

rawMemoryReleased=false

## Dispatch Prompt Envelope

Role: delegated no-commit implementation worker for EACQ-FV-MV2.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_2026-08-27.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

providerExecutionAuthority: FORBIDDEN.

Current-time notes: private provenance repository, 2026-08-27; the operator
continued the roadmap and the value gate selected only MV-2.

Do-not-misread notes: extend the existing task-capsule owner only; no new
protocol, external packet-folder write, mandatory network refresh, roadmap,
MV-3, UAA, provider, public-sync, deployment, push, stage, or commit action is
authorized.

Required first actions: read startup surfaces, every Required First Read, and
the checker sources named below; then prove ancestry, hashes, clean worktree,
empty staging, and run pre-implementation gates.

Return contract: modify exactly five existing implementation/doc/test paths,
create exactly one worker return, run final verification, leave all changes
unstaged and uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Extend the existing external-agent task capsule with four task-proportional
context groups and a deterministic offline, staleness-aware creation path,
while preserving the current live prepare route and strict fail-closed schema.

## Authority Chain

Operator continuation -> revised EACQ-FV roadmap -> accepted MV-1 closure ->
paired MV-2 GC-018 baseline -> this no-commit work order -> independent
reviewer/closer. Worker completion is not closure or successor authority.

## Scope / Target / Owner Boundary

Allowed: the exact six paths in Write Ownership. Forbidden: every other path;
public packet instances and `D:\UNG DUNG AI\EXTERNAL_AGENT_READ`; network or
provider calls; credentials; roadmap/session/standard/hook/catalog mutation;
staging, committing, pushing, publishing, or deployment.

Risk ceiling: R2, local reversible schema/helper change with no external effect.

## Worker Autonomy / No-Question Rule

Inside exact scope, the worker must implement, test, document, and remediate
allowed-scope gate failures without asking the operator. Escalate only for a
source contradiction, required forbidden-path edit, authority expansion,
provider/network/secret/quota action, public effect, destructive action, or
claim-boundary change.

## Agent Roles

- Orchestrator/dispatcher: selects the bounded lane and authors dispatch.
- Worker: implements and tests exactly the six uncommitted paths.
- Reviewer/closer: independently probes semantics, repairs only within bounded
  worker scope if justified, commits accepted material, and syncs continuity.
- Operator: owns any scope expansion, successor, provider, public, deploy, or
  push authority.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R0 revision | governed roadmap records all review dispositions | ACCEPT |
| MV-1 | material `f202f351f`, closure `1e002a52b`, session sync `22644e47e` | ACCEPT |
| operator continuation | explicit instruction on 2026-08-27 | ACCEPT_FOR_MV2_VALUE_GATE |
| current capsule owner | strict schema, Python generator, PowerShell wrapper, README, tests | ACCEPT_AND_EXTEND |
| MV-3 and UAA | no current comparative evidence or reopen trigger | PARKED_NOT_AUTHORIZED |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| four fields only | Required Implementation Contract | four context groups in schema/generator | schema validation and focused assertions | READY |
| named consumers and freshness | Context Group Shape | every group | negative schema cases | READY |
| no mandatory live refresh | Offline Creation Contract | explicit offline CLI/wrapper route | subprocess tests with network/git helpers forbidden | READY |
| backward compatibility | Compatibility Contract | existing prepare route and existing call shape | existing plus new focused tests | READY |
| no measured uplift claim | Claim Boundary | worker return | reviewer semantic check | READY |
| local bounded cost | Verification Commands | six paths, zero provider/network | status/diff and test evidence | READY |

## Required First Reads

1. `AGENTS.md`, `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`,
   `CVF_SESSION_MEMORY.md`, and active handoff.
2. `docs/reference/guard_orientation/README.md` and
   `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
3. The EACQ-FV roadmap, paired MV-2 baseline, and this work order.
4. `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json`.
5. `scripts/external_agent_packet.py`, `scripts/test_external_agent_packet.py`,
   and `scripts/Update-CVF-External-Agent-Packet.ps1`.
6. `docs/reference/external_agent_review/README.md`.
7. Applicable worker-return, reference-structure, trace, task-route, and
   read-ahead checker sources before authoring their target artifacts.

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT --title "EACQ-FV MV-2 External Agent Task Capsule Context" --date 2026-08-27 --base 22644e47e118bd88bf0d004cb74819fd2956c061 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled exact owners, four-group contract, offline source posture, validation-before-write, test matrix, routing, handoff, and no-commit return controls. |
| checkerReadAheadConfirmation | Applicable dispatch checker sources were read before authoring. |
| docOnlyNewFields | N/A with reason: no new doc-only normative field; proposed JSON fields are implementation outputs. |
| claimBoundary | Dispatch authoring provenance only; no implementation or external-effect claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`task capsule implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class "task capsule implementation" --role worker --lifecycle-phase pre-implementation --surface-selector scripts --risk-ceiling MEDIUM --json`.
The dispatch author resolver query also returned no entries and was not
truncated. Any later non-empty result is a mandatory worker-return overlay.

## Pre-Flight Checks

1. Capture `executionBaseHead` and prove the dispatch base is an ancestor.
2. Confirm clean worktree and empty staging before edits.
3. Confirm the worker-return path is absent and the five owners match hashes.
4. Run collision searches and pre-implementation gates.
5. Stop on source drift that changes the contract; do not reset or overwrite.

## Pinned Input Hashes

| Path | SHA-256 |
| --- | --- |
| `docs/roadmaps/CVF_EXTERNAL_AGENT_CODING_QUALITY_AND_FORWARD_VALUE_ABSORPTION_ROADMAP_2026-08-27.md` | `aa1133380ba5b355577a4398d9dfaa8afc8ed23ae2a6d1eac92a903054ee127b` |
| `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json` | `28befe7a7ed4eb69276ae31327f17df5d84b8b7188b41cfa87a83059532748fb` |
| `scripts/external_agent_packet.py` | `d4fa7fefd515131e4de896f3e7339aa38e9a44c878af16acf5f1e08ccd4266c3` |
| `scripts/test_external_agent_packet.py` | `02b1b4a836d1c4972e23783734a5bf47e4ce46cfcbe052ed2326cbf2437bbfe9` |
| `scripts/Update-CVF-External-Agent-Packet.ps1` | `66965ed62cd459f51340e285d5f41aa9a778d7bfdc3dc06db1f70d55ef21c395` |

## Write Ownership

Modify only:

- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json`
- `docs/reference/external_agent_review/README.md`
- `scripts/external_agent_packet.py`
- `scripts/test_external_agent_packet.py`
- `scripts/Update-CVF-External-Agent-Packet.ps1`

Create only:

- `docs/reviews/CVF_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_WORKER_RETURN_2026-08-27.md`

Every other path is read-only. The worker must not stage or commit.

## Required Implementation Contract

### Context Group Shape

Add exactly four root context groups to the existing v1 capsule. Do not rename
the schema or create v2 solely for this additive strict extension.

| Group | Required semantic content | Required metadata |
| --- | --- | --- |
| `protectedPaths` | exact repo-relative paths or path families the worker must not mutate | at least one named consumer and an explicit freshness rule |
| `ownerMap` | current owner paths, symbols, versions when applicable, and competing owners checked | at least one named consumer and an explicit freshness rule |
| `invariants` | must-preserve behaviors and explicit forbidden transitions | at least one named consumer and an explicit freshness rule |
| `verification` | exact focused tests, negative cases, deterministic checks, and required outputs | at least one named consumer and an explicit freshness rule |

Choose the smallest unambiguous JSON shape. Keep `additionalProperties: false`
at every new object boundary. Reject empty strings, empty required lists,
missing groups, unknown keys, unsafe path spellings, and duplicate list items
where applicable. Inputs must be task-specific, not raw reviewer history.

### Consumer And Freshness Semantics

Consumers must be role/interface names used by the packet flow, such as worker,
reviewer, or return validator, not provider names. Each group must carry a
machine-readable freshness rule that says what source anchors it and when it
must be regenerated or rejected. The generator must not invent owner facts or
silently fill missing groups.

### Offline Creation Contract

Add a separate explicit Python CLI route and matching PowerShell mode that
create only the task capsule from an operator-pinned public commit and the
four supplied context groups. This route must not call `refresh_snapshot`, Git
remote commands, network, or read a prior refresh receipt as current truth.

The existing `cvfPublicSource` owner must distinguish:

- live `prepare-task`: verified live public main at creation time;
- offline route: operator-pinned commit, explicitly not live-verified.

Use a deterministic local context JSON input file rather than an unwieldy set
of repeated shell arguments. Validate the input against the governed capsule
schema before writing output. On any invalid context, fail before replacing an
existing capsule; do not leave a partial file.

### Compatibility Contract

Preserve existing `refresh-snapshot`, `prepare-task`, and `validate-return`
behavior and existing caller arguments. The live prepare route may require the
new context JSON because the four groups are mandatory for build/extend coding
tasks; if review/design modes need a proportional exemption, encode an exact
schema-visible rule and tests rather than silently emitting empty groups.

Do not change authorityEnvelope booleans, Gate A/Gate B semantics, return
validation, packet refresh contents, public repository constant, or external
packet files.

### Test Matrix

Tests must include at least:

- strict valid capsule with all four groups;
- each missing group fails;
- empty/unknown/malformed group content fails;
- duplicate or unsafe protected path fails;
- owner path/symbol and competing-owner evidence preserved exactly;
- invariants and forbidden transitions preserved exactly;
- verification positive/negative/deterministic/output items preserved exactly;
- existing live preparation path records live-verified source posture;
- offline path records pinned-not-live-verified posture;
- offline path succeeds while Git/network/refresh helpers are patched to fail
  if invoked;
- invalid offline input does not overwrite an existing capsule;
- existing return-validation tests remain passing;
- PowerShell route/argument construction is source-inspected or tested without
  executing network operations.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| strict current capsule owner | source fact | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json` | root required/properties | `cvf.externalAgentTaskCapsule.v1` | JSON Schema root | ACCEPT |
| current generator | source fact | `scripts/external_agent_packet.py` | `create_capsule` | `create_capsule(args, public_sha)` | packet CLI | ACCEPT |
| live-refresh coupling | source fact | `scripts/external_agent_packet.py` | `main` dispatch | `prepare-task` calls `refresh_snapshot` before `create_capsule` | packet CLI | ACCEPT |
| current wrapper modes | source fact | `scripts/Update-CVF-External-Agent-Packet.ps1` | `ValidateSet` and mode branches | three current modes | PowerShell wrapper | ACCEPT |
| current focused tests | test fact | `scripts/test_external_agent_packet.py` | strict-schema test | `test_generated_task_capsule_matches_strict_schema` | pytest module | ACCEPT |
| four-group roadmap constraint | governed design fact | `docs/roadmaps/CVF_EXTERNAL_AGENT_CODING_QUALITY_AND_FORWARD_VALUE_ABSORPTION_ROADMAP_2026-08-27.md` | External-Agent Coding Context Contract | MV-2 | roadmap | ACCEPT |

## Current Runtime Freshness Verification

Direct reads at dispatch HEAD confirm the current CLI still exposes
`refresh-snapshot`, `prepare-task`, and `validate-return`; the wrapper exposes
the corresponding three modes; the schema has none of the four planned root
groups. This evidence authorizes only the bounded local delta. The worker must
repeat the checks after capturing its execution base and stop on a competing
implementation.

## Negative Search And Collision Discipline

Run:

```powershell
rg -n --fixed-strings "protectedPaths" docs/reference/external_agent_review scripts governance/compat
rg -n --fixed-strings "ownerMap" docs/reference/external_agent_review scripts governance/compat
rg -n "create-capsule|CreateTaskCapsule|offline.*capsule|pinned.*live" docs/reference/external_agent_review scripts governance/compat
```

Current disposition: same-token occurrences outside the task capsule are not
this schema owner; no competing offline capsule-production route was found in
the selected owner files. If a competing current owner appears, return
`BLOCKED_WITH_REASON` rather than creating a parallel protocol.

## Execution Plan

1. Complete preflight, source/hash checks, and collision searches.
2. Design the smallest strict four-group JSON shape and context input format.
3. Update schema and generator atomically, validating before output write.
4. Add the explicit offline CLI and wrapper route without touching live state.
5. Update the owner README and focused tests.
6. Populate the worker return only after the final code/test edit; rerun all
   verification and leave staging empty.

## Acceptance Criteria

All Required Implementation Contract clauses and test cases are mandatory.
The changed set is exactly six paths. Both live and offline source postures are
honest, the offline route makes zero network/Git-remote calls, and existing
packet/return behavior remains passing.

## Evidence Requirements

The worker return must identify the final JSON shapes, consumers and freshness
rules, CLI entrypoints, validation-before-write behavior, both serialized
source-posture values, focused case names, exact commands and exit codes,
six-path changed set, and empty staging. It must distinguish self-reported
worker evidence from independent reviewer acceptance.

## Verification Commands

Run after the final edit and record exit codes plus concise output:

```powershell
git merge-base --is-ancestor 22644e47e118bd88bf0d004cb74819fd2956c061 HEAD
python governance/compat/run_adif_defect_resolver.py --task-class "task capsule implementation" --role worker --lifecycle-phase pre-implementation --surface-selector scripts --risk-ceiling MEDIUM --json
python -m pytest scripts/test_external_agent_packet.py -q
python governance/compat/run_worker_return_fast_gate.py --pytest-target scripts/test_external_agent_packet.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 22644e47e118bd88bf0d004cb74819fd2956c061 --head HEAD
git diff --check
git diff --name-only
git diff --cached --name-only
git status --short
```

Provider and network execution are forbidden. Do not run `prepare-task`
against a real public repository; use isolated mocks/fixtures.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json` | strict four-group and source-posture schema extension |
| `docs/reference/external_agent_review/README.md` | document consumers, freshness, live/offline boundary, and no-effect claim |
| `scripts/external_agent_packet.py` | validate context; preserve live route; add offline capsule-only route |
| `scripts/test_external_agent_packet.py` | focused positive, negative, compatibility, and no-network tests |
| `scripts/Update-CVF-External-Agent-Packet.ps1` | expose explicit offline mode and context input without default widening |
| `docs/reviews/CVF_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_WORKER_RETURN_2026-08-27.md` | full no-commit evidence packet |

Forbidden paths: every path not listed above.

Required proof literals: `VERIFIED_LIVE_PUBLIC_MAIN_AT_CREATION`,
`OPERATOR_PINNED_NOT_LIVE_VERIFIED`, `WORKER_MUST_NOT_COMMIT`, and exact
six-path changed-set evidence. The worker may choose equivalent internal
constant names only if the serialized schema values remain exactly these.

## Required Proof Manifest Atomic Literal Discipline

The four exact proof literals above are atomic serialized values, not
substrings assembled from fragments. Tests must assert their complete values.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_WORKER_RETURN_2026-08-27.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --pytest-target scripts/test_external_agent_packet.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must begin with `Status: COMPLETE_PENDING_REVIEW` or
`Status: BLOCKED_WITH_REASON`, declare `Self-declared worker-return artifact:
yes`, cite this work order in `Responds to work order:` and
`dispatchWorkOrder:`, capture `executionBaseHead`, and include the required
worker-return headings and no-commit evidence derived from the checker source.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; worker must additionally read the current worker-return and reference-structure checkers before authoring outputs |
| literalTokensReviewed | dispatch envelope fields; Source Verification columns; AOT labels; `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; worker-return contract literals |
| gateRunPurpose | Confirm dispatch and output contract shapes before implementation; direct gates verify the final artifacts. |
| claimBoundary | Read-ahead is preparation evidence only, not correctness or closure proof. |

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EACQ-FV-MV2",
  "requestedProfile": "P2_BOUNDED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "ENRICHES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": ["docs/baselines", "docs/reference", "scripts", "docs/reviews"],
  "claims": ["strict local task capsule", "offline pinned source posture"],
  "requiredProof": ["focused positive and negative tests", "no-network offline test", "exact changed-set evidence"],
  "operatorCheckpoints": ["independent review before commit", "fresh value gate before successor"],
  "forbiddenEffects": ["network/provider use", "external packet mutation", "public sync/deploy/push/worker commit"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: bounded named-owner implementation",
    "completenessClaimChanged": false
  }
}
```

Expected route: `P2_BOUNDED`, shadow routing only; current legacy governance
bundle remains authoritative.

## Intake Role Routing Decision

| Field | Assignment |
| --- | --- |
| selected role route | MULTI_AGENT_SINGLE_ROLE |
| intake summary | operator-authorized bounded existing-owner enrichment |
| scope classification | local six-path no-commit schema/helper implementation |
| worker role | delegated implementation worker |
| reviewer role | designated internal orchestrator/reviewer/closer |
| escalation condition | source contradiction, forbidden edit, authority expansion, or external effect |
| risk sensitivity | contract-bearing local change; no external effect |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | delegated no-commit worker followed by independent internal reviewer |
| phase | MV-2 implementation then reviewer closure |
| baseHeadFor(phase) | dispatchBaseHead=`22644e47e118bd88bf0d004cb74819fd2956c061`; executionBaseHead=worker captures; closureBaseHead=reviewer sets |
| changedSetScope(phase) | worker exact six paths; bounded reviewer repair only there; continuity separate |
| traceScope(phase, actor) | reads, decisions, commands, tests, changed set, source posture, and no-commit evidence |
| commitOwner(phase) | designated reviewer/closer only |
| crossBatchIsolation | no MV-3, UAA, provider, public, deploy, push, or unrelated work |
| nextMoveSurfaces | worker return, reviewer closure, then separate continuity sync |

## Commit Mode And Base-Anchor Lifecycle

Commit mode is `WORKER_MUST_NOT_COMMIT`. Dispatch base is an ancestor anchor,
not reset authority. The worker captures actual execution HEAD, never
resets/rebases, keeps staging empty, and reports base drift.

| Field | Value |
| --- | --- |
| baseHeadFor(phase) | dispatchBaseHead=`22644e47e118bd88bf0d004cb74819fd2956c061`; executionBaseHead=worker captures; closureBaseHead=reviewer sets |
| changedSetScope(phase) | exact six worker paths; reviewer closure/session changes separate |
| commitOwner(phase) | reviewer/closer only |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_COMPLETION_2026-08-27.md`

reviewerOwnedClosurePaths: exact six worker paths plus a separate completion
review if semantic repair or independent evidence requires it; continuity is
separate.

The reviewer must independently inspect schema semantics, validate both source
postures, run focused tests, inject malformed context, prove offline no-network
behavior, compare the exact changed set, and accept, repair, or reject.

## Dual Agent Surface Matrix

| Artifact | Worker source view | Reviewer evidence view | Cross-reference | Authority/risk boundary | Adapter boundary |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT task capsule | local schema/generator and supplied context JSON | schema/tests and independent malformed/offline probes | existing task capsule owner | context contract only; no universal enforcement claim | local helper invocation only |
| EXTERNAL_AGENT_CLI_MCP use | receives serialized capsule as operator-supplied context | return evidence checked separately | external-agent round-trip README | external worker cannot gain commit/provider/public authority | no CLI/MCP runtime adapter is implemented here |

## Provider Memory Authority Boundary

Provider-specific memory or worker-local summaries are not CVF source
authority. All task facts in the capsule must trace to the operator input and
governed owner paths; raw reviewer history is forbidden.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

The worker recomputes focused tests and final hashes after edits. Prior MV-1
evidence is dependency evidence only. New prose and code use ASCII unless an
existing path requires a governed exception.

## Foundation Storage Layout Block

N/A with reason: this tranche enriches the existing schema/helper/README/test
owners and creates one review packet; it creates no new durable reference
family or aggregate.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | reviewed proposal -> bounded roadmap -> MV-2 existing-owner enrichment |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing task capsule schema/generator/wrapper |
| Disposition | ENRICH_EXISTING, source-verified and rewritten CVF-native |
| Claim boundary | no direct import, provider action, public mutation, or effectiveness claim |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: bounded current-owner implementation, not a rescan or source reassessment.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no corpus completeness claim.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: R0 already completed the mixed-origin corpus
absorption. MV-2 implements only the accepted task-capsule owner delta.

## Delta Execution Claim Boundary Control Block

Delta execution claim boundary: REQUIRED

| Field | Value |
| --- | --- |
| claimScope | local schema/helper/wrapper/docs/test implementation only |
| claimDisposition | CLAIM_REJECTED: no universal agent-control or runtime-enforcement claim |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no provider/runtime receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local unit/subprocess test execution only |
| invocationBoundary | explicit manual helper/wrapper invocation; no mandatory interception |
| interceptionBoundary | no hook, proxy, daemon, or universal dispatch control |
| claimLanguage | validated local capsule production pending independent review |
| forbiddenExpansion | no provider/live/public/package/Web/MCP/deployment/production claim |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | internal orchestrator/dispatcher |
| Provider or surface | local private-provenance repository |
| Session or invocation | EACQ-FV-MV2 dispatch authoring, 2026-08-27 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | governed reads, source search, Git, scaffold helper, ADIF resolver, `apply_patch` |
| Target paths | `docs/baselines/CVF_GC018_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_2026-08-27.md`; this work order |
| Allowed scope source | operator instruction to continue and roadmap MV-2 value gate |
| Before status evidence | clean worktree at `22644e47e118bd88bf0d004cb74819fd2956c061` |
| After status evidence | dispatch-ready baseline and work order only; implementation absent |
| Diff evidence | two-path dispatch-author diff before commit |
| Approval boundary | MV-2 implementation dispatch only |
| Claim boundary | no implementation, worker commit, provider, public, push, or production claim |
| Agent type | orchestrator/dispatcher/reviewer |
| Invocation ID | `eacq-fv-mv2-dispatch-2026-08-27` |
| Expected manifest | `docs/baselines/CVF_GC018_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_2026-08-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_2026-08-27.md` |
| Actual changed set | `docs/baselines/CVF_GC018_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_2026-08-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_MV2_EXTERNAL_AGENT_TASK_CAPSULE_CONTEXT_2026-08-27.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | NONE |

## Expected Output Manifest

Worker output must be exactly the six paths in Write Ownership. Any extra
changed path is `BLOCKED_WITH_REASON` unless it is pre-existing user work that
the worker leaves untouched and reports.

## Review Gate

Review remains closed until the exact no-commit manifest returns. Reviewer
acceptance requires semantic inspection, focused tests, independent malformed
and offline no-network probes, source-posture honesty, and applicable gates.

## Closure Checklist

- [ ] exact six-path worker manifest and empty staging independently confirmed;
- [ ] strict four-group schema and consumer/freshness semantics reviewed;
- [ ] live and offline source postures tested without real network use;
- [ ] invalid input cannot overwrite the capsule;
- [ ] focused and applicable governance gates pass after final edit;
- [ ] MV-3/UAA and external effects remain parked.

## Return-To-Orchestrator Conditions

Return after final verification with `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`. Repair routine failures within exact scope; do not wait
for permission. Stop rather than widen scope.

operator.checkpoint.waiver: MV-2 dispatch authorization is recorded; the next
human checkpoint is successor admission after independent MV-2 closure.

## Dispatch Packet Authoring Learning Promotion

The dispatcher converted the roadmap's broad context proposal into one
existing-owner, four-group, no-network tranche and kept MV-3 parked until
comparative evidence exists. No new governance rule is promoted by this order.

## Next-Tranche Audit Mini-Package

MV-3 admission after MV-2 closure must cite at least one capsule-enhanced task
or an exact decision-changing reason why such evidence is unavailable. Without
that evidence, MV-3 remains parked. UAA retains its conjunctive index gate.

## Export Surface Decision

No external packet folder or public-sync surface is an output. The worker may
change the reusable private owner code/docs only and must not execute it
against `D:\UNG DUNG AI\EXTERNAL_AGENT_READ`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

No public artifact, remote, commit, or path is authorized or claimed.

## Claim Boundary

This order authorizes only exact six-path, local, deterministic, no-commit
MV-2 work. It does not prove improved external-agent quality, mandate capsule
use universally, authorize MV-3/UAA, access network/provider/secrets, mutate an
external packet folder, publish, deploy, push, or close the tranche.

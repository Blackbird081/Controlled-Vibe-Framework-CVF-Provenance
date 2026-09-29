# CVF Agent Work Order RFR-R3 Native MCP Admission

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Date: 2026-08-24

Batch ID: RFR-R3

## Dispatch Prompt Envelope

```text
Role: implementation worker. The current orchestrator remains independent reviewer/closer.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R3_NATIVE_MCP_ADMISSION_2026-08-24.md
Commit mode: WORKER_MUST_NOT_COMMIT.
Base: capture executionBaseHead from the committed R3 dispatch HEAD at worker start; dispatchBaseHead is cc08ea2da6f23f3f87b6eec7cb6248ecab365b16.
Current-time notes: only RFR-R3 is released; R4-R6 and all external-effect lanes remain parked.
Do-not-misread notes: remove caller-supplied policy authority and require native CVF admission; no provider/live run, Model Gateway production rewrite, deployment, public sync, or production-readiness claim.
Required first actions: read required authority and sources; capture HEAD/status; verify all five hashes and the exact six-path manifest; run the worker ADIF resolver.
Return contract: COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON with exact diff, tests/gates, residuals, unchanged HEAD, empty staging, and zero external calls.
```

Dispatch base head: `cc08ea2da6f23f3f87b6eec7cb6248ecab365b16`

dispatchBaseHead: `cc08ea2da6f23f3f87b6eec7cb6248ecab365b16`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET_AFTER_WORKER_RETURN`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker target: one separate external implementation worker

Reviewer/closer: current orchestrator; worker self-acceptance is forbidden

Baseline: `docs/baselines/CVF_GC018_RFR_R3_NATIVE_MCP_ADMISSION_2026-08-24.md`

Worker return: `docs/reviews/CVF_RFR_R3_NATIVE_MCP_ADMISSION_WORKER_RETURN_2026-08-24.md`

Target completion review: `docs/reviews/CVF_RFR_R3_NATIVE_MCP_ADMISSION_COMPLETION_2026-08-24.md`

## Purpose

Implement bounded RFR-R3 closure of F8 by making native CVF admission intrinsic
to MCP Model Gateway execution and ensuring caller policy data can never grant
executor authority.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "RFR-R3",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "CREATES_OR_CHANGES_AUTHORITY",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.ts",
    "EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.test.ts",
    "EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts",
    "EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts",
    "docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md",
    "docs/reviews/CVF_RFR_R3_NATIVE_MCP_ADMISSION_WORKER_RETURN_2026-08-24.md",
    "docs/baselines/",
    "docs/work_orders/"
  ],
  "claims": ["F8 caller-policy bypass closed at MCP execution admission"],
  "requiredProof": ["direct adapter adversarial tests", "registered-tool proof", "hermetic Model Gateway composition proof", "full MCP package", "TypeScript build", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": ["R4 requires accepted R3 closure; standing roadmap authority permits fresh dependency-ordered dispatch"],
  "forbiddenEffects": ["worker stage or commit", "provider/live call", "credential access", "Model Gateway production edit", "deployment", "public write", "new subsystem"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

Expected route: `ROUTED_SHADOW`, profile `P3_ELEVATED`, selective execution
false, legacy disposition `RUN_FULL_LEGACY_BUNDLE`.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RFR-R3 --title "Runtime Finding Remediation R3 Native MCP Admission" --date 2026-08-24 --base cc08ea2da6f23f3f87b6eec7cb6248ecab365b16 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "RFR-R2 closed bounded at 84d44889fe2724e574241b5fb74d371e900fd6e3 and operator authorized autonomous roadmap continuation on 2026-08-24" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker return |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact F8 source facts, hashes, six-path manifest, native-admission matrix, role split and return contract |
| checkerReadAheadConfirmation | applicable checker sources and routed standards were read before authoring |
| docOnlyNewFields | none; implementation form remains worker-owned inside the acceptance invariant |
| claimBoundary | dispatch authoring provenance only; no implementation or runtime closure claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| RFR-R2 material closure | `84d44889fe2724e574241b5fb74d371e900fd6e3` | accepted R2 required | ACCEPT |
| RFR-R2 continuity | `cc08ea2da6f23f3f87b6eec7cb6248ecab365b16` | state must expose R3 as eligible | ACCEPT |
| operator continuation | explicit 2026-08-24 autonomous roadmap instruction | fresh R3 release | ACCEPT |
| roadmap order | runtime findings roadmap R3 row | F8 follows F2-F4 | ACCEPT |

## Required First Reads

1. `AGENTS.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION_MEMORY.md`
4. `AGENT_HANDOFF_V59_2026-08-11.md`
5. `docs/reference/guard_orientation/README.md`
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
7. `docs/baselines/CVF_GC018_RFR_R3_NATIVE_MCP_ADMISSION_2026-08-24.md`
8. this work order
9. all five pre-existing manifest sources in full
10. applicable checker sources named below before authoring the worker return

## Agent Roles

- Worker: reads, verifies hashes, edits exactly six paths, tests, records full
  evidence, and stops without staging or committing.
- Reviewer/closer: independently inspects all changes, runs additional probes,
  may make bounded in-manifest repairs, decides acceptance, and owns commits.
- Session-sync steward: updates active continuity only after material identity.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | close verified local F8 caller-policy authority bypass |
| scope classification | SECURITY_SENSITIVE_RUNTIME_AUTHORITY_IMPLEMENTATION |
| primary task class | bounded MCP admission implementation |
| risk sensitivity | HIGH |
| selected role route | MULTI_AGENT_SINGLE_ROLE |
| orchestration requirement | external no-commit worker plus independent current reviewer |
| role separation basis | worker cannot accept or commit its own authority-boundary change |
| escalation condition | any seventh path, new owner/dependency, external effect, or Model Gateway production edit |

## Worker Autonomy / No-Question Rule

Proceed autonomously inside the exact manifest. Read a failing checker or test
and repair in-scope defects directly. Return `BLOCKED_WITH_REASON` only when
completion requires another path, changes the canonical MCP/Model Gateway owner
boundary, creates a new subsystem, needs network/secrets/live/public action, or
reveals a new independent critical authority contradiction. Do not stage,
commit, push, or ask permission for an in-scope repair.

## Pre-Flight Checks

- capture `git rev-parse HEAD` as `executionBaseHead`;
- record `git status --short` and stop for any pre-existing overlap;
- verify all five pre-existing source/reference hashes against the manifest;
- verify the worker-return path does not already exist;
- read all allowed paths and applicable worker-return checkers before editing;
- run the ADIF resolver for taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-execution`.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| supreme/local governance | `AGENTS.md` and routed standards | ACCEPT |
| operator | autonomous dependency-ordered continuation instruction | ACCEPT |
| verified defect | governed findings review F8 | ACCEPT |
| prerequisite | RFR-R2 material and continuity commits | ACCEPT |
| implementation | paired R3 baseline and this exact manifest | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| caller policy is copied into Model Gateway request | BYPASS_PATH_CONFIRMED | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.ts` | input and policy construction | `policyResult`; `executeModelGatewayAdapter` | MCP execute adapter | ACCEPT |
| execute adapter exposes injected executor | RUNTIME_BOUNDARY | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.ts` | `ModelGatewayExecutorPort` | `execute` | MCP execute adapter | ACCEPT |
| server owns a native guard engine | EXISTING_OWNER | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | singleton engine construction | `engine`; `createGuardEngine` | MCP Guard Runtime | ACCEPT |
| registered execute tool currently lacks native admission injection | COMPOSITION_GAP | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | execute tool registration | `registerModelGatewayExecuteTool(server)` | MCP server entry point | ACCEPT |
| direct tests self-attest allow/deny | TEST_GAP | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.test.ts` | `VALID_INPUT`; policy tests | `policyResult` | direct adapter tests | ACCEPT |
| composition test forwards self-attested policy | TEST_GAP | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts` | `VALID_INPUT`; adapter calls | `policyResult` | composition proof | ACCEPT |
| existing reference assigns MCP ingress and Model Gateway execution owners | GOVERNANCE_REFERENCE | `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md` | Boundary Decision | MCP/Model Gateway boundary | reference owner | ACCEPT |
| F8 routes to R3 | REVIEW_AUTHORITY | `docs/reviews/CVF_RUNTIME_FINDINGS_VERIFICATION_AND_REMEDIATION_AUTHORITY_2026-08-24.md` | Findings / Position | F8 | governed review | ACCEPT |

## Source Hash Manifest

| Path | Required SHA-256 before edit |
| --- | --- |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.ts` | `24f86294935993fa70bdfe66e204a821bcd4a8378f1d3dfcd2a1242d5f8389e9` |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.test.ts` | `3e5b37eb8a827ebcbcdabca6dc89d1f5bb64e50c3e2743f509a0e06a1ef9fc33` |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts` | `24fce042df76fa68032617165d12be125f853419acab7a03454353f76d4cd99d` |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | `76d1bdfa92cc2897b646d91238c29bc5907a74fe5f95424244e92a095ae5b82b` |
| `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md` | `457c4928155b151f8f49b0f8662c50309570e159b595672195de0f7cc21efe99` |

If any hash differs before editing, return `BLOCKED_WITH_REASON` without repair.

## Exact Implementation Contract

### R3-A caller-policy removal

Remove `policyResult` from the accepted MCP tool schema and from the authority
used to construct `GatewayExecuteRequestPort.policy`. A legacy/untyped caller
that supplies `policyResult: 'allow'` must not gain authority; reject it
explicitly or otherwise prove it cannot reach the executor.

### R3-B native admission

Require the server-owned MCP `GuardRuntimeEngine` (or an equivalently direct,
typed native engine owner already present in the package) at the execute adapter
boundary. Build a deterministic, secret-safe context from validated MCP intent,
role, trace and risk inputs. Evaluate once before the executor.

Do not introduce a generic caller-provided boolean/decision callback that merely
moves self-attestation. The trusted object is supplied by server composition,
not by MCP request data.

### R3-C fail-closed decision mapping

- missing admission owner: reject, zero executor calls;
- thrown admission: shield details, reject, zero executor calls;
- malformed or trace-mismatched admission evidence: reject, zero executor calls;
- `BLOCK`: reject, zero executor calls;
- `ESCALATE`: reject or approval-required, zero executor calls;
- `ALLOW`: construct the downstream policy from the native decision only, then
  call the injected executor once.

The result must distinguish admission acceptance from executor/provider success
and must not claim a provider call from hermetic tests.

### R3-D registered and composition paths

Update MCP registration so the existing server-owned native engine is supplied
to `cvf_model_gateway_execute`. Preserve default failure when no executor is
configured. Update both direct unit tests and the existing ProviderExecutionBridge
composition proof; its provider adapter remains a Vitest mock and makes no live
call or credential lookup outside test-owned memory.

### R3-E reference reconciliation

Update the existing bridge-boundary reference from historical future-only text
to the factual bounded R3 state. Preserve MCP ingress, Model Gateway provider
execution, credential, receipt, and no-live/public/readiness boundaries. Do not
claim universal runtime interception or production readiness.

## Dedicated Adversarial Matrix

Cover at minimum:

- caller `policyResult: 'allow'` cannot authorize;
- native `ALLOW`, `BLOCK`, and `ESCALATE`;
- missing and throwing native engine/admission;
- malformed decision/evidence and mismatched trace;
- unauthorized role and malformed required input;
- nested raw credential rejection before admission/executor;
- executor absent and executor throws with shielded error;
- native decision, downstream policy, admission evidence and Model Gateway
  receipt remain trace-consistent;
- both direct adapter and registered MCP tool composition;
- hermetic ProviderExecutionBridge positive/negative cases with zero live calls.

## Required Artifact Manifest

| Path | Required state | Required at handoff |
| --- | --- | --- |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.ts` | native admission and caller-policy removal | YES |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.test.ts` | direct and registered-tool adversarial matrix | YES |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts` | hermetic native-admission composition proof | YES |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | server-owned engine supplied to registration | YES |
| `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md` | factual bounded R3 reference reconciliation | YES |
| `docs/reviews/CVF_RFR_R3_NATIVE_MCP_ADMISSION_WORKER_RETURN_2026-08-24.md` | truthful no-commit return | YES |

No seventh path is authorized. No deletion or rename is authorized.

## Write Ownership

Worker owns the exact six paths only. Reviewer owns any completion review,
R3-only roadmap transition, material commit, and separate continuity update.

## Work-Order Fulfillment Manifest

| Requirement | Owner | Evidence at return |
| --- | --- | --- |
| verify base/hashes/scope | worker | HEAD, status, five hashes, six-path delta |
| implement native admission | worker | source diff plus adversarial tests |
| preserve Model Gateway authority | worker | hermetic composition proof and reference update |
| independent acceptance | reviewer/closer | separate review after return |
| material and continuity commits | reviewer/closer and session-sync steward | never worker-owned |

## Required Proof Manifest

| ID | Command | Owner |
| --- | --- | --- |
| P1 | `npm test -- --run src/tools/model-gateway-execute.test.ts src/tools/model-gateway-composition-proof.test.ts` | worker from `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER` |
| P2 | `npm test -- --run` | worker from `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER` |
| P3 | `npm run build` | worker from `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER` |
| P4 | `python governance/compat/generate_corpus_scan_registry.py --check` | worker from repository root |
| P5 | `python governance/compat/check_governed_file_size.py --enforce` | worker from repository root |
| P6 | `python governance/compat/run_worker_return_fast_gate.py` | worker from repository root |
| P7 | `git diff --check` | worker from repository root |
| P8 | `git diff --cached --name-only` | worker from repository root |
| P9 | `git rev-parse HEAD` | worker from repository root |
| P10 | `git status --short` | worker from repository root |

## Required Proof Manifest Atomic Literal Discipline

Each proof row contains one command literal. Run the exact commands; do not
substitute a self-selected checker subset or combine proof rows.

## Verification Commands

```powershell
Set-Location EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER
npm test -- --run src/tools/model-gateway-execute.test.ts src/tools/model-gateway-composition-proof.test.ts
npm test -- --run
npm run build
Set-Location ../..
python governance/compat/generate_corpus_scan_registry.py --check
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --cached --name-only
git rev-parse HEAD
git status --short
```

## Execution Plan

1. Capture execution HEAD/status, verify hashes, and complete required reads.
2. Remove caller policy authority and add native admission at the execute adapter.
3. Supply the server-owned engine through registered MCP composition.
4. Extend direct, registered-tool, and hermetic Model Gateway adversarial proof.
5. Reconcile the existing MCP/Model Gateway boundary reference factually.
6. Run focused, full-package, build, governance, and diff proofs.
7. Author the truthful worker return, confirm empty staging and unchanged HEAD,
   then stop for independent review.

## Evidence Requirements

The worker return must record execution base and unchanged final HEAD, exact
before/after hashes, actual six-path changed set including the untracked return,
empty staging, focused/full/build counts, corpus aggregate, file-size and fast
gate results, diff hygiene, reviewer risks, zero provider/live calls, and the
no-commit statement.

## Acceptance Criteria

- MCP caller data cannot create an allow decision;
- native server-side guard admission is mandatory before executor invocation;
- every non-ALLOW or invalid admission case calls executor zero times;
- only native ALLOW can create downstream policy and call executor once;
- direct, registered-tool and hermetic composition paths pass;
- role/credential/error/receipt protections remain fail-closed;
- exact six-path manifest, unchanged HEAD and empty staging are proven;
- no live/provider, credential, public, deployment or production effect occurs.

## Review Gate

The reviewer will reject compatibility fallbacks that trust caller policy,
generic self-attested admission callbacks, admission after executor invocation,
missing registered-tool proof, trace-unbound evidence, assertion weakening,
scope drift, staging, worker commits, or any failed mandatory proof. Passing
worker tests is necessary but not sufficient.

## Closure Checklist

- [ ] Source hashes matched before edit.
- [ ] Exact six-path worker manifest matched.
- [ ] Caller-policy and native-admission adversarial matrix passed.
- [ ] Focused, full-package, build, corpus and file-size proof passed.
- [ ] Worker-return fast gate and diff hygiene passed.
- [ ] HEAD remained unchanged and staging remained empty.
- [ ] Reviewer receives the complete uncommitted diff and evidence.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_worker_experience_retrospective.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_changed_corpus_registry_coverage.py`; `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `COMPLETE_PENDING_REVIEW`; `WORKER_RETURN_FULL_GATE_V1`; Source Verification columns; Agent Operation Trace labels; Public Export Disposition; no-commit statement |
| gateRunPurpose | confirm R3 worker-output shape before execution and prevent dependent-failure discovery at return time; not first discovery |
| claimBoundary | checker compliance does not prove native admission semantics |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_RFR_R3_NATIVE_MCP_ADMISSION_WORKER_RETURN_2026-08-24.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must use `Status: COMPLETE_PENDING_REVIEW` or
`Status: BLOCKED_WITH_REASON`, `docType: review`, `rawMemoryReleased=false`, and
real sections for Purpose, Scope / Methodology, Findings / Position, Risk /
Corrective Action, Decision / Disposition, Source Verification Block,
Implementation Hash Evidence, Test Evidence, Checker Source Read-Ahead Block,
Agent Operation Trace Block, Delta Execution Claim Boundary Control Block,
Public Export Disposition, External Knowledge Intake Routing, Rescan
Intelligence Hardening, Corpus Completeness And Report Integrity,
Finding-To-Governance Learning Disposition, Epistemic Process Block, Worker
Experience Retrospective, Machine Closure Package, Claim Boundary, git status,
Changed Files, Command Evidence, and No-Commit Statement.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_RFR_R3_NATIVE_MCP_ADMISSION_COMPLETION_2026-08-24.md` |
| reviewerOwnedClosurePaths | optional completion review; R3-only roadmap transition; accepted six-path material; later continuity surfaces |
| closureOwner | current independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Agent Handoff Contract Control Block

Historical contract source, not an active handoff; archive-qualified:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

Active handoff source: `AGENT_HANDOFF_V59_2026-08-11.md`.

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | external implementation worker followed by current independent reviewer/closer |
| phase | RFR-R3 implementation return |
| baseHeadFor(phase) | dispatchBaseHead=`cc08ea2da6f23f3f87b6eec7cb6248ecab365b16`; executionBaseHead captured from committed dispatch HEAD; closureBaseHead reviewer-set after return |
| changedSetScope(phase) | exact six-path worker manifest |
| traceScope(phase, actor) | worker reads/edits/tests/returns; reviewer inspects/probes/repairs/commits |
| commitOwner(phase) | reviewer/closer; worker commit forbidden |
| crossBatchIsolation | R4-R6 and every external-effect lane remain parked |
| nextMoveSurfaces | worker return, reviewer decision, material commit, separate continuity sync |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | MCP native Guard Runtime and execute adapter | server-owned admission before executor | direct and composition tests | local TypeScript only | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | `cvf_model_gateway_execute` | caller supplies intent, never authorization | registered-tool hostile input proof | no live/provider invocation | IMPLEMENTED |

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | YES_LOCAL_HERMETIC_ONLY |
| runtimeMutationAuthorized | YES_LOCAL_SOURCE_ONLY |
| freshnessVerificationMode | FRESH_SOURCE_HASH_AND_TEST_RECOMPUTE_REQUIRED |
| reason | R3 changes MCP execution admission but authorizes no provider/live claim |
| requiredFutureAction | reviewer reruns local proof; live or production claim requires separate authority |

## Commit Mode And Base-Anchor Lifecycle

Worker captures the committed dispatch HEAD as `executionBaseHead`, never stages
or commits, and reports unchanged HEAD. Reviewer captures `closureBaseHead` and
owns the material commit. Session sync is a separate commit.

## Pending Artifact Evidence Finality

Worker evidence is `COMPLETE_PENDING_REVIEW`, not closure, final material
identity, clean worktree, or reviewer acceptance. The untracked return must
appear in actual status evidence.

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: R3 changes in-memory admission and tests only; it
creates no persistence, queue, registry family, relocation, or migration.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: RFR-R3 is named-file remediation of a verified
current bypass. It performs no legacy corpus absorption, coverage-index
reassignment, source intake, workflow-chain import, or foundation-plane
migration. Existing MCP-GW-001 coverage remains unchanged.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | verified F8 to existing MCP and Model Gateway owners |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | MCP execute adapter and native Guard Runtime |
| Disposition | ADAPT only the locally verified caller-policy defect |
| Claim boundary | external prompt is provenance input, not implementation authority |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH --max-results 50 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | worker must run its pre-execution resolver; no added constraint now |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | orchestrator/dispatcher |
| Provider or surface | private provenance repository |
| Session or invocation | `rfr-r3-dispatch-20260824` |
| Working directory | repository root |
| Command or tool surface | governed reads, source/hash inspection, Git, Vitest, TypeScript, ADIF and dispatch gates |
| Target paths | paired R3 baseline and work order |
| Allowed scope source | operator's autonomous roadmap continuation instruction |
| Before status evidence | clean worktree at `cc08ea2da6f23f3f87b6eec7cb6248ecab365b16` |
| After status evidence | paired R3 authority paths pending dispatch commit |
| Diff evidence | exact paired path diff before commit |
| Approval boundary | dispatch authority only |
| Claim boundary | no implementation, provider/live, public, deployment or push claim |
| Agent type | dispatcher |
| Invocation ID | `rfr-r3-dispatch-20260824` |
| Expected manifest | `docs/baselines/CVF_GC018_RFR_R3_NATIVE_MCP_ADMISSION_2026-08-24.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R3_NATIVE_MCP_ADMISSION_2026-08-24.md` |
| Actual changed set | `docs/baselines/CVF_GC018_RFR_R3_NATIVE_MCP_ADMISSION_2026-08-24.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R3_NATIVE_MCP_ADMISSION_2026-08-24.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | exact local RFR-R3 no-commit worker dispatch |
| claimDisposition | CLAIM_REJECTED until worker proof and independent review |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: dispatch creates no runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatcher made no production edit |
| invocationBoundary | local authoring and checker processes only |
| interceptionBoundary | no provider, network, public, deployment or production action |
| claimLanguage | worker-authorized local remediation, not closure |
| forbiddenExpansion | seventh worker path, R4-R6, live calls, credentials, deploy, public sync, push or production |

## Epistemic Process Block

### Expected Result / Prediction

F8 should close by requiring the existing native MCP engine before the existing
injected executor, without changing Model Gateway production source.

### Evidence Comparison

The current adapter, tests, registration and boundary reference confirm both the
bypass and the complete bounded owner set.

### Contradiction Or Gap Disposition

Default no-executor composition is safe, but the exported injected-executor path
trusts caller policy. R3 must close that path rather than claim the default is
sufficient.

### Claim Update

R3 implementation is authorized but unproven pending worker return and review.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for hash drift, any required seventh path, inability
to make native admission intrinsic, failing mandatory proof, dependency/network
need, credential/provider/live access, or external effect. Otherwise return
`COMPLETE_PENDING_REVIEW` and stop without staging or committing.

## Operator Checkpoint

No checkpoint is required for in-scope local reversible worker implementation.
The orchestrator may proceed dependency-by-dependency under the operator's
standing roadmap authority; each worker handoff and independent review remains
mandatory. External effects still require separate authority.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance worker dispatch; public sync remains forbidden.

## Claim Boundary

This work order authorizes only exact six-path local RFR-R3 implementation and
proof. It does not prove F8 closure, grant worker commit authority, authorize
R4-R6, or permit provider/live, credentials, deployment, public sync, push, or
production.

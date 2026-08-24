# CVF Agent Work Order - RFR-R7A Canonical MCP Guard Engine Adoption

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-08-24

Batch ID: RFR-R7A-CANONICAL-MCP-GUARD-ENGINE-ADOPTION

Dispatch base head: `fddcfedf5a41a04f71a2b3228f662c399f5e2e6e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: one delegated implementation worker

Reviewer/closer: current independent orchestrator/reviewer/closer

Worker return path: `docs/reviews/CVF_RFR_R7A_CANONICAL_MCP_GUARD_ENGINE_ADOPTION_WORKER_RETURN_2026-08-24.md`

## Dispatch Prompt Envelope

Role: delegated implementation worker for RFR-R7A.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R7A_CANONICAL_MCP_GUARD_ENGINE_ADOPTION_2026-08-24.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: packet authored 2026-08-24 from clean HEAD `fddcfedf5`;
worker must capture the committed dispatch HEAD before edits.

Do-not-misread notes: Defect A only. Do not repair the R4/R3 optional-field
seam, edit the Guard Contract package, install dependencies, or invoke live MCP.

Required first actions: read the bootstrap model, session front door, active
handoff, guard orientation, literal gotchas, paired baseline, this packet and
all checker/source paths cited below; then record HEAD/status and run
pre-implementation before edits.

Return contract: implement exact scope, create the named worker return, run all
required proof, leave every change uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Replace every MCP production dependency on the stale local guard-engine fork
with direct canonical `cvf-guard-contract` consumption. Preserve MCP/CLI
session-phase UX through owner-local state, not through a replacement engine,
and prove the externally reachable engine has the immutable R1/R2 mandatory
core.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "RFR-R7A",
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
    "EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts",
    "EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/sdk.ts",
    "EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/",
    "EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/",
    "EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/integration/",
    "docs/reviews/",
    "docs/baselines/",
    "docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md"
  ],
  "claims": ["MCP production composition roots adopt canonical cvf-guard-contract"],
  "requiredProof": ["production import search", "mandatory guard negative probes", "focused tests", "TypeScript build", "bounded full-package result", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": ["R7B remains dependency-gated until accepted R7A closure"],
  "forbiddenEffects": ["worker stage or commit", "Guard Contract edit", "Model Gateway edit", "dependency installation", "provider/live/network call", "credential access", "deployment", "public write"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

Expected route: `ROUTED_SHADOW`, profile `P3_ELEVATED`, selective execution
false, legacy disposition `RUN_FULL_LEGACY_BUNDLE`.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RFR-R7A-CANONICAL-MCP-GUARD-ENGINE-ADOPTION --title "CVF RFR-R7A Canonical MCP Guard Engine Adoption" --date 2026-08-24 --base fddcfedf5a41a04f71a2b3228f662c399f5e2e6e --commit-mode WORKER_MUST_NOT_COMMIT --dependency "RFR-R6 reviewer disposition accepted at 39ba8f31f with remediation required" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker and MCP/CLI boundary profiles |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | verified dependency, exact owner manifest, session-phase compatibility constraint, tests and return contract |
| checkerReadAheadConfirmation | cited checker sources read before authoring |
| docOnlyNewFields | none |
| claimBoundary | dispatch provenance only; no implementation claim |

## Required First Reads

- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V59_2026-08-11.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/baselines/CVF_GC018_RFR_R7A_CANONICAL_MCP_GUARD_ENGINE_ADOPTION_2026-08-24.md`
- this work order and the source/checker paths cited in it

## Agent Roles

| Role | Owner | Authority |
| --- | --- | --- |
| operator | current operator | approved R7A/R7B split |
| dispatcher | current orchestrator | source verification and bounded packet |
| worker | one delegated worker | exact source/test/return manifest; no commit |
| reviewer/closer | current independent orchestrator | review, allowed-scope repair, commit and continuity |

## Authority Chain

Operator authorization -> R6 reviewer disposition at material `39ba8f31f` -> runtime
findings roadmap -> paired GC-018 baseline -> this work order.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| R6 Defect A accepted | `docs/reviews/CVF_RFR_R6_CROSS_OWNER_ADVERSARIAL_REAUDIT_WORKER_RETURN_2026-08-24.md`; `39ba8f31f` | fresh remediation authority required | ACCEPT |
| operator chose split | operator message dated 2026-08-24 | R7A precedes R7B | ACCEPT |
| package dependency present | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json`, dependencies | no installation or manifest edit needed | ACCEPT |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | repair the reproduced externally reachable stale MCP guard-engine route |
| scope classification | SECURITY_SENSITIVE_RUNTIME_COMPOSITION_IMPLEMENTATION |
| primary task class | bounded runtime composition repair |
| risk sensitivity | HIGH |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| orchestration requirement | one no-commit implementation worker plus independent reviewer/closer |
| role separation basis | worker cannot accept its own mandatory-admission composition change |
| escalation condition | forbidden path, replacement factory, permissive BUILD fallback, new dependency or external effect |

## Scope

Implement direct canonical-engine adoption in the exact manifest below. A
production file may retain local guard types/constants only when no engine or
factory flows through them, but preferred migration is canonical types wherever
the touched seam permits. The local `src/guards/**` fork is read-only in R7A.

## Write Ownership

Worker may edit only these paths:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/sdk.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/cli.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/cli.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/integration/e2e-pipeline.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/integration/canonical-guard-contract-adoption.test.ts` (new)
- `docs/reviews/CVF_RFR_R7A_CANONICAL_MCP_GUARD_ENGINE_ADOPTION_WORKER_RETURN_2026-08-24.md` (new)

Forbidden: every other path, especially `EXTENSIONS/CVF_GUARD_CONTRACT/**`,
`EXTENSIONS/CVF_MODEL_GATEWAY/**`, MCP `package.json`, lockfiles,
MCP `src/guards/**`, governance, roadmap and session surfaces.

## Pre-Flight Checks

1. Capture `git rev-parse HEAD`, `git status --short`, and staged state.
2. Confirm dispatch HEAD includes this packet and paired baseline.
3. Run pre-implementation autorun against captured HEAD.
4. Confirm no pre-existing unrelated change overlaps the manifest.
5. Record baseline full MCP result: exactly the known R7B three failures, or
   stop if a different fourth failure exists before edits.

## Execution Plan

1. Replace production engine/factory imports with direct
   `cvf-guard-contract` imports.
2. Remove engine-owned session-phase assumptions from MCP/CLI roots. Keep the
   phase value as bounded MCP/CLI state; do not monkey-patch or wrap the engine.
3. Make SDK engine exports canonical.
4. Migrate type-only engine imports on touched tool/launcher seams.
5. Add a regression test that statically rejects production imports from the
   local engine/factory and dynamically proves canonical mandatory IDs,
   protected removal/disable, and immutable returned views.
6. Update only directly affected fixtures. Missing BUILD authority must remain
   blocked; never add permissive defaults.
7. Run focused, build, full-package, negative search, governance and manifest
   proof; return uncommitted evidence.

## Acceptance Criteria

- zero non-test production imports of `createGuardEngine` or
  `GuardRuntimeEngine` from MCP `src/guards/**`;
- canonical factory is used by server, standard CLI and governed-exec CLI;
- SDK exports canonical factory/engine;
- canonical mandatory IDs include `ai_commit`, `authority_gate`, `phase_gate`,
  and `build_authority` at every live root;
- unregister/disable of each mandatory ID throws or otherwise fails closed;
- mutating values returned by `getGuard`/`getRegisteredGuards` cannot mutate
  engine identity, order, priority, enabled state or evaluation behavior;
- BUILD mutation without complete authority evidence blocks;
- focused R7A tests pass and TypeScript build passes;
- full package has no failure other than the same three named R7B failures;
- exact changed set stays within the 15 source/test paths plus one return.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap item | Work-order implementation | Proof |
| --- | --- | --- |
| R7A canonical MCP engine adoption | direct production imports plus local phase state | static/dynamic adoption regression test |
| preserve fail-closed R1/R2 | no permissive BUILD defaults | negative BUILD probe |
| keep R7B isolated | no validator or adapter-input repair | exact manifest and known-failure reconciliation |

## Required Proof Manifest

| Proof | Required result |
| --- | --- |
| production import search | zero local engine/factory consumers outside tests and `src/guards/**` |
| focused adoption suite | PASS |
| affected MCP suites | PASS except the three exact R7B assertions when included |
| `npm run build` | PASS |
| full `npm test -- --run` | 745 pass plus the same 3 known R7B failures, or better; no new failure |
| worker return fast gate | PASS |
| diff/status/staging | exact allowed manifest; staging empty; HEAD unchanged |

## Evidence Requirements

Every command row must record command, working directory, atomic counts/result
and terminal disposition. The worker must identify the three known R7B failing
test names rather than reporting only an aggregate. Negative probes must show
actual thrown/block results and registered guard IDs.

## Verification Commands

Run from `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER` unless stated otherwise:

```powershell
npx vitest run src/integration/canonical-guard-contract-adoption.test.ts src/cli/cli.test.ts src/cli/governed-command-launcher.test.ts src/integration/e2e-pipeline.test.ts src/tools/governance-action-preflight.test.ts src/tools/model-gateway-execute.test.ts src/tools/model-gateway-composition-proof.test.ts
npm run build
npm test -- --run
rg -n 'createGuardEngine|GuardRuntimeEngine|guards/index|guards/engine' src -g '*.ts'
```

From repository root:

```powershell
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git status --short
```

## Required Proof Manifest Atomic Literal Discipline

Report each proof command once with one result. Do not merge focused and full
package counts, convert expected R7B failures into PASS, or call the full suite
green while any test fails.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| declared dependency exists | PACKAGE_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json` | dependencies | `cvf-guard-contract` | MCP package | ACCEPT |
| production roots use local factory | RUNTIME_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`, `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/cli.ts`, and `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts` | import blocks | `createGuardEngine` | MCP server/CLI roots | ACCEPT |
| SDK exports local factory | EXPORT_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/sdk.ts` | guard export block | engine/factory exports | MCP SDK | ACCEPT |
| tool and launcher engine types are local | TYPE_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts`, `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts`, and `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.ts` | type imports | `GuardRuntimeEngine` | MCP production seams | ACCEPT |
| canonical factory contains R1/R2 guards | RUNTIME_SOURCE | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | Factory | `AiCommitGuard`; `BuildAuthorityGuard` | Guard Contract | ACCEPT |
| canonical mandatory guards are protected | RUNTIME_SOURCE | `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | unregister/disable/accessor methods | mandatory protection and frozen views | Guard Contract | ACCEPT |
| canonical engine lacks MCP session phase | COMPATIBILITY_SOURCE | `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | public method inventory | no `getSessionPhase`/`setSessionPhase` | Guard Contract boundary | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| artifact paths | exact baseline/work-order/return checks were false before dispatch authoring | ACCEPT |
| tranche tokens | no prior R7A artifact found in `docs` or `CVF_SESSION` | ACCEPT |
| source collision | all production local-engine imports enumerated before manifest lock | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_corpus_scan_registry.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `COMPLETE_PENDING_REVIEW`; Source Verification columns; Actual changed set; Worker Return Packet Shape Contract |
| gateRunPurpose | confirm checker-safe dispatch after source and manifest verification, not first discovery |
| claimBoundary | structural conformance cannot prove runtime adoption, mandatory guard behavior or test correctness |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_RFR_R7A_CANONICAL_MCP_GUARD_ENGINE_ADOPTION_WORKER_RETURN_2026-08-24.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real sections: Purpose; Scope / Methodology; Findings / Position; Risk
/ Corrective Action; Checker Source Read-Ahead Block; Agent Operation Trace
Block; Delta Execution Claim Boundary Control Block; Public Export Disposition;
External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus
Completeness And Report Integrity; Finding-To-Governance Learning Disposition;
Epistemic Process Block; Claim Boundary; git status --short; Changed Files;
Worker Experience Retrospective; Command Evidence; No-Commit Statement; Machine
Closure Package.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| 14 existing MCP source/test paths | modify only when required; list terminal disposition for every allowed path |
| canonical adoption regression test | create and prove static plus dynamic invariants |
| worker return | create at exact path with full gate profile |
| all forbidden paths | remain byte-unchanged |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> one implementation worker -> independent reviewer/closer |
| phase | R7A implementation pending |
| baseHeadFor(phase) | dispatchBaseHead=`fddcfedf5a41a04f71a2b3228f662c399f5e2e6e`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact Write Ownership manifest |
| traceScope(phase, actor) | worker records all commands and file deltas; reviewer independently reproduces decisive probes |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer only |
| crossBatchIsolation | R7B, Guard Contract, Model Gateway, governance, session and external effects remain forbidden |
| nextMoveSurfaces | exact worker return, then independent review |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_RFR_R7A_CANONICAL_MCP_GUARD_ENGINE_ADOPTION_COMPLETION_2026-08-24.md` if reviewer needs a separate decision record |
| reviewerOwnedClosurePaths | worker return, this work order, roadmap and separately governed continuity surfaces |
| closureOwner | current independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Review Gate

Reviewer must inspect every diff, rerun static/dynamic canonical-adoption probes,
confirm no local factory remains production-reachable, verify exact R7B failure
containment, and run reviewer-fast before any commit or R7B release.

## Closure Checklist

- exact manifest reconciled;
- focused tests and build pass;
- full package has no new failure;
- mandatory guard IDs and self-protection independently proven;
- worker HEAD unchanged and staging empty;
- reviewer decision recorded;
- R7B remains held unless R7A is accepted.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | delegated implementation worker | exact local file manifest; no commit | work order | repository-local implementation | `IMPLEMENTATION_AUTHORIZED_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | server, CLI, governed-exec and SDK entrypoints | composition repair only; no invocation/live claim | production imports plus regression test | direct canonical dependency; session phase remains MCP-local state | `IMPLEMENTATION_AUTHORIZED_BOUNDED` |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | repository-local orchestration surface |
| Session or invocation | RFR-R7A dispatch, 2026-08-24 |
| Working directory | repository root |
| Command or tool surface | source reads, searches, scaffold stdout, governed patch and dispatch gates |
| Target paths | paired baseline, this work order and roadmap only during dispatch |
| Allowed scope source | operator authorization plus R6 remediation-required disposition |
| Before status evidence | HEAD `fddcfedf5`; worktree clean before dispatch authoring |
| After status evidence | exact three dispatcher paths pending; staging empty before material commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch artifacts only; source repair remains worker-owned after commit |
| Claim boundary | no implementation or external-effect claim |
| Agent type | dispatcher/orchestrator role |
| Invocation ID | `rfr-r7a-dispatch-2026-08-24` |
| Expected manifest | paired baseline; this work order; runtime findings roadmap |
| Actual changed set | paired R7A baseline; this work order; runtime findings roadmap |
| Manifest delta | NONE |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local source/test implementation and deterministic proof only |
| claimDisposition | CLAIM_REJECTED: dispatch alone proves no execution control or live enforcement |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed by dispatch |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is invoked by dispatch |
| invocationBoundary | worker may run local tests/build only |
| interceptionBoundary | no provider/live command interception or wrapper authority |
| claimLanguage | source-wired and locally tested only after reviewer acceptance |
| forbiddenExpansion | R7B, Guard Contract edits, install, provider/live/network, credentials, public sync, push, deployment and production |

## Epistemic Process Block

- Epistemic Process Applicability: BOUNDED_GOVERNANCE_IMPLEMENTATION
- Expected result / prediction: direct canonical imports plus MCP-local phase
  state remove the live stale-fork route without requiring Guard Contract edits.
- Evidence Comparison: R6 probes and current source show local imports and six
  guards; canonical source shows the hardened factory and immutable core.
- Contradiction or gap disposition: canonical engine lacks session-phase
  methods, so the packet explicitly routes phase state to MCP/CLI rather than
  assuming interface equivalence.
- Claim update: R7A is dispatch-ready, not implemented or accepted.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no external knowledge intake; operator supplied authority only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` plus local CVF source verification |
| Owner surface | MCP Server and Guard Contract source |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | no external content is absorbed or promoted as authority |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: R7A repairs current first-party runtime composition;
it is not legacy absorption, corpus intake, or foundation-plane reassessment.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-execution`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-execution --json`

## Worker Autonomy / No-Question Rule

Worker repairs any allowed-scope source, test, type or formatting failure and
reruns the relevant command. Return only for a repeated need to edit a forbidden
path, a contradictory canonical contract, unrelated baseline failure, or an
authority gap. Do not escalate ordinary allowed-scope implementation choices.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all R7A criteria are met and the only
remaining full-suite failures are the exact known R7B three. Return
`BLOCKED_WITH_REASON` if completion requires Guard Contract, Model Gateway,
package/lockfile, local guard-source, governance, roadmap or session edits.

## Escalation Boundary

No checkpoint inside allowed scope. R7B dispatch requires independent R7A
acceptance; any design that adds a replacement factory or weakens mandatory
BUILD admission returns for operator/reviewer decision.

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | YES_CURRENT_LOCAL_SOURCE_AND_TEST_BASELINE_ONLY |
| runtimeMutationAuthorized | YES_EXACT_WORKER_MANIFEST |
| freshnessVerificationMode | current source inspection plus reviewer R6 probes dated 2026-08-24 |
| reason | R7A changes current MCP composition; no provider/live assertion is made |
| requiredFutureAction | worker and reviewer rerun deterministic local tests and canonical-adoption probes |

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: no durable Foundation storage, database, registry,
generated aggregate, path relocation or index owner is created or moved.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance tranche; no public-sync action is authorized.

## Claim Boundary

This work order authorizes exactly the listed MCP source/test files and one
uncommitted return. It does not authorize Guard Contract or Model Gateway edits,
R7B changes, dependency installation, provider/live/network calls, credentials,
deployment, public sync, push, production readiness, or worker closure.

## Operator Checkpoint

NOT_APPLICABLE_WITH_REASON: no mid-worker operator decision is scheduled. The
worker follows the exact manifest and returns on the stated escalation boundary.

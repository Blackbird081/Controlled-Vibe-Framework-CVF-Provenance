# CVF Agent Work Order - RFR-R2 Immutable Mandatory Core

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Date: 2026-08-24

Batch ID: RFR-R2

## Dispatch Prompt Envelope

```text
Role: implementation worker. The current orchestrator remains independent reviewer/closer.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R2_IMMUTABLE_MANDATORY_CORE_2026-08-24.md
Commit mode: WORKER_MUST_NOT_COMMIT.
Base: capture executionBaseHead from the committed R2 dispatch HEAD at worker start; dispatchBaseHead is 804168de1997504bafd500b4159c981dec4d7627.
Current-time notes: only RFR-R2 is released; R3-R6 and all external-effect lanes remain parked.
Do-not-misread notes: preserve RFR-R1 and the canonical guard set; harden existing engine/Gateway owners only; no Web, MCP, CLI, provider, live, deployment, public, or production work.
Required first actions: read startup and required sources; record HEAD/status; verify the exact six-path manifest and source hashes; run the worker ADIF resolver.
Return contract: COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON with exact diff, tests/gates, residuals, empty staging, unchanged HEAD, and zero external calls.
```

Dispatch base head: `804168de1997504bafd500b4159c981dec4d7627`

dispatchBaseHead: `804168de1997504bafd500b4159c981dec4d7627`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET_AFTER_WORKER_RETURN`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated external implementation worker

Reviewer/closer: current orchestrator/reviewer

Worker return path: `docs/reviews/CVF_RFR_R2_IMMUTABLE_MANDATORY_CORE_WORKER_RETURN_2026-08-24.md`

## Purpose

Implement the bounded RFR-R2 closure of F2-F4 in the existing Guard Contract
engine and Mandatory Gateway, then return the complete uncommitted diff and
evidence for independent review.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "RFR-R2",
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
    "EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts",
    "EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts",
    "EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts",
    "EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.test.ts",
    "docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json",
    "docs/reviews/",
    "docs/baselines/",
    "docs/work_orders/"
  ],
  "claims": ["F2-F4 immutable mandatory-core hardening in existing owners"],
  "requiredProof": ["focused adversarial tests", "full Guard Contract tests", "TypeScript typecheck", "system-chain freshness", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": ["R3 requires accepted R2 closure and fresh operator direction"],
  "forbiddenEffects": ["provider or live call", "credential use", "deployment", "public write", "worker staging or commit", "new subsystem"],
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
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RFR-R2 --title "Runtime Finding Remediation R2 Immutable Mandatory Core" --date 2026-08-24 --base 804168de1997504bafd500b4159c981dec4d7627 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "RFR-R1 closed bounded at a670343706c4fa21427a55a9c2ba464b9cef6cd4 and operator authorized R2 on 2026-08-24" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker return |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact F2-F4 source facts, hashes, six-path manifest, adversarial matrix, role split and return contract |
| checkerReadAheadConfirmation | applicable checker sources and routed standards were read before authoring |
| docOnlyNewFields | none; implementation form remains worker-owned inside the acceptance invariant |
| claimBoundary | dispatch authoring provenance only; no implementation or runtime closure claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| RFR-R1 material closure | `docs/reviews/CVF_RFR_R1_BUILD_AUTHORITY_CLOSURE_COMPLETION_2026-08-24.md`; commit `a670343706c4fa21427a55a9c2ba464b9cef6cd4` | accepted R1 is required for R2 | ACCEPT |
| R2 roadmap eligibility | `docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md`, Work Plan R2 | F2-F4 are the next dependency-ordered tranche | ACCEPT |
| fresh operator release | operator message on 2026-08-24 continuing R2 with old role rules | separate worker and reviewer/closer | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Implementation | Acceptance evidence | Disposition |
| --- | --- | --- | --- |
| object-reference mutation rejects | defensive registered-guard boundary in `GuardRuntimeEngine` | original/ref-return mutation probes and ordering proof | MAPPED |
| config mutation rejects | defensive immutable Mandatory Gateway bootstrap snapshot | nested input/getter mutation and post-bootstrap update probes | MAPPED |
| collision attacks reject | exact canonical bypass equality | prefix/suffix/delimiter/substring/empty-entry negative matrix | MAPPED |
| existing owners only | engine and Mandatory Gateway | exact manifest and reviewer source audit | MAPPED |

## Required First Reads

1. `AGENTS.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION_MEMORY.md`
4. `AGENT_HANDOFF_V59_2026-08-11.md`
5. `docs/reference/guard_orientation/README.md`
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
7. `docs/baselines/CVF_GC018_RFR_R2_IMMUTABLE_MANDATORY_CORE_2026-08-24.md`
8. `docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md`
9. `docs/reviews/CVF_RUNTIME_FINDINGS_VERIFICATION_AND_REMEDIATION_AUTHORITY_2026-08-24.md`
10. this work order, every ACCEPT source path below, and checker sources applicable to the worker return

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| operator | explicit 2026-08-24 R2 continuation instruction | ACCEPT |
| verified defects | governed review F2-F4 | ACCEPT |
| ordered tranche | runtime findings roadmap R2 | ACCEPT |
| prerequisite closure | RFR-R1 material `a670343706c4fa21427a55a9c2ba464b9cef6cd4` | ACCEPT |
| implementation boundary | paired R2 GC-018 and this exact manifest | ACCEPT |

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Operator | authorizes R2 and copies this committed packet to the worker |
| Orchestrator/dispatcher | owns packet, sequencing, scope and later reviewer assignment |
| External implementation worker | edits six allowed paths, runs proof, returns evidence, never stages or commits |
| Reviewer/closer | independently inspects, probes, repairs only authorized scope, and commits accepted material |
| Session-sync steward | updates continuity only after the material commit |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | close verified local F2-F4 authority-hardening findings |
| scope classification | SECURITY_SENSITIVE_RUNTIME_AUTHORITY_IMPLEMENTATION |
| primary task class | bounded Guard Contract implementation |
| risk sensitivity | HIGH |
| selected role route | MULTI_AGENT_SINGLE_ROLE |
| orchestration requirement | external no-commit worker plus independent current reviewer |
| role separation basis | worker cannot accept or commit its own authority-boundary change |
| escalation condition | any seventh path, new owner/dependency, external effect, or contradiction with RFR-R1 |

## Worker Autonomy / No-Question Rule

Proceed autonomously inside the exact manifest. Read a failing checker or test
and repair in-scope defects directly. Return `BLOCKED_WITH_REASON` only when
completion requires another path, changes the canonical phase/guard model,
creates a new subsystem, needs network/secrets/live/public action, or reveals a
new independent critical authority contradiction. Do not stage, commit, push,
or ask permission for an in-scope repair.

## Pre-Flight Checks

- capture `git rev-parse HEAD` as `executionBaseHead`;
- record `git status --short` and stop for any pre-existing overlap;
- verify all five pre-existing source/reference hashes against the manifest;
- verify the worker-return path does not already exist;
- read all allowed paths and applicable worker-return checkers before editing;
- run the ADIF resolver for taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-execution`.

## Scope / Target / Owner Boundary

Worker may modify or create exactly:

1. `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts`
2. `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts`
3. `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts`
4. `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.test.ts`
5. `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`
6. `docs/reviews/CVF_RFR_R2_IMMUTABLE_MANDATORY_CORE_WORKER_RETURN_2026-08-24.md`

Read-only inspection and commands elsewhere are allowed. Every other edit is
forbidden, including types, other guards/tests, Web, MCP, CLI,
AgentExecutionRuntime, package metadata, dependencies, governance checkers,
roadmap, completion review, session state, handoff, public clone, staging, and
commit history.

## Write Ownership

Worker owns the exact six paths only. Reviewer owns any completion review,
R2-only roadmap transition, material commit, and separate continuity update.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| engine stores caller guard reference | RUNTIME_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | lines 19-38 | `guards`; `registerGuard` | Guard Contract engine | ACCEPT |
| accessors expose registered guard objects | RUNTIME_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | lines 70-76 | `getGuard`; `getRegisteredGuards` | Guard Contract engine | ACCEPT |
| mandatory APIs reject disable/unregister only | AUTHORITY_BOUNDARY | `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | lines 40-68 | `unregisterGuard`; `disableGuard` | Guard Contract engine | ACCEPT |
| engine tests are in root test suite | TEST_OWNER | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts` | lines 38-99 | `createGuardEngine`; `GuardRuntimeEngine` suites | Guard Contract tests | ACCEPT |
| Gateway uses shallow configuration copy | CONFIGURATION_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 53-74 | defaults and constructor | Mandatory Gateway | ACCEPT |
| Gateway bypass uses substring matching | AUTHORITY_WIDENING_RISK | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 95-99 and 136-139 | `includes` matching | Mandatory Gateway | ACCEPT |
| Gateway supports authority-changing update | CONFIGURATION_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 248-260 | `getConfig`; `updateConfig` | Mandatory Gateway | ACCEPT |
| current tests encode mutable/substr behavior | TEST_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.test.ts` | lines 41-111 and 141-152 | bypass and update tests | Mandatory Gateway tests | ACCEPT |
| system map fingerprints affected sources | FRESHNESS_DEPENDENCY | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` | `CONTRACT_TO_RUNTIME`, lines 59-116 | `sourceFingerprints` | system-chain map | ACCEPT |
| F2-F4 are accepted R2 findings | REVIEW_AUTHORITY | `docs/reviews/CVF_RUNTIME_FINDINGS_VERIFICATION_AND_REMEDIATION_AUTHORITY_2026-08-24.md` | Findings / Position | F2-F4 | governed review | ACCEPT |

## Source Hash Manifest

| Path | Required SHA-256 before edit |
| --- | --- |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | `159a936f4ab99fc96daa2ca5eaef4cf14f1e6b446932a8458466d97faa28e387` |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts` | `4f1de18834bf2213436bbfaed8dbd91c58cbf0f3e086c57545aed1e85ae34375` |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | `12e513c836f1fd258417be2d9ced2424df6926210a10b02bce0e88fb9235c204` |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.test.ts` | `6f9519ea039500272cb52d08454bc0ed77b8c952315c062b8b7faa3592116201` |
| `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` | `88d3a209bd66e7ba12e8c80e21ad7e383b7d588e50cd4f7533cf8f7be5ef9945` |

Any mismatch before edit is `BLOCKED_WITH_REASON`; do not rebase authority
silently or refresh hashes from a different source state.

## Required Implementation

### F2 registered-guard immutability

Create a defensive registered-guard boundary so later writes through the
original object, `getGuard()`, or `getRegisteredGuards()` cannot mutate engine
identity, enabled state, priority, evaluation selection, or ordering. Preserve
the supported non-mandatory `disableGuard` behavior through an engine-owned
state transition. Mandatory disable/unregister protection must remain exact.

### F3 immutable Gateway bootstrap configuration

Defensively snapshot all constructor configuration, including a distinct
canonical immutable bypass list. Neither the caller's original object/array nor
a getter result may mutate behavior. Reject authority-changing runtime updates
after construction/bootstrap with a deterministic explicit error or an
equivalently fail-closed immutable API. Do not add a global configuration
service, mutable singleton authority, secret, or new dependency.

### F4 exact canonical bypass matching

Use normalized whole-value equality for both `check()` and `checkContext()`.
Canonicalization may trim and case-fold, but must never accept a prefix,
suffix, token segment, delimiter extension, or substring collision. Reject or
ignore empty/malformed bypass entries deterministically. A malformed action
must fail closed without an accidental TypeError and without engine execution.

### Dedicated adversarial tests

Cover at minimum:

- mutation of original registered guard fields and evaluation function;
- mutation attempts through both guard accessors;
- priority/order stability and mandatory protection after hostile mutation;
- supported non-mandatory disable behavior;
- mutation of constructor config, constructor bypass array, getter config, and
  getter bypass array;
- post-bootstrap changes to `enforceAll`, `hardBlock`, `hardEscalate`, bypass
  values, defaults, and control mode;
- exact normalized matches and collisions such as `health-check-ping`,
  `pre-health-check`, `health-check:admin`, `openapi-v2`, empty entries, and
  case/whitespace variants;
- identical behavior across `check()` and `checkContext()`;
- malformed runtime action handling;
- unchanged RFR-R1 mandatory BUILD-authority composition.

## Required Artifact Manifest

| Path | Required state | Required at handoff |
| --- | --- | --- |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | F2 defensive registered-guard boundary | YES |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts` | F2 hostile-reference tests plus RFR-R1 regression | YES |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | F3/F4 immutable config and exact matching | YES |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.test.ts` | F3/F4 adversarial tests | YES |
| `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` | semantic review plus only affected current fingerprints/evidence text | YES |
| `docs/reviews/CVF_RFR_R2_IMMUTABLE_MANDATORY_CORE_WORKER_RETURN_2026-08-24.md` | truthful no-commit worker evidence | YES |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| exact six-path manifest | implement, test, semantically reconcile, and return every required artifact |
| all other paths | keep read-only and report any necessary seventh path as blocker |

## Required Proof Manifest

| Proof ID | Required literal | Evidence owner |
| --- | --- | --- |
| P1 | `npx vitest run src/index.test.ts src/runtime/mandatory-gateway.test.ts --pool forks` | worker |
| P2 | `npm test` | worker |
| P3 | `npm run check` | worker |
| P4 | `python governance/compat/check_system_chain_map_freshness.py --enforce` | worker |
| P5 | `python governance/compat/check_governed_file_size.py --enforce` | worker |
| P6 | `python governance/compat/run_worker_return_fast_gate.py` | worker |
| P7 | `git diff --check` | worker |
| P8 | `git diff --cached --name-only` | worker |
| P9 | `git rev-parse HEAD` | worker |
| P10 | `git status --short` | worker |

## Required Proof Manifest Atomic Literal Discipline

Each proof row contains exactly one command literal. Do not combine commands or
replace the compact worker-return gate with a self-selected checker subset.

## Verification Commands

```powershell
Set-Location EXTENSIONS/CVF_GUARD_CONTRACT
npx vitest run src/index.test.ts src/runtime/mandatory-gateway.test.ts --pool forks
npm test
npm run check
Set-Location ../..
python governance/compat/check_system_chain_map_freshness.py --enforce
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --cached --name-only
git rev-parse HEAD
git status --short
```

## Mandatory Gate-Failure Remediation Protocol

For an in-scope failure, read the failing source/test/checker, repair the exact
cause, and rerun the narrow failed proof before the compact full gate. Do not
weaken assertions, skip tests, change required gates, fabricate evidence, or
edit outside the manifest. A mandatory failure needing another path is a
truthful `BLOCKED_WITH_REASON` return.

## Execution Plan

1. Capture execution HEAD/status, verify hashes, and complete required reads.
2. Implement F2 in the engine and its existing root test suite.
3. Implement F3/F4 in Mandatory Gateway and its dedicated test suite.
4. Run focused proof, then full package and TypeScript proof.
5. Semantically review `CONTRACT_TO_RUNTIME`, refresh only affected
   fingerprints/evidence text, and run the freshness guard.
6. Author the truthful worker return, run its compact gate, confirm empty
   staging and unchanged HEAD, then stop for independent review.

## Evidence Requirements

Record exact execution base/HEAD, five input hashes, six-path name-status,
staging output, focused and full test counts, TypeScript result, freshness and
file-size results, worker-return fast-gate result, diff hygiene, any residual
risk, zero provider/live calls, and the no-commit statement.

## Acceptance Criteria

- all F2 original/accessor-reference mutation probes preserve engine behavior;
- mandatory protection and supported non-mandatory disable behavior coexist;
- constructor/getter nested configuration mutation cannot widen authority;
- post-bootstrap authority-changing configuration updates reject;
- bypass is exact canonical whole-value equality across both entry points;
- malformed and collision cases fail closed without accidental exceptions;
- RFR-R1 composition and the full package remain green;
- exact six-path manifest, unchanged HEAD, and empty staging are proven.

## Review Gate

The reviewer will reject self-acceptance, assertion weakening, mutable nested
references, partial entry-point coverage, hash-only system-map updates, missing
malformed/collision probes, scope drift, staging, worker commits, or any failed
mandatory proof. Passing worker tests is necessary but not sufficient.

## Closure Checklist

- [ ] Source hashes matched before edit.
- [ ] Exact six-path worker manifest matched.
- [ ] F2-F4 adversarial matrix passed.
- [ ] Focused, full-package, TypeScript, freshness and file-size proof passed.
- [ ] Worker-return fast gate and diff hygiene passed.
- [ ] HEAD remained unchanged and staging remained empty.
- [ ] Reviewer receives the complete uncommitted diff and evidence.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_worker_experience_retrospective.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_system_chain_map_freshness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | exact Source Verification columns; worker-return status and headings; Agent Operation Trace labels; retrospective enums; exact manifest; `git diff --name-status` |
| gateRunPurpose | confirm R2 source/evidence shape and prevent dependent-failure discovery at return time; not first discovery |
| claimBoundary | checker read-ahead and local tests do not prove deployment, live behavior, or reviewer acceptance |

## Worker Output Checker Read-Ahead Mandate

Before authoring the worker return, read the checker source for its review path,
docType, worker-return status, trace, epistemic, rescan/corpus, learning,
machine-closure, and no-commit evidence conditions. Use actual headings, not a
checklist containing heading syntax.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_RFR_R2_IMMUTABLE_MANDATORY_CORE_WORKER_RETURN_2026-08-24.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real sections: Purpose; Scope / Methodology; Findings / Position; Risk
/ Corrective Action; Checker Source Read-Ahead Block; Agent Operation Trace
Block; Delta Execution Claim Boundary Control Block; Public Export Disposition;
External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus
Completeness And Report Integrity; Finding-To-Governance Learning Disposition;
Epistemic Process Block; Machine Closure Package; Claim Boundary; git status
--short; Changed Files; Worker Experience Retrospective; Command Evidence; and
No-Commit Statement.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_RFR_R2_IMMUTABLE_MANDATORY_CORE_COMPLETION_2026-08-24.md` |
| reviewerOwnedClosurePaths | optional completion review; R2-only roadmap transition; accepted six-path material diff; later continuity surfaces |
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
| phase | RFR-R2 implementation return |
| baseHeadFor(phase) | dispatchBaseHead=`804168de1997504bafd500b4159c981dec4d7627`; executionBaseHead captured from committed dispatch HEAD; closureBaseHead reviewer-set after return |
| changedSetScope(phase) | exact six-path worker manifest |
| traceScope(phase, actor) | worker reads, edits, tests and returns; reviewer independently inspects, probes, repairs and commits |
| commitOwner(phase) | reviewer/closer; worker commit forbidden |
| crossBatchIsolation | R3-R6 and all external-effect lanes remain parked |
| nextMoveSurfaces | worker return, reviewer decision, material commit, separate continuity sync |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | Guard Contract engine and Mandatory Gateway | exact six-path local implementation; worker cannot stage, commit, or accept | source hashes, focused/package tests and reviewer evidence | repository-local TypeScript APIs only | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no R2 adapter work | no external ingress, authentication, approval, receipt, raw-data, mutation, runtime or public authority | adapter paths excluded from manifest | deferred to fresh adapter authority; no invocation in this tranche | DEFERRED_WITH_REASON |

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | YES_LOCAL_SOURCE_ONLY |
| freshnessVerificationMode | LOCAL_SOURCE_AND_TEST_RECOMPUTE_REQUIRED |
| reason | worker may change local Guard Contract behavior but may not claim provider/live, deployment, production, or universal caller adoption |
| requiredFutureAction | reviewer independently reruns local proof; any later live claim requires separate source-verified authority |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| proposed R2 artifact paths | pre-authoring `Test-Path` returned false for baseline, work order, worker return, and completion review | ABSENT_BEFORE_AUTHORING |
| same-tranche token search | search roots `docs` and `CVF_SESSION`; command `rg -n "RFR-R2|Immutable Mandatory Core|immutable mandatory core" docs CVF_SESSION`; only generic roadmap R2 wording occurred | NO_SAME_OWNER_COLLISION |
| owner coverage | source/tests/docs/JSON/external-evidence review maps all work to existing engine/Gateway owners | EXISTING_OWNER_ENRICHMENT |

## Evidence Reuse And Encoding Plan

| Field | Value |
| --- | --- |
| verificationMode | RECOMPUTE_REQUIRED |
| priorVerificationArtifact | `docs/reviews/CVF_RFR_R1_BUILD_AUTHORITY_CLOSURE_COMPLETION_2026-08-24.md` |
| priorVerificationAnchor | material commit `a670343706c4fa21427a55a9c2ba464b9cef6cd4` |
| recomputeReason | R2 changes engine/Gateway authority behavior, so focused/full/typecheck and freshness proof must be fresh |
| unicodePathHandling | preserve UTF-8 source; use repo-relative literal paths and PowerShell `-LiteralPath` for hashes |
| extractedTextAuthority | N/A with reason: no extracted document text is an authority input |
| freshRecomputeRequired | YES |

## Commit Mode And Base-Anchor Lifecycle

Worker captures the committed dispatch HEAD as `executionBaseHead`, never
stages or commits, and reports unchanged HEAD. Reviewer captures a fresh
`closureBaseHead` after return and owns the material commit. Session sync is a
separate commit after accepted material identity exists.

## Pending Artifact Evidence Finality

Worker evidence remains `COMPLETE_PENDING_REVIEW` and cannot claim closure,
final material identity, clean worktree, or reviewer acceptance. The untracked
worker-return path must appear in actual status evidence.

## Self-Reported Gate Evidence Consistency

Report only commands actually executed and exact observed counts/status. A
failed or skipped mandatory command remains a blocker; future-tense or expected
results are not pass evidence.

## Near-Threshold Owner Maintainability Plan

No near-threshold exception is pre-authorized. If either production file
crosses a governed size threshold, refactor only inside the same exact file or
return `BLOCKED_WITH_REASON` for a required additional path. Do not add an
exception registry entry.

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: RFR-R2 changes only in-memory engine/Gateway
authority behavior, tests, one fingerprint registry, and a review packet. It
creates no durable storage, queue, index family, relocation, or migration.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: RFR-R2 is a named-file remediation of verified
current Guard Contract findings. It performs no legacy corpus absorption,
coverage-index reassignment, source intake, workflow-chain import, or
foundation-plane migration.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent returned output |
| Chain map route | external questions to governed local verification, existing-owner R2 remediation, and independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Guard Contract engine and Mandatory Gateway |
| Disposition | ADAPT only the locally verified F2-F4 deltas; no external code or subsystem import |
| Claim boundary | external questions are provenance input, not implementation authority, runtime evidence, or closure proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH --max-results 50 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no additional ADIF constraint; worker must run its own pre-execution query |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | orchestrator/dispatcher |
| Provider or surface | private provenance repository |
| Session or invocation | `rfr-r2-dispatch-20260824` |
| Working directory | repository root |
| Command or tool surface | governed reads, Git, source/hash inspection, scaffold, ADIF resolver, apply patch, pre-dispatch gates |
| Target paths | paired R2 baseline and work order |
| Allowed scope source | operator's explicit 2026-08-24 R2 continuation instruction |
| Before status evidence | clean worktree at HEAD `804168de1997504bafd500b4159c981dec4d7627` |
| After status evidence | paired R2 authority paths pending dispatch commit |
| Diff evidence | `git diff --name-status` must contain only the paired authority paths before commit |
| Approval boundary | dispatch authority only |
| Claim boundary | no implementation, provider/live, public, deploy, push, or production claim |
| Agent type | dispatcher |
| Invocation ID | `rfr-r2-dispatch-20260824` |
| Expected manifest | paired R2 baseline and work order |
| Actual changed set | paired R2 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: two new authority files only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | exact local RFR-R2 no-commit worker dispatch |
| claimDisposition | CLAIM_REJECTED until worker tests and independent review pass |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt exists |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatcher made no production-source edit |
| invocationBoundary | local repository authoring and checker processes only |
| interceptionBoundary | no provider, network, CLI/MCP, public, deployment, push, or production action |
| claimLanguage | worker-authorized local remediation, not accepted closure |
| forbiddenExpansion | seventh path, R3-R6, new subsystem, external adapter, provider/live, credentials, deploy, public sync, push, or production |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for source-hash drift, any necessary seventh path,
unowned subsystem, RFR-R1 contradiction, mandatory proof failure that cannot be
fixed in scope, dependency/network requirement, secret or quota use, external
effect, or new critical authority defect. Otherwise return
`COMPLETE_PENDING_REVIEW` with the full no-commit evidence packet.

## Operator Checkpoint

No checkpoint is required for in-scope local reversible repairs. Fresh operator
authority is required for any manifest expansion or external effect and before
R3 dispatch.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance worker dispatch; public sync remains forbidden.

## Claim Boundary

This work order authorizes only the exact RFR-R2 six-path local implementation
and proof. It does not prove closure, grant worker commit authority, authorize
R3-R6, or permit provider/live, credentials, external adapters, deployment,
public sync, push, or production.

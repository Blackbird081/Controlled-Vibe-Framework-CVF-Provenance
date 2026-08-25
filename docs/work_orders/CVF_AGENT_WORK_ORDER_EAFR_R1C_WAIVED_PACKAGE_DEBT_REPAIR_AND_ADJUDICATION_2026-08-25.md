# CVF Agent Work Order - EAFR-R1C Waived Package Debt Repair And Adjudication

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Work order ID: EAFR-R1C

Date: 2026-08-25

dispatchBaseHead: `f8cf62c743c6c5ad08a790400ba26a2c05679997`

executionBaseHead: worker must capture actual HEAD and require this committed packet as ancestor

closureBaseHead: reviewer captures the committed dispatch head

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through the committed EAFR roadmap and the explicit bounded R1 waiver

Reviewer/closer: current independent orchestrator/reviewer

Worker: package-debt repair worker role

## Dispatch Prompt Envelope

Batch ID: EAFR-R1C-WAIVED-PACKAGE-DEBT.

Role: no-commit package-debt repair worker.

Canonical packet: this committed work order and its paired baseline.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: R5 is accepted bounded at material commit `04a5cf40e`; the
three waived criteria and their defect root causes were freshly verified at
dispatch head `f8cf62c74`.

Do-not-misread notes: R1C repairs test-side debt and adjudicates what cannot be
repaired; it is not authority to edit production source, change configuration or
package manifests, run a build, use credentials, or relax any R2 through R6
criterion. Improvement is not greenness, and a waived failure is never PASS.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, `DESIGN.md`, this packet, paired baseline, the R1 explicit waiver
closure, the R5 completion review, every pinned input and the applicable checker
sources for every output class.

Return contract: exact thirteen paths, no stage/commit, `COMPLETE_PENDING_REVIEW`
or `BLOCKED_WITH_REASON`.

Worker return path: `docs/reviews/CVF_EAFR_R1C_WAIVED_PACKAGE_DEBT_REPAIR_AND_ADJUDICATION_WORKER_RETURN_2026-08-25.md`

sourceAuthority: paired GC-018 baseline, committed EAFR roadmap, explicit bounded R1 waiver closure, accepted R1A runner fix, and source-verified cvf-web/LPF files named in this packet

## Purpose

Convert the three criteria that the explicit bounded operator waiver left as
named debt into either proven repairs or fresh, evidence-bearing adjudications,
so EAFR-R6 reconciliation can proceed against real package state instead of a
standing waiver.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R1C --title "Waived Package Debt Repair And Adjudication" --date 2026-08-25 --base f8cf62c74 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact thirteen-path manifest, verified root causes, disposition contract, safe-command discipline, production-source protection rule and per-criterion evidence requirements |
| checkerReadAheadConfirmation | applicable dispatch and worker-output checker sources read |
| docOnlyNewFields | Waived Criterion Disposition Contract; Verified Defect Root Causes; Safe Command Discipline |
| claimBoundary | dispatch authoring only |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R1 explicit bounded waiver | `docs/reviews/CVF_EAFR_R1_EXPLICIT_BOUNDED_OPERATOR_WAIVER_CLOSURE_2026-08-25.md`; three criteria recorded `WAIVED_WITH_NAMED_DEBT` naming R1C as follow-up owner | ACCEPT |
| R5 bounded closure | `docs/reviews/CVF_EAFR_R5_RETRIEVAL_EVIDENCE_SEMANTICS_AND_ADMISSION_BOUNDARY_COMPLETION_2026-08-25.md`; material commit `04a5cf40e3a396404b1aff0816534e4d8a6a1567` | ACCEPT |
| R1C roadmap authority | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md`, R1C row and mandatory-before-R6 interlock | ACCEPT |
| R1A non-live runner fix | `docs/reviews/CVF_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_COMPLETION_2026-08-25.md`; accepted at `ef142bfb2` because that material commit exists | ACCEPT |

## Authority And Scope

Governing baseline:
`docs/baselines/CVF_GC018_EAFR_R1C_WAIVED_PACKAGE_DEBT_REPAIR_AND_ADJUDICATION_2026-08-25.md`.

The worker may edit or create exactly the thirteen paths in Write Ownership. No
other path is writable. The worker must not stage or commit.

## Authority Chain

Operator EAFR authority and explicit R1 waiver -> committed roadmap -> paired
baseline -> this work order -> no-commit worker -> independent reviewer/closer.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| repair or freshly adjudicate waived typecheck debt | Required Implementation; Criterion A | twelve test files and worker return | cvf-web typecheck before/after counts | PASS |
| repair or freshly adjudicate waived non-live suite debt | Required Implementation; Criterion B | eleven suite test files and worker return | cvf-web non-live suite before/after counts | PASS |
| repair or freshly adjudicate waived build debt | Required Implementation; Criterion C | worker return adjudication | documentary adjudication against committed R1 evidence | PASS |
| keep R1C mandatory before R6 | Closure Checklist; Machine Closure Package | reviewer closure and roadmap conversion | reviewer closure conversion | PASS |

## Required First Reads

Read `AGENTS.md`, `CVF_SESSION_MEMORY.md`, the bootstrap read model, active
handoff, `docs/reference/guard_orientation/README.md`, governed literal
gotchas, `DESIGN.md`, paired baseline, this work order, the R1 explicit waiver
closure, the R5 completion review, every pinned source and worker-output
checker sources named below. Resolve the full session registry only for a
targeted missing or contradictory fact.

## Agent Roles

Operator owns scope; dispatcher owns the packet; worker repairs, measures and
adjudicates without commit; reviewer independently challenges, repairs, closes
and commits.

## Pre-Flight Checks

Confirm clean worktree, empty staging, actual HEAD, committed dispatch ancestry,
all pinned hashes, absent worker-return path, Node/npm availability and zero
live-test selection. Capture the before-state typecheck and non-live suite
counts before any edit. Hash drift or an existing return path blocks before
edits.

## Write Ownership

Exactly these thirteen paths:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.test.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.test.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.governance-trace.test.ts`
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.knowledge.test.ts`
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/override/route.governance.test.ts`
7. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/knowledge/ingest/route.test.ts`
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/knowledge/ingest/w116-cp5-delta.test.ts`
9. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/intake/route.governance.test.ts`
10. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.test.ts`
11. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/qbs/front-door-clarification/route.test.ts`
12. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-runtime-adapter.test.ts`
13. `docs/reviews/CVF_EAFR_R1C_WAIVED_PACKAGE_DEBT_REPAIR_AND_ADJUDICATION_WORKER_RETURN_2026-08-25.md`

No production source, deletion, rename, checker, package manifest, vitest or
tsconfig configuration, lockfile, environment file, generated aggregate,
session, roadmap, key, adapter, public clone or deployment edit.

## Pinned Input Hashes

| Path | SHA-256 |
| --- | --- |
| `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md` | `1d8948ca091ab984ce272ad44ff291ce0c00f24146ab41d73bde14d3c3601a93` |
| `docs/reviews/CVF_EAFR_R1_EXPLICIT_BOUNDED_OPERATOR_WAIVER_CLOSURE_2026-08-25.md` | `16b3dd69c04e65e15bd481abc987acf6d6886ba8a05740cf1ec182648c011899` |
| `docs/reviews/CVF_EAFR_R5_RETRIEVAL_EVIDENCE_SEMANTICS_AND_ADMISSION_BOUNDARY_COMPLETION_2026-08-25.md` | `23c285f3bd376b3686839bcdf96b2d09e0b4aed6348968f9dfa9b3d6c8d12a3a` |
| `docs/reviews/CVF_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_COMPLETION_2026-08-25.md` | `f303519b013ab8e0c50db7b79c389db4251cf680189b0d29407e46980766e2dd` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.test.ts` | `90e519547418b27d36f6e566f751c13565c76ed69470762541dc29c4e1006af8` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | `9bc1c83b137a25d22e785dd48c3e1dbb3033c6284cf941162c967e7fb5f5be73` |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/vitest.config.ts` | `cf2b92acfe10d67855020fbfcb4cca1c3ce29232e7f008ce313c99b1bc72f4fc` |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/package.json` | `17a143768979030a1b2a4fe4f9d69a36b1d17f35397e25dfcf47fca839b14f55` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | `48163e0e8e2e8a16986af118af0060a9d38c6ae3257575df77a4facfd7ee710e` |

The new worker-return path must be absent. Every hash is calculated at
`f8cf62c74`; mismatch returns `BLOCKED_WITH_REASON` before material edits.

## Verified Defect Root Causes

Verified directly at `f8cf62c74`. The worker must re-derive each and report any
divergence rather than inheriting these findings.

| Criterion | Verified root cause | Repairability at dispatch time |
| --- | --- | --- |
| typecheck | Four mock objects construct `ProviderExecutionBridgeResult` without the required `materialContextManifestDisposition` field declared non-optional at line 62 of the gateway interface. Entirely test-side; no production source is mistyped. | LOCALLY_REPAIRABLE |
| full non-live suite | Route authorization now flows through `authorizeRouteGovernanceProof`, while affected route tests arrange only the older session-mock shape and default the session to null, so routes correctly fail closed with 401 and assertions expecting 200, 400 or 403 fail. Seventeen of twenty-nine failures follow this pattern; the remainder are count and threshold assertions needing per-file diagnosis. | LIKELY_REPAIRABLE_PENDING_PER_FILE_DIAGNOSIS |
| build | Auth.js environment validation fails during page-data collection, depending on environment and credential state that remains parked and unauthorized. | NOT_REPAIRABLE_WITHOUT_PARKED_AUTHORITY |

## Waived Criterion Disposition Contract

Each criterion must terminate in exactly one disposition, with evidence:

- `REPAIRED_AND_GREEN`: passes now, proven by a fresh transcript and exact
  before/after counts.
- `PARTIALLY_REPAIRED_WITH_NAMED_RESIDUAL`: measurable improvement with every
  remaining failure named, counted and root-caused.
- `FRESHLY_ADJUDICATED_BLOCKED`: cannot be repaired inside the authorized
  manifest and parked authority, with the exact blocking condition, the
  authority that would be required, and why that authority is not open.

`WAIVED`, `ACCEPTED_AS_IS`, and relabeling a failing command as PASS are
forbidden. Improvement that is not greenness must not be reported as green.

## Required Implementation

### Criterion A - cvf-web typecheck

- Capture the exact before-state error count and the full error list.
- Repair the four mock construction sites in
  `provider-binding.test.ts` so each satisfies `ProviderExecutionBridgeResult`,
  supplying a real disposition value consistent with the gateway type rather
  than a cast that erases the contract.
- Do not widen, relax or edit the gateway interface, and do not add
  `@ts-expect-error` or `any` to silence the diagnostic.
- Re-run the typecheck and record the exact after-state count.
- Assign a disposition from the contract.

### Criterion B - cvf-web full non-live suite

- Capture the exact before-state counts and the failing-file list.
- For each of the eleven failing files, diagnose the real cause before editing.
  Where the cause is authorization-arrangement drift, update the test to
  arrange the authorization path the route actually uses, so the test proves
  the route's real behavior.
- Where a failure reveals a genuine production defect, do not edit production
  source and do not weaken the assertion. Record the finding and let the
  criterion terminate as partially repaired or freshly adjudicated.
- Re-run the non-live suite and record exact after-state counts and any
  residual failing files with root causes.
- Assign a disposition from the contract.

### Criterion C - cvf-web build

- Do not run `npm run build`.
- Adjudicate documentarily from the committed R1 evidence and current source
  inspection: state the blocking condition, the authority that would be needed
  to prove it, and why that authority is parked.
- Assign a disposition from the contract; `FRESHLY_ADJUDICATED_BLOCKED` is the
  expected outcome unless the worker finds evidence that the blocker no longer
  exists without any parked authority.

## Production Source Protection Rule

R1C is a test-side repair tranche. If a failing test proves a real production
defect, the worker must not fix production source under this manifest. It must
record the finding, mark the criterion appropriately, and return for a separate
source-verified authorization. Changing a test assertion to match incorrect
production behavior is forbidden and is treated as a weakened-admission defect.

## Safe Command Discipline

R5 recorded six unintended provider calls caused by a required command that was
unsafe under ambient credentials. For R1C:

- LPF `npm test` is FORBIDDEN. Invoke the LPF package suite only with the
  explicit provider-test exclusion shown in Required Commands.
- cvf-web `npm run test:run` is permitted; its script already excludes both
  live test extensions.
- `npm run test:live`, `npm run test:e2e`, Playwright, `npm run build`, any
  provider or live test pattern, and any credential-bearing invocation are
  FORBIDDEN.
- If a permitted command still selects a provider test, stop, return
  `BLOCKED_WITH_REASON`, and disclose any call made.

## Adversarial Proof Matrix

| Vector | Boundary under test | Required result |
| --- | --- | --- |
| test edited to match wrong production behavior | assertion integrity | forbidden; recorded as residual instead |
| production source edited to make a test pass | manifest boundary | forbidden; blocked return |
| gateway interface widened to absorb the mock defect | out-of-manifest edit | forbidden; blocked return |
| type diagnostic silenced by cast or suppression | typecheck integrity | forbidden; criterion not green |
| partial improvement reported as green | disposition contract | forbidden; must be partially repaired with named residual |
| build criterion marked PASS without a build | disposition contract | forbidden; documentary adjudication only |
| LPF package suite invoked without provider exclusion | safe command discipline | forbidden; blocked return with disclosure |
| residual failure left uncounted or unnamed | evidence completeness | forbidden; every residual named and root-caused |

## Acceptance Criteria

- exactly thirteen worker paths and no others changed;
- before and after counts recorded for typecheck and the non-live suite;
- each of the three criteria carries exactly one contract disposition with
  evidence;
- every residual failure is named, counted and root-caused;
- no production source, configuration, package manifest, checker or environment
  path is changed;
- no assertion is weakened to match incorrect production behavior;
- zero provider calls, with an explicit statement to that effect;
- worker-return fast gate passes; staging is empty; worker HEAD is unchanged;
- zero live/provider/network/key/build/public/deploy/push effect.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EAFR-R1C",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/",
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/",
    "docs/reviews/",
    "docs/baselines/CVF_GC018_EAFR_R1C_WAIVED_PACKAGE_DEBT_REPAIR_AND_ADJUDICATION_2026-08-25.md"
  ],
  "claims": ["waived package debt is repaired or freshly adjudicated with evidence"],
  "requiredProof": ["before/after typecheck counts", "before/after non-live suite counts", "per-criterion dispositions", "residual root causes", "hashes", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["production source edit", "configuration or package manifest edit", "build command", "live/provider/network/key call", "weakened assertion", "worker stage or commit", "public/deploy/push"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| worker role | no-commit package-debt repair worker |
| reviewer role | independent reviewer/closer |
| external intake | none; all claims verified in CVF-owned sources |
| escalation condition | hash drift, production defect discovered, required extra path, live or build need, or unsafe command selection |
| risk sensitivity | assertion integrity and honest disposition reporting |
| scope classification | exact thirteen-path local test-side repair and adjudication |

## Required Commands

Run from cvf-web:

1. `npm run check` before edits, capturing the exact error count and list;
2. `npm run test:run` before edits, capturing exact counts and the failing-file
   list;
3. `npm run check` after edits;
4. `npm run test:run` after edits;
5. focused re-runs of each repaired file with `npx vitest run <path>`.

Run from the LPF package, only if LPF regression evidence is needed:

6. `npx vitest run --config vitest.config.ts --exclude "tests/**/*.alibaba.test.ts"`.

Run from repository root:

7. bounded positive/negative searches proving no production source,
   configuration, package manifest or checker path was touched;
8. recompute pinned hashes for all inputs outside the worker manifest;
9. `python governance/compat/run_worker_return_fast_gate.py`;
10. `git diff --check`, `git diff --name-status`,
    `git status --short --untracked-files=all`, and
    `git diff --cached --name-only`.

Do not run LPF `npm test`, `npm run build`, live tests, Playwright, release
gate, provider, network, environment/key, public-sync, deployment or
installation commands.

## Execution Plan

1. Capture startup, clean status, empty staging, HEAD, ancestry, return-path
   absence, pinned hashes and both before-state measurements.
2. Repair Criterion A and re-measure the typecheck.
3. Diagnose and repair Criterion B file by file, re-measuring the suite.
4. Adjudicate Criterion C documentarily without running a build.
5. Write the worker return from fresh evidence, run every safe command, and
   return without staging or committing.

## Verification Commands

Run every Required Command, including the full:

`python governance/compat/run_worker_return_fast_gate.py`

Individual checker substitution is forbidden.

## Evidence Requirements

Report pre/post HEAD and status; exact changed paths; before/after typecheck
and suite counts; per-file root causes for repaired and residual failures;
per-criterion contract dispositions; positive/negative search counts;
non-manifest source hashes; worker-return fast gate output; empty staging; an
explicit zero-provider-call statement; and explicit zero external-effect
evidence. Failed, skipped, timed-out or ambiguous commands stay visible and
cannot be relabeled as passing.

## Fail Conditions

Return `BLOCKED_WITH_REASON` for hash drift, a discovered production defect
requiring a source fix, a needed extra path, an unsafe command selection or any
provider call, a weakened assertion, a required configuration or manifest
change, or a build/live/credential requirement.

## Worker Autonomy / No-Question Rule

Repair all allowed-scope defects and rerun safe evidence without asking the
operator. Do not expand scope. A criterion that cannot be repaired inside scope
is adjudicated with evidence, not waived and not silently left failing.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: R1C changes test-side state, so typecheck counts, suite counts, per-file diagnoses, hashes and boundary searches must be fresh against the pending worker tree

priorVerificationArtifact: R1 explicit waiver closure, R1A runner acceptance and R5 completion review

priorVerificationAnchor: pinned SHA-256 values in this work order

freshRecomputeRequired: typecheck and suite before/after counts, per-file root causes, hashes, boundary searches and worker-return gate

unicodePathHandling: use literal repository-relative paths and UTF-8-safe readers

extractedTextAuthority: CVF-governed sources and fresh local command output only

## Current Runtime Freshness Verification

Direct inspection at `f8cf62c74` confirms exactly four typecheck errors in one
test file, twenty-nine non-live suite failures across eleven files, a
route-authorization helper that the affected tests do not arrange, and an LPF
test configuration with no provider-test exclusion. No live behavior is claimed
or required.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R1C is authorized and mandatory before R6 | ROADMAP_AUTHORITY | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md` | Proposed Tranches, EAFR-R1C and EAFR-R6 rows | EAFR-R1C | EAFR roadmap | ACCEPT |
| exactly three criteria are waived debt, not PASS | OWNER_AUTHORITY | `docs/reviews/CVF_EAFR_R1_EXPLICIT_BOUNDED_OPERATOR_WAIVER_CLOSURE_2026-08-25.md` | Machine Closure Package, Typecheck/Full non-live suite/Build rows | WAIVED_WITH_NAMED_DEBT | R1 explicit waiver closure | ACCEPT |
| typecheck failures are confined to one test file | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.test.ts` | lines 46, 150, 165, 203 | bridgeResult; inline execute mocks | cvf-web LPCI provider binding test | ACCEPT |
| the missing field is required by the gateway interface | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | ProviderExecutionBridgeResult interface, lines 57-63 | ProviderExecutionBridgeResult; materialContextManifestDisposition | model gateway execution bridge | ACCEPT |
| route authorization flows through the governance proof helper | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 136-241 | authorizeRouteGovernanceProof; verifySessionCookie | Web route governance proof helper | ACCEPT |
| failing route tests default the session to null | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.test.ts` | beforeEach, lines 127-128 | verifySessionCookieMock | cvf-web LPCI query route test | ACCEPT |
| the non-live runner already excludes both live extensions | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts block, non-live runner entry | scripts non-live test runner entry | cvf-web package manifest | ACCEPT |
| LPF package test selection has no provider-test exclusion | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/vitest.config.ts` | test.include block | include | LPF vitest configuration | ACCEPT |
| the unsafe-command incident grants no live authority | OWNER_RECONCILIATION | `docs/reviews/CVF_EAFR_R5_RETRIEVAL_EVIDENCE_SEMANTICS_AND_ADMISSION_BOUNDARY_COMPLETION_2026-08-25.md` | R5-RF6 section | providerCallCount | R5 completion review | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_equivalence_claim_evidence.py`; `governance/compat/check_worker_experience_retrospective.py` |
| literalTokensReviewed | dispatch status; Source Verification Block; Current Runtime Freshness Verification; Evidence Reuse scalar fields; worker-return headings; trace and delta labels; equivalence disposition tokens; retrospective four-field block |
| gateRunPurpose | confirm as evidence that the completed source-verified packet matches checker shape |
| claimBoundary | checker conformance does not prove that any waived criterion is repairable |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`package debt repair`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "package debt repair" --role worker --lifecycle-phase implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | ordinary CVF controls apply |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact R1C baseline, work-order and return paths | all absent before dispatch authoring | PASS |
| token search | `EAFR-R1C` existed only in roadmap, R1 waiver and continuity next-move text; the separate `EAIC-KR-R1C` lane from 2026-07-23 is a different batch and does not collide | PASS |
| collision decision | repair the twelve existing failing test files in place; create no new test file, helper, checker or configuration | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | cvf-web test suite and typecheck surface | local package health evidence only | before/after counts and per-file root causes | local source only | REPAIR_BOUNDED |
| EXTERNAL_AGENT_CLI_MCP | none | no CLI/MCP read, authority or adapter behavior is created or changed | unchanged adapter boundaries | separate source-verified work order required | DEFERRED_WITH_REASON |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | no-commit worker plus independent reviewer |
| phase | implementation pending worker return |
| baseHeadFor(phase) | dispatchBaseHead=f8cf62c74; executionBaseHead=worker captures; closureBaseHead=reviewer captures |
| changedSetScope(phase) | exact thirteen-path worker manifest |
| traceScope(phase, actor) | local test-side repair, re-measurement and criterion adjudication |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean worktree required; R6, RFR and all external effects parked |
| nextMoveSurfaces | worker return then independent reviewer decision |

## Worker Output Checker Read-Ahead Mandate

Before writing each changed test or worker-return artifact, read every checker
source applicable to its docType, path family and conditional content. Derive
actual headings and literal tokens before authoring; checklist prose is not a
substitute for the real sections.

## Work-Order Fulfillment Manifest

| Artifact group | Required worker action |
| --- | --- |
| provider binding test | satisfy the required gateway result field without widening or suppressing the type |
| eleven failing suite test files | diagnose per file, arrange the real authorization path, and never weaken an assertion |
| build criterion | adjudicate documentarily without running a build |
| worker return | record complete uncommitted evidence with per-criterion dispositions |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_EAFR_R1C_WAIVED_PACKAGE_DEBT_REPAIR_AND_ADJUDICATION_WORKER_RETURN_2026-08-25.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must carry the full review-family/no-commit shape, cite this work
order, report the actual dirty paths, carry one contract disposition per
criterion, and preserve every failure or residual without relabeling.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_EAFR_R1C_WAIVED_PACKAGE_DEBT_REPAIR_AND_ADJUDICATION_COMPLETION_2026-08-25.md` |
| reviewerOwnedClosurePaths | worker manifest, return, optional completion review, EAFR roadmap and continuity |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

Reviewer must independently challenge each criterion disposition, rerun both
measurements, confirm no assertion was weakened and no production source
changed, and verify the zero-provider-call claim.

## Review Gate

Only the independent reviewer/closer may accept, repair authorized defects, run
closure gates and commit. Acceptance requires direct source inspection and fresh
recomputation, not worker self-report.

## Closure Checklist

- exact thirteen-path worker diff and empty staging;
- before/after typecheck and suite counts recorded;
- one contract disposition per criterion with evidence;
- every residual failure named, counted and root-caused;
- no production source, configuration, manifest or checker change;
- no weakened assertion and no suppressed type diagnostic;
- zero provider calls and zero build/live/credential action;
- R2 through R6 criteria unchanged and no waiver precedent created.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with all acceptance evidence, including a
contract disposition for every criterion. Otherwise return
`BLOCKED_WITH_REASON`, naming the first unresolved condition and preserving
partial or failed evidence.

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Foundation Storage Layout Block | N/A with reason: R1C edits twelve existing test files in place and creates no new foundation family file or storage topology |
| Protected storage paths | memory foundation filenames, folder front door, generated aggregates and indexes remain unchanged |
| Follow-up condition | any new stable foundation file, split, relocation or generated-state edit needs separate authorization |

## Operator Checkpoint

operator.checkpoint.waiver: none. Live/provider/build/credential/public/
destructive or production-source expansion requires fresh explicit authority.
This work order creates no waiver precedent and does not relax R2 through R6.

## Commit Prompt Readiness

- worker commit: forbidden;
- reviewer material commit: only after independent acceptance;
- session sync: separate commit;
- push/public sync: unauthorized.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/orchestrator |
| Provider or surface | private local repository |
| Session or invocation | EAFR-R1C dispatch authoring, 2026-08-25 |
| Working directory | repository root |
| Command or tool surface | source reads, searches, hashes, scaffold, ADIF resolver, safe typecheck and non-live suite measurement, packet authoring and gates |
| Target paths | R1C baseline and work order |
| Allowed scope source | EAFR roadmap R1C row and explicit bounded R1 waiver |
| Before status evidence | clean worktree at HEAD `f8cf62c743c6c5ad08a790400ba26a2c05679997`; staging empty |
| After status evidence | two dispatch artifacts pending commit |
| Diff evidence | `git diff --name-status` over exact dispatch document set |
| Approval boundary | R1C dispatch only |
| Claim boundary | no worker implementation, live, provider, build, adapter or public effect |
| Agent type | dispatcher |
| Invocation ID | `eafr-r1c-dispatch-2026-08-25` |
| Expected manifest | baseline and work order |
| Actual changed set | baseline and work order |
| Manifest delta | NONE |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R1C dispatch authority only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: pinned source hashes, fresh typecheck and suite measurements, and defect root-cause inspection |
| actionEvidence | ACTION_EVIDENCE_PRESENT: committed baseline/work order after gates |
| invocationBoundary | local documentation authoring plus safe read-only measurement |
| interceptionBoundary | no universal runtime, CLI, MCP, provider or coding-control interception claim |
| forbiddenExpansion | paths and effects outside the exact manifest, including production source, configuration, build, live and credential action |
| claimLanguage | packet authorizes bounded local test-side repair and adjudication only after commit |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | no new external input; all R1C claims derive from CVF-owned sources and fresh local measurement |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | EAFR roadmap, R1 waiver closure and current cvf-web/LPF sources |
| Disposition | N/A_WITH_REASON: no new external knowledge intake in this tranche |
| Claim boundary | operator waiver is authority; no external report is cited as authority |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: named-file measurement and source verification, not an intake refresh.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - R1C makes no repository-wide or
  all-surface completeness claim.

## Epistemic Process Block

- Epistemic Process Applicability: HIGH_EVIDENCE
- Expected Result / Prediction: direct inspection would show the waived debt
  concentrated in test-side drift rather than production defects, with the
  build criterion blocked by parked environment authority.
- Evidence Comparison: exactly that pattern was observed - four typecheck
  errors in one test file against a required gateway field, seventeen of
  twenty-nine suite failures matching authorization-arrangement drift, and a
  build blocked by Auth.js environment validation.
- Contradiction or Gap Disposition: the R5 incident showed a required command
  can itself be unsafe, so this packet forbids LPF `npm test` and pins the
  explicit-exclusion form instead.
- Claim Update: R1C is ready for exact thirteen-path no-commit worker execution
  after this packet is committed.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| waived package criteria persisted across five tranches without a repair attempt | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | execute this dispatch so each criterion ends in repair or fresh adjudication before R6 |
| a required package command could auto-select ambient-key provider tests | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | this packet pins explicit exclusions and forbids the unsafe command; checker expansion remains a deferred candidate |

## Machine Closure Package

| Surface | R1C closure requirement |
| --- | --- |
| Work order | reviewer converts pending dispatch state only after acceptance |
| Completion/reviewer artifact | reviewer-owned decision with exact counts, dispositions, diff and claim boundary |
| Roadmap | R1C accepted or blocked; R6 remains gated until R1C debt is resolved or freshly adjudicated |
| Registry JSON/Markdown | N/A with reason: no corpus/generated registry classification changes |
| External evidence digest | N/A with reason: no external dataset is consumed |
| System loop interlock | R5 -> R1C -> R6 remains explicit |
| Session continuity | separate post-material sync required |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance package-debt remediation; no public-sync authority.

## Claim Boundary

This work order authorizes only exact thirteen-path local test-side repair,
deterministic re-measurement and fresh adjudication of the three waived
criteria. It authorizes no production source edit, no configuration, package
manifest, checker or environment change, no build, live, provider, network or
credential action, no public sync, deployment, push, production claim, R6 or
RFR action. It creates no waiver precedent and does not relax any R2 through R6
acceptance criterion.

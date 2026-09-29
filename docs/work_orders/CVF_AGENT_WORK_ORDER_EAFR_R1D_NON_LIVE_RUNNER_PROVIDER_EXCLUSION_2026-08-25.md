# CVF Agent Work Order - EAFR-R1D Non-Live Runner Provider Exclusion

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Work order ID: EAFR-R1D

Date: 2026-08-25

dispatchBaseHead: `ca1f14add009cae1b8c57b9dbdf8d28eb53d03d3`

executionBaseHead: worker must capture actual HEAD and require this committed packet as ancestor

closureBaseHead: reviewer captures the committed dispatch head

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through the committed EAFR roadmap and the accepted R1C completion review

Reviewer/closer: current independent orchestrator/reviewer

Worker: test-runner boundary worker role

## Dispatch Prompt Envelope

Batch ID: EAFR-R1D-NON-LIVE-RUNNER-EXCLUSION.

Role: no-commit test-runner boundary worker.

Canonical packet: this committed work order and its paired baseline.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: R1C is accepted bounded at material commit `3c51ac5e6`; the
provider selection path and the five-call incident were freshly verified at
dispatch head `ca1f14add`.

Do-not-misread notes: R1D changes test selection and activation only. It is not
authority to run a provider call, verify by calling a provider, edit
dependencies or lockfiles, disable deliberate live testing, touch BuildAuthority,
or start R6 or RFR. Excluding a provider test from a runner is not a security
proof.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, `DESIGN.md`, this packet, paired baseline, the R1C completion review
`R1C-RF5` section, every pinned input and the applicable checker sources for
every output class.

Return contract: exact four paths, no stage/commit, `COMPLETE_PENDING_REVIEW`
or `BLOCKED_WITH_REASON`.

Worker return path: `docs/reviews/CVF_EAFR_R1D_NON_LIVE_RUNNER_PROVIDER_EXCLUSION_WORKER_RETURN_2026-08-25.md`

sourceAuthority: paired GC-018 baseline, committed EAFR roadmap, accepted R1C completion review, accepted R1A runner fix, and source-verified cvf-web files named in this packet

## Purpose

Make a command labelled safe structurally incapable of performing provider
calls: stop the cvf-web non-live runner from collecting ambient-key
real-provider integration tests, require explicit opt-in before any such case
activates, and reconcile the disclosed five-call incident.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R1D --title "Non-Live Runner Provider Exclusion" --date 2026-08-25 --base ca1f14add --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-verified selection-path trace, exact four-path manifest, defense-in-depth exclusion contract, incident reconciliation requirement and safe-command discipline |
| checkerReadAheadConfirmation | applicable dispatch and worker-output checker sources read |
| docOnlyNewFields | Verified Provider Selection Path; Exclusion Sufficiency Contract; Incident Reconciliation Requirement |
| claimBoundary | dispatch authoring only |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R1C bounded closure | `docs/reviews/CVF_EAFR_R1C_WAIVED_PACKAGE_DEBT_REPAIR_AND_ADJUDICATION_COMPLETION_2026-08-25.md`; material commit `3c51ac5e6` | ACCEPT |
| R1C-RF5 incident routing | same completion review, `R1C-RF5` section, naming R1D as the corrective lane | ACCEPT |
| EAFR roadmap authority | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md`, R1C accepted row | ACCEPT |
| R1A predecessor runner fix | `docs/reviews/CVF_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_COMPLETION_2026-08-25.md`; accepted because material commit `ef142bfb2` exists | ACCEPT |

## Authority And Scope

Governing baseline:
`docs/baselines/CVF_GC018_EAFR_R1D_NON_LIVE_RUNNER_PROVIDER_EXCLUSION_2026-08-25.md`.

The worker may edit or create exactly the four paths in Write Ownership. No
other path is writable. The worker must not stage or commit.

## Authority Chain

Operator EAFR authority and accepted R1C closure -> committed roadmap -> paired
baseline -> this work order -> no-commit worker -> independent reviewer/closer.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| exclude ambient-key real-provider tests from the Web non-live runner | Required Implementation; Selection Barrier | package manifest and vitest configuration | non-live collection listing | PASS |
| prevent activation on ambient credentials alone | Required Implementation; Activation Barrier | provider integration test | explicit opt-in inspection | PASS |
| reconcile the five-call incident | Incident Reconciliation Requirement | worker return | documentary reconciliation | PASS |
| preserve deliberate live testing | Preserved Capability Rule | live runner entry | live runner selection listing | PASS |

## Required First Reads

Read `AGENTS.md`, `CVF_SESSION_MEMORY.md`, the bootstrap read model, active
handoff, `docs/reference/guard_orientation/README.md`, governed literal
gotchas, `DESIGN.md`, paired baseline, this work order, the R1C completion
review, every pinned source and worker-output checker sources named below.
Resolve the full session registry only for a targeted missing or contradictory
fact.

## Agent Roles

Operator owns scope; dispatcher owns the packet; worker implements and proves
without commit; reviewer independently challenges, repairs, closes and commits.

## Pre-Flight Checks

Confirm clean worktree, empty staging, actual HEAD, committed dispatch ancestry,
all pinned hashes, absent worker-return path, Node/npm availability and zero
live-test selection. Capture the before-state non-live collection listing before
any edit. Hash drift or an existing return path blocks before edits.

## Write Ownership

Exactly these four paths:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.integration.test.ts`
4. `docs/reviews/CVF_EAFR_R1D_NON_LIVE_RUNNER_PROVIDER_EXCLUSION_WORKER_RETURN_2026-08-25.md`

A rename of path 3 within its own directory is permitted when recorded as a
rename in the return. No other file may be created. No dependency, lockfile,
environment file, production runtime source, checker, session, roadmap, adapter,
public clone or deployment edit.

## Pinned Input Hashes

| Path | SHA-256 |
| --- | --- |
| `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md` | `f2d741f7c28a1bdb3fb1394d5fa19ab9c6def2cf03760ec5eec60dae2e4cc513` |
| `docs/reviews/CVF_EAFR_R1C_WAIVED_PACKAGE_DEBT_REPAIR_AND_ADJUDICATION_COMPLETION_2026-08-25.md` | `af0e64d3d92f6ffeef0e5ab60a4c898f47d8fad0855759c4095da9724f8dc0a5` |
| `docs/reviews/CVF_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_COMPLETION_2026-08-25.md` | `f303519b013ab8e0c50db7b79c389db4251cf680189b0d29407e46980766e2dd` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | `48163e0e8e2e8a16986af118af0060a9d38c6ae3257575df77a4facfd7ee710e` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` | `d2f043947859a572097cf292ae578c6bd85509ca38e9d6b270a3447f00314305` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.integration.test.ts` | `1cfafc215b5bda8eb971dccb24c0855956dfbd8335dea8810b6c4ba906931211` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts` | `f5b8d0331c2158cff2ec30748f8215ea48de9fde0787a2e650efe257648010a7` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/load-local-env.ts` | `fdbda34c48a288e0257cefc71f0c9fea022008d6a4f8d77a5679b84a67084936` |

The new worker-return path must be absent. Every hash is calculated at
`ca1f14add`; mismatch returns `BLOCKED_WITH_REASON` before material edits.

## Verified Provider Selection Path

```text
non-live runner script
  -> vitest include glob collects every *.test.ts under src
  -> live-suffix exclusions do not match providers.integration.test.ts
  -> shared setup runs loadLocalEnvFiles()
  -> .env.local supplies OPENAI_API_KEY into process.env
  -> ambient-key ternary activates the OpenAI case instead of skipping
  -> real executeAI call with unmocked transport
  -> outbound provider request
```

The worker must re-derive this chain from current source and report any
divergence rather than inheriting it.

## Exclusion Sufficiency Contract

A naming convention alone is not a provider boundary. R1D must satisfy defense
in depth, so no single future rename, new file or script edit silently restores
provider selection:

1. **Selection barrier.** The non-live runner must not collect real-provider
   integration tests, enforced where selection happens rather than only in one
   script string.
2. **Activation barrier.** A real-provider case must not activate merely because
   an ambient key exists; it must require an explicit, deliberate opt-in signal
   that the non-live path never sets.
3. **Evidence.** Show the file is not collected by the non-live runner and that
   safe-suite totals match the corrected R1C figures.

Satisfying only the selection barrier is a partial result and must be reported
as such, never as a completed exclusion.

## Preserved Capability Rule

Deliberate real-provider testing must remain possible. The live runner must
still be able to select and activate real provider cases when an operator
invokes it intentionally with the required opt-in. A change that makes real
provider testing impossible under any invocation is over-correction and must be
returned as `BLOCKED_WITH_REASON` rather than shipped.

## Required Implementation

### Selection barrier

- Ensure the non-live runner cannot collect
  `providers.integration.test.ts` or any future real-provider integration test
  in the same class.
- Prefer a durable mechanism over a single script string: a configuration-level
  exclusion, a naming convention the live runner already recognises, or both.
  If a rename is used, it must be recorded as a rename in the return.
- Do not weaken the existing live-suffix exclusions; extend, do not replace.

### Activation barrier

- Change the real-provider cases so an ambient key alone does not activate them.
  Require an explicit opt-in signal, distinct from the provider key, that the
  non-live path never sets and that an operator must set deliberately.
- Keep the existing skip behaviour when the opt-in or the key is absent; a
  missing opt-in must skip, never fail.
- Do not print, log or echo any key, signed header or unredacted request body.

### Incident reconciliation

- In the return, restate the five-call count and its four attributed sources
  from the R1C completion review.
- Confirm from source whether the same path could still fire after the change.
- State explicitly that R1D grants no repeat-live authority and made zero
  provider calls of its own.

## Verification Discipline

The fix must be proven by **selection and activation inspection**, never by
making a provider call:

- list what the non-live runner collects and show the integration file is
  absent;
- show the live runner still selects it;
- read the activation gate and show an ambient key alone is insufficient;
- run the safe suite and compare totals against the corrected R1C figures.

The absence of a key in the invoking shell is **not** evidence of safety,
because the shared setup file loads `.env.local` into the process environment
independently of the shell. Any claim of safety based on shell environment alone
must be rejected by the worker itself.

## Adversarial Proof Matrix

| Vector | Boundary under test | Required result |
| --- | --- | --- |
| non-live runner invoked with a valid ambient key present | selection barrier | integration file not collected; zero provider calls |
| integration file renamed back or a new sibling added | selection barrier durability | configuration-level exclusion still prevents collection |
| ambient key present but opt-in absent | activation barrier | case skips, does not fail and does not call |
| opt-in present under the live runner | preserved capability | real provider case remains selectable and activatable |
| verification attempted by calling a provider | verification discipline | forbidden; blocked return |
| safety claimed from an empty shell environment | verification discipline | forbidden; setup loads the key independently |
| live-suffix exclusions weakened or replaced | regression | forbidden; existing exclusions must be preserved |
| dependency, lockfile or env file edited | manifest boundary | forbidden; blocked return |

## Acceptance Criteria

- exactly four worker paths, or four with one recorded rename, and no others;
- the non-live runner provably does not collect the real-provider integration
  test;
- an ambient key alone no longer activates any real-provider case;
- the live runner retains the ability to run real provider tests deliberately;
- safe-suite totals match the corrected R1C figures of 312 files, 3527 tests,
  2 failures and zero skips, with the two failures still the known
  BuildAuthority residuals and no new failure introduced;
- the five-call incident is reconciled in the return;
- zero provider calls, with an explicit statement to that effect;
- no dependency, lockfile, environment file, production runtime, or checker
  change;
- worker-return fast gate passes; staging is empty; worker HEAD is unchanged.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EAFR-R1D",
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
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/",
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/",
    "docs/reviews/",
    "docs/baselines/CVF_GC018_EAFR_R1D_NON_LIVE_RUNNER_PROVIDER_EXCLUSION_2026-08-25.md"
  ],
  "claims": ["the non-live runner cannot select ambient-key real-provider integration tests"],
  "requiredProof": ["non-live collection listing", "live collection listing", "activation gate inspection", "safe suite totals", "hashes", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["provider or live call", "dependency or lockfile change", "environment file edit", "production runtime change", "disabling deliberate live testing", "worker stage or commit", "public/deploy/push"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| worker role | no-commit test-runner boundary worker |
| reviewer role | independent reviewer/closer |
| external intake | none; all claims verified in CVF-owned sources |
| escalation condition | hash drift, a second selection path found, required extra path, live or credential need, or inability to preserve deliberate live testing |
| risk sensitivity | provider-call prevention and honest sufficiency reporting |
| scope classification | exact four-path local test-selection hardening |

## Required Commands

Run from cvf-web:

1. non-live collection listing before edits, using the non-live runner's own
   exclusions with a list-only flag, capturing whether the integration file is
   collected;
2. `npm run test:run` before edits is NOT permitted; use the safe explicit form
   in command 4 instead;
3. non-live collection listing after edits, showing the integration file absent;
4. safe suite after edits:
   `npx vitest run --exclude "src/**/*.live.test.ts" --exclude "src/**/*.live.test.tsx" --exclude "src/lib/ai/providers.integration.test.ts"`,
   retained as the belt-and-braces measurement even after the change;
5. `npm run test:run` after edits, permitted only once the exclusion is in place
   and the collection listing in command 3 proves the integration file is not
   collected;
6. live runner collection listing, list-only, showing the real-provider case is
   still selectable;
7. `npm run check`.

Run from repository root:

8. bounded positive/negative searches proving no dependency, lockfile,
   environment file, production runtime or checker path was touched;
9. recompute pinned hashes for all inputs outside the worker manifest;
10. `python governance/compat/run_worker_return_fast_gate.py`;
11. `git diff --check`, `git diff --name-status`,
    `git status --short --untracked-files=all`, and
    `git diff --cached --name-only`.

Do not run `npm run test:live`, Playwright, `npm run build`, LPF `npm test`,
release gate, provider, network, environment/key, public-sync, deployment or
installation commands. Command 5 is gated on command 3 passing first; running it
before the exclusion is proven repeats the R1C-RF5 incident.

## Execution Plan

1. Capture startup, clean status, empty staging, HEAD, ancestry, return-path
   absence, pinned hashes and the before-state collection listing.
2. Implement the selection barrier and prove non-collection.
3. Implement the activation barrier and prove ambient keys are insufficient.
4. Confirm deliberate live testing still works by listing, not by calling.
5. Run the safe suite, compare against corrected R1C figures, write the worker
   return with incident reconciliation, and return without staging or
   committing.

## Verification Commands

Run every Required Command, including the full:

`python governance/compat/run_worker_return_fast_gate.py`

Individual checker substitution is forbidden.

## Evidence Requirements

Report pre/post HEAD and status; exact changed paths including any rename;
before/after collection listings for both runners; the activation gate before
and after; safe-suite totals compared to the corrected R1C figures; confirmation
that the two residual failures are unchanged and no new failure appeared;
incident reconciliation; positive/negative search counts; non-manifest source
hashes; worker-return fast gate output; empty staging; an explicit
zero-provider-call statement; and explicit zero external-effect evidence.
Failed, skipped, timed-out or ambiguous commands stay visible and cannot be
relabeled as passing.

## Fail Conditions

Return `BLOCKED_WITH_REASON` for hash drift, a second uncovered selection path,
a needed extra path, any provider call, an inability to preserve deliberate live
testing, a required dependency/lockfile/environment change, a new suite failure
introduced by the change, or a credential requirement.

## Worker Autonomy / No-Question Rule

Repair all allowed-scope defects and rerun safe evidence without asking the
operator. Do not expand scope. If only the selection barrier can be satisfied,
report a partial result with the activation gap named rather than claiming a
completed exclusion.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: R1D changes test selection, so collection listings, suite totals, activation inspection, hashes and boundary searches must be fresh against the pending worker tree

priorVerificationArtifact: accepted R1C completion review with corrected safe-suite figures and the R1C-RF5 incident record

priorVerificationAnchor: pinned SHA-256 values in this work order

freshRecomputeRequired: collection listings, activation gate inspection, safe suite totals, typecheck, hashes, boundary searches and worker-return gate

unicodePathHandling: use literal repository-relative paths and UTF-8-safe readers

extractedTextAuthority: CVF-governed sources and fresh local command output only

## Current Runtime Freshness Verification

Direct inspection at `ca1f14add` confirms the non-live runner excludes only
live-suffix files, the vitest configuration declares no exclude entry, the
integration file is collected by the include glob, its OpenAI case activates on
an ambient key, and the shared setup injects that key from a local env file. A
targeted survey found exactly one file in this exposure class. No live behavior
is claimed or required.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R1D is the authorized next tranche | ROADMAP_AUTHORITY | `docs/reviews/CVF_EAFR_R1C_WAIVED_PACKAGE_DEBT_REPAIR_AND_ADJUDICATION_COMPLETION_2026-08-25.md` | Risk / Corrective Action, corrective lane 1; Reviewer Decision | EAFR-R1D | R1C completion review | ACCEPT |
| five provider calls occurred through a purportedly safe runner | OWNER_AUTHORITY | `docs/reviews/CVF_EAFR_R1C_WAIVED_PACKAGE_DEBT_REPAIR_AND_ADJUDICATION_COMPLETION_2026-08-25.md` | R1C-RF5 section | incident disclosure | R1C completion review | ACCEPT |
| the non-live runner excludes only live-suffix files | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts block, non-live runner entry | scripts non-live test runner entry | cvf-web package manifest | ACCEPT |
| the integration file is collected by the include glob | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` | test block include entry with no exclude entry | include | cvf-web vitest configuration | ACCEPT |
| the OpenAI case activates on an available key and calls the real provider | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.integration.test.ts` | ambient key constants and OpenAI case | testOpenAI; executeAI | cvf-web provider integration test | ACCEPT |
| the shared setup injects local env values into the process environment | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts` | module-scope setup call | loadLocalEnvFiles | cvf-web test setup | ACCEPT |
| local env loading assigns keys when unset or empty | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/load-local-env.ts` | default env file list and assignment branch | loadLocalEnvFiles; DEFAULT_ENV_FILES | cvf-web local env loader | ACCEPT |
| the sibling provider unit test is contained by a module-scope transport stub | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts` | module-scope global stub | fetchMock | cvf-web provider unit test | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_equivalence_claim_evidence.py`; `governance/compat/check_worker_experience_retrospective.py` |
| literalTokensReviewed | dispatch status; Source Verification Block; Current Runtime Freshness Verification; Evidence Reuse scalar fields; worker-return headings; trace and delta labels; equivalence disposition tokens; retrospective four-field block |
| gateRunPurpose | confirm as evidence that the completed source-verified packet matches checker shape |
| claimBoundary | checker conformance does not prove the exclusion is sufficient |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`test runner provider exclusion`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "test runner provider exclusion" --role worker --lifecycle-phase implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | ordinary CVF controls apply |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact R1D baseline, work-order and return paths | all absent before dispatch authoring | PASS |
| token search | `EAFR-R1D` existed only in the R1C completion review corrective lane and continuity next-move text | PASS |
| exposure class survey | a targeted survey of non-live test files found exactly one ambient-key-gated real-provider file; the sibling provider unit test is contained by a module-scope transport stub | PASS |
| collision decision | harden the existing runner and integration file in place; create no new test file, helper or checker | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | cvf-web test runner selection surface | local test selection only; no runtime or provider behavior change | collection listings and safe suite totals | local scripts and config only | HARDEN_BOUNDED |
| EXTERNAL_AGENT_CLI_MCP | none | no CLI/MCP read, authority or adapter behavior is created or changed | unchanged adapter boundaries | separate source-verified work order required | DEFERRED_WITH_REASON |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | no-commit worker plus independent reviewer |
| phase | implementation pending worker return |
| baseHeadFor(phase) | dispatchBaseHead=ca1f14add; executionBaseHead=worker captures; closureBaseHead=reviewer captures |
| changedSetScope(phase) | exact four-path worker manifest |
| traceScope(phase, actor) | local test selection and activation hardening plus incident reconciliation |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean worktree required; BuildAuthority, R6, RFR and all external effects parked |
| nextMoveSurfaces | worker return then independent reviewer decision |

## Worker Output Checker Read-Ahead Mandate

Before writing each changed file or the worker return, read every checker source
applicable to its docType, path family and conditional content. Derive actual
headings and literal tokens before authoring; checklist prose is not a
substitute for the real sections.

## Work-Order Fulfillment Manifest

| Artifact group | Required worker action |
| --- | --- |
| package manifest and vitest configuration | prevent non-live collection of real-provider integration tests without weakening live-suffix exclusions |
| provider integration test | require explicit opt-in so an ambient key alone cannot activate a real call |
| worker return | record complete uncommitted evidence, sufficiency disposition and incident reconciliation |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_EAFR_R1D_NON_LIVE_RUNNER_PROVIDER_EXCLUSION_WORKER_RETURN_2026-08-25.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must carry the full review-family/no-commit shape, cite this work
order, report the actual dirty paths including any rename, state a sufficiency
disposition against the Exclusion Sufficiency Contract, and preserve every
failure or residual without relabeling.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_EAFR_R1D_NON_LIVE_RUNNER_PROVIDER_EXCLUSION_COMPLETION_2026-08-25.md` |
| reviewerOwnedClosurePaths | worker manifest, return, optional completion review, EAFR roadmap and continuity |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

Reviewer must independently rerun both collection listings, inspect the
activation gate, confirm deliberate live testing still works, verify safe-suite
totals against the corrected R1C figures, and verify the zero-provider-call
claim.

## Review Gate

Only the independent reviewer/closer may accept, repair authorized defects, run
closure gates and commit. Acceptance requires direct source inspection and fresh
recomputation, not worker self-report.

## Closure Checklist

- exact four-path worker diff, plus any recorded rename, and empty staging;
- non-live runner provably does not collect the real-provider integration test;
- ambient key alone cannot activate a real-provider case;
- deliberate live testing preserved;
- safe-suite totals match corrected R1C figures with no new failure;
- five-call incident reconciled and no repeat-live authority claimed;
- zero provider calls and zero dependency, lockfile or environment change.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with all acceptance evidence, including a
sufficiency disposition for both barriers. Otherwise return
`BLOCKED_WITH_REASON`, naming the first unresolved condition and preserving
partial or failed evidence.

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Foundation Storage Layout Block | N/A with reason: R1D edits existing runner, configuration and test files in place and creates no new foundation family file or storage topology |
| Protected storage paths | memory foundation filenames, folder front door, generated aggregates and indexes remain unchanged |
| Follow-up condition | any new stable foundation file, split, relocation or generated-state edit needs separate authorization |

## Operator Checkpoint

operator.checkpoint.waiver: none. Live/provider/build/credential/public/
destructive expansion requires fresh explicit authority. R1D grants no
repeat-live authority and does not reopen the disclosed incident as precedent.

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
| Session or invocation | EAFR-R1D dispatch authoring, 2026-08-25 |
| Working directory | repository root |
| Command or tool surface | source reads, searches, hashes, scaffold, ADIF resolver, safe explicit-exclusion suite measurement, packet authoring and gates |
| Target paths | R1D baseline and work order |
| Allowed scope source | accepted R1C completion review corrective lane and EAFR roadmap |
| Before status evidence | clean worktree at HEAD `ca1f14add009cae1b8c57b9dbdf8d28eb53d03d3`; staging empty |
| After status evidence | two dispatch artifacts pending commit |
| Diff evidence | `git diff --name-status` over exact dispatch document set |
| Approval boundary | R1D dispatch only |
| Claim boundary | no worker implementation, live, provider, credential, build or public effect |
| Agent type | dispatcher |
| Invocation ID | `eafr-r1d-dispatch-2026-08-25` |
| Expected manifest | baseline and work order |
| Actual changed set | baseline and work order |
| Manifest delta | NONE |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R1D dispatch authority only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: pinned source hashes, selection-path source trace and a safe explicit-exclusion suite measurement |
| actionEvidence | ACTION_EVIDENCE_PRESENT: committed baseline/work order after gates |
| invocationBoundary | local documentation authoring plus safe read-only measurement |
| interceptionBoundary | no universal runtime, CLI, MCP, provider or coding-control interception claim |
| forbiddenExpansion | paths and effects outside the exact manifest, including dependency, lockfile, environment, production runtime, live, credential and build action |
| claimLanguage | packet authorizes bounded local test-selection hardening only after commit |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | no new external input; every R1D claim derives from CVF-owned sources and fresh local inspection |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | EAFR roadmap, R1C completion review and current cvf-web sources |
| Disposition | N/A_WITH_REASON: no new external knowledge intake in this tranche |
| Claim boundary | the accepted R1C review is authority; no external report is cited as authority |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: named-file source verification and selection inspection, not an intake
refresh.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - R1D makes no repository-wide or
  all-surface completeness claim. The exposure survey is a bounded targeted
  search over cvf-web test files, not a completeness claim.

## Epistemic Process Block

- Epistemic Process Applicability: HIGH_EVIDENCE
- Expected Result / Prediction: direct inspection would show a runner whose only
  guard is a filename convention, with at least one real-provider test outside
  that convention reachable through ambient credentials.
- Evidence Comparison: exactly that was observed, and the credential source was
  narrower than expected in one respect and broader in another: the invoking
  shell had no key, yet the shared setup injected one from a local env file, so
  shell-level emptiness was never evidence of safety.
- Contradiction or Gap Disposition: because a filename convention proved
  insufficient once, this packet requires defense in depth rather than a second
  convention, and forbids proving the fix by making a call.
- Claim Update: R1D is ready for exact four-path no-commit worker execution
  after this packet is committed.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| a runner labelled safe selected an ambient-key real-provider test because its only guard was a filename convention | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | execute this dispatch; a checker that flags provider-capable tests outside the live convention remains a deferred candidate |
| shell environment emptiness was treated as provider-call safety while a setup file injected credentials | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | RULE_EXISTS | this packet forbids shell-environment safety claims and requires selection and activation inspection instead |

## Machine Closure Package

| Surface | R1D closure requirement |
| --- | --- |
| Work order | reviewer converts pending dispatch state only after acceptance |
| Completion/reviewer artifact | reviewer-owned decision with collection listings, suite totals, dispositions, diff and claim boundary |
| Roadmap | R1D accepted or blocked; R6 remains gated behind the BuildAuthority classification |
| Registry JSON/Markdown | N/A with reason: no corpus/generated registry classification changes |
| External evidence digest | N/A with reason: no external dataset is consumed |
| System loop interlock | R1C -> R1D -> R6 remains explicit |
| Session continuity | separate post-material sync required |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance test-runner remediation; no public-sync authority.

## Claim Boundary

This work order authorizes only exact four-path local test-selection and
activation hardening plus incident reconciliation. It authorizes no provider,
live, network, credential, build, dependency, lockfile, environment, deployment,
public-sync, push or production action, no production runtime change, no
BuildAuthority work, no R6 and no RFR action. Excluding a provider test from a
runner is not a security proof and makes no claim about credential hygiene, past
call content, or provider account state.

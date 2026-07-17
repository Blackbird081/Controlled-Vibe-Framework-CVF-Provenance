# CVF GC-018 - SOT3-APP-T4 Local Controlled Quotation Proof

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: SOT3-APP-T4

Dispatch base head: `dfd77f881`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one narrow no-commit worker tranche to replace the current
fixture-existence Controlled Quotation proof with a deterministic local
source-to-freeze-impact-recall proof using existing application services,
existing binding adapter interfaces, and replayable receipt verification.

## Decision

Proceed with local deterministic proof only. No provider, live API, browser,
server, database migration, dependency, package manifest, lockfile, public,
push, production, or T5/service action is authorized.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T3 closure | `docs/reviews/CVF_SOT3_APP_T3_COMPLETION_REVIEW_2026-07-17.md`; material commit `4bb19d27d`; roadmap status `SOT3_APP_T3_CLOSED_T4_PACKET_AUTHORING_NEXT` | T4 packet authoring may begin only after accepted T3 closure | SATISFIED |
| Session continuity | session-sync commit `dfd77f881` sets next allowed move to T4 packet authoring only | dispatch base must be post-sync clean HEAD | SATISFIED |

## Current T4 Baseline Evidence

| Check | Command | Result |
|---|---|---|
| existing vertical slice script | `corepack pnpm@9.15.0 vertical-slice` | PASS but returns `REFERENCE_VERTICAL_SLICE_READY`, `fixture_count: 11`, `live_bindings_executed: false`, and `FIXTURE_HARNESS_NOT_GOVERNED_RUNTIME_EVIDENCE` |
| existing focused e2e | `corepack pnpm@9.15.0 vitest run tests/e2e/controlled-quotation.e2e.test.ts --workspace vitest.workspace.ts` | PASS, 1 file and 1 test; proves fixture existence only |

## Verification Evidence

The dispatch author directly read the current sibling script/test and the
service, adapter, evidence, and contract source files listed below. The
pre-dispatch baseline commands prove the current T4 surface is executable but
fixture-only, which is the defect this worker must close.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Current Controlled Quotation script only checks fixture files and prints fixture-harness boundary | EXISTS | CANONICAL_CONTRACT: external sibling direct-read evidence; controlled quotation script | lines 4-24 | `fixtureRoot`; `required`; `REFERENCE_VERTICAL_SLICE_READY`; `FIXTURE_HARNESS_NOT_GOVERNED_RUNTIME_EVIDENCE` | script entrypoint | ACCEPT |
| Current Controlled Quotation e2e only asserts fixture existence | EXISTS | CANONICAL_CONTRACT: external sibling direct-read evidence; focused controlled quotation e2e test | lines 4-17 | `controlled quotation fixture harness`; `existsSync` | Vitest test | ACCEPT |
| Source intake service can call existing CVF entry and refinery adapters | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/application/src/services/source-intake.service.ts` | lines 5-19 | `SourceIntakeService.intake` | `SourceIntakeService` | ACCEPT |
| SOT registration can assert kernel references and activate a record | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/application/src/services/sot-registration.service.ts` | lines 5-10 | `SOTRegistrationService.register` | `SOTRegistrationService` | ACCEPT |
| Context builder can build a routed context package from SOT records | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/application/src/services/context-builder.service.ts` | lines 6-53 | `ContextBuilderService.build` | `ContextBuilderService` | ACCEPT |
| Governed output service creates an output only when route decision is continuable | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/application/src/services/governed-output.service.ts` | lines 6-44 | `GovernedOutputService.create`; `SOT_ROUTE_NOT_CONTINUABLE` | `GovernedOutputService` | ACCEPT |
| Review freeze service creates a freeze hash after approval and freeze authorization | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/application/src/services/review-freeze.service.ts` | lines 6-34 | `ReviewFreezeService.freeze`; `freeze_hash` | `ReviewFreezeService` | ACCEPT |
| Impact recall service resolves impacts and recall from dependency edges | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/application/src/services/impact-recall.service.ts` | lines 4-11 | `ImpactRecallService.assess` | `ImpactRecallService` | ACCEPT |
| Freeze package helper validates output/freeze identity | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/evidence/src/freeze-package.ts` | lines 13-25 | `buildFreezePackage`; `SOT_FREEZE_OUTPUT_MISMATCH` | evidence package helper | ACCEPT |
| Receipt helper can hash and verify replay receipts | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/evidence/src/receipt-integrity.ts` | lines 3-11 | `hashReceipt`; `verifyReceipt` | receipt integrity helper | ACCEPT |
| SourceRecord identity fields exist | EXISTS | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/contracts/src/types/source-record.ts` | lines 11-23 | `SourceRecord`; `source_id`; `content_hash`; `state` | contract type | ACCEPT |
| SOTRecord identifier/evidence fields exist | EXISTS | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/contracts/src/types/sot-record.ts` | lines 14-33 | `SOTRecord`; `record_id`; `source_references`; `truth_kernel_references` | contract type | ACCEPT |
| ContextPackage route and evidence fields exist | EXISTS | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/contracts/src/types/context-package.ts` | lines 3-20 | `ContextPackage`; `context_package_id`; `route_decision`; `evidence_references` | contract type | ACCEPT |
| OutputArtifact source and route fields exist | EXISTS | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/contracts/src/types/output-artifact.ts` | lines 9-25 | `OutputArtifact`; `output_id`; `source_references`; `routing_decision_id` | contract type | ACCEPT |
| ReviewRecord approval decision field exists | EXISTS | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/contracts/src/types/review-record.ts` | lines 3-14 | `ReviewRecord`; `decision` | contract type | ACCEPT |
| FreezeRecord freeze hash and receipt fields exist | EXISTS | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/contracts/src/types/freeze-record.ts` | lines 1-15 | `FreezeRecord`; `freeze_hash`; `review_records`; `routing_decisions` | contract type | ACCEPT |
| ImpactRecord exists for impact proof | EXISTS | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/contracts/src/types/impact-record.ts` | lines 1-10 | `ImpactRecord` | contract type | ACCEPT |
| RecallCase exists for recall proof | EXISTS | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/contracts/src/types/recall-case.ts` | lines 1-18 | `RecallCase` | contract type | ACCEPT |
| Local adapter stubs can implement actual port interfaces | EXISTS | CANONICAL_CONTRACT: external sibling direct-read evidence; `packages/cvf-bindings/src/cvf-entry.adapter.ts`; `packages/cvf-bindings/src/refinery.adapter.ts`; `packages/cvf-bindings/src/truth-kernel.adapter.ts`; `packages/cvf-bindings/src/truth-flow.adapter.ts`; `packages/cvf-bindings/src/governed-execution.adapter.ts`; `packages/cvf-bindings/src/evidence.adapter.ts`; `packages/cvf-bindings/src/phase-governance.adapter.ts` | verified by symbol lines in source audit | `CVFEntryPort`; `RefineryPort`; `TruthKernelPort`; `TruthFlowPort`; `GovernedExecutionPort`; `EvidencePort`; `PhaseGovernancePort` | binding adapter interfaces | ACCEPT |

## Allowed Scope

External sibling source root:

- `scripts/run-controlled-quotation.ts`
- `tests/e2e/controlled-quotation.e2e.test.ts`

Provenance worker outputs:

- `docs/reviews/CVF_SOT3_APP_T4_LOCAL_CONTROLLED_QUOTATION_PROOF_EVIDENCE_2026-07-17.md`
- `docs/reviews/CVF_SOT3_APP_T4_WORKER_RETURN_2026-07-17.md`

## Forbidden Scope

Do not edit package manifests, lockfiles, tsconfig files, app routes,
controllers, services, domain logic, binding adapters, persistence, web UI,
fixtures, generated output directories, public-sync paths, registry aggregates,
or session-sync surfaces. Do not install dependencies. Do not initialize Git in
the sibling application root.

## Acceptance Criteria

The worker may return `COMPLETE_PENDING_REVIEW` only if:

1. `scripts/run-controlled-quotation.ts` executes real local service/adaptor
   calls for source intake, SOT registration, context build, governed output,
   approval review, freeze, impact assessment, recall planning, freeze package
   construction, and receipt verification.
2. The script exports an importable proof function and its CLI output reports
   `LOCAL_CONTROLLED_QUOTATION_REPLAY_PASS`, not the old fixture-only status.
3. The proof includes a receipt chain verified by `verifyReceipt` and fails if
   any required source, SOT, context, output, review, freeze, impact, recall,
   or receipt identifier is missing or mismatched.
4. The focused e2e test invokes the proof function directly and proves the
   identifier/evidence chain survives replay.
5. The exact command set passes: focused e2e, root test, root typecheck, root
   build, and doctor.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`local controlled quotation vertical-slice proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "local controlled quotation vertical-slice proof" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional defect-specific dispatch constraint |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Dispatch requirement | Evidence target | Status |
|---|---|---|---|
| prove Controlled Quotation locally | replace fixture-only harness with local service/adaptor proof | `LOCAL_CONTROLLED_QUOTATION_REPLAY_PASS` | READY |
| real local source-to-freeze-impact-recall slice | script must call service chain through freeze and impact/recall | command and evidence companion | READY |
| complete identifier/evidence chain survives replay | e2e must verify required IDs, references, receipt hashes, and replay integrity | focused e2e and worker evidence | READY |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | T4 work order and worker-return evidence | may execute deterministic local script/test only within allowed scope | source verification and command evidence | internal local proof only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no external adapter ratified for this sibling proof | no ingress, auth, mutation, public, or MCP claim | explicit forbidden scope | adapter deferred; no external interface | `DEFERRED_WITH_REASON` |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | DISPATCHER_TO_WORKER_TO_REVIEWER_CLOSER |
| phase | T4 dispatch to no-commit worker |
| baseHeadFor(phase) | dispatchBaseHead=`dfd77f881`; executionBaseHead=worker-captured; closureBaseHead=reviewer-owned |
| changedSetScope(phase) | two external source/test paths and two provenance worker outputs |
| traceScope(phase, actor) | service-chain proof, receipt verification, command receipts, no-commit evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | T4 execution only after reviewer accepts; T5/service and provider/live/public lanes excluded |
| nextMoveSurfaces | reviewer/session-sync steward when closure commit exists |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SOT3_APP_T4_COMPLETION_REVIEW_2026-07-17.md` |
| reviewerOwnedClosurePaths | paired baseline, work order, roadmap, two worker outputs, optional completion review, protected session sync |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Dependency Release Evidence; Source Verification Block; Roadmap-To-Work-Order Trace Matrix; ADIF Defect Registry Disclosure; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Dual Agent Surface Matrix; Machine Closure Package; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm independently established T4 dispatch evidence; gates are not first discovery |
| claimBoundary | structural dispatch confirmation only; no implementation or runtime proof claim |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-APP-T4 --title "Local Controlled Quotation Proof" --date 2026-07-17 --base dfd77f881 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T3 closure 4bb19d27d" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic worker dispatch plus no-commit worker-return profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact local service-chain proof scope, source verification, commands, and closure criteria |
| checkerReadAheadConfirmation | dispatch, handoff, worker-return, trace, closure, public, and size checkers read |
| docOnlyNewFields | `LOCAL_CONTROLLED_QUOTATION_REPLAY_PASS`; `REPLAY_RECEIPT_CHAIN_VERIFIED` |
| claimBoundary | scaffold provenance only; no implementation claim |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this file | `Status: DISPATCH_READY` | PASS |
| Work order status | paired T4 work order | `Status: DISPATCH_READY` | PASS |
| Roadmap state | SOT3-APP roadmap | `Status: SOT3_APP_T4_DISPATCHED_WORKER_NEXT` | PASS |
| Registry JSON | existing GC-051 aggregate | no new provenance source path | PASS |
| Registry Markdown | existing registry documentation | unchanged | PASS |
| Completion or reviewer artifact | future completion review | N/A with reason: worker has not executed |
| External evidence digest | current fixture-only T4 baseline | script result `FIXTURE_HARNESS_NOT_GOVERNED_RUNTIME_EVIDENCE`; focused e2e 1/1 PASS | PASS |
| System loop interlock | T3 closure -> T4 dispatch -> independent review | T4 execution only; later lanes parked | PASS |
| Session continuity | protected sync after dispatch | reviewer/session-sync steward-owned | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private sibling application proof; no public export is authorized.

## Claim Boundary

This baseline authorizes only deterministic local T4 worker implementation in
the two listed external paths plus two provenance returns. It does not claim
the proof has been implemented, and it authorizes no provider/live/browser,
server, database, dependency, package, public-sync, push, production, or T5
action.

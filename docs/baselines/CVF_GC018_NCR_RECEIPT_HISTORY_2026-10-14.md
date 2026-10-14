# CVF GC-018 Baseline - NCR Home Saved Receipt History

Memory class: governed-dispatch-baseline
docType: baseline
Status: DISPATCH_READY
Date: 2026-10-14
Batch ID: CVF-NCR-HOME-RECEIPT-HISTORY-20261014
Inspection base: `d2125357262a6f7825d14fedcb21d76b0b376516`
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: ORCHESTRATOR_GRANT_REQUIRED

## Purpose

Preserve and restore a scalar-only saved receipt projection for the exact selected completed Home execution, show saved-local-history origin in UI and Markdown, and prove one bounded real Alibaba root/reload/owned-server-restart journey. Finite NCR R1/R4 contribution only.

## Decision / Proposed Tranche

`DISPATCH_READY`: Root selected; must bind exact three dispatch artifacts, GC-051 registration plan, current authority, 75-minute release clock and full pre-dispatch gate before worker BUILD/provider calls. Expiry: `2026-10-14T02:00:00Z` or 75 minutes after actual release, whichever first.

## Scope / Target / Owner Boundary

Worker exact eleven paths: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/index.ts`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-receipt-archive.ts`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResultViewer.tsx`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-receipt-archive.test.ts`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.test.tsx`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResultViewer.receipt-history.test.tsx`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/ncr-receipt-history.live.spec.ts`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/ncr-receipt-history-boundary.cjs`, `docs/reviews/evidence/ncr-receipt-history-worker-20261014.json`, `docs/reviews/CVF_NCR_RECEIPT_HISTORY_WORKER_RETURN_2026-10-14.md`. Root owns three dispatch paths, seven review/registry/roadmap paths, six continuity paths; total exact 27. No store, execution-continuity, ProcessingScreen, route, prior closed tests outside this manifest, dependency/config, real-data, send, public or deploy edit. Worker no stage/commit. Server-only Alibaba key, mock 0, other providers/Redis blank, owned empty stores, fresh ignored dist/port, browser keyless.

## Design Control Gate

Version-1 `Execution.savedReceiptArchive?` binds selected execution ID and exact UTF-8 output SHA-256 to strict scalar receipt projection. Required receiptId/evidenceMode/routeId/generatedAt; typed optional allowlist only, canonicalExecutionId=envelopeId when present; never nested receipt, trace, telemetry, integrity, memory or secrets. WebCrypto only. Immediate result unaffected by digest failure. Async capture/restore checks current selected ID, completed output, snapshot receipt/provider/model joins and generation sequence; invalidates on all navigation including Follow Up and unmount. History output remains usable with receipt omitted on invalid/missing/crypto failure. `ResultViewer.savedLocalHistory?`, visible `data-testid="saved-receipt-origin"`, original mode and plain saved-copy/no-reverification notice in UI/Markdown. Local SHA mismatch guard is not authenticity.

## Acceptance Criteria

| ID | Observable requirement |
|---|---|
| REQ-ARCHIVE | Strict schema/scalar allowlist and legacy seven-field snapshot unchanged. |
| REQ-CAPTURE | Immediate completion and Unicode known-vector SHA; stale async/deletion/output-change fail closed. |
| REQ-RESTORE | Exact selected history ID/output/snapshot join; malformed, mismatched and no-crypto omit receipt, no re-execute. |
| REQ-EXPORT | Saved-local origin visible and in downloaded Markdown, original evidence mode intact. |
| REQ-LIVE | One fresh real Alibaba Home root HTTP 200/success/ALLOW/zero chunks, persist/reload/owned restart/download same output+receipt; local negatives zero new calls. |
| REQ-BUDGET-RETURN | One worker UI submit, <=3 provider starts; Root separate <=1/<=3; total <=6 additional, old seven historical; exact eleven/no commit/secret-safe return. |

## Evidence / Verification

Exact source SHA and bounded spans: `docs/reviews/evidence/ncr-receipt-history-dispatch-20261014.json`. Worker six proof IDs in `docs/reviews/evidence/ncr-receipt-history-worker-20261014.json`. Root distinct independent fixture and proof `docs/reviews/evidence/ncr-receipt-history-local-20261014.json`. Historical seven calls retained; program ceiling thirteen. No routine rerun after failed/partial/ambiguous proof without diagnostic and Root decision.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Execution extension and seven-field legacy snapshot | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/index.ts` | 36-67 | `ExecutionEvidenceSnapshot; Execution` | types | ACCEPT |
| Route scalar/nested receipt distinction | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | 133-167 | `GovernanceEvidenceReceipt` | AI types | ACCEPT |
| Zustand optional-field persistence | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/store.ts` | 11-75, 162 | `updateExecution; cvf-executions-storage` | store | ACCEPT |
| Home exact history selection and completion | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx` | 363-438 | `restore effect; handleProcessingComplete` | Home | ACCEPT |
| Home invalidation and follow-up seams | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx` | 121-129, 440-501, 543-558 | `clearRecoveryContext; returnToDraft; handleFollowUp` | Home | ACCEPT |
| Existing receipt UI and Markdown export | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResultViewer.tsx` | 108-170, 552-583 | `generateEvidenceReceiptContent; receipt card` | ResultViewer | ACCEPT |
| Lightweight snapshot is separate | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-continuity.ts` | 88-103 | `buildEvidenceSnapshot` | continuity | ACCEPT |

Full raw source preimages: `docs/reviews/evidence/ncr-receipt-history-dispatch-20261014.json`. Selected inspection only, no corpus completeness claim.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | DRAFT status; exact acceptance ledger and eleven-path manifest; one `independentProbeRequired`; worker/reviewer role split; no Core Guard heading in paired order |
| gateRunPurpose | confirmation/evidence after source and literal review; bound implementation release and empirical live result are still pending |
| claimBoundary | checker literals cannot certify provider, isolation, receipt, download or whole-job behavior |

## Epistemic Process Block

Expected Result / Prediction: saved scalar receipt is bound to the selected completed output across reload and owned server restart.
Evidence Comparison: source inspection only; earlier Alibaba journey and Work Transfer proof remain separate historical evidence.
Contradiction Or Gap Disposition: async races, malformed local storage, actual live response and Root distinct oracle pending.
Claim Update: DRAFT finite R1/R4 contribution, no full NCR or trusted-storage claim.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`dispatch`
Resolver command: `python -B governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase dispatch`
Returned defect count: 0
Returned defects: NONE_RETURNED
Dispatch impact: no additional defect-specific dispatch obligation returned.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python -B governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id CVF-NCR-HOME-RECEIPT-HISTORY-20261014 --title "NCR Home Saved Receipt History" --date 2026-10-14 --base d2125357262a6f7825d14fedcb21d76b0b376516 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --evidence-readiness-applicable --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --scec-problem-key ncr-receipt-history --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | runtime-provider-live plus internal no-commit INITIAL |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | Selected scalar receipt archive, exact source pins, async join/race guards, one-root live profile and finite budget. |
| checkerReadAheadConfirmation | ADAPTED_WITH_REASON: dispatcher reviewed required field/token constants, applicable topology/ledger/role/trace/learning/source guards before tracked authoring; failed drafts retained. |
| docOnlyNewFields | None. |
| claimBoundary | Source-backed dispatch draft only. |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local INTERNAL_AGENT orchestrator/reviewer dispatch owner |
| Provider or surface | private repository, read-only source and authored packet |
| Session or invocation | ncr-receipt-history-dispatch-author-20261014 |
| Working directory | repository root |
| Command or tool surface | progressive source/literal review, ADIF resolver0, governed packet/registration publication and canonical state generator |
| Target paths | `docs/baselines/CVF_GC018_NCR_RECEIPT_HISTORY_2026-10-14.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_RECEIPT_HISTORY_2026-10-14.md`; `docs/reviews/evidence/ncr-receipt-history-dispatch-20261014.json`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Allowed scope source | Root's selected finite NCR continuation assignment |
| Before status evidence | 677d3f92ab6ce768c8213dcc824f1bea2180fae5; clean worktree and staged empty after dispatch material before exact9 pre-release amendment |
| After status evidence | exact9 coherent dispatch amendment/continuity; material commit and dedicated actual-SHA exact6 precede bound release |
| Diff evidence | git status exact9 and git diff --check before commit |
| Approval boundary | Root owns final dispatch release after committed binding |
| Claim boundary | no executed browser/provider or release-quality proof |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-receipt-history-dispatch-author-20261014 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_RECEIPT_HISTORY_2026-10-14.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_RECEIPT_HISTORY_2026-10-14.md`; `docs/reviews/evidence/ncr-receipt-history-dispatch-20261014.json`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_RECEIPT_HISTORY_2026-10-14.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_RECEIPT_HISTORY_2026-10-14.md`; `docs/reviews/evidence/ncr-receipt-history-dispatch-20261014.json`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Manifest delta | MATCH exact9 required before commit |
| Deletion or rename disposition | None |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: private NCR receipt-history dispatch draft.

## Claim Boundary

Finite admitted packet; BUILD waits Root committed bound release; worker cannot stage/commit or publish. Selected HTML pilot, backend cancellation/backup guarantees, business acceptance and R3/R4 remain open.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Root dispatch and closure exact-six continuity; no checker semantics or product permission change.
Protected paths:
- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
Operator authorization: operator 2026-10-14 continue NCR, shared-workspace workers and Alibaba live tests; Root owns final review/commits.
Rollback boundary: exact-six source/generated continuity plus this bounded material; preserve closed/blocked history and parked effects. Material packet is committed first; dedicated continuity records its actual SHA before bound release.

## Locked Scalar And Async Publication Contract

Optional scalar allowlist: decision, riskLevel, provider, model, routingDecision, policySnapshotId, envelopeId, canonicalExecutionId, knowledgeSource, knowledgeInjected, knowledgeCollectionId, knowledgeChunkCount, approvalId, validationHint, vision. Required receiptId/evidenceMode/routeId/generatedAt remain exact. Null only for knowledgeCollectionId; boolean fields must be booleans; chunk count is finite nonnegative integer. No unknown nested or secret payload fields are stored/exported. Capture writes only the original completed row whose output/receipt still match, even if the user has navigated away; it never writes a UI receipt or ambient selection. Restore additionally requires current generation/selection and invalidates on all navigation/unmount.

UI notice data-testid=saved-receipt-origin: EN Saved local history receipt. This is a saved copy; it has not been reverified. VI equivalent; Markdown contains Saved local history and preserves original mode.


## Pre-Release Reviewer Preparation Amendment

Before any BUILD or provider call, Local reviewed and corrected its independent oracle: strict scalar allowlist, snapshot receipt mismatch, exact saved-copy/no-reverification UI wording, confirmed owned-server cleanup and restart timing margin. Current oracle and wrapper hashes are recorded in the dispatch evidence; prior oracle preimage remains private evidence. This does not change the eleven-path implementation or six-call task budget. Owned Next development startup may transiently add its named ignored dist include to tsconfig; capture the preimage and restore only those generated additions after shutdown, holding any other delta for Local review. No lasting configuration change is authorized.

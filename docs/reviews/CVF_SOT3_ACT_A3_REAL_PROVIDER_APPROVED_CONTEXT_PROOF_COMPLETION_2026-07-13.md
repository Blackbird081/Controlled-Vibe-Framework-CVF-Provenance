# CVF SOT3-ACT-A3 Real Provider Approved Context Proof Completion

Memory class: FULL_RECORD

docType: review

Status: CLOSED_PASS_BOUNDED

Date: 2026-07-13

Responds to work order: CVF_AGENT_WORK_ORDER_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13

## Purpose

Independently review the blocked A3 worker return, repair its live-entrypoint
control, preserve the failed-attempt evidence, execute an operator-authorized
recovery, and decide whether the bounded A3 real-provider claim is supported.

## Target / Source

The A3 baseline, work order, worker return, A2 completion, parent roadmap,
current route and SOT3 activation store, original blocked receipt, recovery
launch diagnostic, recovery receipt, recovery manifest, and ADIF-0030 control
this review.

## Scope / Methodology

Reviewed provider-call accounting, prompt-observation secrecy, approved-context
hash inclusion, governance receipt and envelope correlation, full SOT3 owner-ID
chain, direct-invocation behavior, runner launch portability, diagnostic-before-
rerun discipline, focused regression, TypeScript validity, manifest hash/size,
secret-value leakage, and claim boundaries.

## Findings / Position

REVIEWER_ACCEPTED_AFTER_BOUNDED_REPAIR_AND_RECOVERY

The original worker correctly rejected its own PASS claim after making three
Alibaba calls against the original ceiling of two and losing the only passing
in-process observation. The original `BLOCKED` receipt remains retained.

Reviewer review found that the runner's stated `--max-calls` enforcement was
not implemented. The repair replaced that claim with a short-lived, one-use
nonce permit bound to the observation path. The live test now resolves the
provider key only after permit validation, consumes the permit before the
test, and writes a secret-safe call ledger immediately before the network
boundary. Direct Vitest invocation proved one offline guard test PASS while
the live suite was skipped.

The operator then authorized Alibaba calls as unmetered for A3 recovery. This
superseded only the original numeric call ceiling; diagnostic-before-rerun,
evidence persistence, and diminishing-return controls remained binding.

The first recovery launcher invocation failed locally before any provider call
because Python on Windows could not resolve `npx` directly. A secret-safe
diagnostic recorded `observedCallCount=0`. The runner was repaired to resolve
`npx.cmd` or `npx`, offline resolution passed, and the result-changing rerun
completed with one real Alibaba `qwen-turbo` call.

## Accepted Live Evidence

The recovery receipt records:

- HTTP `200`, success `true`, and latency `3668 ms`;
- exactly one provider call in the successful runner invocation;
- approved context observed in the outbound provider system prompt by hash-safe
  inclusion, with no raw prompt persistence;
- governance receipt `rcpt-env-mrj2t4za-vu2qla` and envelope
  `env-mrj2t4za-vu2qla`;
- one durable SOT3 record and one trace;
- Refinery packet `RP-000001`, Kernel decision `KD-000001`, Truth receipt
  `RCPT-000001`, Truth reference `TREF-000001`, and Flow package `DPKG-000001`;
- no raw key, provider body, output, or full prompt persisted.

The receipt therefore supports:

`REAL_PROVIDER_APPROVED_CONTEXT_PROVEN_BOUNDED`

## Risk / Corrective Action

Residual risk is bounded to one controlled fixture, one Alibaba model, one CVF
Web `/api/execute` happy path, local evidence storage, and an unsigned local
manifest without an external anchor. The nonce permit prevents accidental
direct invocation through the normal test entrypoint; it does not claim
malicious-bypass resistance or repository-wide enforcement for every live
test. A4 must separately prove rejection and recovery boundaries. A5 must run
the canonical live release bundle before the roadmap-final claim.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Final evidence | Disposition |
|---|---|---|---|
| real provider through existing route | invoke Alibaba `qwen-turbo` through actual `POST` | HTTP 200 recovery receipt | PASS |
| Flow-approved context reaches provider | observe system prompt without persisting it | context hash inclusion `true` | PASS |
| correlate provider result to durable SOT3 evidence | retain receipt/envelope and full owner IDs | one record, one trace, all five layer IDs | PASS |
| one controlled fixture | seed one collection and one chunk | route-adjacent live test | PASS |
| no route/product mutation | proof-only test and runner | committed changed-path evidence | PASS |
| safe failure diagnostics | classify before meaningful rerun | launch diagnostic with zero calls | PASS_AFTER_REPAIR |
| bounded A3 claim only | exclude A4/A5/final claim | completion claim boundary | PASS |

## Closure Diff Gate

Compared the roadmap A3 design, GC-018 criteria, work-order instructions,
blocked worker claims, final runner/test behavior, blocked and recovery
receipts, manifest, ADIF learning, and this completion claim. The original
numeric ceiling was breached and is not rewritten as compliant; it remains
blocked evidence. The later recovery is separately authorized and separately
receipted. All A3 semantic requirements are satisfied. A4, A5, release,
public, production, scale, universal-control, and real-user claims remain open.

## Verification Evidence

- Recovery live run: 1 live test PASS and 1 permit-guard suite SKIP in runner
  mode; one Alibaba provider call; HTTP 200.
- Direct invocation negative proof: 1 permit-guard test PASS and 1 live suite
  SKIP; zero provider calls.
- Focused regression: 4 files, 60 tests PASS, 1 live suite skipped.
- TypeScript check: PASS.
- Python compile: PASS.
- Recovery manifest SHA-256 and byte length recomputation: PASS.
- Operator-key value scan across all recovery evidence: PASS.
- ADIF entry integrity: 30 entries, zero violations.
- Diff hygiene: PASS.

## Closure Checklist

- [x] Original call-ceiling breach remains disclosed and unaccepted.
- [x] Original blocked receipt remains retained.
- [x] Direct/ad-hoc invocation cannot resolve the provider key or enter the
  live suite without a valid one-use runner permit.
- [x] A pre-network call ledger survives failed live assertions.
- [x] The local launcher failure was diagnosed before rerun.
- [x] The rerun used a concrete Windows launcher-resolution repair.
- [x] Recovery receipt records one successful real provider call.
- [x] Approved context inclusion is hash-observed without raw prompt storage.
- [x] Provider result correlates to governance and all SOT3 owner identifiers.
- [x] Secret-value, manifest, focused regression, and TypeScript checks pass.
- [x] A3 claim remains bounded; A4-A5 and final claim remain open.

## Finding-To-Governance Learning Disposition

Learning lane: GOVERNANCE_CONTROL_PLANE

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| Direct live-test invocation bypassed observation capture | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_ADDED | ADIF-0030 requires runner-only permit and durable observation capture |
| Parsed `--max-calls` option was unused | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_ADDED | remove prose-only enforcement claims; use executable permit control |
| Windows launcher was not source-resolved before live execution | WORKER_EXECUTION_ERROR | RUNTIME_BEHAVIOR_LEARNING | RULE_ADDED | resolve `npx.cmd` or `npx`; record zero-call launch diagnostic before rerun |
| Alibaba quota policy changed by operator | N/A_WITH_REASON | RUNTIME_BEHAVIOR_LEARNING | ACCEPT | numeric quota unmetered; diagnostic and value stop rules retained |

## Epistemic Process Block

Expected Result / Prediction: the worker's bounded runner would persist a
receipt-ready observation within the original two-call ceiling.

Evidence Comparison: three calls occurred outside the unfinished runner, the
passing observation was lost, and the runner's call-limit option was unused.
After permit repair, direct invocation was safely blocked. The first recovery
launcher attempt made zero provider calls and produced a classified local
failure; one result-changing rerun persisted complete PASS evidence.

Contradiction Or Gap Disposition: the original worker claim remains rejected.
The separately authorized recovery resolved the entrypoint, persistence, and
launcher gaps without changing the production route.

Claim Update: A3 reaches `REAL_PROVIDER_APPROVED_CONTEXT_PROVEN_BOUNDED`.
The roadmap-final `LIVE_GOVERNANCE_PROVEN_BOUNDED` remains unavailable until
A4 and A5 close.

## Checker Source Read-Ahead Block

| Field | Disposition |
|---|---|
| applicableCheckersRead | `governance/compat/check_machine_closure_package.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_adif_entry_integrity.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Machine Closure Package; Roadmap state; Completion or reviewer artifact; Acceptance Receipt Assertion Matrix; Agent Operation Trace Block; Public Export Disposition |
| gateRunPurpose | confirm recovery evidence and bounded closure; checker PASS cannot substitute for the real provider receipt |
| claimBoundary | machine compliance cannot expand A3 into A4, A5, release, production, public, or user validation |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| A3-LIVE-01 | recovery receipt | `$.overall` | `PASS` | `PASS` | PASS |
| A3-LIVE-02 | recovery receipt | `$.claim` | `REAL_PROVIDER_APPROVED_CONTEXT_PROVEN_BOUNDED` | exact match | PASS |
| A3-LIVE-03 | recovery receipt | `$.callBudget.observedCallCount` | `1` | `1` | PASS |
| A3-LIVE-04 | recovery receipt | `$.providerProof` | Alibaba, qwen-turbo, HTTP 200, success true | exact match | PASS |
| A3-LIVE-05 | recovery receipt | `$.contextObservation.approvedContextIncluded` | `true` | `true` | PASS |
| A3-LIVE-06 | recovery receipt | `$.correlation.traceCount` | `1` | `1` | PASS |
| A3-LIVE-07 | recovery receipt | `$.secretSafety` | all false | all false | PASS |
| A3-LIVE-08 | launch diagnostic | `$.callBudget.observedCallCount` | `0` | `0` | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | one real Alibaba approved-context happy path through existing CVF Web `/api/execute` |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: approved Flow context reached the real provider and correlated to durable SOT3 evidence |
| receiptEvidence | CVF_RECEIPT_PRESENT: recovery receipt and hash manifest present; original blocked receipt retained |
| actionEvidence | ACTION_EVIDENCE_PRESENT: one recovery provider call, HTTP 200, one SOT3 trace, and complete owner-ID chain |
| invocationBoundary | canonical Python runner, one-use permit, route-adjacent live test, Alibaba `qwen-turbo` |
| interceptionBoundary | pass-through fetch observation only; no provider response, route, IDE, shell, MCP, or CLI interception claim |
| claimLanguage | `REAL_PROVIDER_APPROVED_CONTEXT_PROVEN_BOUNDED` only |
| forbiddenExpansion | no A4/A5, roadmap-final, release, production, public, scale, universal, or user-value assertion |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: A3 uses operator-local credentials and private provenance evidence. No
public-sync action or public capability claim is authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | `docs/baselines/CVF_GC018_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md` | `Status: A3_CLOSED_PASS_BOUNDED_A4_PACKET_NEXT` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: A3 does not scan or classify a corpus and has no GC-051 registry ownership | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/README.md` | BLOCKED with reason: A3 does not modify corpus routing and has no registry front-door ownership | BLOCKED with reason |
| External evidence digest | recovery receipt SHA-256 `cec9eb0925e7afaec48b3af92fb55abb0484b92480b2ee5d1987e87a1b40df56` | recomputed PASS; unsigned, no external anchor | PASS |
| System loop interlock | N/A with reason: no automated loop edge added | N/A | N/A with reason |
| Session continuity | separate post-material session sync | pending until material commit | N/A with reason |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | reviewer/closer |
| Provider or surface | local private provenance repository and Alibaba DashScope-compatible API |
| Session or invocation | SOT3-ACT-A3 bounded repair, recovery, and closure, 2026-07-13 |
| Working directory | repository root |
| Command or tool surface | source review, `apply_patch`, Python runner, Vitest, TypeScript, manifest verification, secret-value scan, ADIF and governance gates |
| Target paths | A3 runner; three recovery evidence files; A3 baseline; A3 work order; parent roadmap; completion review |
| Allowed scope source | A3 Reviewer Closure Conversion and operator authorization for bounded repair, ADIF guard, runner-only recovery, and unmetered Alibaba calls on 2026-07-13 |
| Before status evidence | blocked worker evidence committed at `dd64479bc`; recovery-ready session commit `40d790039` |
| After status evidence | complete real-provider receipt correlation and A3 bounded closure |
| Diff evidence | `git diff --name-status`; receipt/manifest; focused tests; TypeScript; secret scan; closure gates |
| Approval boundary | A3 bounded repair, recovery, closure, and material commit only |
| Claim boundary | `REAL_PROVIDER_APPROVED_CONTEXT_PROVEN_BOUNDED` only |
| Agent type | reviewer/closer |
| Invocation ID | sot3-act-a3-reviewer-recovery-closure-2026-07-13 |
| Expected manifest | `scripts/run_cvf_sot3_a3_live_proof.py`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-launch-diagnostic-2026-07-13.json`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-receipt-2026-07-13.json`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-manifest-2026-07-13.json`; `docs/baselines/CVF_GC018_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md`; `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md`; `docs/reviews/CVF_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_COMPLETION_2026-07-13.md` |
| Actual changed set | `scripts/run_cvf_sot3_a3_live_proof.py`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-launch-diagnostic-2026-07-13.json`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-receipt-2026-07-13.json`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-manifest-2026-07-13.json`; `docs/baselines/CVF_GC018_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md`; `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md`; `docs/reviews/CVF_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_COMPLETION_2026-07-13.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This closure proves one bounded real-provider happy path in which SOT3
Flow-approved context reached Alibaba `qwen-turbo` through the existing CVF Web
route and correlated to the durable SOT3 evidence chain. It also proves the
local A3 test's direct-invocation guard and diagnostic-preserving recovery.
It does not prove A4 rejection/recovery coverage, A5 release-quality proof,
production readiness, public availability, scale, universal enforcement,
malicious-bypass resistance, external immutability, or real-user value.

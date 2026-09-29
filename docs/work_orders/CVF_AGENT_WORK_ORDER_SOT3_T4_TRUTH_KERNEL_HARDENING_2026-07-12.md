# CVF Agent Work Order - SOT3-T4 Truth Kernel Hardening

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-12

Work Order ID: SOT3-T4

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `bbae4a92b`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_MUST_CAPTURE_AT_CLOSURE`

## Dispatch Prompt Envelope

Role: no-commit deterministic TypeScript Kernel package worker.

Canonical packet: this work order and paired T4 GC-018.

Commit mode: WORKER_MUST_NOT_COMMIT

Base: capture HEAD and full status before edits.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

Current-time notes: T0-T3 are accepted; only T4 is released.

Do-not-misread notes: truth-foundation doctrine remains its owner; retained
Kernel code is evidence, not import authority; T2 overrides prototype shapes.

Required first actions: startup reads, roadmap, baseline, T1-T3 reviews, T2
contracts/negative cases, truth-foundation owner, retained README and cited sources.

Return contract: package implementation and `COMPLETE_PENDING_REVIEW`, no commit.

## Purpose

Implement the bounded deterministic Truth Kernel defined by the paired baseline.

## Target / Source

Target root is `EXTENSIONS/CVF_TRUTH_KERNEL/`; source precedence is the paired
baseline Source Verification Block.

## Scope / Methodology

Rewrite contract-first. Implement the smallest coherent local package proving
request admission, evaluation, receipt issuance/hash verification, replay
control, revocation, and eligible TruthReference issuance.

## Authority Chain

Operator continuation -> main roadmap -> accepted T1 owner decision -> T2
contracts -> accepted T3 Refinery -> paired GC-018 -> this work order.

## Agent Roles

Dispatcher owns source fidelity; worker implements without commit;
reviewer/closer audits all contract dependencies in one first-pass matrix.

## Worker Autonomy / No-Question Rule

Repair in-scope package/test defects. Stop for a T2 contradiction, external
dependency, forbidden path, or scope expansion.

## Required First Reads

Startup front doors; guard orientation; literal gotchas; roadmap; baseline;
T1-T3 completion reviews; T2 contracts/negative cases; truth-foundation owner;
retained README, strict gate, verification gate, receipt, hash, types and tests.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/generate_active_session_state.py --check
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | accepted CVF contracts plus retained Kernel evidence |
| Scope classification | EXTERNAL_LEGACY_ADAPTIVE_IMPLEMENTATION |
| Intake role | no-commit package worker |
| Risk sensitivity | HIGH: exclusive trust-decision and receipt authority |
| Provider surface | local deterministic tools only |
| Reviewer role | contract, hash, binding, replay, authority and negative-case audit |
| Routing decision | WORKER_MUST_NOT_COMMIT |
| Escalation condition | T2 contradiction, new dependency, or forbidden path |
| Public route | DEFERRED_PRIVATE_ONLY |
| canonical route mode | MULTI_AGENT_MULTI_ROLE |
| selected role route | dispatcher -> package worker -> reviewer/closer |

## Allowed Scope

Only `EXTENSIONS/CVF_TRUTH_KERNEL/**` and
`docs/reviews/CVF_SOT3_T4_WORKER_RETURN_2026-07-12.md`.

## Forbidden Scope

Truth Flow, Refinery mutation, other extensions, governance checkers/hooks,
session files, Web/UI, provider/live, public-sync, package activation,
database/SOT-index service, monitors, adapters, and direct retained-tree copying.

## Source Verification Block

Use and reopen every row in the paired baseline. T2 and truth-foundation CVF
contracts are canonical; retained sources have ADAPT or REJECT authority only.

## Implementation Contract

- Public contracts: KernelEvaluationRequest, KernelDecision, TruthReceipt,
  TruthReference, EvidenceRecord, ObligationRecord, VerificationResult.
- Engine owns evaluation results; callers supply references, not outcomes.
- Local immutable resolvers bind request, packet, evidence, obligations,
  verification results, decision, receipt and reference identities.
- Inject clock, ID factory, authorized policy/rule version, and deterministic
  verification methods; no wall clock or random global.
- Emit a receipt for every decision outcome.
- Reproduce and test the exact canonical receipt preimage/vector.
- Mint TruthReference only through full receipt-decision-request resolution.
- README records integrity-is-not-truth and no-AI/no-provider boundaries.

## Negative Test Matrix

| Case | Required result |
|---|---|
| empty evidence refs | never ACCEPT_EVIDENCE_CANDIDATE |
| empty Kernel verification results | accepting receipt not ISSUED |
| packet hash mismatch or packet not READY_FOR_KERNEL | reject before evaluation |
| evidence/obligation bound to another packet/source | reject or require evidence |
| stale policy/rule version | reject or escalate; never silently accept |
| non-canonical/partial receipt hash or published-vector mismatch | receipt invalid |
| duplicate receipt identity | replay rejected |
| non-acceptance receipt | TruthReference issuance rejected |
| missing decision/request, binding/content/version mismatch, failed obligations | TruthReference issuance rejected |
| FAIL/BLOCKED verification or revoked receipt | TruthReference issuance rejected |
| invalid/expired reference dates at issuance | issuance rejected |
| same injected input twice | byte-equivalent outputs |
| caller-supplied approval/result/authority boolean | ignored or rejected |
| AI/provider/network dependency | dependency proof fails |

## Dual Agent Surface Matrix

| Surface | Role | Interface | Authority/risk boundary | Evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | worker/reviewer | local files and commands | worker cannot commit; Kernel package only | tests and return | local process |
| EXTERNAL_AGENT_CLI_MCP | future worker | same packet | no provider authority or MCP support | locally revalidated return | NOT_IMPLEMENTED_WITH_REASON: separate adapter authorization required |

## ADIF Defect Registry Disclosure

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024.

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit package worker -> reviewer/closer |
| phase | SOT3-T4 Truth Kernel hardening |
| contractSource | canonical contract citation immediately above |
| baseHeadFor(phase) | dispatch=`bbae4a92b`; execution=worker-captured HEAD; closure=reviewer-captured base |
| changedSetScope(phase) | target package root plus one worker return |
| traceScope(phase, actor) | reads, manifest, code, schemas, tests, scans, gates, no-commit evidence |
| commitOwner(phase) | worker=WORKER_MUST_NOT_COMMIT; reviewer owns accepted commit |
| crossBatchIsolation | T5-T7, other extensions, session, provider, public paths excluded |
| nextMoveSurfaces | reviewer/session-sync steward only after acceptance |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_SOT3_T4_COMPLETION_REVIEW_2026-07-12.md`

reviewerOwnedClosurePaths: completion review and accepted package material;
session continuity in a separate commit.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Instruction | Evidence |
|---|---|---|
| packet-bound verification | immutable resolver chain | negative tests |
| obligation/provenance/receipt authority | exact T2 contracts | schemas and types |
| release/freshness fail closed | eligible reference issuer | NC matrix |
| T5 held | no Flow paths | exact status/diff |

## Execution Plan

Capture base; derive T2 types/schemas; implement deterministic stores,
evaluation, receipts and reference issuance; run full negative matrix,
typecheck/build/test/hash/dependency scans; return without commit.

## Write Ownership

Worker owns target package and worker return only. Reviewer owns closure/commit.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
npm --prefix EXTENSIONS/CVF_TRUTH_KERNEL run typecheck
npm --prefix EXTENSIONS/CVF_TRUTH_KERNEL run build
npm --prefix EXTENSIONS/CVF_TRUTH_KERNEL test
rg -n -i "openai|anthropic|provider|prompt|agent|fetch\(|axios|randomUUID|Date\.now|new Date\(\)" EXTENSIONS/CVF_TRUTH_KERNEL/src
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --check
git status --short --untracked-files=all
git rev-parse --short HEAD
```

## Review Gate

Reviewer builds one dependency-closure matrix before repair and recomputes all
negative cases, receipt vector, binding equality, resolver failures,
dependency scan, exact exports, status/diff, and committed pre-closure range.

## Evidence Requirements

Exact manifest, test counts, typecheck/build output, published receipt-vector
proof, determinism/dependency scans, no-copy disposition, status/diff and unchanged HEAD.

## Acceptance Criteria

All baseline invariants and negative cases pass; no forbidden dependency or
out-of-scope path exists; worker did not commit.

## Operator Checkpoint

No checkpoint for in-scope rewrite. Stop for contract change, dependency,
adapter/database/monitor/Flow integration, activation, or provider/live proof.

## Closure Checklist

- [ ] contract types and schemas complete;
- [ ] request admission and packet binding fail closed;
- [ ] empty evidence/results cannot accept;
- [ ] receipt canonical vector and replay proof pass;
- [ ] eligible-only reference issuance and full resolution pass;
- [ ] determinism and no-AI/no-provider proof pass;
- [ ] exact manifest and no-commit evidence returned.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`,
or `BLOCKED_WITH_REASON`; never a closed-equivalent worker status.

## Worker Return Conditions

Return after all commands pass or one source-backed blocker. Do not commit.

## Return / Escalation Conditions

Escalate only contract contradiction, dependency, forbidden path, or expansion.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| durable family | `EXTENSIONS/CVF_TRUTH_KERNEL/` |
| stable front door | package README |
| canonical owner | new T4 runtime owner; truth-foundation remains doctrine owner |
| generated aggregate | NOT_APPLICABLE_WITH_REASON: direct package source authority |
| index/update route | package exports and later accepted Catalog projection |
| claim boundary | private package candidate until reviewer acceptance |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: T0 already established the 305-file manifest and
T0R-T3 accepted the semantic, owner, contract, and upstream package inputs.
T4 implements only the accepted Kernel capability subset; T7 owns final
per-file terminal reconciliation.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | retained Kernel evidence -> accepted T1-T3 contracts/owners -> CVF-native T4 rewrite |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing doctrine plus new Kernel package candidate |
| Disposition | ADAPT and REJECT_DIRECT_IMPORT |
| Claim boundary | selective rewrite only; retained source is not runtime authority |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-T4 --title "Truth Kernel Hardening" --date 2026-07-12 --base bbae4a92b --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | no-commit TypeScript package worker |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Added T2 Kernel contracts, canonical hash, resolver, negative-case, handoff and storage controls. |
| checkerReadAheadConfirmation | dispatch, structural, handoff, external-intake, worker-return and file-size checkers |
| docOnlyNewFields | deterministic store and verifier interfaces |
| claimBoundary | dispatch only; no implementation proof |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Reviewer Closure Conversion; Roadmap-to-Work-Order Trace Matrix; Public Export Disposition |
| gateRunPurpose | confirm source-derived dispatch before implementation |
| claimBoundary | gates do not prove package semantics |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | SOT3-T4 packet authoring, 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | governed reads, rg, source verification, apply_patch, dispatch gates |
| Target paths | paired T4 baseline and this work order |
| Allowed scope source | operator request to create the next work order |
| Before status evidence | HEAD `bbae4a92b`; clean worktree; target package absent |
| After status evidence | T4 packet authored; implementation awaits pre-dispatch |
| Diff evidence | exact two-path packet diff before commit |
| Approval boundary | T4 packet authoring and bounded no-commit dispatch |
| Claim boundary | no package behavior proof, T5-T7, provider/live or public claim |
| Agent type | dispatcher |
| Invocation ID | `sot3-t4-dispatch-authoring-2026-07-12` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation packet; no public-sync authorization.

## Claim Boundary

This work order authorizes one bounded no-commit T4 worker after pre-dispatch.
It does not authorize T5-T7, provider/live, public, activation, or Flow work.

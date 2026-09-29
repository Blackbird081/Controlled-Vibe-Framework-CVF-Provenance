# CVF GC-018 GC-009/GC-010 Production Caller T1-Interface Design

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_DISPATCH_READY

Batch ID: GC009-GC010-PCALLER-T1I

Date: 2026-07-25

Dispatch base head: `c6ca6428c`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one bounded documentation-only design tranche that source-verifies
the exact context-preserving `MandatoryGateway` interface change and the
receipt/audit projection adapter that T0A found missing before any GC-009
production composition can be released. This baseline does not authorize
creating the interface change, editing `mandatory-gateway.ts`, editing the
execute route, adding package exports, adding tests, or any T1 runtime
composition. It only authorizes designing and source-verifying the interface
contract so that a future, separately authorized implementation packet has an
unambiguous, non-lossy specification to build against.

## Scope / Target / Owner Boundary

The no-commit worker may create exactly:

- `docs/audits/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_2026-07-25.md`;
- `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_WORKER_RETURN_2026-07-25.md`.

The worker may read current CVF source and governed records. It may not edit
`EXTENSIONS/`, package manifests, tests, `governance/compat/`, session state,
handoffs, public-sync, or any other governed artifact.

## Decision / Baseline / Proposed Tranche

This is an interface-design-contract decision, not implementation. It must
source-verify and specify:

- the exact new or extended `MandatoryGateway`/`GuardRequestContext` method
  signature that accepts an already-built canonical context and preserves
  `requestId` and every canonical field without semantic loss;
- the exact mechanism preventing duplicate `engine.evaluate()` calls between
  the future route integration and the gateway;
- the exact bypass-configuration requirement so the execute route runs with
  no gateway bypass actions;
- the exact receipt/audit adapter shape that projects a secret-safe gateway
  summary into the existing Web receipt/audit seam
  (`buildEvidenceReceipt`/`appendAuditEvent`) without claiming the gateway's
  in-memory `auditLog` is durable evidence;
- which of T0A's four "smallest future changed set" candidate files
  (`mandatory-gateway.ts`, its test, the proposed singleton, the proposed
  singleton test, `route-guard-gateway.ts`, its test, `route.ts`) the
  interface change itself touches, distinct from files a later T1 packet
  would touch to wire the singleton and route.

The worker must issue exactly one terminal token from the companion work
order. `NOT_READY` remains a valid, complete outcome if source evidence does
not support a lossless interface specification.

## Evidence / Verification

Dispatch evidence consists of the T0A independent material closure at commit
`0e97a0ace` and continuity commit `c6ca6428c`
(`docs/reviews/CVF_GC009_GC010_PRODUCTION_OWNER_DESIGN_T0A_COMPLETION_2026-07-25.md`,
`Status: CLOSED_PASS_BOUNDED_NOT_READY_OWNER_CONTRACT_REQUIRES_INTERFACE_CHANGE`),
current source citations in `## Source Verification Block`, the ADIF resolver
result, the three-path changed set, and pre-dispatch/commit-steward gate
output. Worker evidence is defined by the companion work order and must be
recomputed at the worker's captured execution base.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition | Status |
|---|---|---|---|---|
| Independent T0A closure | `docs/reviews/CVF_GC009_GC010_PRODUCTION_OWNER_DESIGN_T0A_COMPLETION_2026-07-25.md` | `0e97a0ace` | `CLOSED_PASS_BOUNDED_NOT_READY_OWNER_CONTRACT_REQUIRES_INTERFACE_CHANGE`; preferred owner `mandatory-gateway-singleton.ts` documented; interface and receipt-adapter gap explicit | PASS |
| Operator checkpoint | operator confirmation in the active session after commit `c6ca6428c` naming the T0A interface-change gap as the reason to authorize a fresh source-verified packet | N/A with reason: operator authorization is conversation authority, recorded into this governed packet and later continuity sync | authorize a fresh source-verified interface-design packet; keep T1 runtime composition, T2, T3, and T4 HOLD | PASS |
| Existing runtime gap | `docs/reference/system_chain/gaps/entries/gc009_gc010_no_production_caller.json` | current at dispatch base `c6ca6428c` | `IMPLEMENTED_NOT_INVOCATION_PROVEN` | PASS |

This dependency table does not release T1 runtime composition, T2, T3, or T4.
It releases only the interface-design tranche described above.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | N/A with reason: this baseline was authored directly from the T0A baseline/work order template (`docs/baselines/CVF_GC018_GC009_GC010_PRODUCTION_OWNER_DESIGN_T0A_2026-07-25.md`) rather than `build_dispatch_packet_scaffold.py`, since the T0A packet already provides a source-verified, checker-compliant structural template for this same lane |
| generatedProfile | generic-worker-dispatch plus no-commit worker and held-dependency trigger profiles, inherited from the T0A packet shape |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced T0A-specific dependency, source-verification, and doc-only-field content with T1-Interface-specific content; narrowed scope to the interface/adapter design question only |
| checkerReadAheadConfirmation | dispatch-quality, manifest-table, prompt-envelope, handoff-boundary, read-ahead, structural, operation-trace, and Delta claim checkers read before final authoring |
| docOnlyNewFields | proposed interface method signature and adapter shape are documentation-only until a later implementation work order independently source-verifies and authorizes them |
| claimBoundary | scaffold provenance only; no runtime or production-owner claim |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T0A accepted not-ready with interface-change requirement | VALUE_SET | `docs/reviews/CVF_GC009_GC010_PRODUCTION_OWNER_DESIGN_T0A_COMPLETION_2026-07-25.md` | Findings / Position; Risk / Corrective Action | `NOT_READY_OWNER_CONTRACT_REQUIRES_INTERFACE_CHANGE` | T0A completion review | ACCEPT |
| T0A preferred owner and blocking findings | VALUE_SET | `docs/audits/CVF_GC009_GC010_PRODUCTION_OWNER_DESIGN_T0A_2026-07-25.md` | Required Design Question Answers 1, 3, 4, 6 | `proposedOwnerModule`; `guardEvaluationDisposition` | T0A audit decision | ACCEPT |
| Gap remains invocation-unproven | VALUE_SET | `docs/reference/system_chain/gaps/entries/gc009_gc010_no_production_caller.json` | `currentStatus`; `closeCondition` | `currentStatus`; `closeCondition` | system-chain gap entry | ACCEPT |
| `MandatoryGateway.check` builds its own request ID and accepts only a context subset | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 80-137 | `check` | guard-contract gateway helper | ACCEPT |
| Gateway applies substring bypass before evaluation | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 95-107 | `bypassActions`; `check` | guard-contract gateway helper | ACCEPT |
| Gateway calls `this.engine.evaluate` exactly once per `check` | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 80-140 | `check` | guard-contract gateway helper | ACCEPT |
| Gateway audit is in-memory only | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 69, 105, 118, 178, 195-197 | `auditLog`; `getAuditLog` | guard-contract gateway helper | ACCEPT |
| Canonical `GuardRequestContext` full field set | LITERAL_INVARIANT | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | lines 93-110 | `GuardRequestContext` | guard-contract type | ACCEPT |
| Execute route directly evaluates the shared engine once, no gateway involved | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 561, 578 | `getSharedGuardEngine`; `guardEngine.evaluate` | execute POST route | ACCEPT |
| Web receipt builder is the existing governance evidence-receipt construction seam | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 55-78, 241-280 | `BuildGovernanceEvidenceReceiptInput`; `buildEvidenceReceipt` | Web evidence receipt | ACCEPT |
| Web audit event is the existing durable audit seam | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 140-152 | `appendAuditEvent` | control-plane event store | ACCEPT |
| Package/barrel omit the gateway entirely | LITERAL_INVARIANT | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | package lines 8-27; barrel full export surface | `exports`; `files`; named exports | guard-contract package | ACCEPT |
| Execute route is an active GC-023 owner near threshold | VALUE_SET | `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | `activeOwners`, lines 42-47 | `activeOwners`; `status` | governed file-size registry | ACCEPT |
| Prior route exception is a resolved non-usable tombstone | VALUE_SET | `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | exception entries, lines 159-172 | `status`; `removalProcedure` | governed file-size registry | ACCEPT |

## New Doc-Only Fields

| Proposed item | Documentation meaning | Runtime/source status |
|---|---|---|
| `contextPreservingMethodName` | exact future method name/signature the worker proposes to add to or extend on `MandatoryGateway` that accepts a pre-built `GuardRequestContext` verbatim | DOC_ONLY_NEW; worker must not implement it |
| `receiptAdapterShape` | exact future secret-safe field projection from `GatewayResult` into the existing Web receipt/audit seam | DOC_ONLY_NEW; worker must not implement it |
| `bypassConfigurationRequirement` | exact future configuration value or flag that disables gateway bypass actions for the execute route | DOC_ONLY_NEW; worker must not implement it |
| `duplicateEvaluationProofMechanism` | exact future deterministic test/assertion approach proving exactly one `engine.evaluate` call per request | DOC_ONLY_NEW; worker must not implement it |

## Current Runtime Freshness Verification

At dispatch base `c6ca6428c`, `MandatoryGateway.check` still builds its own
`gw-*` request ID (`mandatory-gateway.ts:124`), still applies substring bypass
matching before evaluation (`mandatory-gateway.ts:96-107`), and still calls
`engine.evaluate` exactly once internally (`mandatory-gateway.ts:140`). The
execute route still evaluates the shared engine directly with no gateway
involvement (`route.ts:561,578`). The T1-Interface worker must recompute all
of these facts at its own `executionBaseHead`, not merely cite this table.

## Negative Search And Collision Discipline

The query
`rg -n "GC009-GC010-PCALLER-T1I|PRODUCTION_CALLER_T1_INTERFACE_DESIGN" docs CVF_SESSION`
must return zero matches before this packet's canonical paths are created.
Proposed interface/adapter names are recorded only in `## New Doc-Only Fields`;
they are not promoted into Source Verification. The same-name
`GuardRuntimeEngine` collision between the canonical guard-contract engine and
the MCP-local engine (documented in T0 and T0A) remains irrelevant to this
interface-design question, since it concerns only `MandatoryGateway`'s own
method contract, not engine selection.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`,
lifecyclePhase=`pre-dispatch`

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50`

Returned defects (20): ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015,
ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044,
ADIF-0045, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031,
ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

Dispatch impact: source claims use exact paths and symbols; proposed
interface/adapter names are doc-only; no protected path is writable; worker
and reviewer manifests are separate; the Verified path or symbol column
carries only the symbol/path, never a value or type (ADIF-0006 discipline).

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_tables.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | `Dependency Release Evidence`; `Source Verification Block`; `New Doc-Only Fields`; exact ADIF query line; `DRAFT_PENDING_REVIEW`; `Public Export Disposition`; ASCII-only prose (no em-dash/arrow characters) |
| gateRunPurpose | confirm baseline dispatch shape after source verification, before first gate run |
| claimBoundary | baseline authoring evidence only; pre-dispatch PASS is recorded after the full packet is complete and reviewed |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | source-verify the exact context-preserving gateway interface method and receipt/audit adapter shape that T0A found missing, without implementing either |
| scopeClassification | bounded documentation-only interface-design tranche |
| riskSensitivity | R0 |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | dispatcher authors and releases; no-commit worker designs; independent reviewer/closer accepts and commits |
| escalationCondition | any runtime, package, test, checker, provider, CLI/MCP, public, or T1-runtime-release need |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | dispatcher, worker, reviewer/closer in this repository | two-output documentation scope only | source citations, interface-design matrix, terminal token | native governed document workflow | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | not applicable; this tranche concerns only the internal guard-contract gateway interface, not any CLI/MCP surface | no invocation, ingress, mutation, or adapter authority | N/A with reason: no CLI/MCP candidate is compared in this interface-design tranche | no adapter authorized | `NOT_APPLICABLE_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external repository, packet, or provider output is consumed |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this baseline and companion work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | CVF-governed source remains the only authority |

## Epistemic Process Block

### Expected Result / Prediction

Current source should support specifying one lossless context-preserving
`MandatoryGateway` method and one bounded receipt/audit adapter shape,
because both the gateway's exact limitations (T0A questions 3, 6) and the
existing Web receipt/audit seams are already source-verified and stable.

### Evidence Comparison

The worker must compare this prediction against the gateway's current
`check` signature, its request-ID/bypass/evaluate behavior, the canonical
`GuardRequestContext` field set, and the existing Web receipt/audit builder
signatures.

### Contradiction Or Gap Disposition

Contradictory evidence (for example, a canonical context field that cannot be
losslessly represented by any gateway method signature) must produce a
not-ready terminal token, not a forced ready result.

### Claim Update

The worker records whether the interface and adapter specification is
confirmed, narrowed, rejected, or parked, and why.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | packet-author (Claude, Sonnet 5) |
| Provider or surface | Claude Code CLI, operator manual copy/paste invocation |
| Session or invocation | GC009-GC010-PCALLER-T1I baseline authoring, 2026-07-25 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, Grep, Bash (`git rev-parse`, `git status`, `python governance/compat/run_adif_defect_resolver.py`) |
| Target paths | this baseline; companion work order; companion roadmap update |
| Allowed scope source | operator authorization following the T0A interface-change finding at commit `c6ca6428c` |
| Before status evidence | HEAD `c6ca6428c`; clean worktree |
| After status evidence | three-path dispatch packet pending review and commit |
| Diff evidence | `git status --short --untracked-files=all` |
| Approval boundary | documentation dispatch authoring only; no runtime, provider, CLI/MCP invocation, public-sync, or commit |
| Claim boundary | repo-local trace only; no OS/user attribution |
| Agent type | packet-author |
| Invocation ID | `gc009-gc010-production-caller-t1-interface-design-baseline-2026-07-25` |
| Expected manifest | this baseline; companion work order; companion roadmap update |
| Actual changed set | same three paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | documentation-only interface/receipt-adapter design dispatch baseline |
| claimDisposition | N/A with reason: no runtime execution behavior is implemented or claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT - no runtime receipt is created |
| actionEvidence | ACTION_EVIDENCE_PRESENT - source verification and dispatch gates |
| invocationBoundary | governed local document authoring only |
| interceptionBoundary | no IDE, shell, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | authorizes a future interface/adapter design decision only, not implementation |
| forbiddenExpansion | no source/test/package/checker/provider/live/public/session mutation, T1 runtime release, deployment, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch baseline; no public-sync authorization.

## Claim Boundary

This baseline authorizes a source-verified interface/receipt-adapter design
decision only. It does not implement the interface change, does not
establish a production owner in runtime, does not release T1 runtime
composition or T2-T4, and does not authorize source, package, test, checker,
provider, CLI/MCP, public, session, deployment, or production changes.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this baseline | `Status: REVIEWER_ACCEPTED_DISPATCH_READY` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_2026-07-25.md` | `Status: REVIEWER_ACCEPTED_DISPATCH_READY` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_COMPLETION_2026-07-25.md` | does not exist yet; worker execution and independent closure remain pending | N/A with reason: substantive execution and independent closure remain pending |
| Roadmap state | `docs/roadmaps/CVF_GC009_GC010_PRODUCTION_CALLER_AND_BOUNDED_E2E_RUNTIME_ROADMAP_2026-07-25.md` | T1-Interface dispatch pending review; T1-runtime/T2-T4 `HOLD_*` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no new corpus packet; aggregate drift check passes | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no new corpus entry required for a bounded interface-design tranche with no corpus scan | PASS |
| External evidence digest | N/A with reason | no external evidence consumed | N/A with reason |
| System loop interlock | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_GAP_INDEX.json` | gap entry remains `IMPLEMENTED_NOT_INVOCATION_PROVEN` pending independent acceptance | N/A with reason: gap closure requires independent reviewer acceptance, not this dispatch |
| Session continuity | active front doors | not updated by this baseline | N/A with reason: session-sync is a separate reviewer/closer-owned step |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Terminal disposition | one fixed enum token | not yet recorded; worker execution pending | N/A with reason: pending worker execution |
| Worker commit | none | not yet executed | N/A with reason: pending worker execution |
| T1-runtime release | HOLD until T1I independent closure | T1-runtime/T2-T4 remain `HOLD_*` | PASS |
| Registry JSON/Markdown acceptance | no new corpus packet required | no corpus scan performed by this dispatch | PASS |

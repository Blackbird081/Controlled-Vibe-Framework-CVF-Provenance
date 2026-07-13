# CVF GC-018 Baseline - SOT3 Activation A1 Scoped Knowledge Context Product Adapter

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-07-13

Baseline ID: GC-018-SOT3-ACT-A1

dispatchBaseHead: `e4d56f2be`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: independent reviewer/closer

Worker target: delegated implementation worker

## Purpose

Authorize one bounded local product-integration tranche that inserts the real
Refinery, Truth Kernel, and Truth Flow public APIs into the CVF Web scoped
knowledge-context path before provider prompt construction.

## Target / Source

The target is the tenant-scoped knowledge retrieval seam in `/api/execute`.
The A0 architecture decision and current runtime/package source control over
chat, provider-local memory, or earlier summaries.

## Scope / Methodology

Add source-provenance metadata to knowledge chunks, a focused SOT3 product
adapter, a route-sized knowledge-context helper, activation modes, local audit
projection, package resolution, and deterministic tests. Preserve existing
behavior in `OFF`; prove fail-closed context admission in `ENFORCE`.

## Findings / Position

The product seam exists, but current knowledge chunks carry no source owner,
capture time, source type, confidentiality, purpose, raw reference, or expected
content hash. A1 must not invent those facts at retrieval time. Provenance is
optional for backward-compatible storage, but mandatory for SOT3 admission.

## Risk / Corrective Action

Risk is R2: A1 changes construction of provider context when explicitly
enabled. Corrective controls are default `OFF`, configuration-only rollback,
no raw fallback in `ENFORCE`, deterministic dependency injection, local-only
tests, audit evidence, and reviewer-owned commit.

## Decision / Baseline / Proposed Tranche

CLOSED_PASS_BOUNDED: one no-commit A1 implementation. A2 persistence, external
provider invocation, A3-A5 proof, public export, and readiness claims remain
outside this baseline.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| A0 architecture decision | `docs/reference/sot_three_layer/CVF_SOT3_ACTIVATION_ARCHITECTURE_DECISION.md`; commit `a777c3fd9` | A0 records `A0_PASS_BOUNDED` and selects the knowledge seam | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md`; commit `a777c3fd9` | next move is fresh A1 packet authoring | ACCEPT |
| Session routing | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; commit `e4d56f2be` | current mode routes to A1 packet authoring only | ACCEPT |
| Operator checkpoint | current operator instruction on 2026-07-13 | create a delegated implementation work order | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Execute retrieves scoped chunks before prompt construction | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | knowledge retrieval block | `queryKnowledgeChunks` | execute route | ACCEPT |
| Provider call follows knowledge prompt construction | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | execute block | `executeAI` | execute route | ACCEPT |
| Retrieval filters organization and team scope | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-retrieval.ts` | scope and query functions | `scopeAllowsCollection` | `queryKnowledgeChunks` | ACCEPT |
| Current chunk contains only ID, content, and keywords | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts` | `KnowledgeChunk` declaration | `KnowledgeChunk` | knowledge store contract | ACCEPT |
| Current chunk does not provide SOT3 provenance | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts` | `KnowledgeChunk` declaration | `KnowledgeChunk` | knowledge store contract | ACCEPT |
| Prompt helper accepts pre-governed context | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-context-injector.ts` | `buildKnowledgeSystemPrompt` | `buildKnowledgeSystemPrompt` | knowledge prompt helper | ACCEPT |
| SourceEnvelope requires identity, provenance, hash, scope, and status | EXISTS | `EXTENSIONS/CVF_REFINERY/src/types/source-envelope.ts` | `SourceEnvelope` declaration | `SourceEnvelope` | Refinery intake contract | ACCEPT |
| Refinery always executes the required stage chain | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_REFINERY/src/pipeline/engine.ts` | `RefineryEngine.run` | `REQUIRED_STAGE_CHAIN` | `RefineryEngine` | ACCEPT |
| Refinery exports the canonical packet hash | EXISTS | `EXTENSIONS/CVF_REFINERY/src/index.ts` | public exports | `computeRefineryPacketHash` | Refinery package entrypoint | ACCEPT |
| Kernel exposes packet/evidence registration, evaluation, and reference issuance | EXISTS | `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts` | `TruthKernel` public methods | `TruthKernel` | Truth Kernel | ACCEPT |
| Flow resolves Kernel authority and owns distribution actions | EXISTS | `EXTENSIONS/CVF_TRUTH_FLOW/src/index.ts` | public exports | `DistributionEngine` | Truth Flow package entrypoint | ACCEPT |
| Audit events accept typed payload records | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | `appendAuditEvent` | `appendAuditEvent` | control-plane event store | ACCEPT |
| Existing route test observes the actual provider system prompt | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.knowledge.test.ts` | tenant-matching test | `executeAIMock` | execute knowledge route test | ACCEPT |
| CVF Web lacks all three SOT3 package dependencies | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependencies | `dependencies` | npm manifest | ACCEPT |
| Next config owns private package transpilation | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts` | `transpilePackages` | `transpilePackages` | Next configuration | ACCEPT |
| Execute route is near the governed hard threshold | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | physical line count on dispatch base | `POST` | CVF Web execute route | ACCEPT |

## New Doc-Only Fields

These names are proposed by A1 and do not exist at dispatch time.

| Proposed field or symbol | Type | Required semantics |
|---|---|---|
| `KnowledgeChunk.sot3Source` | `DOC_ONLY_NEW` | optional storage metadata; mandatory for SOT3 admission |
| `Sot3KnowledgeSourceMetadata` | `DOC_ONLY_NEW` | source ID/type, owner, capture time, purpose, confidentiality, expected content hash, raw reference, status, version and validity fields |
| `CVF_SOT3_KNOWLEDGE_ACTIVATION_MODE` | `DOC_ONLY_NEW` | exact values `OFF`, `SHADOW`, `ENFORCE`; missing or invalid value resolves to `OFF` |
| `Sot3KnowledgeActivationResult` | `DOC_ONLY_NEW` | mode, terminal outcome, injection permission, approved context, failure stage, and layer identifiers |
| `SOT3_KNOWLEDGE_ACTIVATION_EVALUATED` | `DOC_ONLY_NEW` | audit event containing no raw context and no secret |

## Acceptance Criteria

- CVF Web resolves the three private SOT3 packages through manifest, lockfile,
  and Next transpilation configuration.
- Existing chunks and routes remain backward compatible in `OFF`.
- Missing or incomplete provenance never becomes a SourceEnvelope by guessed
  values.
- Correct provenance and expected hash can reach Refinery
  `READY_FOR_KERNEL`, Kernel `ACCEPT_EVIDENCE_CANDIDATE`, active reference,
  and acknowledged Flow package in local tests.
- Incorrect expected hash, missing provenance, non-ready Refinery output,
  non-accepting Kernel decision, inactive reference, or failed Flow action
  produces no approved context.
- `ENFORCE` never falls back to raw retrieved chunks after rejection.
- Rejected context may allow the existing request to continue without a
  knowledge block; A1 does not add a new whole-request block policy.
- `SHADOW` evaluates and audits but preserves current provider context.
- The execute route is reduced by at least 50 physical lines through a
  same-domain extraction while preserving behavior.
- Focused tests, existing knowledge tests, non-live suite, typecheck, build,
  and file-size enforcement pass without an external provider invocation.

## Evidence / Verification

Require package-resolution evidence, focused and non-live test results,
typecheck, build, route before/after line counts, governed file-size output,
audit payload inspection, provider-mock prompt/call-count assertions, diff,
status, and unchanged worker HEAD evidence.

## Stop Conditions

- source provenance would need to be invented from retrieval time or a session
  identity;
- package resolution requires publishing or downloading a new external
  dependency;
- `ENFORCE` can inject raw context after any SOT3 rejection;
- A1 requires persistence, database mutation, external provider execution, or
  changes to SOT3 package authority semantics;
- route extraction changes unrelated governance order;
- an allowed-scope repair cannot satisfy a mandatory checker without expansion.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 30 --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021,
ADIF-0024, ADIF-0028.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Source Verification Block; New Doc-Only Fields; Dependency Release Evidence; ADIF Defect Registry Disclosure; Public Export Disposition |
| gateRunPurpose | confirmation and evidence after direct source and checker review; not first discovery |
| claimBoundary | dispatch baseline only; no implementation or live proof |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id SOT3-ACT-A1 --title "Scoped Knowledge Context Product Adapter" --date 2026-07-13 --base e4d56f2be --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SOT3-ACT-A0 PASS at a777c3fd9" --stdout --include-worker-return-skeleton` |
| generatedProfile | web-ui-dashboard plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with verified A0, Web, package, provenance, risk, and acceptance evidence |
| checkerReadAheadConfirmation | dispatch, handoff, trace, public-export, and file-size guards |
| docOnlyNewFields | provenance metadata, activation mode, result, and audit-event names listed above |
| claimBoundary | dispatch authoring provenance only |

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | PASS: read before packet authoring; no visible UI change is authorized |
| UI claim boundary | server-side execute integration only; no visual, hosted, production, or live-data claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A1_SCOPED_KNOWLEDGE_CONTEXT_PRODUCT_ADAPTER_2026-07-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SOT3_ACT_A1_SCOPED_KNOWLEDGE_CONTEXT_PRODUCT_ADAPTER_COMPLETION_2026-07-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md` | `Status: A1_CLOSED_PASS_BOUNDED_A2_PACKET_NEXT` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | aggregate drift check PASS | PASS |
| Registry Markdown | `docs/corpus-intelligence/README.md` | existing registry front door | PASS |
| External evidence digest | N/A with reason: local non-live implementation | N/A | N/A with reason |
| System loop interlock | N/A with reason: no automated loop edge | N/A | N/A with reason |
| Session continuity | separate post-material session sync | pending until material commit | N/A with reason |

Reason: private-provenance product integration only; no public-sync mutation.

## Claim Boundary

This baseline authorizes A1 local product wiring and tests only. It does not
authorize durable evidence A2, real-provider A3/A4, release proof A5, public
export, production readiness, or user validation.

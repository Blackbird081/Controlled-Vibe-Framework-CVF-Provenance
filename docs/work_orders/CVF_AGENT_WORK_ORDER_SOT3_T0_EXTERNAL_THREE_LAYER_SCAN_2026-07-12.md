# CVF Agent Work Order - SOT3-T0 External Three-Layer Scan

Memory class: FULL_RECORD

Status: HOLD_PENDING_CLEAN_DISPATCH_COMMIT

docType: work_order

Date: 2026-07-12

Work order ID: SOT3-T0

dispatchBaseHead: `615304819`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_MUST_CAPTURE_AT_CLOSURE`

## Dispatch Prompt Envelope

Role: external-review worker. CVF dispatcher and reviewer/closer remain separate roles.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_T0_EXTERNAL_THREE_LAYER_SCAN_2026-07-12.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: executionBaseHead must be captured with `git rev-parse --short HEAD` at worker start.

Current-time notes: operator selected Claude as the intended provider surface;
provider identity does not change the external-review role, authority boundary,
or advisory status. No live API, secret, quota, or public action is authorized.

Do-not-misread notes: scan all three roots and all 305 files; read README and
TREEVIEW first but do not stop there; do not implement, import, edit retained
source, or modify the roadmap and packet.

Required first actions: read the active startup surfaces, paired roadmap,
GC-018 baseline, external review packet, this work order, and external-review
standards; then capture HEAD/status and reproduce all three source snapshots.

Return contract: `COMPLETE_PENDING_REVIEW`,
`COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` with the
three owned output paths, snapshot reconciliation, gates run, actual status,
and unchanged HEAD evidence.

## Purpose

Perform an independent full-body scan of the retained CVF Source of Truth
three-layer corpus. Challenge the supplied architecture position, reconcile
cross-layer contracts, classify selective absorption value, and return
advisory evidence for CVF review.

Success means complete 305-file accounting plus a source-backed architecture
critique. Agreement with the dispatcher is not an acceptance criterion.

## Authority Chain

- Operator instruction: 2026-07-12 request to update the roadmap, create a
  synthesis packet, and issue a work order for Claude to scan.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V41_2026-07-11.md`.
- Roadmap: `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md`.
- Review context: `docs/reviews/CVF_SOT3_T0_EXTERNAL_REVIEW_PACKET_2026-07-12.md`.
- GC-018 baseline: `docs/baselines/CVF_GC018_SOT3_T0_EXTERNAL_THREE_LAYER_REVIEW_2026-07-12.md`.
- External-review authority boundary:
  `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_STANDARD.md`.
- Returned-output route:
  `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`.

Authority boundary: CVF-governed sources control. The retained corpus and the
external return are advisory. Conflicts or missing authority stop the worker
without expanding scope.

## Agent Roles

- Operator: selects the external provider surface and owns scope expansion.
- Dispatcher: authors and releases this packet after gates and clean commit.
- Worker: external reviewer; reads corpus and creates exactly three outputs.
- Reviewer/closer: CVF role that verifies the return, classifies findings, and
  owns any accepted material commit.
- Provider lane: Claude requested by operator; no provider-specific authority.

## Scope / Target / Owner Boundary

Allowed scope:

- recursive read of all files under the three literal source roots;
- read-only comparison against current CVF authority and owner surfaces;
- isolated temporary build/test execution for source evaluation;
- creation and repair of the three worker-owned outputs;
- read-only governance and evidence commands listed below.

Forbidden scope:

- edit any retained source file;
- edit this work order, paired roadmap, packet, baseline, current CVF source,
  schemas, tests, checkers, guards, registries, generated state, session state,
  handoff, or public surface;
- create a new owner, contract, roadmap, baseline, work order, or runtime file;
- direct import, implementation, package activation, install into CVF,
  provider/live API proof, secret use, public-sync, commit, push, or release;
- treat external output as CVF source authority.

Risk ceiling: HIGH evidence rigor, documentation-only mutation, no runtime or
external side effect.

## Worker Autonomy / No-Question Rule

Proceed without operator confirmation for reads, snapshot reproduction,
temporary isolated builds/tests, owned-output authoring, and gate-shape repair
inside Allowed scope.

Escalate only for snapshot drift, unreadable source, authority conflict,
forbidden-path remediation, requested private exposure outside the three roots,
provider/live need, public action, destructive action, or scope expansion.
Routine formatting and evidence repairs inside the three output files are not
operator-preference questions.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external agent review corpus scan`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class "external agent review corpus scan" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector docs/work_orders --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Returned defect count | 0 |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | packet independently carries corpus, external-review, source-verification, no-commit, dissent, and returned-output routing controls |

## Required First Reads

Read in order before output authoring:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
4. `AGENT_HANDOFF_V41_2026-07-11.md`
5. `docs/reference/guard_orientation/README.md`
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
7. `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md`
8. `docs/reviews/CVF_SOT3_T0_EXTERNAL_REVIEW_PACKET_2026-07-12.md`
9. `docs/baselines/CVF_GC018_SOT3_T0_EXTERNAL_THREE_LAYER_REVIEW_2026-07-12.md`
10. this work order
11. `docs/reference/external_agent_review/README.md`
12. `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`
13. `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_STANDARD.md`
14. `docs/reference/external_agent_review/CVF_WORKFLOW_CHAIN_PUBLIC_REVIEW_CONTEXT.md`
15. `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`
16. current truth-foundation, skill truth-packet, evidence, provenance, and
    receipt owner candidates named in the review packet
17. each checker listed in Checker Source Read-Ahead Block before writing its
    matching output section.

## Pre-Flight Checks

Record exact results:

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
Test-Path '.private_reference/legacy/CVF_SOT 10.07/CVF_Refinery_Patch'
Test-Path '.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch'
Test-Path '.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch'
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected dispatch state:

- worker starts from the clean post-dispatch commit;
- all three roots exist;
- Refinery snapshot is 133 files, 160461 bytes, digest
  `c7ace9ccbb470514bb9fea97527976a462146b5b220df88eadc6fdc38b88cbe2`;
- Kernel snapshot is 93 files, 78007 bytes, digest
  `73e4cc652f738d70428326a013de08fc65ce4edb553dcd3e4670eb8a46765497`;
- Flow snapshot is 79 files, 78380 bytes, digest
  `e7be38e77889f6280248fc4a6ceacf354a41c8f1c331fbb2a491e29f8a27858f`.

Snapshot mismatch returns `BLOCKED_WITH_REASON`; do not silently rewrite
expected values.

Mandatory remediation protocol:

- repair owned-output defects and rerun the first failed checker;
- rerun the applicable bundle after direct PASS;
- stop if remediation requires a forbidden path or boundary change;
- do not ask the operator to choose routine formatting repairs.

## Source-Fidelity Pass

### Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| SOT3-T0 is independent full-corpus review | VALUE_SET | `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md` | Tranche Plan | `SOT3-T0` | SOT3 roadmap | ACCEPT |
| external packet requires all three roots | VALUE_SET | `docs/reviews/CVF_SOT3_T0_EXTERNAL_REVIEW_PACKET_2026-07-12.md` | Target / Source | `SOT3-T0-ERP` | external review packet | ACCEPT |
| Refinery doctrine separates preparation from truth and Flow | LITERAL_INVARIANT | `.private_reference/legacy/CVF_SOT 10.07/CVF_Refinery_Patch/README.md` | line 812 | `Refinery prepares information` | Refinery root README | ACCEPT |
| Refinery default engine stages may be empty | RUNTIME_BEHAVIOR | `.private_reference/legacy/CVF_SOT 10.07/CVF_Refinery_Patch/EXTENSIONS/CVF_REFINERY/src/pipeline/refinery-engine.ts` | line 58 | `run` | `RefineryEngine` | ACCEPT |
| Flow describes itself as built on Kernel | LITERAL_INVARIANT | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch/README.md` | line 5 | `built on top of` | Flow root README | ACCEPT |
| Flow also places sources into Flow before Kernel | LITERAL_INVARIANT | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch/EXTENSIONS/CVF_TRUTH_FLOW/README.md` | lines 17-23 | `Sources / human input / external signals` | Flow package README | ACCEPT |
| Flow defines an incompatible embedded packet | VALUE_SET | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch/EXTENSIONS/CVF_TRUTH_FLOW/src/refinery/refinery-engine.ts` | lines 9-14 | `RefineryPacket` | embedded Flow refinery engine | ACCEPT |
| Flow ready state can transition to VERIFIED | VALUE_SET | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch/EXTENSIONS/CVF_TRUTH_FLOW/src/lifecycle/lifecycle-engine.ts` | line 14 | `READY_FOR_VERIFICATION` | `allowed` transition map | ACCEPT |
| Flow publish gate accepts caller truth boolean | EXISTS | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch/EXTENSIONS/CVF_TRUTH_FLOW/src/routing/publish-gate.ts` | lines 3 and 9 | `truthKernelAccepted` | `evaluatePublishGate` | ACCEPT |
| Kernel receipt status derives from result-array searches | RUNTIME_BEHAVIOR | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch/EXTENSIONS/CVF_TRUTH_KERNEL/src/receipts/truth-receipt.ts` | lines 26-30 | `verification_results` | `createTruthReceipt` | ACCEPT |
| Kernel truth packet permits extra fields | VALUE_SET | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch/EXTENSIONS/CVF_TRUTH_KERNEL/schemas/truth.packet.schema.json` | line 6 | `additionalProperties` | truth packet JSON schema | ACCEPT |
| external output is advisory | LITERAL_INVARIANT | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE.md` | Absorption Instruction | `External output is advisory` | external review packet template | ACCEPT |
| no-commit worker route is canonical | VALUE_SET | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | WORKER_MUST_NOT_COMMIT rule | `WORKER_MUST_NOT_COMMIT` | Agent Handoff Contract | ACCEPT |

### Current Runtime Freshness Verification

This work order does not claim that all related runtime owners are absent. The
worker must search current CVF truth foundation, skill truth packets, evidence,
provenance, receipt, routing, lifecycle, and source-intake surfaces before
using `OWNER_SURFACE_NOT_FOUND`.

Required semantic searches include:

```powershell
rg -n --hidden --no-ignore "RefineryPacket|SourceEnvelope|TruthReceipt|TruthReference|DistributionPackage|FeedbackProposal" docs EXTENSIONS governance
rg -n --hidden --no-ignore "READY_FOR_KERNEL|READY_FOR_VERIFICATION|VERIFIED|PUBLISHED" docs EXTENSIONS governance
```

### Negative Search And Collision Discipline

| Check | Evidence requirement | Disposition |
|---|---|---|
| packet and type names | exact `rg` commands and roots in return | semantic collision expected; no absence claim by default |
| truth owner surfaces | current governed paths checked | owner candidate or source-not-found result with evidence |
| lifecycle tokens | retained and current CVF matches separated | same spelling does not prove same semantics |
| root README/TREEVIEW presence | direct file enumeration | missing Kernel root entry surface is a documentation fact only |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| 305-file accounting | Manifest and Ledger Contracts | manifest records and ledger path set | exact count and set equality | PASS |
| README/TREEVIEW first, then bodies | Execution Plan | processing order evidence | ledger and return methodology | PASS |
| independent dissent | External Review Return Shape | dissent and alternative architecture | reviewer inspection | PASS |
| three-layer verdict | External Review Return Shape | final layer map and verdict | citations from all roots | PASS |
| no-AI Refinery challenge | Review Questions | boundary decision | violation inventory | PASS |
| Flow ambiguity resolution | Review Questions | facade/post-Kernel recommendation | source-backed decision | PASS |
| packet mismatch matrix | External Review Return Shape | producer/consumer matrix | both source citations per row | PASS |
| capability dispositions | Processing Ledger and Return | absorb/adapt/defer/reject table | allowed vocabulary check | PASS |
| no direct import or implementation | Scope and Claim Boundary | changed-set evidence | git status and diff | PASS |
| advisory external output | Review Gate | pending CVF reviewer disposition | no closed or authority claim | PASS |

Rows confirm dispatch instruction coverage; they do not claim the planned
worker outputs already exist.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator-selected retained SOT three-layer corpus |
| Intake role | no-commit external-review worker |
| Provider surface | Claude requested by operator; role-neutral authority retained |
| Reviewer role | CVF reviewer/closer verifies and classifies returned observations |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; evidence and critique only |
| Public route | `DEFERRED_PRIVATE_ONLY` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | dispatcher -> external reviewer -> CVF reviewer/closer |
| escalation condition | snapshot drift, unreadable source, authority conflict, forbidden-path need, or scope expansion |

## Dual Agent Surface Matrix

| Surface class | Supported route | Interface | Authority and risk boundary | Required evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | supported for dispatcher and CVF reviewer roles | governed roadmap, packet, baseline, work order, and returned review | CVF roles own dispatch and acceptance; no provider-local authority | repo paths, gates, trace, and reviewer disposition | no hidden internal runtime adapter is claimed |
| EXTERNAL_AGENT_CLI_MCP | operator-selected local Claude review surface only | filesystem reads and three owned output paths | advisory evidence; no mutation outside owned outputs, no commit, no provider/live claim | source manifest, processing ledger, external return, unchanged HEAD | local workspace access only; no general CLI/MCP product support claim |

Disposition: CONTRACT_ONLY for the bounded external-review route. This matrix
does not claim general external-agent runtime integration.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; Roadmap-To-Work-Order Trace Matrix; Intake Role Routing Decision; Dual Agent Surface Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Corpus Completeness And Report Integrity; COMPLETE_PENDING_REVIEW; BLOCKED_WITH_REASON |
| gateRunPurpose | confirm exact dispatch and worker-output evidence shape after checker source review |
| claimBoundary | checker-shape evidence does not prove corpus completeness, review quality, or architecture correctness |

## Worker Output Checker Read-Ahead Mandate

Before writing each output, inspect checker source for that path and document
class. The manifest must be valid JSON. The two review artifacts must include
their required target/source, scope/methodology, findings/position,
risk/corrective-action, decision/disposition, corpus, trace, epistemic,
public-export, and claim-boundary sections before substantive drafting.

Do not use heading-shaped examples before the real sections.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> no-commit external-review worker -> CVF reviewer/closer |
| phase | dispatch authoring; external evidence execution from clean post-dispatch commit; reviewer conversion from accepted return |
| baseHeadFor(phase) | dispatchBaseHead=`615304819`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_MUST_CAPTURE_AT_CLOSURE` |
| changedSetScope(phase) | worker creates exactly the three Planned Worker Fulfillment Manifest paths |
| traceScope(phase, actor) | worker traces source reads, snapshot evidence, commands, outputs, actual changed set, and no-commit state; reviewer traces absorption classification and closure |
| commitOwner(phase) | worker=`WORKER_MUST_NOT_COMMIT`; reviewer/closer owns any accepted material commit |
| crossBatchIsolation | no cleanup, runtime, checker, session, handoff, registry, package, provider, or public path may enter the worker changed set |
| nextMoveSurfaces | worker must not edit continuity; reviewer decides roadmap/session updates only after accepting material evidence |

## Reviewer Closure Conversion

completionReviewPath: N/A with reason: the external review return will carry the
CVF reviewer disposition unless evidence complexity requires a separately
authorized completion artifact.

reviewerOwnedClosurePaths:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_T0_EXTERNAL_THREE_LAYER_SCAN_2026-07-12.md`
- `docs/reviews/CVF_SOT3_T0_EXTERNAL_REVIEW_RETURN_2026-07-12.md`
- `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md`
- `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md`

pendingStatusTokensAllowedBeforeReview: COMPLETE_PENDING_REVIEW,
COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW, DRAFT, HOLD_*

forbiddenClosedEquivalentResidue: pending worker status, not-executed residue,
pre-closure-not-run residue, or dispatch status as final state

predecessorClosureFactSource: external review return plus reviewer-accepted
material commit, not mutable session mode alone

## Planned Worker Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/evidence/sot/sot3-t0-source-manifest.json` | create deterministic three-root source manifest |
| `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md` | create exactly one body-read row per manifest record |
| `docs/reviews/CVF_SOT3_T0_EXTERNAL_REVIEW_RETURN_2026-07-12.md` | create source-backed independent critique and pending-review return |

Forbidden paths: every path not listed above.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | bounded evidence JSON plus two dated review artifacts; no new stable reference or runtime owner |
| Storage decision | source manifest belongs in the SOT evidence family; ledger and advisory return belong in the review family |
| Existing aggregate impact | none; no current generated aggregate is edited |
| Generated state impact | none during worker execution |
| Durable governance boundary | outputs are tranche evidence only and cannot become a hidden SOT, registry, runtime store, or canonical contract |

## Pre-Existing Dirty Path Exemptions

| Path | Status at dispatch authoring | Exemption boundary |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | M | pre-existing operator change; do not edit, stage, revert, or claim |

Dispatch remains on HOLD until a clean post-dispatch commit can isolate this
work from the exempt path.

## Manifest Contract

Top-level JSON fields:

- `schemaVersion`: `0.1.0`;
- `batchId`: `SOT3-T0`;
- `snapshotDate`: `2026-07-12`;
- `roots`: one object per root with root ID, literal path, count, bytes, and
  aggregate digest;
- `fileCount`: 305;
- `totalBytes`: 316848;
- `records`.

Each record contains:

- `rootId`;
- `sourceRelativePath` using `/` separators;
- `sha256` as lowercase 64-hex;
- `bytes` as a non-negative integer;
- `extension`;
- `artifactFamily`;
- `capabilityFamily`.

Sort by `rootId`, then `sourceRelativePath`. Duplicate root/path pairs are
forbidden.

## Processing Ledger Contract

The ledger contains exactly one row per manifest record:

| Column | Required meaning |
|---|---|
| rootId | REFINERY, KERNEL, or FLOW |
| sourceRelativePath | exact manifest key |
| sha256 | exact file digest |
| bodyReadStatus | READ or BLOCKED_UNREADABLE |
| artifactFamily | docs, schema, source, test, guard, adapter, script, rule, template, example, or metadata |
| capabilityFamily | specific layer capability |
| sourceFactsExtracted | concrete body facts, not filename inference |
| crossLayerContract | related producer/consumer contract or N/A with reason |
| existingOwnerCandidates | current CVF paths checked or OWNER_DECISION_NEEDED |
| overlapCandidate | CONFIRMED_EXISTING, ENRICH_EXISTING, NEW_FINDING, REJECT_DIRECT_IMPORT, NO_NEW_VALUE, or OWNER_SURFACE_NOT_FOUND |
| advisoryDisposition | ABSORB, ADAPT, DEFER, REJECT, BLOCK, or NO_NEW_VALUE |
| semanticAuditStatus | PENDING_CVF_REVIEWER |

The external worker must not convert semantic audit status to accepted or
closed.

## External Review Return Shape Contract

Required report sections by section name:

- Purpose
- Target / Source
- Scope / Methodology
- Source Inventory
- Corpus Manifest Reconciliation
- Findings / Position
- Layer-By-Layer Assessment
- Cross-Layer Contract Mismatch Matrix
- Dispatcher Dissent And Alternative Architecture
- Capability Absorption Matrix
- Overlap And Novelty Classification
- Risk / Corrective Action
- Decision / Disposition
- External Knowledge Intake Routing
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Checker Source Read-Ahead Block
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- Claim Boundary
- git status --short
- Changed Files
- No-Commit Statement

Worker status must be `COMPLETE_PENDING_REVIEW`,
`COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON`.

The return must state which dispatcher claims were confirmed, revised,
narrowed, split, or invalidated. It must propose the strongest alternative
architecture even when the three-layer verdict is retained.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The external review return is the worker return. It must be scaffolded before
long-form drafting and must record actual pending paths.

## System Loop Interlock Routing

| Field | Route |
|---|---|
| Upstream loop | retained three-root corpus and external review packet -> manifest, ledger, and external return |
| Downstream loop | CVF reviewer classifies atomic external observations through the external-finding absorption workflow |
| Machine-readable intake path | manifest JSON plus source processing ledger |
| Deferred finding routing | each deferred or blocked item records defectClass, learningLane, nextAction, and workOrderRef |
| Claim boundary | no external row autonomously mutates a CVF owner, roadmap, contract, source, or runtime |

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | retained legacy three-folder source family |
| Upstream or source-mirror disposition | `LEGACY_REFERENCE_ONLY_WITH_REASON`: operator-authored retained patch with no verified upstream identity |
| Enumeration or manifest plan | recursive direct enumeration including ignored files and per-file digests |
| Per-file terminal-ledger plan | exactly one processing row per manifest record |
| Owner or overlap route | worker proposes owner candidates; CVF reviewer decides |
| Value-disposition route | absorb, adapt, defer, reject, block, or no-new-value |
| Claim boundary | evidence and architecture critique only; no direct import or implementation |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | ignored retained legacy source roots |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | exact three-root manifests and per-file body-read ledger |
| Blind-spot prevention action | path equality, digests, body-read status, and reviewer-pending semantic state |
| Residual gap | final value and owner decisions remain with CVF reviewer |
| Blind-spot verdict | PARTIAL_PENDING_WORKER_EXECUTION |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | the three retained roots in Source Verification Block |
| Enumeration command | direct recursive filesystem enumeration per literal root |
| Manifest artifact or inline manifest | planned `docs/evidence/sot/sot3-t0-source-manifest.json` |
| Processing ledger artifact or inline ledger | planned `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline Overlap And Novelty Classification table in this work order; CVF reviewer owns acceptance |
| Unresolved items | 305 before worker execution |
| Completion claim boundary | worker evidence can prove accounting and advisory analysis only, not absorption or readiness |

## Corpus Completeness And Report Integrity

- Corpus task class: retained SOT three-layer external architecture review.
- Corpus root: three literal roots in Source Verification Block.
- Snapshot time: 2026-07-12 dispatch authoring.
- Enumeration command: direct recursive filesystem enumeration per literal root.
- Manifest artifact or inline manifest: planned SOT3-T0 JSON manifest.
- Manifest hash: three root-specific digests in Pre-Flight Checks.
- Processing ledger artifact or inline ledger: planned SOT3-T0 external processing ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=305; ledger_terminal=0 at dispatch; exclusions=0; unresolved=305
- Unresolved files: 305.
- Declared exclusions: none.
- Unreadable or unsupported files: none known at dispatch.
- Aggregation check: 305 files and 316848 bytes.
- Drift check: reproduce every root count, byte total, and digest before body reads.
- Output traceability: root ID, relative path, digest, size, body-read status, and advisory classification.
- Adversarial verification: README/TREEVIEW, tests, and supplied findings cannot substitute for complete source-body evidence.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| three-layer doctrine | preparation, trust evaluation, and distribution separation | DOCTRINE_ADAPTED | SOT3-T2 candidate | external critique and CVF review first | no implementation |
| Refinery primitives | source-bound deterministic preparation | PACKAGE_CANDIDATE | SOT3-T3 candidate | classify and challenge algorithms | no direct import |
| Kernel primitives | evidence, obligation, provenance, verification, receipt | RUNTIME_CANDIDATE | SOT3-T4 candidate | compare against existing owners | no current runtime change |
| Flow primitives | routing, dose, distribution, lifecycle, feedback | RUNTIME_CANDIDATE | SOT3-T5 candidate | remove duplicated upstream ownership | no current runtime change |
| prototype guards and negative cases | enforcement use cases | CHECKER_CANDIDATE | future owner decision | record only | no checker wiring |
| incompatible duplicate contracts | integration risk evidence | REJECT_DIRECT_IMPORT | SOT3-T2 negative contract evidence | source-cite and preserve | no package activation |
| duplicate or non-reusable historical material | context only | NO_PACKAGE_OR_RUNTIME_VALUE | retained provenance | require body-read reason | no runtime or package action |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| truth doctrine | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | ENRICH_EXISTING | retained source is broader than bounded current doctrine | report delta only |
| skill truth packets | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | ENRICH_EXISTING | vertical slice cannot be assumed to own general stack | preserve compatibility question |
| independent Refinery | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | owner decision requires full review | do not create owner |
| post-Kernel Flow | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | owner decision requires full review | do not create owner |
| retained prototype source | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` | REJECT_DIRECT_IMPORT | packet and trust boundaries differ | recommend CVF-native rewrite only |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | retained corpus -> external review packet -> advisory return -> CVF atomic finding classification -> later governed decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` applies to the later CVF absorption review |
| Owner surface | this work order for execution; CVF reviewer for acceptance |
| Disposition | ADAPT external critique only after source verification |
| Claim boundary | no external output directly changes CVF authority or implementation |

## Verification Commands

Run the smallest matching checks first, then the worker-return gate:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_absorption_blindspot_control_presence.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_core.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_value_conversion.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_overlap_discipline.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_knowledge_intake_routing.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_corpus_completeness_report_integrity.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
git rev-parse --short HEAD
```

Expected final HEAD equals `executionBaseHead`.

## Write Ownership

Worker-owned paths:

- `docs/evidence/sot/sot3-t0-source-manifest.json`
- `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md`
- `docs/reviews/CVF_SOT3_T0_EXTERNAL_REVIEW_RETURN_2026-07-12.md`

Write mode: create-only, then modify-listed for allowed gate remediation.

Every other path is forbidden. The worker must not stage or commit.

## Execution Plan

1. Capture startup acknowledgment, `executionBaseHead`, and actual status.
2. Reproduce root counts, bytes, and digests; stop on drift.
3. Create the deterministic 305-record manifest.
4. Read each root independently in the required entry-to-body order.
5. Populate exactly one processing-ledger row per manifest record.
6. Reconcile README/TREEVIEW/architecture claims against source and tests.
7. Compare cross-layer schemas, types, statuses, cardinalities, receipts,
   lifecycle transitions, and adapters.
8. Search current CVF owner candidates before proposing novelty.
9. Author the external return with dissent, alternative architecture, layer
   verdict, mismatch matrix, capability dispositions, and claim limits.
10. Run all matching gates, repair owned-output defects, record actual pending
    status, and return without commit.

## Evidence Requirements

- exact count, bytes, root digest, and per-file SHA-256;
- one manifest record and one ledger row per source file;
- body facts for every readable row;
- source citations for every major architecture claim;
- producer and consumer evidence for every contract mismatch;
- current CVF owner path checked for every novelty claim;
- explicit dispatcher dissent and strongest alternative design;
- isolated build/test commands and results when run;
- actual changed-set and unchanged HEAD evidence;
- no direct import, implementation, provider/live, public, or readiness claim.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the three-layer idea is valuable, but prototype
boundaries and contracts require selective rewrite.

Evidence Comparison Requirement: the worker must compare full-corpus evidence
against that prediction and explicitly identify disconfirming evidence.

Contradiction Handling Requirement: contradictory evidence receives a
Contradiction Or Gap Disposition and updates the affected claim.

Claim Update Requirement: the worker marks the dispatcher verdict confirmed,
revised, narrowed, split, or invalidated.

## Review Gate

The CVF reviewer must:

- reproduce manifest arithmetic and sample file hashes;
- verify every `BLOCKED_UNREADABLE`, `DEFER`, `REJECT`, and `NO_NEW_VALUE` group;
- inspect high-risk packet, receipt, transition, and adapter findings;
- split the external return into atomic observations;
- classify returned observations through the external-finding absorption
  workflow before changing any CVF artifact;
- reject filename-only, README-only, or agreement-only review;
- retain pending status until accepted material is committed and closure gates
  pass on a non-empty range.

## Closure Checklist

- [ ] exactly three worker-owned outputs;
- [ ] 305 unique manifest records;
- [ ] 305 matching processing-ledger rows;
- [ ] zero undeclared exclusions;
- [ ] every readable row contains body facts;
- [ ] every major conclusion cites all relevant layers;
- [ ] mismatch matrix cites producer and consumer sources;
- [ ] dissent and alternative architecture are present;
- [ ] advisory dispositions use allowed vocabulary;
- [ ] semantic audit status remains pending CVF reviewer;
- [ ] actual status lists all pending worker files;
- [ ] worker HEAD is unchanged;
- [ ] required gates are recorded;
- [ ] no forbidden path or claim expansion.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for source drift, unreadable critical architecture
surfaces, authority conflict, forbidden-path need, or required scope expansion.
Return `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW` only when all paths are
accounted but visible limitations remain. Return `COMPLETE_PENDING_REVIEW` only
after full accounting and required gates.

## Operator Checkpoint

No operator checkpoint is needed for routine execution. Operator input is
required for scope expansion, raw private exposure outside the three roots,
implementation selection, provider/live proof, secrets/quota, public-sync,
destructive action, or a new semantic authority decision.

## Acceptance Criteria

| ID | Criterion | Required evidence |
|---|---|---|
| AC-01 | all three source snapshots reproduce | command results and root manifest metadata |
| AC-02 | manifest contains 305 unique records | JSON validation and duplicate check |
| AC-03 | ledger path set equals manifest path set | reconciliation command |
| AC-04 | every readable file has body facts | ledger inspection |
| AC-05 | each layer receives a separate assessment | cited return sections |
| AC-06 | cross-layer mismatches cite both sides | mismatch matrix review |
| AC-07 | no-AI Refinery boundary is challenged file by file | violation and support inventory |
| AC-08 | Flow topology ambiguity receives a recommendation | source-backed architecture decision |
| AC-09 | capability groups receive advisory disposition and owner candidates | conversion and overlap matrices |
| AC-10 | external return contains material dissent | dissent section and alternative design |
| AC-11 | worker touches only three owned outputs | actual git status and diff |
| AC-12 | worker does not commit | HEAD equality |

## Fail Conditions

| Fail condition | Required action |
|---|---|
| snapshot mismatch | return blocked; do not update dispatch values |
| missing manifest or ledger record | repair before return |
| unreadable file hidden from accounting | return limitation or blocked status |
| README/TREEVIEW substituted for body scan | return incomplete |
| owner novelty asserted without current search | revise to owner decision needed |
| direct import or implementation recommended as authorized action | remove authority claim and keep advisory recommendation only |
| external output treated as CVF truth | reviewer rejects return |
| forbidden path changed or worker commit created | stop and return blocked |
| gate remediation requires forbidden scope | return blocked with exact command and issue |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | SOT3-T0 external-review dispatch authoring, 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | PowerShell, rg, Python governance helpers, apply_patch, git read-only commands |
| Target paths | SOT3 roadmap, external review packet, GC-018 baseline, and this work order |
| Allowed scope source | operator requested roadmap update, synthesis packet, and Claude scan work order |
| Before status evidence | dispatchBaseHead `615304819`; pre-existing operator modification to `CVF_SESSION_MEMORY.md` excluded |
| After status evidence | four SOT3 dispatch artifacts pending validation; no runtime or retained-source mutation |
| Diff evidence | `git status --short` and pending-path inspection |
| Approval boundary | dispatch authoring and external-review planning only |
| Claim boundary | no direct import, implementation, provider/live proof, public action, or readiness claim |
| Agent type | dispatcher |
| Invocation ID | `sot3-t0-external-review-dispatch-2026-07-12` |
| Expected manifest | SOT3 roadmap; review packet; GC-018 baseline; work order; pre-existing operator change excluded |
| Actual changed set | SOT3 roadmap; review packet; GC-018 baseline; work order; pre-existing operator change excluded |
| Manifest delta | MATCH_WITH_PREEXISTING_USER_CHANGE_EXCLUDED |
| Deletion or rename disposition | N/A with reason: replaced only untracked dispatcher drafts before dispatch; no governed committed artifact deleted or renamed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | SOT3-T0 external full-corpus architecture review dispatch only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - dispatch records source snapshots, required outputs, role, and return evidence |
| actionEvidence | ACTION_EVIDENCE_PRESENT - roadmap, packet, baseline, and work order are the dispatch-authoring actions |
| invocationBoundary | local governed documentation authoring and future read-only corpus evaluation |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or runtime interception behavior claimed |
| claimLanguage | bounded no-commit external architecture review |
| forbiddenExpansion | direct import, contract ratification, implementation, package activation, checker wiring, provider/live proof, public-sync, commit, release, and production readiness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the work order gives an authorized local external-review role access to
private retained source. It does not authorize publication.

## Claim Boundary

This work order authorizes exactly one no-commit external-review worker to read
the three retained roots and create the three listed outputs after clean
dispatch release. It does not authorize final absorption, CVF semantic
acceptance, owner creation, roadmap mutation, contract ratification, runtime or
checker work, package activation, provider/live proof, public-sync, commit,
push, release, or production readiness.

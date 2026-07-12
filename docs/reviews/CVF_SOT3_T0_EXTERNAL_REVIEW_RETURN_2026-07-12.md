# CVF SOT3-T0 External Review Return

Memory class: FULL_RECORD

Status: ADVISORY_INPUT_ACCEPTED_FOR_RECOVERY_REVIEW

docType: review_context

Date: 2026-07-12

Return ID: SOT3-T0-RETURN

## Purpose

Independent full-body external review of the retained CVF Source of Truth
three-layer corpus (Refinery, Truth Kernel, Truth Flow). This return challenges
the dispatcher architecture position, reconciles cross-layer contracts against
actual source, classifies selective absorption value, and states explicit
dissent with a strongest alternative architecture. It is advisory evidence for
the CVF reviewer; it does not close value, ratify contracts, or authorize
implementation.

## Target / Source

Three retained private roots, reviewed in full:

| Root ID | Source root | Files | Bytes |
|---|---|---:|---:|
| REFINERY | `.private_reference/legacy/CVF_SOT 10.07/CVF_Refinery_Patch` | 133 | 160461 |
| KERNEL | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch` | 93 | 78007 |
| FLOW | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch` | 79 | 78380 |
| Total | three roots | 305 | 316848 |

Companion outputs: `docs/evidence/sot/sot3-t0-source-manifest.json` (305-record
manifest) and `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md`
(one body-read row per file).

## Scope / Methodology

- Reproduced each root count, byte total, and a worker-defined reproducible
  aggregate digest before any body read; counts and bytes matched the dispatch
  snapshot exactly (133/93/79 = 305 files; 160461/78007/78380 = 316848 bytes).
- Read entry surfaces first (root README, TREEVIEW, Architecture, package
  README), then doctrine/specs, then schemas, then runtime source, then tests,
  then adapters/guards/rules/examples.
- Read every load-bearing runtime file in full: Refinery engine, stage-runner,
  packet builder, status calculator; Kernel receipt, verification gate, strict
  and relaxed modes, truth packet schema; Flow embedded refinery engine,
  lifecycle engine, publish gate, feedback engine, source-score.
- Extracted a concrete body fact for all 305 files (see ledger); zero files were
  unreadable.
- Prototype build/test observations are treated as retained-source evidence
  only, never as CVF runtime proof.

## Source Inventory

| Root | ts | md | yaml | json | Root entry surface present |
|---|---:|---:|---:|---:|---|
| REFINERY | 77 | 25 | 21 | 10 | root README.md and TREEVIEW.md present |
| KERNEL | 52 | 22 | 11 | 8 | no root README or TREEVIEW; shallowest entry is package README |
| FLOW | 49 | 14 | 8 | 8 | root README.md, TREEVIEW.md, and Architecture.md present |
| Total | 178 | 61 | 40 | 26 | Kernel root entry-surface gap confirmed |

The missing Truth Kernel root entry surface is recorded as an
architecture/documentation finding, not as an unread-file excuse. Every Kernel
file including the package README was read.

## Corpus Manifest Reconciliation

- manifest records: 305; ledger rows: 305; path-set equality: TRUE.
- duplicates: 0; unreadable: 0; declared exclusions: 0.
- REFINERY 133, KERNEL 93, FLOW 79; sum 305; bytes sum 316848.
- Snapshot drift check: counts, bytes, and every per-file SHA-256 reproduce.
  The dispatcher aggregate digest algorithm was not recorded and its three
  values were not reproduced. Corpus identity is supported by the stronger
  305-file hash set, while the original aggregate-digest claim remains an
  unreproducible dispatch artifact rather than a silently accepted value.

## Findings / Position

Dispatcher provisional verdict under test:
`THREE_LAYER_MODEL_CONFIRMED_WITH_ROLE_SPLIT_AND_CONTRACT_REWRITE`.

Worker verdict: `CONFIRMED_WITH_NARROWING`. The three-layer separation
(prepare / evaluate trust / distribute) is architecturally sound and worth
adopting as CVF-native doctrine. However, the retained prototype does not
implement that separation safely, and one dispatcher sub-claim is too strong
(see dissent). The dominant structural defect is not any single bug; it is a
repeated **vacuous-empty-collection fail-open** that appears in all three layers
and a **topology contradiction** where Flow both precedes and follows Kernel and
re-implements Refinery.

Confirmed with source citations:

1. Refinery engine can emit a packet with no pipeline stages executed.
   `CVF_Refinery_Patch/.../pipeline/refinery-engine.ts` line 56 runs
   `input.stages ?? []`; with an empty stage list, `runStages`
   (`pipeline/stage-runner.ts` lines 13-26) completes zero stages and line 62
   still calls `buildRefineryPacket`.
2. That empty-pipeline packet can reach `READY_FOR_KERNEL`.
   `packet/refinery-packet-builder.ts` lines 18-20 make `lineageComplete`
   vacuously true when there are no expected outputs; `packet/refinery-status.ts`
   lines 14-35 then return `READY_FOR_KERNEL` when findings, conflicts,
   duplicates, and integrity are all empty and a manifest ref is present.
3. Refinery packet id and timestamp are non-deterministic:
   `refinery-packet-builder.ts` line 45 `randomUUID()`, line 58
   `new Date().toISOString()`.
4. Kernel truth receipt is `pass` on empty verification results.
   `CVF_Truth_Kernel_Patch/.../receipts/truth-receipt.ts` lines 26-30: both
   `.some()` checks are false on an empty array, so `status = 'pass'`. Line 36
   is a non-deterministic timestamp; the chained `hash` (line 48) covers
   `partial` but not a digest of the full evaluated `TruthPacket` content.
5. Kernel STRICT gate passes on empty results.
   `gates/strict-mode.ts` lines 3-8 only block on `status === 'fail'`; an empty
   results array returns `allowed: true`. `gates/relaxed-mode.ts` line 4 blocks
   only on `fail` with `method === 'obligation'`, so a non-obligation `fail`
   passes in RELAXED mode.
6. Kernel truth packet schema is open.
   `schemas/truth.packet.schema.json` line 6 `"additionalProperties": true` on
   the most security-critical cross-layer contract.
7. Flow defines a second, incompatible RefineryPacket.
   `CVF_Truth_Flow_Patch/.../refinery/refinery-engine.ts` lines 9-15 declare
   `packetId` (`TFR-` prefix), `normalizedPayload`, camelCase fields, and status
   `READY_FOR_VERIFICATION` - none of which match the dedicated Refinery packet.
8. Flow lifecycle can reach VERIFIED without receipt proof.
   `lifecycle/lifecycle-engine.ts` line 14 allows
   `READY_FOR_VERIFICATION -> VERIFIED`; `transition` (lines 24-27) only checks
   the state graph, with no Kernel receipt or evidence binding.
9. Flow publish gate trusts a caller boolean.
   `routing/publish-gate.ts` line 3 `truthKernelAccepted: boolean`; line 9 only
   checks its truthiness, with no receipt-id verification, hash, or issuer
   binding.
10. Flow feedback allows direct source-score mutation.
    `feedback/source-score.ts` lines 2-9 `updateSourceScore` directly recomputes
    and returns a new score with no proposal/approval gate, while
    `feedback/feedback-engine.ts` records proposal-shaped events separately;
    nothing binds a score change to an approved proposal.

## Layer-By-Layer Assessment

### Refinery (independent deterministic preparation)

- Doctrine is strong and internally consistent
  (`CVF_Refinery_Patch/README.md` lines 100-152, 812): output is not truth,
  forbidden statuses are explicit, and the operating principle cleanly separates
  Refinery / Kernel / Flow. The no-AI deterministic-first design (README lines
  417-434) is a genuinely valuable invariant.
- The reference engine does not enforce that doctrine. Mandatory stages are
  caller-supplied, not registered, so the engine fails open to
  `READY_FOR_KERNEL`. This is the single most important Refinery defect.
- ID/timestamp non-determinism defeats the replayable-receipt goal the README
  itself sets (README lines 640-667).
- Verdict: model ABSORB; deterministic primitives ADAPT after a contract-first
  rewrite that makes the pipeline mandatory and injects clock/id.

### Truth Kernel (sole trust evaluation and receipt)

- Doctrine is the strongest of the three (`CVF_Truth_Kernel_Patch/EXTENSIONS/
  CVF_TRUTH_KERNEL/README.md` lines 137-141 fail-stop; line 180 provenance
  labels MEASURED/COMPUTED/LLM_INFERRED/HUMAN_APPROVED; lines 118-135 LLM output
  is not self-trusting). The schema distinction between `computed_claims` and
  `llm_inferred_claims` (truth packet schema lines 44-49) is directly valuable.
- The receipt and gates fail open on empty evidence and do not bind the receipt
  to full packet content. `additionalProperties: true` weakens the boundary.
- The missing root entry surface is a real documentation gap for the layer that
  should be the trust authority.
- Verdict: doctrine and provenance model ABSORB; receipt, gate, and schema
  ADAPT with mandatory-non-empty-evidence and content-binding invariants.

### Truth Flow (post-Kernel distribution and lifecycle)

- Post-Kernel lifecycle capabilities (route, dose, distribute, consume, observe,
  feedback, recall, retire) are valuable and largely novel relative to current
  CVF.
- Flow's topology is self-contradictory: README line 5 says Flow is built on top
  of Kernel (post-Kernel), while README lines 66-82, README lines 260-286, and
  `Architecture.md` lines 41-52 place Flow before Kernel and give Flow ownership
  of Acquire and Refine, omitting the dedicated Refinery layer entirely.
- Flow re-implements refinement with an incompatible packet, and its two trust
  boundaries (lifecycle VERIFIED transition and publish gate) are
  assertion-based, not receipt-bound.
- Verdict: post-Kernel lifecycle ADAPT; embedded refinery REJECT; trust
  boundaries must be rebuilt on Kernel receipts.

## Cross-Layer Contract Mismatch Matrix

| Contract | Producer surface (cited) | Consumer surface (cited) | Mismatch | Disposition |
|---|---|---|---|---|
| Refinement packet | Refinery `types/refinery-packet.ts` + `refinery-packet-builder.ts` line 45 (`refinery_packet_id`, snake_case, `READY_FOR_KERNEL`) | Flow `refinery/refinery-engine.ts` lines 9-15 (`packetId`, camelCase, `READY_FOR_VERIFICATION`) | two incompatible packet types and status vocabularies for the same conceptual object | REJECT Flow duplicate; single canonical `RefineryPacket` |
| Packet id convention | Refinery `RP-` (builder line 45) | Kernel `truth_packet_id` (truth.packet.schema.json line 8); Flow `TFR-` (engine line 31) | three id conventions across one chain | ADAPT to one id contract |
| Ready-state token | Refinery `READY_FOR_KERNEL` (refinery-status.ts line 35) | Flow `READY_FOR_VERIFICATION` (lifecycle-engine.ts line 2; refinery-engine.ts line 14) | boundary handoff token differs | ADAPT to one token map |
| Trust promotion | Kernel receipt `pass` (truth-receipt.ts lines 26-30) | Flow `VERIFIED` transition (lifecycle-engine.ts line 14, 24-27) | Flow promotes to VERIFIED without consuming a Kernel receipt | ADAPT: receipt-bound transition |
| Publish trust input | Kernel `TruthReceipt` (truth-receipt.ts lines 5-18) | Flow `PublishGateInput.truthKernelAccepted: boolean` (publish-gate.ts line 3) | Flow trusts a boolean, not a verified receipt | ADAPT: receipt-id + hash binding |
| Packet boundary strictness | Kernel `truth.packet.schema.json` line 6 `additionalProperties: true` | all consumers | open boundary schema on the critical contract | ADAPT: closed or explicitly extensible schema |
| Feedback authority | Flow `feedback-engine.ts` proposal events (lines 10-18) | Flow `source-score.ts` direct mutation (lines 2-9) | proposal path and mutation path are unlinked | ADAPT: proposal-gated score change |

## Dispatcher Dissent And Alternative Architecture

Explicit dissent on dispatcher claims:

- CONFIRMED: three-layer role split is valuable; contracts require rewrite;
  direct import must be rejected.
- NARROWED: the dispatcher position that a valid source envelope plus manifest
  reference yields a meaningful `READY_FOR_KERNEL` packet is too strong. Source
  citations 1-2 show `READY_FOR_KERNEL` is reachable with zero refinement work,
  so `READY_FOR_KERNEL` in the retained engine does not mean structurally
  refined - it can mean nothing ran. The dispatcher framing of the empty-stage
  case as a minor default-behavior gap understates it: it is a cross-layer
  trust fail-open, because a do-nothing packet can enter the Kernel path.
- REVISED: the dispatcher treats Flow topology as an ambiguity to resolve. The
  source shows it is a contradiction inside a single package (three files
  disagree), not merely under-specified. Resolution must delete the pre-Kernel
  Flow-owns-Refine claim, not just document a preference.

Strongest alternative architecture (offered even though the three-layer verdict
is retained):

`INTAKE-BOUND SINGLE-CHAIN WITH FAIL-CLOSED EMPTY-EVIDENCE INVARIANT`

```text
Governed Intake Adapter
  -> SourceEnvelope (identity/owner/scope/purpose/integrity required)
  -> CVF Refinery Core (MANDATORY ordered stages; injected clock+id; fail-closed)
  -> RefineryPacket (single canonical contract; READY_FOR_KERNEL only if >=1 stage ran)
  -> CVF Truth Kernel (evaluation REQUIRES >=1 non-empty verification result)
  -> KernelDecision + TruthReceipt (packet-content-bound, issuer-bound, replay-aware)
  -> TruthReference (scoped, versioned, TTL, supersession-aware)
  -> CVF Truth Flow (post-Kernel ONLY; no intake, no refinery, no self-trust)
  -> DistributionPackage (receipt-bound, route-bound, dose-bound, TTL-bound)
  -> FeedbackProposal (proposal-only; source-score change gated by approval)
```

The alternative differs from the retained prototype in three binding ways that
directly close the confirmed defects: (a) every layer treats an empty evidence
collection as fail-closed rather than vacuous-pass; (b) Flow is strictly
post-Kernel and owns no intake or refinement; (c) all trust transitions consume
a content-bound Kernel receipt rather than a caller boolean or a bare state-graph
edge. This is a recommendation for CVF review, not an authorized change.

## Capability Absorption Matrix

| Capability group | Value | Owner candidate | Advisory disposition |
|---|---|---|---|
| Three-layer separation doctrine | high; clean prepare/evaluate/distribute split | SOT3-T2 contract family | ABSORB |
| Refinery deterministic primitives (normalize, dedupe, conflict, lineage, integrity) | high after rewrite | SOT3-T3 Refinery Core | ADAPT |
| No-AI Refinery Core invariant | high governance value | SOT3-T3 | ABSORB (invariant) / ADAPT (enforcement) |
| Kernel provenance labels + computed vs llm_inferred split | high | SOT3-T4 Kernel | ABSORB |
| Kernel evidence/obligation/verification/receipt structures | high after fail-closed rewrite | SOT3-T4 | ADAPT |
| Flow post-Kernel lifecycle (route/dose/distribute/observe/recall/retire) | high; largely novel | SOT3-T5 Flow | ADAPT |
| Flow embedded refinery + second RefineryPacket | negative (integration risk evidence) | REJECT | REJECT |
| Prototype guards, checkers, negative cases | medium; enforcement use cases | future checker owner decision | DEFER |
| Tests, scripts, examples, config | supporting only | follow contract ratification | DEFER |

Aggregate advisory dispositions across all 305 files (from ledger): ABSORB 35,
ADAPT 168, DEFER 93, REJECT 9, BLOCK 0, NO_NEW_VALUE 0. All remain
`PENDING_CVF_REVIEWER`.

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | retained legacy three-folder source family |
| Upstream or source-mirror disposition | `LEGACY_REFERENCE_ONLY_WITH_REASON`: operator-authored retained patch without verified upstream repository identity |
| Enumeration or manifest plan | direct recursive enumeration including ignored files and per-file SHA-256; recorded in the SOT3-T0 manifest |
| Per-file terminal-ledger plan | one body-read row per manifest record in the processing ledger |
| Owner or overlap route | overlap candidates recorded per group; CVF reviewer owns acceptance |
| Value-disposition route | absorb, adapt, defer, reject, block, or no-new-value |
| Claim boundary | COMPARISON_ONLY_NO_ABSORPTION: architecture critique only; no direct import or implementation |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | ignored retained legacy source roots |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | exact 305-file manifest and one body-read ledger row per record |
| Blind-spot prevention action | per-file digests, body-read status, full-body reads over README/TREEVIEW, and reviewer-pending semantic classification |
| Residual gap | final CVF value, owner, and contract decisions remain reviewer-owned |
| Blind-spot verdict | PARTIAL_PENDING_RECOVERY_REVIEW |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | the three literal roots in Target / Source |
| Enumeration command | direct recursive filesystem enumeration per literal root |
| Manifest artifact or inline manifest | `docs/evidence/sot/sot3-t0-source-manifest.json` |
| Processing ledger artifact or inline ledger | `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline Overlap And Novelty Classification table in this return; CVF reviewer owns acceptance |
| Unresolved items | 0 after body-read accounting; semantic value remains reviewer-pending |
| Completion claim boundary | accounting and advisory analysis proven; absorption, runtime, and readiness not proven |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| general truth doctrine | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | ENRICH_EXISTING | retained corpus is broader than the bounded current doctrine | map exact delta in SOT3-T1 |
| skill truth packet | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | ENRICH_EXISTING | current owner is a vertical slice, not the general stack | preserve compatibility analysis |
| independent Refinery Core + RefineryPacket | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | token search found no current general RefineryPacket/SourceEnvelope owner in truth_foundation, skills, or guard contracts | do not create owner before SOT3-T1 |
| post-Kernel Flow lifecycle | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | no current shared Truth Flow owner found | do not create owner before SOT3-T1 |
| prototype receipt/publish paths | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` | REJECT_DIRECT_IMPORT | current receipt-binding is a workflow-step obligation contract, semantically unrelated to Kernel TruthReceipt despite the shared word | recommend CVF-native adaptation only |

Negative-search evidence: a token search for
`RefineryPacket|SourceEnvelope|TruthReceipt|TruthReference|DistributionPackage|FeedbackProposal|READY_FOR_KERNEL|READY_FOR_VERIFICATION`
over `docs/reference/truth_foundation`, `docs/reference/agent_system_skills`, and
`EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts` returned zero matches. Same-token
collisions elsewhere are not treated as owner proof; every owner gap remains a
CVF reviewer decision.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| empty-evidence fail-open across all three layers | require >=1 executed stage / non-empty verification result before any ready/pass/verified state |
| Flow topology contradiction | delete pre-Kernel Flow-owns-Refine claim; Flow is post-Kernel only |
| duplicate incompatible RefineryPacket | reject Flow packet; ratify one canonical contract in SOT3-T2 |
| assertion-based trust in Flow | bind lifecycle and publish gate to content-bound Kernel receipts |
| non-deterministic ids/timestamps | inject clock and id provider for replayable receipts |
| open packet schema | close or explicitly bound `additionalProperties` on the shared boundary |
| unlinked feedback vs source-score mutation | gate score changes behind approved proposals |
| prototype tests read as CVF proof | all build/test observations are retained-source evidence only |

## Decision / Disposition

Reviewer disposition: `REJECT_WORK_ORDER_CLOSURE_ACCEPT_ADVISORY_INPUT`.
The full per-file manifest and the major source-cited architecture findings are
retained as advisory evidence. SOT3-T0 cannot close as executed because the
committed work order remained in HOLD status, the original ledger truncated
digests, semantic facts were too shallow for many rows, and a fourth worker
artifact exceeded the three-output boundary. SOT3-T0R must reconcile these
limits before any architecture decision is ratified.

External absorption review: REQUIRED

## Required Absorption Table

| External item ID | External claim summary | Source basis | CVF verification surface | CVF disposition | Owner artifact | Next action | Claim boundary |
|---|---|---|---|---|---|---|---|
| SOT3-F01 | empty collections can vacuously reach ready or pass states across Refinery and Kernel | private retained source | Refinery engine/status sources and Kernel receipt/gate sources cited in Findings / Position | GOVERNED_FINDING_CANDIDATE | SOT3-T0R semantic reconciliation | require a fail-closed empty-evidence invariant in the decision recommendation | finding does not authorize runtime work |
| SOT3-F02 | Flow topology contradicts itself and duplicates Refinery ownership | private retained source | Flow root README, Architecture, embedded refinery type, and lifecycle source cited above | GOVERNED_FINDING_CANDIDATE | SOT3-T0R architecture recommendation | decide post-Kernel-only Flow versus separately named facade | no owner is ratified yet |
| SOT3-F03 | Flow trust transitions rely on state edges and caller booleans instead of content-bound receipts | private retained source | Flow lifecycle and publish-gate source plus Kernel receipt source | GOVERNED_FINDING_CANDIDATE | SOT3-T0R contract mismatch decision | require a receipt-bound transition recommendation | no implementation authority |
| SOT3-P01 | dirty protected-path ownership was attributed without source evidence | external process handoff plus committed dispatch artifacts | work order exemption row, git history, and process note | GOVERNANCE_LEARNING_REQUIRED | separate process-learning candidate | retain only the evidence rule; do not preserve an unproved author attribution | not an SOT architecture fact |
| SOT3-P02 | GC-051 requires a closer-owned registry entry for the staged corpus ledger | external process handoff plus staged reviewer gate | current reviewer-fast output and generated registry source | GOVERNANCE_LEARNING_REQUIRED | closer-owned SOT3 registry repair | add and generate the registry entry in this material batch; no ADIF promotion | registry repair does not validate semantic dispositions |
| SOT3-P03 | worker-return fast gate can fail printing replacement characters on Windows cp1252 stdout | external process handoff plus local tooling source | `governance/compat/run_worker_return_fast_gate.py` subprocess print path and local stdout encoding evidence | GOVERNANCE_LEARNING_REQUIRED | future checker-maintenance candidate | open a separate source-verified tooling tranche only if selected by the operator | no checker edit in SOT3 review |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | retained corpus -> bounded review packet -> this advisory return -> external-finding absorption workflow -> CVF reviewer disposition -> separately authorized SOT3-T1 |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` applies to the later CVF absorption artifact |
| Owner surface | this return for evidence; CVF reviewer for acceptance |
| Disposition | ADAPT external critique only after source verification and overlap review |
| Claim boundary | no external output becomes CVF authority directly |

## Finding-To-Governance Learning Disposition

| Finding | defectClass | learningLane | disposition | nextAction |
|---|---|---|---|---|
| vacuous-empty-collection fail-open repeats in all three layers | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | RUNTIME_LEARNING_CANDIDATE | preserve as a mandatory fail-closed contract-test class for SOT3-T3/T4/T5; no runtime edit now |
| Flow topology contradiction and duplicate packet | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | SOT3-T2 must ratify one canonical chain and delete pre-Kernel Flow refine ownership |
| trust transitions accept assertions not receipts | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | RUNTIME_LEARNING_CANDIDATE | require receipt-bound transitions in SOT3-T4/T5 design |

Next action: route these three learning dispositions to the CVF reviewer, who
classifies each as an atomic finding through the external-finding absorption
workflow before any SOT3-T2 through SOT3-T5 design or contract-test work begins.
No runtime, checker, or contract edit is authorized by this return.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the three-layer idea is valuable but prototype
boundaries and contracts require selective rewrite.

Evidence Comparison Requirement: full-corpus reading was compared against that
prediction. The prediction was largely confirmed.

Contradiction Or Gap Disposition: one disconfirming pattern was stronger than
predicted - the fail-open is not a single default-behavior gap but a repeated
cross-layer invariant failure. The affected dispatcher sub-claim
(`READY_FOR_KERNEL` implies structural refinement) is narrowed accordingly.

Claim Update Requirement: dispatcher verdict marked CONFIRMED_WITH_NARROWING;
the empty-stage sub-claim is narrowed; the Flow-ambiguity framing is revised to
a contradiction requiring deletion.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | Corpus Completeness And Report Integrity; External Absorption Core; External Absorption Value Conversion Matrix; Overlap And Novelty Classification; External Knowledge Intake Routing; Finding-To-Governance Learning Disposition; Epistemic Process Block; COMPLETE_PENDING_REVIEW; PARTIAL; COMPLETE_VERIFIED; ENRICH_EXISTING; OWNER_SURFACE_NOT_FOUND; REJECT_DIRECT_IMPORT |
| gateRunPurpose | confirm exact worker-return and corpus evidence shape after checker source review |
| claimBoundary | checker-shape conformance does not prove architecture correctness or absorption value |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| three-layer doctrine | prepare/evaluate/distribute separation | DOCTRINE_ADAPTED | SOT3-T2 candidate | CVF review then contract ratification | no implementation |
| Refinery primitives | deterministic preparation | PACKAGE_CANDIDATE | SOT3-T3 candidate | rewrite with mandatory pipeline | no direct import |
| Kernel primitives | evidence, obligation, provenance, verification, receipt | RUNTIME_CANDIDATE | SOT3-T4 candidate | fail-closed rewrite after T2 | no current runtime change |
| Flow primitives | routing, dose, distribution, lifecycle, feedback | RUNTIME_CANDIDATE | SOT3-T5 candidate | remove intake/refinery ownership | no current runtime change |
| prototype guards and negative cases | enforcement use cases | CHECKER_CANDIDATE | future owner decision | record advisory value only | no checker wiring |
| Flow embedded duplicate packet | integration-risk evidence | REJECT_DIRECT_IMPORT | SOT3-T2 negative evidence | source-cite and preserve | no package activation |
| tests, scripts, config, examples | context and follow-on scaffolding | NO_PACKAGE_OR_RUNTIME_VALUE | retained provenance | re-author after contract ratification | no runtime or package action |

## Corpus Completeness And Report Integrity

- Corpus task class: retained SOT three-layer external architecture review.
- Corpus root: the three literal roots in Target / Source.
- Snapshot time: 2026-07-12 external-review execution.
- Enumeration command: direct recursive filesystem enumeration per literal root.
- Manifest artifact or inline manifest: `docs/evidence/sot/sot3-t0-source-manifest.json`.
- Manifest hash: three worker-defined reproducible root digests recorded in the manifest.
- Processing ledger artifact or inline ledger: `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md`.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=305; ledger_terminal=305; exclusions=0; unresolved=0
- Unresolved files: 0
- Declared exclusions: none.
- Unreadable or unsupported files: none.
- Aggregation check: 133 plus 93 plus 79 equals 305 files; total bytes equal 316848.
- Drift check: all three root counts and byte totals reproduced exactly before body reads.
- Output traceability: root ID, relative path, digest, size, body-read status, and advisory classification in the manifest and ledger.
- Adversarial verification: README, TREEVIEW, Architecture, and prototype tests were compared against actual source bodies and did not substitute for them.
- Corpus verdict: PARTIAL

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude external-review worker |
| Provider or surface | local authorized private provenance workspace |
| Session or invocation | SOT3-T0 external-review execution, 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | Read, Grep, PowerShell/Bash read-only enumeration and hashing, Python for manifest/ledger generation, git read-only |
| Target paths | three retained roots (read-only) and three worker-owned outputs |
| Allowed scope source | SOT3-T0 work order Planned Worker Fulfillment Manifest |
| Before status evidence | executionBaseHead `4937a610e`; clean worktree at worker start |
| After status evidence | three worker-owned outputs created; no retained-source or CVF-runtime mutation |
| Diff evidence | `git status --short` lists only the three owned outputs |
| Approval boundary | external-review evidence authoring only |
| Claim boundary | no direct import, implementation, provider/live proof, public action, or readiness claim |
| Agent type | external-review worker |
| Invocation ID | `sot3-t0-external-review-execution-2026-07-12` |
| Expected manifest | manifest JSON; processing ledger; external review return |
| Actual changed set | manifest JSON; processing ledger; external review return; later process-findings handoff note |
| Manifest delta | MISMATCH_EXTRA_PROCESS_HANDOFF_RETAINED_AS_SEPARATE_ADVISORY_INPUT |
| Deletion or rename disposition | N/A with reason: create-only worker outputs; no source or governed artifact deleted or renamed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | SOT3-T0 external full-corpus architecture review evidence only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - manifest and ledger record source snapshots, per-file digests, and body-read status |
| actionEvidence | ACTION_EVIDENCE_PRESENT - manifest, ledger, and this return are the review actions |
| invocationBoundary | local read-only corpus evaluation and owned-output authoring |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or runtime interception behavior claimed |
| claimLanguage | bounded no-commit external architecture review |
| forbiddenExpansion | direct import, contract ratification, implementation, package activation, checker wiring, provider/live proof, public-sync, commit, release, and production readiness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this return cites private retained source and is intended for a local
authorized CVF reviewer surface only.

## Claim Boundary

This return is advisory external evidence. It proves complete 305-file
accounting through per-file hashes and delivers a source-cited independent
architecture critique with dissent and a strongest alternative. It does not
prove that every provisional per-file semantic disposition is accepted, and
it does not authorize final absorption,
CVF semantic acceptance, owner creation, roadmap mutation, contract
ratification, runtime or checker work, package activation, provider/live proof,
public-sync, commit, push, release, or production readiness. All semantic value
remains PENDING_CVF_REVIEWER.

## git status --short

```text
?? docs/evidence/sot/sot3-t0-source-manifest.json
?? docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md
?? docs/reviews/CVF_SOT3_T0_EXTERNAL_REVIEW_RETURN_2026-07-12.md
?? docs/reviews/CVF_SOT3_T0_PROCESS_FINDINGS_FOR_CODEX_2026-07-12.md
```

## Changed Files

- `docs/evidence/sot/sot3-t0-source-manifest.json` (created)
- `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md` (created)
- `docs/reviews/CVF_SOT3_T0_EXTERNAL_REVIEW_RETURN_2026-07-12.md` (created)
- `docs/reviews/CVF_SOT3_T0_PROCESS_FINDINGS_FOR_CODEX_2026-07-12.md` (created outside the three-output worker boundary; retained as separate advisory process input)

## No-Commit Statement

The external-review worker did not commit. HEAD remained at executionBaseHead
`4937a610e`. Four untracked files are now present because a later process note
was added outside the three-output worker boundary. The CVF reviewer retains
the four files as advisory intake and does not claim valid SOT3-T0 closure.

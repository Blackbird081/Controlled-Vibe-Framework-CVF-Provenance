# CVF GC-018 Baseline - RSPB-AI-T6 Capability Projection To Learning Candidate Intake Seam

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: RSPB-AI-T6

Dispatch base head: `6a66a37e11faa59c54d6bcbca244f2714adbcddc`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Orchestrator/reviewer: current independent reviewer/orchestrator role

Worker target: external delegated worker role

Mixed-origin derived synthesis: REQUIRED

rawMemoryReleased=false

## Purpose

Authorize one bounded local-first implementation tranche that binds the
accepted T5 projection to the existing Learning Plane intake bridge as a
deterministic, provenance-bound, review-pending learning candidate. The seam
must reject self-promotion and must not write policy, truth, memory, storage,
or runtime state.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RSPB-AI-T6 --title "Capability Projection To Learning Candidate Intake Seam" --date 2026-08-16 --base 6a66a37e1 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit external-worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | selected eight local files, reconciled current owners, fixed four-path worker manifest, and added hermetic fail-closed acceptance criteria |
| checkerReadAheadConfirmation | dispatch, source-verification, mixed-origin, overlap, value-conversion, dual-agent, trace, and worker-return checker sources read |
| docOnlyNewFields | projection-bound learning candidate, environment specificity, contradiction status, revalidation condition, independent-review requirement |
| claimBoundary | dispatch-authoring evidence only; no storage, policy, truth, memory, executor, provider/live, public, or production claim |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| literalTokensReviewed | Purpose; Source Verification Block; Mixed-Origin Derived Synthesis Provenance; Absorption Decision Vector; System-Chain Value Review; Dual Agent Surface Matrix; Public Export Disposition; Claim Boundary; ACCEPT; REJECT; CONTRACT_ONLY |
| gateRunPurpose | confirmation and dispatch evidence after bounded source inspection |
| claimBoundary | structural readiness does not prove worker implementation correctness |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-absorption-implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class external-absorption-implementation --role dispatcher --lifecycle-phase pre-dispatch --surface-selector EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION --risk-ceiling MEDIUM --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional defect-specific constraint; local-first and independent-review rules remain binding |

## Authorization / Source

- Operator instruction: current agent remains orchestrator/reviewer and another agent is worker.
- Active continuity: `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
- Local-first learning: `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`.
- Accepted projection owner: `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-case-evidence-projection.contract.ts`.
- Current intake owner: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts`.
- Current proposal-only owner: `EXTENSIONS/CVF_TRUTH_FLOW/src/types/feedback-proposal.ts`.
- Accepted 205-row ledger: `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_FILE_LEDGER_2026-08-15.json`.
- Local candidate files are high-value design evidence, not CVF authority or copy authority.

## Decision / Baseline

Decision: `PROCEED_BOUNDED_HIGH_VALUE`.

The current Learning Plane already owns signal intake and autonomous-mutation
denial. The missing delta is a fail-closed adapter-free seam that proves a
candidate came from a current T5 projection, binds its evidence references,
keeps review/deduplication/contradiction pending, and routes the result into
the existing intake record without storing or promoting it.

## Scope / Owner Boundary

Owner: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/`.

Risk ceiling: `R1`. Pure TypeScript validation and transformation only. All
time is explicit input. No filesystem, database, environment read, network,
provider, credential, subprocess, random source, storage, or mutation.

## Allowed Paths

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/capability-learning-candidate-projection.ts` (NEW)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/capability-learning-candidate-projection.test.ts` (NEW)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts`
- `docs/reviews/CVF_RSPB_AI_T6_CAPABILITY_PROJECTION_TO_LEARNING_CANDIDATE_INTAKE_SEAM_WORKER_RETURN_2026-08-16.md` (NEW)

## Forbidden Actions

- No direct import or execution of local candidate implementation/checker.
- No edit to T3-T5 behavior, existing LearningSignalIntakeBridge behavior,
  feedback ledger, Truth Flow, storage, memory, governance checker, registry,
  session state, handoff, Web, CLI/MCP, adapter, executor, or public surface.
- No filesystem/database/environment/network/provider/live access.
- No autonomous review acceptance, deduplication completion, contradiction
  resolution, promotion target, policy/truth mutation, or durable write.
- Worker must not stage, commit, push, or public-sync.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T5 projection owner exists | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-case-evidence-projection.contract.ts` | exported interface and function | `CapabilityCaseEvidenceProjection`; `projectCapabilityCaseEvidence` | Guard Contract | ACCEPT |
| Learning intake owner exists | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | exported input, record, and class | `LearningSignalIntakeInput`; `LearningSignalIntakeRecord`; `LearningSignalIntakeBridge` | Learning Plane | ACCEPT |
| intake forbids autonomous mutation | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | returned record | `autonomousMutationAuthorized` | Learning Plane | ACCEPT |
| runtime learning candidates require work orders | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | `requiresGovernanceWorkOrder` | `RUNTIME_LEARNING_CANDIDATE` | Learning Plane | ACCEPT |
| Truth Flow proposals cannot directly mutate | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_FLOW/src/types/feedback-proposal.ts` | `FeedbackProposal` | `no_direct_mutation_flag` | Truth Flow | ACCEPT |
| local learning implementation is safe to import | RUNTIME_BEHAVIOR | `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/capability_preflight/learning.candidate.ts` | entire implementation | `createLearningCandidate` | mixed-origin candidate | REJECT |
| local promotion checker is canonical enforcement | GOVERNANCE | `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/governance/compat/check_capability_learning_promotion.py` | `main` | standalone candidate checker | mixed-origin candidate | REJECT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact planned path/symbol | no current `capability-learning-candidate-projection` owner | NEW_PATH_CONFIRMED |
| generic learning intake | existing `LearningSignalIntakeBridge` is authoritative owner | ENRICH_EXISTING |
| feedback proposal/promotion | existing Truth Flow and governance owners remain unchanged | NO_PARALLEL_AUTHORITY |

## Mixed-Origin Derived Synthesis Provenance

artifactClass: PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE

authorityStatus: NON_AUTHORITATIVE_UNTIL_REVIEWED

| Input or concept | Origin class | Evidence basis | Claim type | Validation method | Current CVF owner | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| provenance/redaction/review-pending candidate | OPERATOR_AGENT_CO_DESIGNED | local contract, schema, policy, source, tests, fixtures | derived design | detailed content inspection and CVF-native adversarial tests | Learning Plane | ADAPT |
| no self-promotion | CVF_PUBLIC_DERIVED | local negative fixture plus current Truth Flow boundary | governance invariant | literal false/null/PENDING assertions | Learning Plane and Truth Flow | ENRICH_EXISTING |
| local regex and checker implementation | MIXED_ORIGIN | candidate source/checker | candidate code | strength comparison | none | REJECT_DIRECT_IMPORT |

## Absorption Decision Vector

| Decision axis | Decision | Evidence | Cost boundary |
| --- | --- | --- | --- |
| Knowledge absorption | PROCEED_BOUNDED | eight-file selected local cluster | one capability cluster |
| Direct import | REJECT_DIRECT_IMPORT | local code is shallow and weaker than T5 validation | CVF-native implementation only |
| Runtime activation | CONTRACT_ONLY | pure in-memory composition into current intake bridge | no persistence or external adapter |
| Authority promotion | NOT_AUTHORIZED | all candidates remain pending and mutation false | independent review remains mandatory |

## System-Chain Value Review

| Chain component | Evidence path | Existing CVF owner/gap | Value disposition | Readiness disposition | Next action |
| --- | --- | --- | --- | --- | --- |
| capability evidence projection | T5 Guard Contract | accepted upstream output | HIGH_VALUE | READY_TO_CONSUME | bind without strengthening |
| projection-bound candidate | selected local cluster | missing seam | HIGH_VALUE | IMPLEMENT_NOW | add pure projection module |
| learning intake record | LearningSignalIntakeBridge | existing owner | HIGH_VALUE | READY_TO_CONSUME | compose without modifying owner behavior |
| durable learning/policy/truth promotion | feedback/Truth Flow/governance owners | separately governed | DEFER | NOT_AUTHORIZED | independent work order only |

## Absorption Efficiency And Provenance Reuse

manifestLedgerReuse: REUSE_IF_FRESH

semanticReviewUnit: CAPABILITY_CLUSTER

defaultValuePosture: PRESERVE_UNTIL_CONTRADICTED

additionalValueProbe: SKIP_UNLESS_NAMED_GAP

latencyBudget: SINGLE_PASS_BOUNDED

intakePriority: LOCAL_SYNTHESIZED_PACK_FIRST

localSemanticInspection: FILE_AND_USE_CASE_CONTENT_REQUIRED

mappingAction: DIRECT_WORK_ORDER_FOR_HIGH_FIT_CLUSTERS

deliverySequence: WORK_ORDER_THEN_WORKER_THEN_INDEPENDENT_REVIEWER

namePatternInference: FORBIDDEN_AS_VALUE_DISPOSITION

upstreamConsultation: TARGETED_FOR_PROVENANCE_OR_GAP

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | accepted local Capability Preflight Bootstrap folder |
| Enumeration command | predecessor `rg --files --hidden --no-ignore`; named eight-file selection |
| Manifest artifact or inline manifest | `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_MANIFEST_2026-08-15.json` |
| Processing ledger artifact or inline ledger | `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_FILE_LEDGER_2026-08-15.json` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-case-evidence-projection.contract.ts`; `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts`; `EXTENSIONS/CVF_TRUTH_FLOW/src/types/feedback-proposal.ts` |
| Unresolved items | 0 processing rows; implementation pending worker/reviewer |
| Completion claim boundary | selected-cluster dispatch only; no full rescan or durable activation |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| contract/schema/policy | provenance, redaction, scope, review and promotion gates | PACKAGE_CANDIDATE | Learning Plane | adapt | pure contract only |
| source/test/fixtures | positive and self-promotion use cases | RUNTIME_CANDIDATE | focused tests | rewrite | no candidate execution |
| candidate checker | promotion invariants | CHECKER_CANDIDATE | focused tests | encode stronger assertions | no hook wiring |
| local policy concepts | no-self-promotion doctrine | DOCTRINE_ADAPTED | existing Learning/Truth boundaries | encode in contract invariants | no new doctrine owner |
| local source/checker direct import | weaker parallel implementation | REJECT_DIRECT_IMPORT | none | reject | no source execution |
| unrelated local scaffolds | no selected T6 value | NO_PACKAGE_OR_RUNTIME_VALUE | predecessor ledger | retain prior disposition | out of tranche |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| generic learning intake | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | CONFIRMED_EXISTING | upstream owner | compose |
| direct mutation prohibition | `EXTENSIONS/CVF_TRUTH_FLOW/src/types/feedback-proposal.ts` | CONFIRMED_EXISTING | stronger existing boundary | preserve |
| T5-to-learning evidence binding | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-case-evidence-projection.contract.ts`; `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | NEW_FINDING | no current consumer | implement bounded seam |
| candidate local source/checker | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts`; `governance/compat/check_finding_to_governance_learning.py` | REJECT_DIRECT_IMPORT | weaker parallel code | do not copy |

## Mandatory Blind-Spot Control Block

The local folder is provenance-backed derived synthesis. The eight files were
read at content/use-case level and compared with current owners. Existing
overlap narrowed the implementation target; it did not erase the novel
T5-to-learning binding value.

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | selected mixed-origin copied-folder cluster |
| Upstream or source-mirror disposition | accepted predecessor evidence reused; no fetch |
| Enumeration or manifest plan | accepted 205-file ledger; named eight-file cluster |
| Per-file terminal-ledger plan | eight hashes in paired work order |
| Owner or overlap route | existing Learning Plane and Truth Flow |
| Value-disposition route | projection/intake seam DO_NOW; durable promotion deferred |
| Claim boundary | no rescan, direct import, persistence, or authority activation |

## Rescan Intelligence Hardening

- Original source artifact: operator-provided mixed-origin local folder.
- Predecessor intake artifact: accepted RSPB-AI-T0 205-file ledger.
- Delta ledger status: reused; eight selected hashes recomputed.
- Routing matrix status: learning cluster routed to existing Learning Plane.
- Semantic sampling status: all eight selected contents inspected.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Treatment |
| --- | --- |
| UNCHANGED_FROM_INTAKE | 197 files retain prior disposition |
| CHANGED_DISPOSITION | eight selected for bounded adaptation |
| NEW_FINDING | T5-to-learning binding seam missing |
| REMOVED_OR_REJECTED | local source/checker import rejected |

### Follow-Up Routing Matrix

| Routing lane | Handling |
| --- | --- |
| DO_NOW | pure module/tests/export/worker return |
| SEPARATE_RUNTIME_TRANCHE | storage or external consumer |
| STRATEGIC_OPERATOR_DECISION | truth/policy promotion or mutation |
| OUT_OF_SCOPE | provider/live/public/deploy/production |
| RESOLVED_BY_DESIGN | fixed pending/null/false authority boundary |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| RSPB-T6-B1 | learning contract | no self-promotion | ADAPT | inject accepted canonical target | REQUIRE_FAIL_CLOSED |
| RSPB-T6-B2 | schema/policy | provenance and review required | ADAPT | unknown T5 references | REQUIRE_FAIL_CLOSED |
| RSPB-T6-B3 | local implementation | regex redaction is enough | REJECT_DIRECT_IMPORT | nested/hostile secret signal | REQUIRE_REJECTION |

## Corpus Completeness And Report Integrity

- Corpus task class: selected capability-cluster absorption.
- Corpus root: eight selected local files.
- Snapshot time: 2026-08-16 dispatcher selection.
- Enumeration command: predecessor `rg --files --hidden --no-ignore` plus named selection.
- Manifest artifact or inline manifest: selected hashes in paired work order.
- Manifest hash: predecessor ledger SHA-256 `96a8908960a03bbd4ab694cbdb592fd4b93112429f41a0f5198af6ee2935c4a6`; eight selected per-file hashes are in the paired work order.
- Processing ledger artifact or inline ledger: accepted 205-row ledger plus conversion matrix.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=8; ledger_terminal=8; exclusions=197; unresolved=0; predecessor_total=205.
- Unresolved files: 0.
- Declared exclusions: 197 files outside this cluster.
- Unreadable or unsupported files: none selected.
- Aggregation check: 8 + 197 = 205.
- Drift check: eight selected hashes recomputed.
- Output traceability: cluster maps to four worker-owned paths.
- Adversarial verification: provenance, secrets, stale/malformed inputs, evidence references, self-promotion, and determinism.
- Corpus verdict: PARTIAL

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | Learning Plane barrel export | returns pending candidate and intake record only | focused tests required | in-process import only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | none | no adapter, authentication, storage, promotion, or mutation authority | forbidden scope | separate future adapter | DEFERRED_WITH_REASON |

## Risk / Corrective Action

Fail closed on malformed/proxy/accessor/unbounded input, stale projection,
authority mismatch, secret-like content, unknown evidence references, missing
revalidation, or any accepted/promoted/deduplicated/contradiction-resolved
state. Stop if safe behavior requires a fifth worker path or any I/O.

## Evidence / Verification

Required evidence is exact four-path diff, focused composition/adversarial
tests, existing bridge regression, full Learning Plane package tests,
TypeScript no-emit, worker-return fast gate, zero provider/live calls, and
independent Codex reviewer reproduction before any commit.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | accepted ledger -> inspected learning cluster -> current Learning Plane owner -> bounded adaptation |
| Matching local-view guard | `governance/compat/check_mixed_origin_derived_synthesis_absorption.py` |
| Owner surface | Learning Plane projection/intake seam |
| Disposition | PROCEED_BOUNDED_HIGH_VALUE |
| Claim boundary | no autonomous mutation, durable learning, adapter, or external authority |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch; public sync is forbidden.

## Claim Boundary

This baseline authorizes one hermetic projection-to-learning intake seam and
tests. It does not authorize persistence, canonical learning, policy/truth
promotion, runtime execution, provider/live access, public sync, deployment,
or production.

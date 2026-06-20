# CVF LSC-T0 Learning Signal Chain Reconciliation Codex Classification

Memory class: FULL_RECORD

Status: CLASSIFICATION_COMPLETE_LSC_T1_DISPATCH_READY

docType: review

Date: 2026-06-20

## Purpose

Classify Claude's advisory rebuttal of the LSC-T0 roadmap and record the
accepted corrections before any LSC GC-018 or work order is opened.

## Scope / Methodology

Scope is limited to classification of the advisory rebuttal and correction of
the roadmap's LSC-T1 design direction. Methodology: read the rebuttal, verify
the B1 source claim against `learning-signal-intake-bridge.ts`, compare the
finding to the LSC roadmap, and fold accepted corrections into the roadmap
without opening implementation.

## Source Under Review

| Artifact | Disposition |
|---|---|
| `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | UPDATED_AFTER_REBUTTAL |
| `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_2026-06-20.md` | ADVISORY_INPUT_ACCEPTED_WITH_CLASSIFICATION |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | SOURCE_VERIFIED_FOR_B1 |
| `docs/reference/CVF_MLW3_EVIDENCE_TO_TRUTH_LEARNING_SIGNAL_PIPELINE_2026-06-05.md` | SOURCE_VERIFIED |
| `docs/reviews/CVF_RT2_FINDING_TO_LEARNING_SIGNAL_BRIDGE_COMPLETION_2026-05-31.md` | SOURCE_VERIFIED |
| `docs/reference/worker_experience_retrospective/README.md` | SOURCE_VERIFIED |
| `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_ROUND2_2026-06-20.md` | ADVISORY_INPUT_ACCEPTED_FOR_LSC_T1 |

## Classification Decision

Decision: ACCEPT_REBUTTAL_AND_FOLD_INTO_ROADMAP.

Claude's B1 is correct. LSC must not define a second learning signal record
beside `LearningSignalIntakeRecord`. The roadmap has been updated so LSC-T1 must
extend or map into `LearningSignalIntakeInput` / `LearningSignalIntakeRecord`,
reuse existing lane/severity/defectClass/disposition/autonomous-mutation fields,
and add only the missing operational capture fields.

## Findings / Position

Position: Claude's rebuttal is accepted with roadmap corrections. The material
finding is not that LSC is wrong; it is that LSC must become a reconciliation
chain over existing Learning Plane intake records rather than a parallel schema.

## Risk / Corrective Action

Risk: a new LSC signal record would double-count AAF-T5 tokens,
Finding-To-Governance rows, and MLW3 candidates as separate learning facts.

Corrective action: LSC-T1 must define `rootCauseGroupId`, projection de-dup,
and an extension/mapping contract for `LearningSignalIntakeRecord` before any
ledger or helper implementation.

## Finding Classification Matrix

| Finding | Codex disposition | Roadmap action |
|---|---|---|
| B1 Minimal Signal Event Contract overlaps existing implemented intake record | ACCEPT | roadmap now rejects parallel record and adds intake bridge source verification |
| N1 AAF-T5 token and signal event must be one source | ACCEPT | LSC-T1 requires deterministic `WORKER_EXPERIENCE_RETRO -> signal` mapping |
| N2 `promotionState` overlaps existing disposition vocabulary | ACCEPT | roadmap uses `captureState` as operational lifecycle and requires mapping to existing disposition |
| N3 de-dup is core design risk | ACCEPT | de-dup/rootCauseGroupId moved into LSC-T1 exit criteria |
| Add `EVALUATED` between proposal and governance decision | ACCEPT_WITH_BOUNDARY | chain includes `EVALUATED`, mapped to MLW5/MLW6 rather than a new evaluator |
| Split multi-role capture by role | ACCEPT | LSC-T2 requires shared contract with separate eligibility per role |
| JSON source plus generated aggregate | ACCEPT_FOR_T1_REVIEW | LSC-T1 must decide generated aggregate and drift-check shape |
| Five-field CLI/MCP event payload | ACCEPT | roadmap now keeps external-agent capture payload minimal |
| Keep CGE-T3 and ACE-R1 parked | ACCEPT | Non-Abandonment Rule preserved |
| Round-2 N4 exact AAF-to-intake severity mapping | ACCEPT | LSC-T1 work order must define NONE/no-entry and BLOCKING/critical mapping |
| Round-2 N5 `captureState` vs `disposition` authority | ACCEPT | LSC-T1 work order must make `disposition` the governed source of truth and `captureState` derived/advisory |
| Round-2 AAF-T5 checker source citation | ACCEPT | LSC-T1 work order must cite `governance/compat/check_worker_experience_retrospective.py` |
| Round-2 JSON source plus generated Markdown index | ACCEPT_FOR_T1_REVIEW | LSC-T1 contract must require JSON source plus generated drift-checked Markdown index, without making Markdown a second source of truth |

## Corrected LSC-T0 Position

The roadmap remains valid after correction. Its current position is:

- LSC-T0 is a reconciliation roadmap, not implementation authorization.
- LSC-T1 must be a source-verified ledger/source-layout and de-dup contract.
- LSC-T1 must extend the existing Learning Signal Intake Bridge record surface.
- AAF-T5 worker retro tokens, Finding-To-Governance rows, and MLW3 candidates
  must be projections of one signal when they refer to the same root cause.
- External CLI/MCP capture must stay minimal to avoid latency.
- Promotion remains governed and operator-controlled.
- AAF-T5 `frictionLevel: NONE` and the exact no-friction NA token produce no
  signal entry; `BLOCKING` maps to `critical` unless LSC-T1 source verification
  finds a stronger existing owner rule.
- `disposition` is the governed source of truth; `captureState` is a derived
  readout unless LSC-T1 defines an allowed-pairs table and conflict rule.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output to finding classification to governed roadmap correction |
| Owner surface | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` |
| Disposition | ADAPT as CVF-owned roadmap correction |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Claim boundary | Claude rebuttal is advisory until classified by this artifact and folded into the roadmap |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| LSC draft risked parallel-core schema beside `LearningSignalIntakeRecord` | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T1 must extend existing intake record | handled in roadmap |
| De-dup/root-cause grouping is not optional | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | LSC-T1 must define rootCauseGroupId and projection de-dup | deferred to LSC-T1 |
| External CLI/MCP capture must avoid latency | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T6 must keep minimal payload and helper-synthesized defaults | deferred |
| AAF-to-intake severity mapping has a no-entry case | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T1 must define exact severity/no-entry mapping | handled in LSC-T1 dispatch |
| `captureState` can drift from governed `disposition` | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T1 must define source-of-truth and derived-state rule | handled in LSC-T1 dispatch |
| Runtime/provider/cost applicability for this classification | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed by this roadmap classification | handled |

## Claim Boundary

This classification records roadmap-level decisions only. It does not implement
a signal ledger, modify runtime source, change Learning Plane contracts, create
CLI/MCP behavior, authorize provider/live proof, open public-sync, or claim
readiness or universal governed-coding control.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LSC-T0 rebuttal classification only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | review classification and roadmap correction only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | advisory classification of learning-signal roadmap findings only |
| forbiddenExpansion | wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap classification. Public export requires
separate public-sync authorization and public-safe claim calibration.

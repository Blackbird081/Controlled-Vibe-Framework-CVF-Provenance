# CVF SOT3-T0 External Review Packet

Memory class: FULL_RECORD

Status: DRAFT_FOR_EXTERNAL_REVIEW

docType: review_context

Date: 2026-07-12

Review packet ID: SOT3-T0-ERP

## Purpose

Provide the bounded, source-aware context that an external reviewer needs to
challenge the proposed CVF Source of Truth three-layer architecture without
receiving implementation or authority-transfer permission.

## Review Objective

Independently scan and challenge the complete retained three-folder Source of
Truth design. Determine whether CVF Refinery, CVF Truth Kernel, and CVF Truth
Flow form a valid three-layer architecture, which concepts merit selective
CVF-native absorption, and which prototype contracts or implementations must
be adapted, deferred, or rejected.

The review must not optimize for agreement with the dispatcher position.
Contradictions, missing evidence, alternative layer boundaries, and reasons to
reject a proposed absorption are required outputs.

## Target / Source

Review all files under these private retained roots:

| Root ID | Source root | Snapshot files | Snapshot bytes | Root digest |
|---|---|---:|---:|---|
| REFINERY | `.private_reference/legacy/CVF_SOT 10.07/CVF_Refinery_Patch` | 133 | 160461 | `c7ace9ccbb470514bb9fea97527976a462146b5b220df88eadc6fdc38b88cbe2` |
| KERNEL | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch` | 93 | 78007 | `73e4cc652f738d70428326a013de08fc65ce4edb553dcd3e4670eb8a46765497` |
| FLOW | `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch` | 79 | 78380 | `e7be38e77889f6280248fc4a6ceacf354a41c8f1c331fbb2a491e29f8a27858f` |

Total expected source files: 305.

Read order inside each root:

1. root README, TREEVIEW, and architecture entry surfaces when present;
2. package README and doctrine/specification files;
3. schemas and types;
4. runtime source;
5. tests and negative cases;
6. adapters, guards, monitors, scripts, rules, examples, and templates;
7. cross-layer reconciliation after all three independent scans.

Truth Kernel has no root-level README or TREEVIEW. Its package and nested
README files remain mandatory reads, and the missing root entry surface must be
assessed as an architecture/documentation finding.

## Scope / Methodology

Required method:

- enumerate every source file, including ignored private files;
- reproduce root-specific count, byte total, and aggregate digest;
- read every file body or mark the exact file `BLOCKED_UNREADABLE`;
- maintain one processing-ledger row per file;
- inspect README and TREEVIEW claims against actual source behavior;
- compare schemas, TypeScript interfaces, examples, and lifecycle tokens across
  all three layers;
- distinguish doctrine value from prototype implementation quality;
- classify each capability group as absorb, adapt, defer, reject, block, or
  no-new-value;
- compare proposed value against current CVF owner surfaces before proposing a
  new owner;
- return evidence-backed dissent, not implementation.

Prototype build and unit-test results may be reproduced as source evaluation.
They are not CVF runtime or production proof.

## CVF Source-Of-Truth Statement

CVF is the source of truth. The retained folders are non-canonical reference
input. Public explanations, copied packages, provider-local memory, chat
summaries, and this packet's initial findings are not CVF authority unless a
later governed CVF artifact source-verifies and accepts them.

## Public / Private Boundary

| Surface | Disposition |
|---|---|
| Retained three-folder corpus | private provenance input; may be read inside the local authorized workspace |
| This review packet and roadmap | private governed review context |
| Public-safe facts | none authorized for export by this packet |
| Forbidden exposure | no secrets, keys, credentials, environment files, unrelated private material, or raw source publication |
| Public action | forbidden; separate public-sync authorization required |

## Workflow-Chain Interpretation Map

| Label or phrase | Review interpretation | CVF authority to check |
|---|---|---|
| `READY_FOR_KERNEL` | structural eligibility only, not truth | retained Refinery packet spec plus current CVF truth-foundation owners |
| `VERIFIED` | must be supported by a Kernel decision and receipt | retained Kernel receipt/gate sources plus current CVF receipt owners |
| `PUBLISHED` | information distribution state, not execution approval | retained Flow lifecycle and current CVF governance boundaries |
| `Acquire -> Refine -> Verify -> Register -> Route` | conceptual information lifecycle, not automatically one module's ownership | three retained layer boundaries and SOT3 roadmap |
| public/simple CVF phase labels | display vocabulary unless mapped to governed state | `docs/reference/external_agent_review/CVF_WORKFLOW_CHAIN_PUBLIC_REVIEW_CONTEXT.md` |

## Current Authority Surfaces

| Surface | Role | Why it matters |
|---|---|---|
| `AGENTS.md` | repository governance front door | controls authority, source verification, work orders, closure, and private/public boundaries |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current governed session state | identifies current mode and active handoff; not a semantic SOT architecture contract |
| `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md` | proposed review and absorption sequence | defines the bounded three-layer hypothesis and tranche gates |
| `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | current general truth-foundation owner candidate | prevents duplicate doctrine ownership |
| `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_OWNER_SURFACE_RECONCILIATION_MATRIX.md` | existing owner comparison | supports overlap and novelty review |
| `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | current skill-specific vertical slice | compatibility constraint, not proof of a general SOT stack |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` | current receipt-binding runtime owner candidate | compare packet and receipt binding semantics without assuming equivalence |
| `docs/reference/external_agent_review/README.md` | external-review front door | defines advisory status and required absorption route |
| `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | returned-output classifier | external findings must return through this workflow |

## Non-Authority Surfaces

| Surface | Allowed use | Must not be used for |
|---|---|---|
| retained SOT patch folders | architecture and implementation reference input | current CVF authority, direct-import authority, or readiness proof |
| prototype tests | evidence about prototype behavior | CVF integration, release, or production proof |
| dispatcher findings in this packet | hypotheses to challenge | automatic acceptance or closure evidence |
| external reviewer output | advisory critique | CVF semantic authority or implementation authorization |
| provider-local memory and chat | continuity aid only | source verification or canonical evidence |

## Findings / Position

The dispatcher proposes this provisional verdict:

`THREE_LAYER_MODEL_CONFIRMED_WITH_ROLE_SPLIT_AND_CONTRACT_REWRITE`

### Proposed layer map

```text
SourceEnvelope
  -> deterministic CVF Refinery
  -> unverified RefineryPacket
  -> CVF Truth Kernel evaluation and receipt
  -> verified TruthReference
  -> CVF Truth Flow routing, dose, distribution, feedback, and retirement
```

### Refinery position to challenge

- Refinery should be an independent deterministic module.
- It prepares data and produces truth candidates; it does not create truth.
- Source identity is captured before normalization and preserved throughout
  lineage.
- Duplicate grouping should precede conflict selection so repeated copies do
  not inflate conflict candidates.
- Refinery Core contains no AI, agent, prompt, provider SDK, or network
  dependency.
- AI-assisted extraction or similarity, if ever retained, belongs upstream and
  enters as untrusted source-envelope input.

High-value primitives include SourceEnvelope, NormalizedRecord,
DuplicateGroup, ConflictSet, QualityFinding, integrity evidence,
transformation lineage, RefineryPacket, receipts, failure tokens, and
non-destructive grouping.

Initial implementation concerns:

- the engine defaults to an empty stage list;
- date and unit helpers are not fully integrated into a mandatory pipeline;
- JSON schemas are not visibly bound to runtime validation;
- raw records and source envelopes lack a strong one-to-many association;
- random IDs and timestamps weaken reproducibility;
- missing dedupe fields can produce false grouping;
- scope and date overlap logic can fail open or over-group;
- lineage and receipt coverage are incomplete;
- text-level checkers are scaffolds rather than strong enforcement.

### Truth Kernel position to challenge

The Kernel should own evidence admission, obligation evaluation, provenance,
verification, authority decision, receipt issuance, truth references,
supersession, and trust freshness.

High-value primitives include Evidence Registry, Obligation Registry,
provenance labels, SOT Index, verification result, strict and relaxed mode,
Truth Receipt, and project truth references.

Initial implementation concerns:

- an empty verification-result list can produce a non-fail receipt status;
- receipt content binding does not cover the full evaluated packet;
- relaxed mode may permit non-obligation failures;
- release paths do not fully prove packet/receipt/hash identity;
- date parsing can fail open;
- the truth packet schema permits additional properties;
- prototype tests pass while the current TypeScript build fails in the receipt
  implementation.

### Truth Flow position to challenge

Truth Flow has strong value as the post-Kernel lifecycle layer: register,
route, information dose, distribute, consume, observe, feedback proposal,
recall, and retire.

Initial architecture concerns:

- documentation alternates between Flow being built on Kernel and Flow sitting
  before Kernel as the whole lifecycle orchestrator;
- Flow implements a second intake and mini-refinery;
- Flow's RefineryPacket is incompatible with the dedicated Refinery packet;
- lifecycle transitions can promote to VERIFIED without Kernel receipt proof;
- publish gating trusts caller booleans and an unverified receipt identifier;
- routing may match when any selector overlaps rather than satisfying the
  intended policy conjunction;
- information-dose fields are only partially enforced;
- direct source-score mutation conflicts with proposal-only feedback doctrine.

## Review Questions

1. Does the complete corpus support three separately owned layers, or is a
   different decomposition better? Cite file and line/section evidence.
2. Should Truth Flow be only a post-Kernel module, a lifecycle orchestration
   facade over all three layers, or two explicitly named surfaces?
3. Is the proposed no-AI Refinery Core boundary internally consistent with the
   retained package? Identify every file that violates or complicates it.
4. What exact ordering should control source capture, normalization, schema,
   duplicate grouping, conflict detection, integrity, evidence candidates, and
   packet creation?
5. Which Refinery primitives are strong enough to adapt, and which algorithms
   or contracts should be rejected?
6. What minimum Kernel receipt and release invariants prevent empty-result,
   cross-packet, replay, warning-release, and stale-truth failures?
7. Which retained Truth Kernel value is not already owned by current CVF truth
   foundation, skill truth packets, evidence, provenance, or receipt surfaces?
8. Which Flow capabilities remain valuable after intake and refinery ownership
   is removed?
9. List every cross-layer schema, token, lifecycle, casing, and cardinality
   mismatch that prevents integration.
10. Propose an absorb/adapt/defer/reject decision for each capability family,
    with explicit reasons and CVF owner candidates.
11. Identify dispatcher claims that are unsupported, too strong, or wrong.
12. Recommend the smallest safe vertical slice that can prove three-layer value
    without claiming full absorption.

## Expected External-Agent Output

Return one evidence-backed report with these required sections:

| Output type | Required evidence | CVF disposition requested |
|---|---|---|
| Corpus accounting | root count, bytes, digest, and per-file terminal ledger | confirm, limitation, or block |
| Layer verdict | file and section citations from all three roots | confirm, revise, split, or reject |
| Contract mismatch matrix | producer and consumer source citations | adapt, replace, or reject |
| Capability disposition | capability group, value, owner candidate, and risk | absorb, adapt, defer, reject, block, or no-new-value |
| Dispatcher dissent | exact packet claim plus contrary evidence | confirmed, narrowed, or invalidated |
| CVF overlap | current governed owner path checked | existing owner, enrich owner, new finding, or owner not found |
| Missing context | exact source or authority gap | return to CVF reviewer or operator |
| Readiness/runtime claim | current CVF proof | block unless proof exists |

The report must distinguish direct source observation, inference, and
recommendation. Filename-only review or README-only agreement is insufficient.

## Risk / Corrective Action

| Risk | Corrective action required from external reviewer |
|---|---|
| confirmation bias from the supplied position | include a dedicated dissent section and strongest alternative architecture |
| corpus sampling presented as completeness | reconcile all 305 paths or return a visible limitation |
| prototype behavior treated as CVF behavior | label all build/test observations as retained-source evidence only |
| direct import recommendation | reject or rewrite as CVF-native adaptation with owner and contract boundary |
| private material exposure | keep work local and do not publish or copy unrelated private content |
| provider identity treated as authority | use external reviewer role; findings remain advisory |
| implementation advice broadens the task | stop at architecture, contracts, risks, and recommended next work |

## Decision / Disposition

Packet disposition: READY_FOR_BOUNDED_EXTERNAL_REVIEW_WHEN_WORK_ORDER_RELEASES

The packet itself does not dispatch a provider. The paired work order and a
clean post-dispatch commit are required before execution. Returned output must
be reviewed and classified by CVF before any roadmap, contract, source, or
runtime action.

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | retained legacy three-folder source family |
| Upstream or source-mirror disposition | `LEGACY_REFERENCE_ONLY_WITH_REASON`: operator-authored retained patch without verified upstream repository identity |
| Enumeration or manifest plan | recursive direct filesystem enumeration including ignored files and root-specific digests |
| Per-file terminal-ledger plan | one row per source file with body-read and advisory disposition state |
| Owner or overlap route | current CVF owner checks in the external return, final decision by CVF reviewer |
| Value-disposition route | absorb, adapt, defer, reject, block, or no-new-value |
| Claim boundary | architecture critique only; no direct import or authority transfer |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | ignored retained legacy source roots |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | exact 305-file manifest and one body-read ledger row per record |
| Blind-spot prevention action | root digest reproduction, path-set equality, and visible unreadable rows |
| Residual gap | external execution and CVF semantic acceptance remain open |
| Blind-spot verdict | PARTIAL_PENDING_EXTERNAL_REVIEW |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | the three literal roots in Target / Source |
| Enumeration command | direct recursive filesystem enumeration per literal root |
| Manifest artifact or inline manifest | inline Target / Source snapshot table in this packet |
| Processing ledger artifact or inline ledger | inline Scope / Methodology ledger contract in this packet; worker output path is governed by the paired work order |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline Overlap And Novelty Classification table in this packet |
| Unresolved items | 305 before external review |
| Completion claim boundary | packet context only; no absorption, implementation, or readiness proof |

## Corpus Completeness And Report Integrity

- Corpus task class: external review of retained SOT three-layer source family.
- Corpus root: the three roots in Target / Source.
- Snapshot time: 2026-07-12.
- Enumeration command: direct recursive `Get-ChildItem` per literal root.
- Manifest artifact or inline manifest: required external worker manifest.
- Manifest hash: three root-specific digests in Target / Source.
- Processing ledger artifact or inline ledger: required external worker processing ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=305; ledger_terminal=0 before dispatch; exclusions=0; unresolved=305
- Unresolved files: 305 before external execution.
- Declared exclusions: none.
- Unreadable or unsupported files: none known before external execution.
- Aggregation check: root file counts sum to 305 and bytes sum to 316848.
- Drift check: external worker must reproduce root-specific snapshot facts.
- Output traceability: root ID, relative path, digest, and body-read status.
- Adversarial verification: dispatcher scan and prototype tests cannot substitute for independent review.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| three-layer doctrine | preparation, trust evaluation, and distribution separation | DOCTRINE_ADAPTED | SOT3-T2 candidate | external critique and CVF review first | no implementation |
| Refinery primitives | deterministic source preparation | PACKAGE_CANDIDATE | SOT3-T3 candidate | challenge contracts and algorithms | no direct import |
| Kernel primitives | evidence, obligation, provenance, verification, and receipt | RUNTIME_CANDIDATE | SOT3-T4 candidate | compare against current owners | no runtime mutation |
| Flow primitives | routing, dose, distribution, lifecycle, and feedback | RUNTIME_CANDIDATE | SOT3-T5 candidate | remove duplicated upstream ownership | no runtime mutation |
| prototype guards and negative cases | enforcement use cases | CHECKER_CANDIDATE | future owner decision | record advisory value only | no checker wiring |
| incompatible duplicate packet definitions | integration risk evidence | REJECT_DIRECT_IMPORT | SOT3-T2 negative evidence | cite and preserve mismatch | no package activation |
| duplicate or non-reusable historical material | context value only | NO_PACKAGE_OR_RUNTIME_VALUE | retained provenance | require file-level reason | no runtime or package action |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| general truth doctrine | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | ENRICH_EXISTING | retained corpus may contain broader contract value | external reviewer must identify exact delta |
| skill truth packet | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | ENRICH_EXISTING | skill vertical slice is not assumed to own general SOT | preserve compatibility analysis |
| independent Refinery owner | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | general owner not established by this packet | require current worker search before confirming |
| post-Kernel Flow owner | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | general owner not established by this packet | require current worker search before confirming |
| prototype receipt and publish paths | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` | REJECT_DIRECT_IMPORT | retained contracts differ from current CVF binding owner | recommend adaptation only |

## Negative Search And Collision Discipline

Search roots: current `docs`, `EXTENSIONS`, `governance`, schemas, tests, JSON,
and the three retained external-evidence roots.

Search command:
`rg -n --hidden --no-ignore "RefineryPacket|SourceEnvelope|TruthReceipt|TruthReference|DistributionPackage|FeedbackProposal" docs EXTENSIONS governance '.private_reference/legacy/CVF_SOT 10.07'`

Same-token collision result: `CVF` and the listed contract tokens have
non-authoritative or different-meaning occurrences elsewhere; no occurrence is
treated as an absence result or binding owner proof.

Absent-versus-collision disposition: every provisional owner gap remains a
worker search question and CVF reviewer decision, not a packet-level absence
claim.

| Check | Evidence | Disposition |
|---|---|---|
| proposed owner names | exact current-repository search required in external return | no absence claim from dispatcher memory |
| packet and lifecycle tokens | retained and current matches must be separated by source | same token does not prove semantic equivalence |
| owner-surface result | exact path or source-not-found result with command evidence | provisional until worker search and CVF review |
| Truth Kernel root entry files | direct root enumeration | missing root README/TREEVIEW is a bounded documentation fact |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | bounded external-review packet -> advisory external return -> external-finding absorption workflow -> CVF reviewer disposition |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` for the later returned-output absorption artifact |
| Owner surface | this packet for context; SOT3 roadmap for sequencing; CVF reviewer for acceptance |
| Disposition | ADAPT external critique only after source verification and overlap review |
| Claim boundary | no external output becomes CVF authority directly |

## Finding-To-Governance Learning Disposition

| Finding | defectClass | learningLane | disposition | nextAction |
|---|---|---|---|---|
| three retained layers use conflicting topology and packet contracts | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | external review must produce a source-backed mismatch matrix before contract work |
| prototype trust transitions may fail open | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | RUNTIME_LEARNING_CANDIDATE | preserve as a future contract-test candidate; no runtime edit in this tranche |

Next action: dispatch the bounded external scan only after clean commit and
passing pre-dispatch gates; route returned observations to the CVF reviewer.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the three-layer separation is architecturally
valuable, while current implementations require contract and boundary rewrite.

Evidence Comparison Requirement: the external return must compare every major
conclusion against full-corpus evidence and name contradictions.

Contradiction Handling Requirement: contrary evidence must receive a
Contradiction Or Gap Disposition and revise or invalidate the affected claim.

Claim Update Requirement: the external return records whether the proposed
three-layer verdict is confirmed, revised, narrowed, split, or invalidated.

## Checker Source Read-Ahead Block

| Field | Disposition |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Review Objective; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision / Disposition; External Repository Absorption Entry Control; Corpus Completeness And Report Integrity; External Knowledge Intake Routing; Finding-To-Governance Learning Disposition; Epistemic Process Block; PARTIAL |
| gateRunPurpose | confirm packet shape and bounded evidence after pre-write checker review |
| claimBoundary | checker conformance does not prove corpus completeness or validate the architecture position |

## Absorption Instruction

External output is advisory. CVF will split returned observations into atomic
items and classify them through
`docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`
before changing any standard, roadmap, work order, source, runtime, checker, or
operator decision.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this packet names private retained source and is intended for a local
authorized external-review surface only.

## Claim Boundary

This packet supplies bounded review context. It does not authorize provider
execution by itself, public exposure, source mutation, direct import, contract
ratification, runtime or checker work, package activation, live proof, release,
or production readiness. The external reviewer must not claim CVF semantic
truth beyond the supplied current governed authority surfaces.

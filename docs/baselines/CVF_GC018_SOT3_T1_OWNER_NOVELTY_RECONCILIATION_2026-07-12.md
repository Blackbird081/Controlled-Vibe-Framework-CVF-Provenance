# CVF GC-018 Baseline - SOT3-T1 Owner And Novelty Reconciliation

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-12

Baseline ID: GC018-SOT3-T1

Risk ceiling: HIGH_EVIDENCE_DOCS_ONLY

## Purpose

Authorize one no-commit evidence worker to reconcile every accepted SOT3
capability group against current CVF owner surfaces and return explicit
ABSORB, ADAPT, DEFER, REJECT, BLOCK, or NO_NEW_VALUE decisions before any
contract or implementation work.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind gc018-baseline --batch-id SOT3-T1 --title "Owner And Novelty Reconciliation" --date 2026-07-12 --base e8b795551 --stdout` |
| generatedProfile | GC-018 owner/novelty evidence review |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Added T0R dependency, owner search, overlap, external absorption, evidence, fail-condition, and claim-boundary controls. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| docOnlyNewFields | `ownerDecision`; `noveltyDecision`; `canonicalOwnerCandidate`; `collisionDisposition` |
| claimBoundary | Dispatch baseline only; no owner creation, contract ratification, or implementation. |

## Target / Source

Primary accepted evidence:

- `docs/reviews/CVF_SOT3_T0R_COMPLETION_REVIEW_2026-07-12.md`;
- `docs/reviews/CVF_SOT3_T0R_SEMANTIC_RECONCILIATION_MATRIX_2026-07-12.md`;
- `docs/reviews/CVF_SOT3_T0R_THREE_LAYER_ARCHITECTURE_DECISION_RECOMMENDATION_2026-07-12.md`;
- `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md`;
- `docs/evidence/sot/sot3-t0-source-manifest.json`.

Current owner-search roots: `docs/reference/`, `EXTENSIONS/`, `governance/`,
schemas, tests, and active registries. Retained source remains read-only.

## Scope / Target / Owner Boundary

Allowed: current-owner searches, exact capability grouping, overlap and
novelty decisions, owner-candidate recommendations, and three review outputs.

Forbidden: owner creation, canonical contract authoring, runtime/schema/test/
guard/checker mutation, direct import, package activation, provider/live proof,
public-sync, commit, or readiness claim.

## Findings / Position

T0R accepted the layer topology but deliberately did not decide where each
capability belongs in current CVF. T1 must distinguish:

- `ENRICH_EXISTING_OWNER`;
- `NEW_OWNER_CANDIDATE`;
- `SHARED_PRIMITIVE_CANDIDATE`;
- `DEFER_WITH_REOPEN_CONDITION`;
- `REJECT_DIRECT_IMPORT`;
- `NO_NEW_VALUE`;
- `BLOCKED_MISSING_OWNER_EVIDENCE`.

No missing owner may be silently converted into a created owner.

## Baseline Decision

SOT3-T1 owner/novelty reconciliation is authorized as documentation evidence
only. Implementation and SOT3-T2 contract work remain `NOT_AUTHORIZED`.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`owner novelty reconciliation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class "owner novelty reconciliation" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector docs/work_orders --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T0R architecture planning basis is accepted | VALUE_SET | `docs/reviews/CVF_SOT3_T0R_COMPLETION_REVIEW_2026-07-12.md` | Disposition | `REVIEWER_ACCEPTED_BOUNDED` | T0R completion review | ACCEPT |
| implementation remains unauthorized | LITERAL_INVARIANT | `docs/reviews/CVF_SOT3_T0R_COMPLETION_REVIEW_2026-07-12.md` | Implementation Boundary | `NOT_AUTHORIZED` | T0R completion review | ACCEPT |
| current general truth-foundation owner exists | EXISTS | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | file | `CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT` | truth foundation | ACCEPT |
| current skill-specific truth packet owner exists | EXISTS | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | file | `CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD` | agent-system skill truth | ACCEPT |
| current receipt-binding contract exists but requires semantic comparison | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` | exported contract | `receipt-binding.contract.ts` | Guard Contract | ACCEPT |
| T1 is the next roadmap tranche | VALUE_SET | `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md` | Tranche Plan | `SOT3-T1` | SOT3 roadmap | ACCEPT |

## Negative Search And Collision Discipline

| Search token | Exact search command or query | Search roots | Same-token collision result | Disposition |
|---|---|---|---|---|
| `RefineryPacket` | `rg -n "RefineryPacket" docs/reference EXTENSIONS governance` | current CVF docs, extensions, governance | retained and current packet-name matches require semantic comparison | COLLISION_REVIEW_REQUIRED |
| `TruthReceipt` | `rg -n "TruthReceipt|truth receipt|receipt binding" docs/reference EXTENSIONS governance` | current CVF docs, extensions, governance | receipt terms span different workflow and truth semantics | COLLISION_REVIEW_REQUIRED |
| `TruthReference` | `rg -n "TruthReference|truth reference" docs/reference EXTENSIONS governance` | current CVF docs, extensions, governance | same-token documentation candidates do not establish contract ownership | COLLISION_REVIEW_REQUIRED |
| `Truth Flow` | `rg -n "Truth Flow|post-Kernel|distribution lifecycle" docs/reference EXTENSIONS governance` | current CVF docs, extensions, governance | routing and flow terms may belong to unrelated execution surfaces | COLLISION_REVIEW_REQUIRED |

Worker output must preserve commands, matches, semantic comparison, and a
terminal absent-versus-collision disposition for every capability group.

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | retained legacy three-layer family plus accepted T0R evidence |
| Upstream or source-mirror disposition | LEGACY_REFERENCE_ONLY_WITH_REASON |
| Enumeration or manifest plan | reuse committed 305-file manifest and exact T0R evidence |
| Per-file terminal-ledger plan | do not rewrite 305 rows; reconcile value-bearing capability groups |
| Owner or overlap route | exact current-owner path, explicit new-owner candidate, defer/reject/no-value, or blocker |
| Value-disposition route | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Claim boundary | owner decision recommendation only; no owner creation or implementation |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | accepted T0R capability and conversion matrices |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | every T0R capability group and every NEW_ABSORB_CANDIDATE receives a terminal owner/novelty decision |
| Blind-spot prevention action | exact input-to-output reconciliation and negative owner searches |
| Residual gap | canonical contracts remain T2-owned and unauthorized |
| Blind-spot verdict | PARTIAL_PENDING_T1_EXECUTION |

## Corpus Completeness And Report Integrity

- Corpus task class: SOT3 capability owner/novelty reconciliation.
- Corpus root: accepted T0R artifacts plus current CVF owner-search roots.
- Snapshot time: 2026-07-12 dispatch.
- Enumeration command: `rg --files --hidden --no-ignore docs/reviews docs/reference EXTENSIONS governance`, followed by deterministic extraction of the 12 rows in the accepted T0R Capability Absorption Matrix.
- Manifest artifact or inline manifest: `docs/evidence/sot/sot3-t0-source-manifest.json`.
- Manifest hash: reused per-file SHA-256 evidence; no new aggregate claim.
- Processing ledger artifact or inline ledger: T0 ledger plus T0R matrix.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, REJECTED, BLOCKED_UNREADABLE
- Reconciliation: manifest=12; ledger_terminal=0; exclusions=0; unresolved=12
- Unresolved files: 0 identities; 12 capability owner decisions pending.
- Declared exclusions: implementation-level low-value rows remain governed by the T0 ledger unless promoted by a cited capability group.
- Unreadable or unsupported files: none known.
- Aggregation check: exact capability-key set equality required.
- Drift check: stop on source or accepted-evidence drift.
- Output traceability: each owner decision cites current CVF path/search evidence and T0R source evidence.
- Adversarial verification: same-token collision does not prove semantic ownership.
- Corpus verdict: PARTIAL

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | accepted T0R evidence and current CVF owner roots |
| Enumeration command | capability-row extraction plus current-owner `rg` search |
| Manifest artifact or inline manifest | accepted T0R capability matrices |
| Processing ledger artifact or inline ledger | planned T1 owner decision ledger |
| Ledger terminal statuses | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Disposition taxonomy | ENRICH_EXISTING_OWNER, NEW_OWNER_CANDIDATE, SHARED_PRIMITIVE_CANDIDATE, DEFER_WITH_REOPEN_CONDITION, REJECT_DIRECT_IMPORT, NO_NEW_VALUE, BLOCKED_MISSING_OWNER_EVIDENCE |
| Owner-surface map | planned `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md` |
| Unresolved items | capability ownership and novelty decisions pending |
| Completion claim boundary | evidence recommendation only; no owner or runtime creation |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| accepted T0R capability groups | architecture and primitive value | DOCTRINE_ADAPTED | exact T1 owner decision rows | reconcile current owners | no implementation |
| new absorb candidates | deferred but high-value doctrine | OWNER_DECISION_NEEDED | T1 novelty ledger | accept/defer/reject with reason | no package/runtime action |
| rejected direct imports | negative integration evidence | REJECT_DIRECT_IMPORT | T1 negative owner map | preserve exclusion | no direct import |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| general truth doctrine | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | ENRICH_EXISTING candidate | retained stack is broader | verify exact delta |
| skill truth packet | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | preserve vertical owner | skill-specific only | prevent owner collision |
| receipt binding | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` | semantic comparison required | may be unrelated workflow receipt | do not infer TruthReceipt ownership |
| independent Refinery and post-Kernel Flow | current owner not yet proven | owner decision pending | possible new owner surfaces | search before recommending |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | accepted T0R -> T1 owner/novelty reconciliation -> CVF review -> possible T2 packet |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | paired T1 baseline and work order |
| Disposition | ADAPT through source-backed owner reconciliation |
| Claim boundary | no external or worker recommendation directly creates CVF authority |

## Verification / Evidence

- exact capability-key reconciliation;
- current owner path plus section/symbol for every existing-owner decision;
- negative searches for every new-owner candidate;
- collision analysis for similarly named but semantically different surfaces;
- explicit reopen condition for every value-parked defer;
- exactly three worker outputs and unchanged HEAD.

## Checker Source Read-Ahead Block

| Field | Disposition |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | DISPATCH_READY; Source Verification Block; External Absorption Core; Overlap And Novelty Classification; PARTIAL; NOT_AUTHORIZED |
| gateRunPurpose | confirm dispatch evidence shape after source and checker review |
| claimBoundary | checker conformance does not decide owner correctness |

## Acceptance Criteria

- [ ] every input capability group has exactly one terminal owner decision;
- [ ] existing-owner claims cite exact current CVF evidence;
- [ ] new-owner candidates include negative searches;
- [ ] defers include checkable reopen conditions;
- [ ] direct-import rejections and claim-tag extraction remain distinct;
- [ ] implementation remains NOT_AUTHORIZED;
- [ ] exactly three outputs and no worker commit.

## Fail Conditions

- same-token match treated as ownership proof;
- missing owner silently promoted to a new canonical owner;
- capability group omitted, duplicated, or merged without trace;
- vague defer without reopen condition;
- contract, code, package, schema, test, guard, or checker mutation;
- implementation or readiness claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: retained private source and internal owner planning.

## Claim Boundary

This baseline authorizes owner and novelty reconciliation only. It does not
authorize owner creation, canonical contracts, implementation, package
activation, provider/live proof, public-sync, release, or readiness.

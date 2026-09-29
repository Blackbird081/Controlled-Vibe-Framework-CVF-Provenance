# CVF GC-018 Baseline - PINT-R2 Provider Health And Capability Owner Source Comparison

Memory class: POINTER_RECORD

Status: REVIEWER_ACCEPTED_DISPATCH_READY_WITH_REPAIRS

docType: baseline

Batch ID: PINT-R2

Dispatch base head: `b3f7a14c1`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer/closer: independent reviewer/closer

Worker target: delegated documentation worker

## Purpose

Authorize one bounded, documentation-only source-to-owner comparison tranche
for the two PINT-R1 candidates whose recorded reopen condition is now
satisfiable from current local owner sources:

- candidate A: the external six-state provider-health vocabulary versus the
  current `ProviderHealthMonitor` implementation and tests;
- candidate B: the external task-type/capability-tag vocabulary versus the
  current provider capability registry implementation and tests.

This baseline authorizes the worker to produce an exact comparison matrix and
one evidence-backed proposed disposition per candidate (`ENRICH_EXISTING`,
`NO_NEW_VALUE`, or `DEFER_PENDING_OWNER_SOURCE_VERIFICATION`). It does not
authorize the worker to edit owner runtime/source, adopt an enum, activate a
package, implement a checker, or claim production/runtime behavior. Final
semantic acceptance remains reviewer-owned.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | manual authoring from PINT-R1 GC-018/work-order structural precedent (`docs/baselines/CVF_GC018_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_AND_MCP_VALUE_RECONCILIATION_2026-07-23.md`); `build_dispatch_packet_scaffold.py --packet-kind source-intake` pattern followed without a live scaffold invocation |
| generatedProfile | source-intake plus no-commit worker profile |
| generatedSkeletonStatus | MANUAL_TEMPLATE_ADAPTATION |
| manualEditsAfterScaffold | replaced all PINT-R1 corpus-rescan-specific evidence with the narrower two-candidate owner-source comparison scope, owner source citations, and reopen-condition evidence |
| checkerReadAheadConfirmation | dispatch-quality, closure-package, absorption core/value-conversion/overlap, corpus-completeness, checker-read-ahead, ADIF-disclosure, literal-format-gotchas checker sources |
| docOnlyNewFields | per-candidate comparison-matrix columns (vocabulary overlap, semantic overlap, runtime representation, test-proved behavior, external-doctrine-not-present, unsafe-direct-adoption-risk) |
| claimBoundary | dispatch evidence only; no runtime, provider, live, public, package, checker, or MCP/CLI behavior claim |

## Authorization / Decision

`CVF_SESSION/ACTIVE_SESSION_STATE.json` `nextAllowedMove` (recorded after PINT-R1
closure at material commit `9b26de3dc`) explicitly authorizes "an operator
checkpoint to select a new external repository/corpus for governed intake or
explicitly authorize one deferred PINT owner-source comparison." This dispatch
is that explicitly authorized deferred PINT owner-source comparison; it does
not select a new external corpus.

Decision: `AUTHORIZE_PINT_R2_PROVIDER_HEALTH_AND_CAPABILITY_OWNER_SOURCE_COMPARISON_ONLY`.

## Reopen-Condition Trace

| Candidate | PINT-R1 reviewer disposition | Recorded reopen condition | Source |
| --- | --- | --- | --- |
| six-state provider-health enum | `DEFER_PENDING_OWNER_SOURCE_VERIFICATION` | "reopen only when a documentation tranche directly compares the enum against current `ProviderHealthMonitor` source" | `docs/reviews/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_COMPLETION_2026-07-23.md` Reviewer Semantic Value Audit table |
| task-type and capability-tag vocabulary | `DEFER_PENDING_OWNER_SOURCE_VERIFICATION` | "reopen only after direct comparison with `PROVIDER_CAPABILITY_REGISTRY`" | `docs/reviews/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_COMPLETION_2026-07-23.md` Reviewer Semantic Value Audit table |

Both reopen conditions name a bounded documentation comparison, not a runtime,
package, or checker change. This dispatch releases exactly that bounded
comparison and nothing wider.

## Scope / Methodology

The worker opens and inspects the exact current owner source and test files
below, and the exact retained PINT source files below, then builds one
comparison matrix per candidate. The worker must not rely on the PINT-R1 audit
summary text alone; it must re-open the cited source files itself and record
its own verified evidence.

### Candidate A source set

| Role | Path | Verified fact this dispatch already confirmed |
| --- | --- | --- |
| Owner source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | `ProviderHealthState` (lines 1-6) is exactly `"healthy" \| "degraded" \| "rate_limited" \| "unavailable" \| "unknown"` - five states, no `stale` member |
| Owner tests | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-health.test.ts` | two test cases exercise all five owner states: `unknown` through the default `isUsable` path, `healthy` through `recordSuccess`, and `degraded`, `rate_limited`, and `unavailable` through `recordFailure`; no `stale` state exists |
| Retained PINT source (EXTENSIONS variant) | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE/EXTENSIONS/CVF_PROVIDER_INTELLIGENCE/PROVIDER_HEALTH_PROTOCOL.md` | `## States` block (lines 9-16) lists `healthy, degraded, rate_limited, unavailable, unknown, stale` - six states |
| Retained PINT source (absorption-doc variant) | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE/docs/absorptions/openrouter-provider-intelligence/06_PROVIDER_HEALTH_AND_AVAILABILITY_PROTOCOL.md` | `## 2. Health states` block (lines 9-18) lists the identical six-state set; `## 6. Required fields` (lines 58-80) shows a `provider_health_snapshot.v1` JSON schema with `status`, `latency_ms_p50/p95`, `error_rate_pct`, `rate_limit_status`, and `claim_boundary: "health_snapshot_not_quality_or_governance_proof"` |

### Candidate B source set

| Role | Path | Verified fact this dispatch already confirmed |
| --- | --- | --- |
| Owner source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | `PROVIDER_CAPABILITY_REGISTRY` (lines 70-126) keys models by `providerId`/`modelId` and lists `supportedMethods` drawn from `ProviderMethodName`; no task-type or capability-tag field exists anywhere in the file |
| Owner contract source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | `ProviderMethodName` (lines 1-10) is `"complete" \| "chat" \| "stream" \| "tool_call" \| "reasoning" \| "json_mode" \| "vision" \| "embedding" \| "receipt"` - an I/O-method axis, not a task-classification or capability-tag axis |
| Primary owner tests | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts` | asserts `REVIEW_CVF_PROVIDER_METHODS` equals the method list and exercises method-support assertions per model; no task-type or capability-tag field is asserted |
| Retained PINT source | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE/docs/absorptions/openrouter-provider-intelligence/07_TASK_CAPABILITY_MATRIX_SPEC.md` | `## 3. Task types` (lines 27-45) lists 13 task-type strings (`code_fix` through `non_coder_workflow_execution`); `## 4. Capability tags` (lines 47-64) lists 12 capability-tag strings (`cheap_fast` through `benchmark_supported`); `## 5. Matrix schema` (lines 66-85) shows a rule-based `task_capability_matrix.v1` schema distinct from the owner's per-model method list |

Repository search also finds `ProviderMethodName` or registry references in
`dynamic-model-registry-contract.test.ts`,
`provider-adapter-admission.test.ts`, and
`provider-method-fallback-normalization.test.ts`. The worker must inspect these
secondary tests for axis propagation and independently search for any
additional current references before closing.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| PINT-R1 deferred the health enum with an exact reopen condition | VALUE_SET | `docs/reviews/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_COMPLETION_2026-07-23.md` | Reviewer Semantic Value Audit table | `DEFER_PENDING_OWNER_SOURCE_VERIFICATION` | PINT-R1 completion review | ACCEPT |
| PINT-R1 deferred the task-type/capability-tag vocabulary with an exact reopen condition | VALUE_SET | `docs/reviews/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_COMPLETION_2026-07-23.md` | Reviewer Semantic Value Audit table | `DEFER_PENDING_OWNER_SOURCE_VERIFICATION` | PINT-R1 completion review | ACCEPT |
| Current provider-health owner state enum has five members, not six | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | lines 1-6 | `ProviderHealthState` | `ProviderHealthMonitor` | ACCEPT |
| Current capability registry uses an I/O-method axis, not a task-type/capability-tag axis | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | lines 1-10 | `ProviderMethodName` | `PROVIDER_CAPABILITY_REGISTRY` | ACCEPT |
| Next allowed move authorizes exactly one deferred PINT owner-source comparison | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `nextAllowedMove` | `nextAllowedMove` | active session state registry | ACCEPT |
| PINT-T2 remains the current advisory owner for provider-intelligence claim boundary | VALUE_SET | `docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md` | Owner Surface Matrix | `ProviderHealthMonitor` row; `PROVIDER_CAPABILITY_REGISTRY` row | PINT-T2 reference | ACCEPT |
| PINT-T3 closed the checker-implementation lane with reopen conditions tied to repeated real misses, not to this comparison | VALUE_SET | `docs/reviews/CVF_PINT_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | Remaining Value Matrix | `CLOSE_PINT_ABSORPTION_LANE_NO_CHECKER_NOW` | PINT-T3 review | ACCEPT |

## Mandatory Blind-Spot Control Block

ADIF-0014, ADIF-0020, and ADIF-0021 apply. This tranche compares exactly two
already-identified PINT source files against exactly two already-identified
owner source files; it is not a fresh corpus enumeration and does not reopen
the 50-file PINT-R1 rescan. The worker must not treat this dispatch's own
pre-verified facts above as a substitute for its own independent re-read of
every cited source and retained file; it must re-derive line numbers and
literal enum values itself before writing its comparison matrix, because
line-based citations in a completion review are not self-verifying for a
later artifact.

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE` retained legacy folder (same corpus root PINT-R1 already fully enumerated and reconciled) |
| Enumeration command | N/A with reason: this tranche does not re-enumerate the corpus; it opens exactly three retained files already identified by PINT-R1 rows 7, 24, and 25 |
| Manifest artifact or inline manifest | N/A with reason: no new manifest; PINT-R1's existing 50-row ledger remains the corpus manifest of record |
| Processing ledger artifact or inline ledger | the worker's required inline comparison-matrix table (two rows: candidate A, candidate B) |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE (canonical corpus vocabulary; this tranche's own two-row matrix uses only READ, since both candidates are fully re-read) |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE (canonical corpus vocabulary); this tranche's per-candidate proposed-disposition vocabulary is the narrower `ENRICH_EXISTING`, `NO_NEW_VALUE`, or `DEFER_PENDING_OWNER_SOURCE_VERIFICATION`, which maps onto `ADAPT`, `NO_NEW_VALUE`, and `DEFER` respectively |
| Owner-surface map | `docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md` Owner Surface Matrix |
| Unresolved items | 2 at dispatch; both candidate comparisons remain worker-owned |
| Completion claim boundary | bounded documentation comparison only; no runtime/provider/public/production expansion |

## Corpus Completeness And Report Integrity

- Corpus task class: KNOWLEDGE_ABSORPTION.
- Corpus root: `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE` (bounded
  to exactly the three retained files named in this baseline's Scope /
  Methodology section; the full 50-file corpus was already enumerated and
  reconciled by the prior full-content review, whose manifest remains
  authoritative for the corpus as a whole).
- Snapshot time: 2026-07-25 dispatch authoring.
- Enumeration command: direct filesystem-backed `Test-Path` and file-read
  verification of the two named retained files; no new directory-tree
  enumeration is performed.
- Manifest artifact or inline manifest: the Reopen-Condition Trace and
  Candidate A/B source-set tables above.
- Manifest hash: N/A with reason - this tranche reuses the prior full-content
  review's already-recorded content manifest digest
  `f76e62ab30ba48997fa8d7cb517247ce2afaa1406c51f0e4c0e97edc9369ed85` for the
  corpus as a whole; it does not recompute a new digest for the three-file
  bounded subset.
- Processing ledger artifact or inline ledger: the worker's required two-row
  comparison matrix in the paired work order.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=3; ledger_terminal=0; exclusions=0; unresolved=3.
- Unresolved files: 3 at dispatch (all retained PINT files remain
  worker-owned before execution); worker must recompute after its own read.
- Declared exclusions: none.
- Unreadable or unsupported files: none known.
- Aggregation check: 3 named retained files map to the two candidates.
- Drift check: worker must recompute before and after its own source review.
- Output traceability: each candidate's comparison-matrix row must cite a
  semantic locator (section, line range, or symbol) for every claim.
- Adversarial verification: independent reviewer re-opens all four owner
  source/test files and both retained PINT files before accepting either
  proposed disposition.
- Corpus verdict: PARTIAL

Reviewer verdict note: `PARTIAL` is correct for this pre-execution three-file,
two-candidate subset packet because `ledger_terminal=0` and `unresolved=3`. The prior
PINT-R1 `COMPLETE_VERIFIED` verdict remains authoritative only for the full
50-file corpus and is reused by reference, not copied onto this pending subset.

## Rescan Intelligence Hardening

- Original source artifact: `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE`
  (bounded to the three retained files this tranche compares).
- Predecessor intake artifact:
  `docs/audits/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_AND_MCP_VALUE_RECONCILIATION_2026-07-23.md`
  and
  `docs/reviews/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_COMPLETION_2026-07-23.md`.
- Delta ledger status: see Original-Intake Delta Ledger below.
- Routing matrix status: see Follow-Up Routing Matrix below.
- Semantic sampling status: worker required at execution; not yet performed at
  dispatch authoring.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Current finding | Predecessor finding | Delta class | New disposition | Reason |
| --- | --- | --- | --- | --- |
| this dispatch's own line-cited five-state `ProviderHealthState` enum reading | predecessor row noted six PINT states versus owner source without re-reading the owner enum's exact member count | NEW_FINDING | worker must independently confirm the exact five-versus-six delta | predecessor deferred the comparison rather than performing it |
| this dispatch's own finding that `PROVIDER_CAPABILITY_REGISTRY` uses an I/O-method axis, not a task-type axis | predecessor row noted the task-type/capability-tag vocabulary as a comparison candidate without re-reading the registry's actual field structure | NEW_FINDING | worker must independently confirm the axis mismatch | predecessor deferred the comparison rather than performing it |
| candidate A/B routed from `DEFER_PENDING_OWNER_SOURCE_VERIFICATION` toward a worker-owned `ENRICH_EXISTING`/`NO_NEW_VALUE`/`DEFER_PENDING_OWNER_SOURCE_VERIFICATION` decision point | predecessor left both candidates parked at `DEFER_PENDING_OWNER_SOURCE_VERIFICATION` with no comparison performed | CHANGED_DISPOSITION | this tranche converts the parked defer into an active bounded comparison task with a required evidence-backed proposal | the reopen condition named by the predecessor is exactly what this tranche performs |
| PINT-T2/PINT-T3 owner-surface authority | unchanged predecessor doctrine | UNCHANGED_FROM_INTAKE | retain current owner | no runtime authority expansion |
| direct package/checker import | previously rejected at PINT-T0/PINT-T3 | REMOVED_OR_REJECTED | retain rejection | this tranche does not reopen that decision |

### Follow-Up Routing Matrix

| Finding class | Route | Owner |
| --- | --- | --- |
| candidate A/B comparison-matrix completion | DO_NOW | worker, this dispatch |
| runtime/checker/package implementation of either vocabulary | SEPARATE_RUNTIME_TRANCHE | operator and conditional reopen index |
| final semantic acceptance of either proposed disposition | STRATEGIC_OPERATOR_DECISION | independent reviewer/closer |
| direct package/checker import | OUT_OF_SCOPE | already closed by PINT-T3; not reopened |
| corpus-level manifest/digest re-verification | RESOLVED_BY_DESIGN | prior full-content review's manifest of record |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| R2-S1 | `provider-health.ts` lines 1-6 | `ProviderHealthState` has five members | this dispatch's own re-verified fact | does the owner source actually lack `stale`, or was it missed on a fast read? | CONFIRMED_NEW_DELTA - re-read at dispatch authoring time; worker must independently reconfirm |
| R2-S2 | `provider-method-contract.ts` lines 1-10 | `ProviderMethodName` is an I/O-method axis, not a task-type axis | this dispatch's own re-verified fact | could `vision` (method) be mistaken for `vision_capable` (capability tag) and treated as overlap? | NOT_CONFUSED - the owner field governs which I/O methods a model supports, not a policy-layer task classification; worker must independently reconfirm this distinction is preserved |

## External Absorption Value Conversion Matrix

Lane release state: NOT_RELEASED. The six conversion-lane tokens below provide
mandatory taxonomy coverage only. They do not activate a package, runtime,
checker, owner edit, or implementation candidate.

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| candidate A/B source vocabularies used as comparison inputs | health-state and task/capability vocabulary adapted only into a documentation comparison matrix; no owner enrichment is accepted here | DOCTRINE_ADAPTED | PINT-R2 comparison audit | worker proposes; reviewer decides ENRICH_EXISTING/NO_NEW_VALUE/DEFER | comparison adaptation only; owner source remains unchanged |
| foreign package/checker prototypes referenced by PINT-T0/PINT-T3 | already rejected direct import | REJECT_DIRECT_IMPORT | PINT-T3 checker value decision | retain rejection; not reopened by this tranche | no import |
| duplicate/no-new-value PINT rows already dispositioned by the prior full-content review | no additional delta | NO_PACKAGE_OR_RUNTIME_VALUE | prior full-content review's per-file ledger | closed; not reopened | none |
| candidate A/B vocabulary considered as a reusable schema field set | not proposed as a new contract in this tranche; comparison only | PACKAGE_CANDIDATE | conditional reopen index, only if a later tranche proposes an actual schema/enum change | this dispatch does not activate a package candidate; explicitly out of scope | no activation |
| candidate A/B vocabulary considered as future runtime input | not proposed as a runtime change in this tranche | RUNTIME_CANDIDATE | EAIC knowledge-gap owner and Model Gateway owners, only if a later tranche proposes runtime work | this dispatch does not build runtime; explicitly out of scope | runtime moratorium and existing owner boundaries retained |
| candidate A/B vocabulary considered as a static-check invariant | not proposed as a checker in this tranche | CHECKER_CANDIDATE | PINT-T3 checker value decision owner | reopen only if PINT-T3's own reopen condition (repeated real miss) is separately satisfied | no checker edit |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| six-state provider-health vocabulary (candidate A) | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` `ProviderHealthState` | NEW_FINDING | mechanical count delta confirmed: owner has five states and retained source has six; semantic value remains undecided | worker independently compares; reviewer decides disposition |
| task-type/capability-tag vocabulary (candidate B) | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` and `provider-method-contract.ts` `ProviderMethodName` | NEW_FINDING | mechanical axis delta confirmed: current owner is method-oriented while retained source is task/capability-oriented; semantic value remains undecided | worker independently compares; reviewer decides disposition |
| provider-intelligence advisory doctrine generally | `docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md` | CONFIRMED_EXISTING | current owner-surface authority for both candidates | cite owner; do not duplicate |
| checker-implementation lane | `docs/reviews/CVF_PINT_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | REJECT_DIRECT_IMPORT | no new reason to reopen | preserve closed disposition |

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | retained legacy copied folder (same corpus PINT-R1 already scanned) |
| Upstream or source-mirror disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: this is a bounded three-file, two-candidate owner-source comparison, not a new upstream/network migration claim |
| Enumeration or manifest plan | N/A with reason: no new enumeration; PINT-R1's existing manifest and ledger remain authoritative for the corpus |
| Per-file terminal-ledger plan | exactly one comparison-matrix row per candidate (two rows total) |
| Owner or overlap route | PINT-T2 Owner Surface Matrix; current `ProviderHealthMonitor` and `PROVIDER_CAPABILITY_REGISTRY` owner surfaces |
| Value-disposition route | `ENRICH_EXISTING`, `NO_NEW_VALUE`, or `DEFER_PENDING_OWNER_SOURCE_VERIFICATION` per candidate, reviewer-decided |
| Claim boundary | no implementation, provider, network, public, or external invocation |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | retained source (already manifested by PINT-R1) -> owner-source direct comparison -> per-candidate disposition -> reviewer closure |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this baseline plus existing PINT-T2/PINT-T3 owners |
| Disposition | DEFER pending reviewer decision on both candidates; no ADAPT or REJECT is pre-decided by this dispatch |
| Claim boundary | no runtime/provider/public/production authority; no claim that either vocabulary is now adopted |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`,
lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007, ADIF-0014,
ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024, ADIF-0028,
ADIF-0029, ADIF-0031, ADIF-0033, ADIF-0039, ADIF-0043, ADIF-0044, ADIF-0045,
ADIF-0049

Disposition notes for the defects most relevant to this dispatch's shape:

- ADIF-0014: this dispatch carries the External Repository Absorption Entry
  Control and Blind-Spot Control blocks above because it cites
  `.private_reference/legacy/` paths, even though it is comparison-only.
- ADIF-0020 / ADIF-0021: this dispatch reads applicable checker sources before
  drafting (see Checker Source Read-Ahead Block below) and avoids bare
  applicability-marker overmatch by using `COMPARISON_ONLY_NO_ABSORPTION` and
  `NOT_APPLICABLE_WITH_REASON` narrowly rather than broad absorption prose.
- ADIF-0006: the Source Verification table's `Verified path or symbol` cells
  above use real symbols (`ProviderHealthState`, `ProviderMethodName`,
  `nextAllowedMove`), not filenames or value/type annotations.
- ADIF-0033: no protected path (`governance/compat/*.py`, `CVF_SESSION/**`,
  `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF*.md`) is in this dispatch's Write
  Ownership; no Core Guard Self-Protection Authorization block is required or
  included.
- ADIF-0001 / ADIF-0028 / ADIF-0029 / ADIF-0044 / ADIF-0045 /
  ADIF-0007 / ADIF-0015 / ADIF-0016 / ADIF-0017 / ADIF-0024 / ADIF-0031 /
  ADIF-0039 / ADIF-0043 / ADIF-0049: reviewed; none names a pattern present in
  this bounded two-candidate comparison dispatch (no exhaustive-directory
  claim, no provider-local authority claim, no aggregated-output-exceeds-
  evidence claim, no launch/timeout/CLI-signature claim, no commit-shape
  probing, no stale worker-return evidence).

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| literalTokensReviewed | `Verified path or symbol` real-symbol requirement; non-closed dispatch status; `NOT_APPLICABLE_WITH_REASON` visible-reason requirement; ADIF resolver query exact shape; external-intake path markers |
| gateRunPurpose | confirmation and closure evidence after source read-ahead, not first discovery |
| claimBoundary | structural read-ahead only; semantic completeness and final candidate disposition remain reviewer-owned |

## Acceptance Criteria

- both candidate source sets (owner source, owner tests, retained PINT source)
  are opened and cited with real symbols/line evidence by the worker in its
  own words, not copied verbatim from this baseline;
- the worker's comparison matrix separates vocabulary overlap, semantic
  overlap, runtime representation, behavior actually proved by tests, external
  doctrine not present in the current owner, and unsafe direct-adoption risk,
  per candidate;
- the worker proposes exactly one evidence-backed disposition per candidate
  from `ENRICH_EXISTING`, `NO_NEW_VALUE`, or
  `DEFER_PENDING_OWNER_SOURCE_VERIFICATION`;
- the worker does not edit `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts`,
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`,
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts`, any test
  file, `docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md`,
  any roadmap, or session state;
- no runtime, checker, provider, public, package, CLI/MCP, network, or process
  action occurs;
- worker leaves exactly the two allowed outputs unstaged and uncommitted.

## Verification / Evidence

Dispatch evidence is the source-verification table above, the reopen-condition
trace, the ADIF disclosure, the checker read-ahead block, and the pre-dispatch
gates recorded by this dispatch author. Worker completion evidence must be
command-backed in the audit and worker return; it is not preclaimed by this
baseline.

## Baseline Decision

`DISPATCH_READY_FOR_BOUNDED_OWNER_SOURCE_COMPARISON_PENDING_INDEPENDENT_REVIEW`.

This decision does not adopt either external vocabulary, does not claim CVF
runtime behavior changed, and does not reopen the checker-implementation lane
PINT-T3 closed. Independent reviewer acceptance is required before the future
worker task in the paired work order may execute.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | delegated worker reads local owner and retained PINT source and authors governed comparison documents | no commit; no runtime/external action; no source edit | this baseline and the paired work order | parent session only | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | future EAIC owner | no invocation or adapter execution; explicitly forbidden for this tranche | `docs/reference/external_agent_invocation_control/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_GAP_AND_SOURCE_ACQUISITION_MAP.md` | explicitly deferred pending primary sources and separate operator authorization | DEFERRED_WITH_REASON |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher (this packet's author) -> no-commit worker -> independent reviewer/closer |
| phase | dispatch authoring |
| baseHeadFor(phase) | dispatchBaseHead=`b3f7a14c1` |
| changedSetScope(phase) | exactly this baseline and the paired work order; no other path |
| traceScope(phase, actor) | dispatch author records only its own reads, comparisons, and evidence; the worker and reviewer will record their own separately |
| commitOwner(phase) | N/A at dispatch authoring; the independent reviewer/closer owns any future commit |
| crossBatchIsolation | no runtime, checker, hook, session, roadmap, public-sync, provider, process, or unrelated absorption mutation |
| nextMoveSurfaces | independent reviewer acceptance of this baseline and the paired work order, then worker dispatch |

## Reviewer Closure Conversion

This baseline is not self-closing. Future completion review policy: the
independent reviewer either (a) accepts this baseline and the paired work
order as `DISPATCH_READY` after its own review, then a separate worker session
executes the paired work order and returns `COMPLETE_PENDING_REVIEW`, after
which the reviewer authors `docs/reviews/CVF_PINT_R2_PROVIDER_HEALTH_AND_CAPABILITY_OWNER_SOURCE_COMPARISON_WORKER_RETURN_2026-07-25.md`
review/closure content and decides `ENRICH_EXISTING`, `NO_NEW_VALUE`, or
`DEFER_PENDING_OWNER_SOURCE_VERIFICATION` per candidate; or (b) returns
`REVIEWED_BLOCK_ACCEPTED_R1_REQUIRED`-style findings and requests a repaired
dispatch. This dispatcher does not make that acceptance decision.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance owner-source comparison dispatch; no public-sync is
authorized.

## Claim Boundary

This baseline authorizes only a bounded, documentation-only owner-source
comparison for two named PINT-R1 candidates. It does not authorize runtime
construction, CLI/MCP invocation, provider/API/account use, network access,
process control, checker implementation, package activation, public sync,
routing-behavior change, health/capability enum implementation, model/provider
selection, or a claim that either external vocabulary is now CVF authority. It
does not reopen the EAIC MCP/CLI runtime lane or lift the invocation
moratorium.

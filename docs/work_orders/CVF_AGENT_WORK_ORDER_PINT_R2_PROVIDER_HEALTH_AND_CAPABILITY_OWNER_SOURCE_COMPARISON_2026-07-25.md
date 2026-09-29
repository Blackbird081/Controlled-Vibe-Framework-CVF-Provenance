# CVF Agent Work Order - PINT-R2 Provider Health And Capability Owner Source Comparison

Memory class: POINTER_RECORD

Status: REVIEWER_ACCEPTED_DISPATCH_READY_WITH_REPAIRS

Batch ID: PINT-R2

Dispatch base head: `b3f7a14c1`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated documentation worker

Reviewer/closer: independent reviewer/closer

Worker return path:
`docs/reviews/CVF_PINT_R2_PROVIDER_HEALTH_AND_CAPABILITY_OWNER_SOURCE_COMPARISON_WORKER_RETURN_2026-07-25.md`

## Dispatch Prompt Envelope

Role: delegated no-commit documentation worker. A separate independent
reviewer/closer owns acceptance and any final semantic disposition.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_PINT_R2_PROVIDER_HEALTH_AND_CAPABILITY_OWNER_SOURCE_COMPARISON_2026-07-25.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture `git rev-parse --short HEAD` before edits; it must
equal the exact execution head supplied by the operator with this prompt.

Current-time notes: no live key, provider, account, subscription, network,
browser, external CLI/MCP invocation, or process-control action is authorized.

Do-not-misread notes: this is a two-candidate local source-to-owner comparison,
not authorization to implement a health/capability enum, activate a package, or
build MCP/CLI control runtime. Internal Explore, Read, Grep, and Glob helpers
inside the parent worker session are allowed and inherit the parent
internal-agent boundary.

Required first actions: read `CVF_SESSION_MEMORY.md`, resolve
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, read its active handoff,
`docs/reference/guard_orientation/README.md`, the paired GC-018 baseline, this
work order, literal gotchas, and all checker sources in the read-ahead block;
then verify HEAD, clean worktree, and all eleven named source/test files.

Return contract: return `COMPLETE_PENDING_REVIEW` only with exact changed
paths, executionBaseHead, complete comparison matrix for both candidates, one
proposed disposition per candidate, gate results, empty staged diff, and
unchanged HEAD. Otherwise return `BLOCKED_WITH_REASON`.

## Purpose

Build an exact source-to-owner comparison matrix for the two PINT-R1 candidates
whose reopen condition is now satisfiable: the six-state provider-health
vocabulary versus current `ProviderHealthMonitor`, and the task-type/
capability-tag vocabulary versus current `PROVIDER_CAPABILITY_REGISTRY`. Give
one evidence-backed proposed disposition per candidate. Leave final semantic
acceptance to the independent reviewer/closer.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | manual authoring from PINT-R1 work-order structural precedent (`docs/work_orders/CVF_AGENT_WORK_ORDER_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_AND_MCP_VALUE_RECONCILIATION_2026-07-23.md`) |
| generatedProfile | source-intake plus no-commit worker profile, narrowed to a two-candidate comparison |
| generatedSkeletonStatus | MANUAL_TEMPLATE_ADAPTATION |
| manualEditsAfterScaffold | replaced corpus-rescan scope with two-candidate owner-source comparison scope; replaced 50-row ledger requirements with a two-row comparison matrix requirement |
| checkerReadAheadConfirmation | all checker paths listed in the read-ahead block |
| docOnlyNewFields | comparison-matrix columns: vocabulary overlap, semantic overlap, runtime representation, test-proved behavior, external-doctrine-not-present, unsafe-direct-adoption-risk |
| claimBoundary | dispatch provenance only; no runtime/provider/live/public/MCP behavior |

## Authority Chain

- Operator instruction: dispatch-author task naming PINT-R2 as the explicitly
  authorized deferred PINT owner-source comparison.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
  (`nextAllowedMove` names this exact comparison as an available checkpoint).
- Active handoff: resolved from the active session state
  (`AGENT_HANDOFF_V51_2026-07-22.md`).
- Paired GC-018:
  `docs/baselines/CVF_GC018_PINT_R2_PROVIDER_HEALTH_AND_CAPABILITY_OWNER_SOURCE_COMPARISON_2026-07-25.md`.
- Predecessor evidence:
  `docs/audits/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_AND_MCP_VALUE_RECONCILIATION_2026-07-23.md`
  and
  `docs/reviews/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_COMPLETION_2026-07-23.md`.
- Existing doctrine owner:
  `docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md`.
- Existing checker decision:
  `docs/reviews/CVF_PINT_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`.

Authority boundary: this work order does not authorize work outside the cited
authority chain. If any authority artifact conflicts with this work order,
stop and reconcile before implementation.

## Agent Roles

- Orchestrator / dispatcher: dispatcher role (this packet's author).
- Implementer: delegated worker role.
- Reviewer: independent reviewer/closer role.
- Operator approval required for: any scope expansion beyond the two named
  candidates, runtime/checker/package implementation, or moratorium release.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | two deferred PINT-R1 candidates with explicit current-owner source-verification reopen conditions |
| Dispatcher role | authors and source-verifies the bounded packet |
| Worker role | independently re-reads the eleven-file source/test set and authors exactly two documentation outputs |
| Reviewer role | independently decides semantic acceptance, repairs bounded packet defects, and owns commit/closure |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | dispatcher -> no-commit worker -> independent reviewer/closer |
| escalation condition | stop for missing source, owner conflict, scope expansion, runtime/checker/package work, external invocation, provider/network/process action, or public action |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
| --- | --- |
| Legacy coverage applicability | NOT_APPLICABLE_WITH_REASON |
| Reason | PINT-R2 compares three files already covered by the accepted PINT-R1 50-file manifest; it does not add, remove, or rescan corpus coverage. |
| Coverage-index relationship | reuse PINT-R1 registry and manifest evidence without changing the coverage index |
| Legacy source search boundary | exactly three retained source files plus eight current owner source/test files; no broad legacy scan |

## Scope

Allowed scope:

- open and re-read all eleven files in the Required First-Read Table, then
  repeat the repository search for any additional test file that references
  `ProviderHealthMonitor`, `PROVIDER_CAPABILITY_REGISTRY`, or
  `ProviderMethodName`, to confirm or correct this dispatch's facts;
- build the required comparison matrix for both candidates;
- propose exactly one disposition per candidate;
- author exactly the two Allowed Outputs below.

Forbidden scope:

- editing `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts`,
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`,
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts`, or any test
  file;
- editing PINT-T2, PINT-T3, any roadmap, session state, or handoff;
- adopting an enum, activating a package, implementing a checker, or making a
  runtime/production claim;
- any provider/API/account/network/browser/external CLI/MCP action.

Risk ceiling:

- R0

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`worker`,
lifecyclePhase=`pre-implementation`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007, ADIF-0014,
ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024, ADIF-0028,
ADIF-0029, ADIF-0031, ADIF-0033, ADIF-0039, ADIF-0043, ADIF-0044, ADIF-0045,
ADIF-0049 (the same 20-entry set the dispatch author's own pre-dispatch query
returned for `role=dispatcher`; the resolver's `Work-order authoring /
dispatch` taskClass entries are not role-partitioned in the current registry,
so `role=worker` returns the identical 20 defectIds).

- ADIF-0014: the worker must not treat this dispatch's or the reviewer's prior
  citations as a substitute for independently re-opening all eleven named
  files.
- ADIF-0006: the worker's own Source Verification / comparison-matrix cells
  must name real symbols (for example `ProviderHealthState`,
  `ProviderMethodName`), never a bare filename or a value/type annotation.
- ADIF-0024: the worker must record current, re-run gate evidence at
  `COMPLETE_PENDING_REVIEW`, not stale evidence copied from this dispatch.
- Remaining returned defectIds reviewed; none names a pattern applicable to
  this bounded two-candidate comparison beyond the above.

## Required First Reads

1. Startup and guard-orientation files named in the envelope.
2. Paired PINT-R2 GC-018 and this work order.
3. `docs/audits/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_AND_MCP_VALUE_RECONCILIATION_2026-07-23.md`
   rows 7 and 24 (health) and row 25 (capability), and
   `docs/reviews/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_COMPLETION_2026-07-23.md`
   Reviewer Semantic Value Audit table - why this matters: these are the exact
   reopen conditions this dispatch satisfies.
4. `docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md`
   Owner Surface Matrix - why this matters: current owner-surface authority for
   both candidates.
5. All eleven files in the Required First-Read Table below.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
Test-Path "EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts"
Test-Path "EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts"
Test-Path ".private_reference/legacy/CVF_PROVIDER_INTELLIGENCE/EXTENSIONS/CVF_PROVIDER_INTELLIGENCE/PROVIDER_HEALTH_PROTOCOL.md"
Test-Path ".private_reference/legacy/CVF_PROVIDER_INTELLIGENCE/docs/absorptions/openrouter-provider-intelligence/07_TASK_CAPABILITY_MATRIX_SPEC.md"
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base b3f7a14c1 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base b3f7a14c1 --head HEAD --enforce
python governance/compat/check_adif_defect_registry_disclosure.py --base b3f7a14c1 --head HEAD --enforce
```

Expected results:

- worktree clean before worker edits;
- all four `Test-Path` checks return `True`;
- pre-implementation autorun phase gate PASS.

If a pre-flight check fails, stop and record the failed command and result.
The worker must not continue past a failed autorun phase gate.

## Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside this work order's Allowed scope: reading the named files, running
`git status`/`git diff`/`git rev-parse`, running listed governance gates, and
allowed-scope documentation remediation. Escalation is reserved for actions
that would exceed Allowed scope, edit any source/test file, run live/provider
proof, use secrets/quota, public-sync, change risk or claim boundary, or
perform a destructive/irreversible action.

## Write Ownership

Exactly these two Allowed Outputs:

1. create
   `docs/audits/CVF_PINT_R2_PROVIDER_HEALTH_AND_CAPABILITY_OWNER_SOURCE_COMPARISON_2026-07-25.md`;
2. create
   `docs/reviews/CVF_PINT_R2_PROVIDER_HEALTH_AND_CAPABILITY_OWNER_SOURCE_COMPARISON_WORKER_RETURN_2026-07-25.md`.

No other path may change. Do not stage or commit.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| current provider-health state enum has five members | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | lines 1-6 | `ProviderHealthState` | `ProviderHealthMonitor` | ACCEPT |
| current provider-health tests exercise all five owner states | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-health.test.ts` | lines 4-26 | `ProviderHealthMonitor` test suite | `ProviderHealthMonitor` | ACCEPT |
| retained PINT health protocol lists six states including `stale` | EXISTS | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE/EXTENSIONS/CVF_PROVIDER_INTELLIGENCE/PROVIDER_HEALTH_PROTOCOL.md` | lines 9-16 | `## States` block | retained PINT source | ACCEPT |
| retained PINT absorption doc confirms the same six-state set with a JSON schema | EXISTS | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE/docs/absorptions/openrouter-provider-intelligence/06_PROVIDER_HEALTH_AND_AVAILABILITY_PROTOCOL.md` | lines 9-18, 58-80 | `## 2. Health states`; `## 6. Required fields` | retained PINT source | ACCEPT |
| current capability registry uses an I/O-method axis | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | lines 1-10 | `ProviderMethodName` | `PROVIDER_CAPABILITY_REGISTRY` | ACCEPT |
| current capability registry tests assert the nine-method matrix axis, not a task-type axis | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts` | lines 22-33 | `REVIEW_CVF_PROVIDER_METHODS` | `PROVIDER_CAPABILITY_REGISTRY` | ACCEPT |
| retained PINT task-capability spec lists 13 task types and 12 capability tags | EXISTS | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE/docs/absorptions/openrouter-provider-intelligence/07_TASK_CAPABILITY_MATRIX_SPEC.md` | lines 27-45, 47-64 | `## 3. Task types`; `## 4. Capability tags` | retained PINT source | ACCEPT |

## Required First-Read Table

| Field | Requirement |
| --- | --- |
| owner source A | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` |
| owner tests A | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-health.test.ts` |
| PINT source A (protocol) | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE/EXTENSIONS/CVF_PROVIDER_INTELLIGENCE/PROVIDER_HEALTH_PROTOCOL.md` |
| PINT source A (absorption doc) | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE/docs/absorptions/openrouter-provider-intelligence/06_PROVIDER_HEALTH_AND_AVAILABILITY_PROTOCOL.md` |
| owner source B | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` |
| owner contract source B | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` |
| owner tests B | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts` |
| secondary owner test B1 | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/dynamic-model-registry-contract.test.ts` |
| secondary owner test B2 | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-admission.test.ts` |
| secondary owner test B3 | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-method-fallback-normalization.test.ts` |
| PINT source B | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE/docs/absorptions/openrouter-provider-intelligence/07_TASK_CAPABILITY_MATRIX_SPEC.md` |

## Scope / Methodology

1. Re-open all eleven files in the Required First-Read Table with the worker's
   own read, independent of this dispatch's pre-recorded facts.
2. For candidate A, build a comparison row separating: vocabulary overlap
   (which literal state names match); semantic overlap (does `stale` describe
   a concept the owner source handles differently, e.g. via `lastSuccessAt`/
   `lastFailureAt` timestamps rather than a named state); runtime
   representation (`ProviderHealthState` union vs. PINT's flat six-item list);
   behavior actually proved by tests (which of the five owner states currently
   have test coverage); external doctrine not present in the owner (`stale`,
   TTL-based staleness, the five-item fail-closed routing-rule list, the JSON
   snapshot schema); unsafe direct-adoption risk (would adding `stale` require
   a TTL/timestamp policy the owner does not yet define elsewhere).
3. For candidate B, build a comparison row separating: vocabulary overlap
   (none - zero literal task-type or capability-tag strings appear in the
   owner source); semantic overlap (does `ProviderMethodName` express any of
   the same intent as a task-type/capability-tag, e.g. `vision` method vs.
   `vision_capable` tag); runtime representation (per-model `supportedMethods`
   array vs. PINT's rule-based `task_capability_matrix.v1` schema keyed by
   `task_type`); behavior actually proved by tests (method-support assertions
   only); external doctrine not present in the owner (task classification by
   workflow phase/risk/reasoning depth/context length, the full 13-task-type
   and 12-capability-tag vocabulary, the `PROVIDER_CAPABILITY_OWNER_REFS` for
   retry/cost/risk are a partial but distinct existing owner-reference
   pattern); unsafe direct-adoption risk (task-type classification is a
   policy-layer concept the current registry does not attempt, so importing it
   directly would blur the registry's narrow method-support purpose).
4. Propose exactly one disposition per candidate from `ENRICH_EXISTING`,
   `NO_NEW_VALUE`, or `DEFER_PENDING_OWNER_SOURCE_VERIFICATION`, each with an
   explicit evidence citation for why that disposition, not another, was
   chosen.
5. Do not silently upgrade either proposal into an implementation
   recommendation; state disposition and evidence only.

## Execution Plan

1. Verify startup state, execution head, clean worktree, and all four
   `Test-Path` checks.
2. Re-read all eleven files in the Required First-Read Table.
   - Input: the eleven named files.
   - Output: worker's own line-cited notes.
   - Validation: each cited line/section matches current file content.
   - Stop condition: any named file is missing or unreadable.
3. Build the two-row comparison matrix per the Scope / Methodology section.
   - Input: worker's own read notes.
   - Output: comparison matrix in the audit.
   - Validation: matrix separates all six required dimensions per candidate.
   - Stop condition: any dimension cannot be evidenced from the named files.
4. Propose one disposition per candidate.
   - Input: comparison matrix.
   - Output: Proposed Disposition table in the audit.
   - Validation: each disposition cites specific evidence, not summary prose.
   - Stop condition: evidence does not clearly support any of the three
     allowed disposition tokens.
5. Author the audit and worker return, run required gates, repair
   allowed-scope defects, and stop with the required return token.
   - Input: comparison matrix and proposed dispositions.
   - Output: both Allowed Outputs.
   - Validation: `run_worker_return_fast_gate.py` PASS.
   - Stop condition: any required gate fails outside Allowed scope.

Each step stops on unreadable source, authority conflict, or need for a
forbidden action.

## Required Audit Sections

The audit (`docs/audits/CVF_PINT_R2_PROVIDER_HEALTH_AND_CAPABILITY_OWNER_SOURCE_COMPARISON_2026-07-25.md`)
must contain real sections for:

- Target / Source;
- Scope / Methodology;
- Findings / Position;
- Risk / Corrective Action;
- Source Verification Block (worker's own re-verified version);
- Candidate A Comparison Matrix;
- Candidate B Comparison Matrix;
- Proposed Disposition;
- External Absorption Core (comparison-only disposition);
- Corpus Completeness And Report Integrity for the exact three-file retained
  subset; use `COMPLETE_VERIFIED` only when all three files have terminal
  ledger evidence and unresolved=0, while keeping PINT-R1 authoritative for
  the full 50-file corpus;
- Rescan Intelligence Hardening (`NOT_APPLICABLE_WITH_REASON`, not a rescan);
- External Knowledge Intake Routing;
- Epistemic Process Block;
- Finding-To-Governance Learning Disposition;
- Agent Operation Trace Block;
- Public Export Disposition;
- Claim Boundary.

Do not write heading-prefixed checklist literals before the actual sections.

## New Doc-Only Fields

| Field | Purpose | Runtime status |
| --- | --- | --- |
| vocabulary overlap | literal string-level match between PINT and owner vocabularies | documentation only |
| semantic overlap | conceptual match even without literal string match | documentation only |
| runtime representation | how each side actually encodes the concept in code/schema | documentation only |
| test-proved behavior | which owner states/methods currently have test coverage | documentation only |
| external doctrine not present in owner | PINT concepts the owner has no equivalent for today | documentation only |
| unsafe direct-adoption risk | why naive adoption could create policy gaps the owner does not yet define | documentation only |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| target audit and worker-return path collision | pre-authoring `Test-Path` on both Allowed Output paths returned false | ACCEPT |
| additional capability-registry test coverage | three secondary capability test files are named in the Required First-Read Table; worker must repeat the repository search and record any further matches | ACCEPT_PENDING_WORKER_CONFIRMATION |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact:
`docs/reviews/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_COMPLETION_2026-07-23.md`

priorVerificationAnchor: Reviewer Semantic Value Audit table rows for the
six-state health enum and the task-type/capability-tag vocabulary

recomputeReason: PINT-R1 identified the retained source files and deferred
comparison; it did not itself open and compare the current owner source files
line-by-line

freshRecomputeRequired: YES; all eleven named files must be independently
re-opened by the worker

unicodePathHandling: use literal repository-relative paths and UTF-8-safe text
readers; do not normalize source filenames

extractedTextAuthority: AUXILIARY_ONLY

The retained PINT source files remain external evidence; current owner source
files (`.ts`) remain CVF runtime authority.

## Mandatory Blind-Spot Control Block

ADIF-0014 applies. The worker must not treat this dispatch's own pre-verified
facts, or the PINT-R1 audit's summary text, as a substitute for its own
independent re-read of all eleven named files.

## Corpus Completeness And Report Integrity

- Corpus task class: KNOWLEDGE_ABSORPTION.
- Corpus root: `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE` (bounded
  to exactly the three retained files named in the Required First-Read Table
  above; the full 50-file corpus was already enumerated and reconciled by the
  prior full-content review, whose manifest remains authoritative for the
  corpus as a whole).
- Snapshot time: worker execution timestamp.
- Enumeration command: direct filesystem-backed `Test-Path` and file-read
  verification of the three named retained files plus the eight named owner
  source/test files; no new directory-tree enumeration is performed.
- Manifest artifact or inline manifest: the Required First-Read Table above.
- Manifest hash: N/A with reason - this work order reuses the prior
  full-content review's already-recorded content manifest digest
  `f76e62ab30ba48997fa8d7cb517247ce2afaa1406c51f0e4c0e97edc9369ed85` for the
  corpus as a whole; it does not recompute a new digest for the three-file
  bounded subset.
- Processing ledger artifact or inline ledger: the worker's required two-row
  comparison matrix (Candidate A Comparison Matrix, Candidate B Comparison
  Matrix) in the audit.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=3; ledger_terminal=0; exclusions=0; unresolved=3.
- Unresolved files: 3 at dispatch; worker must recompute after its own read.
- Declared exclusions: none.
- Unreadable or unsupported files: none known.
- Aggregation check: 3 named retained files map to the two candidates.
- Drift check: worker must recompute before and after its own source review.
- Output traceability: each candidate's comparison-matrix row must cite a
  semantic locator for every claim.
- Adversarial verification: independent reviewer re-opens all four owner
  source/test files and both retained PINT files before accepting either
  proposed disposition.
- Corpus verdict: PARTIAL

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | retained legacy copied folder (same corpus PINT-R1 already scanned) |
| Upstream or source-mirror disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: this is a bounded three-file, two-candidate owner-source comparison, not a new upstream/network migration claim |
| Enumeration or manifest plan | N/A with reason: no new enumeration; PINT-R1's existing manifest and ledger remain authoritative for the corpus |
| Per-file terminal-ledger plan | exactly one comparison-matrix row per candidate (two rows total) |
| Owner or overlap route | PINT-T2 Owner Surface Matrix; current `ProviderHealthMonitor` and `PROVIDER_CAPABILITY_REGISTRY` owner surfaces |
| Value-disposition route | `ENRICH_EXISTING`, `NO_NEW_VALUE`, or `DEFER_PENDING_OWNER_SOURCE_VERIFICATION` per candidate, reviewer-decided |
| Claim boundary | no implementation, provider, network, public, or external invocation; disposition COMPARISON_ONLY_NO_ABSORPTION |

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE` (same corpus PINT-R1 already fully scanned) |
| Enumeration command | N/A with reason: no new enumeration; exactly two named retained files are opened |
| Manifest artifact or inline manifest | N/A with reason: PINT-R1's existing 50-row ledger remains the corpus manifest of record |
| Processing ledger artifact or inline ledger | the worker's required inline two-row comparison-matrix table |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE (canonical corpus vocabulary; the worker's own two-row matrix uses only READ, since both candidates are fully re-read) |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE (canonical corpus vocabulary); the worker's per-candidate proposed-disposition vocabulary is the narrower `ENRICH_EXISTING`, `NO_NEW_VALUE`, or `DEFER_PENDING_OWNER_SOURCE_VERIFICATION`, mapping onto `ADAPT`, `NO_NEW_VALUE`, and `DEFER` respectively |
| Owner-surface map | `docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md` Owner Surface Matrix |
| Unresolved items | worker must state exact count after its own re-verification |
| Completion claim boundary | bounded documentation comparison only |

## External Absorption Value Conversion Matrix

Lane release state: NOT_RELEASED. The six conversion-lane tokens below provide
mandatory taxonomy coverage only. They do not activate a package, runtime,
checker, owner edit, or implementation candidate.

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| candidate A/B source vocabularies used as comparison inputs | health-state and task/capability vocabulary adapted only into a documentation comparison matrix; no owner enrichment is accepted here | DOCTRINE_ADAPTED | PINT-R2 comparison audit | worker proposes; reviewer decides ENRICH_EXISTING/NO_NEW_VALUE/DEFER | comparison adaptation only; owner source remains unchanged |
| foreign package/checker prototypes referenced by PINT-T0/PINT-T3 | already rejected direct import | REJECT_DIRECT_IMPORT | PINT-T3 checker value decision | retain rejection; not reopened by this tranche | no import |
| duplicate/no-new-value PINT rows already dispositioned by the prior full-content review | no additional delta | NO_PACKAGE_OR_RUNTIME_VALUE | prior full-content review's per-file ledger | closed; not reopened | none |
| candidate A/B vocabulary considered as a reusable schema field set | not proposed as a new contract in this work order; comparison only | PACKAGE_CANDIDATE | conditional reopen index, only if a later tranche proposes an actual schema/enum change | this work order does not activate a package candidate; explicitly out of scope | no activation |
| candidate A/B vocabulary considered as future runtime input | not proposed as a runtime change in this work order | RUNTIME_CANDIDATE | EAIC knowledge-gap owner and Model Gateway owners, only if a later tranche proposes runtime work | this work order does not build runtime; explicitly out of scope | runtime moratorium and existing owner boundaries retained |
| candidate A/B vocabulary considered as a static-check invariant | not proposed as a checker in this work order | CHECKER_CANDIDATE | PINT-T3 checker value decision owner | reopen only if PINT-T3's own reopen condition (repeated real miss) is separately satisfied | no checker edit |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| six-state provider-health vocabulary (candidate A) | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` `ProviderHealthState` | NEW_FINDING | mechanical count delta confirmed; semantic value remains undecided | worker independently compares; reviewer decides disposition |
| task-type/capability-tag vocabulary (candidate B) | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` and `provider-method-contract.ts` `ProviderMethodName` | NEW_FINDING | mechanical axis delta confirmed; semantic value remains undecided | worker independently compares; reviewer decides disposition |
| provider-intelligence advisory doctrine generally | `docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md` | CONFIRMED_EXISTING | current owner-surface authority for both candidates | cite owner; do not duplicate |
| checker-implementation lane | `docs/reviews/CVF_PINT_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | REJECT_DIRECT_IMPORT | no new reason to reopen | preserve closed disposition |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | retained source (already manifested by PINT-R1) -> owner-source direct comparison -> per-candidate disposition -> reviewer closure |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this audit plus PINT-T2/PINT-T3 owners |
| Disposition | DEFER pending reviewer decision on both candidates |
| Claim boundary | no runtime/provider/public/production authority |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| compare six-state health vocabulary against `ProviderHealthMonitor` | Scope / Methodology step 2 | Candidate A Comparison Matrix | worker's own re-read of `provider-health.ts` and both PINT sources | PASS |
| compare task-type/capability-tag vocabulary against `PROVIDER_CAPABILITY_REGISTRY` | Scope / Methodology step 3 | Candidate B Comparison Matrix | worker's own re-read of current registry, contract, tests, and retained source | PASS |
| decide `ENRICH_EXISTING` / `NO_NEW_VALUE` / `DEFER_PENDING_OWNER_SOURCE_VERIFICATION` per candidate | Scope / Methodology step 4 | Proposed Disposition table | evidence citation required for each disposition | PASS |
| do not edit owner runtime/source, adopt enum, activate package, implement checker | Scope Forbidden scope | Claim Boundary section | changed set restricted to two documentation outputs | PASS |
| leave final semantic acceptance to reviewer | Reviewer Closure Conversion | worker return status `COMPLETE_PENDING_REVIEW` | reviewer authors closure | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | parent worker session using local read/search helpers | no commit or external action; no source/test edit | worker trace and Git evidence | internal helpers inherit parent boundary | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | future EAIC adapter owner | invocation explicitly forbidden for this tranche | `docs/reference/external_agent_invocation_control/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_GAP_AND_SOURCE_ACQUISITION_MAP.md` | no adapter execution; fresh source-verified tranche required | DEFERRED_WITH_REASON |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `Verified path or symbol` real-symbol requirement; `NOT_APPLICABLE_WITH_REASON` visible-reason requirement; `Resolver query: taskClass=`...`, role=`...`, lifecyclePhase=`...`` exact regex shape; review-type five structural heading groups (target/source, scope/methodology, findings/position, risk/corrective action, decision/disposition); `## Execution Plan` requirement for work orders |
| gateRunPurpose | confirmation and evidence after source/checker read-ahead |
| claimBoundary | structural compliance support; not semantic proof |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher/reviewer -> no-commit worker -> independent closer |
| phase | documentation execution released after independent review; review, commit, continuity, runtime, and external action held |
| baseHeadFor(phase) | dispatchBaseHead=`b3f7a14c1`; executionBaseHead=operator-supplied committed dispatch head; closureBaseHead=reviewer-captured |
| changedSetScope(phase) | exactly two Allowed Outputs |
| traceScope(phase, actor) | each actor records only its own reads, edits, helpers, commands, and gates |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | no source, runtime, checker, hook, session, handoff, roadmap, public-sync, or unrelated absorption changes |
| nextMoveSurfaces | reviewer updates continuity only after accepted material commit |

Before status evidence: worktree clean at dispatch authoring base
`b3f7a14c1`; worker must independently prove a clean worktree before edits.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | reviewer decides whether a dedicated completion review is required, or whether the worker return plus reviewer-owned repairs are sufficient closure evidence per gotcha 30 |
| reviewerOwnedClosurePaths | paired baseline, this work order, accepted worker outputs, and (if required) a dedicated completion review |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Durable owner | existing `docs/audits/` and `docs/reviews/` path families |
| New stable folder | N/A with reason: no new foundation folder is created |
| Generated aggregate | N/A with reason: this tranche does not regenerate the corpus scan registry aggregate |
| Generator | N/A with reason: no generator is invoked by this tranche |
| Front door | existing PINT-T2/PINT-T3 owner surfaces |
| Maintainability boundary | audit and worker return remain two separate files; no monolithic owner or runtime surface is opened |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| PINT-R2 audit | create two-candidate comparison matrix and Proposed Disposition table |
| worker return | create complete no-commit evidence packet |

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `docs/audits/CVF_PINT_R2_PROVIDER_HEALTH_AND_CAPABILITY_OWNER_SOURCE_COMPARISON_2026-07-25.md` | Yes | comparison matrix and evidence-backed proposed dispositions |
| `docs/reviews/CVF_PINT_R2_PROVIDER_HEALTH_AND_CAPABILITY_OWNER_SOURCE_COMPARISON_WORKER_RETURN_2026-07-25.md` | Yes | no-commit worker-return evidence packet |

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | owner runtime source; comparison target, not edit target |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | owner runtime source; comparison target, not edit target |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | owner runtime source; comparison target, not edit target |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/**` | owner test source; read-only reference |
| `docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md` | existing owner reference; enrichment decision is reviewer-owned, not worker-owned |
| `governance/compat/*.py` | protected checker path; not authorized in this dispatch |
| `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF*.md` | protected session/handoff paths; not authorized in this dispatch |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
| --- | --- | --- | --- |
| `docs/audits/CVF_PINT_R2_PROVIDER_HEALTH_AND_CAPABILITY_OWNER_SOURCE_COMPARISON_2026-07-25.md` | ABSENT | ABSENT (verified by this dispatch author) | N/A |
| `docs/reviews/CVF_PINT_R2_PROVIDER_HEALTH_AND_CAPABILITY_OWNER_SOURCE_COMPARISON_WORKER_RETURN_2026-07-25.md` | ABSENT | ABSENT (verified by this dispatch author) | N/A |

## Worker Return Packet Shape Contract

workerReturnPath:
`docs/reviews/CVF_PINT_R2_PROVIDER_HEALTH_AND_CAPABILITY_OWNER_SOURCE_COMPARISON_WORKER_RETURN_2026-07-25.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Before authoring, generate or inspect the current checker-safe worker-return
skeleton and read checker sources as applied to both worker-owned Markdown
outputs.

## Evidence Requirements

Required evidence:

- exact `git rev-parse --short HEAD` and `git status --short` before and after
  edits;
- eleven named files independently re-read with line-cited evidence;
- complete comparison matrix for both candidates across all six required
  dimensions;
- one evidence-backed proposed disposition per candidate;
- complete Agent Operation Trace Block for the worker return.

Evidence Trace Block requirements:

- Claim: `ProviderHealthState` currently has five members, not six
- Command: direct file read of `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts`
- Result: `"healthy" | "degraded" | "rate_limited" | "unavailable" | "unknown"`
- Key path: `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts:1-6`
- Verdict: ACCEPT

Base-anchor evidence:

- `dispatchBaseHead`: `b3f7a14c1`
- `executionBaseHead`: operator-supplied committed dispatch head
- `closureBaseHead`: N/A - pending review
- Commit mode: `WORKER_MUST_NOT_COMMIT`
- Worker-return fast gate:
  `python governance/compat/run_worker_return_fast_gate.py`
- Committed-range `pre-closure`: N/A - pending review

## Acceptance Criteria

- [ ] both candidate source sets are re-opened and cited with real
  symbols/line evidence by the worker in its own words;
- [ ] the comparison matrix separates vocabulary overlap, semantic overlap,
  runtime representation, test-proved behavior, external doctrine not present
  in owner, and unsafe direct-adoption risk, per candidate;
- [ ] exactly one evidence-backed disposition is proposed per candidate;
- [ ] no source/test/reference/session/handoff/checker path is edited;
- [ ] no runtime, checker, provider, public, package, CLI/MCP, network, or
  process action occurs;
- [ ] exactly two Allowed Outputs exist, nothing staged, HEAD unchanged;
- [ ] required worker gates pass.

Fail conditions:

- [ ] any named source file is missing, moved, or unreadable;
- [ ] a comparison dimension is asserted without a specific line/section
  citation from a re-opened file;
- [ ] a proposed disposition claims runtime/production behavior or implies
  adoption has occurred;
- [ ] the worker edits any forbidden path;
- [ ] the worker attempts external invocation, provider/API/account/network/
  browser access, or process control.

Closure is blocked if any fail condition is present.

## Review Gate

Implementation may proceed only after:

- independent reviewer accepts this GC-018 baseline and this work order as
  `DISPATCH_READY`
- `pre-dispatch` autorun gate passed before dispatch
- `pre-implementation` autorun gate passed before material edits

Closure may proceed only after:

- reviewer no-blocking objection or explicit repair-and-reaccept
- `pre-closure` autorun gate passed and result recorded

For `WORKER_MUST_NOT_COMMIT` mode, worker handoff is not closure. The reviewer
or committer must approve disposition, commit the reviewed owned diff, and run
the committed-range `pre-closure` gate before changing status to a
closed-equivalent value.

## Verification Commands

```powershell
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --check
git diff --cached --name-status
git status --short --untracked-files=all
git rev-parse --short HEAD
```

Do not run pre-closure, commit steward closure mode, push, provider, API, or
external invocation commands.

## Closure Checklist

- [ ] All acceptance criteria satisfied or explicitly marked N/A with reason
- [ ] Required tests or evidence commands run
- [ ] Autorun `pre-closure` gate passed (post-review, not at dispatch)
- [ ] Commit mode recorded as `WORKER_MUST_NOT_COMMIT`
- [ ] `dispatchBaseHead`, `executionBaseHead`, and closure-stage base evidence
  recorded without treating a stale dispatch anchor as current worker proof
- [ ] For `WORKER_MUST_NOT_COMMIT`, pending handoff used a non-closed status,
  recorded actual `git status --short`, and left committed-range
  `pre-closure` to reviewer / committer
- [ ] Worker-return fast gate result is recorded
- [ ] Agent Operation Trace Block is present and complete
- [ ] Changed-file set from `git diff --name-status` is inside this work
  order's Allowed scope
- [ ] Roadmap-to-work-order trace matrix final statuses are PASS or N/A with
  reason
- [ ] Fail conditions checked and absent, or work returned BLOCKED
- [ ] No open checkbox residue remains once closed

## Return-To-Orchestrator Conditions

Return to orchestrator without continuing if:

- pre-flight fails;
- any autorun phase gate fails outside Allowed scope or cannot be repaired
  inside this work order;
- source-fidelity pass finds a missing path, invented symbol, or unverified
  claim;
- scope conflict is discovered;
- implementation would exceed the R0 risk ceiling;
- reviewer raises a structural blocking objection;
- any named source file has drifted from the evidence cited in this work
  order in a way that changes the comparison conclusion.

## Operator Checkpoint

No further operator question is needed for this bounded two-candidate
comparison. Fresh operator authorization is mandatory before enum
implementation, package activation, checker implementation, or any runtime,
provider, public, or process action.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher role |
| Provider or surface | local provenance workspace |
| Session or invocation | PINT-R2 dispatch authoring, 2026-07-25 |
| Working directory | repository root |
| Command or tool surface | local reads, `Test-Path`/`Read` verification, governance gates |
| Target paths | paired PINT-R2 baseline and this work order |
| Allowed scope source | `CVF_SESSION/ACTIVE_SESSION_STATE.json` `nextAllowedMove` explicitly authorizing this exact deferred PINT owner-source comparison |
| Before status evidence | clean worktree at HEAD `b3f7a14c1` |
| After status evidence | independently reviewed and dispatch-ready with bounded reviewer repairs; material commit pending |
| Diff evidence | `git status --short` shows exactly two new untracked files |
| Approval boundary | documentation-only source-comparison dispatch authoring |
| Claim boundary | no runtime/provider/live/public/CLI/MCP invocation or implementation claim |
| Agent type | dispatcher |
| Invocation ID | `pint-r2-dispatch-2026-07-25` |
| Expected manifest | paired PINT-R2 baseline and this work order |
| Actual changed set | paired PINT-R2 baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local documentation two-candidate owner-source comparison dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control or runtime-enforcement behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is claimed |
| invocationBoundary | no external agent invocation is authorized |
| interceptionBoundary | no wrapper, proxy, launch gate, process interception, or cancellation behavior |
| claimLanguage | source comparison and gap-sharpening documentation only |
| forbiddenExpansion | no runtime, provider, live, public, package, checker, or MCP/CLI behavior without fresh authorization |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance owner-source comparison work; no public-sync batch
is authorized.

## Claim Boundary

This work order authorizes a bounded two-candidate local source-to-owner
comparison only. It does not authorize enum implementation, package
activation, checker implementation, runtime construction, CLI/MCP invocation,
provider or account use, process control, or public sync. It does not reopen
the EAIC MCP/CLI runtime lane or lift the invocation moratorium.

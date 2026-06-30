# CVF KIOD-R6 Memory Foundation Enrichment Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_READY_FOR_WORK_ORDER_AUTHORING

docType: roadmap

Date: 2026-06-30

Owner: Codex

rawMemoryReleased: false

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| literalTokensReviewed | `Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; roadmap sections for authorization, purpose, scope, non-goals, dispatch boundary, work plan, acceptance criteria, and verification evidence; `ENRICH_EXISTING`; `NEW_FINDING_CANDIDATE`; `REJECT_DIRECT_IMPORT`; `N/A with reason` |
| gateRunPurpose | confirm this roadmap shape after reading applicable checker source; gates are confirmation, not first discovery |
| claimBoundary | roadmap authoring only; no GC-018, work order, implementation, checker, runtime, provider/live, public-sync, source import, MCP/CLI adapter, dashboard, package lifecycle, automatic invocation, action authority, or production behavior claim |

## Authorization / Decision

The operator selected the next knowledge-intake direction after KIOD-R5:
convert the retained Controlled Memory Index Store value into a governed
memory-foundation enrichment lane.

Decision:
`AUTHOR_KIOD_R6_ROADMAP_FOR_DOC_ONLY_MEMORY_FOUNDATION_ENRICHMENT`.

This roadmap is not a work order. It prepares the boundary and trace seed for a
separate GC-018 baseline and source-verified work order authoring pass.

## Purpose

KIOD-R5 proved that the selected folder is not suitable for direct import, but
it also retained bounded memory-foundation value. R6 should prevent that value
from being lost while also preventing overlap, runtime overclaiming, checker
copying, and synthetic example import.

The useful work is a doc-only enrichment decision over existing CVF memory
foundation owner surfaces. The worker must compare retained KIOD-R5 candidates
against current CVF owner documents and rewrite only CVF-native reference
language that survives that comparison.

## Scope / Target / Owner Boundary

Allowed R6 roadmap scope:

- preserve KIOD-R5 as the source of retained candidate evidence;
- route only doc-only memory-foundation enrichment for the next work order;
- require field-level comparison before adapting any candidate;
- require every accepted value to map to a CVF owner surface;
- keep checker/source implementation candidates separate from this lane.

Candidate owner surfaces for the future work order:

- `docs/reference/memory_foundation/README.md`;
- `docs/reference/memory_foundation/CVF_MEMORY_FOUNDATION_SOURCE_DERIVED_REPLAY_CONTRACT.md`;
- `docs/reference/memory_foundation/CVF_MEMORY_FOUNDATION_OWNER_SURFACE_RECONCILIATION_MATRIX.md`;
- `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` only when the work order source-verifies that the claim belongs to the runtime-adjacent memory plane contract.

Forbidden R6 roadmap scope:

- no source code import from Controlled Memory Index Store;
- no direct import of source checker, tests, generated JSON, generated SQL, or
  generated Markdown examples;
- no SQLite or LanceDB runtime implementation;
- no memory server, daemon, watcher, vector index, embedding, rerank, rebuild
  job, or durable write implementation;
- no MCP/CLI adapter, package activation, automatic invocation, or action
  authority;
- no Web/UI/dashboard work;
- no public-sync or public catalog claim;
- no provider/live proof or governance-behavior proof;
- no production-readiness or runtime capability claim.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| KIOD-R5 retained doc-only memory-foundation value | `docs/reviews/CVF_KIOD_R5_PACKET_BLOCKED_PILOT_COMPLETION_2026-06-30.md` | lines 38-39; lines 136-149 | `ENRICH_EXISTING`; `NEW_FINDING_CANDIDATE`; `REJECT_DIRECT_IMPORT` | KIOD-R5 completion review | DOC_ONLY_NEW | ACCEPT |
| KIOD-R5 accounts for the selected folder without direct import | `docs/reviews/CVF_KIOD_R5_PACKET_BLOCKED_PILOT_COMPLETION_2026-06-30.md` | lines 123; 190-197; 205-206 | `no source files imported`; `Output traceability`; `REJECT_DIRECT_IMPORT` | KIOD-R5 completion review | VALUE_SET | ACCEPT |
| Worker return records reviewer-controlled expansion of accepted enrichment rows | `docs/reviews/CVF_KIOD_R5_PACKET_BLOCKED_PILOT_WORKER_RETURN_2026-06-30.md` | line 416 | `ENRICH_EXISTING rows` | KIOD-R5 worker return | VALUE_SET | ACCEPT |
| Retrieval receipt overlap is a partial heading match needing field-level comparison | `docs/reviews/CVF_KIOD_R5_PACKET_BLOCKED_PILOT_WORKER_RETURN_2026-06-30.md` | lines 309-314; line 421 | `Retrieval Receipt Contract` | KIOD-R5 worker return | VALUE_SET | ACCEPT |
| Controlled memory index terms remain candidates, not implementation authority | `docs/reviews/CVF_KIOD_R5_PACKET_BLOCKED_PILOT_WORKER_RETURN_2026-06-30.md` | lines 360-368 | `NEW_FINDING_CANDIDATE` | KIOD-R5 worker return | VALUE_SET | ACCEPT |
| Checker, test, and generated examples are rejected for direct import | `docs/reviews/CVF_KIOD_R5_PACKET_BLOCKED_PILOT_WORKER_RETURN_2026-06-30.md` | lines 383-384; 400-401; 423 | `REJECT_DIRECT_IMPORT` | KIOD-R5 worker return | VALUE_SET | ACCEPT |
| Memory foundation front door owns documentation contracts for source, derived index, receipts, and replay | `docs/reference/memory_foundation/README.md` | Purpose; Scope / Target / Owner Boundary; Active References | `docs/reference/memory_foundation/README.md` | memory foundation front door | EXISTS | ACCEPT |
| Existing memory foundation contract already defines source authority, derived surfaces, retrieval receipt, rebuild receipt, and claim boundary | `docs/reference/memory_foundation/CVF_MEMORY_FOUNDATION_SOURCE_DERIVED_REPLAY_CONTRACT.md` | Purpose; Source Authority Rule; Source And Derived Surface Classes; Retrieval Receipt Contract; Rebuild Receipt Contract; Claim Boundary | `cvf.memoryFoundation.sourceDerivedReplay.everosT1.v1` | memory foundation source-derived replay contract | EXISTS | ACCEPT |
| Owner surface reconciliation already classifies retrieval receipt as covered contract-only and rebuild receipt as doc-only gap candidate | `docs/reference/memory_foundation/CVF_MEMORY_FOUNDATION_OWNER_SURFACE_RECONCILIATION_MATRIX.md` | Source Verification Block; Reconciliation Matrix; Claim Boundary | `Retrieval receipt minimum fields`; `Rebuild receipt schema/checker` | memory foundation reconciliation matrix | DOC_ONLY_NEW | ACCEPT |

## Non-Goals

R6 does not:

- reopen EverOS T0-T5 or KIOD-R5 closure;
- absorb the selected folder as a package, runtime, adapter, or public surface;
- implement or wire a checker;
- mutate generated aggregates except later session-sync if a material commit
  changes session continuity;
- create a memory index store implementation;
- create live/provider proof;
- claim that CVF currently has SQLite, LanceDB, vector, or automatic memory
  behavior;
- ask a worker to infer source facts from chat history or provider memory.

## Design Control Gate / Dispatch Boundary / Governed Work Lifecycle

The next artifact must be a fresh GC-018 baseline and source-verified work
order. The work-order author must not start by writing prose and then debugging
gates. Before writing the first work-order section, the author must:

- read `docs/reference/guard_orientation/README.md`;
- read `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`;
- identify every applicable `governance/compat/check_*.py` file for baseline,
  work-order, handoff, source-verification, dispatch-quality, and worker-return
  shape;
- read the checker source and constants before writing the first line;
- include a `Checker Source Read-Ahead Block`;
- include an `ADIF Defect Registry Disclosure`;
- include a `Source Verification Block` with only source-backed `ACCEPT`,
  `REJECT`, or `BLOCKED_SOURCE_NOT_FOUND` rows;
- include a Roadmap-to-Work-Order Trace Matrix mapping this roadmap to each
  work-order instruction;
- use `WORKER_MUST_NOT_COMMIT`;
- require reviewer-owned closure conversion after worker return.

If the work-order author cannot source-verify the exact target owner surface or
the exact retained KIOD-R5 candidate, the work order must stay in `HOLD_*`,
`DRAFT`, or `BLOCKED` status.

## Negative Search And Collision Discipline

R6 is a roadmap, so it does not close negative-search evidence by itself. The
future work order must require a fresh collision pass before any candidate is
accepted into a CVF owner surface.

| Field | Required value for the future work order |
|---|---|
| search roots | `docs governance CVF_SESSION EXTENSIONS scripts .github` plus the source-verified KIOD-R5 review artifacts |
| search command or query | `rg -n --fixed-strings "<candidate-token>" docs governance CVF_SESSION EXTENSIONS scripts .github` and a second query limited to the selected owner-surface target files |
| coverage | source, tests, docs, JSON, and external evidence references that are named by the work order |
| absent-versus-collision disposition | each token must be classified as absent, same-token collision, non-authoritative occurrence, different meaning occurrence, or binding owner-surface match |

Known collision tokens in this roadmap:

| Token | Collision / occurrence handling | Disposition |
|---|---|---|
| `ADIF` | same-token collision occurs in existing agent-defect registry and dispatch rules; those occurrences are authoritative only for defect disclosure, not for memory-foundation content | collision, not binding for content |
| `KIOD` | same-token collision occurs in existing KIOD dispatch and review artifacts; those occurrences are source evidence for this lane only when cited by exact file and line | collision, source-bound |
| `OWNER_SURFA` | same-token collision occurs as the prefix of owner-surface terms such as `OWNER_SURFACE_NOT_FOUND`; it is not an accepted owner surface by itself | collision, not binding |
| `REJECT_DIRECT_IMPORT` | same-token collision occurs in KIOD-R5 and external-intake doctrine; it remains the binding direct-import rejection disposition when cited to KIOD-R5 evidence | collision, binding only for rejection |
| `WORKER_MUST_NOT_COMMIT` | same-token collision occurs in handoff and work-order governance; it is binding only for role/commit mode in the future work order | collision, binding only for role control |

Minimum required collision checks for the future work order:

- exact-token search for each retained KIOD-R5 candidate term before any edit;
- owner-surface search across the candidate target files named in this roadmap;
- distinction between heading-only overlap and schema/field overlap;
- explicit `BLOCKED_SOURCE_NOT_FOUND` for any target owner surface or source
  term that cannot be verified;
- explicit `REJECT_DIRECT_IMPORT` for checker, test, generated example, and
  source-package material;
- no accepted row based only on `OWNER_SURFACE_NOT_FOUND`, provider memory,
  chat history, or copied package prose.

## Work Plan

| Step | Output | Stop condition |
|---|---|---|
| R6.0 Work-order authoring | GC-018 and work order for doc-only memory-foundation enrichment | checker source was not read before drafting, source facts are missing, or dispatch quality fails |
| R6.1 Candidate replay | table that replays KIOD-R5 retained rows B, C, D, E, H, I, J, and K against current owner surfaces | any candidate is accepted without field-level comparison |
| R6.2 Owner-surface decision | per-candidate disposition: `ADAPT_DOC_ONLY`, `NO_CHANGE_WITH_REASON`, `DEFER_TO_SEPARATE_RUNTIME_TRANCHE`, `DEFER_TO_SEPARATE_CHECKER_TRANCHE`, or `REJECT_DIRECT_IMPORT` | a runtime/checker/import candidate is mixed into doc-only reference edits |
| R6.3 CVF-native reference patch | bounded edits only to source-verified memory-foundation reference surfaces | copied source prose, generated examples, SQLite/LanceDB runtime schema, or public/runtime claim appears |
| R6.4 Reviewer closure | completion review compares roadmap, work order, worker return, diff, and gates | closure artifact claims implementation or leaves unresolved candidate rows |

## Roadmap-To-Work-Order Trace Seed

| Roadmap requirement | Required work-order instruction | Required evidence |
|---|---|---|
| Preserve value without overlap | replay all retained KIOD-R5 candidate groups before editing | candidate replay table with source paths and dispositions |
| Prevent direct import | prohibit copying checker, tests, generated examples, or source package text | git diff plus explicit `REJECT_DIRECT_IMPORT` rows |
| Keep doc-only scope | limit material edits to source-verified memory reference docs | allowed-scope manifest and git diff name-status |
| Require checker read-ahead | include read-ahead block before section drafting | list of applicable checkers and constants read |
| Require source verification | cite current CVF owner surfaces and KIOD-R5 rows | Source Verification Block with exact files and sections |
| Preserve handoff discipline | use `WORKER_MUST_NOT_COMMIT` and reviewer-owned closure | Agent Handoff Contract Control Block |

## Acceptance Criteria

| ID | Criterion | Required disposition |
|---|---|---|
| AC1 | Work order is source-verified before dispatch and does not rely on chat/provider memory | PASS_REQUIRED |
| AC2 | Work order includes checker read-ahead evidence and ADIF disclosure | PASS_REQUIRED |
| AC3 | Every retained KIOD-R5 candidate group is replayed and classified | PASS_REQUIRED |
| AC4 | Accepted edits enrich existing CVF memory foundation doctrine only | PASS_REQUIRED |
| AC5 | Runtime, checker, package, adapter, Web/UI, public-sync, source-import, and generated-example work remain excluded | PASS_REQUIRED |
| AC6 | Retrieval receipt overlap is resolved by field-level comparison, not heading match | PASS_REQUIRED |
| AC7 | Checker/test/generated-example candidates stay `REJECT_DIRECT_IMPORT` unless a separate future CVF-authored checker work order is opened | PASS_REQUIRED |
| AC8 | Closure evidence includes diff, gates, and unresolved-candidate disposition | PASS_REQUIRED |

## Verification / Evidence

The roadmap author must verify this roadmap with changed-range gates before
claiming it is ready for work-order authoring.

| Evidence item | Command or artifact | Required result |
|---|---|---|
| Read-ahead shape | `python governance/compat/check_governed_artifact_checker_read_ahead.py --base 2f4b0159 --head HEAD --enforce` | PASS |
| Structural roadmap shape | `python governance/compat/check_markdown_structural_completeness.py --base 2f4b0159 --head HEAD --enforce` | PASS |
| Roadmap freshness | `python governance/compat/check_roadmap_closure_freshness.py --base 2f4b0159 --head HEAD --enforce` | PASS |
| Dispatch-quality non-regression | `python governance/compat/check_work_order_dispatch_quality.py --base 2f4b0159 --head HEAD --enforce` | PASS or N/A with reason if no work order is in changed set |
| Material diff | `git diff --name-status 2f4b0159...HEAD` | roadmap-only before session-sync |

The future work order must refresh base and head values from its own dispatch
base. It must not reuse this roadmap's verification range as dispatch evidence.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance roadmap for work-order authoring. It does
not authorize public-sync, public catalog export, or public-facing claim.

## Claim Boundary

This roadmap claims only that KIOD-R6 should prepare a doc-only
memory-foundation enrichment work order from retained KIOD-R5 evidence. It does
not close R6, dispatch a worker, implement reference edits, create a checker,
import external source material, run live/provider proof, mutate runtime
behavior, expose public-sync, or claim any new memory capability.

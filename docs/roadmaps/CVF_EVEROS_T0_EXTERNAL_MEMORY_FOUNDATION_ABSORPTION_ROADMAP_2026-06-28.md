# CVF EVEROS-T0 External Memory Foundation Absorption Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_READY_FOR_OPERATOR_REVIEW

docType: roadmap

Date: 2026-06-28

Owner: Codex

rawMemoryReleased: false

## Authorization / Decision

The operator authorized moving to the external repository
`https://github.com/EverMind-AI/EverOS.git` under the existing external
absorption rules.

Decision:
`ACCEPT_EVEROS_AS_MEMORY_FOUNDATION_DOCTRINE_SEED_WITH_RUNTIME_DEFERRED`.

This roadmap records the T0 audit and routing decision only. It does not
implement an EverOS-derived runtime, vector store, memory server, provider
route, API route, MCP/CLI adapter, package activation, public-sync batch, or
live governance claim.

## Purpose

Audit EverOS and the operator-provided EverOS absorption package deeply enough
to decide which ideas are worth adapting into CVF. The useful value is not
"build EverOS inside CVF." The value is a source-backed foundation contract for
canonical memory, derived indexes, replay/rebuild, retrieval receipts, and
timestamp discipline.

## Non-Goals

This roadmap does not:

- copy EverOS source code into CVF;
- vendor EverOS, LanceDB, SQLite migrations, OpenRouter, DeepInfra, or
  multimodal dependencies;
- run EverOS server, demos, benchmark suites, provider calls, or external
  memory daemons;
- claim CVF has production vector memory, durable memory runtime, OME runtime,
  or route-side memory federation;
- expose private provenance through public handoff or public-sync;
- mutate generated active-session state in the material commit;
- authorize MPI-T6 runtime, provider/live, adapter/package, or public-sync work.

## Scope / Target / Owner Boundary

Allowed material scope:

- file this EVEROS-T0 roadmap;
- classify EverOS patterns into absorb, adapt, defer, and reject groups;
- use the external package only as advisory input after direct EverOS audit;
- recommend a future T1 GC-018/work order for a CVF-native memory foundation
  contract.

Forbidden material scope:

- no runtime implementation;
- no database, vector index, embedding, rerank, watcher, cascade daemon, or OME
  implementation;
- no external package import as trusted CVF source;
- no public-sync or push from the provenance workspace;
- no live/provider proof;
- no MCP/CLI/IDE bridge or Claude plugin activation.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| External source | `https://github.com/EverMind-AI/EverOS.git` at `b7d15f72527b8850b712838a46b13d4dd0f8d214` |
| Local external clone | `.private_reference/external_repos/EverOS` |
| Operator-provided package | `.private_reference/legacy/CVF Controlled Memory Index Store` |
| Chain map route | External repo or copied folder -> Root/folder lifecycle classification plus absorption map when retained -> CVF-owned roadmap -> ABSORB, ADAPT, DEFER, REJECT, or BLOCK |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this EVEROS-T0 roadmap |
| Disposition | ADAPT as CVF memory-foundation doctrine seed; defer runtime |
| Claim boundary | external materials are advisory inputs, not CVF source authority |

## Source Authority And External Evidence Boundary

| Source | Path or identifier | Role | Disposition |
|---|---|---|---|
| CVF external intake chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | governs routing for external repositories and copied folders | ACCEPT |
| CVF guard orientation | `docs/reference/guard_orientation/README.md` | required orientation before governed artifact authoring | ACCEPT |
| EverOS repository | `https://github.com/EverMind-AI/EverOS.git` at `b7d15f72527b8850b712838a46b13d4dd0f8d214` | external evidence source only | EXTERNAL_INPUT_ONLY |
| EverOS local clone | `.private_reference/external_repos/EverOS` | local audit copy, ignored/private | EXTERNAL_INPUT_ONLY |
| Operator-provided package | `.private_reference/legacy/CVF Controlled Memory Index Store` | advisory absorption draft | EXTERNAL_INPUT_ONLY |
| Provider memory/chat | N/A | operating context only | NOT_CVF_SOURCE |

Provider-specific memory, external package prose, browser state, and chat-only
facts are not CVF source authority. Any future T1 work order must source-verify
CVF-owned fields against CVF-governed surfaces before implementation.

## External Repo Evidence Crosswalk

| Evidence item | External evidence | CVF value | T0 disposition |
|---|---|---|---|
| Apache-2.0 licensing | EverOS `LICENSE`; `pyproject.toml` declares Apache-2.0 | permits clean-room learning with attribution discipline | USE_IDEAS_NOT_CODE |
| Markdown is truth | EverOS `docs/overview.md` lines 30-45; `docs/how-memory-works.md` lines 26-38; `docs/storage_layout.md` lines 6-7 | strengthens CVF source-of-truth vs generated/derived surfaces | ABSORB_AS_DOCTRINE |
| Three-piece storage boundary | EverOS `docs/overview.md` lines 43-45; `docs/architecture.md` lines 71-107 | clear split between canonical files, SQLite queues/audit, and LanceDB retrieval | ADAPT_TO_CVF_DERIVED_VIEW_BOUNDARY |
| Atomic write and path containment | EverOS `src/everos/core/persistence/markdown/writer.py` lines 1-18, 33-35, 104-158 | durable Markdown writes and traversal defense pattern | ABSORB_AS_STORAGE_SAFETY_PATTERN |
| Cascade replay model | EverOS `docs/cascade_runbook.md` lines 24-31, 54-82, 133-145 | practical replay/retry semantics for derived indexes | ADAPT_AS_REBUILD_AND_REPLAY_PATTERN |
| Timestamp discipline | EverOS `docs/datetime.md` lines 22-31, 68-70, 158-160; `src/everos/component/utils/datetime.py` lines 5-18 | separates UTC storage from display timezone and CI enforcement | ABSORB_AS_TIMESTAMP_DISCIPLINE |
| Reflection consolidation | EverOS `src/everos/memory/reflection/orchestrator.py`; `docs/reflection.md` | useful select/merge/re-extract/deprecate lifecycle | ADAPT_AS_CLAIM_CONSOLIDATION_PATTERN |
| Layered architecture/import contracts | EverOS `pyproject.toml`; `docs/architecture.md` lines 29-61 | reinforces dependency-boundary enforcement | ADAPT_AS_LAYER_BOUNDARY_PATTERN |
| Prompt slot overlays | EverOS `docs/prompt_slots.md`; `docs/architecture.md` lines 152-164 | possible future governed prompt/config override model | DEFER_TO_SEPARATE_LANE |
| Knowledge document/topic store | EverOS `docs/knowledge.md` | possible future source-backed knowledge pages | DEFER_TO_CORPUS_OR_KNOWLEDGE_LANE |
| OME strategy engine | EverOS OME source and architecture docs | interesting offline evolution pattern but risky for CVF autonomy claims | DEFER_RUNTIME |
| Plugin and use-case examples | EverOS `use-cases/` | reference only; provider-local guidance is not CVF authority | REJECT_DIRECT_IMPORT |

## Advisory Package Audit Result

The operator-provided package named `CVF Controlled Memory Index Store` was
read as advisory material and moved out of root into private legacy/reference.
Its useful content is not the exact schema text; its value is the already-CVF
framing:

| Package finding | Evidence | T0 handling |
|---|---|---|
| It keeps `ABSORPTION_SPEC_ONLY` and no runtime/production claim | package `README.md` lines 1-8; `00_SCOPE_AND_CLAIM_BOUNDARY.md` | retain claim-boundary posture |
| It maps Markdown/SQLite/LanceDB to governed roles | package `README.md` lines 119-151; absorption map lines 36-40 | reuse as T1 input, not source authority |
| It defines read/write gates and retrieval receipts | package `07_MEMORY_READ_WRITE_GATE_CONTRACT.md`; `08_RETRIEVAL_RECEIPT_CONTRACT.md` | adapt after CVF source verification |
| It defines privacy, retention, redaction, and rebuild rules | package `09_PRIVACY_RETENTION_REDACTION_POLICY.md`; `10_INDEX_REBUILD_AND_RECOVERY_PROTOCOL.md` | adapt as contract candidates |
| It proposes runtime phases and sample schemas | package `11_ROADMAP_AND_ACCEPTANCE_CRITERIA.md` lines 104-120 | defer; too implementation-shaped for T0 |

The package should stay in private legacy/reference until a future T1 decides
which fragments are rewritten into CVF-governed reference language.

## Absorption Classification

| Class | Items | Disposition |
|---|---|---|
| Absorb now as doctrine | Markdown canonical truth; disposable derived indexes; atomic write safety; explicit stale-index denial; UTC-storage/display-time split | T1 contract candidate |
| Adapt with CVF controls | SQLite ledger, retrieval receipts, read/write gates, replay/rebuild states, memory class taxonomy, reflection deprecation lifecycle | T1/T2 source-verified contracts |
| Defer | LanceDB implementation, embeddings, rerank, OME strategy engine, prompt-slot runtime, knowledge API, multimodal ingestion | future separate roadmap only |
| Reject direct import | EverOS server/runtime, provider configs, Claude plugin, use-case demos, raw chat reuse, automatic skill promotion, public export of private provenance | no CVF adoption in this lane |

## Recommended Next Tranche

Recommended next work order:

`EVEROS-T1 Markdown Truth, Derived Index, And Replay Boundary Contract`

T1 should create a CVF-native reference contract, not a runtime
implementation. It should define:

- canonical Markdown/source surfaces versus generated aggregates and derived
  indexes;
- SQLite/vector-style index roles as optional derived views only;
- stale/degraded index denial and rebuild receipt rules;
- retrieval receipt minimum fields;
- privacy/redaction/retention boundaries;
- UTC-storage and display-time discipline for future memory/index artifacts;
- explicit no-runtime/no-provider/no-public claim boundary.

## Work Plan

| Step | Output | Stop condition |
|---|---|---|
| Pin external input | EverOS HEAD and local clone recorded | external repo cannot be cloned or pinned |
| Audit primary repo | evidence crosswalk against EverOS docs/source | only file names are inventoried without content review |
| Audit advisory package | useful package fragments classified | package is copied wholesale as CVF authority |
| Route value | absorb/adapt/defer/reject table | runtime implementation is opened in T0 |
| Recommend T1 | CVF-native contract lane named | T1 claims runtime, vector store, provider/live, or public-sync |

## Design Control Gate

| Design control | Handling | Verdict |
|---|---|---|
| External source boundary | EverOS and the package are advisory inputs only | PASS |
| CVF root preservation | CVF governance remains the owner of any absorbed contract | PASS |
| Runtime restraint | no implementation or provider/live proof is claimed | PASS |
| Public/provenance boundary | no public-sync and no private provenance export | PASS |
| Value routing | high-value doctrine routed to T1 contract, not runtime | PASS |
| Package handling | source package moved to private legacy/reference after audit | PASS |

## Verification / Evidence

| Evidence item | Command or artifact | Required result |
|---|---|---|
| EverOS pin | `git ls-remote https://github.com/EverMind-AI/EverOS.git HEAD` | `b7d15f72527b8850b712838a46b13d4dd0f8d214` |
| Local clone pin | `git -C .private_reference/external_repos/EverOS rev-parse --short HEAD` | `b7d15f7` |
| Advisory package preservation | package moved to `.private_reference/legacy/CVF Controlled Memory Index Store` | root worktree clean of copied package |
| External routing guard | `python governance/compat/check_external_knowledge_intake_routing.py --base 8eb10d12 --head HEAD --enforce` | PASS before commit |
| Structural/gate checks | CVF governed artifact gates over base `8eb10d12` and `HEAD` | PASS before commit |

## Acceptance Criteria

| ID | Criterion | Disposition |
|---|---|---|
| AC1 | EverOS is audited by content, not by file list only | PASS |
| AC2 | advisory package value is used without promoting it to CVF source authority | PASS |
| AC3 | high-value patterns are classified into absorb/adapt/defer/reject groups | PASS |
| AC4 | T1 recommendation is a contract lane, not runtime implementation | PASS |
| AC5 | public-sync, runtime/provider/live, adapter/package, and MPI-T6 remain out of scope | PASS |
| AC6 | external repo and package are kept in ignored/private reference locations | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance external-knowledge audit and T0 roadmap.
No public artifact or public-sync batch is authorized.

## Claim Boundary

This roadmap claims only that EverOS contains high-value patterns for a future
CVF memory foundation contract. It does not claim CVF has EverOS runtime,
production vector memory, durable memory storage, route-side federation,
provider-backed governance behavior, public-sync export, or automatic
self-evolving memory.

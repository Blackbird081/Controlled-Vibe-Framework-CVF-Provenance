# CVF CGE-R3 CodeGraph Upstream Source Mirror Absorption Review

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: review

Date: 2026-06-30

Work order: docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md

dispatchBaseHead: 3ef56ead

executionBaseHead: d774a7b2

Commit mode: WORKER_MUST_NOT_COMMIT

External absorption core: REQUIRED

rawMemoryReleased: false

## Purpose

Absorb the current upstream CodeGraph source mirror into CVF-owned reference
language without installing, initializing, indexing, querying, serving, or
activating CodeGraph. This review challenges the prior CGE-R1/CGE-R2 findings
against the current 409-file pinned upstream mirror and returns package,
runtime, checker, and direct-import dispositions for reviewer acceptance.

## Target

| Field | Value |
|---|---|
| Upstream repository | https://github.com/colbymchenry/codegraph.git |
| Pinned commit | da72946d25e112f662f5a60c6b69f363aec60f16 |
| Local mirror | .private_reference/source_mirrors/colbymchenry__codegraph |
| executionBaseHead | d774a7b2 |
| Source mirror file count | 409 non-git files |
| Worker manifest hash | sha256:7521050c35a7f6a5b923c1a3680ada1993fd131085c7e8b217830417b6d8f9a2 |
| Dispatch manifest hash | sha256:7ada7481a4a5cb63417fb839c852b62011aa46cfbdc598a3332d61ae4029de17 |
| Hash disposition | Worker hash uses sorted repo-relative paths normalized with char replacement for backslashes; dispatch hash used an earlier dispatch method. Count and pinned commit match, so this is a hash-method discrepancy, not source mirror drift. |

## Scope / Methodology

1. Captured execution base and clean worktree: `git rev-parse --short HEAD`
   returned `d774a7b2`; `git status --short` returned no rows before worker
   artifact authoring.
2. Verified pinned mirror commit and remote with local git commands.
3. Enumerated all non-git source mirror files using `Get-ChildItem` with
   `-Recurse -File -Force`, excluding `.git`.
4. Ran a readability pass over the full mirror: 400 text files read, 9 binary
   files classified, 0 unreadable files.
5. Semantically reviewed upstream package metadata, README, MCP tools,
   CLI command surface, DB schema, extraction orchestration, language map,
   resolver/framework registry, sync/watch surfaces, design notes,
   benchmarks, and documentation site references.
6. Compared resulting value against CGE-R1 and CGE-R2 owner surfaces.
7. Converted accepted value into the companion owner-surface delta and kept all
   runtime/package/checker findings parked for later governed work orders.

## Findings / Position

Position: COMPLETE_PENDING_REVIEW

The current upstream CodeGraph mirror adds material value beyond the old
89-file snapshot, but the value is still doctrine, candidate classification,
and future-lane design input only. The strongest portable findings are:

- Default agent tool exposure should be minimal: CodeGraph's current MCP
  posture exposes `codegraph_explore` by default and keeps seven narrower tools
  functional but unlisted unless allowlisted.
- Graph context should be answer-size and repo-size budgeted, not treated as an
  unlimited dump. CodeGraph's `getExploreBudget` and output budget tiers are a
  useful pattern for future CVF graph evidence caps.
- Staleness must be explicit. Pending files, connect-time catch-up, status
  output, and manual sync fallback are better doctrine than trusting a graph
  silently.
- A future CVF graph adapter should list static tool metadata independently
  from daemon readiness, and it should degrade to direct-read fallback when no
  index exists.
- Direct import remains rejected. The upstream implementation is a Node/WASM/
  SQLite/daemon/watcher package with installer and provider-adjacent agent
  wiring concerns; CVF would need a separate native governed runtime tranche.

## Risk / Corrective Action

| Risk | Classification | Corrective Action |
|---|---|---|
| Treating upstream CodeGraph source as CVF authority | AUTHORITY_BOUNDARY_RISK | Companion delta marks CodeGraph advisory only; CVF-owned conclusions live in governed review/reference artifacts. |
| Confusing upstream MCP/CLI features with CVF implementation permission | SCOPE_EXPANSION_RISK | Runtime and adapter features are classified as parked candidates requiring fresh GC-018/source-verified work order. |
| Treating benchmark claims as CVF proof | EVIDENCE_OVERCLAIM_RISK | Benchmark material is advisory external evidence only; no CVF governance behavior or performance claim is made. |
| Provider-specific upstream guidance files leaking into authority tables | PROVIDER_SPECIFIC_AUTHORITY_RISK | `.claude`, `.cursor`, and root provider guidance are rejected as CVF authority and used only as non-authoritative source context. |
| Dispatch versus worker manifest hash mismatch | HASH_METHOD_RISK | Review records the normalized worker hash and explains method discrepancy without declaring source drift. |

## Decision / Disposition

Decision: accept CGE-R3 as a source-mirror-backed upstream absorption worker
return pending reviewer acceptance.

Disposition:

- DOCTRINE_ADAPTED for minimal default tool surface, explicit staleness,
  connect-time catch-up, repo-size output budgets, line-numbered read parity,
  and no-read-back steering.
- PACKAGE_CANDIDATE enrichment for the existing metadata-only
  `cvf-code-intelligence-context-review` candidate.
- RUNTIME_CANDIDATE for CLI, MCP, daemon, watcher, SQLite, extraction,
  resolver, framework, and SDK surfaces.
- CHECKER_CANDIDATE for future boundaries around default MCP exposure,
  staleness/fallback receipts, source mirror hash method, and graph evidence
  overclaim prevention.
- REJECT_DIRECT_IMPORT for all upstream implementation code, installers,
  workflows, generated assets, provider-specific guidance, and lock/runtime
  files.

## Worker Status

Status: COMPLETE_PENDING_REVIEW

Limitations: no CodeGraph runtime was executed; no upstream tests were run; no
benchmark was rerun; semantic absorption used high-value source and grouped
family review after a full readability pass rather than line-by-line prose
analysis of every generated, binary, test, and lock artifact.

No commit issued by worker. HEAD remained `d774a7b2` before artifact authoring.

Changed paths expected in worker return:

- docs/reviews/CVF_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_REVIEW_2026-06-30.md
- docs/reference/CVF_CGE_R3_CODEGRAPH_UPSTREAM_OWNER_SURFACE_DELTA_2026-06-30.md

## Source Inventory

| Source | Action | Role |
|---|---|---|
| CVF_SESSION_MEMORY.md | READ | session front door and current mode context |
| CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json | READ | bootstrap read model |
| CVF_SESSION/ACTIVE_SESSION_STATE.json | READ | canonical active state registry |
| AGENT_HANDOFF_V29_2026-06-30.md | READ | active handoff and current lane boundary |
| docs/reference/guard_orientation/README.md | READ | guard surface orientation |
| docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md | READ | artifact literal-shape controls |
| docs/baselines/CVF_GC018_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md | READ | baseline authority |
| docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md | READ | worker contract |
| docs/reference/external_agent_review/README.md | READ | external absorption front door |
| docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md | READ | intake route |
| docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md | READ | absorption core |
| .private_reference/source_mirrors/INDEX.md | READ | source mirror ledger |
| docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md | READ | parked candidate rows |
| docs/reference/CVF_CGE_R1_CODE_INTELLIGENCE_OWNER_SURFACE_MATRIX_2026-06-29.md | READ | prior owner-surface baseline |
| docs/reviews/CVF_CGE_R2_CODEGRAPH_RESCAN_VALUE_AUDIT_AND_CORRECTION_2026-06-29.md | READ | prior correction baseline |
| docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md | READ | package candidate contract |
| docs/reference/agent_system_skills/registry/entries/cvf-code-intelligence-context-review.json | READ | current package candidate |
| .private_reference/source_mirrors/colbymchenry__codegraph | READ | pinned upstream mirror |

## Corpus Manifest

| Manifest group | Count | Terminal status | Disposition |
|---|---:|---|---|
| __tests__ | 122 | READ | ADAPT as checker and validation evidence; no direct test import |
| .claude | 3 | READ | REJECT as provider-specific authority |
| .cursor | 1 | READ | REJECT as provider-specific authority |
| CLAUDE.md | 1 | READ | REJECT as provider-specific authority |
| .github | 2 | READ | REJECT_DIRECT_IMPORT for CI/release workflow patterns |
| Root package/docs/config/install files | 12 | READ | ADAPT selected package/docs facts; reject runtime execution |
| assets binary files | 2 | SKIPPED_WITH_REASON | NO_PACKAGE_OR_RUNTIME_VALUE; generated/static assets only |
| docs | 17 | READ | ADAPT design, benchmark, search-quality, and framework doctrine |
| scripts | 55 | READ | ADAPT as benchmark/eval design evidence only; reject execution |
| site text/docs/source | 31 | READ | ADAPT public documentation facts; reject website source import |
| site public favicon.svg | 1 | SKIPPED_WITH_REASON | NO_PACKAGE_OR_RUNTIME_VALUE; static asset |
| src text/source | 148 | READ | ADAPT as runtime/checker/package candidate evidence; reject direct import |
| src/extraction/wasm | 6 | SKIPPED_WITH_REASON | RUNTIME_CANDIDATE only; no binary import |
| telemetry-worker | 8 | READ | REJECT_DIRECT_IMPORT; telemetry service not CVF runtime evidence |

Manifest total: 409

Worker readability pass: text_read=400; binary_classified=9; unreadable=0.

## Processing Ledger

| Processing group | Count | Evidence basis | Terminal status | Disposition |
|---|---:|---|---|---|
| Upstream package identity and install docs | 12 | README, package metadata, install scripts, root docs/config | READ | ADAPT package identity and runtime candidate boundaries |
| Agent-facing MCP and CLI source | 32 | src/bin, src/mcp, README MCP section, site reference docs | READ | ADAPT minimal-tool and adapter-boundary doctrine |
| Graph DB, query, context, and traversal source | 24 | src/db, src/graph, src/context, src/search, src/types | READ | ADAPT schema/query-budget/runtime candidate patterns |
| Extraction, languages, and WASM grammar family | 48 | src/extraction and language registry; WASM binaries classified | READ | ADAPT language coverage doctrine; reject binary/source import |
| Resolution and framework resolver family | 43 | src/resolution and docs/design framework notes | READ | ADAPT framework/cross-language candidate doctrine |
| Sync, watcher, daemon, liveness, lock, and MCP lifecycle | 37 | src/sync, src/mcp, README freshness/troubleshooting docs | READ | ADAPT staleness, catch-up, and degrade-visible doctrine |
| Installer, target adapters, upgrade, telemetry, and site/service material | 77 | src/installer, src/upgrade, src/telemetry, telemetry-worker, site, scripts | READ | ADAPT only as candidate/anti-overclaim evidence; reject implementation |
| Test and evaluation corpus | 122 | __tests__ plus benchmark/eval docs and scripts | READ | ADAPT as checker/value-probe evidence; no test import |
| Provider-specific instruction material | 5 | .claude, .cursor, root provider guidance | READ | REJECT as CVF authority |
| Workflow/static/binary/no-new-value material | 9 | .github, assets, site favicon, WASM/static binary files | SKIPPED_WITH_REASON | REJECT_DIRECT_IMPORT or NO_PACKAGE_OR_RUNTIME_VALUE |

Processing reconciliation: manifest=409; ledger_terminal=409; exclusions=0;
unresolved=0.

## Absorption Disposition Ledger

| Disposition | Count | Groups |
|---|---:|---|
| ADAPT | 384 | package/docs/source/test/eval/site/script material converted into CVF doctrine, package candidate, runtime candidate, and checker candidate findings |
| REJECT_DIRECT_IMPORT | 11 | CI workflows, telemetry worker implementation, static/binary runtime artifacts, and external implementation source as direct CVF code |
| REJECT | 5 | provider-specific upstream guidance under `.claude`, `.cursor`, and root provider guidance |
| NO_NEW_VALUE | 9 | static assets, generated binary grammar/assets, and lock/config material after package identity and runtime-boundary facts were captured |
| DEFER | 0 | no source family left with unclassified CGE-R3 value |
| BLOCK | 0 | no unreadable source file |

Disposition taxonomy: ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE

Ledger terminal statuses used: READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, SKIPPED_WITH_REASON, BLOCKED_UNREADABLE

## External Absorption Core

| Field | Value |
|---|---|
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | https://github.com/colbymchenry/codegraph.git at da72946d25e112f662f5a60c6b69f363aec60f16; local mirror .private_reference/source_mirrors/colbymchenry__codegraph |
| Enumeration command | `Get-ChildItem -LiteralPath ".private_reference/source_mirrors/colbymchenry__codegraph" -Recurse -File -Force` excluding `.git` |
| Manifest artifact or inline manifest | inline Corpus Manifest table in this review |
| Processing ledger artifact or inline ledger | inline Processing Ledger table in this review |
| Ledger terminal statuses | READ; ADAPTED; DEFERRED; REJECTED; NO_NEW_VALUE; SKIPPED_WITH_REASON; BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB; ADAPT; DEFER; REJECT; BLOCK; NO_NEW_VALUE |
| Owner-surface map | docs/reference/CVF_CGE_R3_CODEGRAPH_UPSTREAM_OWNER_SURFACE_DELTA_2026-06-30.md |
| Unresolved items | 0 |
| Completion claim boundary | documentation/reference absorption only; no runtime, provider/live, public, production, MCP server, watcher, daemon, SQLite index, checker implementation, package activation, or direct import |

## Corpus Completeness And Report Integrity

- Corpus task class: KNOWLEDGE_ABSORPTION
- Corpus root: .private_reference/source_mirrors/colbymchenry__codegraph
- Snapshot time: 2026-06-30 local session
- Enumeration command: `Get-ChildItem -LiteralPath ".private_reference/source_mirrors/colbymchenry__codegraph" -Recurse -File -Force | Where-Object { $_.FullName -notmatch "\\.git\\" }`
- Manifest artifact or inline manifest: inline `## Corpus Manifest` table in this review
- Manifest hash: sha256:7521050c35a7f6a5b923c1a3680ada1993fd131085c7e8b217830417b6d8f9a2
- Processing ledger artifact or inline ledger: inline `## Processing Ledger` table in this review
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=409; ledger_terminal=409; exclusions=9; unresolved=0
- Unresolved files: 0
- Declared exclusions: 9 binary/static files classified with SKIPPED_WITH_REASON because they are generated grammar binaries or static assets with no text doctrine to absorb
- Unreadable or unsupported files: none
- Aggregation check: PASS
- Drift check: PASS for commit/count; hash-method discrepancy recorded in Target table
- Output traceability: companion owner-surface delta maps accepted value to CVF-owned doctrine, package, runtime, checker, and rejection lanes
- Adversarial verification: CGE-R1/CGE-R2 snapshot conclusions were compared against current upstream package metadata, README, MCP tools, CLI, DB, extraction, resolution, sync, docs, and test/eval surfaces
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror -> external absorption core -> full manifest and processing ledger -> value conversion matrix -> CVF owner-surface delta -> future package/runtime/checker work order only if separately authorized |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | docs/reviews/CVF_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_REVIEW_2026-06-30.md; docs/reference/CVF_CGE_R3_CODEGRAPH_UPSTREAM_OWNER_SURFACE_DELTA_2026-06-30.md |
| Disposition | COMPLETE_PENDING_REVIEW source-mirror absorption worker return |
| Claim boundary | documentation/reference only; no runtime, package activation, checker wiring, provider/live proof, public-sync, MCP server, watcher, daemon, benchmark rerun, or production-readiness claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| README, package.json, CLI source | CodeGraph is a real npm package with CLI identity, install/init/index/sync/query/explore/node/files/status/callers/callees/impact/affected/unlock/daemon/serve/upgrade/telemetry surfaces. | RUNTIME_CANDIDATE | owner-surface delta runtime section | Fresh runtime work order if operator selects CodeGraph runtime value-probe lane. | No install/init/index/sync/query/MCP/daemon/watcher/SQLite execution in CGE-R3 |
| MCP tools source and MCP docs | Default exposure is one primary tool, `codegraph_explore`; other tools remain functional but allowlisted/unlisted by default. | DOCTRINE_ADAPTED | owner-surface delta doctrine section | Future adapter design should prefer minimal default surface plus explicit allowlist. | No MCP adapter or external tool projection implemented |
| Explore budget and output budget source | Repo-size-aware and output-size-aware budgets prevent graph context from becoming unbounded result dumps. | DOCTRINE_ADAPTED | owner-surface delta doctrine/checker sections | Future graph receipt/checker lane may enforce budget fields. | Documentation/reference only |
| Watcher, sync, status, catch-up, staleness docs | Stale graph risk should be explicit and paired with direct-read/manual-sync fallback. | DOCTRINE_ADAPTED | owner-surface delta doctrine/checker sections | Future graph-evidence work order should require staleness/fallback fields. | No watcher, daemon, or sync process run |
| DB schema and query source | Local graph state is SQLite/FTS-backed with nodes, edges, files, unresolved refs, and project metadata. | RUNTIME_CANDIDATE | owner-surface delta runtime section | Future runtime design must source-verify storage, lock, WAL, and migration behavior. | No SQLite index or CVF storage implementation |
| Extraction/language/framework source | Multi-language and framework-aware resolution adds value for impact and route discovery. | RUNTIME_CANDIDATE | owner-surface delta runtime/package sections | Future value probe can test representative CVF repos only under fresh authority. | No parser/WASM/binary import |
| __tests__, benchmark docs, eval scripts | Tests and benchmark material identify useful future proof/checker ideas but are not CVF proof. | CHECKER_CANDIDATE | owner-surface delta checker section | Future checker/value-probe work order may adapt staleness, allowlist, fallback, and overclaim checks. | No upstream test execution or benchmark claim |
| Existing cvf-code-intelligence-context-review candidate | CGE-R3 can enrich metadata-only package candidate with upstream package identity and current tool-surface doctrine. | PACKAGE_CANDIDATE | docs/reference/agent_system_skills/registry/entries/cvf-code-intelligence-context-review.json in future tranche only | Separate package work order required before registry mutation or package root creation. | No package root, SKILL.md, generated index, ACTIVE state, resolver, or activation |
| Upstream implementation source and install workflows | Direct source import would cross runtime, dependency, daemon, watcher, adapter, and installer boundaries. | REJECT_DIRECT_IMPORT | owner-surface delta rejection ledger | Future CVF implementation must be native and governed. | No direct external source import |
| Provider-specific upstream guidance | Provider-local instruction files are not CVF authority. | REJECT_DIRECT_IMPORT | provider-specific rejection rows in this review | Use only CVF-governed sources in authority tables. | Not a package/runtime source |
| Static assets, binaries, locks, site chrome | No standalone CVF package/runtime value beyond already captured package/runtime facts. | NO_PACKAGE_OR_RUNTIME_VALUE | processing ledger | No follow-up needed. | No runtime/package behavior |

## Owner-Surface Map

| CVF owner surface | CGE-R3 disposition |
|---|---|
| docs/reference/CVF_CGE_R3_CODEGRAPH_UPSTREAM_OWNER_SURFACE_DELTA_2026-06-30.md | new worker-owned delta surface pending review |
| docs/reference/CVF_CGE_R1_CODE_INTELLIGENCE_OWNER_SURFACE_MATRIX_2026-06-29.md | retained as legacy-snapshot baseline; superseded only for upstream CodeGraph facts by CGE-R3 source mirror |
| docs/reviews/CVF_CGE_R2_CODEGRAPH_RESCAN_VALUE_AUDIT_AND_CORRECTION_2026-06-29.md | retained correction: graph evidence cannot grant freeze/approval/scope authority |
| docs/reference/agent_system_skills/registry/entries/cvf-code-intelligence-context-review.json | candidate enrichment only; no mutation in CGE-R3 |
| docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md | parked runtime/package/checker rows remain active reopen controls |

## Package Candidate Evaluation

The current metadata-only package candidate remains useful but should not be
activated from CGE-R3. Future package work could enrich it with:

- upstream package identity `@colbymchenry/codegraph` version `1.1.6`;
- minimal default MCP tool doctrine;
- explicit allowlist/deferred adapter language;
- source-mirror-backed runtime boundary warnings;
- language/framework coverage as advisory selector metadata;
- staleness/fallback and no-freeze-authority doctrine.

Package conclusion: PACKAGE_CANDIDATE only. No registry mutation, package root,
`SKILL.md`, generated skill index update, ACTIVE state, resolver behavior, or
adapter projection is authorized here.

## Runtime Candidate Evaluation

Runtime candidate families identified:

| Runtime family | Evidence source | CGE-R3 disposition |
|---|---|---|
| CLI command family | README and src/bin/codegraph.ts | RUNTIME_CANDIDATE only |
| MCP server/tool family | src/mcp and site MCP docs | RUNTIME_CANDIDATE only |
| Daemon/proxy/liveness/ppid lifecycle | src/mcp and daemon tests | RUNTIME_CANDIDATE only |
| SQLite/FTS graph storage | src/db/schema.sql and query source | RUNTIME_CANDIDATE only |
| Extraction/parser/WASM grammar family | src/extraction and language registry | RUNTIME_CANDIDATE only |
| Framework and cross-language resolver family | src/resolution and docs/design | RUNTIME_CANDIDATE only |
| Watcher/sync/staleness/catch-up family | README, site indexing guide, src/sync | RUNTIME_CANDIDATE only |
| Installer and agent target config family | README and src/installer | RUNTIME_CANDIDATE only |

Runtime conclusion: valuable but parked. Separate GC-018/source-verified work
order and proof are required before any CVF runtime, MCP, watcher, daemon,
SQLite, CLI adapter, provider-facing, or public claim.

## Checker Candidate Evaluation

Future checker candidates:

| Checker candidate | Source signal | Reopen condition |
|---|---|---|
| Source mirror hash method guard | dispatch/worker hash-method mismatch | add only if future source mirror lanes need stable cross-shell manifest hashing |
| Graph evidence overclaim guard | CGE-R1/CGE-R2/CGE-R3 repeated boundary | add before any graph-backed CVF claim can be marked closure evidence |
| Staleness/fallback receipt guard | CodeGraph pending-file and catch-up design | add if CVF creates graph receipt or adapter artifacts |
| MCP default surface guard | default-one-tool and allowlist design | add before any external CLI/MCP projection of code-intelligence package |
| Read-deny rejection guard | design notes reject blanket read-deny hook | add only if a future agent-instruction lane proposes blocking direct reads |
| Package/runtime lane separation guard | CodeGraph package identity tempts activation | add if registry mutation or package root work is dispatched |

Checker conclusion: CHECKER_CANDIDATE only. No Python checker, hook-chain
catalog, CI workflow, or guard implementation is authorized by CGE-R3.

## Direct Import Rejection Ledger

| Source family | Rejection reason |
|---|---|
| src implementation source | Node/WASM/SQLite/runtime implementation cannot be copied into CVF without native design and fresh authorization. |
| src/mcp and daemon source | External agent adapter behavior requires separate ingress, auth, mutation, raw-data, receipt, and public boundary design. |
| src/sync watcher/daemon behavior | Background watch/sync behavior is runtime action authority, not documentation absorption. |
| install scripts and installer target writers | Installer mutates local agent configuration and is forbidden in CGE-R3. |
| package-lock and generated binaries | Dependency/binary payloads are not CVF-owned source doctrine. |
| telemetry worker | External telemetry service implementation is out of scope and not CVF governance proof. |
| .github workflows | Upstream CI/release automation is not CVF hook or release authority. |
| provider-specific guidance | Provider-local guidance is not CVF authority. |

## Conditional Reopen Index Disposition

| Parked lane | CGE-R3 disposition |
|---|---|
| CGE-R2-code-intelligence-runtime-value-probe | Remains parked; CGE-R3 adds stronger candidate evidence but no runtime proof. |
| CGE-code-intelligence-package-candidate | Remains parked; CGE-R3 recommends candidate enrichment only under later package work order. |
| CGE-code-intelligence-checker-candidates | Remains parked; CGE-R3 adds specific checker candidates and source signals. |
| CodeGraph direct import | Remains rejected; upstream source is advisory external material only. |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Source mirror is pinned to upstream commit | .private_reference/source_mirrors/INDEX.md | CodeGraph mirror row | colbymchenry__codegraph | source mirror index | VALUE_SET | ACCEPT |
| CodeGraph package identity is `@colbymchenry/codegraph` version `1.1.6` | .private_reference/source_mirrors/colbymchenry__codegraph/package.json | package metadata | name; version; bin.codegraph | package.json | VALUE_SET | ACCEPT |
| CLI exposes install/init/index/sync/status/query/explore/node/files/callers/callees/impact/affected/unlock/daemon/serve/upgrade/telemetry families | .private_reference/source_mirrors/colbymchenry__codegraph/src/bin/codegraph.ts | command definitions and command header | program | CLI entrypoint | VALUE_SET | ACCEPT |
| MCP default listed tool is `codegraph_explore` | .private_reference/source_mirrors/colbymchenry__codegraph/src/mcp/tools.ts | DEFAULT_MCP_TOOLS | DEFAULT_MCP_TOOLS | MCP tools registry | VALUE_SET | ACCEPT |
| MCP source defines seven additional narrower tools | .private_reference/source_mirrors/colbymchenry__codegraph/src/mcp/tools.ts | tool definitions | codegraph_search; codegraph_callers; codegraph_callees; codegraph_impact; codegraph_node; codegraph_status; codegraph_files | MCP tools registry | VALUE_SET | ACCEPT |
| Source DB uses nodes, edges, files, unresolved refs, project metadata, and FTS | .private_reference/source_mirrors/colbymchenry__codegraph/src/db/schema.sql | CREATE TABLE and CREATE VIRTUAL TABLE statements | nodes; edges; files; unresolved_refs; project_metadata; nodes_fts | SQLite schema | VALUE_SET | ACCEPT |
| Language extractor registry covers multi-language source families | .private_reference/source_mirrors/colbymchenry__codegraph/src/extraction/languages/index.ts | EXTRACTORS map | EXTRACTORS | extraction language registry | VALUE_SET | ACCEPT |
| Resolver uses framework detection and bounded caches | .private_reference/source_mirrors/colbymchenry__codegraph/src/resolution/index.ts | ReferenceResolver and cache declarations | ReferenceResolver; CODEGRAPH_RESOLVER_CACHE_SIZE | reference resolver | VALUE_SET | ACCEPT |
| Watcher tracks pending files and degrades visibly on resource exhaustion | .private_reference/source_mirrors/colbymchenry__codegraph/src/sync/watcher.ts | FileWatcher and watch resource comments | FileWatcher; WatchOptions | sync watcher | VALUE_SET | ACCEPT |
| Package candidate remains metadata-only | docs/reference/agent_system_skills/registry/entries/cvf-code-intelligence-context-review.json | status and candidate fields | status; candidateState; externalCliMcpDisposition | ASSF registry entry | VALUE_SET | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Prior requirement or operator instruction | CGE-R3 response | Output artifact | Status |
|---|---|---|---|
| Operator selected CodeGraph upstream repo absorption | pinned source mirror reviewed under worker no-commit lane | this review | COMPLETE_PENDING_REVIEW |
| External absorption rules require manifest, ledger, value conversion, owner map | corpus manifest, processing ledger, value conversion matrix, owner-surface map included | this review and companion delta | COMPLETE_PENDING_REVIEW |
| CGE-R1/CGE-R2 used older snapshot and parked runtime/package/checker value | current upstream mirror compared and candidate deltas recorded | companion owner-surface delta | COMPLETE_PENDING_REVIEW |
| Runtime/MCP/package/checker remain parked | all such value classified as candidate only | runtime/package/checker sections | COMPLETE_PENDING_REVIEW |

## Rescan Intelligence Hardening

- Original source artifact: docs/reference/CVF_CGE_R1_CODE_INTELLIGENCE_OWNER_SURFACE_MATRIX_2026-06-29.md
- Predecessor intake artifact: docs/reviews/CVF_CGE_R2_CODEGRAPH_RESCAN_VALUE_AUDIT_AND_CORRECTION_2026-06-29.md
- Delta ledger status: COMPLETE_VERIFIED for CGE-R3 mirror count and grouped terminal disposition.
- Routing matrix status: DO_NOW completed for upstream source-mirror absorption review; SEPARATE_RUNTIME_TRANCHE retained for runtime/package/checker implementation; OUT_OF_SCOPE retained for public-sync/direct import/benchmark.
- Semantic sampling status: COMPLETE_WITH_DELTA_ROUTING_SAMPLE for high-value upstream surfaces named in Source Verification Block.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Status |
|---|---|
| UNCHANGED_FROM_INTAKE | Graph evidence remains advisory and cannot grant freeze, approval, closure, scope expansion, commit, or runtime authority. |
| CHANGED_DISPOSITION | Source authority for upstream CodeGraph facts moves from retained local snapshot to pinned upstream source mirror. |
| NEW_FINDING | Current upstream default MCP surface is one primary explore tool with optional allowlist for narrower tools. |
| NEW_FINDING | Current upstream adds stronger staleness, connect-time catch-up, watcher degradation, and repo-size budget doctrine. |
| REMOVED_OR_REJECTED | Direct import, runtime activation, MCP adapter, watcher, daemon, SQLite index, provider/live proof, public-sync, and benchmark claim remain rejected for CGE-R3. |

### Follow-Up Routing Matrix

| Routing lane | Status |
|---|---|
| DO_NOW | Produce CGE-R3 worker review and owner-surface delta. |
| SEPARATE_RUNTIME_TRANCHE | CodeGraph install/init/runtime/MCP/daemon/watcher/SQLite/adapter/value probe. |
| SEPARATE_PACKAGE_TRANCHE | ASSF candidate enrichment, package root, generated index, resolver, activation, or certification. |
| SEPARATE_CHECKER_TRANCHE | Any checker implementation or hook-chain wiring. |
| STRATEGIC_OPERATOR_DECISION | Choose whether CodeGraph value proceeds as dashboard, MCP/CLI adapter, runtime/model gateway adjacent work, or remains reference-only. |
| OUT_OF_SCOPE | Public-sync, production readiness, provider/live proof, benchmark rerun, direct import, and session-state mutation by worker. |
| RESOLVED_BY_DESIGN | Private source mirror remains read-only and CVF-owned artifacts carry conclusions without importing upstream source. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| CGE-R3-RS1 | package.json | package name/version/bin exist | PACKAGE_CANDIDATE | Package identity could be mistaken for CVF activation. | PASS_BOUNDARY_RETAINED |
| CGE-R3-RS2 | src/mcp/tools.ts | default MCP tools set contains explore only | DOCTRINE_ADAPTED | Multiple tools could bloat agent selection by default. | PASS_ADAPTED |
| CGE-R3-RS3 | README freshness docs and src/sync/watcher.ts | stale/pending files are surfaced visibly | DOCTRINE_ADAPTED | Graph result could be silently stale. | PASS_ADAPTED |
| CGE-R3-RS4 | src/db/schema.sql | SQLite/FTS graph schema exists | RUNTIME_CANDIDATE | Schema could be imported directly. | PASS_REJECT_DIRECT_IMPORT |
| CGE-R3-RS5 | provider-specific upstream guidance files | local agent guidance exists | REJECT | Provider guidance could leak into CVF authority. | PASS_REJECTED_AS_AUTHORITY |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| Dispatch and worker hash methods differed while commit/count matched | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Consider a future source mirror manifest hash-method guard only if this recurs across later source mirror lanes. |
| Default-one-tool MCP posture is a reusable adapter lesson | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | Carry doctrine into any future MCP/CLI adapter work order before implementation. |
| Staleness/fallback appears across CGE-R1, CGE-R2, and CGE-R3 | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | MACHINE_CHECK_CANDIDATE | Add a graph staleness/fallback receipt checker only if graph runtime or adapter work is authorized. |
| Provider-specific upstream guidance appeared in source mirror | RULE_GAP | DOCUMENTATION_ONLY_LEARNING | RULE_EXISTS | Enforce existing AGENTS provider-specific authority boundary; no new ADIF entry needed. |
| Worker-local grouped semantic review limitation | WORKER_EXECUTION_ERROR | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | Non-reusable limitation recorded in Worker Status; reviewer can accept or request deeper source-family audit. |

No new ADIF entry is added in this worker return because no repeated non-obvious
agent defect was discovered beyond already governed provider-boundary and
literal-format patterns.

## Epistemic Process Block

### Expected Result / Prediction

Current upstream CodeGraph would likely add runtime/tooling details absent from
the 89-file snapshot while preserving CGE-R2's correction that graph evidence
cannot become CVF authority.

### Evidence Comparison

The mirror contains package metadata, CLI/MCP source, SQLite schema, extraction
and resolver source, watcher/sync logic, docs, benchmarks, tests, installer
targets, and site docs. These confirm CodeGraph is a substantial runtime
candidate and refine adapter/staleness/output-budget doctrine, while also
strengthening the reason to reject direct import.

### Contradiction Or Gap Disposition

No contradiction found against CGE-R2's authority correction. The main gap is
that CGE-R3 does not run CodeGraph and therefore cannot claim measured CVF value,
runtime compatibility, performance, MCP behavior, or live governance behavior.

### Claim Update

CGE-R3 updates the source basis and owner-surface doctrine for CodeGraph
knowledge absorption only. Runtime, package, checker, public, benchmark, and
provider/live claims remain parked.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | CGE-R3 upstream CodeGraph source-mirror absorption worker return |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - source mirror commit, remote, count, normalized worker manifest hash, readability pass, processing ledger, and companion owner-surface delta |
| actionEvidence | ACTION_EVIDENCE_PRESENT - two worker-owned documentation/reference artifacts created |
| invocationBoundary | local documentation/reference authoring only under WORKER_MUST_NOT_COMMIT |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim; only local read/enumeration commands and file writes inside allowed scope |
| claimLanguage | upstream source-mirror absorption and CVF-owned owner-surface delta |
| forbiddenExpansion | no CodeGraph install/init/MCP/watcher/daemon/SQLite index, package activation, checker implementation, provider/live proof, public-sync, benchmark rerun, CI mutation, direct source import, or production-readiness claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex worker role |
| Provider or surface | local workspace |
| Session or invocation | CGE-R3 CodeGraph upstream source mirror absorption worker return, 2026-06-30 |
| Working directory | D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF |
| Command or tool surface | git, Get-ChildItem, Get-Content, Select-String, apply_patch, governance gates |
| Target paths | docs/reviews/CVF_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_REVIEW_2026-06-30.md; docs/reference/CVF_CGE_R3_CODEGRAPH_UPSTREAM_OWNER_SURFACE_DELTA_2026-06-30.md |
| Allowed scope source | docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md |
| Agent type | worker |
| Invocation ID | cge-r3-codegraph-upstream-absorption-worker-2026-06-30 |
| Expected manifest | docs/reviews/CVF_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_REVIEW_2026-06-30.md; docs/reference/CVF_CGE_R3_CODEGRAPH_UPSTREAM_OWNER_SURFACE_DELTA_2026-06-30.md |
| Actual changed set | docs/reviews/CVF_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_REVIEW_2026-06-30.md; docs/reference/CVF_CGE_R3_CODEGRAPH_UPSTREAM_OWNER_SURFACE_DELTA_2026-06-30.md |
| Manifest delta | MATCH |
| Before status evidence | `git status --short` returned no rows at executionBaseHead d774a7b2 |
| After status evidence | worker artifacts pending reviewer acceptance; no commit by worker |
| Diff evidence | `git diff --name-status` before reviewer closure |
| Approval boundary | no-commit documentation/reference worker output only |
| Claim boundary | no runtime, provider/live, public, production, package activation, checker wiring, MCP server, watcher, daemon, SQLite index, benchmark rerun, or direct import |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: CGE-R3 consumes a private source mirror and private provenance
comparison surfaces. Public-safe export requires separate public-sync
authorization.

## Machine Closure Package

| Field | Evidence |
|---|---|
| Worker status | COMPLETE_PENDING_REVIEW |
| executionBaseHead | d774a7b2 |
| Source mirror commit | da72946d25e112f662f5a60c6b69f363aec60f16 |
| Source mirror remote | https://github.com/colbymchenry/codegraph.git |
| Manifest count | 409 |
| Manifest hash | sha256:7521050c35a7f6a5b923c1a3680ada1993fd131085c7e8b217830417b6d8f9a2 |
| Readability pass | files=409; text_read=400; binary_classified=9; unreadable=0 |
| Changed path count | 2 |
| Commit disposition | WORKER_MUST_NOT_COMMIT; reviewer owns material commit if accepted |
| Pre-implementation autorun | PASS before worker artifact authoring |
| Worker gates | PASS: direct external absorption core, value conversion, external knowledge intake routing, corpus completeness, and worker-return fast gate |
| Git status | two untracked worker artifacts only: this review and the companion owner-surface delta |

## Claim Boundary

This review authorizes and records only CGE-R3 documentation/reference
absorption of the pinned upstream CodeGraph source mirror. It does not
authorize CodeGraph install, init, index, sync, query, MCP server, watcher,
daemon, SQLite index, package activation, package root creation, ASSF registry
mutation, generated index mutation, checker implementation, CI mutation,
provider/live proof, public-sync, benchmark rerun, direct source import,
automatic invocation, action authority, or production readiness.

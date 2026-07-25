# CVF GC-018 - PPMCP-R1 Pinned Upstream And Legacy Delta Re-Intake

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_DISPATCH_READY_WITH_REPAIRS

docType: baseline

Date: 2026-07-25

Batch ID: PPMCP-R1

dispatchBaseHead: 58e9799a9

External absorption core: REQUIRED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | `## External Absorption Core` required-field row labels; `## External Absorption Value Conversion Matrix` required columns and lane tokens (`PACKAGE_CANDIDATE`, `RUNTIME_CANDIDATE`, `CHECKER_CANDIDATE`, `DOCTRINE_ADAPTED`, `REJECT_DIRECT_IMPORT`, `NO_PACKAGE_OR_RUNTIME_VALUE`); `## Overlap And Novelty Classification` required columns and disposition tokens including the requirement that the `Existing CVF owner surface checked` cell itself contain `OWNER_SURFACE_NOT_FOUND` or a `/` path, not only the disposition column; `Source Verification` disposition enum (`ACCEPT`/`REJECT`/`BLOCKED_SOURCE_NOT_FOUND`); `Verified path or symbol` bare-symbol-only rule; `Verified line/section` definition-line rule (confirmed the checker's own regex-computed definition line can differ by one line from a plain source read when a blank line precedes the declaration, and cited the checker-computed line); `Resolver query: taskClass=`, `role=`, `lifecyclePhase=` exact ADIF disclosure line format; `active_markdown` file-size thresholds |
| gateRunPurpose | confirmation/evidence that the drafted packet satisfies checker-enforced shape after literal read-ahead, not first discovery of checker requirements |
| claimBoundary | this block records checker-source read-ahead evidence only; it does not implement, modify, or supersede any `governance/compat/check_*.py` checker |

## Purpose

Author a documentation-only, no-commit dispatch packet for a bounded re-intake
of the `pancake-pos-mcp` external repository against current CVF owner
surfaces. The packet author left this baseline `DRAFT_PENDING_REVIEW`; the
independent reviewer then reviewed and repaired it before recording the
current dispatch-ready disposition.

PPMCP-R1 exists because `pancake-pos-mcp` already has a prior partial
disposition trail (W3 tool-action taxonomy absorption; LHW16-T2 MCP approval
proof advisory closure recorded as `ABSORBED (doc-only connector scope)`; a
`runtime-owned` legacy-spec-absorption registry row noting the generic MCP
business adapter as absorbed with the Pancake-specific profile deferred), but
the upstream repository itself was never pinned in a source mirror and the
9-file legacy interpretation folder was never file-level reconciled against
the current `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` MCP business adapter
contract. This baseline authorizes a bounded worker comparison pass only. It
does not authorize implementation, runtime behavior, or a conclusion that
new value exists.

## Decision / Baseline / Proposed Tranche

Decision: prepare (not dispatch) a source-mirror-backed and legacy-folder
bounded re-intake packet for `pancake-pos-mcp`.

Baseline: `pancake-pos-mcp` upstream source and the retained legacy
interpretation folder are both advisory external material. Neither is CVF
authority. CVF-owned conclusions must be recorded in a governed audit
artifact under `docs/audits/`, not imported from upstream or legacy source.

Proposed tranche: a no-commit worker reads all 107 bounded-corpus files
(98 upstream + 9 legacy), produces a file-level processing ledger, and
compares extracted concepts against the named current CVF owner surfaces,
with permission to close `NO_NEW_VALUE` if the complete comparison supports
it.

## Scope / Target / Owner Boundary

Target source (primary, upstream):

`https://github.com/nguyennguyenit/pancake-pos-mcp.git`

Pinned commit:

`41979fdac4fdf9a8a6f956889c33f19fa3389215`

Local mirror:

`.private_reference/source_mirrors/nguyennguyenit__pancake-pos-mcp/`

Target source (secondary, legacy interpretation):

`.private_reference/legacy/CVF 16.5/pancake-pos-mcp/` (9 files)

Allowed write scope (this dispatch-authoring batch only):

- `.private_reference/source_mirrors/INDEX.md`
- `docs/baselines/CVF_GC018_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md`

Forbidden scope (this dispatch-authoring batch, and future worker tranche
unless separately authorized):

- no dependency install (`bun install`, `npm install`), no `bun`/`node`
  build, no `wrangler` deploy, no `.githooks/pre-commit` execution inside
  the mirror;
- no upstream test run (`vitest`, `tests/e2e-mcp.test.ts`, `tests/worker.test.ts`);
- no MCP server start (stdio, HTTP, or Cloudflare Worker transport), no
  `src/worker.ts` / `src/server.ts` execution;
- no external CLI/MCP agent invocation, no provider/API/account/network/
  browser/process-control activity;
- no changes inside either source payload
  (`.private_reference/source_mirrors/nguyennguyenit__pancake-pos-mcp/` or
  `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/`);
- no `EXTENSIONS/`, runtime source, hook-chain, CI, `scripts/`, or
  `governance/compat/` implementation changes;
- no package activation, no public-sync, no session-state or active-handoff
  edits by the worker;
- no commit by the worker (`WORKER_MUST_NOT_COMMIT`);
- worker must not self-declare `DISPATCH_READY`; only the completed independent
  independent review recorded later in this baseline releases dispatch.

Risk ceiling: R0 documentation/reference and private source-mirror control
plane only.

## Authority Chain

| Authority | Path or source | Disposition |
|---|---|---|
| Operator instruction | operator request 2026-07-25 to process `pancake-pos-mcp` as bounded pinned-upstream-plus-legacy re-intake, packet-author-only, `DRAFT_PENDING_REVIEW` | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| External absorption front door | `docs/reference/external_agent_review/README.md` (chain map and core standard cited directly below) | ACCEPT |
| External absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | ACCEPT |
| External absorption core standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | ACCEPT |
| Source mirror index | `.private_reference/source_mirrors/INDEX.md` | ACCEPT |
| Conditional reopen index | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | ACCEPT |
| Prior W3 tool-action taxonomy absorption | `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` line 141 | ACCEPT |
| Prior LHW16-T2 MCP approval proof advisory closure | `docs/reference/archive/CVF_LHW16_T2_MCP_APPROVAL_PROOF_ADVISORY_CONNECTOR_SPEC_2026-05-30.md` | ACCEPT |
| Prior legacy-spec-absorption registry row | `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` line 120 | ACCEPT |
| Prior corpus registry entry (partial-root LHW-RESCAN-C) | `docs/corpus-intelligence/registry/entries/legacy-cvf-16-5.json` | ACCEPT |
| Current MCP business adapter owner contract | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | ACCEPT |
| Current tool-action taxonomy owner contract | `governance/contracts/tool-action-taxonomy.ts` | ACCEPT |
| Roadmap-to-Work-Order Trace Matrix | NOT_APPLICABLE_WITH_REASON: PPMCP-R1 is an operator-authorized bounded re-intake dispatched directly from operator instruction, not derived from a written roadmap artifact | N/A |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Upstream repository is pinned at the stated commit | `.private_reference/source_mirrors/nguyennguyenit__pancake-pos-mcp/.git` | `git rev-parse HEAD` output | `41979fdac4fdf9a8a6f956889c33f19fa3389215` | mirror git metadata | VALUE_SET | ACCEPT |
| Upstream mirror tracks 98 files | `.private_reference/source_mirrors/nguyennguyenit__pancake-pos-mcp/` | `git ls-files` output count | `98` | mirror git metadata | VALUE_SET | ACCEPT |
| Legacy interpretation folder holds 9 files | `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/` | recursive file enumeration | `9` | filesystem enumeration | VALUE_SET | ACCEPT |
| Current MCP business adapter owner contract already defines a risk-class union type | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | line 2 | `MCPBusinessRiskClass` | mcp.business.adapter.contract.ts | VALUE_SET | ACCEPT |
| Current MCP business adapter owner contract already defines a transport union type | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | line 11 | `MCPBusinessTransport` | mcp.business.adapter.contract.ts | VALUE_SET | ACCEPT |
| Current MCP business adapter owner contract already defines an execution-receipt interface | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | line 60 | `MCPBusinessExecutionReceipt` | mcp.business.adapter.contract.ts | VALUE_SET | ACCEPT |
| Current tool-action taxonomy already defines an approval-state union type | `governance/contracts/tool-action-taxonomy.ts` | line 63 | `ToolActionApprovalState` | tool-action-taxonomy.ts | VALUE_SET | ACCEPT |
| `pancake-pos-mcp` legacy family already has a `PARTIALLY_ABSORBED` disposition with a narrow reopen condition limited to MCP approval proof | `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` | line 141 | `pancake-pos-mcp` row, `PARTIALLY_ABSORBED` | legacy harvest closeout ledger | VALUE_SET | ACCEPT |
| The MCP-approval-proof reopen condition named above was already closed as documentation-only in a prior connector spec | `docs/reference/archive/CVF_LHW16_T2_MCP_APPROVAL_PROOF_ADVISORY_CONNECTOR_SPEC_2026-05-30.md` | `LH1 Trigger Closure` section | `pancake-pos-mcp` - LH1 line 141; `ABSORBED (documentation-only connector scope)` | LHW16-T2 connector spec | VALUE_SET | ACCEPT |
| A separate legacy-spec-absorption registry row marks the generic MCP business adapter as `runtime-owned` absorbed with the Pancake-specific profile deferred | `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` | line 120 | `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/` row, `runtime-owned` | legacy spec absorption registry | VALUE_SET | ACCEPT |
| High-value upstream repo absorption should use a source mirror when available | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | Source Mirror Discipline | `.private_reference/source_mirrors/` | external absorption core standard | LITERAL_INVARIANT | ACCEPT |
| Source mirror index now records the PPMCP-R1 pinned mirror row | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger | `nguyennguyenit__pancake-pos-mcp` | source mirror index | VALUE_SET | ACCEPT |
| Aggregate corpus registry generator exists and defines a `main` entry point | `governance/compat/generate_corpus_scan_registry.py` | function definition line | `main` | corpus scan registry generator | VALUE_SET | ACCEPT |

## Current Runtime Freshness Verification

| Claim checked | Verification command | Observed result | Disposition |
|---|---|---|---|
| No CVF Pancake-specific runtime extension exists | `Test-Path 'EXTENSIONS/CVF_PANCAKE_POS_MCP_ADAPTER'` (or equivalent bash `[ -d ... ]` check) | not present in repository tree | ACCEPT |
| No Pancake-specific checker exists | `Test-Path 'governance/compat/check_pancake_pos_mcp*.py'` | not present in repository tree | ACCEPT |
| Current MCP business adapter contract exists and predates this dispatch | `Test-Path 'EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts'` | `True`; 328 lines | ACCEPT |
| Current MCP business adapter contract has a paired test file | `Test-Path 'EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mcp.business.adapter.contract.test.ts'` | `True`; 207 lines | ACCEPT |
| Upstream mirror worktree is present and git-pinned | `git -C ".private_reference/source_mirrors/nguyennguyenit__pancake-pos-mcp" rev-parse HEAD` | `41979fdac4fdf9a8a6f956889c33f19fa3389215` | ACCEPT |

Freshness boundary: these checks support only the negative runtime/package
claim boundary for PPMCP-R1 dispatch authoring. They do not prove absence of
every possible future Pancake-POS-related string, and they do not authorize
runtime activation.

## Negative Search And Collision Discipline

Search roots: repository root, excluding `.git`; scoped confirmations against
`EXTENSIONS/`, `governance/compat/`, and `docs/reference/agent_system_skills/`.

Search command or structured query: filesystem existence checks
(`Test-Path`-equivalent) plus `git -C` metadata reads, recorded row-by-row in
the `## Current Runtime Freshness Verification` table above.

Coverage across source/tests/docs/JSON/external evidence: checks covered
`EXTENSIONS/` runtime source, `governance/compat/` checker source, and
`docs/reference/agent_system_skills/` package registry; no upstream or
legacy source claim used a bare `NOT FOUND` disposition without this
coverage note.

Same-token collision result and absent-versus-not-binding disposition: the
two negative-existence path tokens in this baseline
(`EXTENSIONS/CVF_PANCAKE_POS_MCP_ADAPTER`,
`governance/compat/check_pancake_pos_mcp*.py`) also occur in the paired work
order because both packets record the same freshness check. Those paired
occurrences are non-authoritative documentation collisions, not evidence that
either target path exists. The scoped filesystem checks remain the binding
absence evidence for this packet.

- `EXTENSIONS/CVF_PANCAKE_POS_MCP_ADAPTER`: non-authoritative same-token
  collision occurs in the paired work order's duplicate freshness check;
  this occurrence is not binding on filesystem absence.
- `governance/compat/check_pancake_pos_mcp*.py`: non-authoritative same-token
  collision occurs in the paired work order's duplicate freshness check;
  this occurrence is not binding on filesystem absence.

Per-token collision disposition for nearby all-caps/camelCase tokens
surfaced by proximity scanning around the `NOT FOUND` claims above:

- `CVF`: this token has a same-token, non-authoritative collision
  throughout the repository (it is the project name and appears in nearly
  every governed file); its occurrence elsewhere is not binding on the
  specific negative-existence claim about the Pancake-specific extension
  path.
- `OWNER_SURFACE_NOT_FOUND`: this token has a same-token, non-authoritative
  collision because it is a shared vocabulary enum value defined by
  `governance/compat/check_external_absorption_overlap_discipline.py` and
  used across many external-absorption artifacts; its occurrence elsewhere
  is not binding on this baseline's specific overlap-classification rows.

`BLOCKED_SOURCE_NOT_FOUND` and `NOT FOUND` are used only as literal
enum/vocabulary tokens defined by the External Absorption Core and Source
Verification standards cited in this baseline, not as a disposition claim
about any specific CVF source; their absence-disposition is `not binding`
on this dispatch-authoring packet because no row in the Source
Verification Block above actually uses `BLOCKED_SOURCE_NOT_FOUND` as a row
disposition.

## Evidence / Verification

Dispatch-authoring verification is bounded to source mirror presence,
independently recomputed file counts, source mirror index control-plane
update, runtime-freshness negative checks, and pre-dispatch governance gates.
Absorption completion evidence is assigned to the future worker audit and
must not be claimed by this baseline.

## External Absorption Core

| Field | Value |
|---|---|
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | `https://github.com/nguyennguyenit/pancake-pos-mcp.git` at `41979fdac4fdf9a8a6f956889c33f19fa3389215`; local mirror `.private_reference/source_mirrors/nguyennguyenit__pancake-pos-mcp/`; secondary legacy folder `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/` |
| Enumeration command | `git -C ".private_reference/source_mirrors/nguyennguyenit__pancake-pos-mcp" ls-files` (98 rows); recursive filesystem enumeration of the 9-file legacy folder |
| Manifest artifact or inline manifest | inline `## Dispatch Bounded Corpus Manifest` table in this baseline; full 107-row file-level manifest with SHA-256 and byte counts required in the planned worker audit |
| Processing ledger artifact or inline ledger | planned worker audit under `docs/audits/CVF_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mcp.business.adapter.contract.test.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts`; `governance/contracts/tool-action-taxonomy.ts`; plus planned worker owner-surface delta in the audit artifact |
| Unresolved items | 107 unresolved at dispatch-authoring time (worker has not yet run); worker must reduce to 0 or return `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| Completion claim boundary | dispatch-authoring and source-mirror intake only; no runtime, provider/live, public, production, MCP transport, install, checker, or package activation |

## Corpus Completeness And Report Integrity

- Corpus task class: KNOWLEDGE_ABSORPTION
- Corpus root: `.private_reference/source_mirrors/nguyennguyenit__pancake-pos-mcp/` (98 upstream files) plus `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/` (9 legacy files); combined bounded corpus of 107 files.
- Snapshot time: 2026-07-25 local session.
- Enumeration command: `git -C ".private_reference/source_mirrors/nguyennguyenit__pancake-pos-mcp" ls-files`; recursive filesystem walk of the legacy folder.
- Manifest artifact or inline manifest: dispatch-authoring recomputed counts and aggregate digest recorded here; full 107-row file-level manifest required in the planned worker audit.
- Manifest hash: `sha256:7deb1ef3b1e31b5770a88039126b0a91d93b3de6c3b40bb4aac7424374f83696` (aggregate digest per the recipe in `## Deterministic Manifest Hash Recipe` below, independently recomputed by the reviewer over all 107 rows).
- Processing ledger artifact or inline ledger: planned worker audit.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=107; ledger_terminal=0 at dispatch-authoring time; exclusions=0; unresolved=107.
- Unresolved files: 107 at dispatch-authoring time.
- Declared exclusions: none.
- Unreadable or unsupported files: none known at dispatch-authoring time.
- Aggregation check: dispatch-authoring proves source availability and count reconciliation (98 + 9 = 107), not absorption completion.
- Drift check: worker must recompute upstream commit, both file counts, and the aggregate manifest digest before processing, and treat any mismatch as `STALE_SNAPSHOT`.
- Output traceability: worker maps accepted value to CVF owner surfaces or returns blocked source gaps in the audit artifact.
- Adversarial verification: worker must challenge the a-priori expectation (from the prior `PARTIALLY_ABSORBED`/LHW16-T2/`runtime-owned` disposition trail cited in this baseline's Source Verification Block) that most legacy concepts are already `CONFIRMED_EXISTING`, rather than assuming it without a file-level comparison.
- Corpus verdict: PARTIAL

## External Repository Absorption Entry Control

| Field | Disposition |
|---|---|
| Source type | pinned upstream external repository (`nguyennguyenit/pancake-pos-mcp`) plus secondary retained legacy interpretation folder |
| Upstream or source-mirror disposition | pinned source mirror is authority for upstream facts; legacy folder is secondary comparison material only |
| Enumeration or manifest plan | `git -C ".private_reference/source_mirrors/nguyennguyenit__pancake-pos-mcp" ls-files` for 98 upstream files; recursive filesystem enumeration for 9 legacy files; combined 107-file bounded corpus per the `## Deterministic Manifest Hash Recipe` below |
| Per-file terminal-ledger plan | planned worker audit records one of READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, or BLOCKED_UNREADABLE for each of the 107 files |
| Owner or overlap route | compare against `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` and `governance/contracts/tool-action-taxonomy.ts`; record CONFIRMED_EXISTING, ENRICH_EXISTING, NEW_FINDING, REJECT_DIRECT_IMPORT, NO_NEW_VALUE, or OWNER_SURFACE_NOT_FOUND per item |
| Value-disposition route | value conversion matrix records DOCTRINE_ADAPTED, PACKAGE_CANDIDATE, RUNTIME_CANDIDATE, CHECKER_CANDIDATE, REJECT_DIRECT_IMPORT, or NO_PACKAGE_OR_RUNTIME_VALUE per item or group |
| Claim boundary | dispatch-authoring and future worker audit only; no runtime, provider/live, public, production, MCP transport, checker, or package activation |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | `.private_reference/source_mirrors/nguyennguyenit__pancake-pos-mcp/`; `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/` |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | scope-triggered bounded pinned-upstream-plus-legacy re-intake |
| Blind-spot prevention action | worker must enumerate and reconcile all 107 bounded-corpus files before accepting or rejecting value |
| Residual gap | worker must return `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW` or `BLOCKED_WITH_REASON` if any manifest item cannot receive a terminal disposition |

## Deterministic Manifest Hash Recipe

This exact recipe must be reproduced verbatim by the worker; do not
paraphrase or infer an equivalent recipe.

1. Path form: workspace-relative to the bounded corpus, forward-slash
   normalized. Upstream rows are prefixed `upstream/` followed by the `git
   ls-files` relative path. Legacy rows are prefixed `legacy/` followed by
   the path relative to `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/`.
2. Ordering: ordinal (byte-value) ascending sort on the prefixed relative
   path string.
3. Per-file hash: SHA-256 over the raw file bytes as stored on disk; no line-
   ending normalization, no text decoding.
4. Per-file byte count: raw on-disk byte length.
5. Aggregate digest: SHA-256 over the UTF-8 bytes of the newline-joined
   string `<relpath>\t<sha256>\t<bytecount>` for every one of the 107 rows in
   sorted order, with exactly one trailing newline after the last row, no
   byte-order mark.

## Rescan Intelligence Hardening

- Original source artifact:
  `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (line 141, `pancake-pos-mcp` row)
- Predecessor intake artifact:
  `docs/reference/archive/CVF_LHW16_T2_MCP_APPROVAL_PROOF_ADVISORY_CONNECTOR_SPEC_2026-05-30.md`
- Delta ledger status: PARTIAL - dispatch-authoring identifies that the prior
  `PARTIALLY_ABSORBED` disposition and doc-only LH1 closure were based on
  reading the 9-file legacy interpretation folder and W3 taxonomy work, not
  a pinned upstream mirror; the 98-file upstream repository was never
  file-level reconciled before this baseline.
- Routing matrix status: DO_NOW for no-commit bounded re-intake audit;
  SEPARATE_RUNTIME_TRANCHE for any runtime/package/checker implementation;
  OUT_OF_SCOPE for public-sync, direct import, and MCP transport execution.
- Semantic sampling status: PARTIAL - dispatch-authoring samples the current
  MCP business adapter contract, the tool-action taxonomy, and the legacy
  `Thong_tin.md` proposal; worker must complete the full 107-file comparison.
- Rescan intelligence verdict: PARTIAL

### Original-Intake Delta Ledger

| Delta category | Status |
|---|---|
| UNCHANGED_FROM_INTAKE | `pancake-pos-mcp` remains advisory external source material, not CVF source of truth; direct import remains rejected. |
| CHANGED_DISPOSITION | Source authority changes from an unpinned legacy-only reading to a pinned upstream source mirror plus the legacy folder as secondary comparison material. |
| NEW_FINDING | The current upstream mirror contains 98 tracked files (tools, Zod schemas, response-projection, replay fixtures, worker/server transport) that have never been individually compared against `mcp.business.adapter.contract.ts`. |
| REMOVED_OR_REJECTED | Direct source import, runtime execution, MCP transport activation, dependency install, and test/build execution remain rejected for this dispatch and for the bounded worker tranche. |

### Follow-Up Routing Matrix

| Routing lane | Status |
|---|---|
| DO_NOW | Author this dispatch packet; then, after independent review, dispatch the no-commit worker audit. |
| SEPARATE_RUNTIME_TRANCHE | Any Pancake-specific runtime extension, MCP transport activation, checker implementation, package mutation, or provider/live proof. |
| STRATEGIC_OPERATOR_DECISION | Operator must select whether any surviving delta becomes runtime, package, checker, or roadmap work after the worker audit closes. |
| OUT_OF_SCOPE | Public-sync, benchmark, production-readiness claim, direct import, dependency install, and session-state mutation. |
| RESOLVED_BY_DESIGN | Private source mirror and legacy folder remain read-only and git-ignored/reference-only; CVF-owned outputs carry conclusions. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| PPMCP-R1-B-RS1 | source mirror git metadata | upstream commit is pinned at `41979fdac4` | DO_NOW | Could a future worker rely on a stale local read instead of re-verifying `git rev-parse HEAD` against this baseline's value? | PASS_PINNED_MIRROR_REQUIRED |
| PPMCP-R1-B-RS2 | legacy `Thong_tin.md` proposal | legacy folder proposes 8 files mapping into `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp-business-adapter/` | NEW_FINDING pending worker verification | Could the worker assume the proposal is fully absorbed merely because a same-named contract file already exists, without a field-level comparison? | CHALLENGE_OPEN_WORKER_MUST_COMPARE_FIELDS |
| PPMCP-R1-B-RS3 | prior LHW16-T2 closure | `pancake-pos-mcp` LH1 trigger already closed doc-only | CONFIRMED_EXISTING candidate | Could dispatch-authoring over-conclude `NO_NEW_VALUE` for the entire corpus because one narrow reopen condition was already closed? | CHALLENGE_OPEN_WORKER_MUST_COMPARE_ALL_107_FILES |
| PPMCP-R1-B-RS4 | upstream `src/shared/schemas.ts`, `src/shared/response-projection.ts`, `tests/replay/` | upstream repo contains Zod schemas, compact response projection, and replay fixtures not present in the 9-file legacy folder | NEW_FINDING pending worker verification | Could the worker under-scan the upstream repo by treating the already-reconciled legacy folder as a proxy for the full upstream repo? | CHALLENGE_OPEN_WORKER_MUST_TREAT_UPSTREAM_AND_LEGACY_SEPARATELY |

## Dispatch Bounded Corpus Manifest

| Manifest item | Evidence |
|---|---|
| Upstream repository | `https://github.com/nguyennguyenit/pancake-pos-mcp.git` |
| Pinned commit | `41979fdac4fdf9a8a6f956889c33f19fa3389215` |
| Local upstream mirror path | `.private_reference/source_mirrors/nguyennguyenit__pancake-pos-mcp/` |
| Upstream tracked file count | 98 (independently recomputed via `git ls-files`) |
| Legacy folder path | `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/` |
| Legacy file count | 9 (independently recomputed via recursive filesystem enumeration) |
| Combined bounded corpus | 107 |
| Aggregate manifest digest (reviewer recompute) | `sha256:7deb1ef3b1e31b5770a88039126b0a91d93b3de6c3b40bb4aac7424374f83696` |
| Full file-level manifest (per-file SHA-256 and byte count) | REQUIRED in planned worker audit, using the recipe in `## Deterministic Manifest Hash Recipe` |

## Mandatory Audit Questions (Non-Predetermined)

The future worker must specifically compare these candidate regions without
assuming they should be absorbed, and without assuming `NO_NEW_VALUE`:

- Zod/discriminated action schemas (`src/shared/schemas.ts`) versus current
  CVF contract schemas in `mcp.business.adapter.contract.ts` and
  `tool-action-taxonomy.ts`;
- action-level read/write/mutation separation versus current tool-level
  risk classification;
- approval-reference semantics (`approvalReference`, `approvalReason` in
  `MCPBusinessToolInvocationRequest`) and whether approval evidence is
  actually authoritative anywhere in current runtime;
- transport separation (`src/worker.ts`, `src/server.ts`, `wrangler.toml`)
  and remote authentication boundary versus `MCPBusinessTransport` and
  `ToolTransport`;
- rate limit, retry, timeout, and failure classification patterns in the
  upstream API client (`src/api-client/`);
- compact response projection (`src/shared/response-projection.ts`,
  `src/shared/compact-masks.ts`) and its possible quota/context-value;
- stable/canonical serialization and receipt correlation versus
  `MCPBusinessExecutionReceipt`;
- replay fixtures (`tests/replay/`) and negative mutation tests
  (`tests/fixtures/orders-delete/`) as possible checker-candidate or
  fixture-candidate value;
- display-ID resolution and safe entity targeting
  (`src/tools/orders-tool.ts`, its delete fixtures, and related resolver
  tests);
- input/output validation coverage versus current schema validation;
- DLP, secret, and PII handling (`.env.example`, `.dev.vars.example`,
  `src/config.ts`);
- idempotency and replay protection;
- durable receipt persistence versus in-memory receipt objects;
- provider/tool discovery snapshot, tool schema attestation, and version
  pinning (`src/tools/tool-registry.ts`, `src/resources/resource-registry.ts`);
- differences between stdio, HTTP, and Cloudflare Worker surfaces
  (`wrangler.toml`, `.githooks/pre-commit`).

Known-risk observations recorded above are investigation leads, not accepted
findings. The worker must not pre-conclude a disposition for any of these
regions before completing the file-level comparison.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror plus secondary legacy folder -> external absorption core -> full manifest and processing ledger -> value conversion matrix -> overlap and novelty classification against existing owner surfaces -> CVF owner-surface delta -> future package/runtime/checker work order only if separately authorized |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | `docs/baselines/CVF_GC018_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md` |
| Disposition | REVIEWER_ACCEPTED_DISPATCH_READY_WITH_REPAIRS for the bounded pinned-upstream-plus-legacy re-intake worker |
| Claim boundary | dispatch-authoring only; no runtime, package activation, checker wiring, provider/live proof, public-sync, MCP transport, or production-readiness claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| Upstream source mirror control plane | Current `pancake-pos-mcp` source authority is now pinned for future absorption instead of relying on the unpinned legacy-only reading. | DOCTRINE_ADAPTED | `.private_reference/source_mirrors/INDEX.md` | Use upstream mirror as source authority for PPMCP-R1 facts. | No runtime or package behavior |
| Legacy `Thong_tin.md` 8-file adapter proposal | Prior proposal already substantially overlaps `mcp.business.adapter.contract.ts` (risk class, transport, approval decision, execution receipt); exact overlap is unverified at file-field level. | DOCTRINE_ADAPTED | planned PPMCP-R1 audit and owner-surface comparison | Worker performs field-level comparison and records `CONFIRMED_EXISTING` or `ENRICH_EXISTING` per field, not a blanket claim. | Documentation/reference only |
| Upstream Zod schemas, response projection, and replay fixtures | May contain concrete enrichment delta not present in the legacy folder or current CVF contracts; not yet compared. | RUNTIME_CANDIDATE | pending PPMCP-R1 audit and conditional reopen index if value survives | Worker records candidate evidence and reopen condition only if a concrete delta is found; implementation requires a fresh runtime work order. | No install, no MCP transport, no runtime wiring, no provider/live proof |
| Replay fixtures and negative mutation test patterns | Possible checker-candidate or fixture-candidate value for future CVF-native test hardening. | CHECKER_CANDIDATE | pending PPMCP-R1 audit and conditional reopen index if value survives | Worker records candidate evidence and reopen condition only if a concrete gap is demonstrated. | No Python checker or hook-chain wiring |
| Upstream implementation files (tools, worker, server, API client) | Direct import remains rejected regardless of comparison outcome. | REJECT_DIRECT_IMPORT | CVF-native rewrite lanes only | Worker rejects direct copy/wiring and records reasons per file or file group. | No direct source import |
| Material already covered by W3 taxonomy and LHW16-T2 closure | Some legacy and upstream concepts may fully duplicate already-absorbed W3/LHW16-T2 value. | NO_PACKAGE_OR_RUNTIME_VALUE | existing `governance/contracts/tool-action-taxonomy.ts` and LHW16-T2 connector spec | Worker records explicit `NO_NEW_VALUE` reason per file or file group where duplication is confirmed. | No runtime or package behavior |
| Upstream tool surface as a whole (24 tool files under `src/tools/`) | Not yet evaluated for ASSF package/skill shape at dispatch-authoring time; no existing CVF package candidate targets Pancake POS specifically. | PACKAGE_CANDIDATE | pending PPMCP-R1 audit and conditional reopen index only if a concrete package-shaped delta is found | Worker evaluates whether any coherent package/skill boundary exists; if none is found, worker records `NO_PACKAGE_OR_RUNTIME_VALUE` instead for this row in the audit. | No package root, `SKILL.md`, ASSF registry mutation, or activation |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Legacy `mcp-business-risk-classifier.ts`, `mcp-business-transport-policy.ts`, `mcp-business-execution-receipt.ts` proposals | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` (`MCPBusinessRiskClass`, `MCPBusinessTransport`, `MCPBusinessExecutionReceipt`) | CONFIRMED_EXISTING | Field names and enum values in the current contract closely match the legacy proposal's risk/transport/receipt shapes; worker must verify field-by-field rather than accept this dispatch-authoring observation as final. | worker confirms or narrows this disposition with a field-level table in the audit |
| Legacy `mcp-business-approval-gate.ts` approval-reference proposal | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` (`MCPBusinessApprovalGateResult`, `approvalReference`); `governance/contracts/tool-action-taxonomy.ts` (`ToolActionApprovalState`, `runtimeExecutionAuthorized`) | ENRICH_EXISTING | Two existing owner surfaces cover overlapping but not identical approval semantics; whether current runtime treats `approvalReference` as authoritative evidence versus advisory is unverified. | worker checks whether approval-reference authoritativeness is a real enrichment delta or already fully covered |
| Upstream `src/shared/schemas.ts`, `src/shared/response-projection.ts`, `src/shared/compact-masks.ts` | OWNER_SURFACE_NOT_FOUND: no current CVF owner surface identified for compact response projection or context-budget masking in the MCP adapter plane | OWNER_SURFACE_NOT_FOUND | Upstream-only material with no legacy-folder analog; genuinely unexamined before this dispatch. | worker performs full read and records ABSORB/ADAPT/DEFER/REJECT/NO_NEW_VALUE with owner-surface recommendation |
| Upstream `tests/replay/`, `tests/fixtures/orders-delete/` | OWNER_SURFACE_NOT_FOUND: no current CVF owner surface identified for replay-fixture or negative-mutation-test patterns in this plane | OWNER_SURFACE_NOT_FOUND | Upstream-only material; potential checker/fixture candidate value is unverified. | worker performs full read and records disposition with reopen condition if value is real but not immediately actionable |
| Prior LHW16-T2 `pancake-pos-mcp` LH1 closure scope (MCP approval proof advisory only) | `docs/reference/archive/CVF_LHW16_T2_MCP_APPROVAL_PROOF_ADVISORY_CONNECTOR_SPEC_2026-05-30.md` | CONFIRMED_EXISTING | The narrow MCP-approval-proof-advisory reopen condition from LH1 line 141 remains closed; PPMCP-R1 does not reopen it. | worker cites this closure and does not re-litigate the approval-proof-advisory scope |

## Conditional Reopen Handling

At dispatch-authoring time, no `PACKAGE_CANDIDATE`, `RUNTIME_CANDIDATE`, or
`CHECKER_CANDIDATE` disposition has been finalized; the value-conversion
matrix rows above are provisional and pending worker verification. This
baseline does not add a row to
`docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md`
at this time.

`NO_CONDITIONAL_REOPEN_INDEX_ENTRY_WITH_REASON`: dispatch-authoring has not
yet produced a worker-verified candidate. The planned worker audit must
propose an exact add/update/cite/decline disposition once file-level
comparison completes. The reviewer owns any resulting conditional reopen
index edit during closure; the index is not in worker write scope.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | planned PPMCP-R1 audit and corpus registry entry | internal CVF agents may read documentation/reference output only; no action authority | this baseline and its paired work order | N/A with reason: no internal runtime adapter is implemented | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future MCP adapter owner, not this dispatch | external agent use requires separate source-verified adapter/runtime authorization | upstream `pancake-pos-mcp` has stdio/HTTP/Cloudflare-Worker MCP surfaces; CVF has not implemented an equivalent runtime adapter | deferred adapter owner; no ingress, auth, mutation, raw-data, receipt, or public boundary is implemented here | DEFERRED_WITH_REASON |

## Package Skill Productionization Control Block

- SOP source: docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md
- Current phase: N/A with reason: PPMCP-R1 dispatch-authoring does not create, approve, activate, or mutate a package skill.
- Target lifecycle state: CANDIDATE_ONLY_REFERENCE
- Prior phase evidence: no existing ASSF package candidate for `pancake-pos-mcp`; the only existing owner surfaces are the current `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` MCP business adapter contract and taxonomy.
- Next forbidden skip: no package root, `SKILL.md`, generated package index mutation, truth packet, ACTIVE state, certification, or activation evidence may be created in PPMCP-R1.
- Runtime/provider proof: N/A with reason: runtime/provider proof is forbidden by this dispatch boundary.
- Claim boundary: package-related findings may be recorded only as candidate evidence for a future source-verified package work order.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| contractSource | ratified canonical contract, not an active or archived handoff: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; stable front door: `docs/reference/agent_handoff/README.md` |
| activeHandoff | `AGENT_HANDOFF_V52_2026-07-25.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | dispatcher/packet-author -> independent reviewer/closer -> worker (future, after reviewer authorization) -> reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING (current); INDEPENDENT_REVIEW (next); EXECUTION; REVIEWER_CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`58e9799a9`; reviewBaseHead=reviewer captures at review start; executionBaseHead=future worker captures with `git rev-parse --short HEAD`; closureBaseHead=reviewer captures before material commit |
| changedSetScope(phase) | packet-author phase changes only the three Allowed Outputs listed in this baseline's Scope section; a future worker may change only the four planned worker outputs named in the paired work order |
| traceScope(phase, actor) | this baseline and its paired work order carry full Agent Operation Trace Block evidence; a future worker return must add its own |
| commitOwner(phase) | packet-author must not commit or stage; independent reviewer decides `DISPATCH_READY` disposition; worker (once dispatched) must not commit; reviewer/closer owns any accepted material commit |
| crossBatchIsolation | this dispatch-authoring batch must not be mixed with worker execution, session/handoff sync, or runtime/package/checker work |
| nextMoveSurfaces | packet-author must not edit session state, active handoff, or roadmap files; reviewer or session-sync steward updates these only after independent review disposition |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_COMPLETION_2026-07-25.md` |
| reviewerOwnedClosurePaths | completion review; `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` only if a worker-verified candidate survives; accepted worker audit, registry entry, regenerated aggregate, and worker return; later session-sync paths remain separate |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external_absorption`, role=`dispatcher`,
lifecyclePhase=`pre_dispatch`, surfaceSelector=`MCP`, riskCeiling=`HIGH`,
maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: the packet author invoked
`governance/compat/run_adif_defect_resolver.py` with the exact query above
(`--task-class external_absorption --role dispatcher --lifecycle-phase
pre_dispatch --surface-selector MCP --risk-ceiling HIGH --max-results 20
--json`) and it returned `totalCandidates=0`. A dash-separated variant of
the same query (`external-absorption`, `pre-dispatch`) was also checked as
a naming-convention sanity check and likewise returned zero.

## Planned Worker Fulfillment Manifest

| Required output | Path | Owner | Status |
|---|---|---|---|
| PPMCP-R1 bounded re-intake audit | `docs/audits/CVF_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md` | worker | PLANNED |
| Corpus registry entry | `docs/corpus-intelligence/registry/entries/ppmcp-r1-pinned-upstream-and-legacy-delta-reintake.json` | worker | PLANNED |
| Corpus registry aggregate (regenerated only via `python governance/compat/generate_corpus_scan_registry.py`) | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | worker | PLANNED |
| Worker return | `docs/reviews/CVF_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_WORKER_RETURN_2026-07-25.md` | worker | PLANNED |
| Material commit (if accepted) | accepted worker outputs committed by reviewer only | reviewer | PENDING_REVIEW |
| Session sync | update front door/state/handoff after material acceptance if next move changes | session-sync steward | PENDING_REVIEW |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | packet-author agent role |
| Provider or surface | local workspace |
| Session or invocation | PPMCP-R1 dispatch packet authoring, 2026-07-25 |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, Grep, Glob, Bash (git, python hashing script, governance gates) |
| Target paths | `.private_reference/source_mirrors/INDEX.md`; `docs/baselines/CVF_GC018_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md` |
| Allowed scope source | operator instruction 2026-07-25 to author a bounded PPMCP-R1 dispatch packet, packet-author-only, `DRAFT_PENDING_REVIEW` for Codex independent review |
| Before status evidence | clean worktree at `58e9799a9` before dispatch-authoring edits; `.private_reference/source_mirrors/nguyennguyenit__pancake-pos-mcp/` already present as an untracked mirror clone (ignored by `.private_reference/source_mirrors/.gitignore`) |
| After status evidence | three Allowed Outputs changed; mirror payload itself untouched (git-ignored, not part of any commit) |
| Diff evidence | `git status --short --untracked-files=all` and `git diff --cached --name-status` recorded in the final return |
| Approval boundary | dispatch-authoring only; no dispatch disposition claimed by the packet author |
| Claim boundary | no runtime, provider/live, public, production, MCP transport, package activation, checker wiring, or direct import |
| Agent type | packet-author (dispatcher role, not worker) |
| Invocation ID | PPMCP-R1-packet-authoring-2026-07-25 |
| Expected manifest | `.private_reference/source_mirrors/INDEX.md`; `docs/baselines/CVF_GC018_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md` |
| Actual changed set | `.private_reference/source_mirrors/INDEX.md`; `docs/baselines/CVF_GC018_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this dispatch-authoring batch |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | PPMCP-R1 dispatch-authoring only: source mirror index update, this baseline, and the paired work order |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - dispatch-authoring records pinned commit, independently recomputed file counts, aggregate manifest digest, and ADIF resolver query result |
| actionEvidence | ACTION_EVIDENCE_PRESENT - source mirror index row added, GC-018 baseline created, work order created |
| invocationBoundary | local documentation and private source-mirror control-plane authoring only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | bounded pinned-upstream-plus-legacy re-intake dispatch packet authoring; no dispatch disposition asserted |
| forbiddenExpansion | no dependency install, no upstream test/server/Worker/hook execution, no MCP transport activation, no package activation, no checker implementation, no provider/live proof, no public-sync, no direct import, no commit, no session/handoff/roadmap edit |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline references a private source mirror and a private
legacy reference folder. Public-safe export requires a separate public-sync
authorization from the sibling public-sync clone.

## Independent Reviewer Disposition

Disposition: REVIEWER_ACCEPTED_DISPATCH_READY_WITH_REPAIRS

Reviewer repairs:

- corrected the aggregate manifest digest after an independent 107-row
  raw-byte recomputation found the packet-author value had omitted its final
  two hex characters;
- corrected the display-ID resolver source location to
  `src/tools/orders-tool.ts` and its delete fixtures/tests;
- removed the impossible worker-owned conditional-reopen-index update and
  assigned any surviving index change to the reviewer at closure;
- separated the worker return from the independent completion review and
  included the regenerated corpus registry aggregate in reviewer closure
  ownership;
- corrected the source mirror index description so Zod is attributed only to
  the upstream repository, not the 9-file legacy interpretation folder.

## Claim Boundary

This baseline records accepted PPMCP-R1 dispatch authoring: a source mirror
index update, this GC-018 baseline, and its paired work order. Its reviewer
acceptance authorizes only the bounded no-commit worker execution defined by
the paired work order. It
does not authorize dependency install, upstream test/server/Worker/hook
execution, MCP transport activation, external CLI/MCP agent invocation,
provider/API/account/network/browser use, package activation, package root
creation, checker implementation, CI mutation, provider/live proof,
public-sync, direct import, or production-readiness claims. This independent
review does not release any later runtime, package, checker, provider,
process-control, or public lane.

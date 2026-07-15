# CVF Agent Work Order - SOT3-APP-T0 Source Ledger And Provenance Disposition

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-07-15

Batch ID: `SOT3-APP-T0`

dispatchBaseHead: `baaf21cd2`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker return path:
`docs/reviews/CVF_SOT3_APP_T0_WORKER_RETURN_2026-07-15.md`

## Dispatch Prompt Envelope

Role: delegated source-intake and provenance-disposition worker for
`SOT3-APP-T0`.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_APP_T0_SOURCE_LEDGER_AND_PROVENANCE_DISPOSITION_2026-07-15.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker must capture the clean committed dispatch HEAD before
any edit and repeat it in the worker return.

Current-time notes: source snapshot and packet date are 2026-07-15; recompute
the full source and hidden-clone metadata snapshot rather than copying values
from this packet.

Do-not-misread notes: this is a documentation/evidence tranche. It does not
authorize SOT-Application or hidden-clone mutation, dependency synchronization,
install, build, typecheck, test, CI, server, browser, provider/live execution,
binding validation, contract ratification, or runtime integration.

Required first actions: read startup state, guard orientation, literal gotchas,
the SOT3-APP roadmap, paired GC-018, this packet, accepted intake review, full
literal 336-file source root, and output-applicable checker sources before
writing either worker artifact.

Return contract: create exactly the two planned outputs, run the required
documentation gates, leave all changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Freeze and terminally process all 336 SOT-Application files, reproduce the
accepted source snapshot, enumerate every declared hidden-CVF-clone path, and
give each declaration an evidence-backed provenance disposition without
executing or changing the application.

## Authority Chain

| Order | Authority | Evidence | Boundary |
|---:|---|---|---|
| 1 | operator authorization | accepted intake commit `24d50f0d7` | split roadmap and bounded first application packet |
| 2 | FSCB cross-batch release | accepted material closure `21659a3ac` | scheduling condition only; FSCB result is not application authority |
| 3 | SOT3-APP roadmap | `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md` | T0 source ledger and provenance disposition |
| 4 | paired GC-018 | `docs/baselines/CVF_GC018_SOT3_APP_T0_SOURCE_LEDGER_AND_PROVENANCE_DISPOSITION_2026-07-15.md` | exact source snapshot, methods, outputs, and exclusions |
| 5 | this work order | current path | worker execution contract |
| 6 | current CVF governed surfaces | source verification and later T1 owner ratification | CVF remains authority; copied folder is evidence input |

Provider-local memory, chat history, the copied application, and its hidden
clone are not CVF authority. Every closure claim must remain inside the
committed packet and directly recomputed evidence.

## Agent Roles

| Role | Responsibility | Commit authority |
|---|---|---|
| dispatcher | authors and commits roadmap/GC-018/work order | dispatch packet only |
| worker | enumerates, reads, hashes, classifies, writes exactly two outputs, runs gates | forbidden |
| reviewer/closer | independently recomputes manifest/provenance evidence, repairs allowed closure defects, accepts or rejects, commits accepted material | accepted closure material only |
| session-sync steward | updates protected continuity after accepted material closure | separate session-sync commit |

## Scope / Target / Owner Boundary

Allowed source root, read-only:
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application`.

Allowed hidden dependency target, read-only Git metadata only:
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\.Controlled-Vibe-Framework-CVF`.

The worker may run only these Git metadata classes against the hidden target:

- `rev-parse` for HEAD and repository identity;
- `status --short --branch` for worktree/branch state;
- `remote -v` for declared remote identity.

No fetch, pull, push, checkout, reset, clean, submodule, maintenance, or file
mutation is allowed in either external root.

Allowed current CVF reads include the roadmap, baseline, intake/rebuttal,
external-absorption standards, corpus standards, current SOT3 and T8 owner
front doors, and applicable checker sources. T0 may record provisional owner
routes; T1 retains runtime/contract owner ratification.

Allowed writes are exactly the two paths in Planned Worker Fulfillment
Manifest. Every other path is forbidden during worker execution.

Forbidden scope includes application or hidden-clone mutation, roadmap,
baseline, work-order, intake/rebuttal, session/handoff/generated-state,
Catalog/GAP/ADIF/index, checker/test/hook, runtime/product, package, public-sync,
provider/live/browser/server/API, install, build, typecheck, test, CI, or
binding-validation changes or commands.

## Write Ownership

| Path | Worker action | Owner boundary |
|---|---|---|
| `docs/reviews/CVF_SOT3_APP_T0_SOURCE_PROCESSING_AND_PROVENANCE_LEDGER_2026-07-15.md` | create | 336-file manifest, hashes, terminal decisions, declaration inventory, hidden-clone provenance dispositions |
| `docs/reviews/CVF_SOT3_APP_T0_WORKER_RETURN_2026-07-15.md` | create | execution evidence, gate evidence, claim boundary, and no-commit return |

Worker may not edit any pre-existing governed or external file.

## Dependency Release Evidence

| Dependency | Accepted artifact | Material commit | Final disposition | Release result |
|---|---|---|---|---|
| intake and operator authorization | `docs/reviews/CVF_SOT3_DOWNSTREAM_APPLICATION_AND_FOUR_SURFACE_ABSORPTION_INTAKE_REVIEW_2026-07-15.md` | `24d50f0d7` | `OPERATOR_AUTHORIZED_FOR_ROADMAP_AUTHORING` | PASS |
| FSCB scheduling condition | `docs/reviews/CVF_FSCB_ADAPT_T0_COMPLETION_2026-07-15.md` | `21659a3ac` | `REVIEWER_ACCEPTED_BOUNDED` | PASS |
| continuity release | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `baaf21cd2` | `sot3_app_t0_packet_authoring_next` | PASS |
| roadmap T0 release | `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md` | current dispatch batch | `T0_DISPATCH_READY` | PASS - T0 only |
| GC-018 source/claim boundary | `docs/baselines/CVF_GC018_SOT3_APP_T0_SOURCE_LEDGER_AND_PROVENANCE_DISPOSITION_2026-07-15.md` | current dispatch batch | `DISPATCH_READY` | PASS |

## Required First Reads

| Order | Path | Required action |
|---:|---|---|
| 1 | `CVF_SESSION_MEMORY.md` | FULL_READ |
| 2 | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | FULL_READ |
| 3 | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | FULL_READ |
| 4 | active handoff named by state | FULL_READ |
| 5 | `docs/reference/guard_orientation/README.md` | FULL_READ |
| 6 | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ |
| 7 | SOT3-APP roadmap, paired GC-018, and this work order | FULL_READ |
| 8 | `docs/reviews/CVF_SOT3_DOWNSTREAM_APPLICATION_AND_FOUR_SURFACE_ABSORPTION_INTAKE_REVIEW_2026-07-15.md` | FULL_READ |
| 9 | `docs/reference/external_agent_review/README.md` | FULL_READ |
| 10 | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | FULL_READ |
| 11 | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | FULL_READ |
| 12 | all 336 files under the literal source root | FULL_READ |
| 13 | checker files identified in Worker Output Checker Read-Ahead Mandate | SOURCE_VERIFIED |

## Pre-Flight Checks

1. Run `git rev-parse --short HEAD`; record it as `executionBaseHead`.
2. Require clean `git status --short` before the first write.
3. Confirm HEAD is the committed dispatch containing this exact packet.
4. Confirm both planned output paths are absent before creation.
5. Enumerate the source root directly with hidden files included.
6. Require exactly 336 files, 238522 bytes, and aggregate SHA-256
   `538d602504e1dec3e9b19581847aebdd73cb14a7490e8251a7cae16f5f9176dc`.
7. Recompute the hidden target existence, Git HEAD, branch/worktree state, and
   remote without changing it. Require short HEAD `a78b35c`, clean worktree,
   branch `main`, and the remote recorded by the baseline.
8. Stop for source or hidden-target drift; do not silently refresh the packet.
9. Read output-applicable checker sources before drafting either output.
10. Do not run any command declared forbidden in Scope / Target / Owner
    Boundary.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| operator authorized the SOT3-APP roadmap lane | VALUE_SET | `docs/reviews/CVF_SOT3_DOWNSTREAM_APPLICATION_AND_FOUR_SURFACE_ABSORPTION_INTAKE_REVIEW_2026-07-15.md` | Status and Decision / Disposition | `OPERATOR_AUTHORIZED_FOR_ROADMAP_AUTHORING` | governed intake review | ACCEPT |
| roadmap requires 336 terminal rows and zero unresolved hidden-clone paths | VALUE_SET | `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md` | Work Plan | `SOT3-APP-T0` | SOT3-APP roadmap | ACCEPT |
| current source snapshot is 336 files and 238522 bytes with a deterministic digest | VALUE_SET | `docs/baselines/CVF_GC018_SOT3_APP_T0_SOURCE_LEDGER_AND_PROVENANCE_DISPOSITION_2026-07-15.md` | Current External Source Snapshot | `aggregate digest` | paired GC-018 evidence carrier | ACCEPT |
| source manifest declares the hidden governance root | VALUE_SET | `docs/baselines/CVF_GC018_SOT3_APP_T0_SOURCE_LEDGER_AND_PROVENANCE_DISPOSITION_2026-07-15.md` | Current External Source Snapshot | `application manifest` | paired GC-018 evidence carrier | ACCEPT |
| seven binding target files resolve through the hidden clone | VALUE_SET | `docs/baselines/CVF_GC018_SOT3_APP_T0_SOURCE_LEDGER_AND_PROVENANCE_DISPOSITION_2026-07-15.md` | Current External Source Snapshot | `binding target family` | paired GC-018 evidence carrier | ACCEPT |
| environment and API config declare/default the hidden core path | VALUE_SET | `docs/baselines/CVF_GC018_SOT3_APP_T0_SOURCE_LEDGER_AND_PROVENANCE_DISPOSITION_2026-07-15.md` | Current External Source Snapshot | `environment default` | paired GC-018 evidence carrier | ACCEPT |
| hidden target exists as a clean Git clone at a recorded public remote and HEAD | VALUE_SET | `docs/baselines/CVF_GC018_SOT3_APP_T0_SOURCE_LEDGER_AND_PROVENANCE_DISPOSITION_2026-07-15.md` | Current External Source Snapshot | `hidden target` | paired GC-018 evidence carrier | ACCEPT |
| root package declares pnpm but no root lockfile is present | VALUE_SET | `docs/baselines/CVF_GC018_SOT3_APP_T0_SOURCE_LEDGER_AND_PROVENANCE_DISPOSITION_2026-07-15.md` | Current External Source Snapshot | `package manager` | paired GC-018 evidence carrier | ACCEPT |
| FSCB material closure released this cross-batch packet lane | VALUE_SET | `docs/reviews/CVF_FSCB_ADAPT_T0_COMPLETION_2026-07-15.md` | Decision / Disposition | `REVIEWER_ACCEPTED_BOUNDED` | FSCB completion review | ACCEPT |
| external absorption requires terminal ledger, value conversion, and overlap evidence | LITERAL_INVARIANT | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | External Absorption Core; Value Conversion; Overlap And Novelty Classification | `External Absorption Core` | external absorption standard | ACCEPT |
| corpus closure requires manifest and processing-ledger reconciliation | LITERAL_INVARIANT | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | Corpus Manifest; Processing Ledger; Reconciliation | `Corpus Completeness And Report Integrity` | GC-047 corpus standard | ACCEPT |

## New Doc-Only Fields

| Output | New fields | Classification | Boundary |
|---|---|---|---|
| source ledger rows | sourceId, relativePath, bytes, sha256, terminalStatus, disposition, valueClass, ownerRoute, reason | DOC_ONLY_NEW | evidence schema only |
| hidden-clone rows | declarationId, sourcePath, sourceLine, literalTarget, resolvedTarget, declarationClass, targetExists, repositoryHead, repositoryRemote, workingTreeState, ownerDisposition, versionDriftDisposition, runtimeUseDisposition, terminalProvenanceDisposition, evidence | DOC_ONLY_NEW | provenance evidence only |
| aggregate receipt | fileCount, totalBytes, aggregateSha256, snapshotTime, executionBaseHead | DOC_ONLY_NEW | reproducibility evidence only |

No proposed field is represented as an existing runtime, API, binding, or CVF
contract field.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Planned artifact | Acceptance evidence |
|---|---|---|---|
| 336-row terminal ledger | Required Inventory Method | source-processing and provenance ledger | 336/336 unique terminal rows |
| aggregate digest | Required Inventory Method | ledger aggregate receipt | exact count, bytes, and aggregate SHA-256 |
| declared hidden-clone path inventory | Hidden-Clone Provenance Method | ledger declaration section | every match retains source path, line, literal, class, and evidence |
| sever/govern/block disposition | Hidden-Clone Provenance Method | ledger declaration section | zero unresolved declaration row for complete return |
| reviewer semantic audit | Review Gate | ledger and worker return | independent manifest/provenance recomputation and semantic audit |
| no source mutation or application execution | Scope and Claim Boundary | both outputs | exact two-path changed set, no-commit evidence, forbidden-command count zero |

## Required Inventory Method

1. Enumerate all files recursively from the literal source root with hidden
   files included.
2. Normalize relative paths to forward slashes and sort ordinally by path.
3. Record byte length and lowercase SHA-256 for each file.
4. Build the aggregate digest from sorted lines shaped
   `relativePath<TAB>bytes<TAB>sha256<LF>`, UTF-8 encoded, then SHA-256 hashed.
5. Read every file body. JSON may be parsed for structure, but no source
   script, test, build, or binding-validation command may run.
6. Assign exactly one file terminal status: `ADAPTED`, `DEFERRED`, `REJECTED`,
   `NO_NEW_VALUE`, or `BLOCKED_UNREADABLE`.
7. Assign exactly one disposition: `ADAPT`, `DEFER`, `REJECT`,
   `NO_NEW_VALUE`, or `BLOCK`.
8. Assign exactly one value class: `DOCTRINE_ADAPTED`, `PACKAGE_CANDIDATE`,
   `RUNTIME_CANDIDATE`, `CHECKER_CANDIDATE`, `REJECT_DIRECT_IMPORT`, or
   `NO_PACKAGE_OR_RUNTIME_VALUE`.
9. Assign one provisional owner route: `SOT3_APP_T1`, `CURRENT_CVF_OWNER`,
   `DOWNSTREAM_APP_ONLY`, `NO_OWNER_VALUE`, or `OWNER_SURFACE_NOT_FOUND`.
10. Reconcile manifest=336, terminal=336, unique paths=336, exclusions=0, and
    unresolved=0 before returning complete.

Repeated or generated-like content may share a semantic reason, but every
physical file must retain its own row, bytes, hash, status, disposition, value
class, owner route, and reason.

## Hidden-Clone Provenance Method

1. Search every source body for the literal target fragment
   `../.Controlled-Vibe-Framework-CVF`, environment/config keys
   `CVF_CORE_PATH` and `CVF_WORKSPACE_ROOT`, binding-directory references, and
   any absolute hidden-clone path.
2. Record every physical match separately. Documentation/treeview matches are
   not deduplicated away from manifest, binding, environment, or code matches.
3. Classify each declaration as `MANIFEST_ROOT`, `BINDING_TARGET`,
   `ENVIRONMENT_DEFAULT`, `CODE_DEFAULT`, `DOCUMENTATION_REFERENCE`,
   `TREEVIEW_REFERENCE`, or `OTHER_DECLARATION`.
4. Normalize and resolve every literal target without following or modifying
   it. Record target existence.
5. Recompute read-only hidden-target metadata: full and short HEAD, branch,
   worktree state, and remotes. Do not contact the network.
6. Record `ownerDisposition` and `versionDriftDisposition` for each declaration.
   Current public-clone metadata is evidence, not proof that the declared
   dependency is acceptable.
7. Record `runtimeUseDisposition` as `DECLARED_ONLY_NOT_EXECUTED` unless direct
   static source establishes a narrower call path. Do not upgrade static source
   to executed behavior.
8. Assign exactly one terminal provenance disposition:
   `SEVER_REQUIRED`, `GOVERNED_VERSION_PIN_CANDIDATE`, `REFERENCE_ONLY`,
   `REJECT_DIRECT_IMPORT`, or `BLOCKED_UNRESOLVED`.
9. A complete return requires zero `BLOCKED_UNRESOLVED` declaration rows. If
   ownership, target, version, drift, or runtime-use disposition cannot be
   established, return `BLOCKED_WITH_REASON` instead.
10. Do not sever, rewrite, pin, fetch, or otherwise implement any disposition.

At minimum, the inventory must account for the manifest governance root, seven
binding target files, `.env.example`, API config default, and all documentation
or treeview references found by the full-source search.

## Execution Plan

1. Capture execution base and clean worktree evidence.
2. Recompute the source and hidden-target snapshots; stop on drift.
3. Enumerate, hash, and read all 336 files.
4. Build the per-file terminal ledger and aggregate receipt.
5. Build the complete hidden-clone declaration inventory and dispositions.
6. Reconcile counts, hashes, terminal totals, declaration totals, and zero
   unresolved items.
7. Write the worker return with exact two-path diff and no-commit evidence.
8. Run worker-return fast gate and all focused documentation gates.
9. Repair allowed-scope literal defects directly and rerun.
10. Return for independent reviewer/closer acceptance without committing.

## Evidence Requirements

- `executionBaseHead` and pre-write clean `git status --short`;
- exact source count, bytes, per-file hashes, and aggregate digest;
- 336 unique terminal rows with no missing or duplicate path;
- complete query inventory for hidden-clone declarations;
- exact hidden-target existence, HEAD, branch/worktree, and remote metadata;
- zero source or hidden-target writes;
- zero application, install, build, typecheck, test, CI, provider, browser,
  server, or binding-validation command;
- exact two-path changed set;
- output-applicable checker source read-ahead;
- gate results and final actual `git status --short`;
- HEAD unchanged from `executionBaseHead`.

## Corpus Completeness And Report Integrity

- Corpus task class: downstream SOT application source freeze and provenance
  disposition.
- Corpus root: literal source root in Scope / Target / Owner Boundary.
- Snapshot time: worker execution start at captured `executionBaseHead`.
- Enumeration command: filesystem-backed direct recursive `Get-ChildItem
  -File -Force` with ordinal normalized-path sorting.
- Manifest artifact or inline manifest: planned 336-row source-processing and
  provenance ledger.
- Manifest hash: deterministic aggregate digest defined in Required Inventory
  Method; dispatch expectation is
  `538d602504e1dec3e9b19581847aebdd73cb14a7490e8251a7cae16f5f9176dc`.
- Processing ledger artifact or inline ledger:
  `docs/reviews/CVF_SOT3_APP_T0_SOURCE_PROCESSING_AND_PROVENANCE_LEDGER_2026-07-15.md`.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE, ADAPTED, REJECTED, NO_NEW_VALUE.
- Reconciliation: manifest=336; ledger_terminal=336; exclusions=0; unresolved=0.
- Unresolved files: 0 required for complete return.
- Declared exclusions: none.
- Unreadable or unsupported files: none.
- Aggregation check: count, byte sum, per-file hashes, aggregate digest, and
  terminal distribution must reconcile.
- Drift check: compare exact source and hidden-target metadata to the committed
  dispatch baseline before writing.
- Output traceability: every file and declaration retains its physical source
  locator, evidence, terminal status/disposition, and reason.
- Adversarial verification: exact snapshot parity does not prove application
  quality, build reproducibility, runtime binding, or safe behavior.
- Corpus verdict: COMPLETE_VERIFIED - required for complete worker return;
  otherwise worker returns BLOCKED.

## Corpus-To-Knowledge-Map Reconciliation

| Check | Required result |
|---|---|
| source manifest coverage | 336 unique physical files |
| terminal ledger coverage | 336 unique rows; zero unresolved |
| hidden declaration coverage | every physical match accounted for separately |
| disposition coverage | each file and declaration has one terminal decision and reason |
| owner routing | provisional ownerRoute per file; owner/version/drift/runtime-use fields per declaration |
| silent-drop check | zero manifest row or query match absent from evidence tables |
| claim boundary | source/provenance evidence only; no runtime/as-built promotion |

## Planned Worker Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reviews/CVF_SOT3_APP_T0_SOURCE_PROCESSING_AND_PROVENANCE_LEDGER_2026-07-15.md` | create 336-row file ledger, aggregate receipt, hidden-clone declaration inventory, terminal dispositions, and reconciliation |
| `docs/reviews/CVF_SOT3_APP_T0_WORKER_RETURN_2026-07-15.md` | create no-commit execution return with evidence, gates, risks, and claim boundary |

No other worker-owned artifact is authorized.

## Near-Threshold Owner Maintainability Plan

| Planned output | Expected size | Maintainability disposition |
|---|---:|---|
| source-processing and provenance ledger | under 800 lines for 336 rows plus bounded evidence sections | keep one sortable ledger because splitting would break manifest/declaration reconciliation; rotate only if the machine size guard requires it |
| worker return | under 500 lines | evidence summary only; do not duplicate all 336 ledger rows |

The worker must not compress evidence by dropping rows merely to satisfy a line
target. Machine file-size policy controls.

## Acceptance Criteria

- [ ] execution base equals committed dispatch HEAD and pre-write worktree is clean;
- [ ] source snapshot is exactly 336 files and 238522 bytes;
- [ ] aggregate digest equals the committed expected SHA-256;
- [ ] 336 unique file rows reconcile with zero missing, extra, duplicate, or unresolved path;
- [ ] every file body was read or completion is blocked;
- [ ] terminal status, disposition, value class, owner route, and reason exist for every file;
- [ ] every hidden-clone declaration match retains its own physical source locator;
- [ ] manifest, seven binding targets, environment default, API config default, and all documentation/treeview matches are accounted for;
- [ ] hidden-target existence, HEAD, branch/worktree state, and remotes are recomputed without network or mutation;
- [ ] every declaration has owner, version/drift, runtime-use, and terminal provenance disposition;
- [ ] zero declaration remains `BLOCKED_UNRESOLVED` for complete return;
- [ ] no source/application/hidden-target/governed pre-existing file changed;
- [ ] no forbidden command ran;
- [ ] exact two-path changed set is recorded;
- [ ] required gates pass after output checker read-ahead;
- [ ] HEAD remains unchanged and worker commits nothing.

## Review Gate

Independent reviewer/closer must:

1. recompute the full 336-path/byte/hash manifest and aggregate digest;
2. compare every ledger row to physical source with zero mismatch;
3. rerun the hidden-clone query family and compare every physical match;
4. independently recompute hidden-target repository metadata;
5. read every `DEFERRED`, `REJECTED`, `NO_NEW_VALUE`, and hidden-clone row;
6. sample at least one source body from every remaining value/owner group;
7. verify no static declaration was upgraded to runtime proof;
8. run reviewer-fast and committed-range pre-closure gates;
9. accept, repair within reviewer-owned closure scope, or return with evidence.

## Current Runtime Freshness Verification

Runtime execution is not applicable to T0. Current-time facts are direct
filesystem and read-only Git metadata only. Any application behavior, binding
resolution, build, test, provider, server, or browser claim is forbidden.

## Closure Checklist

- [ ] worker return reviewed independently;
- [ ] full manifest and declaration query recomputed;
- [ ] semantic audit complete;
- [ ] allowed-scope repair rounds recorded;
- [ ] roadmap T0 state and Machine Closure Package updated by reviewer if accepted;
- [ ] accepted material committed separately from session sync;
- [ ] next move remains T1 packet authoring only after accepted T0 closure.

## Stop Conditions

Stop and return `BLOCKED_WITH_REASON` when:

- source count, bytes, aggregate digest, or any file hash drifts;
- hidden target is missing or its HEAD, worktree state, branch, or remote drifts;
- any source file is unreadable;
- any hidden-clone declaration cannot receive owner, version/drift,
  runtime-use, and terminal provenance disposition;
- a complete return would retain unresolved file or declaration rows;
- output completion requires changing a forbidden path;
- output completion requires executing an application/source command;
- checker repair would require scope expansion;
- a secret or destructive operation would be required.

## Return-To-Orchestrator Conditions

Return only for a stop condition, source contradiction, missing authority,
forbidden-path need, or scope expansion. Include the exact source path,
command evidence, failed invariant, and minimal next action. Literal gate
defects inside allowed scope remain worker-owned.

## Operator Checkpoint

Operator authorization for packet authoring and later delegated worker
execution is already present. No additional checkpoint is required inside T0.
Any source mutation, runtime/build/test/live/public work, or T1 contract choice
requires a later governed packet.

## Worker Autonomy / No-Question Rule

Worker must handle allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker must not
expand scope, self-select another task, or escalate an in-scope formatting
defect.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| dispatcher role | packet author only |
| worker role | distinct delegated no-commit source-intake worker |
| reviewer role | independent reviewer/closer |
| session-sync role | protected continuity steward after material acceptance |
| risk sensitivity | high; source drift, public-sync confusion, provider/live execution, secret exposure, and false readiness claims are prohibited |
| routing decision | `WORKER_MUST_NOT_COMMIT` |
| public route | `DEFERRED_PRIVATE_ONLY` |
| escalation condition | source drift, hidden-target drift, unreadable input, unresolved provenance, forbidden-path need, or scope expansion |

## Legacy Absorption Coverage Index Disposition

`NOT_APPLICABLE_WITH_REASON`: T0 evaluates the current operator-authored SOT
application and its hidden-clone coupling, not a legacy corpus row governed by
`docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md`. The index
is not modified. Reopen only after accepted T0 closure if the index still lacks
a useful downstream copied-folder entry and adding it would not delay the
higher-value T1 contract ratification.

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | downstream operator-provided copied-folder application |
| Upstream or source-mirror disposition | `LOCAL_OPERATOR_AUTHORED_INPUT_WITHOUT_UPSTREAM`; application root lacks Git provenance; declared hidden dependency is a separate public-sync clone |
| Enumeration or manifest plan | direct recursive filesystem enumeration with normalized paths, bytes, SHA-256, and aggregate digest |
| Per-file terminal-ledger plan | one physical row per 336 files using READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, SKIPPED_WITH_REASON, or BLOCKED_UNREADABLE vocabulary |
| Owner or overlap route | provisional T0 ownerRoute plus T1 contract-owner ratification |
| Value-disposition route | ABSORB, ADAPT, DEFER, REJECT, BLOCK, or NO_NEW_VALUE with independent semantic review |
| Claim boundary | source freeze and provenance disposition only |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | operator-provided copied-folder application outside the provenance repository |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | exact 336-file manifest, body read, terminal ledger, aggregate digest, and declaration query |
| Blind-spot prevention action | one physical row per file and per hidden-clone match before any semantic grouping |
| Residual gap | zero required at complete worker return |
| Blind-spot verdict | COMPLETE_VERIFIED required or worker returns blocked |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | literal source root in Scope / Target / Owner Boundary |
| Enumeration command | filesystem-backed direct recursive `Get-ChildItem -File -Force` enumeration |
| Manifest artifact or inline manifest | planned 336-row source-processing and provenance ledger |
| Processing ledger artifact or inline ledger | `docs/reviews/CVF_SOT3_APP_T0_SOURCE_PROCESSING_AND_PROVENANCE_LEDGER_2026-07-15.md` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, SKIPPED_WITH_REASON, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | per-file provisional ownerRoute plus declaration owner/version/drift/runtime-use disposition |
| Unresolved items | 0 required for complete worker return |
| Completion claim boundary | complete documentation-level source freeze and provenance disposition only |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| downstream domain/workflow source | product and contract candidate | PACKAGE_CANDIDATE | SOT3-APP roadmap | terminal T0 classification; T1 ratification | no package activation |
| hidden-clone manifests/bindings/config | provenance and authority coupling | RUNTIME_CANDIDATE | SOT3-APP T0/T1 | sever, govern with version evidence, reject, or block | no runtime resolution claim |
| application guard/phase declarations | static governance intent | CHECKER_CANDIDATE | current guard/phase owners | owner-gap classification only | no checker wiring |
| application documentation model | downstream product doctrine | DOCTRINE_ADAPTED | SOT3-APP roadmap | retain bounded evidence | no CVF Core promotion |
| duplicate local contracts and fixture proof | negative compatibility evidence | REJECT_DIRECT_IMPORT | T1/T3 repair ledger | reject as current CVF proof | no direct import |
| navigation/support/repeated summaries | context without independent product value | NO_PACKAGE_OR_RUNTIME_VALUE | source ledger | retain terminal reason | no package/runtime value |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| three-layer core contracts | `docs/reference/sot_three_layer/README.md` | CONFIRMED_EXISTING | application is a downstream consumer | source-verify in T1 |
| T8 packet binding | `EXTENSIONS/CVF_REFINERY/src/packet-hash/packet-hash.ts` | REJECT_DIRECT_IMPORT | local packet-ID path is insufficient | record defect; redesign only in T1+ |
| hidden public-clone dependency | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | unratified dependency owner/version boundary | terminal T0 provenance disposition |
| downstream application owner | OWNER_SURFACE_NOT_FOUND | NEW_FINDING | possible new sibling product owner | decide only after T0/T1 evidence |
| application-local governance-shaped source | current CVF guard/phase/evidence owners | ENRICH_EXISTING | downstream static use candidate | record without promotion |
| duplicated summaries/navigation | current roadmap/intake evidence | NO_NEW_VALUE | no independent owner value | terminal reason only |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | operator intake -> SOT3-APP roadmap -> T0 GC-018/work order -> no-commit ledger -> independent review -> later T1 decision |
| Matching local-view guard | `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | SOT3-APP roadmap and this work order |
| Disposition | ACCEPT_AS_SOURCE_FREEZE_AND_PROVENANCE_AUDIT_INPUT_ONLY |
| Claim boundary | copied folder and hidden target are evidence inputs, not CVF authority or runtime authorization |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| applicability | NOT_APPLICABLE_WITH_REASON |
| reason | T0 creates two governed markdown evidence files only and does not create or alter application/runtime storage, cache, index, database, source mirror, or generated aggregate layout |
| owner boundary | existing docs/reviews layout |
| future trigger | any later durable application storage or source-mirror proposal requires fresh GC-018 and source verification |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`External knowledge absorption`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "External knowledge absorption" --role dispatcher --lifecycle-phase pre-dispatch --json`

Returned defects: ADIF-0016; ADIF-0020; ADIF-0021; ADIF-0027

| DefectId | Dispatch application |
|---|---|
| ADIF-0016 | reusable declaration/provenance fields and terminal taxonomy are explicit |
| ADIF-0020 | output-applicable checker read-ahead is mandatory before writing |
| ADIF-0021 | real applicability headings and exact literal tokens are recorded without marker-only shortcuts |
| ADIF-0027 | reverse owner/overlap routing is explicit and cannot be skipped at closure |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | committed packet plus two uncommitted worker outputs | worker may read two external roots and write only planned outputs | manifest, hashes, declaration ledger, gates | local filesystem and read-only Git metadata | ACTIVE_BOUNDED |
| EXTERNAL_AGENT_CLI_MCP | no application ingress or adapter ratified | no CLI/MCP execution, binding resolution, or external-agent product claim | explicit deferred evidence | separate source-verified adapter roadmap | DEFERRED_WITH_REASON |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker output, read checker source for that file's docType,
path family, and conditional evidence class.

| Output artifact | Required read-ahead result |
|---|---|
| source-processing and provenance ledger under `docs/reviews/` | derive exact review structural headings, absorption core/value/overlap tables, corpus terminal vocabulary, epistemic fields, trace fields, and claim-boundary terms before writing |
| worker return under `docs/reviews/` | derive worker-return status/self-declaration/work-order markers, required headings, trace labels, delta labels, conditional controls, git status, changed files, command evidence, and no-commit shape before writing |

Do not list fake section headings with a `##` prefix before the real section.
Do not invent PASS evidence before commands run.

## Agent Handoff Contract Control Block

Contract source (stable reference, not an archived session handoff):
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.
Stable front door: `docs/reference/agent_handoff/README.md`, section `Central Core`.

| Field | Value |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher authors committed packet; distinct delegated worker executes and returns without commit; independent reviewer/closer accepts and commits; session-sync steward updates continuity separately |
| phase | `DISPATCH_AUTHORING`; `EXECUTION`; `CLOSURE`; `SESSION_SYNC` |
| baseHeadFor(phase) | dispatchBaseHead=`baaf21cd2`; executionBaseHead=worker captures clean committed dispatch HEAD; closureBaseHead=reviewer captures execution base |
| changedSetScope(phase) | dispatch=SOT3-APP roadmap plus paired GC-018/work order; execution=exact two planned outputs; closure=accepted worker outputs plus reviewer-owned roadmap/work-order/completion paths; session-sync=protected continuity paths only |
| traceScope(phase, actor) | each role records only phase-local commands, paths, hashes, diffs, HEAD, and gate evidence |
| commitOwner(phase) | dispatcher commits dispatch; worker forbidden; reviewer/closer commits accepted material; session-sync steward commits continuity separately |
| crossBatchIsolation | FSCB material and session closure are already committed; T0 execution starts only from clean dispatch HEAD and does not mix later T1 work |
| nextMoveSurfaces | worker cannot edit; reviewer may close T0 and release only T1 packet authoring; session steward updates continuity only after accepted material commit |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SOT3_APP_T0_COMPLETION_2026-07-15.md` |
| reviewerOwnedClosurePaths | SOT3-APP roadmap, this work-order status/closure evidence, accepted worker outputs, and completion review only |
| closureOwner | independent reviewer/closer designated before dispatch |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath:
`docs/reviews/CVF_SOT3_APP_T0_WORKER_RETURN_2026-07-15.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Worker return must include these always-required section names and evidence
terms:

- Purpose
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Checker Source Read-Ahead Block
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- Claim Boundary
- git status --short
- Changed Files
- Command Evidence
- No-Commit Statement
- executionBaseHead

Worker return must include or explicitly resolve these conditional controls:

- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

Return vocabulary:

- success: `COMPLETE_PENDING_REVIEW`
- blocked: `BLOCKED_WITH_REASON`
- no commit: `WORKER_MUST_NOT_COMMIT`

## Verification Commands

Worker must replace `<executionBaseHead>` with the captured committed dispatch
HEAD.

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_external_absorption_core.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_value_conversion.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_overlap_discipline.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_knowledge_intake_routing.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_corpus_completeness_report_integrity.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_governed_artifact_checker_read_ahead.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_governed_file_size.py --enforce
git diff --check
git status --short
```

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Dispatch Prompt Envelope; Role:; Canonical packet:; Commit mode:; executionBaseHead; Current-time notes:; Do-not-misread notes:; Required first actions:; Return contract:; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; Roadmap-To-Work-Order Trace Matrix; Planned Worker Fulfillment Manifest; Acceptance Criteria; Review Gate; Closure Checklist; Worker Autonomy / No-Question Rule; External Repository Absorption Entry Control; Mandatory Blind-Spot Control Block; External Absorption Core; External Absorption Value Conversion Matrix; Overlap And Novelty Classification; External Knowledge Intake Routing; Corpus Completeness And Report Integrity; Dual Agent Surface Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; COMPLETE_PENDING_REVIEW; BLOCKED_WITH_REASON; WORKER_MUST_NOT_COMMIT; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm exact dispatch and worker-output shape after checker-source review, not discover requirements after writing |
| claimBoundary | checker conformance does not prove corpus completion, provenance safety, runtime binding, or product quality |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id SOT3-APP-T0 --title "SOT3 Application Source Ledger And Provenance Disposition" --date 2026-07-15 --base baaf21cd2 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "FSCB-ADAPT-T0 material closure commit 21659a3ac" --stdout --include-worker-return-skeleton` |
| generatedProfile | source-intake plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | authority chain, refreshed dependency release, exact 336-file snapshot, hidden-clone metadata boundary, two-output manifest, full worker-return contract, and zero-runtime exclusions |
| checkerReadAheadConfirmation | dispatch, handoff, worker-return, ADIF, absorption, corpus, trace, encoding, and read-ahead checker sources reviewed |
| docOnlyNewFields | source ledger, hidden-clone inventory, and aggregate receipt fields listed above |
| claimBoundary | dispatch-authoring provenance only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | SOT3-APP-T0 dispatch authoring, 2026-07-15 |
| Working directory | repository root |
| Command or tool surface | startup reads, checker-source reads, direct external enumeration/hashing, read-only hidden-target Git metadata, ADIF resolver, scaffold preview, apply_patch, governance gates |
| Target paths | SOT3-APP roadmap plus paired GC-018 and work order |
| Allowed scope source | operator instruction, accepted intake `24d50f0d7`, FSCB closure `21659a3ac`, and continuity release `baaf21cd2` |
| Before status evidence | clean worktree at dispatchBaseHead `baaf21cd2`; all planned new artifact paths absent |
| After status evidence | exact dispatch artifacts pending pre-dispatch verification and material commit |
| Diff evidence | `git diff --name-status`; `git diff --check` |
| Approval boundary | T0 packet authoring and dispatch only; no worker execution |
| Claim boundary | no source absorption completion, application mutation, or runtime proof |
| Agent type | dispatcher |
| Invocation ID | `sot3-app-t0-dispatch-2026-07-15` |
| Expected manifest | SOT3-APP roadmap; paired T0 GC-018; paired T0 work order |
| Actual changed set | must match the exact three-path expected manifest before dispatch commit |
| Manifest delta | MATCH required |
| Deletion or rename disposition | N/A with reason: none planned |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | SOT3-APP-T0 documentation-only source ledger and provenance disposition dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no application/runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no application/runtime action is executed or observed |
| invocationBoundary | manual filesystem reads, hashing, parsing, read-only Git metadata, and governance checks only |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, binding resolution, or agent coding control |
| claimLanguage | source-processing and provenance evidence only |
| forbiddenExpansion | runtime/provider/live/public/package/Web/MCP/checker behavior requires fresh source-verified authorization |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private copied-folder source-intake dispatch and outputs; no public-sync
authority or public-safe artifact set exists.

## Claim Boundary

This work order authorizes exactly two documentation/evidence outputs from a
clean committed dispatch base. It does not authorize SOT-Application or hidden
clone mutation, dependency synchronization, source copying, direct import,
contract ratification, runtime/binding integration, install, build, typecheck,
test, CI, server, browser, provider/live execution, Catalog/GAP/ADIF/index or
session changes, package activation, public-sync, commit by the worker, or any
claim that the application is integrated, reproducible, safe, live,
production-ready, or user-validated.

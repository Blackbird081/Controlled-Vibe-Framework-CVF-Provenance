# CVF GC-018 - MPI-T5 Memory Access Claim Checker

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-22

docType: gc018_baseline

dispatchBaseHead: b761d1bd

Batch ID: MPI-T5

## Purpose

Authorize one bounded governance-hardening tranche: a static, forward-only
checker that flags Memory Plane overclaims in changed governed Markdown
(GC-018 baselines, work orders, worker returns, completion reviews,
reference contracts). The checker rejects claim language asserting raw
memory access, vector DB, runtime durable store, reinjection, or live
external-agent access through MCP/CLI when only a bounded contract or
read-only helper currently exists, and flags claims that a registry
projection is auto-wired into a route, or that an INDEX artifact replaces
canonical source authority, when current source does not support the claim.

This baseline does not authorize route wiring, runtime memory access,
vector/durable store integration, CLI/MCP adapter behavior, provider/live
proof, or public sync. The checker is a structural/lexical static gate only;
it does not execute, read provider memory, or judge the truth of legacy
findings.

## Decision / Baseline / Proposed Tranche

Decision: dispatch MPI-T5 after MPI-T4 closure and operator selection.

Baseline: current MPI-T2/T3/T4 source-verified contracts and helpers define
the actual boundary of what Memory Plane reads, helpers, and contracts may
currently claim. This checker enforces that boundary going forward in
changed governed Markdown only.

Proposed tranche: one new checker module, one focused test file, hook-chain
wiring into `reviewer-fast`, autorun wiring into the common command bundle,
and one worker-return packet. The worker must not commit.

## Operator Authorization

The operator explicitly selected MPI-T5 on 2026-06-22 after MPI-T4 closed
(material commit `28373d14`, session sync `9b620116`). The selected route is
`WORKER_MUST_NOT_COMMIT`; reviewer/closer retains commit and closure
ownership. Per the roadmap's own MPI-T5 section, this tranche requires its
own GC-018 and protected-path authorization because it edits
`governance/compat/*.py`; both are satisfied by this baseline and its Core
Guard Self-Protection Authorization block below.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22: continue with MPI-T5 after MPI-T4 closure | ACCEPT |
| Phase 2 roadmap | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | ACCEPT |
| Parent MPI roadmap | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | ACCEPT |
| MPI-T4 completion | `docs/reviews/CVF_MPI_T4_FEDERATED_MEMORY_READ_HELPER_WORKER_RETURN_2026-06-22.md` (`Status: ACCEPTED_BY_REVIEWER`) | ACCEPT |
| MPI-T3 contract | `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md` | SOURCE_AUTHORITY_FOR_EXTERNAL_READ_BOUNDARY |
| MPI-T2 contract | `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md` | SOURCE_AUTHORITY_FOR_REGISTRY_PROJECTION_BOUNDARY |
| Memory Plane front door | `docs/reference/CVF_MEMORY_PLANE_MAP.md` | SOURCE_AUTHORITY_FOR_OVERALL_BOUNDARY |
| INDEX classification standard | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | SOURCE_AUTHORITY_FOR_INDEX_VS_CANONICAL_SOURCE_BOUNDARY |
| Existing checker pattern | `governance/compat/check_index_classification.py` | STRUCTURAL_PATTERN_TO_MIRROR |

Provider-specific memory is not CVF authority. Runtime claims in this packet
were refreshed against current source.

## Dependency Release Evidence

| Dependency | Evidence | Status |
|---|---|---|
| MPI-T4 closure | material commit `28373d14`; session sync `9b620116`; worker-return `Status: ACCEPTED_BY_REVIEWER` | RELEASED |
| Operator decision | explicit MPI-T5 selection on 2026-06-22 | RELEASED |
| Source refresh | Source Verification Block below cites current runtime files and symbols | RELEASED |
| Dispatch base | committed HEAD `b761d1bd` before authoring (LPF tsconfig fix included) | RELEASED |

## Scope And Owner Boundary

Allowed worker scope:

- create `governance/compat/check_memory_access_claim.py`;
- create `governance/compat/test_check_memory_access_claim.py`;
- add exactly one new entry to the existing checker-command list in
  `governance/compat/run_local_governance_hook_chain.py` (`reviewer-fast`
  hook), following the existing `("index classification", [...])` tuple
  pattern at line 126;
- add exactly one new entry to the existing checker-command list in
  `governance/compat/run_agent_autorun_workflow_gate.py` (common command
  bundle), following the existing `_range_command("index classification",
  ...)` pattern at line 239;
- create `docs/reviews/CVF_MPI_T5_MEMORY_ACCESS_CLAIM_CHECKER_WORKER_RETURN_2026-06-22.md`.

Forbidden worker scope includes every other file in `governance/compat/`, all
route files, all existing Memory Plane helpers
(`federated-memory-read.ts`, `scan-registry-memory-projection.ts`,
`memory-runtime-readout.ts`), foundation packages, registry
sources/aggregates/generator, durable stores, session and handoff files,
public-sync, provider configuration, dependency manifests, and `.github/**`.

Risk ceiling: R2 bounded static checker plus narrow two-line hook/autorun
wiring; no route, runtime, or external execution behavior. The checker itself
must not execute anything, read provider memory, or mutate any artifact.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| MPI-T5 is an optional governance-hardening checker, not a helper implementation | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | `## MPI-T5 Memory Access Claim Checker` | `MPI-T5` | MPI Phase 2 roadmap | VALUE_SET | ACCEPT |
| MPI-T5 candidate checker targets are named explicitly | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | `## MPI-T5 Memory Access Claim Checker`, candidate checker targets list | `MPI-T5` | MPI Phase 2 roadmap | VALUE_SET | ACCEPT |
| MPI-T5 requires its own GC-018, protected-path authorization, focused tests, and hook/autorun wiring proof | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | `## MPI-T5 Memory Access Claim Checker`, final paragraph | `MPI-T5` | MPI Phase 2 roadmap | VALUE_SET | ACCEPT |
| MPI-T4 closed with the federated helper performing no route wiring, registry write, or adapter behavior | `docs/reviews/CVF_MPI_T4_FEDERATED_MEMORY_READ_HELPER_WORKER_RETURN_2026-06-22.md` | `## Claim Boundary` | `buildFederatedMemoryRead` | MPI-T4 worker return | VALUE_SET | ACCEPT |
| MPI-T3 contract is summary-only with `rawMemoryReleased=false`, `canReinject=false` | `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md` | Inherited Invariants section | `rawMemoryReleased`; `canReinject` | MPI-T3 external read contract | LITERAL_INVARIANT | ACCEPT |
| MPI-T2 projection accepts caller-supplied registry entries; no automatic file/route loading exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts` | lines 1-30 module docstring and signature | `projectScanRegistryFindings` | scan registry memory projection | RUNTIME_BEHAVIOR | ACCEPT |
| Existing reviewer-fast hook chain registers checkers as `(label, command-list)` tuples in one ordered list | `governance/compat/run_local_governance_hook_chain.py` | lines 125-128 | `"index classification"` checker tuple | reviewer-fast hook command registry | RUNTIME_BEHAVIOR | ACCEPT |
| Existing autorun common command bundle registers checkers via `_range_command(label, path, base, head)` | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 238-243 | `_range_command` | autorun common command bundle | RUNTIME_BEHAVIOR | ACCEPT |
| Existing static checker pattern: `--base`/`--head`/`--enforce` CLI, JSON-optional, exits non-zero on violation | `governance/compat/check_index_classification.py` | line 376 | `main` | forward-only INDEX structural checker | RUNTIME_BEHAVIOR | ACCEPT |

## New Implementation Symbols

| Proposed symbol | Target file | Status before worker execution | Boundary |
|---|---|---|---|
| `check_memory_access_claim.py` (module) | `governance/compat/check_memory_access_claim.py` | NEW_SOURCE_SYMBOL | static lexical/structural scan of changed governed Markdown only |
| main checker entry function (worker may name it `main` or `run_check`, mirroring the sibling checker's own entry-point name) | same target | NEW_SOURCE_SYMBOL | accepts `--base`, `--head`, `--enforce`, optional `--json`; returns violations list |
| `test_check_memory_access_claim.py` (module) | `governance/compat/test_check_memory_access_claim.py` | NEW_SOURCE_SYMBOL | focused tests for true positives, true negatives, and the canonical local-view guard reference |

These symbols are proposals, not pre-existing source facts. The worker may
use clearer internal helper-function names only if the worker-return records
the exact replacement and tests prove the same boundary. The public CLI
surface (`--base`, `--head`, `--enforce`, optional `--json`) must match the
existing sibling checkers exactly so hook-chain and autorun wiring work
without special-casing.

## Implementation Requirements

The checker must, over changed files in the given `--base`..`--head` range
(or `HEAD`..`HEAD` working-tree mode, matching the sibling checker's own
range-resolution convention) restricted to governed Markdown under
`docs/baselines/`, `docs/work_orders/`, `docs/reviews/`, and
`docs/reference/`:

1. flag claim language asserting external agents can read CVF memory through
   a live runtime/MCP/CLI route when the changed file does not also cite a
   route file, MCP tool file, or CLI adapter file as a verified source; i.e.
   a bare claim with no source-verified runtime citation;
2. flag claim language asserting scan-registry projection is "auto-wired",
   "automatically loaded", or "wired into the route" without an explicit
   route-file citation in the same Source Verification Block;
3. flag claim language asserting KGR, graph memory, vector DB, or durable
   store is "production memory access" or "live memory access" without an
   explicit durable-store or vector-store source-file citation;
4. flag claim language asserting raw memory, raw `content` exposure, or
   reinjection (`canReinject=true`, "raw memory release", "reinjection is
   allowed") is permitted;
5. flag claim language asserting an INDEX artifact "replaces", "supersedes",
   or "is" canonical source authority, instead of being routed as INDEX input
   per the INDEX classification standard;
6. exit non-zero only under `--enforce` when any violation is found; support
   a non-enforcing report mode;
7. perform no filesystem write, no network call, no provider call, and no
   mutation of any scanned file; read-only static analysis only;
8. emit a clear violation message naming the file, the matched claim
   pattern, and the missing required citation, mirroring
   `check_index_classification.py`'s existing violation-message style.

Focused tests must prove: a true-positive case for at least one pattern per
requirement 1-5 above; a true-negative case where the same claim language
appears but is accompanied by a valid source-verified citation (no false
positive); a true-negative case for ordinary unrelated governed Markdown
prose (no over-triggering on unrelated content); and a CLI-contract test
proving `--base`/`--head`/`--enforce`/optional `--json` behave consistently
with the sibling checker's own contract.

## Negative Search And Collision Discipline

Search roots: `governance/compat`; `docs`.

Search command:
`rg -n -i "memory access claim|check_memory_access_claim|MemoryAccessClaim" governance/compat docs`

Before dispatch, both target source/test files returned `False` from
`Test-Path`; existing matches were roadmap references only (the MPI-T5
section itself). There is no source symbol collision.

## Current Runtime Freshness Verification

| Claim | Current evidence | Disposition |
|---|---|---|
| Reviewer-fast hook chain registers checkers via ordered `(label, command)` tuples | current `run_local_governance_hook_chain.py` lines 125-128 | ACCEPT |
| Autorun common command bundle registers checkers via `_range_command` calls | current `run_agent_autorun_workflow_gate.py` lines 238-243 | ACCEPT |
| MPI-T2/T3/T4 boundaries remain the live source of truth for what claims are currently true | current contract/helper files cited in Source Verification Block | ACCEPT |
| New target files do not exist at dispatch | `Test-Path` returned `False` for both targets | ACCEPT |
| Route wiring | N/A with reason: forbidden by this baseline | N/A_WITH_REASON |
| Provider/live proof | N/A with reason: no provider behavior is changed or claimed | N/A_WITH_REASON |
| Public sync | N/A with reason: private provenance dispatch only | N/A_WITH_REASON |

## Evidence / Verification

Dispatch verification uses current source reads, Source Verification rows,
target-file absence checks, negative collision search, roadmap freshness,
work order dispatch quality, pre-dispatch autorun gate, commit steward
dispatch preflight, local hook chain, and git diff/status evidence.

## Acceptance And Fail Conditions

Accept only when all allowed artifacts exist exactly as scoped, the checker
performs no I/O beyond reading changed Markdown text, focused tests cover
true-positive/true-negative/CLI-contract cases and pass, the hook-chain and
autorun wiring additions are each exactly one new entry following the
existing pattern with no reordering or edits to other entries, no forbidden
path is changed, reviewer-fast and autorun still pass end to end with the new
checker included, and the worker returns uncommitted `COMPLETE_PENDING_REVIEW`.

Fail or return `BLOCKED_WITH_REASON` for false positives on ordinary governed
Markdown, false negatives on the five required claim classes, any edit to a
forbidden `governance/compat/*.py` file outside the two narrow wiring lines,
any executable/network/provider behavior inside the checker, route wiring,
filesystem mutation, or any required change outside Allowed scope.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance checker dispatch; no public artifact or public
claim is authorized.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator selection to CVF-owned GC-018 baseline and work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this MPI-T5 GC-018 baseline |
| Disposition | ADAPT as bounded local checker implementation |
| Claim boundary | external/provider memory is not authority; current CVF source controls |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one new static checker module plus
its focused test module to `governance/compat/`, and register it with
exactly one new entry each in the existing reviewer-fast hook-chain command
list and the existing autorun common command bundle, following the
established `(label, command)` and `_range_command(label, path, base, head)`
patterns. No edit to any other existing checker, hook entry, or autorun entry
is authorized.

Protected paths:

- `governance/compat/run_local_governance_hook_chain.py` (one new tuple entry
  only, inserted adjacent to the existing `"index classification"` entry; no
  reordering or edit of any other entry)
- `governance/compat/run_agent_autorun_workflow_gate.py` (one new
  `_range_command` call only, inserted adjacent to the existing `"index
  classification"` call; no reordering or edit of any other call)

Operator authorization: the operator selected MPI-T5 on 2026-06-22 after
MPI-T4 closed, per the roadmap's own requirement that MPI-T5 needs explicit
protected-path authorization because it edits `governance/compat/*.py`. This
baseline authorizes only the narrow two-entry wiring described above plus the
two brand-new files; no other protected-path edit is in scope.

Rollback boundary: revert the accepted MPI-T5 material closure commit to
remove the checker module, its test module, and both wiring entries together.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MPI-T5 local static checker dispatch |
| claimDisposition | N/A with reason: no Delta execution-control behavior is implemented or claimed |
| receiptEvidence | N/A with reason: no Delta receipt |
| actionEvidence | N/A with reason: dispatch creates no runtime action evidence; worker will provide focused test evidence |
| claimLanguage | MPI-T5 local static checker dispatch only |
| forbiddenExpansion | route/schema/auth changes, automatic source loading, registry/durable writes, CLI/MCP adapter, provider/live, public-sync, wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |
| invocationBoundary | direct CLI invocation by reviewer-fast hook chain, autorun bundle, or a human operator running the script directly |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or route interception beyond reading changed Markdown text for static analysis |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local workspace |
| Session or invocation | MPI-T5 packet authoring, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Target paths | this GC-018 baseline and paired work order |
| Allowed scope source | operator instruction selecting MPI-T5 |
| Before status evidence | clean committed HEAD `b761d1bd` |
| Approval boundary | dispatch only; worker returns uncommitted |
| Claim boundary | no route, write, adapter, provider/live, public-sync, or session behavior beyond the two narrow checker-registry wiring lines |

## Claim Boundary

This baseline authorizes only a local, static, read-only Markdown claim
checker, its focused tests, two narrow registry-wiring additions in existing
checker-command lists, and a worker-return packet. It does not authorize
route/schema/auth changes, automatic source loading, registry or durable
writes, existing Memory Plane helper edits, CLI/MCP adapters, external
commands, vector/graph storage, provider/live proof, public sync, readiness,
or universal control claims. It does not authorize any edit to any
`governance/compat/*.py` file other than the two named protected paths, and
only the two narrow wiring lines described in the Core Guard Self-Protection
Authorization block.

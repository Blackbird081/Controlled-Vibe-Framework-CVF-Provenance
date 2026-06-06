# CVF GC-018 - CI1-T10 Cortex Hub Memory Learning Deep Scan

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_ANALYSIS

docType: baseline

Date: 2026-06-05

baseHead: `649b9808`

## Purpose

Authorize CI1-T10 as a bounded deep scan of the legacy cortex-hub source family:

`.private_reference/legacy/CVF ADD/cortex-hub/`

The tranche reads all 11 files and decides what CVF can absorb as reference,
workflow-chain seed, deferred runtime work, or rejected authority. This is a
private provenance corpus scan only.

## Source

Predecessor evidence:

- CI1-T9 triage packet:
  `docs/audits/CVF_CI1_T9_LEGACY_PARTIAL_SCAN_TRIAGE_PACKET_2026-06-05.md`
- GC-051 corpus scan registry:
  `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- Rescan hardening standard:
  `docs/reference/CVF_RESCAN_INTELLIGENCE_HARDENING_STANDARD_2026-06-05.md`
- Knowledge absorption blind-spot standard:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`

## Decision

Proceed with CI1-T10 on `CVF ADD/cortex-hub/`.

Rationale:

- CI1-T9 selected cortex-hub as the highest-value memory/learning candidate;
- the folder is bounded at 11 files and can be fully read in one tranche;
- source text maps directly to CVF Knowledge Layer, Context Builder, Learning
  Plane, MCP Bridge, Guard/Policy, Audit, and W7-style record binding;
- source text also rejects parallel runtime, governance ownership, truth
  authority, and autonomous learning ownership.

## Scope / Target / Owner Boundary

Corpus target: `.private_reference/legacy/CVF ADD/cortex-hub/`

Known files at dispatch:

| File | Status |
| --- | --- |
| `CVF_CODE_INTELLIGENCE_ADAPTER_SPEC.md` | IN_SCOPE |
| `CVF_CORTEX_CAPABILITY_MATRIX.md` | IN_SCOPE |
| `CVF_CORTEX_GUARD_POLICY.md` | IN_SCOPE |
| `CVF_CORTEX_HUB_INTEGRATION_OVERVIEW.md` | IN_SCOPE |
| `CVF_CORTEX_RUNTIME_USAGE_PLAYBOOK.md` | IN_SCOPE |
| `CVF_CORTEX_TRACE_AND_AUDIT_MODEL.md` | IN_SCOPE |
| `CVF_KNOWLEDGE_MEMORY_ADAPTER_SPEC.md` | IN_SCOPE |
| `CVF_MCP_CORTEX_BRIDGE_SPEC.md` | IN_SCOPE |
| `CVF_SHARED_KNOWLEDGE_SYNC_POLICY.md` | IN_SCOPE |
| `CVF_W7_CORTEX_RECORD_BINDING.md` | IN_SCOPE |
| `Thong_tin.md` | IN_SCOPE |

Total in-scope files: 11

CVF owns:

- corpus evidence discipline;
- deep scan packet and finding packet;
- GC-051 registry update;
- routing accepted value into future workflow-chain work only when authorized.

Out of scope:

- files outside `CVF ADD/cortex-hub/`;
- implementing cortex-hub runtime adapters, MCP tools, external services, code
  graph engines, memory stores, or provider calls;
- changing current runtime, governance checkers, hooks, public-sync, README, or
  catalog claims;
- claiming production readiness, hosted readiness, public readiness, live
  governance behavior, or external cortex-hub availability.

## Claim Boundary

CI1-T10 claims only a bounded source-backed deep scan of the 11-file cortex-hub
legacy corpus. It may accept source value as architecture/reference/workflow
seed, but it does not claim runtime integration or live behavior.

## Corpus Completeness And Report Integrity

- Corpus task class: DISPATCH_BASELINE
- Corpus root: `.private_reference/legacy/CVF ADD/cortex-hub/`
- Snapshot time: 2026-06-05
- Enumeration command: `rg --files --hidden --no-ignore ".private_reference/legacy/CVF ADD/cortex-hub"`
- Manifest artifact or inline manifest: target file table in this baseline
- Manifest hash: `4283027364513ba3b82c83ce32ac1b09db02ba0c8fd5500108e56b3b8555e908`
- Processing ledger artifact or inline ledger: target file table in this
  baseline; deep-read ledger belongs to the CI1-T10 packet
- Allowed terminal statuses: READ_DEEP | READ_SHALLOW | SKIPPED_WITH_REASON |
  DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=11; ledger_terminal=0; exclusions=baseline authorizes but does not perform deep read; unresolved=11
- Unresolved files: 11
- Declared exclusions: deep file-level read and semantic classification are
  assigned to the CI1-T10 packet, not this authorization baseline
- Unreadable or unsupported files: none known at dispatch
- Aggregation check: 11 target files enumerated
- Drift check: PASS for dispatch snapshot
- Output traceability: target file table plus CI1-T10 packet requirement
- Adversarial verification: assigned to CI1-T10 packet
- Corpus verdict: PARTIAL

## Risk Register

| Risk | Control |
| --- | --- |
| Treating cortex-hub as a new core subsystem | reject runtime/control/governance/truth authority |
| Raw memory becomes truth | require Learning Plane/evaluation and provenance downgrade |
| MCP becomes the architectural center | keep MCP as bridge/interface only |
| Legacy W7 names are stale relative to current runtime | route as concept/record-chain candidate, not current source fact |
| Runtime implementation sneaks into scan | explicit no-runtime boundary and separate future GC-018 requirement |

## Knowledge Absorption Blind-Spot Control Block

Standard read:
`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`

- Source inventory:
  - Root: `.private_reference/legacy/CVF ADD/cortex-hub/`
  - Shell command run:
    `rg --files --hidden --no-ignore ".private_reference/legacy/CVF ADD/cortex-hub"`
  - Total file count: 11
  - Content manifest hash:
    `4283027364513ba3b82c83ce32ac1b09db02ba0c8fd5500108e56b3b8555e908`

- Prior absorption evidence resolved:
  - CI1-T9 selected cortex-hub and recorded stale registry delta.
  - Current-source search found no direct cortex-hub owner-surface absorption in
    active `EXTENSIONS`, `docs/reference`, `docs/roadmaps`, `docs/audits`,
    `docs/reviews`, or `governance` surfaces.

- Source families skipped:
  - all sibling `CVF ADD/` folders;
  - all `CVF_Important/` memory/learning folders, including
    `ADDING_LEARNING PLANE/` and `Knowledge Base_Palace/`.

- Owner-surface normalization:
  - memory/shared knowledge map to Knowledge Layer, Context Builder, Learning
    Plane, and future memory-governance workflow chain;
  - code intelligence maps to Knowledge Layer and Context Builder only;
  - MCP maps to bridge/interface only;
  - guard/trace/W7 binding map to governance-control evidence and future
    workflow-chain design.

- Accept/defer/reject matrix at GC-018 level:

| Candidate | Disposition | Reason |
| --- | --- | --- |
| Deep-read all 11 files | ACCEPT | CI1-T10 target scope |
| Accept cortex-hub as external capability-provider reference | ACCEPT | source repeatedly preserves CVF-first authority |
| Implement memory/MCP/code adapter runtime | DEFER | separate source-verified runtime tranche required |
| Import conductor/runtime ownership | REJECT | conflicts with CVF orchestration/execution authority |
| Treat memory/shared knowledge as truth | REJECT | source itself rejects this path |

- Adversarial role review:
  - Implementer: the source set is cohesive and already organized into contract
    files that can seed a workflow chain.
  - Skeptic/Auditor: W7 names and cortex adapter surfaces are legacy proposal
    vocabulary; implementation must source-verify current runtime symbols.
  - Product/Operator Advocate: memory/learning value is high, but public claims
    would require separate public-safe synthesis.
  - Safety/Boundary Owner: no runtime, no public-sync, no live/provider proof.

- Gate 7 completeness cross-check:

| File/folder | In source inventory? | Disposition | Reason |
| --- | --- | --- | --- |
| 11 cortex-hub files | YES | READ by CI1-T10 | In scope |
| Other `CVF ADD/` folders | NO | SKIPPED | Separate tranche |
| `CVF_Important/ADDING_LEARNING PLANE/` | NO | SKIPPED | CI1-T11 candidate |

- Blind-spot verdict: CLEAR

Rationale: all 11 files are filesystem-confirmed, prior triage evidence is
resolved, sibling folders are explicitly out of scope, and runtime/public work
is deferred rather than inferred.

## Rescan Intelligence Hardening

- Original source artifact: `.private_reference/legacy/CVF ADD/cortex-hub/`
- Predecessor intake artifact:
  `docs/audits/CVF_CI1_T9_LEGACY_PARTIAL_SCAN_TRIAGE_PACKET_2026-06-05.md`
- Delta ledger status: DISPATCH_DECLARED_LIMITS - includes
  UNCHANGED_FROM_INTAKE, CHANGED_DISPOSITION, NEW_FINDING, and
  REMOVED_OR_REJECTED categories assigned to the worker packet.
- Routing matrix status: DISPATCH_DECLARED_LIMITS - includes DO_NOW,
  SEPARATE_RUNTIME_TRANCHE, STRATEGIC_OPERATOR_DECISION, OUT_OF_SCOPE, and
  RESOLVED_BY_DESIGN lanes assigned to the worker packet.
- Semantic sampling status: DISPATCH_DECLARED_LIMITS - packet must include
  sampleId, source section, source claim, disposition checked, adversarial
  challenge, and verdict columns.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| sampleId | Delta category | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| CI1-T10-GC018-D1 | UNCHANGED_FROM_INTAKE | CI1-T9 selection | cortex-hub selected | authorize same target | Did baseline change target? | PASS |
| CI1-T10-GC018-D2 | CHANGED_DISPOSITION | CI1-T9 shallow candidate | shallow accept | assign deep-read packet | Is deep read done in baseline? | PASS_WITH_LIMIT |
| CI1-T10-GC018-D3 | NEW_FINDING | dispatch scope | possible memory/MCP findings | require packet findings | Are findings known before read? | PASS_WITH_LIMIT |
| CI1-T10-GC018-D4 | REMOVED_OR_REJECTED | runtime/public path | implementation/public claim | reject from baseline | Could baseline authorize runtime? | PASS |

### Follow-Up Routing Matrix

| Route lane | Target | Disposition | Evidence | Next action |
| --- | --- | --- | --- | --- |
| DO_NOW | CI1-T10 deep scan packet | ACCEPT | CI1-T9 selection | read all 11 files |
| SEPARATE_RUNTIME_TRANCHE | memory/MCP/code runtime | DEFER | runtime out of baseline scope | future GC-018 only |
| STRATEGIC_OPERATOR_DECISION | external service/public memory claim | DEFER | product boundary impact | operator decision later |
| OUT_OF_SCOPE | public-sync/live proof | REJECT | private corpus baseline | no public action |
| RESOLVED_BY_DESIGN | no parallel authority boundary | ACCEPT_SUMMARY_ONLY | GC-018 claim boundary | carry forward |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| CI1-T10-GC018-S1 | `CVF_KNOWLEDGE_MEMORY_ADAPTER_SPEC.md` | memory adapter value | sample required | Could memory become truth? | ASSIGNED_TO_PACKET |
| CI1-T10-GC018-S2 | `CVF_MCP_CORTEX_BRIDGE_SPEC.md` | MCP bridge value | sample required | Could MCP bypass CVF? | ASSIGNED_TO_PACKET |
| CI1-T10-GC018-S3 | `CVF_W7_CORTEX_RECORD_BINDING.md` | record binding value | sample required | Are symbols current? | ASSIGNED_TO_PACKET |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| CI1-T10 target selected | `docs/audits/CVF_CI1_T9_LEGACY_PARTIAL_SCAN_TRIAGE_PACKET_2026-06-05.md` | `Next selected tranche` | `CVF ADD/cortex-hub/` | CI1-T9 triage packet | ACCEPT |
| Target folder has 11 files | N/A - filesystem enumeration | `rg --files --hidden --no-ignore` output | `.private_reference/legacy/CVF ADD/cortex-hub/` | filesystem source corpus | ACCEPT |
| Dispatch baseHead | N/A - git command | `git rev-parse --short HEAD` | `649b9808` | git repository state | ACCEPT |
| Runtime implementation authorized | N/A | no source | runtime implementation | current task scope | REJECT |

## Required Evidence

```powershell
python governance/compat/check_corpus_completeness_report_integrity.py --base 649b9808 --head HEAD --enforce
python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base 649b9808 --head HEAD --enforce
python governance/compat/check_corpus_intelligence_classification.py --base 649b9808 --head HEAD --enforce
python governance/compat/check_corpus_scan_registry.py --base 649b9808 --head HEAD --enforce
python governance/compat/check_rescan_intelligence_hardening.py --base 649b9808 --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base 649b9808 --head HEAD --enforce
```

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update active session continuity only so
the CI1-T10 cortex-hub deep scan can record current mode, current next allowed
move, and current handoff HEAD after CI1-T9 commit `649b9808`.

Protected paths:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`

Operator authorization: 2026-06-05 operator explicitly authorized the next
legacy deep scan, "ok, deep scan ke tiep I1-T10". The protected-file edits are
limited to recording that authorized CI1-T10 scan state.

Rollback boundary: if this continuity sync is wrong, restore only the CI1-T10
continuity text in the protected session files. Do not revert CI1-T9 commit
`649b9808`, the T10 corpus scan artifacts, registry findings, source corpus
files, public-sync history, or historical handoff content.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: CI1-T10 consumes private legacy source material and creates private
absorption evidence only. No public-sync artifact or public repository claim is
created.

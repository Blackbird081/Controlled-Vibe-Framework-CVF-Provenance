# CVF GC-018 - MEMCON-T2 Temporal Ambiguity And Source-Authority Checker

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018_baseline

Date: 2026-06-13

Owner: Codex

Worker: Claude

sourceAuthority:
`docs/reviews/CVF_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_COMPLETION_2026-06-13.md`

rawMemoryReleased=false

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `3f4ddda6`

Parent roadmap:
`docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`

Parent standard:
`docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md`

Schema appendix:
`docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md`

## Purpose

Authorize MEMCON-T2 as a bounded implementation tranche for an early machine
checker that validates Memory Consolidation artifacts for temporal ambiguity,
source authority, raw-memory release boundaries, and operator-visible review
sections.

## Decision / Baseline / Proposed Tranche

Decision: dispatch MEMCON-T2 to Claude.

Baseline:

- MEMCON-T1a is `CLOSED_PASS_BOUNDED`.
- MEMCON-T1b is `CLOSED_PASS_BOUNDED`.
- T1b created stable doc-only field tables for the checker to consume.

Proposed tranche:

- add a deterministic checker under `governance/compat/`;
- add focused tests under `governance/compat/`;
- wire the checker into reviewer-fast and pre-commit hook modes;
- produce a completion/worker-return packet;
- return uncommitted artifacts to Codex for review and commit.

## Knowledge Absorption Blind-Spot Control Block

| Control item | Evidence | Disposition |
| --- | --- | --- |
| Prior absorption evidence resolved | MEMCON roadmap, T1a standard, T1b schema appendix, and current hook runner inspected | ACCEPT |
| Detailed source files read when present | Source verification table cites current docs and runtime/hook source | ACCEPT |
| Accepted value normalized into owner surfaces | Checker scope is derived from T1b schema fields and existing hook-chain pattern | ACCEPT |
| Accept/defer/reject dispositions recorded | Runtime/storage/retrieval/Policy_Local work is rejected from T2 | ACCEPT |
| Adversarial role review | Work order requires negative tests for overclaim and boundary violations | ACCEPT |
| Blind-spot delta | T2 closes early machine-check gap only; memory ledger and retrieval integration remain later tranches | ACCEPT_WITH_BOUNDARY |

## Dependency Release Evidence

| Dependency | Required evidence | Disposition |
| --- | --- | --- |
| MEMCON-T1a closure | material commit `84a46b62`; standard and owner map closed | SATISFIED |
| MEMCON-T1b closure | material commit `f94d2fbd`; session sync `3f4ddda6`; schema appendix closed | SATISFIED |
| T2 fresh authorization | this GC-018 and paired work order | SATISFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| MEMCON-T2 is the temporal/source-authority checker tranche | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | `MEMCON-T2 Detail` | `MEMCON-T2` | MEMCON roadmap | ACCEPT |
| T1b schema lists checker handoff notes | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | `Machine-Check Handoff Notes For MEMCON-T2` | `TIME_AMBIGUOUS_BLOCKED` | MEMCON schema appendix | ACCEPT |
| T1a temporal rule blocks relative dates unless normalized | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | `Temporal Normalization Rule` | `temporalNormalizationStatus` | MEMCON T1a standard | ACCEPT |
| T1a retrieval rule requires raw memory non-release | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | `Retrieval Eligibility Rule` | `rawMemoryReleased` | MEMCON T1a standard | ACCEPT |
| Current hook runner has reviewer-fast mode | `governance/compat/run_local_governance_hook_chain.py` | lines 24-71 | `REVIEWER_FAST_CHECKS` | local hook runner | ACCEPT |
| Current hook runner has pre-commit mode | `governance/compat/run_local_governance_hook_chain.py` | lines 79-181 | `pre-commit` | local hook runner | ACCEPT |
| Existing checker pattern uses repo-root scoped Python script | `governance/compat/check_rescan_intelligence_hardening.py` | top-level constants and CLI | `REPO_ROOT` | rescan intelligence checker | ACCEPT |
| Existing focused checker tests use unittest/pytest-compatible files | `governance/compat/test_check_work_order_dispatch_quality.py` | existing focused checker-test pattern | `WorkOrderDispatchQualityTests` | governance compatibility tests | ACCEPT |

## Evidence / Verification

Required dispatch verification:

- reviewer-fast must pass before Claude receives this packet;
- pre-dispatch autorun must pass on the dispatch range;
- Claude must run the focused checker tests, reviewer-fast, and pre-commit
  after implementation;
- Codex remains the reviewer and committer.

## Rescan Intelligence Hardening

- Original source artifact: N/A with reason - no source-corpus rescan artifact is
being refreshed.

- Predecessor intake artifact: N/A with reason - this packet dispatches a
governance checker from closed MEMCON-T1a/T1b artifacts, not a refreshed
external intake.

- Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS

- Routing matrix status: COMPLETE_WITH_DECLARED_LIMITS

- Semantic sampling status: COMPLETE_WITH_DECLARED_LIMITS

- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

Reason: MEMCON-T2 is a deterministic memory-consolidation artifact checker. It
does not implement rescan orchestration, rescan output ranking, source-corpus
intake, OCR, extraction, or operator rescan recommendation behavior. The only
scan-like behavior authorized here is a bounded governance document check for
MEMCON markers and fields.

### Original-Intake Delta Ledger

| Delta category | Current finding | Predecessor finding | Disposition | Reason |
| --- | --- | --- | --- | --- |
| UNCHANGED_FROM_INTAKE | MEMCON-T1a/T1b define temporal/source-authority controls | MEMCON roadmap and schema appendix | ACCEPT | This packet implements the already planned checker lane |
| CHANGED_DISPOSITION | No changed rescan finding | N/A with reason | N/A with reason | No source-corpus rescan is performed |
| NEW_FINDING | No new rescan finding | N/A with reason | N/A with reason | Dispatch scope is checker implementation only |
| REMOVED_OR_REJECTED | Runtime/source-corpus rescan behavior | N/A with reason | OUT_OF_SCOPE | Runtime rescan behavior is outside MEMCON-T2 |

### Follow-Up Routing Matrix

| Routing lane | Routed item | Disposition | Reason |
| --- | --- | --- | --- |
| DO_NOW | MEMCON checker implementation | ACCEPT | Authorized by this GC-018 and paired work order |
| SEPARATE_RUNTIME_TRANCHE | Runtime memory or retrieval behavior | DEFER | Requires later authority |
| STRATEGIC_OPERATOR_DECISION | Policy_Local PL-S1 use-case adoption | DEFER | Held until operator decides MEMCON foundation is sufficient |
| OUT_OF_SCOPE | Provider/API, OCR, public-sync, external workspace mutation | REJECT | Not authorized by T2 |
| RESOLVED_BY_DESIGN | Rescan intelligence applicability | ACCEPT | This packet records COMPLETE_WITH_DECLARED_LIMITS with explicit boundary |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| MEMCON-T2-S1 | MEMCON-T2 Detail | T2 is a checker lane | ACCEPT | Could this imply runtime memory implementation? | PASS - runtime work is forbidden |
| MEMCON-T2-S2 | Machine-Check Handoff Notes For MEMCON-T2 | checker must cover temporal/source authority and raw release | ACCEPT | Could this require provider/API or external workspace access? | PASS - deterministic docs/checker only |

## New Files To Create

| Path | Purpose | Boundary |
| --- | --- | --- |
| `governance/compat/check_memory_consolidation_artifact_quality.py` | MEMCON-T2 checker | deterministic docs/checker only |
| `governance/compat/test_check_memory_consolidation_artifact_quality.py` | focused tests | no provider/API use |
| `docs/reviews/CVF_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_WORKER_RETURN_2026-06-13.md` | worker return/completion packet | uncommitted worker packet |

## Allowed Scope

Claude may modify only:

- the paired work order if needed for status/worker return evidence;
- the new checker and focused tests;
- `governance/compat/run_local_governance_hook_chain.py` for hook placement;
- the MEMCON roadmap row for worker-return status only;
- the worker return review packet.

Forbidden scope:

- no runtime memory implementation;
- no storage, retrieval, provider/API, OCR, vector, SQLite, FTS5, or database
  work;
- no Policy_Local mutation;
- no public-sync;
- no active session state or handoff mutation by Claude;
- no commit by Claude.

## Claim Boundary

This GC-018 authorizes only a deterministic governance checker and tests for
MEMCON artifacts. It does not claim durable memory storage, retrieval behavior,
cross-agent memory consistency, operator UI, Policy_Local readiness, EC
activation, T12 unlock, provider/API proof, public-sync export,
production/public readiness, memory reinjection, high-risk promotion, or
autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Memory Plane checker dispatch; public-sync is not authorized.

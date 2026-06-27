# CVF GC-018 Authorization Baseline - CCLV-T2 Central Facts Reference Advisory Checker

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-06-16

Batch ID: CCLV-T2

rawMemoryReleased: false

## Purpose

Authorize CCLV-T2 under the Central Core Local View governance refactor program.
This tranche adds a narrow advisory checker for central facts packets and local
reference blocks on changed new batches, so CCLV evidence drift can be detected
earlier without making central packets mandatory for every small batch.

## Authority Chain

- Operator instruction in the 2026-06-16 session: after reviewing Claude's
  recent CCLV work, Codex should choose the next roadmap and create a Claude
  work order.
- Codex audit and selection:
  `docs/reviews/CVF_CCLV_T1_T1A_CODEX_AUDIT_AND_CCLV_T2_SELECTION_2026-06-16.md`.
- CCLV standard:
  `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md`.
- CCLV roadmap:
  `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md`.
- CCLV-T1 template:
  `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md`.
- Local reference rules:
  `docs/reference/CVF_CLOSURE_CENTRAL_FACTS_LOCAL_REFERENCE_RULES.md`.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| CCLV-T2 purpose | `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md` | Tranche Plan row `CCLV-T2` | `CCLV-T2` | CCLV roadmap | EXISTS | ACCEPT |
| Permissive first checker strategy | `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md` | `## Guard Strategy` | `validate the central packet when present` | CCLV standard | EXISTS | ACCEPT |
| Required central facts | `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md` | `## Required Central Facts` | `batchId` through `claimBoundary` | CCLV standard | EXISTS | ACCEPT |
| Required local references | `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md` | `## Required Local References` | `Central Facts Reference`; `Local View Role`; `Local Disposition`; `Local Delta` | CCLV standard | EXISTS | ACCEPT |
| Markdown template authority | `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md` | `## Central Facts Packet` | `Field` table | Closure facts template | EXISTS | ACCEPT |
| JSON template authority | `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.json` | `fieldOrder` | `schemaId` | Closure facts JSON template | EXISTS | ACCEPT |
| Local reference value rules | `docs/reference/CVF_CLOSURE_CENTRAL_FACTS_LOCAL_REFERENCE_RULES.md` | `## Local Reference Block` and `## Field Rules` | `Local View Role`; `Local Disposition` | Local reference rules | EXISTS | ACCEPT |

## Decision / Baseline / Proposed Tranche

Decision: execute CCLV-T2 as a bounded governance-checker tranche.

Baseline state:

- CCLV-T1 created a closure facts Markdown template, JSON companion, and local
  reference rules.
- No checker currently validates central facts packet fields or local reference
  blocks.
- The CCLV standard explicitly says the first machine check should be advisory
  or narrow and must not block small single-file batches where a central packet
  would add overhead.

Target state:

- A focused advisory checker exists under `governance/compat/`.
- Focused tests prove valid packet/reference examples pass and representative
  malformed examples fail.
- The checker validates changed files or explicitly passed paths only.
- The checker is not hard-wired into a global hook as a hard failure in this
  tranche.

## Scope Authorization

Authorized:

- Create `governance/compat/check_central_facts_reference.py`.
- Create focused tests for the checker in `governance/compat/`.
- Add a completion review for CCLV-T2.
- Update the CCLV roadmap CCLV-T2 row to closed-equivalent and release CCLV-T3
  as a candidate after reviewer acceptance.
- Update session continuity only in a separate session-sync commit if closure is
  accepted.

Forbidden:

- Do not rewrite historical closed roadmaps, work orders, reviews, evidence
  files, handoffs, or registries solely to adopt CCLV.
- Do not move the CCLV-T1 template or JSON companion.
- Do not make central facts packets mandatory for all small single-file batches.
- Do not hard-wire the checker as a global hard-fail gate before pilot evidence.
- Do not reduce Agent Operation Trace, closure quality, public export, or
  finding-learning requirements.
- No runtime/provider/API/live/public-sync/legacy broad scan.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Checker validates the twelve central facts fields in Markdown central packet tables when a central packet is present. |
| AC2 | Checker validates JSON `fieldOrder` / template keys for the same twelve central facts when a JSON packet is passed. |
| AC3 | Checker validates the four local reference fields when a local reference block is present. |
| AC4 | Checker reports a violation when `Central Facts Reference` points to a missing repo-local path. |
| AC5 | Checker accepts non-applicable files without forcing a central packet. |
| AC6 | Checker is advisory by default and exits non-zero only with `--enforce` when violations exist. |
| AC7 | Focused tests cover valid packet, missing central field, valid local reference, broken local reference, and non-applicable file cases. |
| AC8 | No global hard-fail hook wiring is introduced in this tranche. |
| AC9 | `reviewer-fast`, focused tests, `git diff --check`, and pre-closure on the committed material range pass before closure. |

## Planned Changed Set

| Path | Action | Reason |
|---|---|---|
| `governance/compat/check_central_facts_reference.py` | CREATE | Advisory checker for central facts packets and local reference blocks |
| `governance/compat/test_check_central_facts_reference.py` | CREATE | Focused unit tests for the advisory checker |
| `docs/reviews/CVF_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_COMPLETION_2026-06-16.md` | CREATE | Completion review when worker evidence is accepted by Codex |
| `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md` | MODIFY | Update CCLV-T2 status and release CCLV-T3 candidate when Codex accepts the material range |

## Evidence / Verification

Required worker verification:

```powershell
pytest governance/compat/test_check_central_facts_reference.py
python governance/compat/check_central_facts_reference.py --paths docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.json docs/reference/CVF_CLOSURE_CENTRAL_FACTS_LOCAL_REFERENCE_RULES.md --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_central_facts_reference.py
git diff --check
```

Reviewer closure verification:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD
```

## Risk Assessment

Risk ceiling: R1 docs/governance checker. The checker may read governed markdown
and JSON files but must not change runtime behavior or provider routing.

Latency posture: keep scope narrow and tests focused. Do not run broad repo scans
except changed-path discovery needed by the checker.

## Claim Boundary

This baseline authorizes an advisory governance checker only. It does not prove
runtime/provider behavior, live governance proof, public readiness, production
readiness, or complete CCLV adoption.

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance baseline. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator/reviewer |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 CCLV-T2 GC-018 authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch |
| Target paths | `docs/baselines/CVF_GC018_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_2026-06-16.md` |
| Allowed scope source | operator requested next roadmap and Claude work order after CCLV-T1 closure |
| Before status evidence | base `28a72f45` |
| After status evidence | GC-018 authored; pending dispatch commit |
| Diff evidence | `git diff --name-status`; `git status --short` |
| Approval boundary | GC-018 authorization only; no implementation by this artifact |
| Claim boundary | repo-local trace only; no OS/user attribution |
| Agent type | Codex orchestrator/reviewer |
| Invocation ID | `cclv-t2-gc018-2026-06-16` |
| Expected manifest | `docs/reviews/CVF_CCLV_T1_T1A_CODEX_AUDIT_AND_CCLV_T2_SELECTION_2026-06-16.md`; `docs/baselines/CVF_GC018_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_FOR_CLAUDE_2026-06-16.md`; `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md` |
| Actual changed set | docs/reviews/CVF_CCLV_T1_T1A_CODEX_AUDIT_AND_CCLV_T2_SELECTION_2026-06-16.md; docs/baselines/CVF_GC018_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_2026-06-16.md; docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_FOR_CLAUDE_2026-06-16.md; docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

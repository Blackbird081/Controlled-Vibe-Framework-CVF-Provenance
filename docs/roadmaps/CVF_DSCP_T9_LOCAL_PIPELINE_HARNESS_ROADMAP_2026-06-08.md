# CVF DSCP-T9 Local Pipeline Harness Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-08

---

## Authorization

GC-018:

`docs/baselines/CVF_GC018_DSCP_T9_LOCAL_PIPELINE_HARNESS_2026-06-08.md`

Selection audit:

`docs/audits/CVF_POST_DSCP_T8_NEXT_ROADMAP_AUDIT_2026-06-08.md`

Predecessor release evidence:

- DSCP-T6 closed at `13cc1505`.
- DSCP-T7 closed at `958f8d2b`.
- DSCP-T8 closed at `e96aacaf`.
- Parent DSCP roadmap T1-T8 closed at `e96aacaf`.

## Purpose

Add a focused deterministic harness proving DSCP's closed surfaces compose
across two domains:

- ECO RAG documents become governed context pack requests.
- CPF governed packer preserves gate evidence and raw-content locks.
- LPF memory blocks become governed context packages with raw-memory locks
  preserved as raw-content locks.
- T4 retrieval receipts preserve package source IDs and force raw source
  release to false.

## Scope / Target / Owner Boundary

In scope:

- New test file:
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.local.pipeline.harness.test.ts`
- GC-051 registry update for the new test path only.
- Worker return packet:
  `docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_WORKER_RETURN_2026-06-08.md`

Out of scope:

- No production/runtime source changes.
- No provider call, live proof, key usage, corpus ingestion, OCR, vector
  retrieval, PolicyLocal T12 authoring, public-sync, hosted readiness,
  production readiness, public readiness, or answer-quality claim.

## Non-Goals

- No production/runtime source implementation.
- No live provider proof.
- No API key use.
- No OCR, corpus ingestion, chunking, or vector retrieval.
- No PolicyLocal T12 authoring or current-law claim.
- No public-sync, hosted-readiness, production-readiness, or public-readiness
  claim.

## Work Plan

| Step | Deliverable | Status |
|---|---|---|
| 1 | GC-018 baseline | DISPATCHED |
| 2 | Work order | DISPATCHED |
| 3 | Implement focused local harness test | CLOSED_PASS_BOUNDED |
| 4 | Register new harness path in GC-051 | CLOSED_PASS_BOUNDED |
| 5 | Run focused vitest and package check | CLOSED_PASS_BOUNDED |
| 6 | Return worker packet, uncommitted | CLOSED_PASS_BOUNDED |
| 7 | Codex reviewer closure and session sync | CLOSED_PASS_BOUNDED |

## Acceptance Criteria

| Criterion | Gate |
|---|---|
| ECO end-to-end local path PASS | focused vitest |
| ECO blocked gate path PASS | focused vitest |
| LPF memory-to-receipt path PASS | focused vitest |
| Raw content/source locks stay false | focused vitest |
| Receipt source IDs match package evidence | focused vitest |
| GC-051 registry covers new test path | registry check |
| Worker does not commit | `git log` unchanged by worker |

## Verification

| Check | Command | Required result |
|---|---|---|
| CPF package check | `npm run check` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| Focused harness test | `npm run test -- tests/dscp.local.pipeline.harness.test.ts` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| Reviewer fast gate | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS |
| Pre-closure autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD` | PASS after reviewer closure |

## T12 Gate Hard Invariant

PolicyLocal T12 remains forbidden. This roadmap does not authorize T12,
current-law claims, legal advice quality claims, or corpus ingestion.

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| `rawContentReleased` remains false | ECO PASS + LPF path: asserted in test, vitest 3/3 PASS at `5c90506a` | PASS |
| `canBypassGovernance` remains false | ECO PASS + LPF path: asserted in test, vitest 3/3 PASS at `5c90506a` | PASS |
| `rawSourceReleased` remains false | ECO PASS + LPF path: asserted in test, vitest 3/3 PASS at `5c90506a` | PASS |
| `contextPackageId` equals package ID | ECO PASS + LPF path: asserted in test | PASS |
| blocked gate returns `BLOCKED` package ID | ECO blocked path: `innerPackage.packageId === "BLOCKED"` | PASS |
| blocked package does not expose source artifact IDs | ECO blocked path: `sourceArtifactIds.length === 0` | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T9_LOCAL_PIPELINE_HARNESS_FOR_CLAUDE_2026-06-08.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_COMPLETION_2026-06-08.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return artifact | `docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_WORKER_RETURN_2026-06-08.md` | committed at `5c90506a` | PASS |
| Roadmap state | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | entry `dscp-t9-local-pipeline-harness` SCANNED at `5c90506a` | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and `AGENT_HANDOFF_V17_2026-06-07.md` | mode marker `dscp_t9_closed_pass_bounded` updated in closure batch | PASS |
| Session JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `currentMode`: `dscp_t9_closed_pass_bounded` | PASS |
| Session continuity | `CVF_SESSION_MEMORY.md` and `AGENT_HANDOFF_V17_2026-06-07.md` | mode + continuity updated in closure batch | PASS |
| External evidence digest | no external artifact | all evidence is in-repo | N/A with reason: deterministic local only |
| System loop interlock | no system-loop mutation | test harness only | N/A with reason: no runtime connection |

## Claim Boundary

This roadmap claims a local deterministic harness plan only. It does not claim
provider behavior, live governance proof, retrieval quality, corpus ingestion,
PolicyLocal T12 readiness, public readiness, hosted readiness, production
readiness, or public-sync.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap; not public-synced.

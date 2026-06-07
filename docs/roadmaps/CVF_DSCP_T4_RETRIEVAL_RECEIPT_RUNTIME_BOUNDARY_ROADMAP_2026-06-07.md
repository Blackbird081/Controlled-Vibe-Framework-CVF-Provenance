# CVF DSCP-T4 Retrieval Receipt Runtime Boundary Roadmap

Memory class: FULL_RECORD

Status: DISPATCHED

docType: roadmap

Date: 2026-06-07

dispatchBaseHead: `a368dae9`

---

## Authorization / Decision

Operator instruction 2026-06-07: after DSCP-T3 review, audit CVF, propose the
optimal next roadmap, and write a work order for Claude.

Decision: dispatch DSCP-T4 Retrieval Receipt Runtime Boundary as the next
bounded deterministic DSCP tranche.

## Purpose

DSCP-T3 proved a governed context package can be produced by CPF internal
runtime code. DSCP-T4 closes the next local evidence gap by adding a
deterministic helper that builds a `GovernedRetrievalReceipt` from an existing
`GovernedContextPackage` plus caller-supplied retrieval metadata.

This completes the local package -> receipt boundary before any live provider,
corpus ingestion, public-sync, or answer-quality claim is attempted.

## Scope / Target / Owner Boundary

In scope:
- Create `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.retrieval.receipt.ts`.
- Create `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.retrieval.receipt.test.ts`.
- Create a deterministic receipt builder using existing DSCP-T2/T3 contracts.
- Prove receipt fields are mapped from package evidence without releasing raw
  source content.

Out of scope:
- No provider API call or LLM query.
- No response hashing implementation; `modelResponseHash` is caller-supplied.
- No corpus ingestion, extraction, OCR, or chunking.
- No public-sync, production readiness, hosted readiness, release readiness, or
  answer-quality claim.
- No mutation of existing TypeScript files or barrel exports.

Owner boundary:
- Worker owns only the two new CPF files and worker return packet.
- Codex owns review, commit, roadmap/session continuity, and closure status.

## Source / Predecessor Evidence

| Predecessor | Path | Status |
|---|---|---|
| DSCP-T2 standard contracts | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | CLOSED_PASS_BOUNDED at `932a40aa` |
| DSCP-T3 governed packer | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` | CLOSED_PASS_BOUNDED at `a368dae9` |
| Post-T3 audit | `docs/audits/CVF_DSCP_POST_T3_NEXT_ROADMAP_AUDIT_2026-06-07.md` | DISPATCHED |
| DSCP chain roadmap | `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md` | OPEN |

## Non-Goals

- No live governance proof.
- No provider behavior claim.
- No retrieval answer generation.
- No corpus eligibility promotion.
- No PolicyLocal T12 authorization.
- No public or production readiness.

## Work Plan

| Step | Action | Status |
|---|---|---|
| 1 | Source-verify `GovernedRetrievalReceipt`, `ContentDeliveryClass`, `GovernedContextPackage`, and package evidence contracts | COMPLETE |
| 2 | Author DSCP-T4 GC-018 baseline | COMPLETE |
| 3 | Author DSCP-T4 work order for Claude | COMPLETE |
| 4 | Claude implements two new CPF files under `WORKER_MUST_NOT_COMMIT` | DISPATCHED |
| 5 | Codex reviews worker return, runs gates, commits closure if bounded PASS | PENDING_WORKER_RETURN |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Receipt builder compiles | `npx tsc --noEmit` in CPF directory |
| Receipt maps package ID | focused vitest assertion against `contextPackage.innerPackage.packageId` |
| Receipt copies source artifact IDs | focused vitest assertion against `governanceEvidence.sourceArtifactIds` |
| Package gate results are preserved | focused vitest assertion for `classificationGate` and `freshnessGate` |
| Caller gate map cannot override package gate results | focused vitest override attempt proves package gates win |
| Raw source lock is preserved | focused vitest asserts `rawSourceReleased === false` |
| No existing TypeScript file is modified | worker return `git status --short` |

## Verification / Evidence

Required worker commands:

| Gate | Command | Expected result |
|---|---|---|
| TypeScript | `npx tsc --noEmit` | PASS |
| Focused vitest | `npx vitest run tests/dscp.governed.retrieval.receipt.test.ts` | PASS |
| Pending worktree | `git status --short` | only new T4 files and worker return staged |
| Markdown structural | `python governance/compat/check_markdown_structural_completeness.py --base a368dae9 --head HEAD --enforce` | COMPLIANT |
| Finding-to-governance | `python governance/compat/check_finding_to_governance_learning.py --base a368dae9 --head HEAD --enforce` | COMPLIANT |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base a368dae9 --head HEAD --enforce` | COMPLIANT |

## Acceptance Receipt Assertion Matrix

DSCP-T4 creates a deterministic local `GovernedRetrievalReceipt` object. It
does not perform retrieval, call a provider, hash a live response, or generate
an LLM answer.

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt object can be built | Worker must create receipt builder and focused tests | PENDING_WORKER_RETURN |
| No runtime query performed | Work order forbids provider/LLM query | N/A with reason: deterministic local receipt boundary only |
| No raw source released | `rawSourceReleased` must be literal `false` | PENDING_WORKER_RETURN |
| No provider response hash computed | `modelResponseHash` is caller-supplied | N/A with reason: no provider response in scope |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T4_RETRIEVAL_RECEIPT_RUNTIME_BOUNDARY_FOR_CLAUDE_2026-06-07.md` | `Status: DISPATCHED`; reviewer updates when worker result is reviewed | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T4_RETRIEVAL_RECEIPT_RUNTIME_BOUNDARY_WORKER_RETURN_2026-06-07.md` | worker-owned pending return packet | BLOCKED with reason: pending worker return |
| Roadmap state | this file | reviewer updates to closed only after committed-range PASS | BLOCKED with reason: pending worker return |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | reviewer-owned session sync after dispatch commit | BLOCKED with reason: reviewer sync pending |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and active handoff | reviewer-owned session sync after dispatch commit | BLOCKED with reason: reviewer sync pending |
| External evidence digest | external artifact path | no external artifact authorized | N/A with reason: deterministic local CPF work |
| System loop interlock | no system-loop mutation authorized | no system loop is in scope | N/A with reason: receipt helper only |
| Session continuity | active session front door and handoff | reviewer-owned session sync after dispatch commit | BLOCKED with reason: reviewer sync pending |

## Claim Boundary

This roadmap authorizes only DSCP-T4 deterministic receipt-boundary
implementation in CPF. It does not claim provider behavior, answer quality,
retrieval completeness, corpus ingestion, PolicyLocal T12 readiness,
public-sync, production readiness, hosted readiness, release readiness,
performance, cost, memory reinjection, autonomous mutation, or public
readiness.

## Finding-To-Governance Learning Disposition

Defect class coverage: RUNTIME_SIGNAL_GAP and ORCHESTRATOR_PACKET_GAP.
Learning lane coverage: GOVERNANCE_CONTROL_PLANE and RUNTIME_BEHAVIOR_LEARNING.
Disposition coverage: DEFER_WITH_ROADMAP and RULE_EXISTS. Next action:
execute DSCP-T4 work order under `WORKER_MUST_NOT_COMMIT`.

| Finding | Defect class | Lane | Disposition | Next action | N/A reason |
|---|---|---|---|---|---|
| DSCP receipt contract exists but has no runtime builder | RUNTIME_SIGNAL_GAP | GOVERNANCE_CONTROL_PLANE | DEFER_WITH_ROADMAP | Execute T4 receipt builder work order | N/A |
| Provider/live route remains premature | ORCHESTRATOR_PACKET_GAP | RUNTIME_BEHAVIOR_LEARNING | RULE_EXISTS | Keep T4 local/deterministic | Existing live-proof rule blocks provider claims without live route |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap; no public-sync, public catalog update, or
public artifact export authorized.

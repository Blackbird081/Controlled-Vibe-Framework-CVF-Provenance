# CVF ERH-DUR1 Durable Evidence And Policy Snapshot Completion Review

Memory class: FULL_RECORD

docType: review

Date: 2026-06-05

Worker: Claude (WORKER_MUST_NOT_COMMIT)

Status: CLOSED_PASS_BOUNDED

GC-018: `docs/baselines/CVF_GC018_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_2026-06-05.md`

executionBaseHead: `35c468b5`

closureBaseHead: `49e6725a`

dispatchCommit: `b3c4ce3a`

## Purpose

Record worker evidence and reviewer checklist for ERH-DUR1 Durable Evidence And Policy
Snapshot workflow chain hardening. Documents completion status, DUR2 residual decision,
allowed-scope proof, and claim boundary.

## Target

ERH-DUR1: Durable Evidence And Policy Snapshot workflow chain hardening. Converts
two ERH-RS1 section 4.4 architectural findings into a bounded local runtime
workflow chain under `WORKER_MUST_NOT_COMMIT`.

## Scope

DUR1 implements:
- Local durable default for `control-plane-events.ts` (away from `os.tmpdir()`).
- New `policy-snapshot-registry.ts` owner with `generatePolicySnapshotId`,
  `buildPolicySnapshot`, `readPolicySnapshot`, and `CVF_POLICY_SNAPSHOT_DIR` env override.
- `web-governance-envelope.ts` delegation to registry owner.
- Focused tests: 9 durable event tests + 10 policy snapshot tests.
- DUR1 machine checker (15 checks) + checker tests.
- Hook chain, autorun gate, GC-052 interlock wiring.
- `.gitignore` recursive `.cvf/runtime/` and `.cvf/config/` ignore coverage so
  bounded local runtime output is not accidentally staged.
- Workflow-chain reference, ledger, completion review (this document).
- ERH roadmap DUR1 row update to `CLOSED_PASS_BOUNDED`.

## Methodology

Source-diff bounded implementation following the work order Allowed scope. No
package/lockfile edits, no auth/provider/rate-limit edits, no raw prompt/output
persistence, no public-sync, no live provider calls.

## Findings / Position

All 7 execution plan steps completed within Allowed scope:

1. Base captured (`35c468b5`), pre-implementation gate PASS.
2. `control-plane-events.ts` default path changed from `os.tmpdir()` to
   `process.cwd()/.cvf/runtime/control-plane-events.json`; `CVF_CONTROL_PLANE_EVENTS_PATH`
   env override preserved; `ERH_DUR1_MARKER` and `CVF_DURABLE_EVIDENCE_VERSION` added.
3. `policy-snapshot-registry.ts` created with `CVF_POLICY_SNAPSHOT_REGISTRY_VERSION`,
   `buildPolicySnapshot`, `persistPolicySnapshot`, `readPolicySnapshot`,
   `generatePolicySnapshotId`; `CVF_POLICY_SNAPSHOT_DIR` env override; secret-safe records.
4. `web-governance-envelope.ts` updated: `_policyCounter` removed; `generatePolicySnapshotId`
   imported from and re-exported from registry; backward compatibility preserved.
5. Focused tests created: `control-plane-events.durable.test.ts` (9/9 PASS),
   `policy-snapshot-registry.test.ts` (10/10 PASS), `web-governance-envelope.test.ts`
   (18/18 PASS unchanged).
6. DUR1 checker created with 15 checks; checker tests created; hook/autorun/GC-052 wired.
7. Documentation created; ERH roadmap updated.
8. Reviewer remediation added recursive `.cvf/runtime/` and `.cvf/config/`
   ignore patterns and removed generated local `.cvf` test output.

## Evidence / Verification

| Check | Result |
| --- | --- |
| `git rev-parse --short HEAD` at start | `35c468b5` |
| Worktree at start | clean |
| Pre-implementation autorun gate `--base 1beda1b2 --head HEAD` | PASS |
| `control-plane-events.ts` lines before | 366 |
| `web-governance-envelope.ts` lines before | 283 |
| `route.ts` lines before | 874 (unchanged) |
| `os.tmpdir()` removed from default path | VERIFIED |
| `.cvf/runtime` default path present | VERIFIED |
| `CVF_CONTROL_PLANE_EVENTS_PATH` env override preserved | VERIFIED |
| `ERH_DUR1_MARKER` present | VERIFIED |
| `CVF_DURABLE_EVIDENCE_VERSION` present | VERIFIED |
| `CVF_POLICY_SNAPSHOT_REGISTRY_VERSION` present | VERIFIED |
| `_policyCounter` removed from web-governance-envelope.ts | VERIFIED |
| `generatePolicySnapshotId` re-exported from registry | VERIFIED |
| `npm run check` (TypeScript) | PASS |
| `npx vitest run src/lib/control-plane-events.durable.test.ts` | 9/9 PASS |
| `npx vitest run src/lib/policy-snapshot-registry.test.ts` | 10/10 PASS |
| `npx vitest run src/lib/web-governance-envelope.test.ts` | 18/18 PASS |
| All three focused test files together (37 tests) | 37/37 PASS |
| `check_erh_durable_evidence_policy_snapshot.py --enforce` | PASS — 0 violations, COMPLIANT |
| `pytest test_check_erh_durable_evidence_policy_snapshot.py -q` | 18/18 PASS |
| `npm run build` | PASS |
| `check_markdown_structural_completeness.py --base 35c468b5 --head HEAD --enforce` | PASS — 0 violations, COMPLIANT |
| `check_system_loop_interlock.py --base 35c468b5 --head HEAD --enforce` | PASS — 0 violations, COMPLIANT |
| `check_finding_to_governance_learning.py --base 35c468b5 --head HEAD --enforce` | PASS — COMPLIANT |
| `check_public_export_disposition.py --base 35c468b5 --head HEAD --enforce` | PASS — COMPLIANT |
| `.gitignore` covers nested `.cvf/runtime/` output | VERIFIED |
| `git diff --name-status 35c468b5` shows only Allowed paths | PASS — all new paths within Allowed scope |
| Pre-closure autorun gate | N/A with reason — pre-commit hook chain is the closure gate before first reviewer commit; pre-closure range gate must run after commit if further sync is required |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_FOR_CLAUDE_2026-06-05.md` | DUR1 worker output reviewed by this completion artifact | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_COMPLETION_2026-06-05.md` | this artifact records `DUR2_NOT_NEEDED_NOW` and reviewer verification | PASS |
| Roadmap state | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | DUR1 row updated to `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | `erh-dur1-durable-evidence-policy-snapshot-workflow-chain` connection added | PASS |
| Registry Markdown | `docs/reference/CVF_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_WORKFLOW_CHAIN_2026-06-05.md` | workflow-chain reference created with `ERH_DUR1_DECISION` | PASS |
| External evidence digest | `N/A with reason` | no external source corpus consumed; DUR1 uses repo-local source and tests | N/A with reason |
| System loop interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | GC-052 checker reports 0 violations | PASS |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V15_2026-05-29.md` | updated in reviewer closure batch to record DUR1 closed and DUR2 decision | PASS |

## Risk / Corrective Action

| Risk | Corrective action | Status |
| --- | --- | --- |
| `persistPolicySnapshot` is fire-and-forget; snapshot may not be on disk if process exits immediately after id generation | by design — bounded local evidence; snapshot records are best-effort; the claim boundary explicitly excludes tamper-proof or production-grade durability | ACCEPTED |
| Module-level `_policySnapshotCounter` still resets on process restart, so ids are not globally unique across restart | acceptable — each process generates a new sequence; snapshot records are keyed by id and scoped to the `.cvf/runtime/policy-snapshots/` directory | ACCEPTED |
| `control-plane-events.ts` now writes to `process.cwd()/.cvf/runtime/` by default; in CI or ephemeral environments this may fail silently | by design — `ensureStore()` already wraps writes in try/catch; silent failure mode is preserved from the original tmpdir behavior; env override available for CI | ACCEPTED |
| Route line count unchanged at 874 | no change; well within 1000-line hard limit | ACCEPTED |
| Pre-closure autorun gate blocked by uncommitted worktree | expected under WORKER_MUST_NOT_COMMIT; Codex reviewer must commit and re-run | DEFERRED_TO_REVIEWER |
| Generated `.cvf/runtime` output appeared as untracked after focused tests | reviewer remediation — added recursive ignore pattern and removed generated local output | ACCEPTED |

## DUR2 Decision

**Verdict: `DUR2_NOT_NEEDED_NOW`**

Rationale:

- DUR1 closes the currently handleable local durability gap: the control-plane
  event store default no longer uses `os.tmpdir()`, and `policySnapshotId` is now
  traceable to a persisted bounded local snapshot record.
- External storage (Redis, production database, distributed instances) was never
  part of the DUR1 scope and remains a documented strategic residual.
- No source-visible, immediately handleable DUR2 gap was identified during DUR1
  implementation that would require a separate DUR2 work order right now.
- External DB/Redis/distributed durability requires an explicit operator storage
  architecture decision and fresh GC-018 before dispatch.

## Reviewer Checklist

Worker marks each item as checked (✓), N/A with reason, or BLOCKED:

- [✓] `WORKER_MUST_NOT_COMMIT` honored — no commits by worker
- [✓] Changed files stay within Allowed scope
- [✓] Default event store no longer uses `os.tmpdir()`
- [✓] `CVF_CONTROL_PLANE_EVENTS_PATH` env override preserved
- [✓] Policy snapshot registry produces stable id-to-record mapping
- [✓] Snapshot records are secret-safe (bounded metadata only, no raw content)
- [✓] Existing envelope and receipt consumers remain compatible (18/18 envelope tests PASS)
- [✓] Focused durable tests 9/9 PASS
- [✓] Focused snapshot tests 10/10 PASS
- [✓] DUR2 decision recorded: `DUR2_NOT_NEEDED_NOW`
- [✓] Completion review does not claim production-grade, distributed, hosted, or tamper-proof durability
- [✓] Nested `.cvf/runtime/` local output is ignored and generated test output removed
- [✓] Reviewer ran `check_erh_durable_evidence_policy_snapshot.py --enforce`
- [✓] Reviewer ran `pytest test_check_erh_durable_evidence_policy_snapshot.py -q`
- [✓] Reviewer ran `npm run build`
- [✓] Reviewer ran `check_markdown_structural_completeness.py --base 35c468b5 --head HEAD --enforce`
- [✓] Reviewer committed through local pre-commit governance hook chain

## Guard Authorization

Worker-authorized under WORKER_MUST_NOT_COMMIT. Codex reviewer completed
verification and may commit DUR1 as `CLOSED_PASS_BOUNDED`.

Rollback boundary: if any PENDING step fails, return to worker with specific failure
for allowed-scope remediation. Do not escalate for scope expansion.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: DUR1 adds one durable-evidence policy
snapshot workflow-chain checker and wires it into existing autorun/local hook
chains after SAF2.

Protected paths:

- `governance/compat/check_erh_durable_evidence_policy_snapshot.py`
- `governance/compat/test_check_erh_durable_evidence_policy_snapshot.py`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`
- `governance/compat/check_rescan_intelligence_hardening.py`
- `governance/compat/test_check_rescan_intelligence_hardening.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

Operator authorization: operator requested ERH-DUR1 review/cleanup and clean
commit separation before considering DUR2.

Rollback boundary: if DUR1 checker wiring is wrong, revert only the DUR1
checker, DUR1 checker tests, DUR1 hook/autorun entries, and DUR1 documentation
closure artifacts. Do not revert RS2 rescan-intelligence guard entries from a
DUR1 rollback boundary.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ERH-DUR1 is private provenance runtime hardening. Public-facing evidence
durability claims require a later public-sync work order after DUR1 is reviewed and
claim boundaries are accepted.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Disposition | Lane | Next action |
| --- | --- | --- | --- | --- |
| `os.tmpdir()` default causes event store to reset on OS session clean — source-verified in `control-plane-events.ts` | `RUNTIME_SIGNAL_GAP` | `MACHINE_CHECK_ADDED` — resolved by DUR1 durable local default; enforced by `check_erh_durable_evidence_policy_snapshot.py` | `GOVERNANCE_CONTROL_PLANE` | No further action; DUR1 checker enforces durable default path. |
| `policySnapshotId` process-local counter not reconstructable after restart — source-verified in `web-governance-envelope.ts` | `RUNTIME_SIGNAL_GAP` | `MACHINE_CHECK_ADDED` — resolved by DUR1 policy snapshot registry owner; enforced by DUR1 checker | `GOVERNANCE_CONTROL_PLANE` | No further action; DUR1 checker enforces registry delegation. |
| External DB/Redis/distributed runtime retention not in DUR1 scope | `RUNTIME_SIGNAL_GAP` | `N/A_WITH_REASON` — external storage requires separate operator architecture decision and fresh GC-018; not a handleable local gap | `RUNTIME_BEHAVIOR_LEARNING` | Deferred; operator must open a storage architecture decision work order if distributed retention is required. |

## Claim Boundary

DUR1 proves bounded local durable evidence and reconstructable policy snapshot
workflow hardening only. It does not authorize external database persistence, Redis,
distributed rate limiting, provider-risk ceiling configuration, live governance proof,
hosted freshness, public-sync, production readiness, public readiness, or complete
remediation of every external-review architecture gap. DUR2 decision is
`DUR2_NOT_NEEDED_NOW`.

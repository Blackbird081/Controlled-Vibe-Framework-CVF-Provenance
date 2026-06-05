# CVF Agent Work Order - ERH-DUR1 Durable Evidence And Policy Snapshot For Claude

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-05

GC-018: `docs/baselines/CVF_GC018_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_2026-06-05.md`

dispatchBaseHead: `1beda1b2`

dispatchCommit: `b3c4ce3a`

executionBaseHead: `35c468b5`

closureBaseHead: `49e6725a`

Assigned worker: Claude

Commit mode: `WORKER_MUST_NOT_COMMIT`

Reviewer closure: Codex reviewed Claude's DUR1 output, completed the pending
verification steps, added recursive `.cvf/runtime/` and `.cvf/config/` ignore
coverage for generated local durable output, and closed DUR1 as
`CLOSED_PASS_BOUNDED` in
`docs/reviews/CVF_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_COMPLETION_2026-06-05.md`.

## Purpose

Implement ERH-DUR1: convert two external-review architecture findings into a
bounded workflow chain:

- move the control-plane event store default away from OS temp storage into a
  durable local `.cvf/runtime` style store while preserving the existing env
  override;
- make `policySnapshotId` reconstructable by mapping each id to a persisted
  bounded policy snapshot record.

Success means the runtime owner functions still work, durable evidence remains
secret-safe, the new policy snapshot registry can be tested without provider
calls, and a machine checker verifies the workflow-chain markers.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-05: after SAF3 not needed, create the next Claude work order for handleable ERH architecture gap | ACCEPT |
| Fresh GC-018 | `docs/baselines/CVF_GC018_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_2026-06-05.md` | ACCEPT |
| SAF2 closure | `docs/reviews/CVF_ERH_SAF2_OUTPUT_SAFETY_AND_REGRESSION_CORPUS_COMPLETION_2026-06-05.md`; commit `cf88f9cb`; session sync through `1beda1b2` | ACCEPT |
| ERH-RS1 full rescan | `docs/reviews/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_COMPLETION_2026-06-04.md` | ACCEPT |
| ERH roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |

Authority boundary:

- This work order authorizes DUR1 only.
- Do not implement Redis, database migration, rate limiter, provider-risk
  ceiling config, public-sync, live proof, or production-readiness claims.
- Do not commit or push.

## Scope / Target / Owner Boundary

Allowed scope:

- update `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts`:
  - preserve `CVF_CONTROL_PLANE_EVENTS_PATH` override;
  - change the default event path from `os.tmpdir()` to a repo/app-local
    `.cvf/runtime/control-plane-events.json` style path;
  - keep append/read/cost/audit/CSV/SIEM behavior compatible;
  - add `ERH_DUR1_MARKER` and `CVF_DURABLE_EVIDENCE_VERSION` markers;
- create or update a bounded policy snapshot owner module, preferably
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.ts`:
  - build a secret-safe snapshot record from existing envelope inputs;
  - persist snapshot records under a local `.cvf/runtime/policy-snapshots`
    style path with an env override such as `CVF_POLICY_SNAPSHOT_DIR`;
  - export read/build helpers used by tests and envelope construction;
  - add `CVF_POLICY_SNAPSHOT_REGISTRY_VERSION` marker;
- update `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`:
  - generate `policySnapshotId` from the policy snapshot owner, not from a
    process-local monotonic counter;
  - keep the public envelope and receipt field names compatible;
  - avoid adding raw prompts, raw outputs, secrets, or private memory payloads;
- add focused tests:
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.durable.test.ts`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.test.ts`
  - update `web-governance-envelope.test.ts` only if required by the new id
    semantics;
- create `governance/compat/check_erh_durable_evidence_policy_snapshot.py`;
- create `governance/compat/test_check_erh_durable_evidence_policy_snapshot.py`;
- update `governance/compat/run_local_governance_hook_chain.py`;
- update `governance/compat/run_agent_autorun_workflow_gate.py`;
- reviewer remediation may update
  `governance/compat/check_work_order_dispatch_quality.py` and
  `governance/compat/test_check_work_order_dispatch_quality.py` only to let
  closed work orders source-verify root `.gitignore` allowed-scope paths;
- reviewer remediation may update
  `governance/compat/check_rescan_intelligence_hardening.py` and
  `governance/compat/test_check_rescan_intelligence_hardening.py` only to avoid
  false positives against non-rescan runtime work orders that merely cite
  external-review findings;
- update `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- create `docs/reference/CVF_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_WORKFLOW_CHAIN_2026-06-05.md`;
- create `docs/reference/CVF_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_LEDGER_2026-06-05.md`;
- create `docs/reviews/CVF_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_COMPLETION_2026-06-05.md`;
- update `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md`;
- update `.gitignore` only to ignore generated local `.cvf/runtime/` and
  `.cvf/config/` durable-output directories across nested app workspaces;
- Codex reviewer may update `CVF_SESSION/ACTIVE_SESSION_STATE.json`,
  `CVF_SESSION_MEMORY.md`, and `AGENT_HANDOFF_V15_2026-05-29.md` only to
  record DUR1 dispatch or closure status.

Forbidden scope:

- package manifests, lockfiles, auth runtime, provider routing, dependency
  migration, rate limiter, Redis/database adapters, public-sync clone, `.env*`;
- broad `/api/execute` refactor;
- raw prompt/output/secret/private-memory persistence;
- live provider proof, hosted-readiness, production-readiness, public-readiness,
  or production-grade durability claims;
- commit or push.

Risk ceiling: R2. Escalate before external storage, sync/async route contract
changes, package edits, auth/rate-limit/provider edits, public-sync, live proof,
or claim-boundary expansion.

## Agent Roles

| Role | Assignee | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | authored DUR1 dispatch packet; reviews Claude output |
| Worker | Claude | implement DUR1 within Allowed scope under `WORKER_MUST_NOT_COMMIT` |
| Reviewer | Codex or human | verify diff, tests, gates, claim boundary, residuals |
| Human authorization required for | public-sync, push, external DB/Redis, package changes, provider/live proof, secrets | not included in DUR1 |

## Required First Reads

| Path | Why it matters |
| --- | --- |
| `docs/baselines/CVF_GC018_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_2026-06-05.md` | tranche authority |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | current control-plane event store owner |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | current envelope and receipt policySnapshotId owner |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/admin/audit/route.ts` | admin audit read/write route through event owner |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/admin/audit-feed/route.ts` | audit CSV export route through event owner |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | GC-052 workflow-chain registration pattern |

## Pre-Flight Checks

| Command | Required result |
| --- | --- |
| `git rev-parse --short HEAD` | Claude captures execution base before editing |
| `git status --short` | Claude records existing worktree state |
| `Get-Content EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts \| Measure-Object -Line` | current count recorded; source is not near hard limit |
| `Get-Content EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts \| Measure-Object -Line` | current count recorded; source is not near hard limit |
| `Get-Content EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts \| Measure-Object -Line` | route count recorded; broad route edit remains forbidden |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 1beda1b2 --head HEAD` | PASS before implementation |

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Control-plane event store has env override | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 86-89 | `CVF_CONTROL_PLANE_EVENTS_PATH` | `getStorePath` | ACCEPT |
| Control-plane event store default uses OS temp directory | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | line 89 | `getStorePath` | `getStorePath` | ACCEPT |
| ensureStore initializes the store file | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 92-107 | `ensureStore` | control-plane event store | ACCEPT |
| writeEvents writes the full event array | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 110-113 | `writeEvents` | control-plane event store | ACCEPT |
| readControlPlaneEvents reads and sorts owner events | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 181-199 | `readControlPlaneEvents` | control-plane event store | ACCEPT |
| appendEvent queues append operations and writes owner store | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 201-218 | `appendEvent` | control-plane event store | ACCEPT |
| appendAuditEvent delegates to appendControlPlaneEvent and SIEM forwarder | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 230-241 | `appendAuditEvent` | control-plane event store | ACCEPT |
| Admin audit route reads audit events through control-plane owner | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/admin/audit/route.ts` | lines 4 and 14-15 | `readAuditEvents` | `/api/admin/audit` GET | ACCEPT |
| Audit feed route exports CSV through control-plane owner | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/admin/audit-feed/route.ts` | lines 4 and 13-15 | `exportAuditEventsToCsv` | `/api/admin/audit-feed` GET | ACCEPT |
| Web governance envelope declares policySnapshotId | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | line 32 | `policySnapshotId` | `WebGovernanceEnvelope` | ACCEPT |
| Policy snapshot id currently uses process-local counter | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 39 and 47-50 | `_policyCounter` | `generatePolicySnapshotId` | ACCEPT |
| buildGovernanceEnvelope assigns generated policySnapshotId | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 88 and 100 | `buildGovernanceEnvelope` | web governance envelope | ACCEPT |
| buildEvidenceReceipt copies policySnapshotId into receipt | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 245 and 257 | `buildEvidenceReceipt` | governance evidence receipt builder | ACCEPT |
| GovernanceEvidenceReceipt type includes policySnapshotId | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | lines 99-108 | `policySnapshotId` | `GovernanceEvidenceReceipt` | ACCEPT |
| Execute route builds governance envelope once per request | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 25 and 80 | `buildGovernanceEnvelope` | `/api/execute` POST route | ACCEPT |
| Execute route propagates policySnapshotId in response payloads | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 413-414, 441-442, 486, 510-511, 584-585, 613-614, 724-725, 837-838 | `policySnapshotId` | `/api/execute` response payloads | ACCEPT |
| control-plane-events.ts current line count is 315 | LINE_COUNT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | full file | `control-plane-events.ts` | GC-023 file-size guard | ACCEPT |
| web-governance-envelope.ts current line count is 256 | LINE_COUNT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | full file | `web-governance-envelope.ts` | GC-023 file-size guard | ACCEPT |
| route.ts current line count is 874 | LINE_COUNT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | full file | `POST` | GC-023 file-size guard | ACCEPT |

## New Doc-Only Fields

| New field or marker | Purpose | Not sourced from runtime? | Runtime claim blocked? |
| --- | --- | --- | --- |
| `ERH_DUR1_MARKER` | Machine marker that DUR1 durable evidence workflow is installed | Yes | Yes - checker marker only until implemented |
| `CVF_DURABLE_EVIDENCE_VERSION` | Version marker for bounded local durable event-store contract | Yes | Yes - no production database claim |
| `CVF_POLICY_SNAPSHOT_REGISTRY_VERSION` | Version marker for reconstructable policy snapshot records | Yes | Yes - no external policy service claim |
| `ERH_DUR1_LEDGER_VERSION` | Ledger marker for DUR1 evidence and residuals | Yes | Yes - documentation/checker marker |
| `CVF_POLICY_SNAPSHOT_DIR` | Optional env override for snapshot store location | Yes | Yes - implementation must source it in new owner module before claiming runtime support |

## Current Runtime Freshness Verification

| Runtime fact | Fresh evidence | Disposition |
| --- | --- | --- |
| Control-plane event default path still uses OS temp | source read at dispatch base `1beda1b2`, line 89 | ACCEPT |
| Control-plane event env override still exists | source read at dispatch base `1beda1b2`, lines 86-89 | ACCEPT |
| Policy snapshot id still uses process-local counter | source read at dispatch base `1beda1b2`, lines 39 and 47-50 | ACCEPT |
| Governance receipt still carries policySnapshotId | source read at dispatch base `1beda1b2`, `buildEvidenceReceipt` line 257 and `GovernanceEvidenceReceipt` line 108 | ACCEPT |
| Admin audit routes still depend on the shared control-plane event owner | source read at dispatch base `1beda1b2`, audit route lines 4 and 14-15; audit-feed route lines 4 and 13-15 | ACCEPT |
| route.ts line count is 874 | measured at dispatch base `1beda1b2` | ACCEPT |
| control-plane-events.ts line count is 315 | measured at dispatch base `1beda1b2` | ACCEPT |
| web-governance-envelope.ts line count is 256 | measured at dispatch base `1beda1b2` | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or predecessor requirement | DUR1 output | Evidence | Status |
| --- | --- | --- | --- |
| ERH-RS1 section 4.4 audit storage weakness | Durable local control-plane event store default, preserving env override | `control-plane-events.ts` source facts | PASS |
| ERH-RS1 section 4.4 policySnapshotId reconstructability weakness | Persisted policy snapshot registry and id-to-record read path | `web-governance-envelope.ts` source facts | PASS |
| ERH-T3 durability was docs-only | DUR1 converts the handleable local runtime subset into source/test/checker workflow | ERH roadmap and T3 boundary | PASS |
| Avoid overclaiming production durability | Completion review must record residual external DB/distributed durability boundary | DUR1 claim boundary | PASS |

## Write Ownership

| Owned path | Mode |
| --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | bounded update |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.test.ts` | update only if existing expectations require it |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.durable.test.ts` | create |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.ts` | create |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.test.ts` | create |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | bounded update |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.test.ts` | update only if required by policySnapshotId semantics |
| `governance/compat/check_erh_durable_evidence_policy_snapshot.py` | create |
| `governance/compat/test_check_erh_durable_evidence_policy_snapshot.py` | create |
| `governance/compat/check_work_order_dispatch_quality.py` | reviewer remediation for root `.gitignore` path parsing only |
| `governance/compat/test_check_work_order_dispatch_quality.py` | reviewer remediation test for root `.gitignore` path parsing only |
| `governance/compat/check_rescan_intelligence_hardening.py` | reviewer remediation for non-rescan runtime work-order false positive only |
| `governance/compat/test_check_rescan_intelligence_hardening.py` | reviewer remediation test for non-rescan runtime work-order false positive only |
| `governance/compat/run_local_governance_hook_chain.py` | update |
| `governance/compat/run_agent_autorun_workflow_gate.py` | update |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | update |
| `docs/reference/CVF_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_WORKFLOW_CHAIN_2026-06-05.md` | create |
| `docs/reference/CVF_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_LEDGER_2026-06-05.md` | create |
| `docs/reviews/CVF_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_COMPLETION_2026-06-05.md` | create |
| `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | update DUR1 row |
| `.gitignore` | update recursive `.cvf/runtime/` and `.cvf/config/` local output ignore coverage |

Forbidden paths: package manifests, lockfiles, auth runtime, provider router,
rate limiter, public-sync clone, `.env*`, unrelated source files.

## Worker Autonomy / No-Question Rule

Claude must fix allowed-scope machine-gate failures directly and rerun the
gate. Do not ask the operator whether to repair an allowed-scope guard failure.

Escalate only for scope expansion, external storage, claim-boundary changes,
public-sync, live/provider proof, secrets/quota, package changes, auth/rate
limit/provider edits, forbidden paths, or destructive/irreversible actions.

## Execution Plan

| Step | Action | Output | Stop condition |
| --- | --- | --- | --- |
| 1 | Capture execution base/status and run pre-implementation gate | base evidence | gate failure outside Allowed scope |
| 2 | Move default event store from OS temp to local `.cvf/runtime` path while preserving env override | durable local event owner | append/read compatibility breaks |
| 3 | Add policy snapshot registry owner and tests | id-to-record mapping, safe persisted records | raw prompt/output/secret would be stored |
| 4 | Wire envelope policySnapshotId through registry owner | reconstructable receipt id path | envelope/receipt field compatibility breaks |
| 5 | Add DUR1 checker, checker tests, hook/autorun wiring, GC-052 entry | machine workflow gate | checker cannot be bounded to source markers |
| 6 | Create workflow reference, ledger, completion review | review-ready packet | completion overclaims production DB/distributed durability |
| 7 | Run focused tests, TypeScript check, build, governance gates | all PASS or classified failure | failure outside Allowed scope |

## Required Artifact Manifest

| Required artifact | Required status at return | Forbidden substitution |
| --- | --- | --- |
| Durable local event-store default | source diff with `ERH_DUR1_MARKER` and preserved env override | docs-only durability claim |
| Policy snapshot registry | source file with `CVF_POLICY_SNAPSHOT_REGISTRY_VERSION` and read/build helpers | process-local counter only |
| Snapshot tests | PASS | manual-only assertion |
| Durable event tests | PASS | no test for default path |
| DUR1 checker | PASS | no checker |
| focused checker tests | PASS | no pytest |
| workflow-chain reference doc | created with decision marker | unversioned notes |
| ledger doc | created with `ERH_DUR1_LEDGER_VERSION` | no residuals |
| completion review | created with residual DB/Redis/distributed boundary | production durability claim |

## Work-Order Fulfillment Manifest

| Fulfillment item | Required evidence at worker return | Disposition before execution |
| --- | --- | --- |
| Durable local event-store default | source diff plus focused durable event tests | NOT_EXECUTED |
| Policy snapshot registry | source diff plus focused snapshot tests | NOT_EXECUTED |
| DUR1 checker | checker source, pytest, hook/autorun wiring | NOT_EXECUTED |
| Workflow docs | reference, ledger, completion review | NOT_EXECUTED |
| Claim boundary | completion review residuals and DUR2 decision | NOT_EXECUTED |

The worker must replace every `NOT_EXECUTED` row with concrete evidence in the
completion review. This dispatch packet intentionally records the expected
fulfillment shape before implementation.

## Acceptance Criteria

- Default control-plane event storage no longer points to `os.tmpdir()` unless
  explicitly forced by `CVF_CONTROL_PLANE_EVENTS_PATH`.
- Existing audit/cost append, read, CSV export, corruption repair, and SIEM
  forward behavior remain compatible.
- `policySnapshotId` maps to a persisted, secret-safe snapshot record through a
  testable read path.
- Durable event and policy snapshot focused tests pass.
- DUR1 checker and checker tests pass, and the checker is wired into local hook
  and autorun gate chains.
- GC-052 interlock contains a DUR1 workflow-chain connection with bounded claim
  boundary.
- Completion review records one DUR2 residual decision and does not claim
  production-grade, distributed, hosted, public, or tamper-proof durability.

## DUR1 Behavior Requirements

| Requirement | Required behavior |
| --- | --- |
| Durable local default | Default event store path must be repo/app-local `.cvf/runtime/control-plane-events.json` or equivalent, not `os.tmpdir()` |
| Env override preserved | `CVF_CONTROL_PLANE_EVENTS_PATH` must continue to override the default |
| Append/read compatibility | `appendAuditEvent`, `appendCostEvent`, `readAuditEvents`, `readCostEvents`, `exportAuditEventsToCsv` remain compatible |
| Snapshot id reconstructability | `policySnapshotId` must be traceable to a persisted snapshot record through a testable read path |
| Secret-safe persistence | Persisted event/snapshot records must not include raw prompts, raw AI output, API keys, provider secrets, or private memory payloads |
| Bounded claim | DUR1 claims local durable evidence only, not production database, distributed instances, Redis, external retention, or tamper-proof audit |

## Post-DUR1 Decision Rules

Completion review must include one residual decision:

| Verdict | Use when |
| --- | --- |
| `DUR2_READY` | DUR1 passes and source-visible need remains for DB/Redis/distributed retention work |
| `DUR2_HOLD` | DUR1 evidence is insufficient or next step requires operator storage architecture choice |
| `DUR2_NOT_NEEDED_NOW` | DUR1 closes the currently handleable local durability gap; external storage remains documented strategic residual |

DUR2 implementation is forbidden in this work order.

## Evidence Requirements

| Evidence | Path or command | Required |
| --- | --- | --- |
| Base anchor | `git rev-parse --short HEAD` | Yes |
| Worktree start state | `git status --short` | Yes |
| File counts before edit | three `Measure-Object -Line` commands in Pre-Flight Checks | Yes |
| TypeScript check | `npm run check` from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` | Yes |
| Focused durable event tests | `npm run test:run -- src/lib/control-plane-events.durable.test.ts` | Yes |
| Focused policy snapshot tests | `npm run test:run -- src/lib/policy-snapshot-registry.test.ts src/lib/web-governance-envelope.test.ts` | Yes |
| Build | `npm run build` from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` | Yes |
| DUR1 checker | `python governance/compat/check_erh_durable_evidence_policy_snapshot.py --enforce` | Yes |
| Checker tests | `python -m pytest governance/compat/test_check_erh_durable_evidence_policy_snapshot.py` | Yes |
| Autorun pre-closure | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD` | Yes |
| Allowed-path proof | `git diff --name-status <executionBaseHead> HEAD` | Yes |
| Closure worktree state | `git status --short` | Yes |

Live proof: N/A with reason. DUR1 changes deterministic local storage and
receipt metadata only, with no provider behavior claim.

## Review Gate

Reviewer must verify:

- `WORKER_MUST_NOT_COMMIT` was honored;
- changed files stay within Allowed scope;
- default event store no longer uses `os.tmpdir()` unless an explicit env
  override points there;
- `CVF_CONTROL_PLANE_EVENTS_PATH` remains supported;
- policy snapshot registry produces a stable id-to-record mapping;
- snapshot records are secret-safe and bounded to policy/evidence metadata;
- existing envelope and receipt consumers remain compatible;
- checker and focused tests pass;
- completion review records DUR2 residual decision and does not claim
  production-grade durability.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_FOR_CLAUDE_2026-06-05.md` | this work order status `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_COMPLETION_2026-06-05.md` | completion review status `CLOSED_PASS_BOUNDED`; DUR2 decision recorded | PASS |
| Roadmap state | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ERH-DUR1 row `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | GC-052 connection `erh-dur1-durable-evidence-policy-snapshot-workflow-chain` added | PASS |
| Registry Markdown | `docs/reference/CVF_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_WORKFLOW_CHAIN_2026-06-05.md` | workflow-chain reference created with `ERH_DUR1_DECISION` | PASS |
| External evidence digest | `N/A with reason` | no external corpus/source consumed; DUR1 uses repo-local source and tests | N/A with reason |
| System loop interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | `check_system_loop_interlock.py --base 49e6725a --head HEAD --enforce` reports 0 violations | PASS |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V15_2026-05-29.md` | continuity updated to DUR1 closed and DUR2 not needed now | PASS |

## Closure Checklist

Worker must mark each item in the completion review as checked, N/A with reason,
or BLOCKED with return-to-orchestrator action:

- pre-implementation autorun gate run with captured execution base;
- source diff limited to Allowed scope;
- no package, lockfile, auth, provider, rate-limit, public-sync, `.env*`, or
  unrelated file changes;
- no raw prompt, raw output, secret, API key, or private memory persistence;
- TypeScript check, focused tests, build, checker, checker tests, and
  pre-closure autorun evidence recorded;
- `git status --short` and `git diff --name-status <executionBaseHead> HEAD`
  evidence recorded;
- DUR2 residual decision recorded.

## Operator Checkpoint

No operator input is required for allowed-scope implementation or remediation.

Return to operator only if DUR1 needs external DB/Redis, package changes,
auth/rate-limit/provider edits, public-sync, live/provider proof, secrets/quota,
claim-boundary expansion, forbidden paths, destructive action, or a storage
architecture decision outside the local durable boundary.

## Failure Conditions

Return to Orchestrator if:

- package, lockfile, auth, rate-limit, provider, public-sync, `.env*`, or
  unrelated files require edits;
- implementation requires external DB/Redis or a storage architecture decision;
- any durable record would store raw prompt, raw output, secret, API key, or
  private memory payload;
- route contract must become async in a way that breaks existing callers;
- route.ts would exceed governed hard line-count threshold;
- checker cannot verify the workflow through source markers and tests;
- completion artifact claims hosted, public, production, distributed, or
  tamper-proof durability.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Codex reviewer may update
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, and
`AGENT_HANDOFF_V15_2026-05-29.md` to record DUR1 dispatch or reviewed closure
status.

Protected paths:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V15_2026-05-29.md`

Operator authorization: 2026-06-05 operator approved creation of the next
Claude work order after SAF3 was ruled unnecessary for current ERH safety
scope.

Rollback boundary: if continuity sync is wrong, restore only the DUR1
continuity text or active-state keys. Do not revert DUR1 source, checker,
roadmap, work-order, review, or historical handoff content.

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason - this work order dispatches runtime
  hardening; it is not a corpus scan or inventory task
- Corpus root: N/A with reason
- Snapshot time: N/A with reason
- Enumeration command: `rg --files --hidden --no-ignore docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_FOR_CLAUDE_2026-06-05.md`
- Manifest artifact or inline manifest: N/A with reason
- Manifest hash: N/A with reason
- Processing ledger artifact or inline ledger: N/A with reason
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=0; ledger_terminal=0; exclusions=0; unresolved=0
- Unresolved files: 0
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: N/A with reason
- Drift check: N/A with reason
- Output traceability: N/A with reason
- Adversarial verification: N/A with reason
- Corpus verdict: COMPLETE_VERIFIED

No corpus completeness claim is made.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Default control-plane event path is OS temp | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | MACHINE_CHECK_CANDIDATE | DUR1 durable local event-store checker |
| policySnapshotId is not tied to persisted snapshot record | AUDIT_RECONSTRUCTABILITY_GAP | RUNTIME_BEHAVIOR_LEARNING | MACHINE_CHECK_CANDIDATE | DUR1 policy snapshot registry |
| ERH-T3 durability was docs-only | DOCUMENTATION_ONLY_GAP | GOVERNANCE_CONTROL_PLANE | WORKFLOW_CHAIN_REQUIRED | DUR1 runtime workflow chain |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ERH-DUR1 is private provenance runtime hardening and dispatch planning.

Next action: public-facing evidence durability claims require a later
public-sync work order after DUR1 is reviewed and claim boundaries are accepted.

## Claim Boundary

This work order authorizes bounded local durable evidence and reconstructable
policy snapshot workflow hardening only. It does not authorize external
database persistence, Redis, distributed rate limiting, provider risk ceiling
configuration, live governance proof, hosted freshness, public-sync, production
readiness, public readiness, or complete remediation of every external-review
architecture gap.

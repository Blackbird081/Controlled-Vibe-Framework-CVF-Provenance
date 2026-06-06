# CVF Agent Work Order - ERH-T2C Route Governance Proof Hardening

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-04

dispatchBaseHead: `7c7dfc52`

executionBaseHead: `7c7dfc52`

closureBaseHead: `dd49a3bf`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Implement the bounded ERH-T2C route governance proof hardening tranche. Success
means the five routes marked `MISSING_ROUTE_GOVERNANCE_PROOF` in ERH-T2A use a
shared route governance proof workflow chain, emit secret-safe route governance
proof, and have focused tests for allowed and denied behavior.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator authorization | 2026-06-04 instruction to choose and proceed with the strongest remaining grounded tranche | ACCEPT |
| ERH roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT |
| ERH-T2A route ledger | `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | ACCEPT |
| GC-018 T2C baseline | `docs/baselines/CVF_GC018_ERH_T2C_ROUTE_GOVERNANCE_PROOF_HARDENING_2026-06-04.md` | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- add one shared `cvf-web` route governance proof helper;
- update only the five ERH-T2A missing-proof route files;
- update or add focused tests for the helper and those five routes;
- add a private reference packet and GC-052 system-loop connection for the
  route governance proof workflow chain;
- update ERH private roadmap/review artifacts with bounded T2C status.
- reviewer closure may update
  `docs/reference/CVF_ERH_T2C_ROUTE_GOVERNANCE_PROOF_WORKFLOW_CHAIN_2026-06-04.md`;
- reviewer closure may update
  `docs/reviews/CVF_ERH_T2C_ROUTE_GOVERNANCE_PROOF_HARDENING_COMPLETION_2026-06-04.md`;
- reviewer closure may update
  `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md`.

Forbidden scope:

- no `/api/execute` behavior changes;
- no provider/live proof or secret use;
- no public-sync clone edits;
- no CI workflow rewrites;
- no production, hosted, or public readiness claim.

Risk ceiling: R1 local runtime-source hardening, no live/provider execution.

## Agent Roles

| Role | Assignee | Boundary |
| --- | --- | --- |
| Orchestrator / dispatcher | Codex | select and dispatch bounded T2C route hardening |
| Implementer | Codex | helper, five route files, focused tests, private completion packet |
| Reviewer / committer | Codex closure review | bounded closure only; no public-sync, hosted, production, or route-complete claim |
| Operator approval required for | public-sync, live/provider proof, CI workflow rewrite, commit/push | not included in this work order |

## Required First Reads

| Path | Why it matters |
| --- | --- |
| `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | defines the five missing-proof routes |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | current session helper |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | current service-token verifier |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | existing session-or-service-token route pattern |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | existing read-body-once auth pattern |

## Pre-Flight Checks

| Command | Required result |
| --- | --- |
| `git rev-parse --short HEAD` | `7c7dfc52` at dispatch start |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 7c7dfc52 --head HEAD` | PASS |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 7c7dfc52 --head HEAD` | PASS before route edits |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: route ledger missing-proof disposition exists | `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | lines 50, 76, 96, 108, 111, 112, 134 | `MISSING_ROUTE_GOVERNANCE_PROOF` | ERH-T2A route ledger | ACCEPT |
| EXISTS: artifact export route POST exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | line 234 | `POST` | artifact export route | ACCEPT |
| EXISTS: governance override route POST exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/override/route.ts` | line 4 | `POST` | governance override route | ACCEPT |
| EXISTS: knowledge ingest route POST exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/knowledge/ingest/route.ts` | line 16 | `POST` | knowledge ingest route | ACCEPT |
| EXISTS: LPCI intake route POST exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/intake/route.ts` | line 50 | `POST` | LPCI intake route | ACCEPT |
| EXISTS: LPCI query route POST exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | line 91 | `POST` | LPCI query route | ACCEPT |
| EXISTS: session helper exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | line 75 | `verifySessionCookie` | middleware auth helper | ACCEPT |
| EXISTS: service-token verifier exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | line 37 | `verifyServiceTokenRequest` | service token auth helper | ACCEPT |
| RUNTIME_BEHAVIOR: execute route accepts session or service token | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 45-68 | `verifyServiceTokenRequest` | execute route auth pattern | ACCEPT |
| EXISTS: system loop interlock registry exists | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | `connections` array | `connections` | GC-052 registry | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order output | Verification | Status |
| --- | --- | --- | --- |
| ERH route coverage missing-proof gap must not remain merely caveated | shared helper plus five route updates | focused tests and source search | PASS |
| Do not overclaim lexical route hits as governance proof | routeGovernanceProof is emitted from runtime guard, not docs prose | response assertions | PASS |
| Keep public-sync separate | no public-sync path in allowed scope | `git diff --name-status` | PASS |
| Keep live/provider proof separate | no route-specific hosted/live proof claim | completion claim boundary | PASS |

## Worker Autonomy / No-Question Rule

The worker proceeds autonomously for source reads, allowed route/helper/test
edits, focused test remediation, and governance gate reruns inside this work
order. Escalation is reserved for public-sync, live/provider proof, secrets or
quota, CI workflow rewrites, `/api/execute` edits, destructive actions, or a
claim-boundary expansion.

## Write Ownership

| Owned path | Mode |
| --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | create |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.test.ts` | create |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | modify-listed |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/override/route.ts` | modify-listed |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/knowledge/ingest/route.ts` | modify-listed |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/intake/route.ts` | modify-listed |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | modify-listed |
| `docs/baselines/CVF_GC018_ERH_T2C_ROUTE_GOVERNANCE_PROOF_HARDENING_2026-06-04.md` | create/update |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T2C_ROUTE_GOVERNANCE_PROOF_HARDENING_2026-06-04.md` | create/update |
| `docs/reviews/CVF_ERH_T2C_ROUTE_GOVERNANCE_PROOF_HARDENING_COMPLETION_2026-06-04.md` | create |
| `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | update T2C status only |
| `docs/reference/CVF_ERH_T2C_ROUTE_GOVERNANCE_PROOF_WORKFLOW_CHAIN_2026-06-04.md` | create |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | add one ERH-T2C connection |

Forbidden paths are listed in the Forbidden Path Manifest below.

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | Yes | shared guard and proof helper |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.test.ts` | Yes | helper authorization tests |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | Yes | route wiring |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/override/route.ts` | Yes | route wiring |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/knowledge/ingest/route.ts` | Yes | route wiring |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/intake/route.ts` | Yes | route wiring |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | Yes | route wiring |
| `docs/reviews/CVF_ERH_T2C_ROUTE_GOVERNANCE_PROOF_HARDENING_COMPLETION_2026-06-04.md` | Yes | completion packet |
| `docs/reference/CVF_ERH_T2C_ROUTE_GOVERNANCE_PROOF_WORKFLOW_CHAIN_2026-06-04.md` | Yes | workflow chain contract |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | Yes | GC-052 system loop connection |

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | high-risk main governance execution route outside this tranche |
| `d:/UNG DUNG AI/TOOL AI 2026/Controlled-Vibe-Framework-CVF-public-sync/**` | public-sync requires separate authorization |
| `.github/workflows/**` | CI hardening is a separate ERH tranche |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
| --- | --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | do not edit |
| `d:/UNG DUNG AI/TOOL AI 2026/Controlled-Vibe-Framework-CVF-public-sync/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | do not edit |
| `.github/workflows/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | do not edit |

## Pre-Existing Dirty Path Exemptions

| Path | Status at dispatch | Exemption boundary |
| --- | --- | --- |
| `docs/reference/CVF_ERH_T1B_PUBLIC_SYNC_HANDOFF_2026-06-04.md` | M | prior ERH-T1C export evidence, do not revert |
| `docs/reviews/CVF_ERH_EXTERNAL_REVIEW_HARDENING_PRIVATE_TRANCHES_COMPLETION_2026-06-04.md` | M | prior ERH-T1C export evidence, do not revert |
| `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | M | may update only for T2C status |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T1B_PUBLIC_SYNC_HANDOFF_2026-06-04.md` | M | prior ERH-T1C export evidence, do not revert |
| `docs/reviews/CVF_ERH_T1C_PUBLIC_SYNC_LOCAL_CLAIM_BOUNDARY_PREP_COMPLETION_2026-06-04.md` | ?? | prior ERH-T1C export evidence, do not revert |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T1C_PUBLIC_SYNC_LOCAL_CLAIM_BOUNDARY_PREP_2026-06-04.md` | ?? | prior ERH-T1C export evidence, do not revert |

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| helper proof schema | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | `routeGovernanceProof` | Yes |
| workflow chain version | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | `ROUTE_GOVERNANCE_PROOF_WORKFLOW_CHAIN_VERSION` | Yes |
| service token header | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | `x-cvf-service-token` | Yes |
| no secret echo | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.test.ts` | `serviceTokenConfigured` | Yes |
| five-route closure | `docs/reviews/CVF_ERH_T2C_ROUTE_GOVERNANCE_PROOF_HARDENING_COMPLETION_2026-06-04.md` | `5/5` | Yes |

## Execution Plan

| Step | Input | Output | Stop condition |
| --- | --- | --- | --- |
| 1 | existing auth helpers | shared workflow chain helper | helper type/test failure |
| 2 | five route files | registry-driven guard wiring and proof response | route test failure outside scope |
| 3 | focused test suite | PASS evidence | inability to preserve existing behavior |
| 4 | system loop registry | GC-052 connection | system-loop gate failure |
| 5 | private ERH docs | completion packet and roadmap update | governance gate failure outside scope |

## Evidence Requirements

| Evidence | Path or command | Required result |
| --- | --- | --- |
| Focused tests | `npm run test:run -- src/lib/route-governance-proof.test.ts src/app/api/artifacts/export/route.test.ts src/app/api/knowledge/ingest/route.test.ts src/app/api/knowledge/ingest/w116-cp5-delta.test.ts src/app/api/lpci/intake/route.test.ts src/app/api/lpci/query/route.test.ts` | PASS |
| TypeScript check | `npm run check` in `cvf-web` | PASS or bounded failure recorded if unrelated |
| Markdown structural | `python governance/compat/check_markdown_structural_completeness.py --base 7c7dfc52 --head HEAD --all-changed --enforce` | PASS |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 7c7dfc52 --head HEAD --enforce` | PASS |
| Finding learning | `python governance/compat/check_finding_to_governance_learning.py --base 7c7dfc52 --head HEAD --enforce` | PASS |
| Public export disposition | `python governance/compat/check_public_export_disposition.py --base 7c7dfc52 --head HEAD --enforce` | PASS |

## Review Gate

Implementation may proceed only after:

- dispatch-quality gate passes for the T2C work order;
- markdown structural completeness passes for the changed dispatch artifacts;
- pre-dispatch and pre-implementation autorun gates pass on base `7c7dfc52`.

Worker handoff was not closure because commit mode was `WORKER_MUST_NOT_COMMIT`.
Reviewer/committer closure is recorded after focused review and must be backed
by a committed-range pre-closure gate on the closure commit.

## Acceptance Criteria

| Criterion | Evidence | Status |
| --- | --- | --- |
| Shared workflow chain allows valid session or valid service token | helper tests | PASS |
| Shared workflow chain denies missing/invalid auth with proof metadata | helper test | PASS |
| All five missing-proof routes emit `routeGovernanceProof` on success or denial | focused route tests | PASS |
| Route governance proof is registry/system-loop backed | helper tests, reference packet, GC-052 check | PASS |
| Existing validation behavior remains intact after auth passes | focused route tests | PASS |
| No public-sync, live proof, or production claim is made | diff and completion boundary | PASS |

## Fail Conditions

| Condition | Disposition |
| --- | --- |
| Route guard prints or returns raw service token | BLOCKS_CLOSURE |
| Existing route request parsing breaks after auth passes | BLOCKS_CLOSURE |
| Public-sync files are changed | BLOCKS_CLOSURE |
| Live/provider proof is claimed without release gate | BLOCKS_CLOSURE |
| `/api/execute/route.ts` is modified | BLOCKS_CLOSURE |

## Closure Checklist

| Item | Status |
| --- | --- |
| Shared workflow chain helper created and tested | PASS |
| Five missing-proof routes wired | PASS |
| System loop interlock registered | PASS |
| Focused tests run | PASS |
| Markdown and dispatch gates rerun | PASS |
| Completion packet filed | PASS |
| Public-sync explicitly not touched | PASS |
| `pre-closure` committed-range gate | PASS - reviewer closure range uses `dd49a3bf..HEAD` |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T2C_ROUTE_GOVERNANCE_PROOF_HARDENING_2026-06-04.md` | ERH-T2C `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_T2C_ROUTE_GOVERNANCE_PROOF_HARDENING_COMPLETION_2026-06-04.md` | completion review `CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ERH-T2C and E7 closed bounded | PASS |
| Registry JSON | `N/A with reason` | no GC-051 corpus registry state changed by ERH-T2C route proof closure | BLOCKED with reason |
| Registry Markdown | `N/A with reason` | no GC-051 corpus registry markdown state changed by ERH-T2C route proof closure | BLOCKED with reason |
| External evidence digest | `N/A with reason` | no external corpus/source digest consumed by ERH-T2C closure | N/A with reason |
| System loop interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | GC-052 connection `erh-route-ledger-to-route-governance-proof-workflow` | PASS |
| Session continuity | `AGENT_HANDOFF_V15_2026-05-29.md` | follow-up handoff sync commit records T2C closure | PASS |

## Return Conditions

Return to orchestrator if helper implementation would require `/api/execute`
edits, provider/live proof, public-sync changes, CI workflow rewrites, stronger
public claims, secrets/quota, or production/hosted readiness assertions.

## Operator Checkpoint

N/A with reason: operator authorized autonomous selection and execution of the
most grounded remaining ERH tranche. This work order does not cross public-sync,
live proof, commit/push, or secret-use boundaries.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Five ERH route surfaces had missing visible route governance proof | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | RUNTIME_LEARNING_CANDIDATE | implement shared route governance proof helper and focused route tests |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order targets private provenance runtime-source hardening.
Public-sync claim updates are forbidden until reviewed evidence exists and a
separate public-sync batch is authorized.

Next action: after reviewer closure, decide whether to summarize the narrowed
route gap publicly.

## Claim Boundary

This work order may claim local source and focused-test evidence for
session/service-token route governance proof. It must not claim live governance
behavior, provider behavior, hosted freshness, production readiness, public
readiness, or full CI hardening.

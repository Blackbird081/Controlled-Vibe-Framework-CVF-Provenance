# CVF GC-018 FPC-SCG-T8 Foundation System-Chain Acceptance Ledger Provenance Carrier Reconciliation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018_baseline

Date: 2026-06-27

Owner: Codex

rawMemoryReleased: false

## Purpose

Authorize and close a bounded FPC-SCG-T8 tranche that reconciles the T7
acceptance ledger's `materialCommit` rows with the current provenance rebuild
carrier before any later downstream lane uses the ledger as authority.

## Scope / Target / Owner Boundary

Allowed material scope:

- update `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` so required FPC-SCG closure rows cite the current provenance carrier;
- harden `governance/compat/check_fpc_system_chain_acceptance_ledger.py` so stale pre-rebuild carrier SHAs are rejected;
- add focused test coverage for stale carrier detection;
- update FPC guidance to record T8 closure;
- close this GC-018, work order, and completion review in the same material batch.

Forbidden scope:

- no system-loop registry mutation;
- no expected-chain manifest expansion;
- no runtime/MCP/CLI/IDE bridge implementation;
- no provider/live proof;
- no public-sync or push from this provenance workspace;
- no Policy_Local, Document Translator, Model Gateway, Sandbox Runtime, DICE runtime expansion, package activation, certification decision, or MPI-T6 runtime work;
- no generated active-session state mutation in the material commit.

## Decision / Baseline / Proposed Tranche

Decision: T8 is source-verified and closeable as a small
dispatcher/implementer/reviewer tranche because it corrects ledger provenance
carrier evidence only.

Baseline: current session state and the active handoff record that FPC-SCG-T2
through FPC-UAP-T2 material state is carried by `be253923`, and that older
unpublished material SHAs from the pre-rebuild branch are backup-history
references only.

Proposed tranche:
`FPC-SCG-T8 Foundation System-Chain Acceptance Ledger Provenance Carrier Reconciliation`.

## Source Authority

| Source | Path | Role |
|---|---|---|
| Active front door | `CVF_SESSION_MEMORY.md` | current material carrier and parked checkpoint |
| Active handoff | `AGENT_HANDOFF_V24_2026-06-27.md` | provenance rebuild carrier boundary |
| T7 ledger | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | acceptance ledger to reconcile |
| T7 checker | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | current machine gate to harden |
| T7 focused tests | `governance/compat/test_check_fpc_system_chain_acceptance_ledger.py` | focused regression surface |
| FPC guidance | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | next roadmap guidance |

No provider-specific memory file, external app source tree, or chat-only fact is
source authority for this tranche.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| current material carrier for FPC-SCG-T2 through FPC-UAP-T2 is `be253923` | `AGENT_HANDOFF_V24_2026-06-27.md` | `Provenance Push Debt Rebuild Sync - 2026-06-27` | `Current provenance material carrier` | active handoff | VALUE_SET | ACCEPT |
| pre-rebuild material SHAs must not be current remote ancestry evidence | `AGENT_HANDOFF_V24_2026-06-27.md` | `Provenance Push Debt Rebuild Sync - 2026-06-27` | `backup-history references only` | active handoff | LITERAL_INVARIANT | ACCEPT |
| front door records FPC-SCG-T2 through FPC-SCG-T7 as closed at `be253923` | `CVF_SESSION_MEMORY.md` | `Latest Closed Work` and `Parked Checkpoint` | `FPC-SCG-T2`; `FPC-SCG-T7`; `be253923` | active session front door | VALUE_SET | ACCEPT |
| T7 ledger has required closure rows with `materialCommit` | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | `acceptedClosureChain` | `materialCommit` | T7 ledger schema | EXISTS | ACCEPT |
| T7 checker validates required closure fields | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | `REQUIRED_CLOSURE_FIELDS` | `materialCommit` | T7 checker | VALUE_SET | ACCEPT |
| T8 checker hardening is a new local governance invariant | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | new edit in this tranche | `EXPECTED_MATERIAL_COMMITS` | T7 checker | DOC_ONLY_NEW | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json`; `governance/compat/check_fpc_system_chain_acceptance_ledger.py`; `governance/compat/test_check_fpc_system_chain_acceptance_ledger.py`; `AGENT_HANDOFF_V24_2026-06-27.md`; `CVF_SESSION_MEMORY.md` |
| Runtime behavior claimed | N/A_WITH_REASON: checker behavior is local governance validation only; no product runtime, provider route, CLI/MCP adapter, OCR call, retrieval behavior, or downstream adapter behavior is changed |
| Provider/live proof claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - T8 uses current active handoff/front-door rebuild evidence and current T7 ledger/checker surfaces |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | T7 ledger and checker | internal agents may verify bounded foundation acceptance against current provenance carrier evidence before downstream selection | ledger JSON, checker, focused tests, completion review | N/A with reason: internal provenance governance only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external CLI/MCP interface authorized | no external read/write/runtime authority is added | forbidden scope and public export disposition | deferred adapter owner; fresh source-verified authorization required | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

Chain map citation:
`docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: this tranche absorbs no new external knowledge item; the section is present because external-agent boundary terms appear in the artifact |
| Matching local-view guard | N/A with reason: no external knowledge intake item is promoted or absorbed |
| Owner surface | `docs/baselines/CVF_GC018_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_2026-06-27.md` |
| Disposition | N/A_WITH_REASON: no external input is used as source authority |
| Claim boundary | CVF-governed source files remain the only source authority for this tranche |

## Acceptance Criteria

| ID | Criterion | Disposition |
|---|---|---|
| AC1 | T7 ledger `materialCommit` rows use current provenance carrier evidence for FPC-SCG-T0 and FPC-SCG-T2 through FPC-SCG-T6 | PASS |
| AC2 | FPC-SCG-T1 remains anchored to pushed base `75fcad20` | PASS |
| AC3 | checker rejects stale pre-rebuild material carrier SHAs | PASS |
| AC4 | focused tests cover stale carrier detection | PASS |
| AC5 | runtime/provider/live/public/MPI-T6 lanes remain parked | PASS |

## Evidence / Verification

| Evidence item | Command or artifact | Required result |
|---|---|---|
| Ledger checker | `python governance/compat/check_fpc_system_chain_acceptance_ledger.py --enforce` | PASS |
| Focused tests | `python -m pytest governance/compat/test_check_fpc_system_chain_acceptance_ledger.py -q` | PASS |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 1f229fc6 --head HEAD --enforce` | PASS |
| Pre-implementation autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 1f229fc6 --head HEAD --serial` | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_FOR_CODEX_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Ledger JSON | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | `materialCommit` carrier rows reconciled | PASS |
| Registry JSON | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | acceptance-ledger registry carrier rows reconciled | PASS |
| Registry Markdown | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | T8 reconciliation recorded in guidance | PASS |
| Ledger checker | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | `EXPECTED_MATERIAL_COMMITS` | PASS |
| Focused tests | `governance/compat/test_check_fpc_system_chain_acceptance_ledger.py` | stale carrier fixture | PASS |
| Roadmap state | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | T8 recorded as completed bounded reconciliation | PASS |
| External evidence digest | N/A with reason: no external knowledge input or external evidence digest is consumed by T8 | no external source promoted | N/A with reason |
| System loop interlock | `python governance/compat/check_system_loop_interlock.py --base 1f229fc6 --head HEAD --enforce` | PASS required before commit | PASS |
| Session continuity | reviewer-owned post-material sync | pending separate session-sync after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| FPC-SCG-T8-Q1 | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | `acceptedClosureChain[?trancheId=FPC-SCG-T2].materialCommit` | `be253923` | `be253923` | PASS |
| FPC-SCG-T8-Q2 | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | `acceptedClosureChain[?trancheId=FPC-SCG-T1].materialCommit` | `75fcad20` | `75fcad20` | PASS |
| FPC-SCG-T8-Q3 | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | `EXPECTED_MATERIAL_COMMITS` | stale carrier rejection | checker hardened | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance acceptance-ledger reconciliation. Public-sync is not
authorized.

## Claim Boundary

This baseline closes only a bounded provenance-carrier reconciliation for the
T7 acceptance ledger and local governance checker. It does not certify
production readiness, public readiness, provider behavior, runtime execution,
downstream adapter behavior, or MPI-T6 runtime value.

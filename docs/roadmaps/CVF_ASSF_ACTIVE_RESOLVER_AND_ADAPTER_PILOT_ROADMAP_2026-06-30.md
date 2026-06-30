# CVF ASSF ACTIVE Resolver And Adapter Pilot Roadmap

Memory class: FULL_RECORD

Status: ACTIVE_ROADMAP

docType: roadmap

Date: 2026-06-30

Batch ID: ASCP-R0

## Purpose

Open the next ASSF skill control-plane lane after truth packets and usage
receipts: a bounded ACTIVE resolver, then a CLI/MCP adapter projection, then
later package activation work. The roadmap keeps package selection, package body
use, external adapter posture, and provider behavior as separate control points.

## Authorization

Operator approved the next roadmap direction as ACTIVE resolver, CLI/MCP
adapter, and package activation, with remaining package runtime conversion
deferred. Operator also authorized live API-key use when a live proof is needed.

This roadmap does not itself claim live provider behavior. ASCP-T1 uses local
repo metadata, truth packets, and runtime loader logic only.

## Current Baseline

| Surface | Current fact | Evidence |
|---|---|---|
| ASSF generated index | 32 package metadata records | `docs/reference/agent_system_skills/generated/skill-index.json` |
| Runtime-eligible packages | 6 packages resolve as runtime eligible when the loader is run with `--max-results 100` | `python governance/compat/run_assf_runtime_package_loader.py --json --max-results 100` |
| Truth packets | 6 approved STRICT runtime-eligible truth packets | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Usage receipts | emitted only when eligible package bodies are explicitly requested through the runtime loader | `governance/compat/run_assf_runtime_package_loader.py` |
| External CLI/MCP adapter | not implemented | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` |

## Non-Goals

- No remaining-package runtime conversion in ASCP-T1.
- No package lifecycle source mutation to `ACTIVE`.
- No automatic package invocation.
- No package instruction body read.
- No external CLI/MCP adapter implementation.
- No provider call or live governance proof.
- No public-sync or production-readiness claim.

## Design Control Gate

| Gate | Disposition |
|---|---|
| Resolver before adapter | PASS - ASCP-T1 creates an internal decision helper only |
| Readiness before body use | PASS - skill usage receipts remain owned by the runtime loader |
| Truth packet before readiness | PASS - resolver requires approved STRICT runtime-eligible truth records |
| External adapter separation | PASS - `EXTERNAL_AGENT_CLI_MCP` is denied in ASCP-T1 |
| Remaining conversion parked | PASS - ASCP-T5 is value-parked |

## Scope

Included:

- ASCP-T1 ACTIVE resolver pilot for the six current runtime-eligible packages.
- ASCP-T2 activation policy hardening for decision receipt acceptance and
  operator-facing activation language.
- ASCP-T3 CLI/MCP adapter projection after resolver output is stable.
- ASCP-T4 package activation lifecycle decision after adapter and resolver
  boundaries are proven.

Excluded:

- converting the remaining packages into runtime packages;
- package lifecycle mutation to `ACTIVE` without a later source-verified
  promotion work order;
- automatic package invocation;
- external adapter implementation in ASCP-T1;
- provider or live API calls unless a later tranche makes a live governance
  claim.

## Work Plan

| Tranche | Objective | Status |
|---|---|---|
| ASCP-T1 | Implement read-only ACTIVE resolver decision layer over generated ASSF metadata, truth index, and loader eligibility | CLOSED_PASS_BOUNDED |
| ASCP-T2 | Define activation policy semantics: selected, ready, body-read requested, and used-with-receipt | READY_AFTER_T1 |
| ASCP-T3 | Implement CLI/MCP adapter projection using resolver output and external readout allowlist | HOLD_AFTER_T2 |
| ASCP-T4 | Decide whether any package lifecycle source should move to `ACTIVE` | HOLD_AFTER_T3 |
| ASCP-T5 | Reopen remaining package runtime conversion only after T1-T4 evidence shows value | VALUE_PARKED |

## ASCP-T1 Result

ASCP-T1 added `governance/compat/run_assf_active_resolver.py` and
`governance/compat/test_run_assf_active_resolver.py`.

The resolver:

- reads generated ASSF metadata;
- reuses the runtime loader eligibility gate without requesting instruction
  bodies;
- reads the generated skill truth index;
- returns `ACTIVATION_READY` only when loader eligibility and truth packet
  requirements both pass;
- returns a deterministic resolver decision receipt;
- denies `EXTERNAL_AGENT_CLI_MCP` until a separate adapter tranche exists.

Focused verification observed 6 `ACTIVATION_READY` packages and 32 total
generated-index candidates.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF contract separates package lifecycle states and adapter posture | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields; Provider Adapter Boundary | `ACTIVE`; `adapterContract` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Runtime loader gates body reads by certification, UAT, internal disposition, and package root | `governance/compat/run_assf_runtime_package_loader.py` | `_runtime_ineligibility_reasons`; `build_runtime_package_packet` | `include_instruction_bodies`; `runtimeEligible` | runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Truth packets are canonical for evidence, obligations, verification results, and truth receipts | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | Source Authority Boundary | `truth/packets/*.json` | skill truth packet standard | LITERAL_INVARIANT | ACCEPT |
| Usage receipts are emitted by the loader only for explicit eligible package body reads | `docs/reference/agent_system_skills/CVF_SKILL_USAGE_RECEIPT_TRACE_STANDARD.md` | Purpose; Claim Boundary | `skillUsageReceipts` | skill usage receipt standard | LITERAL_INVARIANT | ACCEPT |
| External CLI/MCP adapter implementation remains deferred | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | Adapter Admission Boundary | `EXTERNAL_AGENT_CLI_MCP` | external readout boundary contract | LITERAL_INVARIANT | ACCEPT |
| ACTIVE resolver helper is new in ASCP-T1 | `governance/compat/run_assf_active_resolver.py` | ASCP-T1 new file | `build_active_resolver_packet` | active resolver helper | DOC_ONLY_NEW | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`,
lifecyclePhase=`implementation`, surfaceSelector=`docs/reference/agent_system_skills`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: the ADIF resolver was called through Python import because the
module has no CLI `main()` output path.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASCP-T1 active resolver helper | may receive activation-readiness decisions only; no body read or authority grant | focused tests and resolver smoke | no external adapter | `IMPLEMENTED_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter projection | denied by ASCP-T1 until a separate adapter implementation tranche exists | external readout boundary contract | deferred adapter owner | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | local CVF skill-control roadmap -> no external knowledge promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this roadmap and ASCP-T1 artifacts |
| Disposition | REJECT_DIRECT for external intake promotion; repo-local sources only |
| Claim boundary | no external artifact, provider output, or provider-local memory is promoted as CVF authority |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASSF package contract, truth packet standard, usage receipt standard, runtime loader, external adapter boundary contract |
| Runtime behavior claimed | read-only active resolver decision helper only |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - source evidence supports local readiness decisions, not adapter or lifecycle mutation |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | ASCP-T1 creates a read-only active resolver helper | helper file exists |
| AC2 | Resolver returns ready only when loader eligibility and truth checks pass | focused tests |
| AC3 | Resolver does not emit skill usage receipts | focused tests |
| AC4 | External CLI/MCP consumer remains denied | focused tests |
| AC5 | Real repo smoke observes 6 ready packages | resolver smoke |

## Verification / Evidence

| Evidence | Observed result |
|---|---|
| `python -m unittest governance.compat.test_run_assf_active_resolver` | PASS, 7 tests |
| `python governance/compat/run_assf_active_resolver.py --json --max-results 100` | 32 total candidates, 6 `ACTIVATION_READY` |
| Live provider proof | NOT_RUN_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: ASCP-T1 resolver did not consume package instruction output as work evidence |
| Package root | N/A with reason: no package body was requested |
| Invocation context | ASCP-T1 resolver smoke used metadata and truth index only |
| Receipt evidence | N/A with reason: no `skillUsageReceipt` is emitted until the runtime loader explicitly reads an eligible body |
| Output consumed by CVF | resolver decision receipt metadata only |
| Truth packet or source path | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Authority boundary | resolver decision receipt does not grant authority, activate a package, or bypass work-order scope |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | local Python helper and repo metadata only |
| Output consumed by CVF | N/A with reason: no provider skill output consumed |
| CVF source-of-truth promotion path | N/A with reason: no provider skill output promoted |
| Evidence artifact | this roadmap and ASCP-T1 completion artifacts |
| Authority boundary | provider-owned skill output is not CVF canonical authority |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap references internal ASSF provenance and private
skill-control surfaces. Public-safe export requires separate public-sync
authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T1_ACTIVE_RESOLVER_PILOT_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASCP_T1_ACTIVE_RESOLVER_PILOT_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | this roadmap | `Status: ACTIVE_ROADMAP` | PASS |
| Registry JSON | N/A with reason: no registry mutation authorized or performed | N/A with reason | PASS |
| Registry Markdown | N/A with reason: no registry markdown mutation | N/A with reason | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no provider route, adapter, or package execution changed | N/A with reason | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | active resolver tests | PASS | PASS |
| Runtime smoke | active resolver smoke | PASS | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Claim Boundary

This roadmap opens and records a bounded ASSF skill control-plane path. ASCP-T1
implements local activation-readiness decisions only. It does not convert
remaining packages, mutate lifecycle sources, read package instruction bodies,
call providers, expose CLI/MCP adapter behavior, public-sync, or claim
production readiness.

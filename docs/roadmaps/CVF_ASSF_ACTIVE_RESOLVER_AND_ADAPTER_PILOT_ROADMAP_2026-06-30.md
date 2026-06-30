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

This roadmap now records one ASCP-T5 live provider proof after explicit
operator authorization. ASCP-T1 through ASCP-T4 use local repo metadata, truth
packets, resolver logic, policy classification, external projection filtering,
runtime loader receipt semantics, and lifecycle source-state decision output
only.

## Current Baseline

| Surface | Current fact | Evidence |
|---|---|---|
| ASSF generated index | 32 package metadata records | `docs/reference/agent_system_skills/generated/skill-index.json` |
| Runtime-eligible packages | 6 packages resolve as runtime eligible when the loader is run with `--max-results 100` | `python governance/compat/run_assf_runtime_package_loader.py --json --max-results 100` |
| Truth packets | 6 approved STRICT runtime-eligible truth packets | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Usage receipts | emitted only when eligible package bodies are explicitly requested through the runtime loader | `governance/compat/run_assf_runtime_package_loader.py` |
| External CLI/MCP adapter | bounded metadata/policy projection implemented; external package execution adapter not implemented | `governance/compat/run_assf_cli_mcp_adapter_projection.py` |
| Internal package use-proof adapter | bounded receipt-backed package use and one live provider proof implemented | `governance/compat/run_assf_package_use_proof_adapter.py` |

## Non-Goals

- No remaining-package runtime conversion in ASCP-T1 or ASCP-T2.
- No package lifecycle source mutation to `ACTIVE`.
- No automatic package invocation.
- No package instruction body read before ASCP-T5.
- No external package execution adapter in ASCP-T3 or ASCP-T5.
- No provider call or live governance proof before ASCP-T5.
- No public-sync or production-readiness claim.

## Design Control Gate

| Gate | Disposition |
|---|---|
| Resolver before adapter | PASS - ASCP-T1 creates an internal decision helper only |
| Readiness before body use | PASS - skill usage receipts remain owned by the runtime loader |
| Truth packet before readiness | PASS - resolver requires approved STRICT runtime-eligible truth records |
| External adapter separation | PASS - ASCP-T3 projects metadata/policy only and denies package execution |
| Remaining conversion parked | PASS - ASCP-T5 implements use-proof only; remaining conversion stays out of scope |

## Scope

Included:

- ASCP-T1 ACTIVE resolver pilot for the six current runtime-eligible packages.
- ASCP-T2 activation policy hardening for selected, ready, body-read requested,
  and used-with-receipt semantics.
- ASCP-T3 CLI/MCP adapter projection after resolver output is stable.
- ASCP-T4 package activation lifecycle decision after adapter and resolver
  boundaries are proven.
- ASCP-T5 internal package execution/use-proof adapter after operator reopened
  the lane before any ACTIVE lifecycle promotion.

Excluded:

- converting the remaining packages into runtime packages;
- package lifecycle mutation to `ACTIVE` without a later source-verified
  promotion work order;
- automatic package invocation;
- external package execution adapter implementation in ASCP-T3;
- provider or live API calls outside the ASCP-T5 bounded use-proof command.

## Work Plan

| Tranche | Objective | Status |
|---|---|---|
| ASCP-T1 | Implement read-only ACTIVE resolver decision layer over generated ASSF metadata, truth index, and loader eligibility | CLOSED_PASS_BOUNDED |
| ASCP-T2 | Define activation policy semantics: selected, ready, body-read requested, and used-with-receipt | CLOSED_PASS_BOUNDED |
| ASCP-T3 | Implement CLI/MCP adapter projection using resolver output and external readout allowlist | CLOSED_PASS_BOUNDED |
| ASCP-T4 | Decide whether any package lifecycle source should move to `ACTIVE` | CLOSED_PASS_BOUNDED |
| ASCP-T5 | Implement package execution/use-proof adapter before any ACTIVE lifecycle promotion | CLOSED_PASS_BOUNDED |

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

## ASCP-T2 Result

ASCP-T2 added:

- `docs/reference/agent_system_skills/CVF_ASSF_ACTIVATION_POLICY_SEMANTICS_STANDARD.md`;
- `governance/compat/run_assf_activation_policy_resolver.py`;
- `governance/compat/test_run_assf_activation_policy_resolver.py`.

The policy layer:

- classifies selected package rows separately from activation readiness;
- treats `ACTIVATION_READY` as permission to request the runtime loader, not as
  package body loading;
- classifies `BODY_READ_REQUESTED` without opening package bodies;
- requires a matching `CVF_ASSF_SKILL_USAGE_RECEIPT` before
  `USED_WITH_RECEIPT`;
- denies consumed-output claims without matching receipts;
- keeps external CLI/MCP adapter behavior deferred to ASCP-T3.

Focused verification passed 7 activation-policy unit tests and local smokes
for `ACTIVATION_READY` and `BODY_READ_REQUESTED` on
`cvf-engineering-spec-driven-development`.

## ASCP-T3 Result

ASCP-T3 added:

- `docs/reference/agent_system_skills/CVF_ASSF_CLI_MCP_ADAPTER_PROJECTION_STANDARD.md`;
- `governance/compat/run_assf_cli_mcp_adapter_projection.py`;
- `governance/compat/test_run_assf_cli_mcp_adapter_projection.py`.

The projection layer:

- targets `EXTERNAL_AGENT_CLI_MCP`;
- uses the external metadata readout allowlist;
- merges activation policy state from the ASCP-T2 resolver;
- emits `IMPLEMENTED_BOUNDED_PROJECTION`, not package execution authority;
- denies external package body reads with
  `DENIED_EXTERNAL_BODY_READ_NOT_IMPLEMENTED`;
- denies external output use with
  `DENIED_EXTERNAL_OUTPUT_USE_NOT_IMPLEMENTED`;
- does not emit package bodies, loader commands, truth objects, resolver
  receipts, policy receipts, matched usage receipt IDs, or skill usage
  receipts.

Focused verification passed 6 projection unit tests and a local projection
smoke on `cvf-engineering-spec-driven-development`.

## ASCP-T4 Result

ASCP-T4 added:

- `governance/compat/run_assf_package_lifecycle_decision.py`;
- `governance/compat/test_run_assf_package_lifecycle_decision.py`.

The lifecycle decision helper:

- summarizes runtime-loader eligibility, active-resolver readiness, CLI/MCP
  projection readiness, and current active source records;
- emits `HOLD_NO_ACTIVE_SOURCE_MUTATION`;
- emits `NO_SOURCE_MUTATIONS_AUTHORIZED`;
- emits no recommended source mutations;
- does not open package instruction bodies;
- does not mutate registry entries, generated indexes, truth packets, package
  roots, provider routes, execution adapters, session state, or public-sync.

Focused verification passed 5 lifecycle decision unit tests. Local decision
smoke observed 32 total candidates, 6 runtime eligible packages, 6 activation
ready packages, 6 external projection ready packages, 0 active source records,
and the hold decision.

## ASCP-T5 Result

ASCP-T5 added:

- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_USE_PROOF_ADAPTER_STANDARD.md`;
- `governance/compat/run_assf_package_use_proof_adapter.py`;
- `governance/compat/test_run_assf_package_use_proof_adapter.py`.

The use-proof adapter:

- loads one eligible package through the runtime package loader;
- captures `CVF_ASSF_SKILL_USAGE_RECEIPT`;
- confirms activation policy `USED_WITH_RECEIPT`;
- optionally calls a live provider with a bounded task prompt;
- emits `CVF_ASSF_PACKAGE_USE_PROOF_RECEIPT` after provider success;
- emits secret-safe live diagnostics on missing key or provider failure;
- keeps `lifecycleMutation=false`, `activePromotionAuthorized=false`, and
  `sourceMutations=[]`.

Focused verification passed 5 use-proof adapter unit tests and 20 focused
loader/policy/use-proof regression tests. The live proof on
`cvf-engineering-spec-driven-development` returned `LIVE_PROVIDER_USE_PROOF_PASS`,
HTTP 200, and use-proof receipt
`sha256:f67bd3331f81e088c2f75f7287db0fce60508abbc89cd7099481e5e86aeaa7dc`.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF contract separates package lifecycle states and adapter posture | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields; Provider Adapter Boundary | `ACTIVE`; `adapterContract` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Runtime loader gates body reads by certification, UAT, internal disposition, and package root | `governance/compat/run_assf_runtime_package_loader.py` | `_runtime_ineligibility_reasons`; `build_runtime_package_packet` | `include_instruction_bodies`; `runtimeEligible` | runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Truth packets are canonical for evidence, obligations, verification results, and truth receipts | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | Source Authority Boundary | `truth/packets/*.json` | skill truth packet standard | LITERAL_INVARIANT | ACCEPT |
| Usage receipts are emitted by the loader only for explicit eligible package body reads | `docs/reference/agent_system_skills/CVF_SKILL_USAGE_RECEIPT_TRACE_STANDARD.md` | Purpose; Claim Boundary | `skillUsageReceipts` | skill usage receipt standard | LITERAL_INVARIANT | ACCEPT |
| External CLI/MCP adapter implementation remains deferred | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | Adapter Admission Boundary | `EXTERNAL_AGENT_CLI_MCP` | external readout boundary contract | LITERAL_INVARIANT | ACCEPT |
| ACTIVE resolver helper is new in ASCP-T1 | `governance/compat/run_assf_active_resolver.py` | ASCP-T1 new file | `build_active_resolver_packet` | active resolver helper | DOC_ONLY_NEW | ACCEPT |
| Activation policy helper is new in ASCP-T2 | `governance/compat/run_assf_activation_policy_resolver.py` | ASCP-T2 new file | `build_activation_policy_packet` | activation policy resolver | DOC_ONLY_NEW | ACCEPT |
| CLI/MCP projection helper is new in ASCP-T3 | `governance/compat/run_assf_cli_mcp_adapter_projection.py` | ASCP-T3 new file | `build_cli_mcp_adapter_projection` | CLI/MCP adapter projection helper | DOC_ONLY_NEW | ACCEPT |
| Package lifecycle decision helper is new in ASCP-T4 | `governance/compat/run_assf_package_lifecycle_decision.py` | ASCP-T4 new file | `build_package_lifecycle_decision` | package lifecycle decision helper | DOC_ONLY_NEW | ACCEPT |
| Package use-proof adapter is new in ASCP-T5 | `governance/compat/run_assf_package_use_proof_adapter.py` | ASCP-T5 new file | `build_package_use_proof_packet` | package use-proof adapter | DOC_ONLY_NEW | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`,
lifecyclePhase=`implementation`, surfaceSelector=`docs/reference/agent_system_skills`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure command:

```text
python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase implementation --surface-selector docs/reference/agent_system_skills --risk-ceiling HIGH --max-results 20 --json
```

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASCP-T1 active resolver helper | may receive activation-readiness decisions only; no body read or authority grant | focused tests and resolver smoke | no external adapter | `IMPLEMENTED_BOUNDED` |
| `INTERNAL_AGENT` | ASCP-T2 activation policy helper | may receive selected/ready/body-read/use classification only; no body read or authority grant | focused tests and policy smoke | no external adapter | `IMPLEMENTED_BOUNDED` |
| `INTERNAL_AGENT` | ASCP-T5 package use-proof adapter | may run one explicit receipt-backed package use proof | ASCP-T5 tests and live proof | no lifecycle mutation | `IMPLEMENTED_BOUNDED_USE_PROOF_ADAPTER` |
| `EXTERNAL_AGENT_CLI_MCP` | ASCP-T3 projection helper | may inspect allowlisted metadata and policy state only; no body read or output use | ASCP-T3 tests and smoke | execution adapter remains deferred | `IMPLEMENTED_BOUNDED_PROJECTION` |
| `EXTERNAL_AGENT_CLI_MCP` | package execution adapter | no external package body read or output use authorized | N/A with reason: external execution adapter not implemented | separate MCP runtime work order required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | local CVF skill-control roadmap -> no external knowledge promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this roadmap and ASCP-T1 through ASCP-T5 artifacts |
| Disposition | REJECT_DIRECT for external intake promotion; repo-local sources and live proof hashes only |
| Claim boundary | provider model output is proof evidence only and is not promoted as CVF canonical authority |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASSF package contract, truth packet standard, usage receipt standard, use-proof adapter standard, runtime loader, activation policy resolver, CLI/MCP projection helper, lifecycle decision helper, provider env loader, provider capability registry |
| Runtime behavior claimed | read-only active resolver, activation policy classifier, external metadata/policy projection, lifecycle source-state decision, and bounded package use-proof adapter |
| Live/provider proof claimed | YES - ASCP-T5 live provider proof returned HTTP 200 and use-proof receipt |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - source evidence supports bounded use-proof, not lifecycle mutation or external MCP execution |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | ASCP-T1 creates a read-only active resolver helper | helper file exists |
| AC2 | Resolver returns ready only when loader eligibility and truth checks pass | focused tests |
| AC3 | Resolver does not emit skill usage receipts | focused tests |
| AC4 | External CLI/MCP consumer remains denied | focused tests |
| AC5 | Real repo smoke observes 6 ready packages | resolver smoke |
| AC6 | Policy helper classifies selected, ready, body-read requested, and used-with-receipt | focused tests |
| AC7 | Policy helper denies consumed-output claims without matching receipts | focused tests |
| AC8 | ASCP-T3 becomes ready only after ASCP-T2 closure | roadmap Work Plan |
| AC9 | ASCP-T3 projection exposes metadata/policy state while denying external body reads and output use | focused tests and projection smoke |
| AC10 | ASCP-T4 becomes ready only after ASCP-T3 closure | roadmap Work Plan |
| AC11 | ASCP-T4 decides no lifecycle source moves to `ACTIVE` in this tranche | lifecycle decision helper, tests, and smoke |
| AC12 | ASCP-T5 implements bounded package use-proof after operator reopen | use-proof helper, tests, and live proof |
| AC13 | ASCP-T5 still blocks ACTIVE promotion and remaining package conversion | claim boundary and changed set review |

## Verification / Evidence

| Evidence | Observed result |
|---|---|
| `python -m unittest governance.compat.test_run_assf_active_resolver` | PASS, 7 tests |
| `python governance/compat/run_assf_active_resolver.py --json --max-results 100` | 32 total candidates, 6 `ACTIVATION_READY` |
| `python -m unittest governance.compat.test_run_assf_activation_policy_resolver` | PASS, 7 tests |
| `python governance/compat/run_assf_activation_policy_resolver.py --skill-id cvf-engineering-spec-driven-development --json` | returned `ACTIVATION_READY` |
| `python governance/compat/run_assf_activation_policy_resolver.py --skill-id cvf-engineering-spec-driven-development --body-read-requested` | returned `BODY_READ_REQUESTED` |
| `python -m unittest governance.compat.test_run_assf_cli_mcp_adapter_projection` | PASS, 6 tests |
| `python governance/compat/run_assf_cli_mcp_adapter_projection.py --skill-id cvf-engineering-spec-driven-development --json` | returned `ACTIVATION_READY` with external body/read output denied |
| `python -m unittest governance.compat.test_run_assf_package_lifecycle_decision` | PASS, 5 tests |
| `python governance/compat/run_assf_package_lifecycle_decision.py --json` | returned 32 total candidates, 6 runtime eligible, 6 activation ready, 6 external projection ready, 0 active source records, and `HOLD_NO_ACTIVE_SOURCE_MUTATION` |
| `python -m unittest governance.compat.test_run_assf_package_use_proof_adapter` | PASS, 5 tests |
| `python -m unittest governance.compat.test_run_assf_runtime_package_loader governance.compat.test_run_assf_activation_policy_resolver governance.compat.test_run_assf_package_use_proof_adapter` | PASS, 20 tests |
| `python governance/compat/run_assf_package_use_proof_adapter.py --skill-id cvf-engineering-spec-driven-development --json` | returned `DRY_RUN_READY_FOR_LIVE_PROVIDER_USE_PROOF` and `USED_WITH_RECEIPT` |
| `python governance/compat/run_assf_package_use_proof_adapter.py --skill-id cvf-engineering-spec-driven-development --live --json --receipt-out .cvf/runtime/assf-use-proof/ascp-t5-live-proof.json` | returned `LIVE_PROVIDER_USE_PROOF_PASS`, HTTP 200, latency 2162 ms, and use-proof receipt `sha256:f67bd3331f81e088c2f75f7287db0fce60508abbc89cd7099481e5e86aeaa7dc` |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | USED_WITH_RECEIPT |
| CVF skill id | `cvf-engineering-spec-driven-development` |
| Package root | `docs/reference/agent_system_skills/packages/cvf-engineering-spec-driven-development/SKILL.md` |
| Invocation context | ASCP-T5 live use-proof adapter smoke |
| Receipt evidence | `sha256:aa4e26d13ccd75475431e434ef1bd304f20d3b72d77f95a4726fdf6038f2455f` |
| Output consumed by CVF | package-use proof receipt and live output hash only |
| Truth packet or source path | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Authority boundary | skill usage receipt does not grant authority, activate package lifecycle state, or bypass work-order scope |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | ASCP-T5 model-completion proof; provider skill surface: none |
| Output consumed by CVF | N/A with reason: no provider skill output consumed |
| CVF source-of-truth promotion path | N/A with reason: no provider skill output promoted |
| Evidence artifact | this roadmap and ASCP-T1 through ASCP-T5 completion artifacts |
| Authority boundary | provider model output is proof evidence only; provider skill surface: none; not CVF canonical authority |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap references internal ASSF provenance and private
skill-control surfaces. Public-safe export requires separate public-sync
authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T5_PACKAGE_EXECUTION_USE_PROOF_ADAPTER_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASCP_T5_PACKAGE_EXECUTION_USE_PROOF_ADAPTER_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | this roadmap | `Status: ACTIVE_ROADMAP` | PASS |
| Registry JSON | N/A with reason: no registry mutation authorized or performed | N/A with reason | PASS |
| Registry Markdown | N/A with reason: no registry markdown mutation | N/A with reason | PASS |
| External evidence digest | `.cvf/runtime/assf-use-proof/ascp-t5-live-proof.json` | `sha256:6fb08064c35dbfcdb1a7dbc3657edd345d57bbe78e186ca9267a60576d932c4a` | PASS |
| System loop interlock | no lifecycle mutation or external MCP execution adapter | output fields `lifecycleMutation=false`; `sourceMutations=[]` | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | active resolver, activation policy, projection, lifecycle decision, and use-proof tests | PASS | PASS |
| Runtime smoke | active resolver, activation policy, projection, lifecycle decision, dry-run use-proof, and live use-proof smokes | PASS | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | HTTP 200 and use-proof receipt | PASS |

## Claim Boundary

This roadmap opens and records a bounded ASSF skill control-plane path. ASCP-T1
implements local activation-readiness decisions, ASCP-T2 implements local
activation policy classification, ASCP-T3 implements bounded external
metadata/policy projection, ASCP-T4 decides no lifecycle source moves to
`ACTIVE`, and ASCP-T5 implements bounded internal package use-proof. It does
not convert remaining packages, mutate lifecycle sources, implement external
MCP package execution, public-sync, or claim production readiness.

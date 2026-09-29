# CVF GC-018 Baseline - Form-Mode Elicitation Sensitive-Data Guard Implementation

Memory class: governed-dispatch-baseline

Status: REVIEWER_ACCEPTED_DISPATCH_READY

Batch ID: MCP-KAR-T4

Dispatch base head: 583c0911a8049e708bc1a75648ea6eeb907fb167

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: parent reviewer/closer

Worker target: implementation worker subagent

## Purpose

Implement the T3-approved, pure local MCP form-mode sensitive-data admission
invariant as `MCP-PR-011`. Preserve the existing composite profile while
failing closed before collection, without opening any runtime or external lane.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MCP-KAR-T4 --title "Form-Mode Elicitation Sensitive-Data Guard Implementation" --date 2026-08-24 --base 583c0911a8049e708bc1a75648ea6eeb907fb167 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MCP-KAR-T3 reviewer-accepted closure c62f926f2; operator authorized autonomous valuable absorption on 2026-08-24" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker and MCP/CLI boundary stubs |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact T3 authority, four-path implementation manifest, MCP-PR-011 behavior, verification, and held boundaries |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| docOnlyNewFields | `elicitationMode`; `requestedDataCategories`; `MCP-PR-011`; `UNSAFE_ELICITATION_REQUEST` |
| claimBoundary | dispatch authority only; no implementation has occurred |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| operator selection | autonomous valuable absorption instruction, 2026-08-24 | operator may select later tranche within CVF rules | RELEASED |
| T3 owner/value decision | reviewer-accepted closure `c62f926f27b7c98390e937fc0ca8063af9040611`; return locks exact four-path manifest | `PROCEED_ELICITATION_GUARD` and exact owner required | RELEASED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`MCP form-mode elicitation sensitive-data guard implementation dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "MCP form-mode elicitation sensitive-data guard implementation dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: resolver returned none |
| Dispatch impact | canonical guards remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | dispatch status, Source Verification columns, fulfillment manifest, worker-return profile, operation trace, Delta boundary, MCP adapter boundary, and public disposition |
| gateRunPurpose | confirm authored dispatch completeness and record evidence before worker handoff; gates are not first-discovery tools |
| claimBoundary | paired documentation packet only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T3 authorizes bounded guard candidate | GOVERNED_REVIEW | `docs/reviews/CVF_MCP_KAR_T3_FORM_MODE_ELICITATION_SENSITIVE_DATA_OWNER_VALUE_DECISION_WORKER_RETURN_2026-08-24.md` | Decision / Disposition and reviewer decision | `PROCEED_ELICITATION_GUARD`; exact four-path later manifest | T3 reviewer-accepted closure `c62f926f2` | ACCEPT |
| normative owner is existing MCP profile | GOVERNED_REFERENCE | `docs/reference/mcp_gateway/CVF_MCP_NORMATIVE_INVARIANT_PROFILE.md` | Scope / Applies-To lines 18-26; Protocol Contract lines 39-55 | implementation owner path and MCP-PR vocabulary | MCP gateway reference | ACCEPT |
| source seam is pure aggregate evaluator | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.protocol.invariant.profile.ts` | lines 77-111 | `MCPProtocolInvariantProfileInput`; `MCPProtocolInvariantProfile.evaluate` | execution-plane foundation | ACCEPT |
| focused test preserves composite profile | TEST_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mcp.protocol.invariant.profile.test.ts` | `validInput` and `MCPProtocolInvariantProfile` suite | current accepted composite and negative oracle | execution-plane test owner | ACCEPT |
| export owner exists | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | MCP protocol profile export | `mcp.protocol.invariant.profile` export | execution-plane foundation barrel | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| proposed dispatch paths | both absent at dispatch start | PASS |
| rule collision | T3 confirmed current rules stop at `MCP-PR-010` and no elicitation admission rule exists | PASS_WITH_GAP_OBSERVED |
| owner collision | T3 selected the existing profile composition seam, not a new parallel owner | PASS |
| decision-code collision | worker must source-search before choosing `UNSAFE_ELICITATION_REQUEST` and report any collision | PASS_REQUIRES_FRESH_WORKER_CHECK |

## Decision / Baseline

The worker may add exactly one pure rule, `MCP-PR-011`, to the existing profile.
Its input vocabulary must be closed and typed. Form mode rejects password,
API-key, access-token, and payment-credential categories. Unknown or malformed
categories fail closed. URL mode permits those categories because collection
occurs outside the form surface. Ordinary contact/profile form categories are
accepted. The evaluator receives category metadata only and must never receive,
inspect, store, log, or return raw secret values. The local decision code is
`UNSAFE_ELICITATION_REQUEST` unless a fresh source collision requires an
equally bounded source-verified local choice.

## Scope / Owner Boundary

Allowed implementation paths are exactly the normative reference, invariant
source, focused test, and existing barrel export named below. The only other
worker write is one uncommitted worker return. Package manifests, runtime
bridges, transports, external fixtures, sessions, providers, live systems,
public sync, deployment, and production are forbidden.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | MCP normative profile and pure execution-plane evaluator | deterministic category admission only | source plus focused tests | N/A with reason: direct local contract composition | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | possible future MCP caller | no transport, collection, invocation, receipt, or mutation authority | future adapter requires separate work order | deferred runtime/adapter | `DEFERRED_WITH_REASON` |

## MCP/CLI Adapter Boundary

| Field | Value |
| --- | --- |
| Adapter scope | none; pure local typed invariant only |
| No-runtime-overclaim | This dispatch does not authorize an MCP client/server, CLI, wrapper, bridge, transport, form collector, or external fixture import. |

## Risk / Corrective Action

Primary risk is either permissive unknown-category handling or accidental raw
secret-value flow. Correct by closed vocabulary, explicit malformed/unknown
negative tests, category-only input types, and inspection proving no value
field or raw secret appears. Preserve all ten prior rules and the accepted
composite test.

## Evidence / Verification

- focused tests must cover four sensitive form categories, unknown and malformed
  categories, sensitive URL mode, ordinary contact/profile form mode, and the
  unchanged composite profile;
- run TypeScript checking and the focused test owner using repository scripts;
- prove exact changed set and no raw secret values;
- run pre-implementation and worker-return fast governance gates;
- provider/network/live call count must remain zero.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | implement CVF-native invariant from the accepted T3 decision; no new intake |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | exact four-path MCP invariant profile manifest |
| Disposition | bounded native implementation; no direct external import |
| Claim boundary | protocol fact informs local contract only |

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: this tranche uses the accepted T3 targeted decision
and exact manifest; it opens no source family, scan, or new corpus claim.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - targeted implementation from an
  accepted source/owner decision; no inventory or all-files-read claim.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: no new source enumeration, direct import,
manifest, ledger, package, or runtime work occurs.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch; no public-sync authority.

## Claim Boundary

This baseline authorizes only a pure repository-local contract implementation
within the exact manifest. It does not claim MCP interoperability, runtime
enforcement, secret collection or redaction, package readiness, provider/live
behavior, public export, deployment, production readiness, or authority beyond
the operator-selected T4 tranche.

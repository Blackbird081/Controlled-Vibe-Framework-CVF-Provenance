# CVF GC-018 Baseline - CADP AI T5-R5 Authentication Composition Implementation

Memory class: governed-dispatch-baseline

rawMemoryReleased=false

Status: REVIEWER_ACCEPTED_DISPATCH_READY

Batch ID: CADP-AI-T5-R5

Dispatch base head: `189d8ff95`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Dispatcher/reviewer/closer: role-separated governed agents

Worker target: one source-and-test implementation worker in a later bounded phase

## Purpose

Authorize the exact T5-R4 Planned Implementation Manifest items 1-5: remove
the service-token test bypass, add deterministic proof time, enforce
non-test/non-development Auth.js configuration invariants, implement the
operator-selected fail-closed CADP credential-precedence policy, and add a
separate literal-false CADP authorization projection. No route or registry row
is authorized.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CADP-AI-T5-R5 --title "CADP AI T5 R5 Authentication Composition Implementation" --date 2026-08-15 --base 189d8ff95 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "CADP-AI-T5-R4 accepted bounded at af2f425d8 with Option A CADP_FAIL_CLOSED_ON_INVALID_TOKEN" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact T5-R4 authority, ten-path source/test manifest, focused verification, ownership, boundary, and return requirements |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| docOnlyNewFields | none |
| claimBoundary | dispatch authoring evidence only; no source behavior exists until separately executed and reviewed |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | baseline structure; source-verification columns; ADIF disclosure; ASCII-default discipline |
| gateRunPurpose | confirm packet shape after source-backed authoring |
| claimBoundary | baseline and companion dispatch only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`source-test implementation work-order dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "source-test implementation work-order dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: resolver returned none |
| Dispatch impact | no additional ADIF-specific constraint |

## Authorization / Source

| Authority | Evidence | Disposition |
|---|---|---|
| T5-R4 accepted contract | `docs/reference/CVF_CADP_AI_T5_R4_AUTHENTICATION_COMPOSITION_CONTRACT_2026-08-15.md` at material commit `af2f425d8` | PASS |
| operator policy checkpoint | Option A `CADP_FAIL_CLOSED_ON_INVALID_TOKEN`, recorded in the accepted contract and closure state | PASS |
| operator continuation | explicit `next` instruction on 2026-08-15 | PASS |
| clean dispatch base | `git status --short --untracked-files=all` empty at `189d8ff95c8b6eb99411844690672adc2fadf09b` | PASS |

## Decision / Baseline

Proceed with one no-commit implementation worker on exact manifest items 1-5.
Option A is fixed; route and registry work remain a later tranche.

## Scope / Owner Boundary

The worker may modify or create only the ten source/test paths named below and
the worker return. Authentication composition remains owned by
`authorizeRouteGovernanceProof`; the CADP policy wrapper selects Option A;
the CADP authorization projection remains a separate pure module and grants
no execution, mutation, or activation authority.

## Allowed Paths

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.test.ts`
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts`
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.test.ts`
7. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/cadp-authentication-policy.ts`
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/cadp-authentication-policy.test.ts`
9. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/cadp-authorization.ts`
10. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/cadp-authorization.test.ts`
11. `docs/reviews/CVF_CADP_AI_T5_R5_AUTHENTICATION_COMPOSITION_IMPLEMENTATION_WORKER_RETURN_2026-08-15.md`

## Forbidden Actions

- no CADP route, `ROUTE_GOVERNANCE_PROOF_REGISTRY` row, MCP/CLI/HTTP adapter,
  public response expansion, durable receipt store, provider/live/network call,
  credential readout, public sync, deployment, or production action;
- no edits outside the eleven-path allowed manifest;
- no weakening Option A, no session fallback after a presented invalid token
  on the CADP wrapper, and no authority field with a truthy value;
- no worker staging or commit.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| test mode currently bypasses token signature and timestamp after token equality | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | lines 37-67 | `verifyServiceTokenRequest` | service-token authentication | ACCEPT |
| route composition currently falls through from invalid token to session | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 118-208 | `authorizeRouteGovernanceProof` | route governance proof | ACCEPT |
| proof time currently uses ambient `new Date` | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 89-116 | `buildProof` | proof generator | ACCEPT |
| Auth.js currently uses mock secret/provider defaults and legacy-admin fallback | RISK_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | lines 30-79 | `authSecret`; `nextAuthConfig` | Auth.js configuration | ACCEPT |
| current route tests do not cover invalid-token plus valid-session denial or injected time | TEST_COVERAGE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.test.ts` | tests at lines 39-101 | `authorizeRouteGovernanceProof` | route proof tests | ACCEPT |
| current token tests cover production valid and bad-signature cases | TEST_COVERAGE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts` | tests at lines 27-52 | `verifyServiceTokenRequest` | token tests | ACCEPT |
| Option A and exact items 1-5 are accepted | GOVERNED_DECISION | `docs/reference/CVF_CADP_AI_T5_R4_AUTHENTICATION_COMPOSITION_CONTRACT_2026-08-15.md` | Required Contract Questions 3, 11, and 14 | `CADP_FAIL_CLOSED_ON_INVALID_TOKEN`; Planned Implementation Manifest | T5-R4 contract | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| packet paths | both proposed dispatch paths absent before authoring | PASS |
| new source/test paths | all five planned new paths returned `False` from `Test-Path` | PASS |
| batch collision | `rg -n "CADP-AI-T5-R5|AUTHENTICATION_COMPOSITION_IMPLEMENTATION" docs CVF_SESSION` returned no match before authoring | PASS |
| clean base | HEAD `189d8ff95c8b6eb99411844690672adc2fadf09b`; status empty | PASS |

## Evidence / Verification

Required proof is local and hermetic: TypeScript no-emit, five focused Vitest
files, the CADP authority-boundary checker, worker-return fast gate, diff
checks, and independent reviewer recomputation. Mock tests may prove code
behavior; they make no live or production claim.

## Risk / Corrective Action

Highest risks are identity confusion, accidental global Auth.js breakage, and
truthy CADP authority. Corrective controls are an explicit opt-in policy on the
CADP wrapper, compatibility tests for existing non-CADP composition, pure
environment validation with test/dev allowances, and exact literal-false tests.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch; no public-sync authority.

## Claim Boundary

This baseline authorizes a later no-commit source/test worker for exact items
1-5 only. It does not prove or authorize route registration, live governance,
provider access, public export, deployment, or production readiness.

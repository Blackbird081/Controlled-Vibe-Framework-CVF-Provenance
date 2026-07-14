# CVF GC-018 System Chain UC-04B R1 Web Auth And Readout Recovery

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: gc018_baseline

Date: 2026-07-14

Risk classification: R1

## Purpose

Authorize one fresh, bounded, provider-free recovery proof for the existing
CVF Web Operations chain after SCLP-UC04B-T4 closed blocked. The recovery must
prove authentication before the live ceiling starts, freeze the proof source,
record the invocation before execution, and never rerun.

## Proposed Tranche / Decision

Authorize `SCLP-UC04B-R1` as a no-commit recovery worker. The retained proof
spec may be repaired before execution. The worker may then invoke exactly one
Playwright command containing the positive developer case and negative
reviewer case. It may produce two Web submissions, one checker execution, zero
retries, and zero provider calls. Reviewer/closer owns acceptance and closure.

## Design Control Gate

| Control | Decision |
|---|---|
| auth path | direct NextAuth CSRF, credentials callback, and session check |
| positive actor | mock user `dev`, role `developer`, mapped Web operator |
| negative actor | mock user `reviewer`, read-only role |
| selected job | `docs_governance_check` |
| proof source | retained UC-04B Playwright spec, hashed after preflight |
| live ceiling | one Playwright command, two submissions, one checker execution |
| retry and provider ceiling | zero retries; zero provider calls |
| mutation boundary | proof and evidence only; runtime owners read-only |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| credentials auth resolves canonical mock users | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | credentials provider authorize block | `authorize` | NextAuth credentials provider | RUNTIME_BEHAVIOR | ACCEPT |
| mock password rule is username plus 123 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | credentials provider authorize block | `password` | NextAuth credentials provider | LITERAL_INVARIANT | ACCEPT |
| auth has a local fallback secret | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | NextAuth config secret field | `secret` | NextAuth configuration | VALUE_SET | ACCEPT |
| developer and reviewer users and roles exist | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mock-enterprise-db.ts` | MOCK_USERS entries | `MOCK_USERS` | mock enterprise user store | VALUE_SET | ACCEPT |
| direct auth flow obtains CSRF, posts credentials, and verifies session | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/utils.ts` | lines 28-51 | `signInViaNextAuth` | Playwright E2E auth helper | RUNTIME_BEHAVIOR | ACCEPT |
| selected job invokes the docs checker | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` | allowlisted job definitions | `docs_governance_check` | Web governance job owner | VALUE_SET | ACCEPT |
| reviewer is blocked before command execution | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` | authorization and submit blocks | `canTrigger`; `submitGovernanceJob` | Web governance job owner | RUNTIME_BEHAVIOR | ACCEPT |
| API maps developer and returns 403 for policy denial | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/system/jobs/route.ts` | POST handler | `POST` | Next API route | RUNTIME_BEHAVIOR | ACCEPT |
| Operations page submits and renders the selected job | canonical-contract:cvf-web-operations-page-source | current JOBS, runJob, latest, and jobs blocks | `JOBS`; `runJob`; `latest`; `jobs` | Web Operations page | RUNTIME_BEHAVIOR | ACCEPT |
| Playwright starts the real Next development server | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.ts` | webServer block | `webServer` | Playwright configuration | VALUE_SET | ACCEPT |
| retained proof spec is registered | `docs/corpus-intelligence/registry/entries/system-chain-uc04b-web-operations-proof.json` | paths list | `paths` | corpus scan registry source entry | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

Fresh reads at dispatch base `97becbd7d` confirm the auth, role, job, route,
page, and real-server facts above. The worker must refresh them at execution
base and run the focused owner and auth tests before freezing the proof spec.
Any contradiction or failed preflight stops before the live ledger starts.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| original T4 attempt closed blocked | material closure commit `d69b6d7b3` | SATISFIED |
| recovery is current next move | session commit `97becbd7d` | SATISFIED |
| contradiction learning is governed | `CVF_ADIF-0034` | SATISFIED |
| dispatch start clean | empty status at `97becbd7d` | SATISFIED |

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Recovery control | Evidence | Disposition |
|---|---|---|---|
| real Web runtime | existing Playwright config | server and route evidence | READY |
| auth certainty | direct source-backed preflight | session role assertion | READY |
| selected job execution | docs checker only | one positive job and audit chain | READY |
| meaningful denial | reviewer same-job POST | 403 and no runner events | READY |
| bounded cost | immutable ledger | 1/2/1/0/0 counters | READY |
| learning retention | ADIF-0034 controls | reviewer reconciliation | READY |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Live runtime or provider proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cvf-web`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Live runtime or provider proof" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --max-results 20 --json`

Returned defects: ADIF-0033

Directly applicable governed defect: `CVF_ADIF-0034`

## Cost And Retry Control

One Playwright command, two Web submissions, one checker execution, zero
retries, and zero provider calls. The invocation ledger is set to started
before the command. After that transition, proof source and receipt logic are
frozen. Any failure produces one diagnostic and stops.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current local source plus bounded live Web proof |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | Web Operations chain and system-chain coverage ledger |
| Disposition | BLOCKED_UNTIL_CVF_PROOF |
| Claim boundary | prior attempts and chat are not current R1 proof |

## Acceptance Criteria

- Auth preflight proves developer and reviewer sessions before live execution.
- Focused Web owner and auth tests pass before source freeze.
- Proof-spec SHA-256 agrees across ledger and receipt.
- Exactly one command yields the two stable cases and exact counters.
- Developer sees the successful job readout and matching audit sequence.
- Reviewer receives the stable 403 denial and no running/final event.
- No provider call, retry, owner edit, secret disclosure, or commit occurs.

## Evidence / Verification

Required evidence includes execution base, source and auth refresh, focused
test results, frozen proof hash, monotonic ledger, sole command fingerprint,
two stable cases, exact counters, UI/API/audit/checker reconciliation, secret
scan, exact changed set, stage state, and unchanged HEAD.

## Fail Conditions

Source contradiction, preflight failure, unstable auth, hash mismatch, proof
edit after ledger start, second command, wrong counters, positive failure,
negative allow, audit mismatch, provider use, secret leak, owner mutation, or
stronger claim stops the tranche.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance recovery packet; no public-sync scope.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Dependency Release Evidence`; `Public Export Disposition` |
| gateRunPurpose | confirmation after source inventory, not first discovery |
| claimBoundary | dispatch authorization only; no Web invocation in this batch |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` |
| generatedProfile | GC-018 dispatch baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | source-backed bounded recovery authoring |
| checkerReadAheadConfirmation | guard orientation, literal gotchas, and applicable checker contracts read |
| docOnlyNewFields | invocation ledger and frozen proof hash fields in dated evidence only |
| claimBoundary | packet authorization only |

## Claim Boundary

A PASS may prove only one local development Web path for one selected checker,
one authorized role, and one read-only denial in one evidence window. It does
not prove all jobs, provider governance, production, public readiness, scale,
certification, or user value.

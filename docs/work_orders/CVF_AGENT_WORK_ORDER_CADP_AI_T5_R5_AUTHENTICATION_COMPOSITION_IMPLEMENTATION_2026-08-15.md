# CVF Agent Work Order - CADP AI T5-R5 Authentication Composition Implementation

Memory class: governed-worker-dispatch

rawMemoryReleased=false

Status: REVIEWER_ACCEPTED_DISPATCH_READY

Batch ID: CADP-AI-T5-R5

Dispatch base head: `189d8ff95`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: one source-and-test implementation worker in a later bounded phase

Reviewer/closer: independent reviewer/closer role

Worker return path: `docs/reviews/CVF_CADP_AI_T5_R5_AUTHENTICATION_COMPOSITION_IMPLEMENTATION_WORKER_RETURN_2026-08-15.md`

## Dispatch Prompt Envelope

Role: source-and-test implementation worker for `CADP-AI-T5-R5`.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T5_R5_AUTHENTICATION_COMPOSITION_IMPLEMENTATION_2026-08-15.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker must capture the clean committed HEAD at start.

Current-time note: artifact and authority date is 2026-08-15.

Do-not-misread: implement only T5-R4 manifest items 1-5. Do not add a route,
registry row, transport adapter, durable store, live call, public sync, deploy,
or production configuration.

Required first actions: read startup front doors, active handoff, guard
orientation, literal gotchas, paired baseline, this work order, the accepted
T5-R4 contract and return, every source/test path in Source Verification, and
applicable checker sources; capture clean execution base; run
pre-implementation before editing.

Return contract: implement and test the exact manifest, create the worker
return, leave every change unstaged and uncommitted, and return one allowed
worker terminal token.

## Purpose

Implement the accepted Option A authentication-composition contract with
deterministic proof time, fail-closed service-token verification, bounded
Auth.js environment invariants, and a separate literal-false CADP
authorization projection while preserving existing non-CADP route behavior.

## Operator Checkpoint

Resolved on 2026-08-15: Option A is mandatory. The exact policy token is
`CADP_FAIL_CLOSED_ON_INVALID_TOKEN`; Option B is outside this packet.

## Authorization / Dependencies

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T5-R4 contract | `docs/reference/CVF_CADP_AI_T5_R4_AUTHENTICATION_COMPOSITION_CONTRACT_2026-08-15.md` accepted at `af2f425d8` | Option A and items 1-5 must remain unchanged | PASS |
| T5-R4 worker return | `docs/reviews/CVF_CADP_AI_T5_R4_AUTHENTICATION_COMPOSITION_CONTRACT_HARDENING_WORKER_RETURN_2026-08-15.md` accepted with repairs | reviewer corrections are binding | PASS |
| operator continuation | explicit `next` instruction on 2026-08-15 | authorizes fresh packet, not direct ungoverned implementation | PASS |
| clean closure state | continuity commit `189d8ff95` | dispatch may be authored from clean HEAD | PASS |

## Authority Chain

Operator `next` instruction -> accepted T5-R4 Option A contract -> paired
GC-018 baseline -> this exact T5-R5 work order -> no-commit worker ->
independent reviewer/closer.

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | selected Option A and opened the next governed packet |
| dispatcher | source-verify, gate, commit, and sync this packet |
| implementation worker | edit only the eleven owned paths; test; do not commit |
| independent reviewer/closer | recompute evidence, repair within reviewer scope, commit, and sync |

## Worker Autonomy / No-Question Rule

The worker must repair any failing gate, typecheck, or focused test inside the
Allowed scope, rerun it, and record the result. Mandatory allowed-scope
remediation is not optional. Return only when a source contradiction or
required forbidden-scope expansion makes completion impossible.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake source | operator continuation of accepted repo-local T5-R4 contract |
| Route | `SINGLE_AGENT_MULTI_ROLE` |
| canonical route mode | `SINGLE_AGENT_MULTI_ROLE` |
| scope classification | R2 security-sensitive source/test implementation |
| risk sensitivity | authentication precedence, environment configuration, and literal-false authority; fail closed |
| selected role route | dispatcher authors; one no-commit worker implements; independent reviewer/closer accepts |
| Runtime/source modification | exact ten source/test paths only |
| External evidence intake | not authorized |
| Disposition | no-commit implementation after committed dispatch continuity |
| escalation condition | forbidden path, Option A change, route/registry, secret/network/live/public/deploy effect, destructive action, or claim-boundary expansion |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CADP-AI-T5-R5 --title "CADP AI T5 R5 Authentication Composition Implementation" --date 2026-08-15 --base 189d8ff95 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "CADP-AI-T5-R4 accepted bounded at af2f425d8 with Option A CADP_FAIL_CLOSED_ON_INVALID_TOKEN" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | completed exact source/test behavior, manifest, gates, rollback, ownership, and worker-return shape |
| checkerReadAheadConfirmation | same nine checker sources recorded in the paired baseline |
| docOnlyNewFields | none |
| claimBoundary | scaffold provenance only; worker execution remains pending |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`source-test implementation work-order dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "source-test implementation work-order dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: resolver returned none |
| Dispatch impact | no additional ADIF-specific constraint; all canonical guards still apply |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | Source Verification columns; Agent Operation Trace fields; no-commit profile fields; `COMPLETE_PENDING_REVIEW`; Public Export Disposition; Epistemic Process labels |
| gateRunPurpose | derive the packet and return shape before dispatch and use gates only as confirmation |
| claimBoundary | covers this dispatch and its worker return; no unrelated checker family claim |

## Required First Reads

| Source | Action | Reason |
|---|---|---|
| `AGENTS.md` | READ | root authority and routing |
| `CVF_SESSION_MEMORY.md` | READ | current mode and boundary |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ | compact startup facts |
| `AGENT_HANDOFF_V59_2026-08-11.md` | READ | active handoff |
| `docs/reference/guard_orientation/README.md` | FULL_READ | worker orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ | literal safety |
| `docs/baselines/CVF_GC018_CADP_AI_T5_R5_AUTHENTICATION_COMPOSITION_IMPLEMENTATION_2026-08-15.md` | FULL_READ | paired authorization |
| `docs/reference/CVF_CADP_AI_T5_R4_AUTHENTICATION_COMPOSITION_CONTRACT_2026-08-15.md` | FULL_READ | binding design and Option A |
| `docs/reviews/CVF_CADP_AI_T5_R4_AUTHENTICATION_COMPOSITION_CONTRACT_HARDENING_WORKER_RETURN_2026-08-15.md` | FULL_READ | reviewer corrections |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | SOURCE_VERIFIED | token verification behavior |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts` | SOURCE_VERIFIED | existing token tests |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | SOURCE_VERIFIED | composition and proof time |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.test.ts` | SOURCE_VERIFIED | compatibility tests |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | SOURCE_VERIFIED | Auth.js fallbacks |
| `governance/compat/check_cadp_authority_boundary_drift.py` | READ | literal-false boundary |
| applicable worker-return checker sources | READ | exact output shape |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| token equality bypasses signature and time in test mode | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | lines 37-67 | `verifyServiceTokenRequest` | service-token authentication | ACCEPT |
| invalid token currently falls through to session | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 118-208 | `authorizeRouteGovernanceProof` | route governance proof | ACCEPT |
| generated time is ambient | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 89-116 | `buildProof` | proof generator | ACCEPT |
| mock Auth.js values and legacy admin fallback exist | RISK_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | lines 30-79 | `authSecret`; `nextAuthConfig` | Auth.js configuration | ACCEPT |
| current route tests cover four basic cases only | TEST_COVERAGE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.test.ts` | lines 39-101 | `authorizeRouteGovernanceProof` | route proof tests | ACCEPT |
| current token tests cover production signature paths | TEST_COVERAGE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts` | lines 27-52 | `verifyServiceTokenRequest` | token tests | ACCEPT |
| Option A is binding | GOVERNED_DECISION | `docs/reference/CVF_CADP_AI_T5_R4_AUTHENTICATION_COMPOSITION_CONTRACT_2026-08-15.md` | Question 3 and Reviewer Correction Ledger carry-forward | `CADP_FAIL_CLOSED_ON_INVALID_TOKEN` | CADP authentication policy | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| two dispatch paths | absent before authoring | PASS |
| five new implementation paths | exact `Test-Path` results false before dispatch | PASS |
| batch/title collision | `rg -n "CADP-AI-T5-R5|AUTHENTICATION_COMPOSITION_IMPLEMENTATION" docs CVF_SESSION` returned no match before authoring | PASS |
| source symbols | current files contain every cited symbol | PASS |

## Scope / Implementation Requirements

1. Remove the `NODE_ENV === 'test'` authentication shortcut. Token equality
   alone must never bypass HMAC signature and timestamp verification. Update
   tests and existing route-proof fixtures to use real local HMAC inputs.
2. Add explicit time injection to `authorizeRouteGovernanceProof` and
   `buildProof`, using one supplied millisecond value for token-window
   verification and `generatedAt`. Preserve default ambient time for existing
   callers and avoid global clock stubs.
3. Add a named invalid-token precedence input to the existing composition
   helper. Default behavior for existing non-CADP callers must remain session
   fallback for compatibility; the CADP wrapper must always pass
   `CADP_FAIL_CLOSED_ON_INVALID_TOKEN` and must not evaluate session after a
   presented invalid token.
4. Create `cadp-authentication-policy.ts` as the only CADP policy wrapper. It
   must export the named Option A constant and a typed wrapper over
   `authorizeRouteGovernanceProof`; it must not register any route.
5. Add a pure, separately owned Auth.js environment validator. Test and
   development may use the existing mock values. Any other environment must
   require non-empty `NEXTAUTH_SECRET`, `GITHUB_ID`, `GITHUB_SECRET`,
   `GOOGLE_ID`, and `GOOGLE_SECRET`; missing values must throw before Auth.js
   configuration is accepted. The legacy `CVF_ADMIN_USER`/`CVF_ADMIN_PASS`
   credentials fallback must be unavailable outside test/development.
6. Create `cadp-authorization.ts` as a pure projection from authenticated
   identity/session provenance to CADP authority metadata. It must preserve
   `actorId`, impersonated `realActorId`, and role where present, and must
   expose `receiptGrantsExecution`, `receiptGrantsMutation`, and
   `receiptGrantsActivation` as literal `false`. It must not decide route
   access or persist a receipt.
7. Preserve deny `actorId: null`, secret-safe responses, body-text signing,
   existing five-route registry contents, and existing non-CADP behavior.

## Pre-Flight Checks

1. Capture full HEAD and exact status; stop unless the worktree is clean.
2. Confirm this baseline/work order are committed and all five `NEW` paths are absent.
3. Reproduce every Source Verification symbol search.
4. Run pre-implementation from the captured execution base.
5. Stop on drift, collision, concurrent changes, or forbidden-path need.

## Execution Plan

1. Harden service-token verification and update its focused tests.
2. Add deterministic time and explicit precedence input to route proof; update tests.
3. Add the CADP Option A wrapper and focused policy tests.
4. Add Auth.js environment invariants and focused configuration tests.
5. Add the separate literal-false CADP authorization projection and tests.
6. Run TypeScript, all five focused test files, CADP drift, file-size, fast-return, and diff checks.
7. Create the worker return, rerun every final command, and hand off unstaged/uncommitted.

## Write Ownership

### Worker-Owned Writable Paths

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

### Reviewer-Owned Closure Paths

Completion review if required, this baseline/work order, CADP roadmap or
corpus intelligence if actually affected, and continuity surfaces.

Every other path is forbidden to the worker.

## Focused Test Matrix

| Case | Required result |
|---|---|
| valid signed service token | ALLOW without session evaluation |
| valid token missing/bad signature in test and production modes | DENY token verification |
| invalid presented token plus valid session through CADP wrapper | DENY; session verifier not called |
| no token plus valid session through CADP wrapper | ALLOW session |
| existing non-CADP helper with invalid token plus valid session | existing compatibility fallback remains ALLOW |
| injected time | exact deterministic `generatedAt` and token-window verification |
| impersonated session projection | preserves actor and real actor; all three authority fields false |
| non-impersonated and service identities | bounded provenance; all authority fields false |
| production-like missing Auth.js env | throws/fails closed |
| test/development Auth.js env | mock defaults remain available |
| legacy admin fallback outside test/development | unavailable |
| registry membership | remains the same five routes; no CADP row |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| ten source/test paths in Worker-Owned Writable Paths | implement or update exactly as required; every path must exist at handoff |
| worker return | create full evidence packet with source inventory, test receipts, exact changed set, and no-commit proof |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | role-neutral dispatch; later implementation worker; subsequent independent reviewer/closer |
| phase | dispatch, implementation, review, closure conversion |
| baseHeadFor(phase) | dispatchBaseHead=`189d8ff95`; executionBaseHead=worker capture; closureBaseHead=reviewer set |
| changedSetScope(phase) | worker eleven-path manifest; reviewer-owned closure and continuity separately |
| traceScope(phase, actor) | worker records source edits/tests/diff; reviewer independently recomputes |
| commitOwner(phase) | `WORKER_MUST_NOT_COMMIT`; reviewer/closer commits |
| crossBatchIsolation | no unrelated paths or concurrent batch changes |
| nextMoveSurfaces | reviewer updates governed state only after acceptance |

## Single-Agent Multi-Role Control Block

| Field | Control |
|---|---|
| Single agent owns implementation and review | NO |
| Role separation ledger | delegated worker owns implementation and worker return; independent reviewer/closer owns acceptance, commit, and continuity |
| Evidence basis | current repo source, actual diff, TypeScript, focused tests, CADP drift checker, and governance receipts; provider memory is not authority |
| Self-review boundary | worker may self-check but may not accept, close, stage, or commit its own output |
| Gate sequence | pre-dispatch by dispatcher; pre-implementation, focused checks, and fast return by worker; reviewer-fast and material-only pre-closure by reviewer |
| Escalation conditions | forbidden paths, Option A change, route/registry, provider/live/network, secrets, public sync, deploy, destructive action, or claim expansion |
| Worker | delegated implementation worker |
| Reviewer / committer | independent reviewer/closer |
| Human escalation checkpoint | scope or policy expansion only |
| Collusion boundary | reviewer must inspect the real diff and rerun required checks before commit |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CADP_AI_T5_R5_AUTHENTICATION_COMPOSITION_IMPLEMENTATION_COMPLETION_2026-08-15.md` (optional; prefer corrected worker return if it safely carries final decision) |
| reviewerOwnedClosurePaths | worker outputs after accepted repair; baseline; work order; affected roadmap/telemetry; continuity |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CADP_AI_T5_R5_AUTHENTICATION_COMPOSITION_IMPLEMENTATION_WORKER_RETURN_2026-08-15.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Disposition; Source Inventory; Gate
Evidence; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta
Execution Claim Boundary Control Block; External Knowledge Intake Routing;
Rescan Intelligence Hardening; Corpus Completeness And Report Integrity;
Finding-To-Governance Learning Disposition; Epistemic Process Block; Public
Export Disposition; Machine Closure Package; Claim Boundary; git status
--short; Changed Files; Worker Experience Retrospective; Command Evidence;
No-Commit Statement.

## Required Checks

Run from repository root unless a command explicitly changes directory:

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
Push-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm run check
npx vitest run src/lib/service-token-auth.test.ts src/lib/route-governance-proof.test.ts src/auth.test.ts src/lib/cadp-authentication-policy.test.ts src/lib/cadp-authorization.test.ts
Pop-Location
python governance/compat/check_cadp_authority_boundary_drift.py
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git diff --cached --name-status
git status --short --untracked-files=all
git rev-parse HEAD
```

No package install, network access, browser, external provider, HTTP/MCP/CLI
invocation, credentials, or live test is authorized.

## Verification Commands

Use the exact command block under Required Checks. The mandatory return gate is
`python governance/compat/run_worker_return_fast_gate.py`; individual checker
substitution is forbidden.

## Evidence Requirements

- exact execution HEAD before and after work;
- exact changed-set and empty cached diff;
- TypeScript no-emit PASS;
- all five focused test paths PASS after the last edit;
- CADP authority drift and worker-return fast gate PASS;
- negative proof that CADP invalid-token precedence does not call session;
- no raw secret values in output or evidence.

## Acceptance Criteria

- all ten source/test paths exist and no other source/test path changes;
- focused tests and TypeScript no-emit pass after the last edit;
- Option A denies before session evaluation;
- existing non-CADP behavior and five-route registry stay compatible;
- deterministic time requires no global clock stub;
- production-like missing Auth.js configuration fails closed;
- all CADP authority flags are literal false;
- worker-return fast gate passes and HEAD/staging remain unchanged.

Fail conditions: any scope expansion, CADP route/registry addition, truthy
authority flag, invalid-token session fallback through the CADP wrapper,
secret exposure, live/provider/network action, or unreviewed commit.

## Review Gate

Worker handoff is not closure. Independent review must inspect all eleven
paths, rerun the required checks, accept or repair the returned implementation,
create the material commit, and run material-only committed-range pre-closure
before continuity changes.

## Epistemic Process Block

Epistemic Process Applicability: BOUNDED_GOVERNANCE_IMPLEMENTATION

Expected Result / Prediction: Option A can be implemented as an opt-in CADP
policy while preserving the current helper default for existing routes; time
and environment behavior can be made deterministic and fail closed inside the
exact manifest.

Evidence Comparison Requirement: compare focused tests, TypeScript results,
and actual diff against every prediction and manifest row.

Contradiction Handling Requirement: source/API incompatibility or required
out-of-manifest change must return a contradiction or gap disposition and stop.

Claim Update Requirement: classify the result as confirmed, narrowed, revised,
or blocked without extending to live or production readiness.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer role |
| Provider or surface | local private provenance repository |
| Session or invocation | CADP-AI-T5-R5 dispatch authoring, 2026-08-15 |
| Working directory | repository root |
| Command or tool surface | governed reads, source searches, scaffold helper, ADIF resolver, patch edits, governance gates, git status/diff |
| Target paths | paired GC-018 baseline and this work order |
| Allowed scope source | operator `next` instruction plus accepted T5-R4 contract |
| Before status evidence | clean HEAD `189d8ff95c8b6eb99411844690672adc2fadf09b` |
| After status evidence | exact two-file dispatch authoring set before commit |
| Diff evidence | `git diff --name-status`; `git diff --check` |
| Approval boundary | author packet only; worker execution begins from later committed post-sync HEAD |
| Claim boundary | local dispatch evidence only; no implementation or runtime result |
| Agent type | dispatcher |
| Invocation ID | `cadp-ai-t5-r5-dispatch-2026-08-15` |
| Expected manifest | `docs/baselines/CVF_GC018_CADP_AI_T5_R5_AUTHENTICATION_COMPOSITION_IMPLEMENTATION_2026-08-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T5_R5_AUTHENTICATION_COMPOSITION_IMPLEMENTATION_2026-08-15.md` |
| Actual changed set | `docs/baselines/CVF_GC018_CADP_AI_T5_R5_AUTHENTICATION_COMPOSITION_IMPLEMENTATION_2026-08-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T5_R5_AUTHENTICATION_COMPOSITION_IMPLEMENTATION_2026-08-15.md` |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | T5-R5 source/test implementation dispatch authoring |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: packet and current-source verification only |
| receiptEvidence | CVF_RECEIPT_PRESENT: local command and gate evidence will be captured before dispatch commit |
| actionEvidence | ACTION_EVIDENCE_PRESENT: exact two-file dispatch diff |
| invocationBoundary | local document authoring and static source inspection only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, runtime, or adapter interception claim |
| claimLanguage | dispatch is ready for a later no-commit worker after committed continuity sync |
| forbiddenExpansion | no route/registry, HTTP/MCP/CLI, provider/live/network, secrets, public sync, deployment, or production |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: N/A with reason - worker may not edit a
protected governance or session path.

Protected paths: N/A with reason - none in the worker manifest.

Operator authorization: N/A with reason - no protected-path worker edit.

Rollback boundary: N/A with reason - no protected-path worker edit.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current runtime source verification and governed work-order evidence; no external artifact intake |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order |
| Disposition | BLOCKED_UNTIL_CVF_PROOF for runtime readiness; local implementation/test evidence only in this tranche |
| Claim boundary | CVF-governed repo sources remain the only authority |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing CVF Web `src/lib/` authentication and authorization module family plus colocated tests |
| Storage decision | add two same-domain pure modules and colocated tests; reuse existing auth and route-proof owners |
| Existing aggregate impact | none |
| Generated state impact | none during worker implementation |
| Durable governance boundary | no durable governance foundation, registry, index, route, or storage owner is created |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this packet changes current CVF Web authentication
source/tests under an accepted T5-R4 contract; it makes no legacy-corpus,
foundation-plane absorption, or workflow-chain completeness claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch; public sync is forbidden.

## Worker Terminal Disposition Enum

Return exactly one:

- `COMPLETE_PENDING_REVIEW`;
- `BLOCKED_STALE_EXECUTION_BASE`;
- `BLOCKED_SOURCE_DRIFT`;
- `BLOCKED_SCOPE_EXPANSION_REQUIRED`;
- `BLOCKED_TEST_OR_TYPECHECK_FAILURE`.

## Closure Checklist

- [ ] exact worker manifest reconciled;
- [ ] TypeScript and five focused test files pass after last edit;
- [ ] CADP drift, file-size, worker-return fast gate, and diff check pass;
- [ ] HEAD unchanged and staging empty at worker handoff;
- [ ] independent reviewer accepts and creates material commit;
- [ ] material-only committed-range pre-closure passes;
- [ ] continuity is updated in a separate commit and separately gated.

## Return-To-Orchestrator Conditions

Return without continuing on stale base, source contradiction, missing
dependency, forbidden-path need, required network/credential access, or any
change to the accepted Option A boundary. A test/type/gate failure inside the
Allowed scope must be repaired and rerun; return only if it remains impossible
because the repair requires forbidden expansion.

## Claim Boundary

This work order authorizes exact local source/test implementation and hermetic
verification only. It does not authorize a CADP route or registry row, durable
receipt persistence, external invocation, provider/live proof, credentials,
public sync, deployment, production change, or worker commit.

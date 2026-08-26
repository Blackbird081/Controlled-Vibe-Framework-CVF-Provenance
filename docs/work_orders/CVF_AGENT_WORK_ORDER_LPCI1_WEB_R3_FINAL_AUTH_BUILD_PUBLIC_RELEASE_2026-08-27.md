# CVF Agent Work Order - LPCI1 Web R3 Final Auth Build Public Release

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-08-27

Batch ID: LPCI1-WEB-R3-FINAL-AUTH-BUILD-PUBLIC-RELEASE

dispatchBaseHead: `c1fc509f3`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_MUST_CAPTURE_AT_CLOSURE

Responds to baseline: `docs/baselines/CVF_GC018_LPCI1_WEB_R3_FINAL_AUTH_BUILD_PUBLIC_RELEASE_2026-08-27.md`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: no-commit dependency-closed public-candidate worker; the current
orchestrator remains independent reviewer, commit steward and release owner.

Canonical packet: this work order plus its paired R3 baseline.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: operator evidence confirms all six Auth.js variable names
exist in Netlify at all scopes and contexts; values remain undisclosed.

Do-not-misread notes: synthetic local values are not production credentials;
never weaken auth, read secrets, commit, push or deploy.

Required first actions: startup and guard reads, both repository identity and
clean-state checks, public baseline capture, then all allowlisted paths.

Return contract: leave both HEADs unchanged and staging empty, retain the
public candidate uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON` in the named artifact.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id LPCI1-WEB-R3 --title "Final Auth Build Public Release" --date 2026-08-27 --base c1fc509f3 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "R2 closed blocked at 92c96a04d" --stdout` |
| generatedProfile | public-sync no-commit candidate plus reviewer publication |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact dual-repository allowlist, synthetic auth build boundary and reviewer-only deploy |
| checkerReadAheadConfirmation | dispatch, route, return, trace, public export, handoff and Delta checkers read |
| docOnlyNewFields | Auth Build Proof |
| claimBoundary | packet provenance only; no public or hosted claim |

## Authority Chain

Operator release authority -> accepted blocked R2 `92c96a04d` -> paired R3
baseline -> this work order -> one no-commit worker -> independent reviewer and
release steward.

## Agent Roles

Worker: exact public candidate preparer and local proof collector. Reviewer:
semantic reviewer, private/public commit steward and deployment observer.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| Intake source | R2 build evidence plus operator Netlify variable-name presence evidence |
| Route | MULTI_AGENT_SINGLE_ROLE |
| canonical route mode | MULTI_AGENT_SINGLE_ROLE |
| risk sensitivity | P1 hosted blocker; public effects reviewer-owned |
| scope classification | terminal dependency-closed public candidate |
| selected role route | dispatcher -> no-commit worker -> independent reviewer/release steward |
| Worker role | exact allowlist projection and non-secret local proof |
| Reviewer role | review, commits, push, Netlify observation and terminal closure |
| Commit mode | WORKER_MUST_NOT_COMMIT |
| Checkpoint disposition | local candidate released; public effects reviewer-only |
| escalation condition | unowned dependency, secret access, auth weakening or manifest drift |

## Required First Reads

1. startup front door, bootstrap model and active handoff
2. guard orientation and literal-format gotchas
3. paired R3 baseline and this work order
4. critical repository boundary and public one-shot preflight standard
5. accepted R1/R2 returns and every allowlisted source path
6. `scripts/check_cvf_public_sync_candidate.py`

## Target / Source

Private repository: current workspace at the exact clean execution HEAD supplied
by the orchestrator. Public candidate repository:
`D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`.

Dispatch base: `c1fc509f3`.

Required worker return:
`docs/reviews/CVF_LPCI1_WEB_R3_FINAL_AUTH_BUILD_PUBLIC_RELEASE_WORKER_RETURN_2026-08-27.md`.

## Purpose

Prepare and prove the exact dependency-closed public candidate needed to carry
accepted R1/R2 LPCI build repairs into the public repository while preserving
the production Auth.js fail-closed invariant. Do not commit, push or deploy.

## Preflight

Before mutation:

1. confirm private HEAD exactly matches the orchestrator-supplied execution HEAD
   and contains dispatch base `c1fc509f3` as ancestor;
2. confirm private worktree and staging are clean;
3. in public-sync, run `git remote -v`, require the exact public remote, branch
   `main`, clean worktree and empty staging;
4. capture public baseline HEAD;
5. confirm the worker-return path is absent;
6. do not read `.env.local`, browser storage, Netlify values, Git credentials,
   API keys or OAuth values.

## Write Ownership

Private repository:

- `docs/reviews/CVF_LPCI1_WEB_R3_FINAL_AUTH_BUILD_PUBLIC_RELEASE_WORKER_RETURN_2026-08-27.md` only.

Public-sync repository, exact candidate allowlist:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.coordination.barrel.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/delegation.contract.test.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/package.json`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/package.boundary.test.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/receipt-identity.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/package.json`
- `EXTENSIONS/CVF_MODEL_GATEWAY/package-lock.json`
- `EXTENSIONS/CVF_MODEL_GATEWAY/scripts/run-p4b-b-live-proof.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/lpci-safe.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/p4b-b-dry-run-gate.test.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/lpci-safe.test.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/package.json`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/package-lock.json`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-live-provider-value-pilot.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/live.provider.value.pilot.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.live.provider.value.pilot.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts`

No optional path exists. If dependency closure requires another file, return
`BLOCKED_WITH_REASON`; do not add it.

## Execution Plan

1. Capture dual-repository anchors and prove clean boundaries.
2. Fully read and hash-compare the exact allowlist.
3. Project current private contents into only mismatched public paths.
4. Run package checks and focused tests.
5. Run synthetic process-local production build and remove residue.
6. Run public-sync preflight and diff hygiene.
7. Author the private worker return and yield without commit/push/deploy.

## Implementation Method

For each allowlisted public path, compare public baseline content with the
current private source. Copy only the current private file content into the
matching public destination. Do not copy commit history or any private docs.
Run `npm install --package-lock-only` only inside an allowlisted package and
only if required to reconcile an allowlisted lockfile; do not upgrade unrelated
dependencies.

### Reviewer Amendment 1 - Superseding Recovery Method

The original current-post-image copy method is rejected for reviewer recovery
because it imported later unrelated CADP content. The independent reviewer may
prepare the candidate directly, without another worker, using only these exact
provenance deltas:

- `8007e269f`: the three allowlisted Control Plane paths;
- `1e31db99a`: the Model Gateway package/lock, harness, runner and focused test;
- `f7f5cf1ef`: the allowlisted R1 paths, with only its 12-line delta applied to
  Guard Contract `src/package.boundary.test.ts`;
- `92c96a04d`: the five allowlisted Execution Plane paths;
- `5c86f6d77`: only the ten-line export delta in Model Gateway `src/index.ts`.
- `3c51ac5e6`: only the fail-closed 401 expectation delta in Web LPCI
  `query/route.test.ts`.

New files use their exact introducing-commit post-image. A path whose public
blob equals the relevant source commit's parent may use the exact source commit
post-image. Model Gateway package and lockfile changes are applied in order
`1e31db99a` then `f7f5cf1ef`. Do not project any later private post-image, CADP
contract cluster, documentation or registry. Do not run plain `npm install`;
existing local dependencies may be relinked without network only by a command
whose offline behavior is explicit and whose tracked delta remains allowlisted.

Amended public allowlist count: 24 paths. This amendment is part of R3 and
admits no R4.

## Auth Build Proof

Do not read Netlify secrets. For local structural proof, launch the exact Web
build from a child process whose environment adds synthetic, clearly non-live
values for the five required Auth.js variables and
`NEXTAUTH_URL=https://cvfcoding.vn`. Do not persist these values. The build must
make no OAuth or provider request. Remove generated `.next` residue after proof.

## Verification Commands

Run in the public candidate:

```powershell
npm --prefix EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION run check
npm --prefix EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION test -- --run tests/delegation.contract.test.ts
npm --prefix EXTENSIONS/CVF_GUARD_CONTRACT run check
npm --prefix EXTENSIONS/CVF_GUARD_CONTRACT test -- --run src/package.boundary.test.ts
npm --prefix EXTENSIONS/CVF_MODEL_GATEWAY run check
npm --prefix EXTENSIONS/CVF_MODEL_GATEWAY test -- --run tests/p4b-b-dry-run-gate.test.ts tests/lpci-safe.test.ts
npm --prefix EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION run check
npm --prefix EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION test -- --run tests/mao.live.provider.value.pilot.test.ts
npm --prefix EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web run check
npm --prefix EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web test -- --run src/lib/lpci/provider-binding.test.ts src/app/api/lpci/query/route.test.ts src/lib/package-test-script-boundary.test.ts
```

Then run the synthetic process-local production build and:

```powershell
python scripts/check_cvf_public_sync_candidate.py --public-root "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" --authorized-paths-json <worker-created-temporary-manifest-outside-both-repos> --expected-remote "https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git" --expected-branch main --baseline-ref <captured-public-head> --json
python governance/compat/run_worker_return_fast_gate.py --base <dispatch-commit> --head HEAD
git -C "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" diff --check
```

Temporary manifest must be outside both repositories and removed before return.

## Acceptance Criteria

- exact allowlist only, no manifest delta;
- missing-relative-dependency count zero beyond accepted public baseline debt;
- all named checks/tests pass;
- synthetic process-local production build exits zero;
- no `.next`, log, test-result or temporary residue remains;
- no provider/OAuth/network call occurs;
- private repository changes only by the worker return;
- both staging areas empty and both HEADs unchanged;
- public candidate remains uncommitted for independent review.

## Review Gate

Reviewer inspects every public diff, reproduces dependency/preflight and build
proof, verifies zero private artifact export, then alone decides commits, push,
deploy observation and terminal roadmap closure.

## Closure Checklist

Exact manifest; public remote/branch; clean start; package checks; focused
tests; synthetic build exit zero; cleanup; public preflight; zero secrets and
provider calls; reviewer commits; pushed SHA; Netlify success; `/landing` and
auth smoke; no R4.

## Return-To-Orchestrator Conditions

Return only `COMPLETE_PENDING_REVIEW` when every worker criterion passes, or
`BLOCKED_WITH_REASON` on the first concrete fail condition. Both HEADs and
staging areas remain unchanged.

## Operator Checkpoint

The operator supplied secret-name presence evidence and authorized the terminal
release workflow. Worker public effects remain forbidden. Reviewer may push and
observe deploy only after clean independent proof.

## Worker Autonomy / No-Question Rule

Within the exact dual-repository manifest, prepare and prove the candidate
directly. Do not ask optional questions or widen scope. Stop only on a named
fail condition.

## Fail Conditions

Stop and return `BLOCKED_WITH_REASON` on any unowned dependency, non-public
remote, dirty starting state, secret requirement, provider/OAuth call, auth
invariant weakening, failed build/test/preflight, or need to commit/push/deploy.
Do not widen scope or create R4.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_LPCI1_WEB_R3_FINAL_AUTH_BUILD_PUBLIC_RELEASE_WORKER_RETURN_2026-08-27.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python -X utf8 governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Evidence Requirements

Record private/public before and after HEAD/status/staging, exact manifest,
source hashes, command exits and counts, synthetic-build boundary, generated
cleanup, public-sync preflight JSON summary, and zero secret/provider/external
effect statement. Never record environment values.

## Reviewer Closure Conversion

The independent reviewer owns semantic review, repairs within the same exact
allowlist, material private commit, public candidate commit, pre-push gates,
push to public `main`, Netlify deploy observation, hosted `/landing` and
authentication-route smoke, roadmap terminal closure and session sync.

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_LPCI1_WEB_R3_FINAL_AUTH_BUILD_PUBLIC_RELEASE_COMPLETION_2026-08-27.md` |
| reviewerOwnedClosurePaths | worker return, completion review, roadmap, public commit receipt and continuity |
| closureOwner | independent orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: the worker may prepare but cannot publish. Only reviewer evidence may
convert this to `EXPORTED`.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | no-commit public-candidate worker |
| Provider or surface | private provenance plus sibling public-sync clone |
| Session or invocation | LPCI1-WEB-R3 worker execution |
| Working directory | both exact repository roots named above |
| Command or tool surface | Git reads, allowlisted file edits, npm local checks/tests/build, public-sync preflight |
| Target paths | exact write ownership manifest |
| Allowed scope source | this committed work order |
| Before status evidence | private clean worktree and public clean worktree; both staging areas empty; exact HEADs |
| After status evidence | private return only; public exact candidate; both staging empty |
| Diff evidence | both `git diff --name-status` outputs |
| Approval boundary | no commit, push, deploy, secret read or provider call |
| Claim boundary | candidate proof only, not public release |
| Agent type | worker |
| Invocation ID | `lpci1-web-r3-final-auth-build-public-release-worker-2026-08-27` |
| Expected manifest | one private return plus exact public allowlist |
| Actual changed set | worker records exactly |
| Manifest delta | must be NONE |
| Deletion or rename disposition | forbidden |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | private no-commit public candidate preparation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT only after named commands run |
| actionEvidence | ACTION_EVIDENCE_PRESENT only for exact local diffs |
| invocationBoundary | local files and synthetic build environment only |
| interceptionBoundary | no secret, OAuth, provider, push or deploy action |
| claimLanguage | candidate-ready, never published/production-ready |
| forbiddenExpansion | any path/action outside this work order |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current CVF source plus operator external configuration evidence |
| Matching local-view guard | `governance/compat/check_public_export_disposition.py`; `scripts/check_cvf_public_sync_candidate.py` |
| Owner surface | Auth.js, package owners, public-sync and Netlify |
| Disposition | RECONCILED_DESIGN_INPUT_ONLY |
| Claim boundary | no secret value or hosted success inferred |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: bounded exact dependency-closure projection, not a corpus scan.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - exact allowlisted source cluster.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| hosted build configuration can lag a newly enforced production invariant | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | R3 binds configuration-name proof, synthetic build, public preflight and hosted observation in one terminal tranche |

## Claim Boundary

This work order authorizes one no-commit local candidate worker only. It grants
no commit, push, deploy, OAuth login, secret access, provider/live call,
production claim, private history export, R4 or unrelated successor.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | dispatch envelope, anchors, exact manifest, no-commit return, public disposition, handoff and trace fields |
| gateRunPurpose | confirm packet shape after exact dependency mapping; this is evidence confirmation, not first discovery |
| claimBoundary | gate conformance does not prove build, push or deploy |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Public sync`, role=`dispatcher`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Public sync" --role dispatcher --lifecycle-phase pre-implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | exact no-commit public candidate controls apply |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit worker then independent reviewer/release steward |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=`c1fc509f3`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exact private return plus public allowlist |
| traceScope(phase, actor) | dual-repo hashes/diffs, tests/build, preflight and cleanup |
| commitOwner(phase) | reviewer only |
| crossBatchIsolation | no private export, secret read, provider call or unrelated roadmap work |
| Before status evidence | private clean worktree and public clean worktree; staging empty; exact remotes/branches |
| nextMoveSurfaces | named worker return then independent release review |

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "LPCI1-WEB-R3",
  "requestedProfile": "P4_CRITICAL",
  "classification": {
    "taskKind": "PUBLIC_RELEASE",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "CREDENTIAL_REFERENCE",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": ["AGENT_HANDOFF_V59_2026-08-11.md", "CVF_SESSION", "CVF_SESSION_MEMORY.md", "EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION", "EXTENSIONS/CVF_GUARD_CONTRACT", "EXTENSIONS/CVF_MODEL_GATEWAY", "EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION", "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web", "docs/baselines", "docs/roadmaps", "docs/reviews"],
  "claims": ["dependency-closed public candidate builds without weakening Auth.js"],
  "requiredProof": ["package checks", "focused tests", "synthetic production build", "public-sync preflight", "independent review"],
  "operatorCheckpoints": ["secret exposure", "remote mismatch", "scope expansion"],
  "forbiddenEffects": ["worker commit", "worker push", "worker deploy", "secret read", "provider call", "private history export"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

Value disposition: `CONTINUE_HIGH_VALUE`; this is the single terminal release
tranche and admits no R4.

## Reviewer Amendment 2 Exact Security-Recovery Manifest

This reviewer-owned correction remains LPCI1-WEB-R3 and supersedes the
24-path count with exactly 36 public paths. The original 24 paths remain
authorized. Add exactly:

- `.github/workflows/cvf-web-ci.yml`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.knowledge.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/override/route.governance.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/knowledge/ingest/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/knowledge/ingest/w116-cp5-delta.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/intake/route.governance.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/qbs/front-door-clarification/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/home-surface-controls.test.tsx`

For the seven test paths, apply only their source delta from `3c51ac5e6`.
For already allowlisted `lpci/query/route.test.ts` and
`provider-binding.test.ts`, the same commit delta may replace the earlier
partial projection where applicable. Dependency resolution may access the npm
registry but must not use `--force`; no provider API, OAuth flow, hosted secret
read, runtime auth weakening, or unrelated dependency modernization is allowed.

The workflow edit is limited to synthetic build-only Auth.js variables and the
package-script edit is limited to excluding both `.live.test.ts` and
`.live.test.tsx` from non-live unit and coverage commands. The reviewer must
preserve the 80% function threshold; the home-surface test may cover only
existing TemplateCard, CategoryTabs, and IntentEntry user interactions. The reviewer must
create a new candidate commit, push only the candidate branch, wait for both
exact-SHA server gates, and promote that identical SHA only on clean results.

## Reviewer Amendment 3 Exact Zero-Warning Manifest

Candidate `9373818caa33be9d424d1abaea9dbe9224281a56` is rejected
after exact-SHA server Web CI found 23 lint warnings under the existing
`--max-warnings=0` contract. Preserve that contract and add exactly these nine
public paths to the prior 36-path manifest:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.sot3-activation.alibaba.live.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/admin/AdminImpersonationControls.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/home/HomeBrowseExperience.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/hooks/useExecute.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/sot3-activation-evidence-readout.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.test.ts`

The cumulative amended manifest is exactly 45 paths. Allowed changes are only
removal of reported unused imports and obsolete lint directives, explicit
consumption of intentionally omitted integrity hashes, and replacement of the
two internal location assignments with `useRouter().push()`. Do not alter the
live-test exclusion, provider behavior, authentication decisions, coverage
threshold, workflow lint command or any other path. Create and push a new
candidate SHA, rerun both server gates, and promote only that identical SHA on
success. This amendment remains LPCI1-WEB-R3 and admits no R4.

Server build after lint PASS exposed one more clean-runner contract gap on the
already-authorized `.github/workflows/cvf-web-ci.yml`: Execution Plane package
dependencies are not installed, so its declared local Control Plane dependency
cannot resolve. Add exactly one `npm ci` step with working directory
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` before Web install/build. No new
path is admitted and the exact manifest remains 45 paths. Repeat both
exact-SHA server gates; the prior candidate remains forbidden from promotion.

## Reviewer Amendment 4 Exact Hosted-Build Manifest

Netlify deploy `6a8f4da837f87b0008019fb3` for exact public commit
`32315f3dcf8d123cf1792ad14e4dd2df9ff2ada6` ended in `error` without publish.
The detailed authenticated log is unavailable, so do not claim its exact error
line. Source and clean-runner evidence establish that `netlify.toml` omits the
sibling package install sequence required by the green GitHub build.

Add exactly root `netlify.toml` to the public manifest, bringing the cumulative
count from 45 to 46. Its build command may only mirror the green CI install
order for Control Plane, Model Gateway, Learning Plane, Guard Contract and
Execution Plane before the existing Web build. Preserve base, publish path,
environment-name handling, plugin, redirects and headers. No other path,
secret read, provider call, runtime change, threshold change or successor is
authorized. Run public-sync preflight, push a replacement candidate, promote
the identical SHA, and require successful Netlify publish plus safe hosted GET
smoke. This remains LPCI1-WEB-R3 and admits no R4.

## Reviewer Amendment 5 Exact Hosted Runtime

Replacement SHA `df7eb5df779c881685e4a70ac82efc319d2848f6` passed the
46-path public-sync preflight, but Netlify deploy
`6a8f4fcee9cb860008f7a0f1` ended in `error` before publish. The authenticated
Netlify error line remains unavailable and must not be claimed. A reviewer
reproduction with the configured Node 20 runtime fails before Web compilation
while installing Learning Plane's native `better-sqlite3`; the same exact
command is green under Node 22, matching the green GitHub Web runner.

Keep the cumulative manifest at exactly 46 paths. Change only root
`netlify.toml` build environment `NODE_VERSION` from `20` to `22`; preserve the
Amendment 4 command and every other field. No dependency upgrade, lockfile,
runtime source, secret access, provider call, threshold change or successor is
authorized. Push a replacement candidate, require public-sync PASS, promote
the identical SHA and require successful Netlify publish plus safe hosted GET
smoke. This remains LPCI1-WEB-R3 and admits no R4.

## Foundation Storage Layout Block

N/A with reason: R3 projects existing package-owned source files into the
public-sync clone and creates no new durable governance foundation, storage
layout, index or locator.

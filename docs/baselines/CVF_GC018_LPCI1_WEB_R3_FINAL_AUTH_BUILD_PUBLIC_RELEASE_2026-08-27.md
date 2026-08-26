# CVF GC-018 Baseline - LPCI1 Web R3 Final Auth Build Public Release

Memory class: FULL_RECORD

Status: ACTIVE_DISPATCH_BASELINE

docType: baseline

Date: 2026-08-27

Batch ID: LPCI1-WEB-R3-FINAL-AUTH-BUILD-PUBLIC-RELEASE

## Decision / Proposed Tranche

Proceed with exactly one terminal R3 containing a no-commit public-candidate
worker phase and reviewer-owned publication phase. No R4 is admitted.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | dispatch lifecycle, exact manifest, public disposition, no-commit and trace fields |
| gateRunPurpose | confirm terminal public-release packet shape after source verification; this is evidence confirmation, not first discovery |
| claimBoundary | checker conformance is not build, push, deploy or hosted evidence |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Public sync`, role=`dispatcher`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Public sync" --role dispatcher --lifecycle-phase pre-implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | exact public boundary, no-commit worker and reviewer-only publication remain mandatory |

## Purpose

Close the one remaining LPCI1 Web hosted-release blocker without weakening the
accepted production authentication invariant or exporting private provenance.
R2 material `92c96a04d` repairs the provider-grant caller chain. The exact Web
build now compiles and typechecks, then fails closed because production requires
`NEXTAUTH_SECRET`, `GITHUB_ID`, `GITHUB_SECRET`, `GOOGLE_ID`, and
`GOOGLE_SECRET`.

Operator evidence dated 2026-08-27 confirms all six production names now exist
in Netlify at all scopes and all deploy contexts: the five required variables
plus `NEXTAUTH_URL`. Values were never disclosed to an agent.

## Authorization / Decision

Decision: `PROCEED_ONE_CONSOLIDATED_R3`.

R3 contains one local no-commit worker phase followed by one independent
reviewer release phase. This is one tranche, not two successors. The worker may
prepare only the exact dependency-closed public candidate and non-secret build
proof. Only the reviewer may commit, push, trigger/observe Netlify, or declare
public export.

## Source Verification

| Fact | Verified path or symbol | Disposition |
| --- | --- | --- |
| production auth fails closed on five names | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts`; `validateAuthEnvironmentInvariants` | PRESERVE |
| root Netlify build targets cvf-web | `netlify.toml`; build base and command | REUSE |
| public remote owner | sibling public-sync clone `origin` | VERIFIED_PUBLIC_BOUNDARY |
| public auth source and root Netlify config already match private | `src/auth.ts`; root `netlify.toml` | NO_PROJECTION_NEEDED |
| public clone lacks R1/R2 grant/safe-entrypoint chain | exact private/public SHA-256 comparison over named files | PROJECT_BOUNDED_CHAIN |
| R1 accepted blocked material | `f7f5cf1ef` | INPUT |
| R2 accepted blocked material | `92c96a04d` | INPUT |
| Control Plane grant owner | `ProviderExecutionGrant`; `evaluateProviderExecutionAuthority` | OWNER_DEPENDENCY |
| Model Gateway grant harness | `runLiveProof`; `LiveProofHarnessOptions` | OWNER_DEPENDENCY |

## Scope

Private worker output is the named worker return only. Public-sync candidate
scope is the exact allowlist in the paired work order. The worker may copy the
current private form of an allowlisted file into the sibling public clone only
after confirming the public baseline is clean and the destination path is
tracked or explicitly authorized as new.

## Reviewer Amendment 1 - Provenance-Delta Recovery

The first worker return is accepted as a blocked diagnostic but not as a
candidate. Independent review proved that copying current private post-images
mixed later CADP changes into LPCI R3. Pulling the resulting 33-file Guard
Contract cluster would be unrelated scope inflation and is forbidden.

The same terminal R3 may recover without another worker or R4 by applying only
the exact code deltas introduced by source commits `8007e269f`, `1e31db99a`,
`f7f5cf1ef`, and `92c96a04d`. For
`EXTENSIONS/CVF_GUARD_CONTRACT/src/package.boundary.test.ts`, apply only the
12 LPCI R1 lines from `f7f5cf1ef`, not that commit's full post-image. Add the
ten-line Model Gateway root export delta from original LPCI binding commit
`5c86f6d77` to repair a previously omitted public dependency. Apply the single
fail-closed route-test expectation delta from `3c51ac5e6`; it updates stale 403
expectations to the earlier 401 authorization denial the route actually
enforces. No other path or historical delta is admitted.

This correction changes the public candidate from 22 to 24 exact paths. It
does not weaken Auth.js, authorize secrets/provider calls, or open a successor.

## Reviewer Amendment 2 - Security-Gate And CI Contract Recovery

The exact-SHA candidate `819d8acf62b73a4ff84c960940941a3ea53cec29`
passed the public-sync preflight but the Web CI dependency audit found ten
published vulnerabilities, including two critical and seven high findings.
Promotion of that SHA is forbidden. This is a serious release blocker inside
R3, not authority for R4 or a new roadmap.

The reviewer may update only cvf-web `package.json` and `package-lock.json` to
the smallest registry-resolved zero-audit set proven locally: `next@16.3.3`,
`eslint-config-next@16.3.3`, `next-auth@5.0.0-beta.32`, and `docx@9.7.1`, plus
non-force transitive lockfile remediation. The production build must preserve
the existing Auth.js fail-closed invariant.

Once audit advanced, full CI exposed pre-existing public test-contract drift:
seven test files still presented unsigned service tokens although the current
runtime requires HMAC timestamp/signature, and the unit-test scripts excluded
only `.live.test.ts` while one live proof uses `.live.test.tsx`. The exact HMAC
test corrections are already provenance-owned by private commit `3c51ac5e6`;
apply only its deltas for the seven newly admitted test paths plus the already
allowlisted execute/query/provider-binding test paths. Update the two package
scripts to exclude both TypeScript extensions. No unsigned-token bypass or
runtime authorization change is allowed.

GitHub Actions may receive synthetic, non-secret build-only Auth.js values in
`.github/workflows/cvf-web-ci.yml` so its production build exercises the same
composition gate as local proof. These values must be literals with no hosted
credential meaning. The amended public manifest is exactly 34 paths. A new
candidate SHA must pass audit, build, tests, coverage, public-sync preflight and
server-side Web CI before identical-SHA promotion; `819d8acf` remains rejected.

## Non-Goals

- no private docs, reviews, roadmaps, session state, registries or governance
  internals enter public-sync;
- no OAuth secret value is read, printed, copied into source, logs or evidence;
- no weakening, bypass or removal of `validateAuthEnvironmentInvariants`;
- no provider/model live call;
- no worker commit, push, Netlify mutation or deploy trigger;
- no R4 or unrelated cleanup.

## Build And Secret Boundary

Local build proof may use process-local synthetic non-empty values named
`NEXTAUTH_SECRET`, `GITHUB_ID`, `GITHUB_SECRET`, `GOOGLE_ID`, and
`GOOGLE_SECRET`, plus `NEXTAUTH_URL=https://cvfcoding.vn`. Synthetic values
prove build composition only and must not be written to a file or described as
production credentials. Netlify values remain opaque and reviewer-observed by
name/status only.

## Public Projection Boundary

The public candidate must be prepared only in
`D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync` on
branch `main`, remote
`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`.
The private provenance repository must never be pushed.

## Acceptance Criteria

- public candidate contains only the exact allowlist;
- public-sync preflight returns PASS with zero new missing relative dependency;
- Guard Contract, Control Plane, Model Gateway and Execution Plane checks and
  relevant focused tests pass in the public candidate;
- cvf-web TypeScript and focused LPCI tests pass;
- production build with process-local synthetic auth variables exits zero;
- worker leaves both repositories uncommitted and staging empty;
- reviewer independently re-verifies, commits public candidate, pushes public
  `main`, observes Netlify success and performs `/landing` plus auth endpoint
  smoke without exposing secrets;
- roadmap closes with no R4.

## Risk And Stop Conditions

Stop on any unowned path, missing dependency outside the allowlist, secret
value exposure, auth-invariant weakening, generated residue, provider call,
public remote mismatch, non-main public branch, or build failure. A stop is not
authority to widen scope.

## Evidence

Record exact private/public HEADs, remote/branch/status, allowlisted manifest,
hash comparison, public-sync preflight, check/test/build counts, zero-secret
and zero-provider statement, and reviewer-only public commit/deploy receipts.

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: export becomes `EXPORTED` only after reviewer-owned public commit,
push, successful Netlify deploy and hosted smoke evidence exist.

## Claim Boundary

This baseline authorizes one consolidated final release repair. It does not
authorize a worker commit, push, deploy, credential read, provider call,
private-repository publication, production-readiness claim before hosted proof,
or any successor beyond R3.

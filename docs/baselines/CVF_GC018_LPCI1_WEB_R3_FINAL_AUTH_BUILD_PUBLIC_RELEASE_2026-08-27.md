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
credential meaning. Removing the accidentally admitted live `.tsx` proof
revealed real function coverage of 79.79% against the 80% gate. Do not lower
the threshold or re-admit the live proof. Add one behavioral test at
`src/components/home-surface-controls.test.tsx` covering keyboard/click and
intent-front-door handlers. The amended public manifest is exactly 36 paths. A new
candidate SHA must pass audit, build, tests, coverage, public-sync preflight and
server-side Web CI before identical-SHA promotion; `819d8acf` remains rejected.

## Reviewer Amendment 3 - Zero-Warning Server-Lint Recovery

Candidate `9373818caa33be9d424d1abaea9dbe9224281a56` passed the
exact-SHA public-sync preflight and dependency audit, but server-side Web CI
correctly stopped at `eslint --max-warnings=0` on 23 warnings across nine
cvf-web paths. Promotion of that SHA is forbidden. Local lint evidence that
reported zero errors while tolerating warnings was insufficient for the
server contract.

Keep the zero-warning server gate unchanged. Within this same terminal R3, the
reviewer may remove only the reported unused imports/directives/bindings and
replace the two lint-rejected internal `window.location.href` navigations with
the canonical Next.js router. No behavior, auth invariant, threshold, live-test
selection or runtime authorization may be weakened. The cumulative public
manifest becomes exactly 45 paths. The replacement candidate must repeat both
exact-SHA server gates before identical-SHA promotion. This correction is a
release-gate recovery, not R4 or a new roadmap.

After the zero-warning correction passed server lint, the same clean runner
exposed a dependency-install omission at build: Execution Plane declares
`cvf-control-plane-foundation` but the workflow never installs Execution Plane
dependencies. The already-authorized workflow path may add exactly one
`npm ci` step for `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` before the Web
install/build. No package, lockfile, import, runtime or manifest expansion is
authorized; the cumulative public manifest remains 45 paths.

## Reviewer Amendment 4 - Netlify Clean-Runner Dependency Install

Public SHA `32315f3dcf8d123cf1792ad14e4dd2df9ff2ada6` passed both
exact-SHA GitHub server gates and was promoted, but Netlify deploy
`6a8f4da837f87b0008019fb3` failed before publish. Public deploy metadata proves
the exact commit and error state; detailed build logs require unavailable
authenticated UI access. Source verification shows root `netlify.toml` runs
only the Web build from the Web base, while the clean GitHub runner required
the sibling foundation install sequence before that same build could resolve
Execution Plane's declared Control Plane dependency.

Treat this as a source-backed hosted build-contract omission, with the exact
Netlify error line not claimed. Add only root `netlify.toml` as public path 46
and make its build command install the five sibling packages in the already
server-proven CI order before `npm run build`. Do not alter production variables,
plugins, redirects, runtime code or package versions. The replacement SHA must
pass public-sync preflight and retain the green Web-CI ancestor, then Netlify
must publish that exact SHA before hosted smoke. This remains terminal R3, not
R4 or a new roadmap.

## Reviewer Amendment 5 - Netlify Node Runtime Alignment

Replacement public SHA `df7eb5df779c881685e4a70ac82efc319d2848f6`
passed the exact 46-path public-sync gate, while Netlify deploy
`6a8f4fcee9cb860008f7a0f1` again ended in `error` before publish. A local
reproduction using the configured Node 20 runtime failed during Learning Plane
`better-sqlite3` installation before Web compilation; the already-green local
and GitHub Web build used Node 22. This is bounded evidence for hosted build
runtime mismatch, not a claim about Netlify's unavailable exact error line.

Keep the public manifest at exactly 46 paths and change only root
`netlify.toml` from Node 20 to Node 22. Preserve the Amendment 4 build command,
base, publish path, plugin, redirects, headers, auth invariants and secrets.
Require a replacement exact SHA, public-sync PASS, successful Netlify publish
and safe hosted smoke. This remains R3 and admits no R4.

## Reviewer Amendment 6 - Netlify Monorepo Root Build

Node-aligned public SHA `a57d495c87738dafec88026f31613423aafbd72e`
passed the exact 46-path public-sync gate, while Netlify deploy
`6a8f5252174df600082fbd96` again ended in `error` before publish. Netlify's
canonical monorepo documentation states that dependency discovery and install
occur in the configured base directory before the build command, and recommends
repository-root base for monorepos. The existing Web-subdirectory base therefore
runs automatic Web dependency installation before the sibling bootstrap command.

Keep the manifest at exactly 46 paths and change only root `netlify.toml`: use
the repository root as base, express all install/build paths from that root,
explicitly install Web dependencies after the five sibling packages, and make
the publish directory the Web `.next` path relative to root. Preserve Node 22,
plugin, redirects, headers, auth invariants and secrets. If this replacement
still fails without a readable exact log, stop; do not open another speculative
amendment. This remains terminal R3 and admits no R4.

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

EXPORTED

Public remote: `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Public commit: `a0ef5923d100b02c43294815ac9d01d8db20e8b8`

Exported artifacts: exact 46-path manifest governed by this baseline. Netlify
deploy `6a8f535e6e1655000873655b` published the same SHA and hosted smoke passed.

## Claim Boundary

This baseline authorizes one consolidated final release repair. It does not
authorize a worker commit, push, deploy, credential read, provider call,
private-repository publication, production-readiness claim before hosted proof,
or any successor beyond R3.

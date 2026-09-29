# CVF GC-018 Baseline - LPCI1 Web UC-01 Public Hosted Build Composition Repair

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-26

Batch ID: LPCI1-WEB-R1-PUBLIC-HOSTED-BUILD-COMPOSITION-REPAIR

Dispatch base head: `112ae0112`

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

## Purpose

Resume the parked LPCI1 Web roadmap through one source-backed P1 repair. The
public `main` tip `9c01832930226f2f770eafa346e01279160f22cb` fails the exact
Netlify production build because the UC-01 route consumes the TypeScript
Model Gateway package through a barrel and package topology that are not safe
after installation under `node_modules`.

## Scope

One consolidated implementation repairs only the package-safe Model Gateway
entry consumed by LPCI, its Guard Contract dependency edge if required, the
cvf-web build composition, and focused regression proof. The worker operates
only in the private provenance repository. Public export, push, Netlify
deploy, provider execution, hosted smoke and production-readiness claims stay
reviewer/operator owned after private closure.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id LPCI1-WEB-R1 --title "UC-01 Public Hosted Build Composition Repair" --date 2026-08-26 --base 112ae0112 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "parked LPCI1 re-entry baseline accepted" --stdout` |
| generatedProfile | public-sync shape narrowed to private no-commit implementation before export |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact failure receipts, private-first repository boundary, package-safe acceptance rules and no-live boundary |
| checkerReadAheadConfirmation | dispatch, source verification, TPGR, public export, trace, Delta and worker-return guards reviewed |
| docOnlyNewFields | Build Failure Reproduction Matrix; Private-First Export Interlock |
| claimBoundary | dispatch authoring and read-only external verification only |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| LPCI1 parked re-entry baseline | `docs/reference/CVF_LPCI1_WEB_CURRENT_ASSESSMENT_AND_PARKED_REENTRY_BASELINE_2026-08-12.md` | RELEASED_BY_OPERATOR_REENTRY |
| target identity | operator supplied GitHub public repository, Netlify project `vibcode`, and production domain `cvfcoding.vn` | ACCEPT_AS_OPERATOR_INPUT |
| public tip | read-only `git ls-remote` returned `9c01832930226f2f770eafa346e01279160f22cb` for `refs/heads/main` | ACCEPT |
| failure reproduction | exact public-sync tip failed local `npm run build` at the Model Gateway TypeScript barrel | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Code implementation`, role=`dispatcher`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Code implementation" --role dispatcher --lifecycle-phase pre-implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | ordinary private-first implementation and independent review controls apply |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; Task Governance Routing Manifest; Public Export Disposition; Agent Operation Trace Block; Delta fields |
| gateRunPurpose | confirm packet shape after source and external-state evidence were already inspected |
| claimBoundary | checker compliance does not prove the repair or hosted readiness |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| cvf-web consumes Model Gateway as a local file dependency | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependency line 28 | `cvf-model-gateway` | cvf-web package manifest | ACCEPT |
| Model Gateway is absent from the Next transpilation allowlist | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts` | `transpilePackages`, lines 39-47 | `transpilePackages` | Next build configuration | ACCEPT |
| LPCI route imports the package root | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | import line 5 | `CredentialBoundary` | LPCI query route | ACCEPT |
| LPCI provider binding imports the package root | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts` | import lines 1-16 | `ProviderExecutionBridge` | LPCI provider binding | ACCEPT |
| package root exports unrelated monorepo-relative owners | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | lines 1-51 | `SkillAdapter` | Model Gateway root barrel | ACCEPT |
| receipt owner also uses a monorepo-relative Guard Contract path | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | lines 3-5 | `createReceiptEnvelope` | Gateway receipt builder | ACCEPT |
| production target serves through Netlify | external observation | canonical operator-provided target metadata and screenshot | operator message dated 2026-08-26 plus HTTP 200 and `Server: Netlify` | `cvfcoding.vn/landing` | target metadata | ACCEPT |

## Build Failure Reproduction Matrix

| Probe | Observed result | Interpretation |
| --- | --- | --- |
| exact public tip without source edits | Webpack parse failure at `node_modules/cvf-model-gateway/src/index.ts` | Model Gateway is not transpiled |
| temporary transpile allowlist addition | parse failure cleared; five monorepo-relative module-resolution failures surfaced | transpilation alone is insufficient |
| temporary files after probe | public-sync clone restored clean | no diagnostic edit retained |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact R1 baseline/work-order/return paths | absent before authoring | PASS |
| target identity search | no committed site ID or URL existed before operator input | ACCEPT_OPERATOR_INPUT_REQUIRED |
| collision decision | no existing LPCI1 hosted build-composition repair packet exists | CREATE_NEW |

## Decision / Baseline / Proposed Tranche

Decision: `CONTINUE_HIGH_VALUE`. Severity is P1 because public `main` cannot
produce the production artifact while Netlify serves an older successful
deploy. The root cause is independent from TPGR and from R1E delegation
authority. Marginal value is observed: restoring buildability is required
before any trustworthy hosted smoke. Consolidate packaging, Web composition
and regression proof into this single tranche; do not open a design tranche.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | private Model Gateway and cvf-web source owners | exact no-commit local repair; no external effect | reproduced deterministic build failure | package-safe LPCI entry only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP consumer in this repair | no ingress, authentication, mutation or public claim | no matching consumer required | deferred; no adapter implementation | N/A_WITH_REASON |

## Evidence / Verification

Worker evidence must include focused Model Gateway/cvf-web tests, TypeScript,
the exact production build, final diff/status, and the worker-return fast gate.
No provider key or live call is needed to prove compilation.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: named local source repair, not external absorption.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - exact named package/build paths only.

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON: the public clone is a governed projection target,
not an external knowledge corpus.

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: private implementation and review must close before a separately
verified public-sync commit and push may trigger Netlify.

## Claim Boundary

This baseline authorizes one private, no-commit implementation worker. It does
not authorize worker commit, public-sync mutation, push, Netlify deploy,
provider execution, hosted smoke, secret access or production-readiness claim.

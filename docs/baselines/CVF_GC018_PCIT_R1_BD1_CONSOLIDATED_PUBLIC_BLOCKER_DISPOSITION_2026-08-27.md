# CVF GC-018 Baseline - PCIT-R1-BD1 Consolidated Public Blocker Disposition

Memory class: governed-dispatch-baseline

Status: APPROVED_FOR_EXECUTION

Batch ID: PCIT-R1-BD1

Dispatch base head: `47260a08d9`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: independent orchestrator/reviewer

Worker target: one no-commit public test-repair and blocker-disposition worker

## Purpose

Use one bounded same-roadmap packet to repair two source-verified public test
drifts and produce a non-destructive disposition for the skill-registry
failure observed in exact hosted run `33042997497`. This is not PCIT-R2 and
does not authorize registry regeneration, product changes or external effects.

## Decision / Baseline

Operator approved one consolidated blocker-disposition packet on 2026-08-27.
The private dispatch base is `47260a08d9`; the public candidate base is
`bbea31745`; PR `#4` remains unmerged. The worker may change at most three
named public test surfaces and one named private return.

## Evidence / Verification

Exact hosted evidence shows 61 passed and four failed Python unit tests, plus
one runtime-page failure after 3454 passed and 43 skipped Web tests. Local
source inspection identifies placeholder exception assertions, one fixture
wording mismatch and an async assertion race. Registry validation reports 335
user records against 62 source skills and 344 errors; its cleanup helper deletes
all user records, so bulk reconciliation lacks bounded write authority here.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id PCIT-R1-BD1 --title "Consolidated Public Blocker Disposition" --date 2026-08-27 --base 47260a08d9 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | public-sync plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact PCIT evidence, capped ownership and registry safety boundary |
| checkerReadAheadConfirmation | dispatch-quality, governed-artifact, task-route, public-disposition and scaffold-provenance checkers |
| docOnlyNewFields | finding-family disposition matrix; destructive registry boundary |
| claimBoundary | authoring provenance only; no repair, hosted success or public export claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| PCIT-R1-SA1 independent review | private evidence commit `06643ac4b`; continuity `1e671171b`; exact-anchor repair `47260a08d9` | operator approves one bounded disposition packet | RELEASED_BY_OPERATOR |
| public candidate | branch commit `bbea31745`; PR `#4` unmerged | remain local and uncommitted during worker execution | RELEASED_READ_ONLY_BASE |
| registry ownership | validator, generator and destructive cleaner inspected | no registry write until canonical lifecycle is proven | HELD_READ_ONLY |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| three Python exception tests are placeholders | test drift | `EXTENSIONS/CVF_v1.3_IMPLEMENTATION_TOOLKIT/sdk/tests/unit/test_skill_contract.py` | lines 60, 70, 78 | `pytest.raises(Exception)` with empty body | SDK unit tests | ACCEPT |
| rollback assertion conflicts with fixture wording | fixture/test drift | `EXTENSIONS/CVF_v1.3_IMPLEMENTATION_TOOLKIT/sdk/tests/conftest.py` | line 122 | `ROLLBACK_POSSIBILITY` | SDK test fixture | ACCEPT |
| runtime boundary assertion can run before snapshot render | hosted nondeterminism | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/runtime/page.test.tsx` | lines 109-116 | Vietnamese render test | Testing Library async query | ACCEPT |
| registry cleanup is unbounded for this packet | destructive owner boundary | `governance/skill-library/registry/clean_user_registry.py` | lines 26-40 | all `USR-*.gov.md` plus index deletion | user registry lifecycle helper | ACCEPT |
| validator expects registry/source parity | genuine corpus reconciliation debt | `governance/skill-library/registry/validate_registry.py` | lines 148-154 | user registry count check | skill registry validator | ACCEPT |

## Negative Search And Collision Discipline

Both named PCIT-R1-BD1 artifact paths were absent before authoring. Exact token
search found no competing BD1 authority. The packet remains under PCIT-R1 and
does not create or imply R2.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`public-sync`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_authoring.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | source table columns, dispatch status, exact ownership, return contract and public disposition |
| gateRunPurpose | confirm the bounded packet after source verification |
| claimBoundary | checker conformance does not prove implementation or hosted success |

## Current Runtime Freshness Verification

N/A with reason: this dispatch uses current hosted CI receipts only to bound
test ownership. It claims no live runtime, provider readiness or deployment
state and authorizes no external invocation.

## Public/Provenance Boundary

Private provenance owns authority and the worker return. The sibling public
clone owns only the three allowlisted test candidates. No commit, push, merge,
deployment, secret access or hosted rerun is worker-authorized.

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: no accepted local candidate or exact-SHA hosted proof exists for this
packet, and the registry blocker remains subject to bounded disposition.

## Claim Boundary

This baseline authorizes one no-commit worker pass over two small test-drift
families and a read-only registry disposition. It does not authorize product
source, workflow, validator, registry, generator, dependency or external-state
changes, and it does not authorize a successor roadmap.

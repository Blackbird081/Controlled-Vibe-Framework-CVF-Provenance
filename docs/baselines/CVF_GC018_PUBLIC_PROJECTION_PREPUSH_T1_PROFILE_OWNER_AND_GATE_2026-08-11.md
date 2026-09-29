# CVF GC-018 Baseline - Public Projection Pre-Push T1 Profile Owner And Gate

Memory class: FULL_RECORD

Status: READY_FOR_DISPATCH

docType: baseline

Date: 2026-08-11

Batch ID: PUBLIC-PROJECTION-PREPUSH-T1

dispatchBaseHead: `5a25a3328bcc5016eac41c1fe712989447bbe791`

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Reopen the accepted `BLOCKED_NO_OWNER` public-projection pre-push finding with
an operator-nominated stable owner, implement a narrow provenance-owned gate,
and prove whether public candidate `021f8b852afc245a6383177dd69bf56caf488b02`
may proceed to a later push tranche without running private-only checks inside
the public clone.

## Scope / Target / Owner Boundary

Stable owner role: Public Projection Release Steward, fulfilled by the
reviewer/closer lane.

Stable owner paths:

- `docs/reference/CVF_PUBLIC_PROJECTION_PRE_PUSH_PROFILE_STANDARD_2026-08-11.md`
- `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json`
- `governance/compat/run_public_projection_pre_push_gate.py`
- `governance/compat/test_run_public_projection_pre_push_gate.py`

The standard owns classification and gate-versus-report policy. The JSON owns
machine-readable classification and pinned inherited-debt expectations. The
runner owns deterministic evaluation. The test owns fail-closed regression
coverage. The worker return is
`docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md`.

## Source / Predecessor Evidence

- `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T0_OWNER_FEASIBILITY_AUDIT_COMPLETION_2026-08-06.md` records `BLOCKED_NO_OWNER` and its three-part reopen condition.
- `docs/audits/CVF_PUBLIC_PROJECTION_PREPUSH_T0_OWNER_FEASIBILITY_AUDIT_2026-08-06.md` records 99 generic checks, 73 private-owned checks, and four confirmed public-relevant defect families.
- `governance/compat/local_governance_hook_catalog_pre_push.py` is the generic private-provenance pre-push catalog and is not the new public profile owner.
- `scripts/cvf-public-sync.ps1` and `scripts/cvf_projection_policy.json` remain the public projection selection and leakage controls.
- Public clone remote is `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`; clean branch `lpci1-ref-staging` is at candidate `021f8b852` and remote branch is absent as of dispatch evidence.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | source verification columns, protected-path authorization, operation trace fields, bounded claim vocabulary, public disposition enum |
| gateRunPurpose | confirm source-backed dispatch shape after owner and policy boundaries were selected; not first discovery |
| claimBoundary | dispatch authority only; no push/deploy claim |

## Dependency Release Evidence

The operator delegated orchestrator/reviewer decision authority and instructed
`next`. That instruction nominates the Public Projection Release Steward role
for this bounded lane. T0's remaining reopen requirements are assigned to the
standard, policy JSON, runner, and independent review in this tranche.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024,
ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

Dispatch impact: source-backed ownership, exact protected paths, tested command
signature, bounded public-root input, and no worker commit.

## Large-Scope Change Authorization

AUTHORIZED_EXACT_INHERITED_PUBLIC_RANGE: the future profile may evaluate the
already-committed exact 41-path public range
`2103a38fda01ee827e9fc6c3be38a824fa5d54ad..021f8b852afc245a6383177dd69bf56caf488b02`.
This authorization does not permit the T1 worker to edit the public clone and
does not waive manifest, leakage, build, or regression checks.

## Required Semantic Delta

The profile must:

1. validate explicit public-root containment, exact public remote, clean
   worktree, branch, base, head, and non-empty range;
2. load a versioned policy registry, reject unknown/missing classifications,
   and separate `PUBLIC_OWNED` from `PRIVATE_OWNED` checks;
3. treat the four T0 public-relevant defect families as gates for new/worsened
   debt and as reports only when exactly pinned inherited debt is unchanged;
4. validate the authorized 41-path manifest and fail on any extra, missing,
   deleted, renamed, or unclassified path;
5. run public projection/leakage proof, diff checks, and explicitly configured
   package test/type/lint/build commands without secrets or network install;
6. emit deterministic JSON plus human-readable summary and nonzero exit on any
   gate failure.

## Forbidden Scope

No edit to generic pre-push catalogs or weakening of private gates. No public
clone edit, commit, push, deploy, Netlify action, secret read, network install,
public `main`, production promotion, or unrelated source change.

## Verification Contract

- focused pytest for the new runner;
- runner `--help` and policy schema validation;
- negative tests for wrong remote, dirty tree, wrong head, manifest drift,
  unclassified check, worsened inherited debt, missing command, and command
  failure;
- positive fixture proving exact pinned inherited debt can report without
  waiving new regressions;
- existing Core reviewer-fast and pre-closure gates.

## Acceptance Criteria

- AC-01: all three T0 reopen conditions have explicit owners and machine evidence.
- AC-02: generic private gate remains unchanged.
- AC-03: exact 41-path candidate is represented by deterministic policy data.
- AC-04: four confirmed public defect families have pinned gate/report rules.
- AC-05: profile fails closed for every negative case above.
- AC-06: worker changes only the four owner paths plus worker return.
- AC-07: no public, remote, provider, or deployment effect occurs.

## Decision / Baseline / Proposed Tranche

Decision: PROCEED_PUBLIC_PROFILE_IMPLEMENTATION.

This is the owner-and-policy implementation tranche required by T0. Successful
closure permits a separate push-readiness rerun; it does not itself authorize
push or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: provenance-owned gate authority and implementation only.

## Claim Boundary

This baseline authorizes a local provenance-owned public-projection gate and
tests. It makes no claim of push, deploy, hosted behavior, production
readiness, or public export.

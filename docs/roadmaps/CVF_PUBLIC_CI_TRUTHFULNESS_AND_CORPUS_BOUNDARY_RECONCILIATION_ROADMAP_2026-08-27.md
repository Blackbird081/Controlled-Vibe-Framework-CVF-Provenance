# CVF Public CI Truthfulness And Corpus Boundary Reconciliation Roadmap

Memory class: governed-roadmap

Status: PCIT_R1_DISPATCH_READY_SINGLE_TRANCHE_CAP

Date: 2026-08-27

## Purpose

Make the public repository's always-on CI report the public product corpus
truthfully. Remove private-provenance assumptions from public checks, repair
workflow-only dependency/bootstrap drift, and preserve real product failures
instead of hiding them behind false governance failures.

## Authorization / Decision

The operator selected the next roadmap after terminal LPCI1 Web R3 closure and
authorized one fresh high-value lane. This roadmap admits exactly one
no-commit implementation return, PCIT-R1. There is no automatic R2.

## Current Evidence

At exact public commit `a0ef5923d100b02c43294815ac9d01d8db20e8b8`:

- Public Sync Preflight run `33013062735` and CVF Public Surface run
  `33013062743` passed.
- CVF CI Pipeline run `33013062792` failed before Web tests because
  `.github/workflows/ci.yml` invoked the private
  `run_local_governance_hook_chain.py --hook pre-commit` contract.
- The failed hook named absent public-corpus paths including
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`, private completion artifacts and
  private corpus registries. This is a public/private corpus mismatch, not a
  Web test result.
- CVF CI run `33013062759` and CVF Static CI Gate run `33013062933` exposed
  additional stale bootstrap, typecheck, test and static-gate outcomes. Their
  jobs must be classified independently; no green result may be manufactured
  by suppressing a genuine product defect.
- The public repository already owns dedicated public-safe checks:
  `.github/workflows/public-sync-preflight.yml` and
  `.github/workflows/public-surface.yml`.

## Scope / Target / Owner Boundary

Target: the always-on public GitHub Actions topology and the static runner it
directly invokes.

One bounded worker may edit only these public-sync paths:

- `.github/workflows/ci.yml`
- `.github/workflows/cvf-ci.yml`
- `.github/workflows/cvf-static-ci.yml`
- `.github/workflows/cvf-web-ci.yml`
- `scripts/run_cvf_static_ci_gate.py`
- `scripts/test_run_cvf_static_ci_gate.py` if a focused regression test is
  required

The private worker may create only its named worker return. Product/runtime
source, package versions, lockfiles, private governance checkers and generated
aggregates are outside ownership.

## Design Control Gate

PCIT-R1 must classify each failing always-on job as exactly one of:

1. `PUBLIC_PRIVATE_CORPUS_MISMATCH`;
2. `WORKFLOW_BOOTSTRAP_DRIFT`;
3. `DUPLICATE_OR_STALE_WORKFLOW`;
4. `GENUINE_PRODUCT_DEFECT`;
5. `NOT_REPRODUCED_WITH_EVIDENCE`.

For the first three, the worker may make the smallest workflow/runner repair
inside the allowlist. A genuine product defect must remain visible and be
returned as a named blocker; it must not be skipped, marked non-blocking, or
converted into a passing job. A non-reproduced result needs exact command and
SHA evidence.

## Tranche Value Admission

| Factor | Evidence-backed decision |
| --- | --- |
| outcome consumer | public repository users and maintainers who rely on CI status |
| severity | P1 because every recent public main push is red and later product jobs are masked |
| finding evidence | OBSERVED at three exact GitHub runs on the published SHA |
| root cause | independent public/private corpus and workflow-bootstrap contract drift |
| marginal value | OBSERVED: restore trustworthy release feedback without changing product behavior |
| cost ceiling | one worker return, workflow/runner-only cluster, zero provider calls |
| stop condition | stop on any required product source, dependency upgrade, secret, deploy or second tranche |
| disposition | CONTINUE_HIGH_VALUE as one consolidated PCIT-R1 |

The accepted TPGR value record is not declared here because its current
standard scopes the machine record first to remediation/finding repair and
requires separately accepted extension evidence for app/project delivery.
This roadmap applies the same cost discipline manually without claiming a new
machine-governed task class.

## Work Plan

PCIT-R1 performs one sequence: capture exact public state; reproduce or inspect
every red always-on job; build a coverage/ownership matrix; apply the minimal
allowlisted correction; run local focused proof and public-sync preflight; and
return uncommitted evidence for independent review. The reviewer alone may
commit, push and evaluate exact-SHA server runs.

## Acceptance Criteria

- No always-on public job invokes a checker that requires private-only corpus.
- Workflow bootstrap steps match the package dependencies actually required by
  their named jobs.
- Dedicated public-safe checks remain enabled.
- Duplicate or stale workflows are either repaired or removed from automatic
  triggers only after their useful coverage is mapped to an active owner.
- Genuine product failures remain blocking and visible.
- No product source, dependency version, lockfile, threshold, auth behavior,
  provider behavior or Netlify configuration changes.
- Worker leaves both repositories uncommitted with empty staging areas.
- Independent reviewer decides any commit/push and requires exact-SHA GitHub
  results before closure.

## Verification / Evidence

Required worker evidence includes public/private HEAD and status, remotes,
current workflow inventory, exact run/job URLs or IDs, failure classification,
before/after command results, focused runner tests if changed, YAML parse or
GitHub workflow validation, public-sync preflight, and an exact changed-file
manifest.

## Non-Goals

No dependency modernization, package or lockfile edit, application/runtime
repair, provider/live call, OAuth exercise, secret read, Netlify change,
private-history export, broad governance redesign, or automatic successor.

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: this roadmap is private dispatch authority. Any accepted workflow or
runner delta must be committed and pushed separately from the public-sync
clone by the independent reviewer before an `EXPORTED` claim exists.

## Next Allowed Move

Execute exactly PCIT-R1 under the paired GC-018 baseline and work order. On
return, independently review the evidence. Close the roadmap after one accepted
public candidate or one honest blocker. Do not create R2 unless a fresh
operator decision cites a distinct source-backed P0/P1 product defect and its
incremental value.

## Claim Boundary

This roadmap authorizes one no-commit public CI reconciliation candidate. It
does not authorize commit, push, deployment, provider/live use, secret access,
product-source repair, dependency upgrade, CI weakening, or a claim that the
current public CI is green.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_governed_artifact_authoring.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | real section headings, public disposition token, task manifest boundary |
| gateRunPurpose | confirm governed roadmap shape after source review |
| claimBoundary | structural conformance does not prove CI repair or hosted results |


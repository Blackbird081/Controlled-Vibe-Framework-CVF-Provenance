# CVF Public CI Truthfulness And Corpus Boundary Reconciliation Roadmap

Memory class: governed-roadmap

Status: ROADMAP_CLOSED_PASS_BOUNDED_REGISTRY_DEBT_PARKED

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

Disposition: `EXPORTED`
Public-sync remote: `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`
Public-sync branch: `pcit-r1-public-ci-truthfulness`
Public-sync commits: `bbea31745`, `94732b6f`, `8b9c4a67`, `86b1e728`
Public artifact paths: public workflows/bootstrap repairs, two bounded test
repairs and two Python 3.9 compatibility repairs recorded by the PCIT worker
return. Public catalog paths: N/A with reason: CI truthfulness has no catalog
surface. PR `#4` remains open and unmerged on separately parked registry debt.

## Next Allowed Move

PCIT-R1 and BD1 are closed bounded at private evidence commit `8480ed51f` and
public exact-SHA candidate `86b1e728`. The two test-drift families, Web/build
proof and Python 3.9 compatibility defect are closed. Registry validation
remains truthfully red and is transferred, without automatic continuation, to
the separately selected PSRR-R1 roadmap. There is no PCIT-R2.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_PCIT_R1_BD1_CONSOLIDATED_PUBLIC_BLOCKER_DISPOSITION_2026-08-27.md` | dispatch status plus terminal reviewer return | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_PCIT_R1_BD1_CONSOLIDATED_PUBLIC_BLOCKER_DISPOSITION_WORKER_RETURN_2026-08-27.md` | final disposition and exact hosted table | PASS |
| Roadmap state | this roadmap | `Status: ROADMAP_CLOSED_PASS_BOUNDED_REGISTRY_DEBT_PARKED` | PASS |
| Registry JSON | N/A with reason: PCIT changed no JSON registry | blocked until PSRR-R1 resolves the generated registry family | BLOCKED with reason: no applicable PCIT JSON registry owner |
| Registry Markdown | `governance/skill-library/registry/user-skills/INDEX.md` | mutation transferred to separately authorized PSRR-R1 | BLOCKED with reason: 335/62 generated-registry debt remains outside PCIT |
| External evidence digest | N/A with reason: GitHub run/job IDs are recorded directly in the reviewer artifact | no separate digest required | N/A with reason |
| System loop interlock | N/A with reason: PCIT changed no system-loop contract | no interlock mutation | N/A with reason |
| Session continuity | `CVF_SESSION/state/entries/pcitR1PublicCiTruthfulnessDispatched20260827.json` | closure status and parked registry disposition | PASS |

## Claim Boundary

This roadmap records bounded public CI reconciliation and exact-SHA proof. It
does not claim the aggregate Documentation & Testing workflow is green: its
registry family remains truthfully red and transfers only through separately
authorized PSRR-R1. No merge, deploy, provider/live, secret, CI weakening or
automatic PCIT successor is authorized.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_governed_artifact_authoring.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | real section headings, public disposition token, task manifest boundary |
| gateRunPurpose | confirm governed roadmap shape after source review |
| claimBoundary | structural conformance does not prove CI repair or hosted results |


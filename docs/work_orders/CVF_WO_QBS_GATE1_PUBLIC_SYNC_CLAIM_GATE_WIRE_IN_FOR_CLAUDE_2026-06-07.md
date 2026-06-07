# CVF WO QBS-GATE1 Public-Sync Claim Gate Wire-In For Claude

Memory class: WORK_ORDER

docType: work_order

Status: READY_FOR_DISPATCH

Date: 2026-06-07

dispatchBaseHead: `9676ae37`

executionBaseHead: `9676ae37`

closureBaseHead: `9676ae37`

publicSyncBaseHead: `7d33a5887`

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Wire the QBS claim gate into the public-sync repository so future public QBS
benchmark artifacts cannot bypass reviewer-agreement, corpus-power,
no-parity, or calibration-anchor boundaries.

## Scope / Target / Owner Boundary

Target repository:

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`

Primary target surfaces:

- public-sync `governance/compat/check_qbs_claim_gate.py`;
- public-sync `governance/compat/run_local_governance_hook_chain.py`;
- public-sync `.github/workflows/documentation-testing.yml`;
- focused checker fixtures/tests if a local pattern exists, otherwise a small
  self-test block in the checker or dedicated lightweight test script;
- public-sync completion evidence recorded back in this provenance repo by
  reviewer/closer only.

Boundary:

- This is a guard wire-in tranche, not a benchmark rerun.
- Do not change QBS methodology, claim ladder, corpus, reviewer scores, scored
  run outputs, provider scripts, or live execution behavior except where a
  fixture/test artifact is needed to prove the checker.
- Do not push public-sync unless the operator explicitly asks after review.

## Claim / Final / Verification Boundary

Final claim may state only that the public-sync repository now runs the QBS
claim gate locally and in documentation CI against public QBS benchmark
artifacts. It may not claim output-quality parity, L4/L5 score, family-level
power, live benchmark evidence, hosted readiness, production readiness, or
public release readiness.

## 0. Surface Fidelity Gate

This work order is source-verified against current provenance and public-sync
owner files. Claude must not treat provenance-only default scans as sufficient,
because the provenance repository currently has no `docs/benchmark` tree.

## 1. Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-07 "commit đi, viết workorder cho claude thi công" | ACCEPT |
| QBS method remediation closure | `docs/reviews/CVF_QBS_METHOD_RELIABILITY_REMEDIATION_COMPLETION_2026-06-07.md` | ACCEPT |
| QBS claim gate fix commit | private commit `9676ae37` | ACCEPT |
| Public-sync QBS remediation commit | public-sync commit `7d33a5887` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V16_2026-06-06.md` | ACCEPT |

## 2. Transfer Objective

Implement QBS-GATE1 by moving the accepted `check_qbs_claim_gate.py` behavior
onto the public-sync execution surface and wiring it into public-sync local
hook and documentation CI paths. The implementation must fail closed for future
QBS scored-run artifacts missing `calibration_anchor_ref`, while preserving
pre-standard legacy behavior based on source-visible dates.

## 3. Source Packet

### Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Provenance QBS checker declares QBS claim-boundary enforcement | EXISTS | `governance/compat/check_qbs_claim_gate.py` | lines 1-20 | `CVF QBS Claim Gate Checker` | QBS claim gate checker | ACCEPT |
| QBS kappa thresholds are declared in the checker | VALUE_SET | `governance/compat/check_qbs_claim_gate.py` | lines 35-36 | `KAPPA_PASS_GATE` / `KAPPA_DIRECTIONAL_GATE` | QBS claim gate checker | ACCEPT |
| Checker extracts run dates from started/completed/scored/produced/id fields | RUNTIME_BEHAVIOR | `governance/compat/check_qbs_claim_gate.py` | lines 72-97 | `_extract_run_date` | QBS claim gate checker | ACCEPT |
| Checker fails closed for missing anchor on/after cutoff or unknown date | RUNTIME_BEHAVIOR | `governance/compat/check_qbs_claim_gate.py` | lines 221-244 | `CALIBRATION_ANCHOR_MISSING` / `CALIBRATION_ANCHOR_MISSING_OR_DATE_UNKNOWN` | QBS claim gate checker | ACCEPT |
| Provenance local hook chain owns `pre-commit` guard list | EXISTS | `governance/compat/run_local_governance_hook_chain.py` | lines 24-45 | `HOOK_CHAINS["pre-commit"]` | local governance hook chain | ACCEPT |
| Provenance local hook chain owns `pre-push` guard list | EXISTS | `governance/compat/run_local_governance_hook_chain.py` | lines 181-270 | `HOOK_CHAINS["pre-push"]` | local governance hook chain | ACCEPT |
| Provenance autorun common phase gates are separate from local pre-push chain | EXISTS | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 50-196 | `_common_commands` | agent autorun workflow gate | ACCEPT |
| Provenance pre-push autorun calls the local pre-push hook chain | EXISTS | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 198-203, 286-288 | `PRE_PUSH_COMMANDS` / `commands.extend(PRE_PUSH_COMMANDS)` | agent autorun workflow gate | ACCEPT |
| Public-sync local hook chain owns pre-commit/pre-push lists | EXISTS | `../Controlled-Vibe-Framework-CVF-public-sync/governance/compat/run_local_governance_hook_chain.py` | lines 21-48 and 48-211 | `HOOK_CHAINS` | public-sync local governance hook chain | ACCEPT |
| Public-sync documentation workflow triggers on governance/compat and docs changes | EXISTS | `../Controlled-Vibe-Framework-CVF-public-sync/.github/workflows/documentation-testing.yml` | lines 3-18 | `on.push.paths` | public-sync documentation CI | ACCEPT |
| Public-sync documentation workflow status check aggregates named jobs | EXISTS | `../Controlled-Vibe-Framework-CVF-public-sync/.github/workflows/documentation-testing.yml` | lines 895-898 | `Status Check` | public-sync documentation CI | ACCEPT |

### New Runtime Fields

None. QBS-GATE1 is guard/CI wiring only.

### Observed Pre-Dispatch Boundary Checks

| Observation | Command / evidence | Disposition |
| --- | --- | --- |
| Public-sync repository is the public target | `git remote -v` in public-sync returned `origin https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` | ACCEPT |
| Public-sync contains QBS public benchmark run artifacts | `Test-Path docs/benchmark/runs` in public-sync returned `True` | ACCEPT |
| Public-sync does not currently contain `check_qbs_claim_gate.py` | `Test-Path governance/compat/check_qbs_claim_gate.py` in public-sync returned `False` | GAP_TO_CLOSE |
| Provenance repository has no local `docs/benchmark` tree | `Test-Path docs/benchmark` in provenance returned `False` | BLOCK_AS_EVIDENCE |

## 4. Current Runtime Freshness Verification

| Surface | Freshness check | Disposition |
| --- | --- | --- |
| Public-sync QBS artifact tree | `docs/benchmark/runs` exists in public-sync | PASS |
| Public-sync checker file | `governance/compat/check_qbs_claim_gate.py` does not currently exist in public-sync | GAP_TO_CLOSE |
| Public-sync hook chain | No `check_qbs_claim_gate.py` command is currently wired | GAP_TO_CLOSE |
| Public-sync docs CI | No QBS claim gate job is currently present | GAP_TO_CLOSE |
| Provenance-only default scan | Provenance lacks `docs/benchmark`; default checker scan would be 0 artifacts | BLOCK_AS_EVIDENCE |

## 5. Role Assignment

Claude acts as worker/implementer only.

Codex or another reviewer must review and close. Claude must not mark the
work order closed, push public-sync, or update session continuity without
reviewer authority.

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Orchestrator | Codex | This work order, source fidelity, claim boundary |
| Worker | Claude | Implement public-sync checker/hook/CI wiring and tests |
| Reviewer | Codex or assigned reviewer | Verify false-negative fixtures and public/provenance boundary |
| Closer | Codex or assigned closer | Completion packet, session state, public-sync push if later authorized |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V16_2026-06-06.md`
- `docs/work_orders/CVF_WO_QBS_METHOD_RELIABILITY_REMEDIATION_2026-06-06.md`
- `docs/reviews/CVF_QBS_METHOD_RELIABILITY_REMEDIATION_COMPLETION_2026-06-07.md`
- `governance/compat/check_qbs_claim_gate.py`
- public-sync `governance/compat/run_local_governance_hook_chain.py`
- public-sync `.github/workflows/documentation-testing.yml`

## Pre-Flight Checks

Run before edits:

```powershell
git status --short
git rev-parse --short HEAD
git -C "d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" status --short
git -C "d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" remote -v
git -C "d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" rev-parse --short HEAD
```

The public-sync remote must be:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

## Worker Autonomy / No-Question Rule

Claude owns all guard conformance, fixture repair, and local gate remediation
inside the allowed public-sync scope. Claude must stop and return to
orchestrator if the work requires live provider calls, benchmark reruns,
public push, secrets, package installation, or changes outside allowed scope.

## Write Ownership

Allowed in public-sync:

- `governance/compat/check_qbs_claim_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `.github/workflows/documentation-testing.yml`
- focused QBS checker test/fixture file if needed under an existing suitable
  test or governance path

Allowed in provenance only for reviewer/closer, not Claude worker unless
explicitly reassigned:

- completion review for QBS-GATE1;
- active session state/handoff sync after review.

Forbidden:

- modifying QBS scored run results or historical benchmark artifacts;
- modifying QBS methodology/claim ladder unless the checker cannot be wired
  without a clarifying note;
- live/provider calls or QBS reruns;
- public-sync push;
- package/lockfile edits;
- secrets or `.env*`;
- provenance public repo push.

## Execution Plan

1. Copy or port the accepted QBS checker behavior into public-sync.
2. Add fixture coverage proving:
   - future `run-manifest.json` with `started_at >= 2026-06-07` and no
     `calibration_anchor_ref` fails;
   - future `aggregate-results.json` with date embedded in `run_id` and no
     `calibration_anchor_ref` fails;
   - date-unknown scored result fails closed;
   - pre-standard dated legacy result passes;
   - future result with `calibration_anchor_ref` passes.
3. Wire the checker into public-sync local hook chain:
   - pre-commit, if performance remains acceptable;
   - pre-push at minimum.
4. Wire the checker into public-sync documentation CI with a named job and add
   it to the status aggregation if the workflow uses explicit `needs`.
5. Run public-sync checker scan against `docs/benchmark`.
6. Run public-sync local hook chain or the focused subset needed to prove the
   new hook entry.
7. Record changed files, commands, and claim boundary for reviewer.

## Evidence Requirements

Claude must provide:

- public-sync `git remote -v` output;
- public-sync `git diff --name-status`;
- checker fixture command output showing expected FAIL/PASS cases;
- `python governance/compat/check_qbs_claim_gate.py --scan-dir docs/benchmark --enforce` output from public-sync;
- local hook chain proof from public-sync:
  `python governance/compat/run_local_governance_hook_chain.py --hook pre-push`
  or a justified focused subset if the full chain is too broad;
- CI YAML diff showing the QBS job and status aggregation entry.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Public-sync has `check_qbs_claim_gate.py` | PASS |
| Public-sync checker scans `docs/benchmark` and reports >0 artifacts | PASS |
| Future missing-anchor manifest fails | PASS |
| Future missing-anchor aggregate result fails | PASS |
| Date-unknown scored result fails closed | PASS |
| Pre-standard legacy result remains allowed | PASS |
| Future anchored result passes | PASS |
| Public-sync hook chain includes QBS claim gate | PASS |
| Documentation CI includes QBS claim gate job | PASS |
| No benchmark results, methodology, provider scripts, package files, or secrets changed | PASS |

## Review Gate

Reviewer must reject closure if:

- the checker passes 0 artifacts in public-sync;
- hook/CI calls the checker only in provenance where `docs/benchmark` is absent;
- fixture coverage omits either `started_at` or `run_id` date extraction;
- future date-unknown scored result passes;
- QBS methodology or historical benchmark outputs are edited without explicit
  scope expansion;
- public-sync remote is not the public CVF repository.

## Return Conditions

Return to orchestrator if:

- public-sync lacks the expected hook/CI owner files;
- CI job wiring needs workflow restructuring beyond adding one job and status
  dependency;
- checker false positives require changing current public QBS artifacts;
- public-sync push is requested;
- live benchmark or provider proof is needed.

## operator.checkpoint.waiver

Required before public-sync push, live/provider calls, QBS rerun, package
installation, methodology changes, historical result mutation, or any claim of
QBS quality score / L4 / L5 / parity.

## Closure Checklist

- [ ] Public-sync remote verified.
- [ ] Public-sync checker added.
- [ ] Fixture false-negative tests passed.
- [ ] Public-sync `docs/benchmark` scan passed with nonzero artifact count.
- [ ] Local hook chain wired and verified.
- [ ] Documentation CI wired and status aggregation updated.
- [ ] No benchmark/historical result mutation.
- [ ] Reviewer completion packet filed.

## Public Export Disposition

Expected final disposition: `EXPORTED` only if the public-sync commit is made
and reviewer records public remote, commit, and changed artifact paths.

If reviewer does not push public-sync, final disposition must be
`BLOCKED_MISSING_PUBLIC_ARTIFACTS` or `DEFERRED_PRIVATE_ONLY` with next action.

## Claim Boundary

QBS-GATE1 is a public-sync guard wire-in. It does not claim QBS output-quality
parity, L4/L5 quality uplift, family-level power, benchmark rerun evidence,
provider behavior, hosted readiness, production readiness, public readiness, or
release readiness.

# CVF GC-018 Baseline - SCEC-T1-R1 Mixed-Fence Active-Block Parser Hardening

Memory class: governed-dispatch-baseline

Status: APPROVED_FOR_EXECUTION

Batch ID: SCEC_T1_R1_MIXED_FENCE_ACTIVE_BLOCK_PARSER_HARDENING

Dispatch base head: `8b5ae0d144c498cbaf492ec21352c947568a2a56`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: Codex orchestrator/reviewer

Worker target: one external governance implementation worker

## Purpose

Repair one fail-closed SCEC parser defect discovered by the first real
effectiveness-packet authoring attempt. A valid active SCEC JSON block is
silently missed when an earlier non-JSON fenced block causes the current regex
to pair a closing fence with a later fence boundary.

## Root Problem

`CODE_FENCE_JSON_RE` matches any line beginning with three backticks followed
by optional `json` and whitespace. A closing fence therefore also satisfies
the opening pattern. With an earlier `powershell` block, the regex consumes
the document in the wrong fence pairs and `find_active_blocks()` returns zero
for a later valid SCEC JSON block. The required-work-order gate then reports a
false `MISSING_REQUIRED_SCEC_BLOCK` violation.

This is a foundation effectiveness failure, not a packet-format error to work
around. The parser must recognize opening fences structurally and ignore
closing fences as starts.

## Accepted Authority

- Operator direction: harden the CVF foundation whenever successor tranches
  expose an effectiveness gap.
- SCEC-T1 material closure:
  `bd4ac2882482a9c38c4e8b97d1cae265028c4368`.
- SCEC-T1 continuity closure:
  `8b5ae0d144c498cbaf492ec21352c947568a2a56`.
- Active standard:
  `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`.
- Direct reproducer: a governed work order containing a `powershell` fence
  before one valid SCEC JSON fence produced `find_active_blocks(...) == []`.

## Decision / Baseline

1. Repair only active fenced-JSON discovery; do not change SCEC semantic
   validation, counters, thresholds, progression vocabulary, or activation
   boundary.
2. Add regression coverage for mixed fenced blocks before and after the SCEC
   block, including opening language tags and ordinary closing fences.
3. Preserve quoted/example-marker immunity and malformed-block fail-closed
   behavior.
4. Record the discovered defect and prevention in ADIF-0055.
5. Do not resume SCEC-E1 effectiveness reconciliation until this repair is
   independently reviewed and committed.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Fence extraction uses one regex over raw markdown | source behavior | `governance/compat/check_semantic_convergence_control.py` | `CODE_FENCE_JSON_RE` and `find_active_blocks` | `find_active_blocks` | SCEC checker | ACCEPT |
| Standard requires a real fenced JSON object | contract | `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` | Activation Sentinel and invariants 10-12 | `CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` | SCEC control plane | ACCEPT |
| Existing focused suite did not cover a non-JSON fence before the active block | test-gap observation | `governance/compat/test_check_semantic_convergence_control.py` | active-block extraction tests | `ValidInitialChainBlockTests` | focused SCEC tests | ACCEPT |
| ADIF-0055 owns repeated semantic-convergence control failures | governance learning | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0055.md` | defect and prevention sections | `CVF_ADIF-0055.md` | ADIF registry | ACCEPT |

## Required Artifact Manifest

The worker may change exactly four paths:

1. `governance/compat/check_semantic_convergence_control.py`
2. `governance/compat/test_check_semantic_convergence_control.py`
3. `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0055.md`
4. `docs/reviews/CVF_SCEC_T1_R1_MIXED_FENCE_ACTIVE_BLOCK_PARSER_HARDENING_WORKER_RETURN_2026-08-31.md`

## Acceptance Strategy

Accept only when focused tests prove the exact reproducer, mixed-fence order
variants, quoted marker immunity, malformed active-block behavior, and all
prior SCEC tests pass. The direct checker, worker-return fast gate, Python size
guard, compile check, and diff/status checks must also pass.

## Evidence / Verification

Required evidence is the direct pre-repair mixed-fence reproducer, focused
positive and negative parser tests, the full existing SCEC test suite, direct
checker output, Python hard-size and compile checks, worker-return fast gate,
and exact git diff/status evidence. All results must be rerun after the last
worker edit.

## ADIF Defect Registry Disclosure

- Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.
- Resolver returned and applied: `ADIF-0001`, `ADIF-0002`, `ADIF-0014`,
  `ADIF-0015`, `ADIF-0020`, `ADIF-0021`, `ADIF-0028`, `ADIF-0029`,
  `ADIF-0033`, `ADIF-0044`.
- Additional directly controlling entry: `ADIF-0055`.
- Other returned entries are applied through exact source claims, protected
  path authorization, checker read-ahead, bounded manifest, no-commit split,
  and complete worker-return evidence.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_python_automation_size.py`; `governance/compat/check_adif_entry_integrity.py` |
| literalTokensReviewed | active block marker, opening/closing fence structure, exact SCEC schema, required-work-order behavior, protected-path authorization labels, worker-return shape, Python hard-size thresholds |
| gateRunPurpose | Confirm the bounded repair packet and final implementation; not discover the parser contract. |
| claimBoundary | Structural extraction hardening only; no semantic progression or product-readiness change. |

## Claim Boundary

This baseline authorizes one parser and regression-test repair. It does not
authorize broader checker refactoring, semantic threshold changes, product or
runtime work, provider/live action, public sync, deployment, or production.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening with no public-sync authority.

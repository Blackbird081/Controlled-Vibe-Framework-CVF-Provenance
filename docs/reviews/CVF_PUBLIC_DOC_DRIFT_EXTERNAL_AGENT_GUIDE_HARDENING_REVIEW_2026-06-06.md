# CVF Public Doc Drift External-Agent Guide Hardening Review

Memory class: POINTER_RECORD

Status: READY_FOR_EXTERNAL_REVIEW

## Purpose

Record the bounded hardening response for repeated external-review findings
around stale public docs, unclear public review entry points, and agent
overread risk.

## Target / Source Under Review

Target files:

- `governance/compat/check_public_doc_drift_phrases.py`
- `governance/compat/test_check_public_doc_drift_phrases.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `docs/reference/CVF_POSITIONING.md`
- public-sync `docs/guides/external-agent-review-guide.md`
- public-sync README/GET_STARTED/public evaluation boundary links

## Scope / Methodology

The review checks whether known external-review drift classes are promoted into
a machine guard and whether public-sync gives external AI reviewers a clear
first-read path. The scope is documentation/control-plane hardening only.

## Findings / Position

- Stale public-doc defects repeated across version strings, skill counts, and
  public handoff labels.
- Human-only reminders were insufficient because external agents typically
  start from a pasted public repository link.
- A bounded phrase guard is appropriate for known high-signal stale phrases.
- A public external-agent guide is appropriate so reviewers separate public
  evidence, known open debt, live-proof unavailability, and production-readiness
  gaps.

## Risk / Corrective Action

Risk: without this hardening, future public reviews can keep rediscovering the
same drift class and can overread public files into unsupported runtime,
production, provider-parity, or private-provenance claims.

Corrective action:

- add `check_public_doc_drift_phrases.py` with focused tests;
- wire the checker into local hook chains;
- repair the same-class `CVF_POSITIONING.md` stale skill/date text caught by
  the new guard;
- add and link the public-sync external-agent review guide.

## Decision / Recommendation / Disposition

Disposition: accept the bounded hardening for external review.

Recommendation: keep the guard narrow to known recurring phrase classes. Add
future stale public-doc findings to this checker only when they are stable,
high-signal, and source-backed.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled |
| --- | --- | --- | --- | --- | --- |
| Repeated stale public-doc phrases and unclear public review entry point | `RULE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_ADDED` | Keep `governance/compat/check_public_doc_drift_phrases.py` in the local hook chain and add future source-backed recurring stale public-doc phrases only when stable enough for low-noise detection | HANDLED |
| Runtime/provider/cost findings | N/A_WITH_REASON | `RUNTIME_BEHAVIOR_LEARNING` N/A | N/A_WITH_REASON | No runtime behavior, provider call, or cost behavior is changed by this public-doc/control-plane hardening | N/A |

## Verification

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 5fdb794f --head HEAD`: PASS.
- `python governance/compat/check_public_doc_drift_phrases.py --enforce`: PASS in private and public-sync.
- `python -m pytest governance/compat/test_check_public_doc_drift_phrases.py -q`: PASS in private and public-sync.
- Public-sync `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit`: PASS.

## Claim Boundary

This review proves only bounded public-doc drift and external-review guidance
hardening. It does not prove runtime behavior, dependency migration,
live-provider governance proof, hosted readiness, production readiness, public
readiness beyond bounded public-sync documentation, provider parity, memory
reinjection, high-risk promotion implementation, Learning Orchestrator runtime
behavior, or autonomous mutation.

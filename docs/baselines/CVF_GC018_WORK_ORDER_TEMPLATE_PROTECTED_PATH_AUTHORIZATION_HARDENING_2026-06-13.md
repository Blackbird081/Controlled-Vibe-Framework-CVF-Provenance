# CVF GC-018 - Work-Order Template Protected-Path Authorization Hardening

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-06-13

Owner: Claude (single-actor governed batch under operator authorization)

Commit mode: SELF_COMMIT_SINGLE_ACTOR

dispatchBaseHead: `4c803586`

sourceAuthority:
`docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_COMPLETION_2026-06-13.md`

rawMemoryReleased=false

## Purpose

Authorize a small governed batch that hardens the work-order authoring
discipline so the ORCHESTRATOR_PACKET_GAP learning recorded at DIR-T1 closure
cannot recur. The batch promotes the prose learning into a binding rule and a
dispatch-time machine check: any work order that authorizes a protected path
must carry a complete `Core Guard Self-Protection Authorization` block.

This follows the CVF agent-error-to-governance learning philosophy: a repeated
defect pattern is promoted to a written rule, the rule is promoted to a machine
check, and the machine check is placed at the earliest applicable gate
(dispatch quality), not at closure only.

## Scope / Target / Owner Boundary

Target: the binding work-order template, the closure-quality standard prose, and
the dispatch-quality checker.

In scope:

- add template section `7A. Protected-Path Authorization Carrier`;
- add a dispatch-quality validator
  `_validate_protected_path_authorization_carrier` that hard-fails a
  dispatch/ready work order authorizing a protected path without a complete
  carrier;
- reuse the exact carrier vocabulary already enforced by
  `check_core_guard_self_protection.py` (no new token, no duplicate authority);
- record the governance learning closure.

Out of scope:

- changing core-guard self-protection semantics or its protected-path set;
- changing closure-time enforcement;
- runtime, provider, OCR, retrieval, external repo, or public-sync work;
- re-opening DIR-T1 or any other closed tranche.

Owner boundary: single-actor governed batch. The operator authorized the
work-order-template hardening batch directly; Claude authors, self-checks, and
commits under the full pre-commit hook chain.

## Decision / Baseline / Proposed Tranche

Decision: promote DIR-T1 ORCHESTRATOR_PACKET_GAP (TEMPLATE_UPDATED) into a
binding template section and a dispatch-quality hard-fail machine check.

Baseline:

- DIR-T1 closure commit: `4bf991f3`.
- DIR-T1 session-sync commit: `4c803586` (current dispatch base).
- Core-guard carrier vocabulary source of truth:
  `governance/compat/check_core_guard_self_protection.py`
  (`AUTH_MARKER` plus the four required tokens).

Enforcement-strength decision (audited, not preference): the agent-error-to-
governance philosophy in CLAUDE.md requires promoting a loosely-interpretable
rule into a machine check at the earliest applicable phase gate. Therefore the
rule is a dispatch-time hard-fail, not advisory.

Vocabulary decision (audited, not preference): CVF anti-duplication discipline
requires composing the existing core-guard carrier vocabulary rather than
inventing a sixth token. Therefore the dispatch check requires exactly the
`Core Guard Self-Protection Authorization` heading plus
`Authorized guard-maintenance scope`, `Protected paths`,
`Operator authorization`, and `Rollback boundary`.

## Knowledge Absorption Blind-Spot Control Block

| Control item | Evidence | Disposition |
| --- | --- | --- |
| Prior absorption evidence resolved | batch builds only on the closed DIR-T1 completion review learning and the existing core-guard checker | COMPLETE |
| Detailed source files read | core-guard checker, dispatch-quality checker, and template were read before editing | COMPLETE |
| Current owner surfaces checked | carrier vocabulary sourced from `check_core_guard_self_protection.py`; no duplicate authority created | COMPLETE |
| Accept/defer/reject dispositions recorded | enforcement-strength and vocabulary decisions recorded above with audited basis | COMPLETE |
| Adversarial role review applied | new validator unit-tested across no-carrier, no-protected-path, complete-carrier, and incomplete-carrier cases | COMPLETE |
| Blind-spot delta | no core-guard semantic change, no protected-path set change, no closed-tranche reopen | COMPLETE |

Verdict: `COMPLETE_WITH_DECLARED_BOUNDARIES`.

## Rescan Intelligence Hardening

- Original source artifact: the DIR-T1 completion review learning and the
  existing core-guard and dispatch-quality checkers, not any external repo.
- Predecessor intake artifact:
  `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_COMPLETION_2026-06-13.md`.
- Delta ledger status: DISPATCH_DECLARED_LIMITS - this batch only adds a
  template section, standard prose, and one dispatch-quality validator.
- Routing matrix status: DISPATCH_DECLARED_LIMITS - core-guard semantics,
  protected-path set, closure-time enforcement, runtime, and public-sync remain
  out of scope.
- Semantic sampling status: DISPATCH_DECLARED_LIMITS - the new validator reuses
  the core-guard carrier vocabulary and mirrors its protected-path rule.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| sampleId | Delta category | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| TPH-D1 | NEW_FINDING | DIR-T1 learning | protected-path authorization carrier was not mandatory in work orders | this batch adds a dispatch hard-fail | Could a future work order still omit the carrier? | PASS |
| TPH-D2 | UNCHANGED_FROM_INTAKE | core-guard checker | carrier vocabulary is owned by check_core_guard_self_protection.py | dispatch check reuses the same tokens | Did the batch duplicate authority? | PASS |
| TPH-D3 | CHANGED_DISPOSITION | DIR-T1 learning disposition | ORCHESTRATOR_PACKET_GAP moved from TEMPLATE_UPDATED-pending to MACHINE_CHECK_ADDED | dispatch validator added this batch | Did the disposition close without a machine check? | PASS |
| TPH-D4 | REMOVED_OR_REJECTED | core-guard semantics | protected-path set and closure enforcement unchanged | out-of-scope retained | Could the batch alter core-guard behavior? | PASS |

### Follow-Up Routing Matrix

| Route lane | Target | Disposition | Evidence | Next action |
| --- | --- | --- | --- | --- |
| DO_NOW | template section 7A, standard rule, dispatch validator | ACCEPT | DIR-T1 learning and core-guard checker | Claude implements and self-commits |
| SEPARATE_RUNTIME_TRANCHE | core-guard semantic change | DEFER | out-of-scope boundary | fresh authorization if ever needed |
| STRATEGIC_OPERATOR_DECISION | broaden protected-path set or apply carrier to non-work-order artifact classes | DEFER | not requested by operator | operator decision later if ever needed |
| OUT_OF_SCOPE | protected-path set change, closure-time enforcement change | REJECT | claim boundary | no change |
| RESOLVED_BY_DESIGN | dispatch hard-fail vs advisory choice | REJECT | agent-error-to-governance philosophy mandates earliest-gate machine check | hard-fail selected |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| TPH-S1 | core-guard checker | four required tokens plus AUTH_MARKER | dispatch validator requires the same | Could vocabularies drift? | PASS |
| TPH-S2 | dispatch validator | runs only in dispatch/ready branch | closed work orders unaffected | Could it false-fire on closed work orders? | PASS |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: core-guard auth marker | `governance/compat/check_core_guard_self_protection.py` | line 24 | `AUTH_MARKER` | core-guard self-protection gate | ACCEPT |
| EXISTS: core-guard required tokens | `governance/compat/check_core_guard_self_protection.py` | `_has_core_auth` | `Authorized guard-maintenance scope`, `Protected paths`, `Operator authorization`, `Rollback boundary` | core-guard self-protection gate | ACCEPT |
| EXISTS: core-guard protected-path rule | `governance/compat/check_core_guard_self_protection.py` | `_is_protected` | governance/compat/*.py, CVF_SESSION/**.json, CVF_SESSION_MEMORY.md, AGENT_HANDOFF*.md | core-guard self-protection gate | ACCEPT |
| EXISTS: dispatch-quality work-order validator | `governance/compat/check_work_order_dispatch_quality.py` | `_validate_work_order` | dispatch/ready branch | dispatch-quality gate | ACCEPT |
| EXISTS: work-order template owner surface | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Section 7 / 8 | template body | binding work-order template | ACCEPT |
| EXISTS: DIR-T1 learning source | `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_COMPLETION_2026-06-13.md` | Finding-To-Governance Learning Disposition | ORCHESTRATOR_PACKET_GAP -> TEMPLATE_UPDATED | DIR-T1 completion review | ACCEPT |

## New Doc-Only Fields Authorized

| New field or symbol | Source | Target | Boundary |
| --- | --- | --- | --- |
| Template section `7A. Protected-Path Authorization Carrier` | this baseline | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | authoring-rule section; reuses existing carrier tokens |
| `_validate_protected_path_authorization_carrier` | this baseline | `governance/compat/check_work_order_dispatch_quality.py` | dispatch-time validator; mirrors core-guard protected-path rule |
| `_is_protected_authorization_path` | this baseline | `governance/compat/check_work_order_dispatch_quality.py` | local mirror of core-guard `_is_protected` |

## Authorized Artifact Set

This batch may create or update only:

- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`;
- `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`;
- `governance/compat/check_work_order_dispatch_quality.py`;
- this GC-018 baseline;
- `docs/reviews/CVF_WORK_ORDER_TEMPLATE_PROTECTED_PATH_AUTHORIZATION_HARDENING_COMPLETION_2026-06-13.md`;
- session-state/front-door/handoff continuity files in a separate session-sync
  commit after material closure.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one dispatch-quality validator and its
protected-path mirror helper to `check_work_order_dispatch_quality.py`, without
changing core-guard self-protection semantics or its protected-path set, and
keep the dispatch carrier vocabulary identical to the core-guard gate. Out of
scope: any change to `check_core_guard_self_protection.py` itself.

Protected paths:

- `governance/compat/check_work_order_dispatch_quality.py`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `AGENT_HANDOFF_V18_2026-06-12.md`

Operator authorization: the operator selected the work-order-template hardening
batch as the next allowed move after DIR-T1 closure and directed Claude to
audit and follow CVF's own rules for enforcement strength and carrier
vocabulary.

Rollback boundary: revert only this hardening batch (template section 7A, the
dispatch-quality validator, the standard prose, this baseline, and the
completion review) plus its session-sync if the rule proves miscalibrated. Do
not revert DIR-T1 material closure `4bf991f3`, DIR-T1 session-sync `4c803586`,
or any earlier closed tranche.

## Evidence / Verification

Required verification:

- dispatch-quality checker `py_compile` passes;
- new validator unit-tested across no-carrier, no-protected-path,
  complete-carrier, and incomplete-carrier cases;
- reviewer-fast and full pre-commit gates pass before commit;
- this baseline carries its own Core Guard Self-Protection Authorization block,
  dogfooding the rule it adds.

## Claim Boundary

This GC-018 authorizes a bounded work-order authoring-discipline hardening
batch only. It does not change core-guard self-protection semantics, alter the
protected-path set, change closure-time enforcement, claim runtime behavior,
authorize provider/OCR/retrieval/external-repo/public-sync work, or reopen any
closed tranche.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

This is a private provenance governance hardening baseline. No public-sync
artifact or public catalog claim is authorized by this batch.

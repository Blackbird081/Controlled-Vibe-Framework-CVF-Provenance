# GC-018 Dispatch Packet Authoring Guard Hardening

Memory class: POINTER_RECORD

rawMemoryReleased: false

Baseline ID: GC018-DISPATCH-PACKET-AUTHORING-GUARD-HARDENING-2026-06-15

Date: 2026-06-15

Status: DISPATCHED_TO_CLAUDE

dispatchBaseHead: `047f9ea4`

## Purpose

Authorize a bounded governance-foundation hardening tranche that promotes the
P4B-B work-order authoring defects into reusable packet-authoring controls.

The tranche must test against the current defective P4B-B GC-018/work-order
packet before any P4B-B packet repair is attempted. The goal is to make future
orchestrator/agent-authored dispatch packets fail early when they repeat the
same defects.

## Scope / Target / Owner Boundary

Target owner surfaces:

- `governance/compat/check_work_order_dispatch_quality.py`;
- `governance/compat/test_check_work_order_dispatch_quality.py`;
- optional packet-author fast gate wrapper under `governance/compat/`;
- optional reference standard under `docs/reference/`;
- completion review under `docs/reviews/`.

Read-only regression input:

- `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4B_B_CONCRETE_PROVIDER_LIVE_PROOF_2026-06-15.md`;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4B_B_CONCRETE_PROVIDER_LIVE_PROOF_FOR_CODEX_2026-06-15.md`.

Those P4B-B files are not authorized for repair in this tranche. They are the
negative sample.

## Defect Packet

The current P4B-B packet produced these dispatch-quality failures:

| Finding | Required reusable control |
|---|---|
| `dispatchBaseHead` is prose instead of a commit SHA | Dispatch packets must carry a real commit hash before ready/dispatched status |
| Missing Worker Autonomy / No-Question Rule | Ready/dispatched work orders must include the section before worker handoff |
| Source Verification table uses noncanonical columns | Source Verification must use the canonical six-column schema |
| Source Verification disposition includes boundary prose | Disposition must use the canonical vocabulary; boundary prose belongs in a separate table |

The new operator live-key authorization for P4B-B is outside this hardening
tranche. This tranche must not consume provider API keys, read `.env.local`, or
run a live provider call.

## Decision / Baseline / Proposed Tranche

Decision: release one bounded governance hardening tranche to Claude under
`WORKER_MUST_NOT_COMMIT`.

Baseline: the existing dispatch-quality checker already detects the current
P4B-B packet defects, but the packet-author workflow lacks a dedicated
regression bundle and a clear packet-author fast command. This creates repeated
reviewer latency and lets authors return packets that are predictably blocked.

Proposed tranche: add regression coverage and a packet-authoring control path
without changing Model Gateway runtime or the defective P4B-B packet.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Work-order template requires Worker Autonomy / No-Question Rule for ready/dispatched work orders | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | lines 98 and 523 | `Worker Autonomy / No-Question Rule` | work-order template | ACCEPT |
| Work-order template requires dispatchBaseHead as an explicit evidence field | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 1028 | `dispatchBaseHead` | work-order template | ACCEPT |
| Dispatch checker classifies ready/dispatched status tokens | `governance/compat/check_work_order_dispatch_quality.py` | lines 130-141 and 296 | `DISPATCH_STATUS_TOKENS`; `_is_ready_or_dispatch_status` | dispatch-quality checker | ACCEPT |
| Dispatch checker validates Worker Autonomy / No-Question Rule | `governance/compat/check_work_order_dispatch_quality.py` | lines 618 and 2175 | `_has_worker_autonomy_clause` | dispatch-quality checker | ACCEPT |
| Dispatch checker validates real dispatchBaseHead commit shape | `governance/compat/check_work_order_dispatch_quality.py` | lines 649-656 | `dispatchBaseHead` | dispatch-quality checker | ACCEPT |
| Dispatch checker validates canonical Source Verification table columns | `governance/compat/check_work_order_dispatch_quality.py` | line 922 | `Source Verification table uses noncanonical columns` | dispatch-quality checker | ACCEPT |
| Dispatch checker validates Source Verification disposition vocabulary | `governance/compat/check_work_order_dispatch_quality.py` | line 61 | `ALLOWED_SOURCE_VERIFICATION_DISPOSITIONS` | dispatch-quality checker | ACCEPT |
| Local hook chain already runs dispatch-quality in reviewer-fast/pre-commit/pre-push chains | `governance/compat/run_local_governance_hook_chain.py` | line 24 | `REVIEWER_FAST_CHECKS` | local hook chain | ACCEPT |
| Autorun pre-dispatch runs dispatch-quality | `governance/compat/run_agent_autorun_workflow_gate.py` | line 50 | `_common_commands` | autorun workflow gate | ACCEPT |

## Authorized Work

1. Add a regression test that models the current P4B-B packet authoring defect
   bundle and asserts all four reusable findings are detected.
2. Add or harden a packet-author fast gate so a packet author can run one
   command before returning a GC-018/work-order packet.
3. Document the packet-authoring workflow rule: author runs the fast gate before
   claiming `DISPATCHED`, `READY`, or equivalent status.
4. Record the initial failing P4B-B packet evidence before fixing any packet.

## Not Authorized

- Do not repair the P4B-B GC-018/work order in this tranche.
- Do not run live provider calls or read API keys.
- Do not modify Model Gateway runtime source.
- Do not modify session/front-door state unless closure explicitly changes next
  allowed move.
- Do not weaken existing dispatch-quality checks.

## Required Verification

Claude must run and record:

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 047f9ea4 --head HEAD --enforce
```

before implementation and confirm that the current P4B-B packet triggers the
four finding classes listed above.

After implementation, Claude must run the focused governance tests for changed
guard/wrapper files plus:

```powershell
python governance/compat/run_worker_return_fast_gate.py
git diff --check
```

The completion review must include a Finding-To-Governance Learning Disposition
classifying this as governance/control-plane learning.

## Evidence / Verification

Required evidence:

- pre-implementation dispatch-quality failure against the current P4B-B packet;
- focused regression test that captures the four finding classes together;
- packet-author fast command or documented equivalent;
- worker-return fast gate result;
- `git diff --check` result.

## Negative Search And Collision Discipline

This tranche does not perform broad negative search over runtime symbols. It
uses the current P4B-B packet as a narrow collision sample. Claude must record
whether any finding text is a same-token documentation collision and must not
promote boundary prose into Source Verification disposition cells.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-15 dispatch packet authoring guard hardening dispatch |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `rg`; `apply_patch`; governance gate review |
| Target paths | this GC-018 and Claude work order |
| Allowed scope source | operator instruction 2026-06-15: raise CVF foundation, test with current findings before fixing, transfer to Claude |
| Before status evidence | P4B-B packet fails dispatch-quality with four reusable authoring defects |
| After status evidence | Guard-hardening work order authored for Claude |
| Diff evidence | uncommitted dispatch packet only |
| Approval boundary | governance hardening only; no P4B-B repair and no live call |
| Claim boundary | dispatch packet authoring guard hardening, not provider/runtime proof |
| Agent type | Codex orchestrator |
| Invocation ID | dispatch-packet-authoring-guard-hardening-2026-06-15 |
| Expected manifest | `docs/baselines/CVF_GC018_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_FOR_CLAUDE_2026-06-15.md`; `governance/compat/test_check_work_order_dispatch_quality.py`; `governance/compat/run_dispatch_packet_author_fast_gate.py`; `governance/compat/test_run_dispatch_packet_author_fast_gate.py`; `docs/reviews/CVF_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_COMPLETION_2026-06-15.md` |
| Actual changed set | `docs/baselines/CVF_GC018_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_FOR_CLAUDE_2026-06-15.md`; `governance/compat/test_check_work_order_dispatch_quality.py`; `governance/compat/run_dispatch_packet_author_fast_gate.py`; `governance/compat/test_run_dispatch_packet_author_fast_gate.py`; `docs/reviews/CVF_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_COMPLETION_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening. No public-sync batch is
authorized.

## Claim Boundary

This baseline authorizes only dispatch-packet authoring guard hardening. It does
not authorize P4B-B packet repair, live provider execution, credential reads,
Model Gateway runtime changes, public-sync, production readiness, or public
readiness.

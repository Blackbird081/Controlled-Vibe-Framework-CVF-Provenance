import importlib.util
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().with_name("check_agent_handoff_boundary.py")
SPEC = importlib.util.spec_from_file_location("check_agent_handoff_boundary", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


VALID_CONTROL_BLOCK = """
## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one-agent-many-roles |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead; executionBaseHead; closureBaseHead |
| changedSetScope(phase) | phase-local changed set only |
| traceScope(phase, actor) | one trace per phase actor |
| commitOwner(phase) | Codex owns all phases in this batch |
| crossBatchIsolation | one-batch-per-clean-worktree; clean worktree required before dispatch |
| nextMoveSurfaces | session sync must update all four active next-move surfaces |
"""


def _types(issues: list[dict[str, str]]) -> set[str]:
    return {issue["type"] for issue in issues}


def test_handoff_work_order_without_contract_block_fails() -> None:
    text = """
# Work Order

Status: DISPATCH_READY

Batch ID: AHB-T3
dispatchBaseHead: abc123
executionBaseHead: abc123
closureBaseHead: abc123
"""

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T3.md", text)

    assert "handoff_contract_control_block_missing" in _types(issues)


def test_valid_single_agent_multi_role_work_order_passes() -> None:
    text = f"""
# Work Order

Status: CLOSED_PASS_BOUNDED

Batch ID: AHB-T3
Commit mode: WORKER_MAY_COMMIT
dispatchBaseHead: abc123
executionBaseHead: abc123
closureBaseHead: abc123

{VALID_CONTROL_BLOCK}
"""

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T3.md", text)

    assert not issues


def test_worker_must_not_commit_requires_reviewer_closure_conversion() -> None:
    text = f"""
# Work Order

Status: DISPATCH_READY

Batch ID: AHB-T3
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchBaseHead: abc123
executionBaseHead: abc123
closureBaseHead: abc123

{VALID_CONTROL_BLOCK}
"""

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T3.md", text)

    assert "reviewer_closure_conversion_missing" in _types(issues)


def test_descriptive_worker_must_not_commit_token_does_not_trigger_c4_rule() -> None:
    text = f"""
# Work Order

Status: CLOSED_PASS_BOUNDED

Batch ID: AHB-T3
Commit mode: WORKER_MAY_COMMIT
dispatchBaseHead: abc123
executionBaseHead: abc123
closureBaseHead: abc123

This batch documents `WORKER_MUST_NOT_COMMIT` as a rule but does not select it.

{VALID_CONTROL_BLOCK}
"""

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T3.md", text)

    assert not issues


def test_worker_must_not_commit_with_reviewer_conversion_passes() -> None:
    text = f"""
# Work Order

Status: DISPATCH_READY

Batch ID: AHB-T3
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchBaseHead: abc123
executionBaseHead: abc123
closureBaseHead: abc123

{VALID_CONTROL_BLOCK}

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_EXAMPLE_COMPLETION.md` |
| reviewerOwnedClosurePaths | `docs/reviews/CVF_EXAMPLE_COMPLETION.md` |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Before status evidence | clean worktree |
"""

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T3.md", text)

    assert not issues


def test_c3_work_order_requires_closer_designation() -> None:
    text = f"""
# Work Order

Status: CLOSED_PASS_BOUNDED

Batch ID: AHB-T3
This C3 three-or-more-agent chain uses N-plus-agent role routing.
dispatchBaseHead: abc123
executionBaseHead: abc123
closureBaseHead: abc123

{VALID_CONTROL_BLOCK}
"""

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T3.md", text)

    assert "c3_closer_not_designated" in _types(issues)


def test_dispatch_ready_requires_clean_worktree_trace_evidence() -> None:
    text = f"""
# Work Order

Status: DISPATCH_READY

Batch ID: AHB-T3
dispatchBaseHead: abc123
executionBaseHead: abc123
closureBaseHead: abc123

{VALID_CONTROL_BLOCK}

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Before status evidence | unknown |
"""

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T3.md", text)

    assert "cross_batch_isolation_clean_worktree_missing" in _types(issues)


def test_non_handoff_work_order_is_ignored() -> None:
    text = """
# Work Order

Status: DISPATCH_READY

Scope: update a small documentation note.
"""

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_NOTE.md", text)

    assert not issues


def test_standard_and_hook_bindings_are_checked(tmp_path: Path) -> None:
    repo_root = tmp_path
    standard_path = repo_root / MODULE.STANDARD_PATH
    standard_path.parent.mkdir(parents=True)
    standard_path.write_text("Status: ACTIVE_STANDARD_AND_MACHINE_ENFORCED\n", encoding="utf-8")

    with patch.object(MODULE, "REPO_ROOT", repo_root):
        issues = MODULE._validate_standard(MODULE.STANDARD_PATH, standard_path.read_text())

    assert "standard_marker_missing" in _types(issues)

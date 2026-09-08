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
| sharedWorktreeCoordinationMode | `SEPARATE_GIT_WORKTREE` |

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


LANE_CONTROL_BLOCK_TEMPLATE = """
## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> worker -> reviewer/closer |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead; executionBaseHead; closureBaseHead |
| changedSetScope(phase) | phase-local changed set only |
| traceScope(phase, actor) | one trace per phase actor |
| commitOwner(phase) | reviewer/closer owns accepted material |
| crossBatchIsolation | explicit lane handoff with dispatcher mutation forbidden |
| sharedWorktreeCoordinationMode | `{mode}` |
{lane_rows}| nextMoveSurfaces | reviewer disposition then continuity projection |
"""

FULL_LANE_ROWS = (
    "| activeLaneOwner | internal no-commit worker from execution anchor capture |\n"
    "| laneOwnedPaths | exactly the eight Write Ownership paths |\n"
    "| dispatcherMutationBoundary | `NO_MUTATION_WHILE_LANE_ACTIVE` |\n"
    "| laneReleaseEvidence | worker return records final status and empty staging |\n"
)


def _lane_work_order(mode: str, lane_rows: str = FULL_LANE_ROWS, *, status: str = "DISPATCH_READY") -> str:
    block = LANE_CONTROL_BLOCK_TEMPLATE.format(mode=mode, lane_rows=lane_rows)
    return f"""
# Work Order

Status: {status}

Batch ID: ROLE-SOT-MH-T1
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchBaseHead: abc123
executionBaseHead: WORKER_MUST_CAPTURE_AT_START
closureBaseHead: REVIEWER_TO_SET

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_EXAMPLE_COMPLETION_2026-09-08.md`
reviewerOwnedClosurePaths: exact worker paths

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Before status evidence | clean worktree, empty staging |

{block}
"""


def test_explicit_lane_handoff_with_all_fields_passes() -> None:
    text = _lane_work_order("EXPLICIT_LANE_HANDOFF")

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_MH_T1.md", text)

    assert not issues


def test_separate_git_worktree_coordination_passes() -> None:
    text = _lane_work_order("SEPARATE_GIT_WORKTREE", lane_rows="")

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_MH_T1.md", text)

    assert not issues


def test_dispatch_ready_no_commit_with_unrecognized_mode_value_fails() -> None:
    """A declared field carrying a non-canonical value is invalid, not missing."""
    text = _lane_work_order("UNDECLARED_MODE", lane_rows="")

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_MH_T1.md", text)

    assert "shared_worktree_coordination_mode_invalid" in _types(issues)


def test_dispatch_ready_no_commit_without_coordination_field_fails() -> None:
    text = _lane_work_order("EXPLICIT_LANE_HANDOFF", lane_rows="").replace(
        "| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF` |\n", ""
    )

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_MH_T1.md", text)

    assert "shared_worktree_coordination_mode_missing" in _types(issues)


def test_unrelated_field_naming_other_mode_does_not_affect_selection() -> None:
    """A mode token in a different field is not a second declaration."""
    rows = "| alternateMode | `SEPARATE_GIT_WORKTREE` |\n" + FULL_LANE_ROWS
    text = _lane_work_order("EXPLICIT_LANE_HANDOFF", lane_rows=rows)

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_MH_T1.md", text)

    assert not issues


def test_explicit_lane_handoff_missing_mutation_boundary_fails() -> None:
    rows = (
        "| activeLaneOwner | internal no-commit worker |\n"
        "| laneOwnedPaths | exactly the eight Write Ownership paths |\n"
        "| laneReleaseEvidence | worker return records final status |\n"
    )
    text = _lane_work_order("EXPLICIT_LANE_HANDOFF", lane_rows=rows)

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_MH_T1.md", text)

    assert "explicit_lane_handoff_field_missing" in _types(issues)


def test_explicit_lane_handoff_missing_release_evidence_fails() -> None:
    rows = (
        "| activeLaneOwner | internal no-commit worker |\n"
        "| laneOwnedPaths | exactly the eight Write Ownership paths |\n"
        "| dispatcherMutationBoundary | `NO_MUTATION_WHILE_LANE_ACTIVE` |\n"
    )
    text = _lane_work_order("EXPLICIT_LANE_HANDOFF", lane_rows=rows)

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_MH_T1.md", text)

    assert "explicit_lane_handoff_field_missing" in _types(issues)


def test_explicit_lane_handoff_placeholder_owner_fails() -> None:
    rows = (
        "| activeLaneOwner | TBD |\n"
        "| laneOwnedPaths | exactly the eight Write Ownership paths |\n"
        "| dispatcherMutationBoundary | `NO_MUTATION_WHILE_LANE_ACTIVE` |\n"
        "| laneReleaseEvidence | worker return records final status |\n"
    )
    text = _lane_work_order("EXPLICIT_LANE_HANDOFF", lane_rows=rows)

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_MH_T1.md", text)

    assert "explicit_lane_handoff_field_missing" in _types(issues)


def test_explicit_lane_handoff_wrong_mutation_boundary_token_fails() -> None:
    rows = (
        "| activeLaneOwner | internal no-commit worker |\n"
        "| laneOwnedPaths | exactly the eight Write Ownership paths |\n"
        "| dispatcherMutationBoundary | dispatcher may edit freely |\n"
        "| laneReleaseEvidence | worker return records final status |\n"
    )
    text = _lane_work_order("EXPLICIT_LANE_HANDOFF", lane_rows=rows)

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_MH_T1.md", text)

    assert "explicit_lane_handoff_mutation_boundary_invalid" in _types(issues)


def test_worker_may_commit_work_order_is_outside_lane_control() -> None:
    """Boundary case: the lane control applies only to no-commit dispatch."""
    text = _lane_work_order("EXPLICIT_LANE_HANDOFF", lane_rows="").replace(
        "Commit mode: WORKER_MUST_NOT_COMMIT", "Commit mode: WORKER_MAY_COMMIT"
    )

    issues = MODULE._validate_shared_worktree_coordination(
        "docs/work_orders/CVF_AGENT_WORK_ORDER_MH_T1.md",
        text,
        MODULE._extract_section(text, MODULE.CONTROL_BLOCK),
    )

    assert not issues


def test_closed_work_order_is_outside_lane_control() -> None:
    """Boundary case: historical closed packets are not retro-validated."""
    text = _lane_work_order(
        "EXPLICIT_LANE_HANDOFF", lane_rows="", status="CLOSED_PASS_BOUNDED"
    )

    issues = MODULE._validate_shared_worktree_coordination(
        "docs/work_orders/CVF_AGENT_WORK_ORDER_MH_T1.md",
        text,
        MODULE._extract_section(text, MODULE.CONTROL_BLOCK),
    )

    assert not issues


def test_existing_clean_worktree_rule_remains_active() -> None:
    """Boundary case: the prior AHB isolation rule must not regress."""
    text = _lane_work_order("EXPLICIT_LANE_HANDOFF").replace(
        "| Before status evidence | clean worktree, empty staging |", ""
    )

    issues = MODULE._validate_work_order("docs/work_orders/CVF_AGENT_WORK_ORDER_MH_T1.md", text)

    assert "cross_batch_isolation_clean_worktree_missing" in _types(issues)


def test_lane_field_value_reads_inline_form() -> None:
    block = "sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF\nactiveLaneOwner: internal worker\n"

    assert MODULE._lane_field_value(block, "activeLaneOwner") == "internal worker"


# --- Rework generation 1: exact coordination-field parsing (findings 4, 5) --


def _lane_issue_types(rows: str) -> set[str]:
    text = _lane_work_order("PLACEHOLDER", lane_rows="").replace(
        "| sharedWorktreeCoordinationMode | `PLACEHOLDER` |\n", ""
    )
    text = text.replace(
        "| nextMoveSurfaces |", rows + "| nextMoveSurfaces |"
    )
    block = MODULE._extract_section(text, MODULE.CONTROL_BLOCK)
    return {
        issue["type"]
        for issue in MODULE._validate_shared_worktree_coordination(
            "docs/work_orders/CVF_AGENT_WORK_ORDER_MH_T1.md", text, block
        )
    }


LANE_BODY_ROWS = (
    "| activeLaneOwner | internal no-commit worker |\n"
    "| laneOwnedPaths | exactly the eight Write Ownership paths |\n"
    "| dispatcherMutationBoundary | `NO_MUTATION_WHILE_LANE_ACTIVE` |\n"
)


def test_other_mode_token_in_lane_prose_does_not_break_singleton() -> None:
    """Finding 4: only the field declaration selects the mode."""
    rows = (
        "| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF` |\n"
        + LANE_BODY_ROWS
        + "| laneReleaseEvidence | this is not a SEPARATE_GIT_WORKTREE run; worker returns status |\n"
    )

    assert _lane_issue_types(rows) == set()


def test_coordination_mode_with_invalid_suffix_fails() -> None:
    rows = (
        "| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF_EXPERIMENTAL` |\n"
        + LANE_BODY_ROWS
        + "| laneReleaseEvidence | worker returns status |\n"
    )

    assert "shared_worktree_coordination_mode_invalid" in _lane_issue_types(rows)


def test_duplicate_identical_coordination_field_declarations_fail() -> None:
    rows = (
        "| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF` |\n"
        "| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF` |\n"
        + LANE_BODY_ROWS
        + "| laneReleaseEvidence | worker returns status |\n"
    )

    assert "shared_worktree_coordination_mode_not_singleton" in _lane_issue_types(rows)


def test_two_contradictory_coordination_field_declarations_fail() -> None:
    rows = (
        "| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF` |\n"
        "| sharedWorktreeCoordinationMode | `SEPARATE_GIT_WORKTREE` |\n"
        + LANE_BODY_ROWS
        + "| laneReleaseEvidence | worker returns status |\n"
    )

    assert "shared_worktree_coordination_mode_not_singleton" in _lane_issue_types(rows)


def test_missing_coordination_field_fails() -> None:
    rows = LANE_BODY_ROWS + "| laneReleaseEvidence | worker returns status |\n"

    assert "shared_worktree_coordination_mode_missing" in _lane_issue_types(rows)


def test_mutation_boundary_with_except_suffix_fails() -> None:
    """Finding 5: a suffixed carve-out inverts the boundary it names."""
    rows = (
        "| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF` |\n"
        "| activeLaneOwner | internal no-commit worker |\n"
        "| laneOwnedPaths | exactly the eight Write Ownership paths |\n"
        "| dispatcherMutationBoundary | `NO_MUTATION_WHILE_LANE_ACTIVE_EXCEPT_DISPATCHER` |\n"
        "| laneReleaseEvidence | worker returns status |\n"
    )

    assert "explicit_lane_handoff_mutation_boundary_invalid" in _lane_issue_types(rows)


def test_mutation_boundary_wrapped_in_prose_fails() -> None:
    rows = (
        "| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF` |\n"
        "| activeLaneOwner | internal no-commit worker |\n"
        "| laneOwnedPaths | exactly the eight Write Ownership paths |\n"
        "| dispatcherMutationBoundary | the boundary is NO_MUTATION_WHILE_LANE_ACTIVE for now |\n"
        "| laneReleaseEvidence | worker returns status |\n"
    )

    assert "explicit_lane_handoff_mutation_boundary_invalid" in _lane_issue_types(rows)


def test_exact_mutation_boundary_value_passes() -> None:
    rows = (
        "| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF` |\n"
        + LANE_BODY_ROWS
        + "| laneReleaseEvidence | worker returns status |\n"
    )

    assert _lane_issue_types(rows) == set()


def test_contradictory_lane_field_declarations_fail() -> None:
    rows = (
        "| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF` |\n"
        "| activeLaneOwner | internal no-commit worker |\n"
        "| activeLaneOwner | some other owner |\n"
        "| laneOwnedPaths | exactly the eight Write Ownership paths |\n"
        "| dispatcherMutationBoundary | `NO_MUTATION_WHILE_LANE_ACTIVE` |\n"
        "| laneReleaseEvidence | worker returns status |\n"
    )

    assert "explicit_lane_handoff_field_not_singleton" in _lane_issue_types(rows)


def test_lane_field_values_supports_inline_and_table_forms() -> None:
    block = (
        "| activeLaneOwner | table owner |\n"
        "dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE\n"
    )

    assert MODULE._lane_field_values(block, "activeLaneOwner") == ["table owner"]
    assert MODULE._lane_field_values(block, "dispatcherMutationBoundary") == [
        "NO_MUTATION_WHILE_LANE_ACTIVE"
    ]


# --- Rework generation 2: semantic placeholders in lane fields -------------


def _lane_rows(
    *,
    owner: str = "internal no-commit worker from execution anchor capture",
    paths: str = "exactly the eight Write Ownership paths",
    boundary: str = "`NO_MUTATION_WHILE_LANE_ACTIVE`",
    release: str = "worker return records final status and empty staging",
) -> str:
    return (
        "| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF` |\n"
        f"| activeLaneOwner | {owner} |\n"
        f"| laneOwnedPaths | {paths} |\n"
        f"| dispatcherMutationBoundary | {boundary} |\n"
        f"| laneReleaseEvidence | {release} |\n"
    )


def _lane_types(rows: str) -> set[str]:
    text = _lane_work_order("EXPLICIT_LANE_HANDOFF", lane_rows="").replace(
        "| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF` |\n", ""
    )
    text = text.replace("| nextMoveSurfaces |", rows + "| nextMoveSurfaces |")
    block = MODULE._extract_section(text, MODULE.CONTROL_BLOCK)
    return {
        issue["type"]
        for issue in MODULE._validate_shared_worktree_coordination(
            "docs/work_orders/CVF_AGENT_WORK_ORDER_MH_T1.md", text, block
        )
    }


def test_active_lane_owner_worker_to_set_is_rejected() -> None:
    assert "explicit_lane_handoff_field_missing" in _lane_types(
        _lane_rows(owner="WORKER_TO_SET")
    )


def test_lane_owned_paths_required_is_rejected() -> None:
    assert "explicit_lane_handoff_field_missing" in _lane_types(
        _lane_rows(paths="REQUIRED")
    )


def test_lane_release_evidence_not_executed_yet_is_rejected() -> None:
    assert "explicit_lane_handoff_field_missing" in _lane_types(
        _lane_rows(release="NOT_EXECUTED_YET")
    )


def test_active_lane_owner_na_with_reason_is_rejected() -> None:
    """A deferred N/A is not an operational lane owner."""
    assert "explicit_lane_handoff_field_missing" in _lane_types(
        _lane_rows(owner="N/A with reason: deferred")
    )


def test_reviewer_to_set_placeholder_is_rejected() -> None:
    assert "explicit_lane_handoff_field_missing" in _lane_types(
        _lane_rows(owner="REVIEWER_TO_SET")
    )


def test_dispatcher_to_set_placeholder_is_rejected() -> None:
    assert "explicit_lane_handoff_field_missing" in _lane_types(
        _lane_rows(paths="DISPATCHER_TO_SET")
    )


def test_owner_to_set_placeholder_is_rejected() -> None:
    assert "explicit_lane_handoff_field_missing" in _lane_types(
        _lane_rows(release="OWNER_TO_SET")
    )


def test_not_applicable_with_reason_placeholder_is_rejected() -> None:
    assert "explicit_lane_handoff_field_missing" in _lane_types(
        _lane_rows(owner="NOT_APPLICABLE_WITH_REASON: deferred")
    )


def test_placeholder_matching_is_case_insensitive() -> None:
    assert "explicit_lane_handoff_field_missing" in _lane_types(
        _lane_rows(owner="worker_to_set")
    )


def test_real_descriptive_lane_values_pass() -> None:
    assert _lane_types(_lane_rows()) == set()


def test_descriptive_value_containing_placeholder_word_still_passes() -> None:
    """Only a whole-value placeholder is rejected, not prose that mentions one."""
    assert _lane_types(
        _lane_rows(release="worker return records status; no field is left as TBD")
    ) == set()


def test_mutation_boundary_exactness_is_unchanged_by_placeholder_rule() -> None:
    types = _lane_types(_lane_rows(boundary="`NO_MUTATION_WHILE_LANE_ACTIVE_EXCEPT_DISPATCHER`"))

    assert "explicit_lane_handoff_mutation_boundary_invalid" in types

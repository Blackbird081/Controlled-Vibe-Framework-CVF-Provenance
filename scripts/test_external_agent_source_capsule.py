from __future__ import annotations

from argparse import Namespace
from pathlib import Path

import pytest

from scripts.external_agent_packet import SOURCE_POSTURE_LIVE, PacketError
from scripts.external_agent_source_capsule import (
    EXPECTED_RETURN_STATUS, classify_task_capsule_drift, create_source_capsule,
    resolve_output_root, resolve_public_cvf_pin, validate_return_cvf_pin,
)


COMMIT = "b" * 40


def _args(tmp_path: Path) -> Namespace:
    return Namespace(
        packet_root=str(tmp_path), task_id="source-001", title="Source audit",
        objective="Create typed candidates", source_repository="https://github.com/example/repo.git",
        source_commit=COMMIT, source_license_expression="MIT",
        source_license_source=f"https://github.com/example/repo/blob/{COMMIT}/LICENSE",
        source_immutable_reference=[f"https://github.com/example/repo/blob/{COMMIT}/README.md"],
        output_root="D:/returns/source-001", non_goal=["No implementation"],
    )


def test_source_capsule_binds_operational_intake_fields(tmp_path: Path) -> None:
    capsule = create_source_capsule(_args(tmp_path), "a" * 40, SOURCE_POSTURE_LIVE)
    assert capsule["task"]["workingMode"] == "SOURCE_PACK_PREPARATION"
    assert capsule["task"]["expectedReturnStatus"] == EXPECTED_RETURN_STATUS
    assert capsule["sourceRepositories"][0]["licenseExpression"] == "MIT"
    assert capsule["authorityEnvelope"]["commit"] is False
    assert capsule["task"]["shortObjectivePolicy"] == "FOCUS_WITHIN_CAPSULE_ENVELOPE_NO_STRING_EQUALITY"
    assert capsule["cvfPublicSource"]["comparisonBaseline"] == "TASK_CAPSULE_PIN_NORMATIVE"


def test_foreign_host_output_root_rebind_preserves_request() -> None:
    result = resolve_output_root("D:/operator/out", "/workspace/artifacts/out", "/workspace/artifacts", False)
    assert result["requestedOutputRoot"] == "D:/operator/out"
    assert result["actualOutputRoot"] == "/workspace/artifacts/out"
    assert result["outputRootDisposition"] == "OUTPUT_ROOT_REBOUND"


def test_usable_output_root_is_not_rebound() -> None:
    result = resolve_output_root("/workspace/out", "/ignored", "/workspace", True)
    assert result["outputRootDisposition"] == "REQUESTED_OUTPUT_ROOT_USED"
    assert result["actualOutputRoot"] == "/workspace/out"


def test_output_rebind_outside_authorized_root_fails() -> None:
    with pytest.raises(PacketError, match="outside the authorized"):
        resolve_output_root("D:/operator/out", "/tmp/out", "/workspace", False)


def test_public_cvf_pin_match_passes_and_drift_never_repins() -> None:
    assert resolve_public_cvf_pin("a" * 40, "a" * 40)["status"] == "PASS"
    drift = resolve_public_cvf_pin("a" * 40, "b" * 40)
    assert drift["status"] == "PUBLIC_CVF_PIN_DRIFT_RECORDED"
    assert drift["comparisonCommit"] == "a" * 40


def test_return_mapping_against_unpinned_public_commit_fails() -> None:
    with pytest.raises(PacketError, match="normative task-capsule pin"):
        validate_return_cvf_pin("a" * 40, "b" * 40)


def test_short_objective_and_deeper_focus_do_not_create_drift(tmp_path: Path) -> None:
    capsule = create_source_capsule(_args(tmp_path), "a" * 40, SOURCE_POSTURE_LIVE)
    assert classify_task_capsule_drift(capsule, short_objective="xem repo nay") == "NO_TASK_CAPSULE_DRIFT"
    assert classify_task_capsule_drift(capsule, short_objective="audit security more deeply") == "NO_TASK_CAPSULE_DRIFT"


def test_different_repo_or_forbidden_effect_creates_drift(tmp_path: Path) -> None:
    capsule = create_source_capsule(_args(tmp_path), "a" * 40, SOURCE_POSTURE_LIVE)
    assert classify_task_capsule_drift(capsule, requested_repository="https://github.com/example/other.git") == "TASK_CAPSULE_DRIFT"
    assert classify_task_capsule_drift(capsule, forbidden_effect_requested=True) == "TASK_CAPSULE_DRIFT"


def test_source_capsule_requires_license_expression(tmp_path: Path) -> None:
    args = _args(tmp_path)
    args.source_license_expression = " "
    with pytest.raises(PacketError, match="non-blank"):
        create_source_capsule(args, "a" * 40, SOURCE_POSTURE_LIVE)


def test_source_capsule_requires_commit_bound_license_source(tmp_path: Path) -> None:
    args = _args(tmp_path)
    args.source_license_source = "https://github.com/example/repo/blob/main/LICENSE"
    with pytest.raises(PacketError, match="license-source"):
        create_source_capsule(args, "a" * 40, SOURCE_POSTURE_LIVE)


def test_source_capsule_requires_immutable_reference(tmp_path: Path) -> None:
    args = _args(tmp_path)
    args.source_immutable_reference = []
    with pytest.raises(PacketError, match="at least one"):
        create_source_capsule(args, "a" * 40, SOURCE_POSTURE_LIVE)


def test_source_capsule_rejects_moving_reference(tmp_path: Path) -> None:
    args = _args(tmp_path)
    args.source_immutable_reference = ["https://github.com/example/repo/blob/main/README.md"]
    with pytest.raises(PacketError, match="exact source commit"):
        create_source_capsule(args, "a" * 40, SOURCE_POSTURE_LIVE)


def test_source_capsule_rejects_malformed_public_commit(tmp_path: Path) -> None:
    with pytest.raises(PacketError, match="public CVF commit"):
        create_source_capsule(_args(tmp_path), "not-a-sha", SOURCE_POSTURE_LIVE)

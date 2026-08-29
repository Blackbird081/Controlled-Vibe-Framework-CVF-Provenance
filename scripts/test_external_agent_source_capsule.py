from __future__ import annotations

from argparse import Namespace
from pathlib import Path

import pytest

from scripts.external_agent_packet import SOURCE_POSTURE_LIVE, PacketError
from scripts.external_agent_source_capsule import EXPECTED_RETURN_STATUS, create_source_capsule


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

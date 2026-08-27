from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from argparse import Namespace
from pathlib import Path

import jsonschema
import pytest

from scripts.external_agent_packet import (
    SOURCE_POSTURE_LIVE,
    SOURCE_POSTURE_OFFLINE,
    PacketError,
    _update_snapshot_text,
    create_capsule,
    create_capsule_offline,
    load_context_groups,
    validate_return,
)


CAPSULE_SCHEMA_PATH = Path("docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json")


def _load_capsule_schema() -> dict:
    return json.loads(CAPSULE_SCHEMA_PATH.read_text(encoding="utf-8"))


def _valid_context_groups() -> dict:
    return {
        "protectedPaths": {
            "consumers": ["worker"],
            "freshness": {"anchor": "dispatch base head", "regenerateWhen": "base head changes"},
            "paths": ["governance/compat/", "AGENTS.md"],
        },
        "ownerMap": {
            "consumers": ["worker", "reviewer"],
            "freshness": {"anchor": "current HEAD source read", "regenerateWhen": "owner file content changes"},
            "owners": [
                {
                    "path": "scripts/external_agent_packet.py",
                    "symbol": "create_capsule",
                    "version": "1.1.0",
                    "competingOwnersChecked": ["none found"],
                }
            ],
        },
        "invariants": {
            "consumers": ["worker", "reviewer"],
            "freshness": {"anchor": "work order Required Implementation Contract", "regenerateWhen": "contract text changes"},
            "mustPreserve": ["strict schema additionalProperties false"],
            "forbiddenTransitions": ["must not widen authorityEnvelope"],
        },
        "verification": {
            "consumers": ["worker", "return validator"],
            "freshness": {"anchor": "pinned Verification Commands section", "regenerateWhen": "command list changes"},
            "focusedTests": ["pytest scripts/test_external_agent_packet.py"],
            "negativeCases": ["missing group fails"],
            "deterministicChecks": ["git status --short empty"],
            "requiredOutputs": ["six-path changed set"],
        },
    }


def _base_task_args(tmp_path: Path, working_mode: str = "EXTEND_SUPPLIED_REPOSITORY") -> Namespace:
    return Namespace(
        packet_root=str(tmp_path),
        task_id="t1",
        title="Title",
        objective="Objective",
        working_mode=working_mode,
        source_repository="https://github.com/example/repo.git",
        source_commit="b" * 40,
        output_root="D:/out",
        non_goal=[],
    )


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _make_return(root: Path) -> None:
    root.mkdir()
    authority = (
        "artifactClass: PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE\n"
        "authorityStatus: NON_AUTHORITATIVE_UNTIL_REVIEWED\n"
    )
    for name in ("README.md", "SOURCE_MANIFEST.md", "DECISION_LOG.md", "TEST_EVIDENCE.md", "CLAIM_BOUNDARY.md"):
        (root / name).write_text(authority if name == "README.md" else f"# {name}\n", encoding="utf-8", newline="\n")
    manifest = {
        "schema": "cvf.externalAgentReturn.v1",
        "artifactClass": "PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE",
        "authorityStatus": "NON_AUTHORITATIVE_UNTIL_REVIEWED",
        "task": {"title": "Example", "objective": "Test", "date": "2026-08-23", "nonGoals": []},
        "cvfPublicSource": {
            "repository": "https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git",
            "commit": "a" * 40,
            "pathsRead": ["README.md"],
        },
        "sources": [{
            "id": "SRC-001",
            "repository": "https://github.com/example/repo.git",
            "commit": "b" * 40,
            "immutableReference": f"https://github.com/example/repo/blob/{'b' * 40}/README.md",
            "licenseExpression": "MIT",
            "licenseSource": f"https://github.com/example/repo/blob/{'b' * 40}/LICENSE",
            "usageType": "REFERENCE_ONLY",
            "ownerSurface": "docs/reference/example.md",
            "overlapDisposition": "ENRICH_EXISTING",
        }],
        "origins": [],
        "files": [],
        "excludedPaths": [],
        "dependencies": [],
        "verification": {"commands": [{"command": "pytest", "executed": True, "result": "PASS", "testClass": "negative"}], "passed": 1, "failed": 0, "skipped": 0, "liveCalls": 0},
        "externalEffects": [],
        "secretsReturned": False,
        "knownLimitations": [],
        "unresolvedQuestions": [],
        "suggestedAbsorptionCandidates": [],
    }
    manifest_path = root / "EXTERNAL_AGENT_RETURN_MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")
    manifest["files"] = [
        {"path": path.name, "sha256": _sha(path), "role": "evidence", "originIds": []}
        for path in sorted(root.iterdir(), key=lambda item: item.name)
        if path.name != "EXTERNAL_AGENT_RETURN_MANIFEST.json"
    ]
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")
    inventory = [
        f"{_sha(path)}  {path.name}"
        for path in sorted(root.iterdir(), key=lambda item: item.name)
        if path.name != "FILE_INVENTORY.sha256"
    ]
    (root / "FILE_INVENTORY.sha256").write_text("\n".join(inventory) + "\n", encoding="utf-8", newline="\n")


def test_update_snapshot_requires_exact_fields() -> None:
    original = """protocolVersion: 1.0.0
updatedAt: 2026-01-01
Verified: 2026-01-01 (Asia/Ho_Chi_Minh)
Audit-anchor commit:
`1111111111111111111111111111111111111111`
Commit date: `old`
Commit subject: `old`
contained 1 entries;
"""
    from datetime import datetime
    from zoneinfo import ZoneInfo
    updated = _update_snapshot_text(original, "a" * 40, "2026-08-23T00:00:00+07:00", "new", 8231, datetime(2026, 8, 23, tzinfo=ZoneInfo("Asia/Ho_Chi_Minh")))
    assert "protocolVersion: 1.1.0" in updated
    assert "`" + "a" * 40 + "`" in updated
    assert "contained 8,231 entries;" in updated


def test_update_snapshot_fails_when_shape_drifts() -> None:
    from datetime import datetime
    from zoneinfo import ZoneInfo
    with pytest.raises(PacketError):
        _update_snapshot_text("no managed fields", "a" * 40, "date", "subject", 1, datetime.now(ZoneInfo("Asia/Ho_Chi_Minh")))


def test_validate_return_pass_and_semantic_failure(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "PASS", receipt["errors"]

    manifest_path = root / "EXTERNAL_AGENT_RETURN_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["sources"][0]["immutableReference"] = "https://github.com/example/repo/blob/main/README.md"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")
    inventory_lines = []
    for path in sorted(root.iterdir(), key=lambda item: item.name):
        if path.name != "FILE_INVENTORY.sha256":
            inventory_lines.append(f"{_sha(path)}  {path.name}")
    (root / "FILE_INVENTORY.sha256").write_text("\n".join(inventory_lines) + "\n", encoding="utf-8", newline="\n")
    receipt = validate_return(root, tmp_path / "receipt2.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("immutableReference" in error for error in receipt["errors"])


def test_validate_return_rejects_mismatched_license_commit(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    manifest_path = root / "EXTERNAL_AGENT_RETURN_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["sources"][0]["licenseSource"] = f"https://github.com/example/repo/blob/{'c' * 40}/LICENSE"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")
    inventory_lines = [f"{_sha(path)}  {path.name}" for path in sorted(root.iterdir(), key=lambda item: item.name) if path.name != "FILE_INVENTORY.sha256"]
    (root / "FILE_INVENTORY.sha256").write_text("\n".join(inventory_lines) + "\n", encoding="utf-8", newline="\n")
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("licenseSource SHA" in error for error in receipt["errors"])


def test_cli_returns_nonzero_for_invalid_return(tmp_path: Path) -> None:
    root = tmp_path / "empty"
    root.mkdir()
    proc = subprocess.run(
        ["python", "scripts/external_agent_packet.py", "validate-return", "--return-root", str(root)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert proc.returncode == 1


def test_validate_return_cli_remains_standard_library_only(tmp_path: Path) -> None:
    root = tmp_path / "empty"
    root.mkdir()
    blocker = tmp_path / "blocked_dependency"
    blocker.mkdir()
    (blocker / "jsonschema.py").write_text(
        "raise ModuleNotFoundError('jsonschema deliberately unavailable')\n",
        encoding="utf-8",
    )
    env = os.environ.copy()
    env["PYTHONPATH"] = str(blocker) + os.pathsep + env.get("PYTHONPATH", "")
    proc = subprocess.run(
        [sys.executable, "scripts/external_agent_packet.py", "validate-return", "--return-root", str(root)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    assert proc.returncode == 1
    assert "RETURN_FOR_REPAIR" in proc.stdout
    assert "ModuleNotFoundError" not in proc.stderr


def test_generated_task_capsule_matches_strict_schema(tmp_path: Path) -> None:
    args = Namespace(
        packet_root=str(tmp_path),
        task_id="repo-review-001",
        title="Review repository",
        objective="Produce an absorption-ready return",
        working_mode="SOURCE_PACK_PREPARATION",
        source_repository="https://github.com/example/repository.git",
        source_commit="b" * 40,
        output_root="D:/OUTPUT/repository-review",
        non_goal=["No push", "No provider calls"],
    )
    capsule = create_capsule(args, "a" * 40)
    schema = json.loads(Path("docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json").read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(capsule)
    assert capsule["authorityEnvelope"]["push"] is False

    widened = json.loads(json.dumps(capsule))
    widened["authorityEnvelope"]["dispatchAllowed"] = True
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.Draft202012Validator(schema).validate(widened)


# --- EACQ-FV-MV2: four context groups plus offline creation route ---------


def test_strict_valid_capsule_with_all_four_groups(tmp_path: Path) -> None:
    args = _base_task_args(tmp_path)
    capsule = create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=_valid_context_groups())
    schema = _load_capsule_schema()
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(capsule)
    for group in ("protectedPaths", "ownerMap", "invariants", "verification"):
        assert group in capsule
    assert capsule["cvfPublicSource"]["sourcePosture"] == SOURCE_POSTURE_LIVE


@pytest.mark.parametrize("missing_group", ["protectedPaths", "ownerMap", "invariants", "verification"])
def test_each_missing_group_fails_for_context_required_mode(tmp_path: Path, missing_group: str) -> None:
    groups = _valid_context_groups()
    del groups[missing_group]
    args = _base_task_args(tmp_path, working_mode="EXTEND_SUPPLIED_REPOSITORY")
    with pytest.raises(PacketError, match=missing_group):
        create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=groups)


def test_review_only_mode_does_not_require_context_groups(tmp_path: Path) -> None:
    args = _base_task_args(tmp_path, working_mode="REVIEW_ONLY")
    capsule = create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=None)
    schema = _load_capsule_schema()
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(capsule)
    for group in ("protectedPaths", "ownerMap", "invariants", "verification"):
        assert group not in capsule


@pytest.mark.parametrize(
    "mutator",
    [
        lambda g: g["protectedPaths"].update({"paths": []}),
        lambda g: g["protectedPaths"].update({"consumers": []}),
        lambda g: g["protectedPaths"].update({"unknownKey": "x"}),
        lambda g: g["ownerMap"]["owners"][0].pop("symbol"),
        lambda g: g["invariants"].update({"mustPreserve": []}),
        lambda g: g["verification"].update({"focusedTests": []}),
    ],
)
def test_empty_unknown_or_malformed_group_content_fails(tmp_path: Path, mutator) -> None:
    groups = _valid_context_groups()
    mutator(groups)
    args = _base_task_args(tmp_path)
    with pytest.raises(PacketError, match="strict schema validation"):
        create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=groups)


def test_duplicate_protected_path_fails(tmp_path: Path) -> None:
    groups = _valid_context_groups()
    groups["protectedPaths"]["paths"] = ["AGENTS.md", "AGENTS.md"]
    args = _base_task_args(tmp_path)
    with pytest.raises(PacketError, match="strict schema validation"):
        create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=groups)


@pytest.mark.parametrize(
    "unsafe_path",
    [
        "../../etc/passwd",
        "C:/Windows/System32",
        "https://evil.example/path",
        "./AGENTS.md",
        ".",
        "governance//compat/",
        " AGENTS.md",
        "AGENTS.md ",
        "governance\\compat\\",
    ],
)
def test_unsafe_protected_path_fails(tmp_path: Path, unsafe_path: str) -> None:
    groups = _valid_context_groups()
    groups["protectedPaths"]["paths"] = [unsafe_path]
    args = _base_task_args(tmp_path)
    with pytest.raises(PacketError, match="strict schema validation"):
        create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=groups)


@pytest.mark.parametrize("valid_path", ["AGENTS.md", "governance/compat/", "docs/reference/example.md"])
def test_repo_relative_protected_path_is_accepted(tmp_path: Path, valid_path: str) -> None:
    groups = _valid_context_groups()
    groups["protectedPaths"]["paths"] = [valid_path]
    args = _base_task_args(tmp_path)
    capsule = create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=groups)
    assert capsule["protectedPaths"]["paths"] == [valid_path]


def test_owner_path_symbol_and_competing_owners_preserved_exactly(tmp_path: Path) -> None:
    groups = _valid_context_groups()
    args = _base_task_args(tmp_path)
    capsule = create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=groups)
    owner = capsule["ownerMap"]["owners"][0]
    assert owner["path"] == "scripts/external_agent_packet.py"
    assert owner["symbol"] == "create_capsule"
    assert owner["competingOwnersChecked"] == ["none found"]


def test_invariants_and_forbidden_transitions_preserved_exactly(tmp_path: Path) -> None:
    groups = _valid_context_groups()
    args = _base_task_args(tmp_path)
    capsule = create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=groups)
    assert capsule["invariants"]["mustPreserve"] == ["strict schema additionalProperties false"]
    assert capsule["invariants"]["forbiddenTransitions"] == ["must not widen authorityEnvelope"]


def test_verification_items_preserved_exactly(tmp_path: Path) -> None:
    groups = _valid_context_groups()
    args = _base_task_args(tmp_path)
    capsule = create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=groups)
    verification = capsule["verification"]
    assert verification["focusedTests"] == ["pytest scripts/test_external_agent_packet.py"]
    assert verification["negativeCases"] == ["missing group fails"]
    assert verification["deterministicChecks"] == ["git status --short empty"]
    assert verification["requiredOutputs"] == ["six-path changed set"]


def test_live_preparation_path_records_live_verified_source_posture(tmp_path: Path) -> None:
    args = _base_task_args(tmp_path, working_mode="REVIEW_ONLY")
    capsule = create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE)
    assert capsule["cvfPublicSource"]["sourcePosture"] == SOURCE_POSTURE_LIVE


def test_offline_path_records_pinned_not_live_verified_posture(tmp_path: Path) -> None:
    context_path = tmp_path / "context.json"
    context_path.write_text(json.dumps(_valid_context_groups()), encoding="utf-8")
    args = _base_task_args(tmp_path)
    args.context_file = str(context_path)
    args.cvf_public_commit = "c" * 40
    capsule = create_capsule_offline(args)
    assert capsule["cvfPublicSource"]["sourcePosture"] == SOURCE_POSTURE_OFFLINE
    assert capsule["cvfPublicSource"]["commit"] == "c" * 40


def test_offline_path_makes_zero_network_or_git_remote_calls(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Patch subprocess.run (the sole Git/network entrypoint in this module)
    to fail if invoked; the offline route must not call it at all."""
    import scripts.external_agent_packet as packet_module

    def _forbidden_subprocess_run(*_args, **_kwargs):
        raise AssertionError("offline capsule creation must not invoke subprocess.run (Git/network)")

    monkeypatch.setattr(packet_module.subprocess, "run", _forbidden_subprocess_run)

    context_path = tmp_path / "context.json"
    context_path.write_text(json.dumps(_valid_context_groups()), encoding="utf-8")
    args = _base_task_args(tmp_path)
    args.context_file = str(context_path)
    args.cvf_public_commit = "c" * 40
    capsule = create_capsule_offline(args)
    assert capsule["cvfPublicSource"]["sourcePosture"] == SOURCE_POSTURE_OFFLINE


def test_invalid_offline_input_does_not_overwrite_existing_capsule(tmp_path: Path) -> None:
    capsule_path = tmp_path / "CVF_EXTERNAL_AGENT_TASK_CAPSULE.json"
    original_bytes = b'{"marker": "pre-existing valid capsule, must survive a failed offline attempt"}'
    capsule_path.write_bytes(original_bytes)

    bad_context_path = tmp_path / "bad_context.json"
    bad_context_path.write_text(json.dumps({"protectedPaths": {"paths": []}}), encoding="utf-8")
    args = _base_task_args(tmp_path)
    args.context_file = str(bad_context_path)
    args.cvf_public_commit = "c" * 40
    with pytest.raises(PacketError):
        create_capsule_offline(args)

    assert capsule_path.read_bytes() == original_bytes


def test_offline_context_file_missing_fails_with_packet_error(tmp_path: Path) -> None:
    args = _base_task_args(tmp_path)
    args.context_file = str(tmp_path / "does_not_exist.json")
    args.cvf_public_commit = "c" * 40
    with pytest.raises(PacketError, match="context file not found"):
        create_capsule_offline(args)


def test_offline_context_file_invalid_json_fails(tmp_path: Path) -> None:
    context_path = tmp_path / "context.json"
    context_path.write_text("{not valid json", encoding="utf-8")
    args = _base_task_args(tmp_path)
    args.context_file = str(context_path)
    args.cvf_public_commit = "c" * 40
    with pytest.raises(PacketError, match="invalid JSON"):
        create_capsule_offline(args)


def test_offline_context_file_unknown_group_fails(tmp_path: Path) -> None:
    groups = _valid_context_groups()
    groups["unknownGroup"] = {"x": 1}
    context_path = tmp_path / "context.json"
    context_path.write_text(json.dumps(groups), encoding="utf-8")
    args = _base_task_args(tmp_path)
    args.context_file = str(context_path)
    args.cvf_public_commit = "c" * 40
    with pytest.raises(PacketError, match="unknown group"):
        create_capsule_offline(args)


def test_offline_invalid_public_commit_fails(tmp_path: Path) -> None:
    context_path = tmp_path / "context.json"
    context_path.write_text(json.dumps(_valid_context_groups()), encoding="utf-8")
    args = _base_task_args(tmp_path)
    args.context_file = str(context_path)
    args.cvf_public_commit = "not-a-sha"
    with pytest.raises(PacketError, match="40-character Git SHA"):
        create_capsule_offline(args)


def test_load_context_groups_round_trips_valid_file(tmp_path: Path) -> None:
    context_path = tmp_path / "context.json"
    groups = _valid_context_groups()
    context_path.write_text(json.dumps(groups), encoding="utf-8")
    loaded = load_context_groups(context_path)
    assert loaded == groups


def test_prepare_task_cli_exposes_context_file_option() -> None:
    """Source-inspected: the prepare-task subparser must accept --context-file
    without executing any network operation."""
    from scripts.external_agent_packet import _build_parser

    parser = _build_parser()
    prepare_actions = {
        action.dest for action in parser._subparsers._group_actions[0].choices["prepare-task"]._actions  # type: ignore[attr-defined]
    }
    assert "context_file" in prepare_actions


def test_create_capsule_offline_cli_subcommand_registered() -> None:
    """Source-inspected: create-capsule-offline must be a registered
    subcommand exposing the pinned-commit and context-file arguments."""
    from scripts.external_agent_packet import _build_parser

    parser = _build_parser()
    choices = parser._subparsers._group_actions[0].choices  # type: ignore[attr-defined]
    assert "create-capsule-offline" in choices
    offline_actions = {action.dest for action in choices["create-capsule-offline"]._actions}
    assert {"packet_root", "cvf_public_commit", "context_file", "task_id"}.issubset(offline_actions)


def test_existing_return_validation_tests_remain_passing(tmp_path: Path) -> None:
    """Non-regression sentinel: validate_return continues to accept the same
    minimal valid return shape used by the pre-existing suite."""
    root = tmp_path / "returned"
    _make_return(root)
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "PASS", receipt["errors"]

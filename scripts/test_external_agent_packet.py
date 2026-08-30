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
    CANDIDATE_CONTRACT_VERSION,
    LANE_CVF_INTERNAL_DEFECT,
    LANE_EXTERNAL_SOURCE_VALUE,
    PRELIMINARY_VALUE_DISPOSITIONS,
    PROTOCOL_VERSION,
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
        execution_class=None,
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
    assert f"protocolVersion: {PROTOCOL_VERSION}" in updated
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


def test_detached_implementation_capsule_requires_execution_class_and_context(tmp_path: Path) -> None:
    args = _base_task_args(tmp_path, working_mode="DETACHED_IMPLEMENTATION_PROPOSAL")
    with pytest.raises(PacketError, match="execution-class is required"):
        create_capsule(args, "a" * 40, context_groups=_valid_context_groups())
    args.execution_class = "DETACHED_EXTERNAL_AGENT"
    with pytest.raises(PacketError, match="requires all four context groups"):
        create_capsule(args, "a" * 40, context_groups=None)
    capsule = create_capsule(args, "a" * 40, context_groups=_valid_context_groups())
    assert capsule["task"]["executionClass"] == "DETACHED_EXTERNAL_AGENT" and capsule["task"]["expectedReturnStatus"] == "EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION"


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
def test_owner_missing_competing_owners_checked_fails(tmp_path: Path) -> None:
    groups = _valid_context_groups()
    del groups["ownerMap"]["owners"][0]["competingOwnersChecked"]
    args = _base_task_args(tmp_path)
    with pytest.raises(PacketError, match="strict schema validation"):
        create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=groups)


def test_owner_empty_competing_owners_checked_fails(tmp_path: Path) -> None:
    groups = _valid_context_groups()
    groups["ownerMap"]["owners"][0]["competingOwnersChecked"] = []
    args = _base_task_args(tmp_path)
    with pytest.raises(PacketError, match="strict schema validation"):
        create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=groups)


@pytest.mark.parametrize("blank_item", [" ", "\t", "  \t  ", "\n"])
def test_owner_whitespace_only_competing_owners_item_fails(tmp_path: Path, blank_item: str) -> None:
    groups = _valid_context_groups()
    groups["ownerMap"]["owners"][0]["competingOwnersChecked"] = [blank_item]
    args = _base_task_args(tmp_path)
    with pytest.raises(PacketError, match="strict schema validation"):
        create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=groups)


def test_owner_duplicate_competing_owners_item_fails(tmp_path: Path) -> None:
    groups = _valid_context_groups()
    groups["ownerMap"]["owners"][0]["competingOwnersChecked"] = ["same finding", "same finding"]
    args = _base_task_args(tmp_path)
    with pytest.raises(PacketError, match="strict schema validation"):
        create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=groups)


def test_owner_exact_duplicate_owner_record_fails(tmp_path: Path) -> None:
    groups = _valid_context_groups()
    groups["ownerMap"]["owners"].append(dict(groups["ownerMap"]["owners"][0]))
    args = _base_task_args(tmp_path)
    with pytest.raises(PacketError, match="strict schema validation"):
        create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=groups)


def test_owner_valid_non_blank_competing_owners_evidence_still_passes(tmp_path: Path) -> None:
    groups = _valid_context_groups()
    args = _base_task_args(tmp_path)
    capsule = create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=groups)
    schema = _load_capsule_schema()
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(capsule)
    assert capsule["ownerMap"]["owners"][0]["competingOwnersChecked"] == ["none found"]


def test_owner_two_distinct_owner_records_still_pass(tmp_path: Path) -> None:
    groups = _valid_context_groups()
    second_owner = dict(groups["ownerMap"]["owners"][0])
    second_owner["path"] = "scripts/test_external_agent_packet.py"
    second_owner["symbol"] = "_valid_context_groups"
    second_owner["competingOwnersChecked"] = ["distinct from first owner"]
    groups["ownerMap"]["owners"].append(second_owner)
    args = _base_task_args(tmp_path)
    capsule = create_capsule(args, "a" * 40, source_posture=SOURCE_POSTURE_LIVE, context_groups=groups)
    schema = _load_capsule_schema()
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(capsule)
    assert len(capsule["ownerMap"]["owners"]) == 2


def test_paired_ev1_task_capsule_validates_against_current_schema() -> None:
    """The committed EACQ-FV-EV1 task capsule JSON must itself validate
    against the schema this tranche hardens, proving the dispatcher's own
    ownerMap evidence satisfies the new requirement."""
    capsule_path = Path("docs/work_orders/CVF_EACQ_FV_EV1_CAPSULE_ENHANCED_OWNER_MAP_EVIDENCE_TASK_CAPSULE_2026-08-28.json")
    capsule = json.loads(capsule_path.read_text(encoding="utf-8"))
    schema = _load_capsule_schema()
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(capsule)
    for owner in capsule["ownerMap"]["owners"]:
        assert owner["competingOwnersChecked"]
        assert all(item.strip() for item in owner["competingOwnersChecked"])


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
def _rewrite_manifest(root: Path, mutator) -> dict:
    manifest_path = root / "EXTERNAL_AGENT_RETURN_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    mutator(manifest)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")
    inventory_lines = [f"{_sha(path)}  {path.name}" for path in sorted(root.iterdir(), key=lambda item: item.name) if path.name != "FILE_INVENTORY.sha256"]
    (root / "FILE_INVENTORY.sha256").write_text("\n".join(inventory_lines) + "\n", encoding="utf-8", newline="\n")
    return manifest


def _source_value_candidate(candidate_id: str = "ESC-001") -> dict:
    return {
        "candidateId": candidate_id,
        "preliminaryLane": LANE_EXTERNAL_SOURCE_VALUE,
        "sourceRefs": ["SRC-001"],
        "sourceLocations": [{"sourceRef": "SRC-001", "path": "path/to/file.py", "symbols": ["SymbolName"]}],
        "candidateSummary": "atomic reusable source pattern",
        "claimedValue": "source-bounded statement of why the pattern may matter",
        "publicOwnerSearch": {"status": "OWNER_CANDIDATES_FOUND", "candidates": [{"path": "public/path", "symbol": "SymbolName", "basis": "public evidence"}]},
        "publicOverlap": {"status": "PUBLIC_SUGGESTS_ENRICHMENT", "basis": "public-evidence-only comparison"},
        "preliminaryValueDisposition": "ADAPT",
        "questionsForLocalAgent": ["exact current-owner question"],
    }


def _internal_defect_candidate(candidate_id: str = "ESC-002") -> dict:
    return {
        "candidateId": candidate_id,
        "preliminaryLane": LANE_CVF_INTERNAL_DEFECT,
        "cvfPublicLocations": [{"path": "public/cvf/path.py", "symbols": ["SymbolName"]}],
        "triggerContextSourceRefs": ["SRC-001"],
        "candidateSummary": "bounded public-CVF defect hypothesis",
        "publicOwnerSearch": {"status": "OWNER_CANDIDATES_FOUND", "candidates": [{"path": "public/cvf/owner/path.py", "symbol": "SymbolName", "basis": "public evidence"}]},
        "questionsForLocalAgent": ["verify whether this exists in current local CVF"],
    }


def test_strict_v1_empty_candidate_collection_passes(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": CANDIDATE_CONTRACT_VERSION, "suggestedAbsorptionCandidates": []}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "PASS", receipt["errors"]
    assert receipt["candidateContractStatus"] == "STRICT_V1"
    assert receipt["validatedCandidateContractVersion"] == CANDIDATE_CONTRACT_VERSION


def test_strict_v1_valid_source_value_candidate_passes(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [_source_value_candidate()]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "PASS", receipt["errors"]


def test_strict_v1_valid_internal_defect_candidate_passes(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [_internal_defect_candidate()]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "PASS", receipt["errors"]


def test_strict_v1_both_lanes_together_pass(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    _rewrite_manifest(root, lambda m: m.update({
        "candidateContractVersion": 1,
        "suggestedAbsorptionCandidates": [_source_value_candidate("ESC-001"), _internal_defect_candidate("ESC-002")],
    }))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "PASS", receipt["errors"]


def test_strict_v1_duplicate_candidate_ids_fail(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    _rewrite_manifest(root, lambda m: m.update({
        "candidateContractVersion": 1,
        "suggestedAbsorptionCandidates": [_source_value_candidate("ESC-001"), _internal_defect_candidate("ESC-001")],
    }))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("duplicate" in error.lower() for error in receipt["errors"])


def test_strict_v1_internal_defect_with_forbidden_source_value_fields_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    contaminated = _internal_defect_candidate()
    contaminated["claimedValue"] = "should not be here"
    contaminated["sourceLocations"] = [{"sourceRef": "SRC-001", "path": "x", "symbols": ["Y"]}]
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [contaminated]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("forbidden" in error.lower() for error in receipt["errors"])


def test_strict_v1_unknown_lane_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    bad = _source_value_candidate()
    bad["preliminaryLane"] = "SOMETHING_ELSE"
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [bad]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("preliminaryLane" in error for error in receipt["errors"])


@pytest.mark.parametrize(
    "field",
    ["candidateId", "sourceRefs", "sourceLocations", "candidateSummary", "claimedValue", "publicOwnerSearch", "publicOverlap", "preliminaryValueDisposition"],
)
def test_strict_v1_source_value_missing_required_field_fails(tmp_path: Path, field: str) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    del candidate[field]
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"


def test_strict_v1_source_value_blank_summary_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["candidateSummary"] = "   "
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("candidateSummary" in error for error in receipt["errors"])


@pytest.mark.parametrize("unsafe_path", ["../../etc/passwd", "/abs/path"])
def test_strict_v1_source_value_unsafe_location_path_fails(tmp_path: Path, unsafe_path: str) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["sourceLocations"][0]["path"] = unsafe_path
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"


def test_strict_v1_source_value_invalid_enum_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["publicOwnerSearch"]["status"] = "NOT_A_REAL_STATUS"
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("publicOwnerSearch" in error for error in receipt["errors"])


def test_strict_v1_source_value_missing_source_id_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["sourceRefs"] = ["SRC-DOES-NOT-EXIST"]
    candidate["sourceLocations"][0]["sourceRef"] = "SRC-DOES-NOT-EXIST"
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("unresolved source id" in error for error in receipt["errors"])


def test_strict_v1_source_value_unresolved_location_ref_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["sourceLocations"][0]["sourceRef"] = "SRC-OTHER"
    candidate["sourceRefs"] = ["SRC-001", "SRC-OTHER"]
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"


def test_strict_v1_source_value_multiple_locations_for_one_ref_still_passes(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["sourceRefs"] = ["SRC-001"]
    candidate["sourceLocations"] = [
        {"sourceRef": "SRC-001", "path": "a.py", "symbols": ["A"]},
        {"sourceRef": "SRC-001", "path": "b.py", "symbols": ["B"]},
    ]
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "PASS", receipt["errors"]


def test_strict_v1_source_value_set_equality_violation_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["sourceLocations"] = [{"sourceRef": "SRC-001", "path": "a.py", "symbols": ["A"]}]

    def _mutator(m: dict) -> None:
        m["sources"].append({**m["sources"][0], "id": "SRC-002"})
        candidate["sourceRefs"] = ["SRC-001", "SRC-002"]
        m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]})

    _rewrite_manifest(root, _mutator)
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("set(sourceRefs)" in error for error in receipt["errors"])


def test_strict_v1_internal_defect_missing_owner_search_without_local_question_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _internal_defect_candidate()
    candidate["publicOwnerSearch"] = {"status": "OWNER_CANDIDATES_FOUND", "candidates": []}
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("publicOwnerSearch.candidates" in error for error in receipt["errors"])


def test_strict_v1_internal_defect_unresolved_trigger_ref_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _internal_defect_candidate()
    candidate["triggerContextSourceRefs"] = ["SRC-MISSING"]
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("triggerContextSourceRefs" in error for error in receipt["errors"])


def test_legacy_empty_candidates_accepted_without_typed_claim(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "PASS", receipt["errors"]
    assert receipt["candidateContractStatus"] == "LEGACY_EMPTY"
    assert receipt["validatedCandidateContractVersion"] is None


def test_legacy_non_empty_candidates_not_promotable(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    _rewrite_manifest(root, lambda m: m.update({"suggestedAbsorptionCandidates": [{"freeform": "untyped legacy row"}]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "PASS", receipt["errors"]
    assert receipt["candidateContractStatus"] == "LEGACY_UNTYPED_NOT_PROMOTABLE"
    assert receipt["validatedCandidateContractVersion"] is None


def test_malformed_discriminator_returns_unsupported_and_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 2, "suggestedAbsorptionCandidates": []}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert receipt["candidateContractStatus"] == "UNSUPPORTED_OR_MALFORMED"


def test_malformed_discriminator_string_type_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": "1", "suggestedAbsorptionCandidates": []}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert receipt["candidateContractStatus"] == "UNSUPPORTED_OR_MALFORMED"


def test_strict_v1_invalid_row_fails_closed(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [{"candidateId": "X"}]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"


def test_receipt_binds_exact_manifest_protocol_and_candidate_version(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": []}))
    manifest_path = root / "EXTERNAL_AGENT_RETURN_MANIFEST.json"
    expected_sha = _sha(manifest_path)
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "PASS", receipt["errors"]
    assert receipt["validatedReturnManifestSha256"] == expected_sha
    assert receipt["validatedProtocolVersion"] == "1.3.0" == PROTOCOL_VERSION
    assert receipt["validatedCandidateContractVersion"] == CANDIDATE_CONTRACT_VERSION


def test_receipt_for_another_manifest_has_different_hash(tmp_path: Path) -> None:
    root_a = tmp_path / "returned_a"
    root_b = tmp_path / "returned_b"
    _make_return(root_a)
    _make_return(root_b)
    _rewrite_manifest(root_a, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": []}))
    _rewrite_manifest(root_b, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [], "task": {"title": "Different", "objective": "Different", "date": "2026-08-29", "nonGoals": []}}))
    receipt_a = validate_return(root_a, tmp_path / "receipt_a.json")
    receipt_b = validate_return(root_b, tmp_path / "receipt_b.json")
    assert receipt_a["validatedReturnManifestSha256"] != receipt_b["validatedReturnManifestSha256"]


def test_receipt_candidate_version_mismatch_is_visible_as_none_for_legacy(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "PASS", receipt["errors"]
    assert receipt["validatedCandidateContractVersion"] is None
    assert receipt["candidateContractStatus"] != "STRICT_V1"


def test_strict_v1_manifest_with_legacy_unaware_receipt_is_insufficient_for_typed_reconciliation(tmp_path: Path) -> None:
    """Simulates Local reconciliation's required equality check: a PASS
    receipt that never enforced candidate semantics (candidateContractStatus
    != STRICT_V1) cannot satisfy externalReturnBinding.candidateContractVersion
    == receipt.validatedCandidateContractVersion for a strict-v1 binding."""
    root = tmp_path / "returned"
    _make_return(root)
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "PASS"
    external_return_binding_candidate_contract_version = 1
    assert external_return_binding_candidate_contract_version != receipt["validatedCandidateContractVersion"]


def test_candidate_validation_pass_does_not_widen_authority_or_semantic_acceptance(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [_source_value_candidate()]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "PASS", receipt["errors"]
    assert receipt["claimBoundary"] == "Structural, integrity, and bounded semantic intake validation only; not CVF acceptance or absorption approval."
    assert "implementationAuthorized" not in receipt
    assert "authorityStatus" not in receipt


def test_strict_v1_duplicate_source_ids_fail_as_ambiguous_candidate_references(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)

    def _mutator(manifest: dict) -> None:
        manifest["sources"].append({**manifest["sources"][0], "repository": "https://github.com/example/other.git"})
        manifest.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [_source_value_candidate()]})

    _rewrite_manifest(root, _mutator)
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("duplicate under strict candidate contract v1" in error for error in receipt["errors"])


@pytest.mark.parametrize("candidate_factory", [_source_value_candidate, _internal_defect_candidate])
def test_strict_v1_source_evidence_must_be_nonblank_free_text(tmp_path: Path, candidate_factory) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = candidate_factory()
    candidate["sourceEvidence"] = {"not": "free text"}
    _rewrite_manifest(root, lambda manifest: manifest.update({
        "candidateContractVersion": 1,
        "suggestedAbsorptionCandidates": [candidate],
    }))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("sourceEvidence must be a non-blank string" in error for error in receipt["errors"])
def test_boolean_discriminator_true_is_rejected_not_treated_as_strict_v1(tmp_path: Path) -> None:
    """Reviewer probe 1: candidateContractVersion: true must not be accepted
    as the integer 1 (bool is a subclass of int in Python)."""
    root = tmp_path / "returned"
    _make_return(root)
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": True, "suggestedAbsorptionCandidates": []}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert receipt["candidateContractStatus"] == "UNSUPPORTED_OR_MALFORMED"
    assert receipt["validatedCandidateContractVersion"] is None


def test_boolean_discriminator_false_is_rejected(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": False, "suggestedAbsorptionCandidates": []}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert receipt["candidateContractStatus"] == "UNSUPPORTED_OR_MALFORMED"


def test_empty_questions_for_local_agent_fails_both_lanes(tmp_path: Path) -> None:
    """Reviewer probe 2: questionsForLocalAgent must be a non-empty list of
    non-blank strings, not merely a list (an empty list previously passed)."""
    root = tmp_path / "returned"
    _make_return(root)
    source_candidate = _source_value_candidate("ESC-001")
    source_candidate["questionsForLocalAgent"] = []
    defect_candidate = _internal_defect_candidate("ESC-002")
    defect_candidate["questionsForLocalAgent"] = []
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [source_candidate, defect_candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert sum("questionsForLocalAgent" in error for error in receipt["errors"]) >= 2


def test_blank_question_string_in_list_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["questionsForLocalAgent"] = ["   "]
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("questionsForLocalAgent" in error for error in receipt["errors"])


def test_per_row_authority_status_fails_both_lanes(tmp_path: Path) -> None:
    """Reviewer probe 3: a candidate row must never carry its own
    authorityStatus; the parent manifest's authorityStatus governs all rows."""
    root = tmp_path / "returned"
    _make_return(root)
    source_candidate = _source_value_candidate("ESC-001")
    source_candidate["authorityStatus"] = "NON_AUTHORITATIVE_UNTIL_REVIEWED"
    defect_candidate = _internal_defect_candidate("ESC-002")
    defect_candidate["authorityStatus"] = "NON_AUTHORITATIVE_UNTIL_REVIEWED"
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [source_candidate, defect_candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert sum("authorityStatus" in error for error in receipt["errors"]) >= 2


def test_reverse_lane_contamination_source_value_with_defect_fields_fails(tmp_path: Path) -> None:
    """Reviewer probe 4: the external-source-value lane must reject
    cvfPublicLocations/triggerContextSourceRefs (the reverse contamination
    direction from the already-tested internal-defect-with-source-fields
    case)."""
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["cvfPublicLocations"] = [{"path": "public/cvf/x.py", "symbols": ["X"]}]
    candidate["triggerContextSourceRefs"] = ["SRC-001"]
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("cvfPublicLocations" in error and "forbidden" in error for error in receipt["errors"])
    assert any("triggerContextSourceRefs" in error and "forbidden" in error for error in receipt["errors"])


def test_invalid_preliminary_value_disposition_fails(tmp_path: Path) -> None:
    """Reviewer probe 5: preliminaryValueDisposition must be exactly one of
    ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE."""
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["preliminaryValueDisposition"] = "MAYBE_LATER"
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("preliminaryValueDisposition" in error for error in receipt["errors"])


@pytest.mark.parametrize("disposition", list(PRELIMINARY_VALUE_DISPOSITIONS))
def test_every_allowed_preliminary_value_disposition_passes(tmp_path: Path, disposition: str) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["preliminaryValueDisposition"] = disposition
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "PASS", receipt["errors"]


def test_fake_missing_owner_candidate_path_fails(tmp_path: Path) -> None:
    """Reviewer probe 6: a publicOwnerSearch status other than
    OWNER_CANDIDATES_FOUND must not carry a fabricated non-empty candidates
    list (a fake missing-owner path)."""
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["publicOwnerSearch"] = {
        "status": "PUBLIC_OWNER_SURFACE_NOT_FOUND",
        "candidates": [{"path": "public/fake/path.py", "symbol": "Fake", "basis": "fabricated"}],
    }
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("publicOwnerSearch.candidates" in error for error in receipt["errors"])


def test_owner_search_candidate_missing_symbol_or_basis_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["publicOwnerSearch"] = {
        "status": "OWNER_CANDIDATES_FOUND",
        "candidates": [{"path": "public/path.py", "symbol": "", "basis": ""}],
    }
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("symbol" in error for error in receipt["errors"])
    assert any("basis" in error for error in receipt["errors"])


def test_owner_search_candidate_unsafe_path_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["publicOwnerSearch"] = {
        "status": "OWNER_CANDIDATES_FOUND",
        "candidates": [{"path": "../../etc/passwd", "symbol": "X", "basis": "evidence"}],
    }
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("publicOwnerSearch.candidates" in error and "path" in error for error in receipt["errors"])


def test_blank_overlap_basis_fails(tmp_path: Path) -> None:
    """Reviewer probe 7: publicOverlap.basis must be a non-blank string, not
    merely a bounded status with an empty/missing basis."""
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["publicOverlap"] = {"status": "PUBLIC_SUGGESTS_ENRICHMENT", "basis": ""}
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("publicOverlap.basis" in error for error in receipt["errors"])


def test_publicoverlap_missing_basis_field_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["publicOverlap"] = {"status": "PUBLIC_SUGGESTS_ENRICHMENT"}
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("publicOverlap.basis" in error for error in receipt["errors"])


def test_undeclared_field_on_source_value_lane_fails(tmp_path: Path) -> None:
    """Exact allowed-field-set enforcement: an undeclared field on the
    external-source-value lane must fail closed under strict v1."""
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _source_value_candidate()
    candidate["notInTheAllowedSet"] = "sneaky"
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("undeclared field" in error for error in receipt["errors"])


def test_undeclared_field_on_internal_defect_lane_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_return(root)
    candidate = _internal_defect_candidate()
    candidate["notInTheAllowedSet"] = "sneaky"
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("undeclared field" in error for error in receipt["errors"])


def test_optional_source_evidence_field_is_allowed_on_both_lanes(tmp_path: Path) -> None:
    """sourceEvidence is an explicitly optional bounded field on both lanes;
    it must not be rejected as undeclared."""
    root = tmp_path / "returned"
    _make_return(root)
    source_candidate = _source_value_candidate("ESC-001")
    source_candidate["sourceEvidence"] = "bounded summary only"
    defect_candidate = _internal_defect_candidate("ESC-002")
    defect_candidate["sourceEvidence"] = "bounded summary only"
    _rewrite_manifest(root, lambda m: m.update({"candidateContractVersion": 1, "suggestedAbsorptionCandidates": [source_candidate, defect_candidate]}))
    receipt = validate_return(root, tmp_path / "receipt.json")
    assert receipt["status"] == "PASS", receipt["errors"]

from __future__ import annotations

import hashlib
import json
import subprocess
from argparse import Namespace
from pathlib import Path

import jsonschema
import pytest

from scripts.external_agent_packet import PacketError, _update_snapshot_text, create_capsule, validate_return


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

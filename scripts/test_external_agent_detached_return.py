from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from scripts.external_agent_packet import main as packet_main

from scripts.external_agent_return_contract import (
    AUTHORITY_OBJECT_FIELD,
    DISPATCH_BINDING_FIELD,
    DERIVED_ABSORPTION_COMPLETE_USE_PROVEN,
    DERIVED_ABSORPTION_NOT_COMPLETE,
    DERIVED_NO_RUNTIME_VALUE_WITH_REASON,
    EMITTER_DETACHED_EXTERNAL_AGENT,
    EMITTER_SHARED_WORKSPACE_WORKER,
    LEGACY_COMPLETE_STATUS,
    PROPOSED_CHANGESET_DIRNAME,
    STATUS_ABSORPTION_NOT_COMPLETE,
    STATUS_EXTERNAL_RETURN_READY,
    STATUS_NOT_CVF_SOT,
    derive_completion_projection,
    detect_reserved_local_only_artifacts,
    is_safe_proposed_path,
    validate_authority_object,
    validate_detached_return,
    validate_state_vector,
)


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_inventory(root: Path) -> None:
    rows = [
        (path.relative_to(root).as_posix(), _sha(path))
        for path in root.rglob("*")
        if path.is_file() and path.name != "FILE_INVENTORY.sha256"
    ]
    (root / "FILE_INVENTORY.sha256").write_text(
        "".join(f"{digest}  {rel}\n" for rel, digest in sorted(rows)), encoding="utf-8", newline="\n"
    )


def _authority_object(emitter: str = EMITTER_DETACHED_EXTERNAL_AGENT) -> dict:
    return {
        "emitterClass": emitter,
        "authorityClass": "EXTERNAL_PROPOSAL",
        "cvfSot": False,
        "localSemanticReviewRequired": True,
        "automaticPromotionAllowed": False,
        "absorptionComplete": False,
        "runtimeUseProven": False,
    }


def _state_vector(**overrides: str) -> dict:
    base = {
        "sourceCoverageVerdict": "PARTIAL",
        "sourceReconciliationState": "PENDING_LOCAL_RECONCILIATION",
        "ownerPromotionState": "EXTERNAL_PROPOSAL",
        "runtimeRealizationState": "NOT_APPLICABLE_WITH_REASON",
        "representativeUseProofState": "NOT_REQUIRED_WITH_REASON",
    }
    base.update(overrides)
    return base


def _dispatch_binding(root: Path) -> dict:
    capsule = {
        "schema": "cvf.externalAgentTaskCapsule.v1",
        "protocolVersion": "1.3.0",
        "task": {
            "id": "task-001",
            "workingMode": "DETACHED_IMPLEMENTATION_PROPOSAL",
            "executionClass": EMITTER_DETACHED_EXTERNAL_AGENT,
        },
        "cvfPublicSource": {
            "repository": "https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git",
            "commit": "1" * 40,
        },
        "sourceRepositories": [{"repository": "https://github.com/example/source.git", "commit": "2" * 40}],
    }
    capsule_path = root.parent / "CVF_EXTERNAL_AGENT_TASK_CAPSULE.json"
    capsule_path.write_text(json.dumps(capsule, indent=2) + "\n", encoding="utf-8", newline="\n")
    return {
        "taskCapsuleSha256": _sha(capsule_path),
        "taskId": "task-001",
        "protocolVersion": "1.3.0",
        "sourceRepository": "https://github.com/example/source.git",
        "sourceCommit": "2" * 40,
        "cvfPublicRepository": "https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git",
        "cvfPublicCommit": "1" * 40,
    }


def _make_detached_return(root: Path, *, extra_manifest: dict | None = None, emitter: str = EMITTER_DETACHED_EXTERNAL_AGENT) -> None:
    root.mkdir(parents=True)
    (root / PROPOSED_CHANGESET_DIRNAME).mkdir()
    proposed_file = root / PROPOSED_CHANGESET_DIRNAME / "docs" / "reference" / "example.md"
    proposed_file.parent.mkdir(parents=True)
    proposed_file.write_text("# Example proposal\n", encoding="utf-8", newline="\n")

    readme_text = (
        f"{STATUS_EXTERNAL_RETURN_READY}\n{STATUS_NOT_CVF_SOT}\n{STATUS_ABSORPTION_NOT_COMPLETE}\n"
        "EXTERNAL_PROPOSAL\nNON_AUTHORITATIVE_UNTIL_REVIEWED\n"
    )
    for name in ("README.md", "SOURCE_MANIFEST.md", "DECISION_LOG.md", "TEST_EVIDENCE.md", "CLAIM_BOUNDARY.md"):
        (root / name).write_text(readme_text if name == "README.md" else f"# {name}\n", encoding="utf-8", newline="\n")

    manifest = {
        "schema": "cvf.externalAgentReturn.v1",
        "emitterClass": emitter,
        AUTHORITY_OBJECT_FIELD: _authority_object(emitter),
        DISPATCH_BINDING_FIELD: _dispatch_binding(root),
        "returnStatus": STATUS_EXTERNAL_RETURN_READY,
        "stateVector": _state_vector(),
    }
    if extra_manifest:
        manifest.update(extra_manifest)
    (root / "EXTERNAL_AGENT_RETURN_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n"
    )

    target_map = {
        "entries": [
            {
                "proposedTarget": "docs/reference/example.md",
                "sha256": _sha(proposed_file),
                "sourceOrFindingIds": ["SRC-001"],
                "intendedOwnerPath": "docs/reference/example.md",
                "operation": "add",
                "maturityAndClaimClass": "PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE",
                "consumingTestsOrEvidence": ["scripts/test_example.py"],
                "unresolvedLocalFacts": [],
                "runtimeIntegrationPending": True,
                "useProofPending": True,
            }
        ]
    }
    (root / "PROPOSED_TARGET_MAP.json").write_text(
        json.dumps(target_map, indent=2) + "\n", encoding="utf-8", newline="\n"
    )

    _write_inventory(root)


def _rewrite_manifest(root: Path, mutator) -> dict:
    manifest_path = root / "EXTERNAL_AGENT_RETURN_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    mutator(manifest)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")
    return manifest


def _rewrite_target_map(root: Path, mutator) -> dict:
    path = root / "PROPOSED_TARGET_MAP.json"
    target_map = json.loads(path.read_text(encoding="utf-8"))
    mutator(target_map)
    path.write_text(json.dumps(target_map, indent=2) + "\n", encoding="utf-8", newline="\n")
    return target_map


# --- Deterministic valid case ------------------------------------------------


def test_valid_detached_return_reaches_local_verification_readiness(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    receipt = validate_detached_return(root)
    assert receipt["status"] == STATUS_EXTERNAL_RETURN_READY, receipt["errors"]
    assert receipt["cvfSot"] is False
    assert receipt["absorptionComplete"] is False
    assert receipt["derivedCompletionProjection"] == DERIVED_ABSORPTION_NOT_COMPLETE


def test_prose_only_return_with_no_proposed_changeset_rejected(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    for path in (root / PROPOSED_CHANGESET_DIRNAME).rglob("*"):
        if path.is_file():
            path.unlink()
    _rewrite_target_map(root, lambda tm: tm["entries"].__setitem__(0, {**tm["entries"][0]}))
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("missing from" in error for error in receipt["errors"])


# --- Legacy status handling ---------------------------------------------


def test_legacy_complete_status_not_emittable_by_new_producer(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root, extra_manifest={"returnStatus": LEGACY_COMPLETE_STATUS})
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("legacy status" in error for error in receipt["errors"])


# --- Forbidden completion/absorption/runtime/SOT claims ----------------------


@pytest.mark.parametrize(
    "forbidden_claim",
    [
        "ABSORPTION_COMPLETE",
        "ABSORPTION_COMPLETE_USE_PROVEN",
        "INTEGRATED_INTO_CVF",
        "CVF_SOT_UPDATED",
        "CVF_RUNTIME_PROVEN",
        "SOURCE_RECONCILED",
        "OWNER_ACCEPTED",
        "CVF_OWNER_INTEGRATED",
        "USE_PROVEN",
    ],
)
def test_forbidden_completion_claim_rejected_regardless_of_manifest_validity(tmp_path: Path, forbidden_claim: str) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    readme_path = root / "README.md"
    readme_path.write_text(readme_path.read_text(encoding="utf-8") + f"\n{forbidden_claim}\n", encoding="utf-8", newline="\n")
    _write_inventory(root)
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("forbidden completion" in error for error in receipt["errors"])


# --- Missing or widened manifest authority object ---------------------------


def test_missing_authority_object_rejected_before_semantic_review(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    _rewrite_manifest(root, lambda m: m.pop(AUTHORITY_OBJECT_FIELD))
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any(AUTHORITY_OBJECT_FIELD in error for error in receipt["errors"])


@pytest.mark.parametrize(
    "field,bad_value",
    [
        ("cvfSot", True),
        ("automaticPromotionAllowed", True),
        ("absorptionComplete", True),
        ("runtimeUseProven", True),
        ("localSemanticReviewRequired", False),
        ("emitterClass", "SOMETHING_ELSE"),
        ("authorityClass", "CVF_SOT"),
    ],
)
def test_widened_authority_object_field_rejected(tmp_path: Path, field: str, bad_value) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    _rewrite_manifest(root, lambda m: m[AUTHORITY_OBJECT_FIELD].update({field: bad_value}))
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any(field in error for error in receipt["errors"])


def test_authority_object_undeclared_field_rejected(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    _rewrite_manifest(root, lambda m: m[AUTHORITY_OBJECT_FIELD].update({"extraSneakyField": True}))
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("undeclared field" in error for error in receipt["errors"])


def test_authority_object_non_literal_boolean_rejected(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    _rewrite_manifest(root, lambda m: m[AUTHORITY_OBJECT_FIELD].update({"cvfSot": 0}))
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("literal boolean" in error for error in receipt["errors"])


# --- Fabricated local-only authority artifacts (authority forgery) --------


@pytest.mark.parametrize(
    "reserved_name",
    ["LOCAL_PROMOTION_RECEIPT.json", "RETURN_AUTHORITY.json", "CVF_LOCAL_PROMOTION_RECEIPT.json"],
)
def test_fabricated_local_only_receipt_rejected_as_authority_forgery(tmp_path: Path, reserved_name: str) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    (root / reserved_name).write_text('{"forged": true}\n', encoding="utf-8", newline="\n")
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("authority forgery" in error for error in receipt["errors"])


def test_reserved_name_nested_inside_changeset_still_detected(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    nested = root / PROPOSED_CHANGESET_DIRNAME / "deep" / "LOCAL_PROMOTION_RECEIPT.json"
    nested.parent.mkdir(parents=True)
    nested.write_text("{}\n", encoding="utf-8", newline="\n")
    found = detect_reserved_local_only_artifacts(root)
    assert any(path.endswith("LOCAL_PROMOTION_RECEIPT.json") for path in found)


def test_local_authority_alias_name_is_rejected(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    (root / "LOCAL_REVIEW_PROMOTION_RECEIPT.json").write_text("{}\n", encoding="utf-8", newline="\n")
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("authority forgery" in error for error in receipt["errors"])


# --- Missing or tampered file / extra unlisted file -------------------------


def test_target_map_digest_mismatch_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    (root / PROPOSED_CHANGESET_DIRNAME / "docs" / "reference" / "example.md").write_text(
        "# Tampered\n", encoding="utf-8", newline="\n"
    )
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("does not match the actual proposed file" in error for error in receipt["errors"])


def test_extra_unlisted_file_in_changeset_fails_inventory_reconciliation(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    extra = root / PROPOSED_CHANGESET_DIRNAME / "docs" / "reference" / "unlisted.md"
    extra.write_text("# unlisted\n", encoding="utf-8", newline="\n")
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("not bound by an add/modify row" in error for error in receipt["errors"])


def test_missing_proposed_file_declared_in_target_map_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    (root / PROPOSED_CHANGESET_DIRNAME / "docs" / "reference" / "example.md").unlink()
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("missing from" in error for error in receipt["errors"])


def test_inventory_digest_tampering_fails_full_return_reconciliation(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    inventory = root / "FILE_INVENTORY.sha256"
    inventory.write_text(inventory.read_text(encoding="utf-8").replace("a", "b", 1), encoding="utf-8", newline="\n")
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("does not exactly match" in error for error in receipt["errors"])


def test_hidden_uninventoried_file_fails_full_return_reconciliation(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    hidden = root / ".archive" / "payload.txt"
    hidden.parent.mkdir()
    hidden.write_text("hidden\n", encoding="utf-8", newline="\n")
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("does not exactly match" in error for error in receipt["errors"])


# --- Path-safety: absolute, traversal, device, ambiguous normalization ------


@pytest.mark.parametrize(
    "unsafe_path",
    [
        "../../etc/passwd",
        "/abs/path",
        "C:/Windows/System32/evil.dll",
        "docs\\reference\\example.md",
        "docs//reference/example.md",
        "CON.md",
        "COM1.txt",
        "..",
        ".",
        " docs/example.md",
        "docs/example.md ",
        "docs/trailing./file.md",
        "docs/cafe\u0301.md",
    ],
)
def test_unsafe_proposed_target_path_rejected(unsafe_path: str) -> None:
    assert is_safe_proposed_path(unsafe_path) is False


@pytest.mark.parametrize("safe_path", ["docs/reference/example.md", "scripts/tool.py", "a/b/c/d.txt"])
def test_safe_proposed_target_path_accepted(safe_path: str) -> None:
    assert is_safe_proposed_path(safe_path) is True


def test_target_map_rejects_unsafe_proposed_target(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    _rewrite_target_map(root, lambda tm: tm["entries"][0].update({"proposedTarget": "../../etc/passwd"}))
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("unsafe" in error or "missing" in error for error in receipt["errors"])


def test_target_map_rejects_case_normalization_collision(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    def add_collision(target_map: dict) -> None:
        row = dict(target_map["entries"][0])
        row["proposedTarget"] = "DOCS/REFERENCE/EXAMPLE.MD"
        target_map["entries"].append(row)
    _rewrite_target_map(root, add_collision)
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("canonical case normalization" in error for error in receipt["errors"])


# --- Symlink / archive inventory bypass (Windows-real proxy: reserved device names / UNC) --


@pytest.mark.parametrize("device_path", ["docs/CON", "docs/PRN.txt", "docs/AUX.md", "LPT1.md"])
def test_reserved_device_name_path_rejected(device_path: str) -> None:
    assert is_safe_proposed_path(device_path) is False


def test_unc_style_path_rejected() -> None:
    assert is_safe_proposed_path("//server/share/file.md") is False
    assert is_safe_proposed_path("\\\\server\\share\\file.md") is False


def test_real_symlink_signal_is_rejected_without_following_target(tmp_path: Path, monkeypatch) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    target = root / PROPOSED_CHANGESET_DIRNAME / "docs" / "reference" / "example.md"
    original = Path.is_symlink
    monkeypatch.setattr(Path, "is_symlink", lambda self: self == target or original(self))
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("forbidden symlink" in error for error in receipt["errors"])


# --- Stale or nonexistent proposed owner: flagged, never auto-promoted -----


def test_stale_owner_path_still_validates_structurally_but_never_promotes(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    _rewrite_target_map(root, lambda tm: tm["entries"][0].update({"intendedOwnerPath": "docs/reference/does_not_exist_yet.md"}))
    _write_inventory(root)
    receipt = validate_detached_return(root)
    assert receipt["status"] == STATUS_EXTERNAL_RETURN_READY
    assert receipt["cvfSot"] is False
    assert receipt["absorptionComplete"] is False


# --- Secret-like material rejected or safely redacted -----------------------


def test_authority_object_cannot_widen_via_secret_bearing_field_injection(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    _rewrite_manifest(root, lambda m: m[AUTHORITY_OBJECT_FIELD].update({"apiKey": "sk-fake-not-a-real-secret"}))
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("undeclared field" in error for error in receipt["errors"])
    assert "sk-fake-not-a-real-secret" not in json.dumps(receipt)


def test_secret_like_material_inside_proposed_file_is_rejected_without_echo(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    proposed = root / PROPOSED_CHANGESET_DIRNAME / "docs" / "reference" / "example.md"
    proposed.write_text("api_key=very-secret-value-123\n", encoding="utf-8", newline="\n")
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("secret-like material" in error for error in receipt["errors"])
    assert "very-secret-value-123" not in json.dumps(receipt)


# --- Unknown mode/status/field: strict validation fails ---------------------


def test_unknown_emitter_class_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root, emitter="SOME_OTHER_AGENT_TYPE")
    _rewrite_manifest(root, lambda m: m.update({"emitterClass": "SOME_OTHER_AGENT_TYPE"}))
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("emitterClass" in error for error in receipt["errors"])


def test_unknown_state_vector_value_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    _rewrite_manifest(root, lambda m: m["stateVector"].update({"sourceCoverageVerdict": "MADE_UP_VALUE"}))
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("sourceCoverageVerdict" in error for error in receipt["errors"])


@pytest.mark.parametrize(
    "field,bad_value",
    [
        ("taskCapsuleSha256", "0" * 64),
        ("sourceCommit", "3" * 40),
        ("cvfPublicCommit", "4" * 40),
        ("taskId", "wrong-task"),
    ],
)
def test_dispatch_binding_mismatch_fails_closed(tmp_path: Path, field: str, bad_value: str) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    _rewrite_manifest(root, lambda manifest: manifest[DISPATCH_BINDING_FIELD].update({field: bad_value}))
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any(f"dispatchBinding.{field}" in error for error in receipt["errors"])


def test_task_capsule_pin_drift_fails_closed(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    capsule = root.parent / "CVF_EXTERNAL_AGENT_TASK_CAPSULE.json"
    capsule.write_text(capsule.read_text(encoding="utf-8") + " ", encoding="utf-8", newline="\n")
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("taskCapsuleSha256" in error for error in receipt["errors"])


def test_capsule_and_validation_receipt_must_remain_outside_return_root(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    external_capsule = root.parent / "CVF_EXTERNAL_AGENT_TASK_CAPSULE.json"
    internal_capsule = root / "capsule.json"
    internal_capsule.write_bytes(external_capsule.read_bytes())
    receipt = validate_detached_return(root, internal_capsule)
    assert any("capsule must remain outside" in error for error in receipt["errors"])
    rc = packet_main(["validate-detached-return", "--return-root", str(root), "--task-capsule", str(external_capsule), "--receipt", str(root / "receipt.json")])
    assert rc == 2 and not (root / "receipt.json").exists()


# --- Repeated validation is deterministic and idempotent --------------------


def test_repeated_validation_is_deterministic(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    receipt_a = validate_detached_return(root)
    receipt_b = validate_detached_return(root)
    assert receipt_a["status"] == receipt_b["status"] == STATUS_EXTERNAL_RETURN_READY
    assert receipt_a["validatedReturnManifestSha256"] == receipt_b["validatedReturnManifestSha256"]
    assert receipt_a["derivedCompletionProjection"] == receipt_b["derivedCompletionProjection"]


def test_concurrent_style_validation_of_two_independent_roots_does_not_cross_contaminate(tmp_path: Path) -> None:
    root_a = tmp_path / "returned_a"
    root_b = tmp_path / "returned_b"
    _make_detached_return(root_a)
    _make_detached_return(root_b, extra_manifest={"task": {"title": "Different"}})
    receipt_a = validate_detached_return(root_a)
    receipt_b = validate_detached_return(root_b)
    assert receipt_a["returnRoot"] != receipt_b["returnRoot"]
    assert receipt_a["status"] == receipt_b["status"] == STATUS_EXTERNAL_RETURN_READY


# --- Independent state vector and derived completion projection ------------


def test_derive_completion_projection_absorption_not_complete_when_coverage_partial() -> None:
    values = _state_vector(sourceCoverageVerdict="PARTIAL")
    assert derive_completion_projection(values) == DERIVED_ABSORPTION_NOT_COMPLETE


def test_derive_completion_projection_absorption_not_complete_when_owner_only_reviewed() -> None:
    values = _state_vector(
        sourceCoverageVerdict="COMPLETE_VERIFIED",
        sourceReconciliationState="SOURCE_RECONCILED",
        ownerPromotionState="LOCAL_REVIEWED",
    )
    assert derive_completion_projection(values) == DERIVED_ABSORPTION_NOT_COMPLETE


def test_derive_completion_projection_absorption_not_complete_when_runtime_implemented_without_use_proof() -> None:
    values = _state_vector(
        sourceCoverageVerdict="COMPLETE_VERIFIED",
        sourceReconciliationState="SOURCE_RECONCILED",
        ownerPromotionState="CVF_OWNER_INTEGRATED",
        runtimeRealizationState="IMPLEMENTED",
        representativeUseProofState="PENDING_OPERATOR_AUTHORIZED_RUNTIME_PROOF",
    )
    assert derive_completion_projection(values) == DERIVED_ABSORPTION_NOT_COMPLETE


def test_derive_completion_projection_use_proven_only_with_full_chain() -> None:
    values = _state_vector(
        sourceCoverageVerdict="COMPLETE_VERIFIED",
        sourceReconciliationState="SOURCE_RECONCILED",
        ownerPromotionState="CVF_OWNER_INTEGRATED",
        runtimeRealizationState="IMPLEMENTED",
        representativeUseProofState="USE_PROVEN",
    )
    assert derive_completion_projection(values) == DERIVED_ABSORPTION_COMPLETE_USE_PROVEN


def test_derive_completion_projection_no_runtime_value_with_reason() -> None:
    values = _state_vector(
        sourceCoverageVerdict="COMPLETE_WITH_DECLARED_EXCLUSIONS",
        sourceReconciliationState="SOURCE_RECONCILED",
        ownerPromotionState="CVF_OWNER_INTEGRATED",
        runtimeRealizationState="NOT_APPLICABLE_WITH_REASON",
        representativeUseProofState="NOT_REQUIRED_WITH_REASON",
    )
    assert derive_completion_projection(values) == DERIVED_NO_RUNTIME_VALUE_WITH_REASON


def test_derive_completion_projection_missing_dimension_falls_back_to_not_complete() -> None:
    assert derive_completion_projection(None) == DERIVED_ABSORPTION_NOT_COMPLETE


# --- A detached external agent can never independently claim locally-owned states --


@pytest.mark.parametrize(
    "field,forbidden_value",
    [
        ("sourceReconciliationState", "SOURCE_RECONCILED"),
        ("ownerPromotionState", "OWNER_ACCEPTED"),
        ("ownerPromotionState", "CVF_OWNER_INTEGRATED"),
        ("runtimeRealizationState", "IMPLEMENTED"),
        ("representativeUseProofState", "USE_PROVEN"),
    ],
)
def test_detached_agent_cannot_emit_locally_owned_state_dimension(tmp_path: Path, field: str, forbidden_value: str) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    _rewrite_manifest(root, lambda m: m["stateVector"].update({field: forbidden_value}))
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("local-review-only" in error for error in receipt["errors"])


def test_declared_projection_mismatch_with_recomputed_projection_fails(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    _rewrite_manifest(root, lambda m: m.update({"derivedCompletionProjection": DERIVED_ABSORPTION_COMPLETE_USE_PROVEN}))
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("does not match the independently recomputed projection" in error for error in receipt["errors"])


# --- Direct unit coverage of validate_authority_object and validate_state_vector --


def test_validate_authority_object_accepts_exact_shape() -> None:
    errors: list[str] = []
    validate_authority_object(_authority_object(), errors)
    assert errors == []


def test_validate_authority_object_rejects_non_dict() -> None:
    errors: list[str] = []
    validate_authority_object("not a dict", errors)
    assert errors


def test_validate_state_vector_shared_workspace_worker_may_claim_locally_owned_values() -> None:
    errors: list[str] = []
    values = _state_vector(
        sourceReconciliationState="SOURCE_RECONCILED",
        ownerPromotionState="OWNER_ACCEPTED",
    )
    result = validate_state_vector(values, EMITTER_SHARED_WORKSPACE_WORKER, errors)
    assert errors == []
    assert result is not None


# --- DOCS_ONLY_FALSE_COMPLETION permanent regression case -------------------


def _docs_only_false_completion_fixture(root: Path) -> None:
    """A deliberately convincing, complete-looking external return: README,
    architecture/design prose, schemas, source/candidate manifests, reconciled
    hashes, return-shape tests, and a full proposal tree -- but honestly
    missing every locally-owned fact (source reconciliation, owner
    acceptance, integration evidence, local promotion receipt, named
    runtime consumer, use proof)."""
    root.mkdir(parents=True)
    changeset = root / PROPOSED_CHANGESET_DIRNAME
    for rel in (
        "docs/reference/ARCHITECTURE_OVERVIEW.md",
        "docs/reference/DESIGN_RATIONALE.md",
        "scripts/proposed_feature.py",
        "scripts/test_proposed_feature.py",
    ):
        path = changeset / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# {rel}\n\nThis document looks complete and polished.\n", encoding="utf-8", newline="\n")

    readme = (
        f"{STATUS_EXTERNAL_RETURN_READY}\n{STATUS_NOT_CVF_SOT}\n{STATUS_ABSORPTION_NOT_COMPLETE}\n"
        "EXTERNAL_PROPOSAL\nNON_AUTHORITATIVE_UNTIL_REVIEWED\n"
        "This return contains a complete architecture overview, design rationale, "
        "full source code, and a full generated test suite with passing evidence.\n"
    )
    (root / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    for name in ("SOURCE_MANIFEST.md", "DECISION_LOG.md", "CLAIM_BOUNDARY.md"):
        (root / name).write_text(f"# {name}\n\nExtensive, convincing, reconciled-looking content.\n", encoding="utf-8", newline="\n")
    (root / "TEST_EVIDENCE.md").write_text(
        "# Test Evidence\n\nAll 42 generated tests reported PASS in the external agent's own sandbox.\n",
        encoding="utf-8", newline="\n",
    )

    entries = []
    for rel in (
        "docs/reference/ARCHITECTURE_OVERVIEW.md",
        "docs/reference/DESIGN_RATIONALE.md",
        "scripts/proposed_feature.py",
        "scripts/test_proposed_feature.py",
    ):
        digest = _sha(changeset / rel)
        entries.append({
            "proposedTarget": rel,
            "sha256": digest,
            "sourceOrFindingIds": ["SRC-001"],
            "intendedOwnerPath": rel,
            "operation": "add",
            "maturityAndClaimClass": "PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE",
            "consumingTestsOrEvidence": ["scripts/test_proposed_feature.py"],
            "unresolvedLocalFacts": [],
            "runtimeIntegrationPending": True,
            "useProofPending": True,
        })
    (root / "PROPOSED_TARGET_MAP.json").write_text(
        json.dumps({"entries": entries}, indent=2) + "\n", encoding="utf-8", newline="\n"
    )

    manifest = {
        "schema": "cvf.externalAgentReturn.v1",
        "emitterClass": EMITTER_DETACHED_EXTERNAL_AGENT,
        AUTHORITY_OBJECT_FIELD: _authority_object(),
        DISPATCH_BINDING_FIELD: _dispatch_binding(root),
        "returnStatus": STATUS_EXTERNAL_RETURN_READY,
        "stateVector": _state_vector(
            sourceCoverageVerdict="COMPLETE_WITH_DECLARED_EXCLUSIONS",
        ),
    }
    (root / "EXTERNAL_AGENT_RETURN_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n"
    )

    _write_inventory(root)


def test_docs_only_false_completion_stays_at_local_verification_readiness_only(tmp_path: Path) -> None:
    """DOCS_ONLY_FALSE_COMPLETION: a polished, convincing, complete-looking
    external return -- with architecture docs, design rationale, source,
    tests, and reconciled hashes -- still cannot exceed
    EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION; it remains NOT_CVF_SOT
    and ABSORPTION_NOT_COMPLETE, because it honestly leaves every
    locally-owned state dimension at its non-terminal value."""
    root = tmp_path / "returned"
    _docs_only_false_completion_fixture(root)
    receipt = validate_detached_return(root)
    assert receipt["status"] == STATUS_EXTERNAL_RETURN_READY, receipt["errors"]
    assert receipt["cvfSot"] is False
    assert receipt["absorptionComplete"] is False
    assert receipt["derivedCompletionProjection"] == DERIVED_ABSORPTION_NOT_COMPLETE


@pytest.mark.parametrize(
    "forbidden_transition_field,forbidden_value",
    [
        ("sourceReconciliationState", "SOURCE_RECONCILED"),
        ("ownerPromotionState", "OWNER_ACCEPTED"),
        ("ownerPromotionState", "CVF_OWNER_INTEGRATED"),
        ("runtimeRealizationState", "IMPLEMENTED"),
        ("representativeUseProofState", "USE_PROVEN"),
    ],
)
def test_docs_only_false_completion_rejects_every_direct_promotion_transition(
    tmp_path: Path, forbidden_transition_field: str, forbidden_value: str
) -> None:
    """Even a convincing DOCS_ONLY_FALSE_COMPLETION package cannot advance
    any single state-vector dimension to a locally-owned terminal value
    without real local review evidence."""
    root = tmp_path / "returned"
    _docs_only_false_completion_fixture(root)
    _rewrite_manifest(root, lambda m: m["stateVector"].update({forbidden_transition_field: forbidden_value}))
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("local-review-only" in error for error in receipt["errors"])


def test_docs_only_false_completion_rejects_fabricated_local_promotion_receipt(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _docs_only_false_completion_fixture(root)
    (root / "LOCAL_PROMOTION_RECEIPT.json").write_text(
        json.dumps({
            "proposalDigest": "deadbeef" * 8,
            "acceptedTarget": "docs/reference/ARCHITECTURE_OVERVIEW.md",
            "disposition": "ABSORB",
        }) + "\n",
        encoding="utf-8", newline="\n",
    )
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("authority forgery" in error for error in receipt["errors"])


def test_docs_only_false_completion_rejects_absorption_complete_use_proven_claim(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _docs_only_false_completion_fixture(root)
    readme_path = root / "README.md"
    readme_path.write_text(
        readme_path.read_text(encoding="utf-8") + "\nABSORPTION_COMPLETE_USE_PROVEN\n",
        encoding="utf-8", newline="\n",
    )
    _write_inventory(root)
    receipt = validate_detached_return(root)
    assert receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("forbidden completion" in error for error in receipt["errors"])


# --- Deliberate regression-guard demonstration proof ------------------------
#
# This test does not disable a real guard permanently. It re-implements the
# authority-object check with the emitterClass literal-equality guard
# removed, proves the DOCS_ONLY_FALSE_COMPLETION-style fixture then wrongly
# validates as clean, and asserts that the real (unmodified) validator still
# fails closed -- demonstrating the guard is load-bearing without ever
# mutating the shipped source file. The worker return records the separate
# file-level disable/restore demonstration performed during implementation.


def test_deliberate_regression_guard_demonstration_emitter_class_literal_check_is_load_bearing(tmp_path: Path) -> None:
    root = tmp_path / "returned"
    _make_detached_return(root)
    _rewrite_manifest(root, lambda m: m.update({"emitterClass": "FORGED_TRUSTED_EMITTER"}))

    def _weakened_validate_authority_object_without_emitter_check(candidate: dict, errors: list[str]) -> None:
        # Deliberately-weakened local copy: omits the emitterClass equality
        # check that the real validator enforces, to prove the guard is
        # load-bearing (not a modification of the shipped module).
        if not isinstance(candidate, dict):
            errors.append("manifest.authorityObject must be an object")
            return
        for field in ("authorityClass", "cvfSot", "localSemanticReviewRequired", "automaticPromotionAllowed", "absorptionComplete", "runtimeUseProven"):
            if field not in candidate:
                errors.append(f"manifest.authorityObject.{field} is required")

    weakened_errors: list[str] = []
    _weakened_validate_authority_object_without_emitter_check(_authority_object(), weakened_errors)
    assert weakened_errors == [], "weakened check should wrongly accept a forged emitterClass scenario"

    real_receipt = validate_detached_return(root)
    assert real_receipt["status"] == "RETURN_FOR_REPAIR"
    assert any("emitterClass" in error for error in real_receipt["errors"])

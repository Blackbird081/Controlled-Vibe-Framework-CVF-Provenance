#!/usr/bin/env python3
"""Prepare CVF external-agent packets and validate returned folders.

The packet refresh path is deliberately fail-closed: the public-sync worktree
must be clean, its HEAD must equal live origin/main, and required public files
must exist before an operator-local snapshot is rewritten.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess  # Retained as the offline-route network/Git test sentinel.
import sys
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any
from zoneinfo import ZoneInfo

try:
    from scripts.external_agent_snapshot_projection import (
        SnapshotProjectionError,
        refresh_public_snapshot,
        update_snapshot_metadata,
    )
    from scripts.external_agent_return_contract import (
        CANDIDATE_LANE_CONTRACT_VERSION,
        CANDIDATE_LANE_CVF_INTERNAL_DEFECT,
        CANDIDATE_LANE_EXTERNAL_SOURCE_VALUE,
        CANDIDATE_LANE_NAMES,
        CANDIDATE_LANE_PRELIMINARY_VALUE_DISPOSITIONS,
        EMITTER_DETACHED_EXTERNAL_AGENT,
        EMITTER_SHARED_WORKSPACE_WORKER,
        LEGACY_COMPLETE_STATUS,
        STATUS_EXTERNAL_RETURN_READY,
        candidate_lane_validate_candidates,
        validate_detached_return,
    )
except ModuleNotFoundError:  # Direct `python scripts/external_agent_packet.py` execution.
    from external_agent_snapshot_projection import (  # type: ignore[no-redef]
        SnapshotProjectionError,
        refresh_public_snapshot,
        update_snapshot_metadata,
    )
    from external_agent_return_contract import (  # type: ignore[no-redef]
        CANDIDATE_LANE_CONTRACT_VERSION,
        CANDIDATE_LANE_CVF_INTERNAL_DEFECT,
        CANDIDATE_LANE_EXTERNAL_SOURCE_VALUE,
        CANDIDATE_LANE_NAMES,
        CANDIDATE_LANE_PRELIMINARY_VALUE_DISPOSITIONS,
        EMITTER_DETACHED_EXTERNAL_AGENT,
        EMITTER_SHARED_WORKSPACE_WORKER,
        LEGACY_COMPLETE_STATUS,
        STATUS_EXTERNAL_RETURN_READY,
        candidate_lane_validate_candidates,
        validate_detached_return,
    )


PROTOCOL_VERSION = "1.3.0"
PROTOCOL_ID = "cvf.external-agent-round-trip"

# Candidate-lane (EARTR-ESC-R1) constants are owned by
# external_agent_return_contract; these names are the public API this module
# has always exposed, kept stable for callers and the legacy test suite.
CANDIDATE_CONTRACT_VERSION = CANDIDATE_LANE_CONTRACT_VERSION
LANE_EXTERNAL_SOURCE_VALUE = CANDIDATE_LANE_EXTERNAL_SOURCE_VALUE
LANE_CVF_INTERNAL_DEFECT = CANDIDATE_LANE_CVF_INTERNAL_DEFECT
CANDIDATE_LANES = CANDIDATE_LANE_NAMES
PRELIMINARY_VALUE_DISPOSITIONS = CANDIDATE_LANE_PRELIMINARY_VALUE_DISPOSITIONS
PUBLIC_REPOSITORY = "https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git"
CAPSULE_SCHEMA_PATH = Path(__file__).resolve().parent.parent / "docs" / "reference" / "external_agent_review" / "CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json"
# Source-posture literals for cvfPublicSource.sourcePosture. These are the
# atomic serialized values every consumer must match exactly; do not assemble
# them from fragments.
SOURCE_POSTURE_LIVE = "VERIFIED_LIVE_PUBLIC_MAIN_AT_CREATION"
SOURCE_POSTURE_OFFLINE = "OPERATOR_PINNED_NOT_LIVE_VERIFIED"
# Working modes that require the four context groups (protectedPaths,
# ownerMap, invariants, verification) because they involve writing code
# against a real repository. REVIEW_ONLY, DESIGN_ONLY, and
# SOURCE_PACK_PREPARATION are proportionally exempt: they do not mutate a
# repository, so an owner map / protected-path / invariant contract has no
# referent yet. This mirrors the schema's own `if/then` requirement.
DETACHED_IMPLEMENTATION_PROPOSAL_MODE = "DETACHED_IMPLEMENTATION_PROPOSAL"
CONTEXT_REQUIRED_MODES = ("BUILD_NEW_REPOSITORY", "EXTEND_SUPPLIED_REPOSITORY", DETACHED_IMPLEMENTATION_PROPOSAL_MODE)
WORKING_MODES = ("REVIEW_ONLY", "DESIGN_ONLY", "BUILD_NEW_REPOSITORY", "EXTEND_SUPPLIED_REPOSITORY", "SOURCE_PACK_PREPARATION", DETACHED_IMPLEMENTATION_PROPOSAL_MODE)

CONTEXT_GROUP_NAMES = ("protectedPaths", "ownerMap", "invariants", "verification")
CONSUMER_ROLES = ("worker", "reviewer", "return validator")
PACKET_FILES = (
    "CVF_EXTERNAL_AGENT_BOOTSTRAP_INSTRUCTIONS.md",
    "CVF_CONTEXT_BRIEF.md",
    "CVF_CURRENT_PUBLIC_SNAPSHOT.md",
    "CVF_EXTERNAL_AGENT_RETURN_CONTRACT.md",
)
REQUIRED_PUBLIC_PATHS = (
    "README.md",
    "ARCHITECTURE.md",
    "AGENTS.md",
    "docs/guides/external-agent-review-guide.md",
    "docs/guides/CVF_EXTERNAL_AGENT_ROUND_TRIP_KIT.md",
    "docs/reference/CVF_EXTERNAL_AGENT_OWNER_SURFACE_INDEX.json",
    "docs/reference/CVF_PUBLIC_EVALUATION_CLAIM_BOUNDARY_2026-06-04.md",
    "docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md",
    "docs/reference/CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md",
)
RETURN_REQUIRED = (
    "README.md",
    "EXTERNAL_AGENT_RETURN_MANIFEST.json",
    "SOURCE_MANIFEST.md",
    "DECISION_LOG.md",
    "TEST_EVIDENCE.md",
    "CLAIM_BOUNDARY.md",
    "FILE_INVENTORY.sha256",
)
INVENTORY_EXCLUDED_DIRS = {".git", "node_modules", ".venv", "venv", "dist", "build", "__pycache__", ".pytest_cache"}
SHA40 = re.compile(r"^[0-9a-f]{40}$")
IMMUTABLE_GITHUB = re.compile(r"^https://github\.com/[^/]+/[^/]+/(?:blob|tree)/[0-9a-f]{40}/")


class PacketError(RuntimeError):
    """A fail-closed packet preparation or validation error."""


def _now() -> datetime:
    return datetime.now(ZoneInfo("Asia/Ho_Chi_Minh"))


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def _update_snapshot_text(text: str, sha: str, commit_date: str, subject: str, tree_count: int, stamp: datetime) -> str:
    try:
        return update_snapshot_metadata(
            text, protocol_version=PROTOCOL_VERSION, sha=sha, commit_date=commit_date,
            subject=subject, tree_count=tree_count, snapshot_date=stamp.date().isoformat(),
        )
    except SnapshotProjectionError as exc:
        raise PacketError(str(exc)) from exc


def refresh_snapshot(public_repo: Path, packet_root: Path, owner_index_source: Path) -> dict[str, Any]:
    try:
        return refresh_public_snapshot(
            public_repo, packet_root, owner_index_source,
            protocol_version=PROTOCOL_VERSION, public_repository=PUBLIC_REPOSITORY,
            packet_files=PACKET_FILES, required_public_paths=REQUIRED_PUBLIC_PATHS,
        )
    except (OSError, SnapshotProjectionError) as exc:
        raise PacketError(f"cannot refresh public snapshot: {exc}") from exc


def _load_capsule_schema() -> dict[str, Any]:
    return json.loads(CAPSULE_SCHEMA_PATH.read_text(encoding="utf-8"))


def _validate_capsule(capsule: dict[str, Any]) -> None:
    """Validate a capsule against the governed strict schema before any write.
    Raises PacketError (not a bare jsonschema exception) so callers can fail
    closed without partially writing an existing capsule file."""
    try:
        import jsonschema
    except ModuleNotFoundError as exc:
        raise PacketError(
            "capsule validation requires the jsonschema package; "
            "refresh-snapshot and validate-return remain standard-library-only"
        ) from exc
    schema = _load_capsule_schema()
    try:
        jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(capsule)
    except jsonschema.ValidationError as exc:
        raise PacketError(f"capsule failed strict schema validation: {exc.message}") from exc


def load_context_groups(context_file: Path) -> dict[str, Any]:
    """Load and structurally validate the four task-proportional context
    groups from an operator-authored local JSON file. Raises PacketError on
    any missing file, invalid JSON, unknown group, or non-object shape;
    per-field strict validation happens later via the full capsule schema so
    there is exactly one source of truth for group shape."""
    if not context_file.is_file():
        raise PacketError(f"context file not found: {context_file}")
    try:
        raw = json.loads(context_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise PacketError(f"context file is invalid JSON: {exc}") from exc
    if not isinstance(raw, dict):
        raise PacketError("context file must contain a JSON object")
    unknown = sorted(set(raw) - set(CONTEXT_GROUP_NAMES))
    if unknown:
        raise PacketError(f"context file has unknown group(s): {', '.join(unknown)}")
    return raw


def create_capsule(
    args: argparse.Namespace,
    public_sha: str,
    *,
    source_posture: str = SOURCE_POSTURE_LIVE,
    context_groups: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if not SHA40.fullmatch(args.source_commit):
        raise PacketError("--source-commit must be a lowercase 40-character Git SHA")
    if source_posture not in (SOURCE_POSTURE_LIVE, SOURCE_POSTURE_OFFLINE):
        raise PacketError(f"unknown source posture: {source_posture}")
    stamp = _now()
    capsule: dict[str, Any] = {
        "schema": "cvf.externalAgentTaskCapsule.v1",
        "protocolVersion": PROTOCOL_VERSION,
        "projectionOf": PROTOCOL_ID,
        "generatedAt": stamp.isoformat(timespec="seconds"),
        "task": {
            "id": args.task_id,
            "title": args.title,
            "objective": args.objective,
            "workingMode": args.working_mode,
            "outputRoot": args.output_root,
            "nonGoals": args.non_goal,
        },
        "cvfPublicSource": {"repository": PUBLIC_REPOSITORY, "commit": public_sha, "sourcePosture": source_posture},
        "sourceRepositories": [{"repository": args.source_repository, "commit": args.source_commit, "usage": "REFERENCE_AND_ANALYSIS"}],
        "gateA": {
            "name": "SOURCE_OWNER_OVERLAP",
            "requiredBefore": "DESIGN_OR_CODE",
            "requiredEvidence": ["immutable source identity", "license expression and source", "CVF owner surface", "overlap/novelty disposition"],
            "terminalStates": ["PASS", "RETURN_FOR_REPAIR", "BLOCKED"],
        },
        "gateB": {
            "name": "DESIGN_CODE_TEST",
            "opensOnlyWhen": "gateA=PASS",
            "requiredEvidence": ["positive tests", "negative semantic tests", "malformed-input tests", "claim boundary", "exact commands and results"],
        },
        "authorityEnvelope": {
            "commit": False,
            "push": False,
            "publication": False,
            "deployment": False,
            "providerCalls": False,
            "credentials": False,
            "destructiveActions": False,
        },
    }
    if args.working_mode == DETACHED_IMPLEMENTATION_PROPOSAL_MODE:
        capsule["task"]["expectedReturnStatus"] = STATUS_EXTERNAL_RETURN_READY
        execution_class = getattr(args, "execution_class", None)
        if execution_class is None:
            raise PacketError("--execution-class is required for DETACHED_IMPLEMENTATION_PROPOSAL")
        if execution_class not in (EMITTER_SHARED_WORKSPACE_WORKER, EMITTER_DETACHED_EXTERNAL_AGENT):
            raise PacketError(f"unknown --execution-class: {execution_class}")
        capsule["task"]["executionClass"] = execution_class
    else:
        capsule["task"]["expectedReturnStatus"] = LEGACY_COMPLETE_STATUS
    if context_groups:
        for group_name in CONTEXT_GROUP_NAMES:
            if group_name in context_groups:
                capsule[group_name] = context_groups[group_name]
    if args.working_mode in CONTEXT_REQUIRED_MODES:
        missing = sorted(set(CONTEXT_GROUP_NAMES) - set(capsule))
        if missing:
            raise PacketError(
                f"working mode {args.working_mode} requires all four context groups; "
                f"missing: {', '.join(missing)}"
            )
    _validate_capsule(capsule)
    _write_json(Path(args.packet_root) / "CVF_EXTERNAL_AGENT_TASK_CAPSULE.json", capsule)
    return capsule


def create_capsule_offline(args: argparse.Namespace) -> dict[str, Any]:
    """Create a task capsule from an operator-pinned public commit and a
    local context-groups JSON file, with zero network or Git-remote access.
    Fails before writing (via create_capsule's pre-write validation) rather
    than overwriting an existing capsule with invalid output."""
    if not SHA40.fullmatch(args.cvf_public_commit):
        raise PacketError("--cvf-public-commit must be a lowercase 40-character Git SHA")
    context_groups = load_context_groups(Path(args.context_file))
    return create_capsule(args, args.cvf_public_commit, source_posture=SOURCE_POSTURE_OFFLINE, context_groups=context_groups)


def _safe_rel_path(value: str) -> bool:
    path = PurePosixPath(value)
    return bool(value) and not path.is_absolute() and ".." not in path.parts and "\\" not in value


def _inventory_entries(root: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    for path in root.rglob("*"):
        if not path.is_file() or any(part in INVENTORY_EXCLUDED_DIRS for part in path.relative_to(root).parts):
            continue
        rel = path.relative_to(root).as_posix()
        if rel in {"FILE_INVENTORY.sha256", "RETURN_VALIDATION_RECEIPT.json"}:
            continue
        entries[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    return dict(sorted(entries.items()))


def _parse_inventory(path: Path, errors: list[str]) -> dict[str, str]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        errors.append("FILE_INVENTORY.sha256 must not contain a UTF-8 BOM")
    if b"\r\n" in raw or (raw and not raw.endswith(b"\n")):
        errors.append("FILE_INVENTORY.sha256 must use LF and one trailing LF")
    result: dict[str, str] = {}
    previous = ""
    for number, line in enumerate(raw.decode("utf-8-sig", errors="replace").splitlines(), 1):
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            errors.append(f"inventory line {number} has invalid format")
            continue
        digest, rel = match.groups()
        if not _safe_rel_path(rel):
            errors.append(f"inventory line {number} has unsafe path: {rel}")
        if previous and rel <= previous:
            errors.append("inventory paths are not unique ordinal-sorted")
        previous = rel
        result[rel] = digest
    return result


def _validate_source_rows(manifest: dict[str, Any], errors: list[str]) -> None:
    sources = manifest.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("manifest.sources must be a non-empty list")
        return
    for index, source in enumerate(sources):
        prefix = f"sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{prefix} must be an object")
            continue
        commit = source.get("commit")
        if not isinstance(commit, str) or not SHA40.fullmatch(commit):
            errors.append(f"{prefix}.commit must be a lowercase 40-character Git SHA")
        immutable = source.get("immutableReference")
        if not isinstance(immutable, str) or not IMMUTABLE_GITHUB.match(immutable):
            errors.append(f"{prefix}.immutableReference must be a GitHub blob/tree URL pinned to a 40-character SHA")
        elif isinstance(commit, str) and f"/{commit}/" not in immutable:
            errors.append(f"{prefix}.immutableReference SHA must equal {prefix}.commit")
        license_source = source.get("licenseSource")
        if not isinstance(license_source, str) or not IMMUTABLE_GITHUB.match(license_source):
            errors.append(f"{prefix}.licenseSource must be a GitHub blob/tree URL pinned to a 40-character SHA")
        elif isinstance(commit, str) and f"/{commit}/" not in license_source:
            errors.append(f"{prefix}.licenseSource SHA must equal {prefix}.commit")
        for field in ("licenseExpression", "usageType", "ownerSurface", "overlapDisposition"):
            if not isinstance(source.get(field), str) or not source[field].strip():
                errors.append(f"{prefix}.{field} must be non-empty")


_validate_candidates = candidate_lane_validate_candidates


def validate_return(root: Path, receipt_path: Path) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    for name in RETURN_REQUIRED:
        if not (root / name).is_file():
            errors.append(f"missing required root artifact: {name}")
    manifest: dict[str, Any] = {}
    manifest_path = root / "EXTERNAL_AGENT_RETURN_MANIFEST.json"
    if manifest_path.is_file():
        try:
            loaded = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest = loaded if isinstance(loaded, dict) else {}
            if not isinstance(loaded, dict):
                errors.append("return manifest must be a JSON object")
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"return manifest is invalid JSON: {exc}")

    expected = {
        "schema": "cvf.externalAgentReturn.v1",
        "artifactClass": "PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE",
        "authorityStatus": "NON_AUTHORITATIVE_UNTIL_REVIEWED",
        "secretsReturned": False,
    }
    for field, value in expected.items():
        if manifest.get(field) != value:
            errors.append(f"manifest.{field} must equal {value!r}")
    cvf_source = manifest.get("cvfPublicSource")
    if not isinstance(cvf_source, dict) or not SHA40.fullmatch(str(cvf_source.get("commit", ""))):
        errors.append("manifest.cvfPublicSource.commit must be a lowercase 40-character Git SHA")
    elif cvf_source.get("repository") != PUBLIC_REPOSITORY:
        errors.append("manifest.cvfPublicSource.repository is not the canonical public repository")
    _validate_source_rows(manifest, errors)
    candidate_contract_status = _validate_candidates(manifest, errors)

    files = manifest.get("files")
    manifest_files: dict[str, str] = {}
    if not isinstance(files, list) or not files:
        errors.append("manifest.files must be a non-empty list")
    else:
        for index, item in enumerate(files):
            if not isinstance(item, dict) or not _safe_rel_path(str(item.get("path", ""))):
                errors.append(f"manifest.files[{index}].path is invalid")
                continue
            rel = item["path"]
            digest = item.get("sha256")
            if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                errors.append(f"manifest.files[{index}].sha256 is invalid")
            elif rel in manifest_files:
                errors.append(f"manifest.files contains duplicate path: {rel}")
            else:
                manifest_files[rel] = digest

    actual = _inventory_entries(root) if root.is_dir() else {}
    inventory = _parse_inventory(root / "FILE_INVENTORY.sha256", errors) if (root / "FILE_INVENTORY.sha256").is_file() else {}
    if inventory != actual:
        errors.append("FILE_INVENTORY.sha256 does not exactly match returned files and hashes")
    manifest_expected = {path: digest for path, digest in actual.items() if path != "EXTERNAL_AGENT_RETURN_MANIFEST.json"}
    if manifest_files != manifest_expected:
        errors.append("manifest.files does not exactly match returned files and hashes, excluding the self-referential manifest")

    verification = manifest.get("verification")
    if not isinstance(verification, dict) or not isinstance(verification.get("commands"), list):
        errors.append("manifest.verification.commands must be a list")
    else:
        executed = [row for row in verification["commands"] if isinstance(row, dict) and row.get("executed") is True]
        negative = [row for row in executed if row.get("testClass") in {"negative", "malformed", "authority-widening", "replay-expiry", "secret-redaction", "dependency-failure"}]
        if not executed:
            errors.append("verification must contain at least one executed command record")
        if not negative:
            errors.append("verification must contain executed negative semantic evidence")
    effects = manifest.get("externalEffects")
    if not isinstance(effects, list):
        errors.append("manifest.externalEffects must be a list")
    else:
        for index, effect in enumerate(effects):
            if not isinstance(effect, dict) or not all(effect.get(field) for field in ("type", "target", "authorizedBy", "evidence", "rollback")):
                errors.append(f"externalEffects[{index}] lacks authorization/evidence/rollback fields")

    readme = (root / "README.md").read_text(encoding="utf-8", errors="replace") if (root / "README.md").is_file() else ""
    for marker in (expected["artifactClass"], expected["authorityStatus"]):
        if marker not in readme:
            errors.append(f"README.md lacks authority marker: {marker}")

    status = "PASS" if not errors else "RETURN_FOR_REPAIR"
    manifest_sha256 = hashlib.sha256(manifest_path.read_bytes()).hexdigest() if manifest_path.is_file() else None
    receipt = {
        "schema": "cvf.externalAgentReturnValidationReceipt.v1",
        "protocolVersion": PROTOCOL_VERSION,
        "validatedAt": _now().isoformat(timespec="seconds"),
        "returnRoot": str(root.resolve()),
        "status": status,
        "gateA": "PASS" if not any("source" in error.lower() or "license" in error.lower() or "owner" in error.lower() or "overlap" in error.lower() for error in errors) else "RETURN_FOR_REPAIR",
        "gateB": "PASS" if not any("verification" in error.lower() or "inventory" in error.lower() or "hash" in error.lower() for error in errors) else "RETURN_FOR_REPAIR",
        "filesObserved": len(actual),
        "errors": errors,
        "warnings": warnings,
        "validatedReturnManifestSha256": manifest_sha256,
        "validatedProtocolVersion": PROTOCOL_VERSION,
        "candidateContractStatus": candidate_contract_status,
        "validatedCandidateContractVersion": CANDIDATE_CONTRACT_VERSION if candidate_contract_status == "STRICT_V1" else None,
        "claimBoundary": "Structural, integrity, and bounded semantic intake validation only; not CVF acceptance or absorption approval.",
    }
    _write_json(receipt_path, receipt)
    return receipt


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    refresh = sub.add_parser("refresh-snapshot", help="bind an operator packet to verified live public main")
    refresh.add_argument("--public-repo", required=True)
    refresh.add_argument("--packet-root", required=True)
    refresh.add_argument("--owner-index-source", required=True)

    prepare = sub.add_parser("prepare-task", help="refresh the packet and generate a per-task capsule")
    prepare.add_argument("--public-repo", required=True)
    prepare.add_argument("--packet-root", required=True)
    prepare.add_argument("--owner-index-source", required=True)
    prepare.add_argument("--task-id", required=True)
    prepare.add_argument("--title", required=True)
    prepare.add_argument("--objective", required=True)
    prepare.add_argument("--working-mode", required=True, choices=WORKING_MODES)
    prepare.add_argument("--source-repository", required=True)
    prepare.add_argument("--source-commit", required=True)
    prepare.add_argument("--output-root", required=True)
    prepare.add_argument("--non-goal", action="append", default=[])
    prepare.add_argument(
        "--context-file",
        help="local JSON file with protectedPaths/ownerMap/invariants/verification groups; "
        "required for BUILD_NEW_REPOSITORY and EXTEND_SUPPLIED_REPOSITORY working modes",
    )
    prepare.add_argument(
        "--execution-class",
        choices=(EMITTER_SHARED_WORKSPACE_WORKER, EMITTER_DETACHED_EXTERNAL_AGENT),
        help=f"required for --working-mode {DETACHED_IMPLEMENTATION_PROPOSAL_MODE}",
    )

    offline = sub.add_parser(
        "create-capsule-offline",
        help="create a task capsule from an operator-pinned public commit with zero network/Git-remote access",
    )
    offline.add_argument("--packet-root", required=True)
    offline.add_argument("--cvf-public-commit", required=True, help="operator-pinned 40-char public CVF commit SHA; not live-verified")
    offline.add_argument("--context-file", required=True, help="local JSON file with the four context groups")
    offline.add_argument("--task-id", required=True)
    offline.add_argument("--title", required=True)
    offline.add_argument("--objective", required=True)
    offline.add_argument("--working-mode", required=True, choices=WORKING_MODES)
    offline.add_argument("--source-repository", required=True)
    offline.add_argument("--source-commit", required=True)
    offline.add_argument("--output-root", required=True)
    offline.add_argument("--non-goal", action="append", default=[])
    offline.add_argument(
        "--execution-class",
        choices=(EMITTER_SHARED_WORKSPACE_WORKER, EMITTER_DETACHED_EXTERNAL_AGENT),
        help=f"required for --working-mode {DETACHED_IMPLEMENTATION_PROPOSAL_MODE}",
    )

    validate = sub.add_parser("validate-return", help="validate a returned external-agent folder")
    validate.add_argument("--return-root", required=True)
    validate.add_argument("--receipt")

    validate_detached = sub.add_parser(
        "validate-detached-return",
        help="validate a DETACHED_EXTERNAL_AGENT implementation-proposal return root; "
        "see scripts/external_agent_return_contract.py for the owned contract",
    )
    validate_detached.add_argument("--return-root", required=True)
    validate_detached.add_argument("--task-capsule", required=True)
    validate_detached.add_argument("--receipt")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        if args.command in {"refresh-snapshot", "prepare-task"}:
            receipt = refresh_snapshot(Path(args.public_repo), Path(args.packet_root), Path(args.owner_index_source))
            if args.command == "prepare-task":
                context_groups = load_context_groups(Path(args.context_file)) if args.context_file else None
                create_capsule(args, receipt["publicCommit"], source_posture=SOURCE_POSTURE_LIVE, context_groups=context_groups)
                capsule_path = Path(args.packet_root) / "CVF_EXTERNAL_AGENT_TASK_CAPSULE.json"
                receipt["taskCapsuleSha256"] = hashlib.sha256(capsule_path.read_bytes()).hexdigest()
                receipt["taskId"] = args.task_id
                _write_json(Path(args.packet_root) / "CVF_EXTERNAL_AGENT_PACKET_REFRESH_RECEIPT.json", receipt)
            print(json.dumps(receipt, indent=2, sort_keys=True))
            return 0
        if args.command == "create-capsule-offline":
            capsule = create_capsule_offline(args)
            capsule_path = Path(args.packet_root) / "CVF_EXTERNAL_AGENT_TASK_CAPSULE.json"
            result = {
                "schema": "cvf.externalAgentCapsuleOfflineCreationReceipt.v1",
                "status": "CREATED_OFFLINE_PINNED_NOT_LIVE_VERIFIED",
                "taskCapsuleSha256": hashlib.sha256(capsule_path.read_bytes()).hexdigest(),
                "taskId": args.task_id,
                "sourcePosture": capsule["cvfPublicSource"]["sourcePosture"],
                "claimBoundary": "Proves offline capsule creation from an operator-pinned commit only; no live public-main verification, network, provider, or Git-remote call.",
            }
            print(json.dumps(result, indent=2, sort_keys=True))
            return 0
        root = Path(args.return_root)
        if args.command == "validate-detached-return":
            receipt_path = Path(args.receipt) if args.receipt else root.parent / f"{root.name}.DETACHED_RETURN_VALIDATION_RECEIPT.json"
            if root.resolve() == receipt_path.resolve() or root.resolve() in receipt_path.resolve().parents:
                raise PacketError("detached validation receipt must be written outside the detached return root")
            receipt = validate_detached_return(root, Path(args.task_capsule))
            _write_json(receipt_path, receipt)
            print(json.dumps(receipt, indent=2, sort_keys=True))
            return 0 if receipt["status"] == "EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION" else 1
        receipt_path = Path(args.receipt) if args.receipt else root.parent / f"{root.name}.RETURN_VALIDATION_RECEIPT.json"
        receipt = validate_return(root, receipt_path)
        print(json.dumps(receipt, indent=2, sort_keys=True))
        return 0 if receipt["status"] == "PASS" else 1
    except (OSError, PacketError, ValueError) as exc:
        print(json.dumps({"status": "BLOCKED", "error": str(exc)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

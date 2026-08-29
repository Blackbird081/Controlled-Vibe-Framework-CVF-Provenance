#!/usr/bin/env python3
"""Generate provenance-bound SOURCE_PACK_PREPARATION task capsules.

This is a bounded companion to external_agent_packet.py. It exists because the
general packet orchestrator is at its governed size ceiling; it does not define
a second protocol, schema, validator, receipt owner, or authority model.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path, PurePosixPath
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.external_agent_packet import (
    PROTOCOL_ID,
    PROTOCOL_VERSION,
    PUBLIC_REPOSITORY,
    SOURCE_POSTURE_LIVE,
    SOURCE_POSTURE_OFFLINE,
    PacketError,
    _now,
    _validate_capsule,
    _write_json,
    refresh_snapshot,
)


EXPECTED_RETURN_STATUS = "COMPLETE_PENDING_LOCAL_RECONCILIATION"


def resolve_output_root(requested: str, candidate: str, authorized_root: str, requested_usable: bool) -> dict[str, str]:
    """Return evidence for a safe output-root choice without touching disk."""
    if requested_usable:
        return {"requestedOutputRoot": requested, "actualOutputRoot": requested,
                "outputRootDisposition": "REQUESTED_OUTPUT_ROOT_USED", "reason": "requested root is usable"}
    candidate_path = PurePosixPath(candidate.replace("\\", "/"))
    authorized_path = PurePosixPath(authorized_root.replace("\\", "/"))
    try:
        candidate_path.relative_to(authorized_path)
    except ValueError as exc:
        raise PacketError("fallback output root is outside the authorized task/artifact root") from exc
    if ".." in candidate_path.parts:
        raise PacketError("fallback output root is outside the authorized task/artifact root")
    return {"requestedOutputRoot": requested, "actualOutputRoot": candidate,
            "outputRootDisposition": "OUTPUT_ROOT_REBOUND", "reason": "requested root is unavailable on this host"}


def resolve_public_cvf_pin(capsule_pin: str, live_head: str) -> dict[str, str]:
    status = "PASS" if capsule_pin == live_head else "PUBLIC_CVF_PIN_DRIFT_RECORDED"
    return {"comparisonCommit": capsule_pin, "observedLiveHead": live_head, "status": status}


def validate_return_cvf_pin(capsule_pin: str, return_mapping_commit: str) -> None:
    if capsule_pin != return_mapping_commit:
        raise PacketError("return public-CVF mapping commit does not match the normative task-capsule pin")


def classify_task_capsule_drift(
    capsule: dict[str, Any], *, requested_repository: str | None = None,
    requested_commit: str | None = None, requested_mode: str | None = None,
    forbidden_effect_requested: bool = False, short_objective: str = "",
) -> str:
    """Classify material conflicts; short-objective wording is intentionally non-authoritative."""
    del short_objective
    source = capsule["sourceRepositories"][0]
    normalized = lambda value: value.removesuffix(".git").rstrip("/")
    conflicts = [
        requested_repository is not None and normalized(requested_repository) != normalized(source["repository"]),
        requested_commit is not None and requested_commit != source["commit"],
        requested_mode is not None and requested_mode != capsule["task"]["workingMode"],
        forbidden_effect_requested,
    ]
    return "TASK_CAPSULE_DRIFT" if any(conflicts) else "NO_TASK_CAPSULE_DRIFT"


def create_source_capsule(args: argparse.Namespace, public_sha: str, source_posture: str) -> dict[str, Any]:
    if len(args.source_commit) != 40 or any(char not in "0123456789abcdef" for char in args.source_commit):
        raise PacketError("--source-commit must be a lowercase 40-character Git SHA")
    if len(public_sha) != 40 or any(char not in "0123456789abcdef" for char in public_sha):
        raise PacketError("public CVF commit must be a lowercase 40-character Git SHA")
    if source_posture not in (SOURCE_POSTURE_LIVE, SOURCE_POSTURE_OFFLINE):
        raise PacketError(f"unknown source posture: {source_posture}")
    if not args.source_license_expression.strip():
        raise PacketError("--source-license-expression must be non-blank")
    if args.source_commit not in args.source_license_source:
        raise PacketError("--source-license-source must bind the exact source commit")
    if not args.source_immutable_reference:
        raise PacketError("at least one --source-immutable-reference is required")
    if any(args.source_commit not in reference for reference in args.source_immutable_reference):
        raise PacketError("every --source-immutable-reference must bind the exact source commit")

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
            "workingMode": "SOURCE_PACK_PREPARATION",
            "expectedReturnStatus": EXPECTED_RETURN_STATUS,
            "outputRoot": args.output_root,
            "outputRootPolicy": {
                "requestedRootSemantics": "OPERATOR_PREFERRED_DESTINATION",
                "whenAvailable": "USE_REQUESTED_OUTPUT_ROOT",
                "whenUnavailable": "OUTPUT_ROOT_REBOUND",
                "allowedFallback": "AUTHORIZED_WRITABLE_TASK_OR_ARTIFACT_ROOT_ONLY",
                "evidenceFields": ["requestedOutputRoot", "actualOutputRoot", "outputRootDisposition", "reason"],
            },
            "shortObjectivePolicy": "FOCUS_WITHIN_CAPSULE_ENVELOPE_NO_STRING_EQUALITY",
            "nonGoals": args.non_goal,
        },
        "cvfPublicSource": {
            "repository": PUBLIC_REPOSITORY,
            "commit": public_sha,
            "sourcePosture": source_posture,
            "comparisonBaseline": "TASK_CAPSULE_PIN_NORMATIVE",
            "liveHeadDisposition": "RECORD_DRIFT_DO_NOT_SILENTLY_REPIN",
        },
        "sourceRepositories": [{
            "repository": args.source_repository,
            "commit": args.source_commit,
            "usage": "REFERENCE_AND_ANALYSIS",
            "licenseExpression": args.source_license_expression,
            "licenseSource": args.source_license_source,
            "immutableReferences": args.source_immutable_reference,
        }],
        "gateA": {
            "name": "SOURCE_OWNER_OVERLAP",
            "requiredBefore": "DESIGN_OR_CODE",
            "requiredEvidence": [
                "immutable source identity", "license expression and source",
                "CVF owner surface", "overlap/novelty disposition",
            ],
            "terminalStates": ["PASS", "RETURN_FOR_REPAIR", "BLOCKED"],
        },
        "gateB": {
            "name": "DESIGN_CODE_TEST",
            "opensOnlyWhen": "gateA=PASS",
            "requiredEvidence": [
                "positive tests", "negative semantic tests", "malformed-input tests",
                "claim boundary", "exact commands and results",
            ],
        },
        "authorityEnvelope": {
            "commit": False, "push": False, "publication": False,
            "deployment": False, "providerCalls": False, "credentials": False,
            "destructiveActions": False,
        },
    }
    _validate_capsule(capsule)
    _write_json(Path(args.packet_root) / "CVF_EXTERNAL_AGENT_TASK_CAPSULE.json", capsule)
    return capsule


def _add_task_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--packet-root", required=True)
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--objective", required=True)
    parser.add_argument("--working-mode", choices=("SOURCE_PACK_PREPARATION",), required=True)
    parser.add_argument("--source-repository", required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--source-license-expression", required=True)
    parser.add_argument("--source-license-source", required=True)
    parser.add_argument("--source-immutable-reference", action="append", required=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--non-goal", action="append", default=[])
    parser.add_argument("--context-file")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    live = commands.add_parser("prepare-task")
    _add_task_arguments(live)
    live.add_argument("--public-repo", required=True)
    live.add_argument("--owner-index-source", required=True)
    offline = commands.add_parser("create-capsule-offline")
    _add_task_arguments(offline)
    offline.add_argument("--cvf-public-commit", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "prepare-task":
            receipt = refresh_snapshot(Path(args.public_repo), Path(args.packet_root), Path(args.owner_index_source))
            capsule = create_source_capsule(args, receipt["publicCommit"], SOURCE_POSTURE_LIVE)
            receipt["taskCapsuleSha256"] = hashlib.sha256(
                (Path(args.packet_root) / "CVF_EXTERNAL_AGENT_TASK_CAPSULE.json").read_bytes()
            ).hexdigest()
            receipt["taskId"] = capsule["task"]["id"]
            _write_json(Path(args.packet_root) / "CVF_EXTERNAL_AGENT_PACKET_REFRESH_RECEIPT.json", receipt)
            print(json.dumps(receipt, indent=2, sort_keys=True))
        else:
            capsule = create_source_capsule(args, args.cvf_public_commit, SOURCE_POSTURE_OFFLINE)
            print(json.dumps({
                "schema": "cvf.externalAgentCapsuleOfflineCreationReceipt.v1",
                "status": "CREATED_OFFLINE_PINNED_NOT_LIVE_VERIFIED",
                "taskCapsuleSha256": hashlib.sha256(
                    (Path(args.packet_root) / "CVF_EXTERNAL_AGENT_TASK_CAPSULE.json").read_bytes()
                ).hexdigest(),
                "taskId": capsule["task"]["id"],
                "sourcePosture": SOURCE_POSTURE_OFFLINE,
            }, indent=2, sort_keys=True))
        return 0
    except (OSError, PacketError, ValueError) as exc:
        print(json.dumps({"status": "BLOCKED", "error": str(exc)}, indent=2))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

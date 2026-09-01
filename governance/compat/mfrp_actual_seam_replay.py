#!/usr/bin/env python3
"""Deterministic MFRP P3-R1B replay through the actual P2 seams."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

try:
    from agent_autorun_machine_verification import (
        RECEIPT_SCHEMA,
        VERIFIER_IDENTITY_PROFILE,
        _machine_verification_digest,
        _machine_verification_object,
        _validate_receipt_integrity,
    )
    from agent_automation_machine_verification_readout import (
        DETERMINISTIC_PREFLIGHT_COMPLETE,
        build_machine_verification_readout,
        machine_readout_to_dict,
    )
except ModuleNotFoundError:
    from governance.compat.agent_autorun_machine_verification import (
        RECEIPT_SCHEMA,
        VERIFIER_IDENTITY_PROFILE,
        _machine_verification_digest,
        _machine_verification_object,
        _validate_receipt_integrity,
    )
    from governance.compat.agent_automation_machine_verification_readout import (
        DETERMINISTIC_PREFLIGHT_COMPLETE,
        build_machine_verification_readout,
        machine_readout_to_dict,
    )


REPO_ROOT = Path(__file__).resolve().parents[2]
ORACLE_SCHEMA = "cvf.mfrp.actualSeamReplayOracle.v1"
RESULT_SCHEMA = "cvf.mfrp.actualSeamReplayResult.v1"
ORACLE_PATH = Path("governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json")
ORACLE_SHA256 = "6aa32c3157092c974441c269d17e85aed20d5ba535479523eda5b64d23b3fbf2"
ORACLE_JCS_SHA256 = "8d64ed3414959ca281cc47daf7067047d79776819b44df16c81dff7a6cbfa80c"
REQUIRED_SET_SHA256 = "04be6dc1fa061e13af195c5490769bf88fba3309e2ddb4aa0ed24a8fd6440fca"
ORACLE_COMMIT = "7f607d353bdec11e456731793f181e72abddc297"
RECEIPT_OWNER = Path("governance/compat/agent_autorun_machine_verification.py")
READOUT_OWNER = Path("governance/compat/agent_automation_machine_verification_readout.py")
OWNER_HASHES = {
    str(RECEIPT_OWNER): "8280a95e0985bd1273aa359afff455be1d18346e8b49cb92e9746922d835d022",
    str(READOUT_OWNER): "ff6088bf8144deec4582ce9faf62384b314346c9cbbb87f6b3349a2d23f7e7c3",
}
DESIGN_HASHES = {
    "docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md": "22a086d7742dbdaec5b887fd377890962ad34396953f48287ce865f743766011",
    "docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md": "65698a95dc7bb7f437fe061a81559701b91a3e611c445f5122ad8145c5f13df5",
}
NON_REPRESENTABLE = {"C07", "C08", "C18"}
ALLOWED_MUTATIONS = {
    "NO_MUTATION", "REPLACE_JSON_POINTER", "ALTER_SOURCE_IDENTITY",
    "DELETE_JSON_POINTER", "ALTER_CHECK_SET", "INJECT_SECRET_SENTINEL",
    "ADD_JSON_POINTER",
}
SECRET_SENTINEL = "MFRP_FIXED_NON_SECRET_SENTINEL_C15"
FORBIDDEN_REVIEWER_OUTCOMES = {"REPLAY_PASS", "RETURN_TO_DESIGN"}


@dataclass(frozen=True)
class _Result:
    name: str


def _jcs_bytes(value: object) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def _sha_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha_file(path: Path) -> str:
    return _sha_bytes(path.read_bytes())


def _git_head() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True,
        capture_output=True, check=True,
    ).stdout.strip()


def _git_blob(commit: str, path: Path) -> bytes:
    return subprocess.run(
        ["git", "show", f"{commit}:{path.as_posix()}"], cwd=REPO_ROOT,
        capture_output=True, check=True,
    ).stdout


def _required_set(oracle: dict) -> dict:
    return {
        "requiredCaseIds": oracle["requiredCaseIds"],
        "requiredFamilies": oracle["requiredFamilies"],
        "requiredZeroToleranceClasses": oracle["requiredZeroToleranceClasses"],
    }


def validate_oracle(oracle: object, raw_bytes: bytes) -> dict:
    if not isinstance(oracle, dict) or oracle.get("schema") != ORACLE_SCHEMA:
        raise ValueError("oracle schema mismatch")
    if _sha_bytes(raw_bytes) != ORACLE_SHA256:
        raise ValueError("oracle identity drift")
    if _sha_bytes(_jcs_bytes(oracle)) != ORACLE_JCS_SHA256:
        raise ValueError("oracle all-field JCS identity drift")
    required = _required_set(oracle)
    if _sha_bytes(_jcs_bytes(required)) != REQUIRED_SET_SHA256:
        raise ValueError("oracle required-set identity drift")
    cases = oracle.get("cases")
    if not isinstance(cases, list) or len(cases) != 19:
        raise ValueError("oracle must contain exactly 19 cases")
    case_ids = [case.get("caseId") for case in cases if isinstance(case, dict)]
    families = [case.get("family") for case in cases if isinstance(case, dict)]
    if case_ids != oracle["requiredCaseIds"] or len(set(case_ids)) != 19:
        raise ValueError("case coverage mismatch")
    if set(families) != set(oracle["requiredFamilies"]) or len(set(families)) != 18:
        raise ValueError("family coverage mismatch")
    zero_classes = {
        case.get("zeroToleranceClass") for case in cases
        if case.get("zeroToleranceClass") != "NONE"
    }
    if zero_classes != set(oracle["requiredZeroToleranceClasses"]) or len(zero_classes) != 7:
        raise ValueError("zero-tolerance coverage mismatch")
    for case in cases:
        source = case.get("sourceRef", {})
        mutation = case.get("mutation", {})
        if not source.get("locator") or len(source.get("sourceExcerptSha256", "")) != 64:
            raise ValueError(f"{case.get('caseId')}: source locator/excerpt drift")
        if mutation.get("operator") not in ALLOWED_MUTATIONS:
            raise ValueError(f"{case.get('caseId')}: unknown mutation")
        expected = (
            "NOT_REPRESENTABLE_BY_CURRENT_P2"
            if case.get("caseId") in NON_REPRESENTABLE else "STATICALLY_REACHABLE"
        )
        if case.get("feasibilityDisposition") != expected:
            raise ValueError(f"{case.get('caseId')}: feasibility mismatch")
    return required


def _canonical_receipt() -> dict:
    context = {
        "phase": "pre-implementation",
        "base": "mfrp-r1b-base",
        "head": "mfrp-r1b-head",
        "baseSha": "1" * 40,
        "headSha": "2" * 40,
        "commandManifestHash": "3" * 64,
        "worktreeFingerprint": "4" * 64,
        "verifierIdentityProfile": VERIFIER_IDENTITY_PROFILE,
    }
    verifier_digest = "5" * 64
    results = (_Result("mfrp-r1b-control"),)
    machine = _machine_verification_object(context, verifier_digest, results)
    return {
        "schema": RECEIPT_SCHEMA,
        "status": "PASS",
        **context,
        "verifierIdentityDigest": verifier_digest,
        "machineVerification": machine,
        "receiptDigest": _machine_verification_digest(machine),
        "totalDurationSeconds": 0.0,
        "checks": [{
            "name": results[0].name,
            "command": ["python", "-B", "mfrp-r1b-control"],
            "durationSeconds": 0.0,
            "status": "PASS",
        }],
    }


def _set_pointer(document: dict, pointer: str, value: object, *, append: bool = False) -> None:
    parts = pointer.lstrip("/").split("/")
    target: object = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    leaf = parts[-1]
    if isinstance(target, list):
        if append or leaf == "-" or int(leaf) == len(target):
            target.append(value)
        else:
            target[int(leaf)] = value
    else:
        target[leaf] = value


def _delete_pointer(document: dict, pointer: str) -> None:
    parts = pointer.lstrip("/").split("/")
    target: object = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    if isinstance(target, list):
        del target[int(parts[-1])]
    else:
        del target[parts[-1]]


def apply_mutation(receipt: dict, case: dict) -> bool:
    """Consume a committed typed mutation and report serialized-byte change."""
    before = _jcs_bytes(receipt)
    case_id = case["caseId"]
    operator = case["mutation"]["operator"]
    pointer = case["mutation"]["jsonPointer"]
    if operator == "NO_MUTATION":
        pass
    elif operator == "DELETE_JSON_POINTER":
        _delete_pointer(receipt, pointer)
    elif operator == "ADD_JSON_POINTER":
        _set_pointer(receipt, pointer, "MFRP_FOCUSED_PROBE_CONTRADICTION", append=True)
    elif operator == "INJECT_SECRET_SENTINEL":
        _set_pointer(receipt, pointer, SECRET_SENTINEL)
    elif operator == "ALTER_CHECK_SET":
        if pointer == "/checks":
            receipt["checks"].append({
                "name": "mfrp-altered-check", "command": ["python", "-B", "altered"],
                "durationSeconds": 0.0, "status": "PASS",
            })
        else:
            _set_pointer(receipt, pointer, [{"name": "narrow-only", "status": "PASS"}])
    elif case_id in {"C03", "C11"}:
        _set_pointer(receipt, pointer, "6" * 64 if case_id == "C03" else "not-a-sha256")
    elif case_id == "C02":
        _set_pointer(receipt, pointer, [{"name": "same-role-substitution", "status": "PASS"}])
    elif case_id == "C04":
        _set_pointer(receipt, pointer, "AVAILABLE_MATCHED")
    elif case_id == "C05":
        _set_pointer(receipt, pointer, "0" * 40)
    elif case_id == "C06":
        _set_pointer(receipt, pointer, "RECONCILED")
    elif case_id == "C12":
        _set_pointer(receipt, pointer, "CLOSED")
    elif case_id == "C13":
        receipt["machineVerification"]["deterministicResults"].append(
            {"name": "fabricated-unrun-check", "status": "PASS"}
        )
    elif case_id == "C16B":
        _set_pointer(receipt, pointer, "7" * 64)
    else:
        _set_pointer(receipt, pointer, "MFRP_MUTATED_VALUE")
    changed = _jcs_bytes(receipt) != before
    if operator == "NO_MUTATION" and changed:
        raise AssertionError(f"{case_id}: NO_MUTATION changed payload")
    if operator != "NO_MUTATION" and not changed:
        raise AssertionError(f"{case_id}: mutation did not change serialized bytes")
    return changed


def observe_receipt(receipt: dict) -> dict:
    validator_payload = receipt
    valid, reason = _validate_receipt_integrity(validator_payload)
    readout_payload = validator_payload
    readout = machine_readout_to_dict(
        build_machine_verification_readout(valid, readout_payload, reason)
    )
    assert readout is not None
    return {
        "validatorAccepted": valid,
        "validatorReason": reason,
        "validatorReadoutSamePayloadObject": validator_payload is readout_payload,
        "readout": readout,
    }


def evaluate_predicate(case: dict, observation: dict) -> bool:
    predicate = case["requiredSafetyPredicate"]
    valid = observation["validatorAccepted"]
    readout = observation["readout"]
    if predicate == "POSITIVE_CONTROL_VALID":
        return valid and readout["status"] == DETERMINISTIC_PREFLIGHT_COMPLETE
    if predicate == "RECEIPT_REJECTED":
        return not valid
    if predicate == "IDENTITY_DRIFT_REJECTED":
        return not valid and any(
            term in observation["validatorReason"]
            for term in ("identity", "Identity", "envelope", "Digest", "digest")
        )
    if predicate == "GAP_SURFACED_UNCLASSIFIED":
        return bool(
            readout["unclassified"] or readout["notCheckedScope"]
            or readout["limitations"] or readout["exceptions"]
        )
    if predicate == "HARD_OBLIGATION_NOT_CLOSED":
        return (not valid) or "hard-obligation map not checked" in readout["unclassified"]
    if predicate == "SECRET_SENTINEL_NOT_EMITTED":
        return SECRET_SENTINEL not in json.dumps(readout, sort_keys=True)
    raise ValueError(f"unknown predicate: {predicate}")


def assert_evaluator_conformance(evaluator: Callable[[dict, dict], bool]) -> None:
    negative_case = {"requiredSafetyPredicate": "SECRET_SENTINEL_NOT_EMITTED"}
    negative_observation = {
        "validatorAccepted": False,
        "validatorReason": "receipt receiptDigest mismatch",
        "readout": {"exceptions": [SECRET_SENTINEL]},
    }
    if evaluator(negative_case, negative_observation):
        raise ValueError("predicate evaluator accepts the fixed negative calibration")


def build_ledger(oracle_path: Path, execution_base: str | None = None) -> dict:
    raw = oracle_path.read_bytes()
    oracle = json.loads(raw.decode("utf-8"))
    required = validate_oracle(oracle, raw)
    identities = {
        "oracleContainingCommit": ORACLE_COMMIT,
        "oracleContainingCommitBlobSha256": _sha_bytes(_git_blob(ORACLE_COMMIT, ORACLE_PATH)),
        "oracleContainingCommitMatch": _sha_bytes(_git_blob(ORACLE_COMMIT, ORACLE_PATH)) == ORACLE_SHA256,
        "oracleFileSha256": _sha_bytes(raw),
        "oracleAllFieldJcsSha256": _sha_bytes(_jcs_bytes(oracle)),
        "requiredSetJcsSha256": _sha_bytes(_jcs_bytes(required)),
        "p2Owners": [
            {"path": path, "sha256": _sha_file(REPO_ROOT / path),
             "expectedSha256": expected, "match": _sha_file(REPO_ROOT / path) == expected}
            for path, expected in OWNER_HASHES.items()
        ],
        "governanceDesigns": [
            {"path": path, "sha256": _sha_file(REPO_ROOT / path),
             "expectedSha256": expected, "match": _sha_file(REPO_ROOT / path) == expected}
            for path, expected in DESIGN_HASHES.items()
        ],
    }
    if not identities["oracleContainingCommitMatch"]:
        raise ValueError("oracle containing-commit identity drift")
    if not all(item["match"] for item in identities["p2Owners"] + identities["governanceDesigns"]):
        raise ValueError("P2 owner or design identity drift")
    control = _canonical_receipt()
    control_valid, _ = _validate_receipt_integrity(control)
    if not control_valid:
        raise ValueError("canonical P2 control receipt rejected")
    assert_evaluator_conformance(evaluate_predicate)
    results = []
    for case in oracle["cases"]:
        if case["caseId"] in NON_REPRESENTABLE:
            results.append({
                "caseId": case["caseId"], "family": case["family"],
                "zeroToleranceClass": case["zeroToleranceClass"],
                "mutationOperator": case["mutation"]["operator"],
                "executionDisposition": "NOT_REPRESENTABLE_BY_CURRENT_P2",
                "predicate": case["requiredSafetyPredicate"],
                "predicateSatisfied": False,
                "limitation": "no honest current-P2 observation route exists",
            })
            continue
        receipt = copy.deepcopy(control)
        changed = apply_mutation(receipt, case)
        observation = observe_receipt(receipt)
        results.append({
            "caseId": case["caseId"], "family": case["family"],
            "zeroToleranceClass": case["zeroToleranceClass"],
            "mutationOperator": case["mutation"]["operator"],
            "serializedBytesChanged": changed,
            "executionDisposition": "ACTUAL_P2_SEAM_OBSERVED",
            "validatorReadoutSamePayloadObject": observation["validatorReadoutSamePayloadObject"],
            "validatorAccepted": observation["validatorAccepted"],
            "validatorReason": observation["validatorReason"],
            "readout": observation["readout"],
            "predicate": case["requiredSafetyPredicate"],
            "predicateSatisfied": evaluate_predicate(case, observation),
        })
    missing = sorted(set(required["requiredCaseIds"]) - {item["caseId"] for item in results})
    if missing or len(results) != 19:
        raise ValueError("execution coverage is incomplete")
    predicate_misses = [item["caseId"] for item in results if not item["predicateSatisfied"]]
    candidate = (
        "REPLAY_EVIDENCE_COMPLETE_PASS_CANDIDATE"
        if not predicate_misses else "REPLAY_EVIDENCE_COMPLETE_RETURN_TO_DESIGN_CANDIDATE"
    )
    ledger = {
        "schema": RESULT_SCHEMA,
        "executionBaseHead": execution_base or _git_head(),
        "sourceIdentities": identities,
        "coverage": {
            "requiredCaseCount": 19, "observedCaseCount": len(results),
            "requiredFamilyCount": 18, "observedFamilyCount": len({x["family"] for x in results}),
            "requiredZeroToleranceClassCount": 7,
            "observedZeroToleranceClassCount": len({
                x["zeroToleranceClass"] for x in results if x["zeroToleranceClass"] != "NONE"
            }),
            "missingCaseIds": [], "extraCaseIds": [],
            "nonRepresentableCaseIds": sorted(NON_REPRESENTABLE),
            "actualP2ObservationCount": sum(
                x["executionDisposition"] == "ACTUAL_P2_SEAM_OBSERVED" for x in results
            ),
        },
        "cases": results,
        "limitations": [
            "C07, C08 and C18 are not representable by current P2 and are not counted as detected or satisfied.",
            "C15 deliberately records that the fixed non-secret sentinel is emitted by the current readout.",
            "Receipt-local consistency is not correctness, phase-return identity, authorization, or closure.",
        ],
        "predicateMissCaseIds": predicate_misses,
        "workerTerminalCandidate": candidate,
        "reviewerDisposition": "REVIEWER_OWNED_NOT_SET",
        "claimBoundary": "Local deterministic actual-P2 replay evidence only; reviewer retains evaluation, acceptance and closure.",
    }
    if any(value in FORBIDDEN_REVIEWER_OUTCOMES for value in _walk_strings(ledger)):
        raise ValueError("runner attempted to emit a reviewer-owned outcome")
    return ledger


def _walk_strings(value: object):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from _walk_strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from _walk_strings(item)


def ledger_bytes(ledger: dict) -> bytes:
    return (json.dumps(ledger, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--oracle", default=str(ORACLE_PATH))
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--execution-base",
        default=None,
        help="Frozen execution base to bind into deterministic output (defaults to HEAD).",
    )
    args = parser.parse_args()
    oracle_path = Path(args.oracle)
    if not oracle_path.is_absolute():
        oracle_path = REPO_ROOT / oracle_path
    output = Path(args.output)
    if not output.is_absolute():
        output = REPO_ROOT / output
    ledger = build_ledger(oracle_path, execution_base=args.execution_base)
    output.write_bytes(ledger_bytes(ledger))
    print(json.dumps({
        "schema": ledger["schema"],
        "caseCount": ledger["coverage"]["observedCaseCount"],
        "actualP2ObservationCount": ledger["coverage"]["actualP2ObservationCount"],
        "predicateMissCaseIds": ledger["predicateMissCaseIds"],
        "workerTerminalCandidate": ledger["workerTerminalCandidate"],
        "outputSha256": _sha_file(output),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Fail-closed detached implementation-proposal return contract.

Owns authority, dispatch binding, path/inventory safety, state projection and
local-authority-forgery rejection. A positive result is local-verification
readiness only: never CVF SOT, promotion, integration or runtime proof.
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any


class ReturnContractError(RuntimeError):
    """A fail-closed detached-return contract violation."""


EMITTER_SHARED_WORKSPACE_WORKER = "SHARED_WORKSPACE_DELEGATED_WORKER"
EMITTER_DETACHED_EXTERNAL_AGENT = "DETACHED_EXTERNAL_AGENT"
EMITTER_CLASSES = (EMITTER_SHARED_WORKSPACE_WORKER, EMITTER_DETACHED_EXTERNAL_AGENT)

STATUS_EXTERNAL_RETURN_READY = "EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION"
STATUS_NOT_CVF_SOT = "NOT_CVF_SOT"
STATUS_ABSORPTION_NOT_COMPLETE = "ABSORPTION_NOT_COMPLETE"
REQUIRED_DETACHED_STATUS_STATEMENTS = (
    STATUS_EXTERNAL_RETURN_READY,
    STATUS_NOT_CVF_SOT,
    STATUS_ABSORPTION_NOT_COMPLETE,
)

# Legacy protocol-1.2 read alias; new detached producers must never emit it.
LEGACY_COMPLETE_STATUS = "COMPLETE_PENDING_LOCAL_RECONCILIATION"

# Forbidden completion/absorption/integration/runtime/SOT claims.
FORBIDDEN_COMPLETION_CLAIMS = (
    "ABSORPTION_COMPLETE",
    "ABSORPTION_COMPLETE_USE_PROVEN",
    "INTEGRATED_INTO_CVF",
    "CVF_SOT_UPDATED",
    "CVF_RUNTIME_PROVEN",
    "SOURCE_RECONCILED",
    "OWNER_ACCEPTED",
    "CVF_OWNER_INTEGRATED",
    "USE_PROVEN",
)

AUTHORITY_OBJECT_FIELD = "authorityObject"
DISPATCH_BINDING_FIELD = "dispatchBinding"
_AUTHORITY_OBJECT_REQUIRED_FIELDS = {
    "emitterClass": EMITTER_DETACHED_EXTERNAL_AGENT,
    "authorityClass": "EXTERNAL_PROPOSAL",
    "cvfSot": False,
    "localSemanticReviewRequired": True,
    "automaticPromotionAllowed": False,
    "absorptionComplete": False,
    "runtimeUseProven": False,
}
_AUTHORITY_OBJECT_ALLOWED_FIELDS = frozenset(_AUTHORITY_OBJECT_REQUIRED_FIELDS)
_DISPATCH_BINDING_FIELDS = frozenset({
    "taskCapsuleSha256", "taskId", "protocolVersion", "sourceRepository",
    "sourceCommit", "cvfPublicRepository", "cvfPublicCommit",
})

RESERVED_LOCAL_ONLY_NAMES = frozenset({
    "LOCAL_PROMOTION_RECEIPT.json",
    "RETURN_AUTHORITY.json",
    "CVF_LOCAL_PROMOTION_RECEIPT.json",
    "LOCAL_PROMOTION_RECEIPT",
})
RESERVED_LOCAL_AUTHORITY_ALIAS = re.compile(
    r"(?i)(?:local.*promotion|promotion.*receipt|return.*authority|sot.*acceptance).*(?:\.json)?$"
)

DETACHED_RETURN_REQUIRED_ROOT_ARTIFACTS = (
    "README.md",
    "EXTERNAL_AGENT_RETURN_MANIFEST.json",
    "SOURCE_MANIFEST.md",
    "DECISION_LOG.md",
    "TEST_EVIDENCE.md",
    "CLAIM_BOUNDARY.md",
    "FILE_INVENTORY.sha256",
    "PROPOSED_TARGET_MAP.json",
)
PROPOSED_CHANGESET_DIRNAME = "PROPOSED_CVF_CHANGESET"

TARGET_MAP_OPERATIONS = ("add", "modify", "delete-proposal")
TARGET_MAP_ALLOWED_FIELDS = frozenset({
    "proposedTarget", "sha256", "sourceOrFindingIds", "intendedOwnerPath",
    "intendedOwnerSymbol", "operation", "maturityAndClaimClass",
    "consumingTestsOrEvidence", "unresolvedLocalFacts",
    "runtimeIntegrationPending", "useProofPending",
})

SOURCE_COVERAGE_VERDICTS = (
    "NOT_VERIFIED", "PARTIAL", "COMPLETE_WITH_DECLARED_EXCLUSIONS", "COMPLETE_VERIFIED", "BLOCKED", "STALE_SNAPSHOT",
)
SOURCE_RECONCILIATION_STATES = ("NOT_STARTED", "PENDING_LOCAL_RECONCILIATION", "SOURCE_RECONCILED", "BLOCKED")
OWNER_PROMOTION_STATES = ("EXTERNAL_PROPOSAL", "LOCAL_REVIEWED", "OWNER_ACCEPTED", "CVF_OWNER_INTEGRATED", "REJECTED_OR_DEFERRED")
RUNTIME_REALIZATION_STATES = ("NOT_APPLICABLE_WITH_REASON", "RUNTIME_CANDIDATE", "IMPLEMENTED", "BLOCKED")
REPRESENTATIVE_USE_PROOF_STATES = ("NOT_REQUIRED_WITH_REASON", "PENDING_OPERATOR_AUTHORIZED_RUNTIME_PROOF", "USE_PROVEN", "BLOCKED")

DERIVED_ABSORPTION_NOT_COMPLETE = "ABSORPTION_NOT_COMPLETE"
DERIVED_ABSORPTION_COMPLETE_USE_PROVEN = "ABSORPTION_COMPLETE_USE_PROVEN"
DERIVED_NO_RUNTIME_VALUE_WITH_REASON = "NO_RUNTIME_VALUE_WITH_REASON"

# Locally owned terminal states a detached emitter may never claim.
_EXTERNAL_FORBIDDEN_STATE_VALUES = {
    "sourceReconciliationState": {"SOURCE_RECONCILED"},
    "ownerPromotionState": {"OWNER_ACCEPTED", "CVF_OWNER_INTEGRATED"},
    "runtimeRealizationState": {"IMPLEMENTED"},
    "representativeUseProofState": {"USE_PROVEN"},
}

SAFE_REL_PATH = re.compile(r"^(?!/)(?!\.\./)(?!.*/\.\./)(?!.*\\)(?!.*:)(?!.*//)(?!\s)(?!.*\s$).+$")
SHA40 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
SECRET_LIKE = re.compile(
    rb"(?i)(?:-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|"
    rb"(?:api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*[\"']?[A-Za-z0-9_./+\-=]{8,})"
)
_WINDOWS_RESERVED_DEVICE_NAMES = frozenset({
    "CON", "PRN", "AUX", "NUL",
    *(f"COM{n}" for n in range(1, 10)),
    *(f"LPT{n}" for n in range(1, 10)),
})


def _nonblank_str(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _candidate_safe_rel_path(value: str) -> bool:
    path = PurePosixPath(value)
    return bool(value) and not path.is_absolute() and ".." not in path.parts and "\\" not in value


def is_safe_proposed_path(value: str) -> bool:
    """Accept only unambiguous repo-relative POSIX paths."""
    if not isinstance(value, str) or not value or not SAFE_REL_PATH.match(value):
        return False
    if value.startswith("~"):
        return False
    if unicodedata.normalize("NFC", value) != value or any(ord(char) < 32 for char in value):
        return False
    posix = PureWindowsPath(value.replace("/", "\\"))
    if posix.drive or posix.root:
        return False
    parts = value.split("/")
    for part in parts:
        if not part or part in (".", "..") or part.endswith((" ", ".")):
            return False
        stem = part.split(".", 1)[0].upper()
        if stem in _WINDOWS_RESERVED_DEVICE_NAMES:
            return False
    return True


def detect_reserved_local_only_artifacts(root: Path) -> list[str]:
    """Find reserved local-authority artifacts anywhere below the return root."""
    found: list[str] = []
    if not root.is_dir():
        return found
    for path in root.rglob("*"):
        if path.is_file() and (
            path.name in RESERVED_LOCAL_ONLY_NAMES or RESERVED_LOCAL_AUTHORITY_ALIAS.fullmatch(path.name)
        ):
            found.append(path.relative_to(root).as_posix())
    return sorted(found)


def validate_authority_object(candidate: Any, errors: list[str]) -> None:
    """Validate the strict mode-scoped authority object without proving its claims."""
    if not isinstance(candidate, dict):
        errors.append(f"manifest.{AUTHORITY_OBJECT_FIELD} must be an object")
        return
    undeclared = sorted(set(candidate) - _AUTHORITY_OBJECT_ALLOWED_FIELDS)
    if undeclared:
        errors.append(
            f"manifest.{AUTHORITY_OBJECT_FIELD} contains undeclared field(s): {', '.join(undeclared)}"
        )
    for field, expected in _AUTHORITY_OBJECT_REQUIRED_FIELDS.items():
        if field not in candidate:
            errors.append(f"manifest.{AUTHORITY_OBJECT_FIELD}.{field} is required")
            continue
        actual = candidate[field]
        if isinstance(expected, bool):
            if type(actual) is not bool or actual != expected:
                errors.append(
                    f"manifest.{AUTHORITY_OBJECT_FIELD}.{field} must be the literal boolean {expected!r}"
                )
        elif actual != expected:
            errors.append(
                f"manifest.{AUTHORITY_OBJECT_FIELD}.{field} must equal {expected!r}, got {actual!r}"
            )


def validate_status_statements(readme_text: str, manifest: dict[str, Any], errors: list[str]) -> None:
    """Require readiness boundaries and reject detached completion claims."""
    haystacks = [readme_text]
    for field in ("returnStatus", "status", "absorptionStatus"):
        value = manifest.get(field)
        if isinstance(value, str):
            haystacks.append(value)
    combined = "\n".join(haystacks)

    for required in REQUIRED_DETACHED_STATUS_STATEMENTS:
        if required not in combined:
            errors.append(f"detached return must expose required status statement: {required}")

    for forbidden in FORBIDDEN_COMPLETION_CLAIMS:
        if forbidden in combined:
            errors.append(f"detached return contains forbidden completion/absorption claim: {forbidden}")

    declared_status = manifest.get("returnStatus")
    if declared_status == LEGACY_COMPLETE_STATUS:
        errors.append(
            f"new detached implementation-proposal producers must not emit legacy status {LEGACY_COMPLETE_STATUS!r}; "
            f"use {STATUS_EXTERNAL_RETURN_READY!r}"
        )


def validate_dispatch_binding(candidate: Any, capsule_path: Path, errors: list[str]) -> str | None:
    """Bind the return to the exact locally supplied capsule and its source/public pins."""
    if not isinstance(candidate, dict) or set(candidate) != _DISPATCH_BINDING_FIELDS:
        errors.append(f"manifest.{DISPATCH_BINDING_FIELD} must contain exactly {sorted(_DISPATCH_BINDING_FIELDS)}")
        return None
    if not SHA256.fullmatch(str(candidate.get("taskCapsuleSha256", ""))):
        errors.append(f"manifest.{DISPATCH_BINDING_FIELD}.taskCapsuleSha256 must be lowercase SHA-256")
    for field in ("sourceCommit", "cvfPublicCommit"):
        if not SHA40.fullmatch(str(candidate.get(field, ""))):
            errors.append(f"manifest.{DISPATCH_BINDING_FIELD}.{field} must be a lowercase 40-character Git SHA")
    for field in ("taskId", "protocolVersion", "sourceRepository", "cvfPublicRepository"):
        if not _nonblank_str(candidate.get(field)):
            errors.append(f"manifest.{DISPATCH_BINDING_FIELD}.{field} must be non-blank")
    if capsule_path.is_symlink() or not capsule_path.is_file():
        errors.append("the exact local task capsule is missing or is a symlink")
        return None
    raw = capsule_path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    try:
        capsule = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        errors.append("the exact local task capsule is not valid UTF-8 JSON")
        return digest
    sources = capsule.get("sourceRepositories") if isinstance(capsule, dict) else None
    source = sources[0] if isinstance(sources, list) and len(sources) == 1 and isinstance(sources[0], dict) else {}
    task = capsule.get("task") if isinstance(capsule, dict) and isinstance(capsule.get("task"), dict) else {}
    public = capsule.get("cvfPublicSource") if isinstance(capsule, dict) and isinstance(capsule.get("cvfPublicSource"), dict) else {}
    expected = {
        "taskCapsuleSha256": digest, "taskId": task.get("id"), "protocolVersion": capsule.get("protocolVersion"),
        "sourceRepository": source.get("repository"), "sourceCommit": source.get("commit"),
        "cvfPublicRepository": public.get("repository"), "cvfPublicCommit": public.get("commit"),
    }
    for field, value in expected.items():
        if candidate.get(field) != value:
            errors.append(f"manifest.{DISPATCH_BINDING_FIELD}.{field} does not match the exact local task capsule")
    if task.get("workingMode") != "DETACHED_IMPLEMENTATION_PROPOSAL" or task.get("executionClass") != EMITTER_DETACHED_EXTERNAL_AGENT:
        errors.append("the exact local task capsule is not a DETACHED_EXTERNAL_AGENT implementation-proposal capsule")
    return digest


def validate_detached_inventory(root: Path, errors: list[str]) -> None:
    """Reject symlinks/secrets and reconcile every hidden or ordinary returned file."""
    actual: dict[str, str] = {}
    for path in root.rglob("*") if root.is_dir() else ():
        rel = path.relative_to(root).as_posix()
        if path.is_symlink():
            errors.append(f"detached return contains a forbidden symlink: {rel}")
            continue
        if not path.is_file() or rel == "FILE_INVENTORY.sha256":
            continue
        if not is_safe_proposed_path(rel):
            errors.append(f"detached return contains an unsafe filesystem path: {rel}")
        raw = path.read_bytes()
        actual[rel] = hashlib.sha256(raw).hexdigest()
        if SECRET_LIKE.search(raw):
            errors.append(f"detached return contains secret-like material in: {rel}")
    inventory_path = root / "FILE_INVENTORY.sha256"
    if not inventory_path.is_file() or inventory_path.is_symlink():
        return
    raw_inventory = inventory_path.read_bytes()
    if raw_inventory.startswith(b"\xef\xbb\xbf") or b"\r\n" in raw_inventory or (raw_inventory and not raw_inventory.endswith(b"\n")):
        errors.append("FILE_INVENTORY.sha256 must be UTF-8 without BOM, use LF, and have one trailing LF")
    declared: dict[str, str] = {}
    previous = ""
    for number, line in enumerate(raw_inventory.decode("utf-8-sig", errors="replace").splitlines(), 1):
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            errors.append(f"inventory line {number} has invalid format")
            continue
        digest, rel = match.groups()
        if not is_safe_proposed_path(rel) or rel == "FILE_INVENTORY.sha256":
            errors.append(f"inventory line {number} has an unsafe or self-referential path")
        if previous and rel <= previous:
            errors.append("inventory paths are not unique ordinal-sorted")
        previous = rel
        declared[rel] = digest
    if declared != dict(sorted(actual.items())):
        errors.append("FILE_INVENTORY.sha256 does not exactly match every returned file and digest")


def validate_proposed_target_map(target_map: Any, changeset_root: Path, errors: list[str]) -> dict[str, dict[str, Any]]:
    """Validate the target map and return its path-to-row projection."""
    rows: dict[str, dict[str, Any]] = {}
    if not isinstance(target_map, dict):
        errors.append("PROPOSED_TARGET_MAP.json must be a JSON object")
        return rows
    if set(target_map) != {"entries"}:
        errors.append("PROPOSED_TARGET_MAP.json must contain only the entries field")
    entries = target_map.get("entries")
    if not isinstance(entries, list) or not entries:
        errors.append("PROPOSED_TARGET_MAP.json.entries must be a non-empty list")
        return rows

    seen_targets: set[str] = set()
    seen_canonical_targets: set[str] = set()
    for index, entry in enumerate(entries):
        prefix = f"PROPOSED_TARGET_MAP.entries[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{prefix} must be an object")
            continue
        undeclared = sorted(set(entry) - TARGET_MAP_ALLOWED_FIELDS)
        if undeclared:
            errors.append(f"{prefix} contains undeclared field(s): {', '.join(undeclared)}")
        target = entry.get("proposedTarget")
        if not is_safe_proposed_path(str(target)):
            errors.append(f"{prefix}.proposedTarget is missing, unsafe, or not repo-relative")
            target = None
        elif target in seen_targets:
            errors.append(f"{prefix}.proposedTarget is a duplicate: {target}")
        else:
            seen_targets.add(target)
            canonical_target = unicodedata.normalize("NFC", target).casefold()
            if canonical_target in seen_canonical_targets:
                errors.append(f"{prefix}.proposedTarget collides after canonical case normalization: {target}")
            seen_canonical_targets.add(canonical_target)

        digest = entry.get("sha256")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            errors.append(f"{prefix}.sha256 must be a 64-character lowercase hex digest")

        source_ids = entry.get("sourceOrFindingIds")
        if not isinstance(source_ids, list) or not source_ids or not all(_nonblank_str(item) for item in source_ids):
            errors.append(f"{prefix}.sourceOrFindingIds must be a non-empty list of non-blank strings")
        unresolved = entry.get("unresolvedLocalFacts")
        if not isinstance(unresolved, list) or not all(_nonblank_str(item) for item in unresolved):
            errors.append(f"{prefix}.unresolvedLocalFacts must be a list of non-blank strings")

        if not is_safe_proposed_path(str(entry.get("intendedOwnerPath", ""))):
            errors.append(f"{prefix}.intendedOwnerPath must be a safe repo-relative path")

        operation = entry.get("operation")
        if operation not in TARGET_MAP_OPERATIONS:
            errors.append(f"{prefix}.operation must be one of {TARGET_MAP_OPERATIONS}")

        if not _nonblank_str(entry.get("maturityAndClaimClass")):
            errors.append(f"{prefix}.maturityAndClaimClass must be a non-blank string")

        tests = entry.get("consumingTestsOrEvidence")
        if not isinstance(tests, list) or not tests or not all(_nonblank_str(item) for item in tests):
            errors.append(f"{prefix}.consumingTestsOrEvidence must be a non-empty list of non-blank strings")

        for bool_field in ("runtimeIntegrationPending", "useProofPending"):
            if bool_field not in entry or type(entry.get(bool_field)) is not bool:
                errors.append(f"{prefix}.{bool_field} must be a literal boolean")

        if target and operation in ("add", "modify"):
            actual_path = changeset_root / target
            if not actual_path.is_file():
                errors.append(
                    f"{prefix}.proposedTarget {target!r} declares operation {operation!r} "
                    f"but is missing from {PROPOSED_CHANGESET_DIRNAME}/"
                )
            elif isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest):
                actual_digest = hashlib.sha256(actual_path.read_bytes()).hexdigest()
                if actual_digest != digest:
                    errors.append(
                        f"{prefix}.sha256 does not match the actual proposed file at {target!r}"
                    )
        elif target and operation == "delete-proposal" and (changeset_root / target).exists():
            errors.append(
                f"{prefix}.proposedTarget {target!r} is a delete-proposal but a file exists under "
                f"{PROPOSED_CHANGESET_DIRNAME}/; a deletion must remain proposal-only evidence, not an actual file"
            )

        if target:
            rows[target] = entry
    return rows


def validate_changeset_tree_matches_target_map(changeset_root: Path, target_rows: dict[str, dict[str, Any]], errors: list[str]) -> None:
    """Reject physical proposal files without matching add/modify rows."""
    if not changeset_root.is_dir():
        return
    add_or_modify = {path for path, row in target_rows.items() if row.get("operation") in ("add", "modify")}
    for path in changeset_root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(changeset_root).as_posix()
        if rel not in add_or_modify:
            errors.append(
                f"{PROPOSED_CHANGESET_DIRNAME}/{rel} is present on disk but is not bound by an "
                f"add/modify row in PROPOSED_TARGET_MAP.json"
            )


def validate_state_vector(state_vector: Any, emitter_class: str, errors: list[str]) -> dict[str, str] | None:
    """Validate the independent machine-readable state vector. A detached
    external agent may report facts but can never emit a locally-owned
    terminal value for sourceReconciliationState, ownerPromotionState,
    runtimeRealizationState, or representativeUseProofState."""
    if not isinstance(state_vector, dict):
        errors.append("manifest.stateVector must be an object")
        return None

    checks = (
        ("sourceCoverageVerdict", SOURCE_COVERAGE_VERDICTS),
        ("sourceReconciliationState", SOURCE_RECONCILIATION_STATES),
        ("ownerPromotionState", OWNER_PROMOTION_STATES),
        ("runtimeRealizationState", RUNTIME_REALIZATION_STATES),
        ("representativeUseProofState", REPRESENTATIVE_USE_PROOF_STATES),
    )
    values: dict[str, str] = {}
    for field, allowed in checks:
        value = state_vector.get(field)
        if value not in allowed:
            errors.append(f"manifest.stateVector.{field} must be one of {allowed}")
        else:
            values[field] = value

    if emitter_class == EMITTER_DETACHED_EXTERNAL_AGENT:
        for field, forbidden_values in _EXTERNAL_FORBIDDEN_STATE_VALUES.items():
            actual = values.get(field)
            if actual in forbidden_values:
                errors.append(
                    f"a {EMITTER_DETACHED_EXTERNAL_AGENT} return must not emit "
                    f"stateVector.{field}={actual!r}; that value is local-review-only"
                )
    return values if len(values) == len(checks) else None


def derive_completion_projection(values: dict[str, str] | None) -> str:
    """Compute the derived maximum completion projection from a fully valid
    state vector, per the roadmap's non-implication rule. Returns the most
    conservative (least-complete) projection whenever any required
    dimension is missing or unsatisfied."""
    if not values:
        return DERIVED_ABSORPTION_NOT_COMPLETE

    coverage = values.get("sourceCoverageVerdict")
    reconciliation = values.get("sourceReconciliationState")
    owner = values.get("ownerPromotionState")
    runtime = values.get("runtimeRealizationState")
    use_proof = values.get("representativeUseProofState")

    coverage_satisfied = coverage in ("COMPLETE_WITH_DECLARED_EXCLUSIONS", "COMPLETE_VERIFIED")
    if not coverage_satisfied or reconciliation != "SOURCE_RECONCILED":
        return DERIVED_ABSORPTION_NOT_COMPLETE

    if owner in ("EXTERNAL_PROPOSAL", "LOCAL_REVIEWED", "OWNER_ACCEPTED"):
        return DERIVED_ABSORPTION_NOT_COMPLETE

    if owner == "CVF_OWNER_INTEGRATED":
        if runtime in ("RUNTIME_CANDIDATE", "IMPLEMENTED") and use_proof != "USE_PROVEN":
            return DERIVED_ABSORPTION_NOT_COMPLETE
        if runtime == "IMPLEMENTED" and use_proof == "USE_PROVEN":
            return DERIVED_ABSORPTION_COMPLETE_USE_PROVEN
        if runtime == "NOT_APPLICABLE_WITH_REASON" and use_proof == "NOT_REQUIRED_WITH_REASON":
            return DERIVED_NO_RUNTIME_VALUE_WITH_REASON

    return DERIVED_ABSORPTION_NOT_COMPLETE


# Legacy EARTR-ESC-R1 candidate-lane validators retained for API compatibility.

CANDIDATE_LANE_CONTRACT_VERSION = 1
CANDIDATE_LANE_EXTERNAL_SOURCE_VALUE = "EXTERNAL_SOURCE_VALUE_CANDIDATE"
CANDIDATE_LANE_CVF_INTERNAL_DEFECT = "CVF_INTERNAL_DEFECT_CANDIDATE"
CANDIDATE_LANE_NAMES = (CANDIDATE_LANE_EXTERNAL_SOURCE_VALUE, CANDIDATE_LANE_CVF_INTERNAL_DEFECT)
CANDIDATE_LANE_PUBLIC_OWNER_SEARCH_STATUSES = ("OWNER_CANDIDATES_FOUND", "PUBLIC_OWNER_SURFACE_NOT_FOUND", "PUBLIC_INSUFFICIENT_EVIDENCE", "NOT_APPLICABLE")
CANDIDATE_LANE_PUBLIC_OVERLAP_STATUSES = ("PUBLIC_CONFIRMED_EXISTING", "PUBLIC_SUGGESTS_ENRICHMENT", "PUBLIC_OWNER_SURFACE_NOT_FOUND", "PUBLIC_INSUFFICIENT_EVIDENCE", "NOT_APPLICABLE")
CANDIDATE_LANE_PRELIMINARY_VALUE_DISPOSITIONS = ("ABSORB", "ADAPT", "DEFER", "REJECT", "BLOCK", "NO_NEW_VALUE")
_CANDIDATE_LANE_SOURCE_VALUE_ALLOWED_FIELDS = frozenset({
    "candidateId", "preliminaryLane", "sourceRefs", "sourceLocations", "candidateSummary", "claimedValue",
    "publicOwnerSearch", "publicOverlap", "preliminaryValueDisposition", "questionsForLocalAgent", "sourceEvidence",
})
_CANDIDATE_LANE_INTERNAL_DEFECT_ALLOWED_FIELDS = frozenset({
    "candidateId", "preliminaryLane", "cvfPublicLocations", "triggerContextSourceRefs", "candidateSummary",
    "publicOwnerSearch", "questionsForLocalAgent", "sourceEvidence",
})
_CANDIDATE_LANE_INTERNAL_DEFECT_FORBIDDEN_FIELDS = ("sourceLocations", "claimedValue", "publicOverlap", "preliminaryValueDisposition")
_CANDIDATE_LANE_SOURCE_VALUE_FORBIDDEN_FIELDS = ("cvfPublicLocations", "triggerContextSourceRefs")


def _candidate_lane_no_undeclared_fields(candidate: dict[str, Any], prefix: str, allowed: frozenset[str], errors: list[str]) -> None:
    if "authorityStatus" in candidate:
        errors.append(f"{prefix}.authorityStatus is forbidden on a candidate row; authority status is manifest-level only")
    undeclared = sorted(set(candidate) - allowed - {"authorityStatus"})
    if undeclared:
        errors.append(f"{prefix} contains undeclared field(s) under strict v1: {', '.join(undeclared)}")
def _candidate_lane_optional_source_evidence(candidate: dict[str, Any], prefix: str, errors: list[str]) -> None:
    if "sourceEvidence" in candidate and not _nonblank_str(candidate.get("sourceEvidence")):
        errors.append(f"{prefix}.sourceEvidence must be a non-blank string when present")
def _candidate_lane_nonblank_list(value: Any, prefix: str, field: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not value or not all(_nonblank_str(item) for item in value):
        errors.append(f"{prefix}.{field} must be a non-empty list of non-blank strings")
def _candidate_lane_owner_search(search: Any, prefix: str, errors: list[str]) -> None:
    if not isinstance(search, dict) or search.get("status") not in CANDIDATE_LANE_PUBLIC_OWNER_SEARCH_STATUSES:
        errors.append(f"{prefix}.publicOwnerSearch.status must be one of {CANDIDATE_LANE_PUBLIC_OWNER_SEARCH_STATUSES}")
        return
    candidates = search.get("candidates")
    if search.get("status") == "OWNER_CANDIDATES_FOUND":
        if not isinstance(candidates, list) or not candidates:
            errors.append(f"{prefix}.publicOwnerSearch.candidates must be a non-empty list when status is OWNER_CANDIDATES_FOUND")
        else:
            for cand_index, owner_candidate in enumerate(candidates):
                cand_prefix = f"{prefix}.publicOwnerSearch.candidates[{cand_index}]"
                if not isinstance(owner_candidate, dict):
                    errors.append(f"{cand_prefix} must be an object")
                    continue
                if not _candidate_safe_rel_path(str(owner_candidate.get("path", ""))):
                    errors.append(f"{cand_prefix}.path is invalid or unsafe")
                if not _nonblank_str(owner_candidate.get("symbol")):
                    errors.append(f"{cand_prefix}.symbol must be a non-blank string")
                if not _nonblank_str(owner_candidate.get("basis")):
                    errors.append(f"{cand_prefix}.basis must be a non-blank string")
    elif candidates is not None and (not isinstance(candidates, list) or candidates):
        errors.append(f"{prefix}.publicOwnerSearch.candidates must be absent or empty when status is not OWNER_CANDIDATES_FOUND")
def _candidate_lane_overlap(overlap: Any, prefix: str, errors: list[str]) -> None:
    if not isinstance(overlap, dict) or overlap.get("status") not in CANDIDATE_LANE_PUBLIC_OVERLAP_STATUSES:
        errors.append(f"{prefix}.publicOverlap.status must be one of {CANDIDATE_LANE_PUBLIC_OVERLAP_STATUSES}")
        return
    if not _nonblank_str(overlap.get("basis")):
        errors.append(f"{prefix}.publicOverlap.basis must be a non-blank string")
def _candidate_lane_source_value(candidate: dict[str, Any], prefix: str, source_ids: set[str], errors: list[str]) -> None:
    _candidate_lane_no_undeclared_fields(candidate, prefix, _CANDIDATE_LANE_SOURCE_VALUE_ALLOWED_FIELDS, errors)
    for field in _CANDIDATE_LANE_SOURCE_VALUE_FORBIDDEN_FIELDS:
        if field in candidate:
            errors.append(f"{prefix}.{field} is forbidden for {CANDIDATE_LANE_EXTERNAL_SOURCE_VALUE}")
    source_refs = candidate.get("sourceRefs")
    if not isinstance(source_refs, list) or not source_refs or not all(_nonblank_str(item) for item in source_refs):
        errors.append(f"{prefix}.sourceRefs must be a non-empty list of non-blank strings")
        source_refs = []
    unresolved = [ref for ref in source_refs if ref not in source_ids]
    if unresolved:
        errors.append(f"{prefix}.sourceRefs contains unresolved source id(s): {', '.join(unresolved)}")
    locations = candidate.get("sourceLocations")
    location_refs: list[str] = []
    if not isinstance(locations, list) or not locations:
        errors.append(f"{prefix}.sourceLocations must be a non-empty list")
    else:
        for loc_index, location in enumerate(locations):
            loc_prefix = f"{prefix}.sourceLocations[{loc_index}]"
            if not isinstance(location, dict):
                errors.append(f"{loc_prefix} must be an object")
                continue
            ref = location.get("sourceRef")
            if not _nonblank_str(ref):
                errors.append(f"{loc_prefix}.sourceRef must be a non-blank string")
            else:
                location_refs.append(ref)
                if ref not in source_ids:
                    errors.append(f"{loc_prefix}.sourceRef does not resolve to an existing source id: {ref}")
            if not _candidate_safe_rel_path(str(location.get("path", ""))):
                errors.append(f"{loc_prefix}.path is invalid or unsafe")
            symbols = location.get("symbols")
            if not isinstance(symbols, list) or not symbols or not all(_nonblank_str(item) for item in symbols):
                errors.append(f"{loc_prefix}.symbols must be a non-empty list of non-blank strings")
    if isinstance(source_refs, list) and isinstance(locations, list) and locations:
        if set(source_refs) != set(location_refs):
            errors.append(f"{prefix}: set(sourceRefs) must equal set(sourceLocations[].sourceRef)")
    if not _nonblank_str(candidate.get("candidateSummary")):
        errors.append(f"{prefix}.candidateSummary must be a non-blank string")
    if not _nonblank_str(candidate.get("claimedValue")):
        errors.append(f"{prefix}.claimedValue must be a non-blank string")
    _candidate_lane_owner_search(candidate.get("publicOwnerSearch"), prefix, errors)
    _candidate_lane_overlap(candidate.get("publicOverlap"), prefix, errors)
    disposition = candidate.get("preliminaryValueDisposition")
    if disposition is None:
        errors.append(f"{prefix}.preliminaryValueDisposition is required")
    elif disposition not in CANDIDATE_LANE_PRELIMINARY_VALUE_DISPOSITIONS:
        errors.append(f"{prefix}.preliminaryValueDisposition must be one of {CANDIDATE_LANE_PRELIMINARY_VALUE_DISPOSITIONS}")
    _candidate_lane_nonblank_list(candidate.get("questionsForLocalAgent"), prefix, "questionsForLocalAgent", errors)
    _candidate_lane_optional_source_evidence(candidate, prefix, errors)
def _candidate_lane_internal_defect(candidate: dict[str, Any], prefix: str, source_ids: set[str], errors: list[str]) -> None:
    _candidate_lane_no_undeclared_fields(candidate, prefix, _CANDIDATE_LANE_INTERNAL_DEFECT_ALLOWED_FIELDS, errors)
    for field in _CANDIDATE_LANE_INTERNAL_DEFECT_FORBIDDEN_FIELDS:
        if field in candidate:
            errors.append(f"{prefix}.{field} is forbidden for {CANDIDATE_LANE_CVF_INTERNAL_DEFECT}")
    locations = candidate.get("cvfPublicLocations")
    if not isinstance(locations, list) or not locations:
        errors.append(f"{prefix}.cvfPublicLocations must be a non-empty list")
    else:
        for loc_index, location in enumerate(locations):
            loc_prefix = f"{prefix}.cvfPublicLocations[{loc_index}]"
            if not isinstance(location, dict):
                errors.append(f"{loc_prefix} must be an object")
                continue
            if not _candidate_safe_rel_path(str(location.get("path", ""))):
                errors.append(f"{loc_prefix}.path is invalid or unsafe")
            symbols = location.get("symbols")
            if not isinstance(symbols, list) or not symbols or not all(_nonblank_str(item) for item in symbols):
                errors.append(f"{loc_prefix}.symbols must be a non-empty list of non-blank strings")
    trigger_refs = candidate.get("triggerContextSourceRefs")
    if trigger_refs is not None:
        if not isinstance(trigger_refs, list) or not all(_nonblank_str(item) for item in trigger_refs):
            errors.append(f"{prefix}.triggerContextSourceRefs must be a list of non-blank strings")
        else:
            unresolved = [ref for ref in trigger_refs if ref not in source_ids]
            if unresolved:
                errors.append(f"{prefix}.triggerContextSourceRefs contains unresolved source id(s): {', '.join(unresolved)}")
    if not _nonblank_str(candidate.get("candidateSummary")):
        errors.append(f"{prefix}.candidateSummary must be a non-blank string")
    _candidate_lane_owner_search(candidate.get("publicOwnerSearch"), prefix, errors)
    _candidate_lane_nonblank_list(candidate.get("questionsForLocalAgent"), prefix, "questionsForLocalAgent", errors)
    _candidate_lane_optional_source_evidence(candidate, prefix, errors)


def candidate_lane_validate_candidates(manifest: dict[str, Any], errors: list[str]) -> str:
    """Validate suggestedAbsorptionCandidates under the dual-reader contract.
    Returns the effective candidate-contract status label."""
    discriminator = manifest.get("candidateContractVersion")
    candidates = manifest.get("suggestedAbsorptionCandidates")
    candidates_list = candidates if isinstance(candidates, list) else []
    if discriminator is None:
        return "LEGACY_EMPTY" if not candidates_list else "LEGACY_UNTYPED_NOT_PROMOTABLE"
    # bool is a subclass of int in Python; reject it explicitly so
    # `candidateContractVersion: true` is never accepted as the integer 1.
    if type(discriminator) is not int or discriminator != CANDIDATE_LANE_CONTRACT_VERSION:
        errors.append(f"manifest.candidateContractVersion is unsupported or malformed: {discriminator!r}")
        return "UNSUPPORTED_OR_MALFORMED"
    if not isinstance(candidates, list):
        errors.append("manifest.suggestedAbsorptionCandidates must be a list when candidateContractVersion is set")
        return "STRICT_V1"
    source_ids: set[str] = set()
    for source_index, source in enumerate(manifest.get("sources") or []):
        if not isinstance(source, dict):
            continue
        source_id = source.get("id")
        if not _nonblank_str(source_id):
            errors.append(f"sources[{source_index}].id must be a non-blank string under strict candidate contract v1")
        elif source_id in source_ids:
            errors.append(f"sources[{source_index}].id is a duplicate under strict candidate contract v1: {source_id}")
        else:
            source_ids.add(source_id)
    seen_ids: set[str] = set()
    for index, candidate in enumerate(candidates_list):
        prefix = f"suggestedAbsorptionCandidates[{index}]"
        if not isinstance(candidate, dict):
            errors.append(f"{prefix} must be an object")
            continue
        candidate_id = candidate.get("candidateId")
        if not _nonblank_str(candidate_id):
            errors.append(f"{prefix}.candidateId must be a non-blank string")
        elif candidate_id in seen_ids:
            errors.append(f"{prefix}.candidateId is a duplicate within this return: {candidate_id}")
        else:
            seen_ids.add(candidate_id)
        lane = candidate.get("preliminaryLane")
        if lane == CANDIDATE_LANE_EXTERNAL_SOURCE_VALUE:
            _candidate_lane_source_value(candidate, prefix, source_ids, errors)
        elif lane == CANDIDATE_LANE_CVF_INTERNAL_DEFECT:
            _candidate_lane_internal_defect(candidate, prefix, source_ids, errors)
        else:
            errors.append(f"{prefix}.preliminaryLane must be one of {CANDIDATE_LANE_NAMES}")
    return "STRICT_V1"


def validate_detached_return(root: Path, task_capsule_path: Path | None = None) -> dict[str, Any]:
    """Validate readiness only; never grant promotion, integration or completion."""
    errors: list[str] = []

    for name in DETACHED_RETURN_REQUIRED_ROOT_ARTIFACTS:
        if not (root / name).is_file():
            errors.append(f"missing required detached-return root artifact: {name}")

    validate_detached_inventory(root, errors)

    forged = detect_reserved_local_only_artifacts(root)
    for path in forged:
        errors.append(
            f"detached return root contains reserved local-only authority artifact (authority forgery): {path}"
        )

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

    emitter_class = manifest.get("emitterClass")
    if emitter_class not in EMITTER_CLASSES:
        errors.append(f"manifest.emitterClass must be one of {EMITTER_CLASSES}")

    validate_authority_object(manifest.get(AUTHORITY_OBJECT_FIELD), errors)
    capsule_path = task_capsule_path or root.parent / "CVF_EXTERNAL_AGENT_TASK_CAPSULE.json"
    if root.resolve() == capsule_path.resolve() or root.resolve() in capsule_path.resolve().parents:
        errors.append("the local task capsule must remain outside the detached return root")
    validated_capsule_sha256 = validate_dispatch_binding(
        manifest.get(DISPATCH_BINDING_FIELD), capsule_path, errors
    )

    readme = (root / "README.md").read_text(encoding="utf-8", errors="replace") if (root / "README.md").is_file() else ""
    validate_status_statements(readme, manifest, errors)

    changeset_root = root / PROPOSED_CHANGESET_DIRNAME
    target_map: dict[str, Any] = {}
    target_map_path = root / "PROPOSED_TARGET_MAP.json"
    if target_map_path.is_file():
        try:
            target_map = json.loads(target_map_path.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"PROPOSED_TARGET_MAP.json is invalid JSON: {exc}")
    else:
        errors.append("missing required detached-return root artifact: PROPOSED_TARGET_MAP.json")

    target_rows = validate_proposed_target_map(target_map, changeset_root, errors) if isinstance(target_map, dict) else {}
    validate_changeset_tree_matches_target_map(changeset_root, target_rows, errors)

    state_values = validate_state_vector(manifest.get("stateVector"), emitter_class, errors)
    derived_projection = derive_completion_projection(state_values)

    declared_projection = manifest.get("derivedCompletionProjection")
    if declared_projection is not None and declared_projection != derived_projection:
        errors.append(
            f"manifest.derivedCompletionProjection {declared_projection!r} does not match the "
            f"independently recomputed projection {derived_projection!r}"
        )
    if emitter_class == EMITTER_DETACHED_EXTERNAL_AGENT and derived_projection != DERIVED_ABSORPTION_NOT_COMPLETE:
        errors.append(
            f"a {EMITTER_DETACHED_EXTERNAL_AGENT} return can never independently derive "
            f"{derived_projection!r}; only local review can advance past {DERIVED_ABSORPTION_NOT_COMPLETE!r}"
        )

    status = STATUS_EXTERNAL_RETURN_READY if not errors else "RETURN_FOR_REPAIR"
    manifest_sha256 = hashlib.sha256(manifest_path.read_bytes()).hexdigest() if manifest_path.is_file() else None
    return {
        "schema": "cvf.externalAgentDetachedReturnValidationReceipt.v1",
        "returnRoot": str(root.resolve()),
        "emitterClass": emitter_class,
        "status": status,
        "cvfSot": False,
        "absorptionComplete": False,
        "derivedCompletionProjection": derived_projection,
        "validatedReturnManifestSha256": manifest_sha256,
        "validatedTaskCapsuleSha256": validated_capsule_sha256,
        "errors": errors,
        "claimBoundary": (
            "Structural, integrity, path-safety, authority-object, and state-vector validation only. "
            "Maximum positive result is EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION; this is never a "
            "CVF acceptance, absorption, integration, or SOT promotion decision."
        ),
    }

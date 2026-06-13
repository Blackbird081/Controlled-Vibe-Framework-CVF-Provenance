#!/usr/bin/env python3
"""
CVF Work Order Dispatch Quality Gate

Hard-fails new or amended governed dispatch packets that try to move from
planning into execution before the required source, roadmap, prerequisite, and
GC-018 evidence exists.
"""

from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BASE_CANDIDATES = ("origin/main", "origin/master", "main", "master")

STANDARD_PATH = "docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md"
WORK_ORDER_TEMPLATE_PATH = "docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md"
WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_PATH = (
    "docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md"
)
WORK_ORDER_FINALITY_ADDENDUM_PATH = (
    "docs/reference/CVF_AGENT_WORK_ORDER_FINALITY_AND_REVIEW_CONVERSION_ADDENDUM_2026-06-12.md"
)
WORKER_AUTONOMY_STANDARD_PATH = "docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md"
HOOK_CHAIN_PATH = "governance/compat/run_local_governance_hook_chain.py"
THIS_SCRIPT_PATH = "governance/compat/check_work_order_dispatch_quality.py"
FILE_SIZE_REGISTRY_PATH = "governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json"
NEAR_THRESHOLD_PLAN_MARKER = "Near-Threshold Owner Maintainability Plan"
NEAR_THRESHOLD_TEMPLATE_OWNER_MARKER = "Near-Threshold Template Owner Discipline"
FULFILLMENT_MANIFEST_MARKER = "Work-Order Fulfillment Manifest"
COMMIT_MODE_ANCHOR_MARKER = "Commit Mode And Base-Anchor Lifecycle"
EXPORT_SURFACE_DECISION_MARKER = "Export Surface Decision"
NEXT_TRANCHE_AUDIT_MINI_PACKAGE_MARKER = "Next-Tranche Audit Mini-Package"
DISPATCH_PACKET_LEARNING_MARKER = "Dispatch Packet Authoring Learning Promotion"
NEGATIVE_SEARCH_COLLISION_MARKER = "Negative Search And Collision Discipline"
SINGLE_AGENT_MULTI_ROLE_MARKER = "Single-Agent Multi-Role Control Block"
INTAKE_ROLE_ROUTING_MARKER = "Intake Role Routing Decision"
EVIDENCE_REUSE_ENCODING_PLAN_MARKER = "Evidence Reuse And Encoding Plan"
REQUIRED_PROOF_ATOMIC_LITERAL_MARKER = "Required Proof Manifest Atomic Literal Discipline"
EVIDENCE_REUSE_ENCODING_STANDARD_PATH = (
    "docs/reference/CVF_PRIOR_VERIFICATION_REUSE_AND_UNICODE_EVIDENCE_HANDLING_STANDARD_2026-06-11.md"
)
ALLOWED_COMMIT_MODES = {
    "WORKER_MAY_COMMIT",
    "WORKER_MUST_NOT_COMMIT",
}
ALLOWED_SOURCE_VERIFICATION_DISPOSITIONS = {
    "ACCEPT",
    "REJECT",
    "BLOCKED_SOURCE_NOT_FOUND",
}
DEFERRED_SOURCE_VERIFICATION_RE = re.compile(
    r"\b("
    r"ACCEPT_PENDING_WORKER|PENDING_WORKER|UNVERIFIED|TBD|TODO|"
    r"confirm later|confirm field name|verify during implementation|"
    r"worker to verify|to be confirmed|inferred|stale-memory|placeholder|assume"
    r")\b",
    re.IGNORECASE,
)
PENDING_DEPENDENCY_LANGUAGE_RE = re.compile(
    r"\bCLOSED_PASS(?:_BOUNDED)?\b[\s\S]{0,180}\b("
    r"pending|required before|must be reviewer-committed before|"
    r"reviewer commit required|before\s+(?:worker\s+)?execution|"
    r"pending implementation|pending reviewer commit"
    r")\b"
    r"|"
    r"\b("
    r"pending|required before|must be reviewer-committed before|"
    r"reviewer commit required|before\s+(?:worker\s+)?execution|"
    r"pending implementation|pending reviewer commit"
    r")\b[\s\S]{0,180}\bCLOSED_PASS(?:_BOUNDED)?\b",
    re.IGNORECASE,
)
NEGATIVE_SEARCH_CLAIM_RE = re.compile(
    r"\bNOT\s+FOUND\b|\bBLOCKED_SOURCE_NOT_FOUND\b",
    re.IGNORECASE,
)
NEGATIVE_SEARCH_TOKEN_STOPWORDS = {
    "ACCEPT",
    "BLOCKED_SOURCE_NOT_FOUND",
    "CLOSED_PASS",
    "CLOSED_PASS_BOUNDED",
    "DISPATCHED",
    "DISPATCH_READY",
    "DOCS",
    "DOCUMENTATION",
    "EXTENSIONS",
    "EXTERNAL",
    "FOUND",
    "GOVERNANCE",
    "HOLD",
    "JSON",
    "NOT",
    "READY",
    "REJECT",
    "SOURCE",
    "SOURCES",
    "TEST",
    "TESTS",
}
VERIFIED_LINE_RE = re.compile(r"\bline\s+(\d+)\b", re.IGNORECASE)
IMPLEMENTATION_ROLE_TOKENS = {"worker", "implementer", "executor", "builder", "coder"}
REVIEW_ROLE_TOKENS = {"reviewer", "committer", "closer", "auditor"}
ORCHESTRATION_ROLE_TOKENS = {"orchestrator", "planner", "dispatcher"}
ROLE_ROUTING_MODES = {
    "SINGLE_AGENT_SINGLE_ROLE",
    "SINGLE_AGENT_MULTI_ROLE",
    "MULTI_AGENT_MULTI_ROLE",
    "MULTI_AGENT_SINGLE_ROLE",
}
EVIDENCE_REUSE_VERIFICATION_MODES = {
    "REUSE_PRIOR_VERIFICATION",
    "RECOMPUTE_REQUIRED",
    "REVIEWER_RECOMPUTE_ONLY",
}
PENDING_ROLE_ROUTING_MODES = {
    "HOLD_PENDING_OPERATOR_DECISION",
    "BLOCKED_PENDING_OPERATOR_DECISION",
    "PARKED_PENDING_OPERATOR_DECISION",
}

REQUIRED_SOURCE_COLUMNS = (
    "Claimed item",
    "Source file",
    "Verified line/section",
    "Verified path or symbol",
    "Owning interface/function/schema",
    "Disposition",
)

PATH_RE = re.compile(
    r"`((?:docs|governance|EXTENSIONS|CVF_SESSION|scripts|sdk|\.github|\.private_reference)/[^`|)]+)`"
    r"|((?:docs|governance|EXTENSIONS|CVF_SESSION|scripts|sdk|\.github|\.private_reference)/[^`\s|)]+)"
)
ROOT_GOVERNANCE_PATH_RE = re.compile(
    r"`((?:AGENTS\.md|CLAUDE\.md|README\.md|\.gitignore|CVF_SESSION_MEMORY\.md|AGENT_HANDOFF[^`|)]+\.md))`"
    r"|(?<![A-Za-z0-9_./])((?:AGENTS\.md|CLAUDE\.md|README\.md|\.gitignore|CVF_SESSION_MEMORY\.md|AGENT_HANDOFF[A-Za-z0-9_.-]*\.md))(?![A-Za-z0-9_./])"
)
LHW_RE = re.compile(r"LHW[-_]?(\d+)(?!\d)", re.IGNORECASE)
IMPORTANT_FULL_SCAN_AUDIT_PATH = "docs/audits/CVF_IMPORTANT_FULL_FILE_SCAN_BLINDSPOT_RECORD_2026-05-31.md"


def _run_git(args: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def _ref_exists(ref: str) -> bool:
    code, _, _ = _run_git(["rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}"])
    return code == 0


def _discover_default_base(head: str) -> tuple[str, str]:
    env_base = os.getenv("CVF_COMPAT_BASE")
    if env_base:
        return env_base, "env:CVF_COMPAT_BASE"
    for ref in DEFAULT_BASE_CANDIDATES:
        if not _ref_exists(ref):
            continue
        code, out, _ = _run_git(["merge-base", ref, head])
        if code == 0 and out:
            return out, f"merge-base({ref},{head})"
    return "HEAD~1", "fallback:HEAD~1"


def _resolve_range(base: str | None, head: str | None) -> tuple[str, str, str]:
    resolved_head = head or "HEAD"
    if base:
        return base, resolved_head, "explicit:--base"
    resolved_base, source = _discover_default_base(resolved_head)
    return resolved_base, resolved_head, source


def _parse_name_status(output: str) -> dict[str, set[str]]:
    changed: dict[str, set[str]] = {}
    for raw_line in output.splitlines():
        parts = raw_line.split("\t")
        if len(parts) < 2:
            continue
        status = parts[0].strip()
        path = parts[2] if (status.startswith("R") or status.startswith("C")) and len(parts) > 2 else parts[1]
        normalized = path.replace("\\", "/").strip()
        changed.setdefault(normalized, set()).add(status)
    return changed


def _get_changed(base: str, head: str) -> dict[str, set[str]]:
    changed: dict[str, set[str]] = {}
    code, out, err = _run_git(["diff", "--name-status", f"{base}..{head}"])
    if code != 0:
        raise RuntimeError(f"git diff failed for range {base}..{head}: {err or out}")
    for path, statuses in _parse_name_status(out).items():
        changed.setdefault(path, set()).update(statuses)
    for args in (["diff", "--name-status"], ["diff", "--name-status", "--cached"]):
        code, out, _ = _run_git(args)
        if code == 0 and out:
            for path, statuses in _parse_name_status(out).items():
                changed.setdefault(path, set()).update(statuses)
    code, out, _ = _run_git(["ls-files", "--others", "--exclude-standard"])
    if code == 0 and out:
        for raw_line in out.splitlines():
            normalized = raw_line.replace("\\", "/").strip()
            if normalized:
                changed.setdefault(normalized, set()).add("A")
    return changed


def _read_rel(path: str) -> str:
    full = REPO_ROOT / path
    if not full.exists() or full.is_dir():
        return ""
    return full.read_text(encoding="utf-8")


def _read_rel_at(ref: str, path: str) -> str:
    normalized = path.replace("\\", "/")
    code, out, _ = _run_git(["show", f"{ref}:{normalized}"])
    return out if code == 0 else ""


def _exists_rel(path: str) -> bool:
    normalized = path.strip().strip("`").replace("\\", "/").rstrip(".,;:")
    return bool(normalized) and (REPO_ROOT / normalized).exists()


def _commit_contains_path(ref: str, path: str) -> bool:
    normalized = path.strip().strip("`").replace("\\", "/").rstrip(".,;:")
    if not normalized:
        return False
    code, _, _ = _run_git(["cat-file", "-e", f"{ref}:{normalized}"])
    return code == 0


def _extract_status(text: str) -> str:
    match = re.search(r"^Status:\s*(.+?)\s*$", text, re.MULTILINE | re.IGNORECASE)
    return match.group(1).strip() if match else ""


def _is_dispatch_status(status: str) -> bool:
    normalized = status.upper()
    return "DISPATCHED" in normalized or "READY" in normalized or "CLOSED" in normalized


def _is_hold_status(status: str) -> bool:
    return "HOLD" in status.upper() or "PROPOSED" in status.upper() or "DRAFT" in status.upper()


def _is_closed_status(status: str) -> bool:
    normalized = status.strip().upper()
    return re.match(r"^CLOSED(?:\b|_)", normalized) is not None


def _validate_status_token_hygiene(text: str, artifact_label: str) -> list[str]:
    status = _extract_status(text)
    normalized = status.upper()
    if _is_hold_status(status) and re.search(r"(?:^|_)CLOSED(?:\b|_)", normalized):
        return [
            f"{artifact_label} hold/draft/proposed status must not contain `CLOSED`; "
            "use PASS or SATISFIED wording for prerequisite status tokens"
        ]
    return []


def _validate_closed_artifact_finality(text: str, artifact_label: str) -> list[str]:
    issues: list[str] = []
    status = _extract_status(text)
    if not _is_closed_status(status):
        return issues
    open_rows = re.findall(r"(?m)^\|.*\|\s*OPEN\s*\|\s*$", text)
    if open_rows:
        issues.append(
            f"closed {artifact_label} contains {len(open_rows)} table row(s) still marked OPEN"
        )
    unchecked_items = re.findall(r"(?m)^\s*[-*]\s+\[\s\]\s+", text)
    if unchecked_items:
        issues.append(
            f"closed {artifact_label} contains {len(unchecked_items)} unchecked checklist item(s)"
        )
    stale_resolution_rows = re.findall(
        r"(?im)^\|.*\|\s*(?:HOLD(?:_[A-Z0-9_]+)?|PENDING(?:_[A-Z0-9_]+)?|READY_FOR_DISPATCH)\s*\|\s*$",
        text,
    )
    if stale_resolution_rows:
        issues.append(
            f"closed {artifact_label} contains {len(stale_resolution_rows)} table row(s) "
            "still marked HOLD/PENDING/READY_FOR_DISPATCH"
        )
    if artifact_label == "work order":
        stale_work_order_phrases = sorted(
            {
                match.group(0)
                for pattern in (
                    r"\bremains\s+on\s+HOLD\b",
                    r"\bwhile\s+on\s+HOLD\b",
                    r"\bnot\s+ready\s+for\s+worker\s+execution\b",
                    r"\bnot\s+dispatch(?:ed|able)?\b",
                )
                for match in re.finditer(pattern, text, re.IGNORECASE)
            }
        )
        if stale_work_order_phrases:
            issues.append(
                "closed work order contains stale hold/dispatch-blocking prose: "
                + ", ".join(stale_work_order_phrases)
            )
    return issues


def _validate_closed_roadmap_status_residue(text: str) -> list[str]:
    issues: list[str] = []
    status = _extract_status(text)
    if not _is_closed_status(status):
        return issues
    residue_patterns = (
        r"\bWORK_ORDER_READY\b",
        r"\bREADY_FOR_IMPLEMENTATION\b",
        r"\bHOLD_UNTIL_[A-Z0-9_]+\b",
        r"\bHOLD\s+until\b",
    )
    residues = sorted(
        {
            match.group(0)
            for pattern in residue_patterns
            for match in re.finditer(pattern, text, re.IGNORECASE)
        }
    )
    if residues:
        issues.append(
            "closed roadmap contains stale dispatch/hold status residue: "
            + ", ".join(residues)
        )
    return issues


def _validate_mandatory_remediation_escalation(text: str, artifact_label: str) -> list[str]:
    issues: list[str] = []
    context = (
        r"guard|gate|autorun|pre-dispatch|pre-implementation|pre-closure|pre-push|"
        r"check_work_order_dispatch_quality|check_active_session_state|"
        r"Source Verification|closure residue|allowed scope|Finding-To-Governance|"
        r"N/A with reason|runtime/provider/cost"
    )
    preference = (
        r"do you want|would you like|should I|may I|operator checkpoint|"
        r"operator approval|ask(?:ed)? operator|waiting for operator|pending operator|"
        r"bạn muốn|ban muon|có muốn|co muon|tôi có nên|toi co nen|"
        r"chờ operator|cho operator"
    )
    repair = (
        r"fix|repair|correct|resolve|rerun|re-run|add|update|adjust|clean|"
        r"sửa|sua|chỉnh|chinh|thêm|them|chạy lại|chay lai"
    )
    patterns = (
        rf"(?is)\b(?:{preference})\b[\s\S]{{0,220}}\b(?:{repair})\b[\s\S]{{0,220}}\b(?:{context})\b",
        rf"(?is)\b(?:{context})\b[\s\S]{{0,220}}\b(?:{preference})\b[\s\S]{{0,220}}\b(?:{repair})\b",
        rf"(?is)\b(?:{repair})\b[\s\S]{{0,220}}\b(?:{context})\b[\s\S]{{0,220}}\b(?:{preference})\b",
    )
    for pattern in patterns:
        if re.search(pattern, text):
            issues.append(
                f"{artifact_label} treats mandatory allowed-scope gate remediation as an operator preference; "
                "repair machine-gate failures inside Allowed scope instead of asking the operator"
            )
            break
    return issues


def _validate_fast_lane_status_consistency(text: str) -> list[str]:
    issues: list[str] = []
    status = _extract_status(text).upper()
    if status in {"ACTIVE", "DRAFT", "HOLD"} and re.search(
        r"(?im)^\s*(?:\*\*)?(?:Disposition|Decision|Position)\s*(?:\*\*)?\s*:\s*(?:\*\*)?(?:FAST_LANE_PASS|PASS|APPROVE|ACCEPT)",
        text,
    ):
        issues.append(
            "fast-lane audit status is still ACTIVE/DRAFT/HOLD while disposition or decision is pass/approve"
        )
    return issues


def _extract_wave_id(path: str, text: str) -> int | None:
    # Wave ID must come from the filename, not the body — roadmaps that merely
    # reference LHW waves in their prose must not be mis-classified as LHW connector
    # waves. Only the file path is authoritative for wave identity.
    match = LHW_RE.search(path)
    return int(match.group(1)) if match else None


def _extract_wave_ids_from_path(path: str) -> set[int]:
    return {int(match.group(1)) for match in LHW_RE.finditer(path)}


def _is_connector_wave(path: str, text: str) -> bool:
    wave_id = _extract_wave_id(path, text)
    return wave_id is not None and wave_id >= 6


def _has_gc018_for_wave(wave_id: int) -> bool:
    baseline_root = REPO_ROOT / "docs" / "baselines"
    if not baseline_root.exists():
        return False
    wave = f"LHW{wave_id}".upper()
    for path in baseline_root.rglob("*.md"):
        name = path.name.upper()
        if wave in name and re.search(r"GC[-_]?018", name):
            return True
    return False


def _extract_paths(text: str) -> list[str]:
    paths = []
    for path_pattern in (PATH_RE, ROOT_GOVERNANCE_PATH_RE):
        for match in path_pattern.finditer(text):
            path = (match.group(1) or match.group(2)).replace("\\", "/").rstrip(".,;:")
            if "*" in path or "<" in path or ">" in path:
                continue
            paths.append(path)
    return paths


def _extract_section(text: str, heading_fragment: str) -> str:
    pattern = re.compile(
        rf"^##\s+.*{re.escape(heading_fragment)}.*$([\s\S]*?)(?=^##\s+|\Z)",
        re.MULTILINE | re.IGNORECASE,
    )
    match = pattern.search(text)
    return match.group(1) if match else ""


def _is_protected_authorization_path(path: str) -> bool:
    """Mirror check_core_guard_self_protection._is_protected.

    Protected = governance/compat/*.py checkers, CVF_SESSION/** JSON state,
    CVF_SESSION_MEMORY.md, and AGENT_HANDOFF*.md handoffs. Kept in sync with the
    core-guard self-protection gate so dispatch and closure agree on what
    requires a Core Guard Self-Protection Authorization carrier.
    """
    normalized = path.replace("\\", "/").strip()
    if normalized in {"CVF_SESSION_MEMORY.md"}:
        return True
    if re.match(r"^AGENT_HANDOFF[^/]*\.md$", normalized):
        return True
    if normalized.startswith("governance/compat/") and normalized.endswith(".py"):
        return True
    if normalized.startswith("CVF_SESSION/") and normalized.endswith(".json"):
        return True
    return False


def _validate_protected_path_authorization_carrier(text: str) -> list[str]:
    """Require a Core Guard Self-Protection Authorization carrier when a work
    order authorizes the worker to create or modify a protected path.

    Closes the DIR-T1 ORCHESTRATOR_PACKET_GAP learning: authorizing a
    governance/compat checker or CVF_SESSION/handoff file in scope without the
    authorization carrier forces the worker to synthesize one mid-task. The
    required tokens match check_core_guard_self_protection so dispatch and the
    closure-time core-guard gate share one vocabulary.
    """
    issues: list[str] = []
    scope_text = "\n".join(
        [
            _extract_allowed_scope_text(text),
            _extract_section(text, "Allowed Implementation Scope"),
            _extract_section(text, "New Files To Create"),
            _extract_section(text, "New Source And Test"),
            _extract_section(text, "Write Ownership"),
            _extract_section(text, "Authorized Artifact Set"),
        ]
    )
    forbidden_text = "\n".join(
        [
            _extract_forbidden_scope_text(text),
            _extract_section(text, "Forbidden Path Manifest"),
        ]
    )
    forbidden_paths = set(_extract_paths(forbidden_text))

    authorized_protected = sorted(
        {
            p
            for p in _extract_paths(scope_text)
            if _is_protected_authorization_path(p) and p not in forbidden_paths
        }
    )
    if not authorized_protected:
        return issues

    if "Core Guard Self-Protection Authorization" not in text:
        sample = ", ".join(authorized_protected[:5])
        issues.append(
            "work order authorizes protected path(s) "
            f"({sample}) without a `Core Guard Self-Protection Authorization` "
            "block; add the carrier per template section 7A"
        )
        return issues

    required_tokens = (
        "Authorized guard-maintenance scope",
        "Protected paths",
        "Operator authorization",
        "Rollback boundary",
    )
    missing = [token for token in required_tokens if token not in text]
    if missing:
        issues.append(
            "Core Guard Self-Protection Authorization block is missing required "
            f"field(s): {', '.join(missing)}"
        )

    carrier_section = _extract_section(text, "Core Guard Self-Protection Authorization")
    # Each authorized protected path must be named in the carrier's Protected
    # paths list.
    carrier_paths = set(_extract_paths(carrier_section))
    unlisted = [p for p in authorized_protected if p not in carrier_paths]
    if unlisted and "Protected paths" not in missing:
        sample = ", ".join(unlisted[:5])
        issues.append(
            "Core Guard Self-Protection Authorization `Protected paths` list does "
            f"not name every authorized protected path; missing: {sample}"
        )
    return issues


def _has_trace_matrix(text: str) -> bool:
    return re.search(r"Roadmap[- ]To[- ]Work[- ]Order Trace Matrix", text, re.IGNORECASE) is not None


def _has_worker_autonomy_clause(text: str) -> bool:
    return re.search(r"Worker Autonomy\s*/\s*No-Question Rule", text, re.IGNORECASE) is not None


def _validate_commit_mode_and_anchor_lifecycle(text: str) -> list[str]:
    issues: list[str] = []
    mode_match = re.search(
        r"(?im)^\s*(?:[-*]\s*)?Commit mode:\s*`?([A-Z_]+)`?\s*$",
        text,
    )
    if not mode_match:
        issues.append(
            "dispatch/ready work order lacks explicit `Commit mode: "
            "WORKER_MAY_COMMIT | WORKER_MUST_NOT_COMMIT`"
        )
    elif mode_match.group(1) not in ALLOWED_COMMIT_MODES:
        issues.append(
            "dispatch/ready work order has invalid commit mode "
            f"`{mode_match.group(1)}`; use WORKER_MAY_COMMIT or WORKER_MUST_NOT_COMMIT"
        )

    missing_anchors = [
        anchor
        for anchor in ("dispatchBaseHead", "executionBaseHead", "closureBaseHead")
        if anchor not in text
    ]
    if missing_anchors:
        issues.append(
            "dispatch/ready work order lacks base-anchor lifecycle marker(s): "
            + ", ".join(missing_anchors)
        )
    dispatch_base_match = re.search(
        r"(?im)^\s*(?:[-*]\s*)?dispatchBaseHead:\s*`?([^`\n]+?)`?\s*$",
        text,
    )
    if dispatch_base_match:
        dispatch_base = dispatch_base_match.group(1).strip()
        if not re.fullmatch(r"[0-9a-f]{6,40}", dispatch_base, re.IGNORECASE):
            issues.append(
                "dispatch/ready work order has non-commit `dispatchBaseHead`; "
                "the orchestrator must set a real git commit hash before dispatch"
            )
    return issues


def _is_worker_must_not_commit(text: str) -> bool:
    return (
        re.search(
            r"(?im)^\s*(?:[-*]\s*)?Commit mode:\s*`?WORKER_MUST_NOT_COMMIT`?\s*$",
            text,
        )
        is not None
    )


def _completion_review_assigned_to_worker(text: str) -> bool:
    for line in text.splitlines():
        if "completion review" not in line.lower():
            continue
        if re.search(r"\|\s*(?:Worker|Executor)\s*\|[^|\n]*completion review", line, re.IGNORECASE):
            return True
        if re.search(r"completion review[^|\n]*\|\s*(?:Worker|Executor)\s*\|", line, re.IGNORECASE):
            return True
        if re.search(
            r"\b(?:worker|executor)\b[^.\n|]*(?:create|author|produce|write|file)[^.\n|]*completion review",
            line,
            re.IGNORECASE,
        ):
            return True
    return False


def _validate_worker_completion_review_boundary(text: str) -> list[str]:
    if not _is_worker_must_not_commit(text):
        return []
    if not _completion_review_assigned_to_worker(text):
        return []
    return [
        "WORKER_MUST_NOT_COMMIT dispatch assigns completion review to Worker; "
        "use a worker handoff/evaluation artifact and reviewer-owned completion review, "
        "or explicitly change role/commit mode before dispatch"
    ]


def _validate_no_commit_reviewer_closure_contract(text: str) -> list[str]:
    if not _is_worker_must_not_commit(text):
        return []

    issues: list[str] = []
    if re.search(r"Reviewer Closure Conversion", text, re.IGNORECASE) is None:
        issues.append(
            "WORKER_MUST_NOT_COMMIT dispatch lacks Reviewer Closure Conversion block"
        )
    if "completionReviewPath" not in text:
        issues.append(
            "WORKER_MUST_NOT_COMMIT dispatch lacks `completionReviewPath` for reviewer-owned closure"
        )
    if "reviewerOwnedClosurePaths" not in text:
        issues.append(
            "WORKER_MUST_NOT_COMMIT dispatch lacks `reviewerOwnedClosurePaths` for closure scope"
        )
    if "_COMPLETION_" not in text:
        issues.append(
            "WORKER_MUST_NOT_COMMIT dispatch lacks conventional `_COMPLETION_` reviewer artifact path"
        )
    if re.search(
        r"ACTIVE_SESSION_STATE\.json[\s\S]{0,160}(?:closure invariant|final invariant|source invariant)",
        text,
        re.IGNORECASE,
    ):
        issues.append(
            "WORKER_MUST_NOT_COMMIT dispatch treats mutable ACTIVE_SESSION_STATE.json as a closure invariant; "
            "cite stable completion/review artifacts for predecessor closure facts"
        )
    return issues


def _is_roadmap_derived(text: str) -> bool:
    return "docs/roadmaps/" in text or "roadmap-derived" in text.lower() or "Roadmap requirement" in text


def _parse_markdown_tables(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if "|" not in line or "Claimed item" not in line or "Source file" not in line:
            index += 1
            continue
        headers = [cell.strip() for cell in line.strip().strip("|").split("|")]
        index += 1
        if index < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", lines[index]):
            index += 1
        while index < len(lines) and "|" in lines[index]:
            raw_cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
            is_source_verification_table = all(
                column in headers
                for column in (
                    "Claimed item",
                    "Source file",
                    "Verified line/section",
                    "Verified path or symbol",
                    "Disposition",
                )
            )
            if len(raw_cells) > len(headers) and is_source_verification_table and len(raw_cells) >= 6:
                raw_cells = [
                    raw_cells[0],
                    raw_cells[1],
                    raw_cells[2],
                    " | ".join(raw_cells[3 : len(raw_cells) - 2]),
                    raw_cells[-2],
                    raw_cells[-1],
                ]
            if len(raw_cells) >= len(headers):
                rows.append(dict(zip(headers, raw_cells)))
            index += 1
        continue
    return rows


def _parse_any_markdown_tables(text: str) -> list[list[dict[str, str]]]:
    tables: list[list[dict[str, str]]] = []
    lines = text.splitlines()
    index = 0
    while index + 1 < len(lines):
        header_line = lines[index].strip()
        separator_line = lines[index + 1].strip()
        if not header_line.startswith("|") or "|" not in header_line:
            index += 1
            continue
        if not re.match(r"^\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?$", separator_line):
            index += 1
            continue
        headers = [cell.strip() for cell in header_line.strip("|").split("|")]
        table_rows: list[dict[str, str]] = []
        index += 2
        while index < len(lines) and lines[index].strip().startswith("|"):
            cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
            if len(cells) < len(headers):
                cells.extend([""] * (len(headers) - len(cells)))
            table_rows.append(dict(zip(headers, cells[: len(headers)])))
            index += 1
        if table_rows:
            tables.append(table_rows)
    return tables


def _normalize_table_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def _row_value(row: dict[str, str], *names: str) -> str:
    normalized = {_normalize_table_key(key): value for key, value in row.items()}
    for name in names:
        value = normalized.get(_normalize_table_key(name))
        if value is not None:
            return value.strip()
    return ""


def _section_tables(text: str, heading_fragment: str) -> list[list[dict[str, str]]]:
    section = _extract_section(text, heading_fragment)
    return _parse_any_markdown_tables(section)


def _truthy_cell(value: str) -> bool:
    normalized = value.strip().strip("`").lower()
    return normalized in {"yes", "y", "true", "required", "must", "handoff"}


def _clean_manifest_path(value: str) -> str:
    return value.strip().strip("`").replace("\\", "/").rstrip(".,;:")


def _required_proof_literal_issue(raw_literal: str) -> str | None:
    raw = raw_literal.strip()
    if not raw:
        return None
    spans = re.findall(r"`([^`]+)`", raw)
    if len(spans) > 1:
        return (
            "Required Proof Manifest row has multiple required literals in one "
            "cell; split the proof into one row per literal"
        )
    stripped = raw.strip("`").strip()
    if re.search(r"`\s*(?:and|or|,|;)\s*`", raw, re.IGNORECASE):
        return (
            "Required Proof Manifest row has compound literal syntax; split the "
            "proof into one row per literal"
        )
    if re.search(r"\s+(?:and|or)\s+", stripped, re.IGNORECASE) and re.search(
        r"`|[A-Z0-9_]{4,}", stripped
    ):
        return (
            "Required Proof Manifest literal appears compound; use an atomic "
            "literal row or record an explicit N/A with reason"
        )
    return None


def _validate_required_proof_manifest_atomic_literals(text: str) -> list[str]:
    issues: list[str] = []
    for table in _section_tables(text, "Required Proof Manifest"):
        for row in table:
            required = _truthy_cell(_row_value(row, "Required at handoff", "Required", "Must exist"))
            if not required:
                continue
            raw_literal = _row_value(row, "Required literal", "Literal", "Required token")
            issue = _required_proof_literal_issue(raw_literal)
            if issue and issue not in issues:
                issues.append(issue)
    return issues


def _path_matches_pattern(path: str, pattern: str) -> bool:
    normalized = path.replace("\\", "/").strip()
    clean_pattern = _clean_manifest_path(pattern).rstrip("/")
    if not clean_pattern:
        return False
    if any(marker in clean_pattern for marker in ("*", "?", "[")):
        return fnmatch.fnmatch(normalized, clean_pattern)
    return normalized == clean_pattern or normalized.startswith(f"{clean_pattern}/")


def _source_table_has_required_columns(text: str) -> bool:
    tables = _parse_markdown_tables(text)
    if not tables:
        return False
    return all(column in tables[0] for column in REQUIRED_SOURCE_COLUMNS)


def _validate_source_verification_table_shape(text: str) -> list[str]:
    sections = [
        section
        for heading in ("Source Verification Block", "Source Verification Table")
        if (section := _extract_section(text, heading))
    ]
    issues: list[str] = []
    source_like_headers = {
        "claimeditem",
        "sourcefile",
        "verifiedlinesection",
        "verifiedpathorsymbol",
        "owninginterfacefunctionschema",
        "disposition",
        "symbolpath",
        "symbol",
        "path",
        "file",
        "verifiedline",
        "verifiedsection",
        "owner",
        "schema",
    }
    required_display = " | ".join(REQUIRED_SOURCE_COLUMNS)
    for section in sections:
        for table in _parse_any_markdown_tables(section):
            headers = set(table[0].keys()) if table else set()
            normalized_headers = {_normalize_table_key(header) for header in headers}
            if all(column in headers for column in REQUIRED_SOURCE_COLUMNS):
                continue
            if source_like_headers.intersection(normalized_headers):
                issues.append(
                    "Source Verification table uses noncanonical columns; "
                    f"required columns are: {required_display}"
                )
    return sorted(set(issues))


def _extract_declared_string_values(source_text: str, symbol: str) -> set[str]:
    symbol_name = re.sub(r"[^A-Za-z0-9_].*$", "", symbol.strip().strip("`"))
    if not symbol_name:
        return set()
    type_match = re.search(
        rf"(?:export\s+)?type\s+{re.escape(symbol_name)}\s*=\s*([\s\S]*?);",
        source_text,
    )
    if not type_match:
        return set()
    return set(re.findall(r"['\"]([^'\"]+)['\"]", type_match.group(1)))


def _row_literal_tokens(row: dict[str, str]) -> set[str]:
    joined = " | ".join(row.values())
    tokens = set(re.findall(r"`([^`]+)`", joined))
    tokens.update(re.findall(r"['\"]([^'\"]+)['\"]", joined))
    return {token for token in tokens if re.match(r"^[A-Za-z0-9_.:-]+$", token)}


def _symbol_field_name(symbol: str) -> str:
    cleaned = symbol.strip().strip("`")
    if _verified_symbol_contains_assignment(cleaned):
        return ""
    parts = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", cleaned)
    return parts[-1] if parts else ""


def _verified_symbol_contains_assignment(symbol: str) -> bool:
    cleaned = symbol.strip().strip("`")
    return re.search(
        r"\b[A-Za-z_][A-Za-z0-9_.]*\s*(?:=|:)\s*\S+",
        cleaned,
        re.IGNORECASE,
    ) is not None


def _claims_false_invariant(*cells: str) -> bool:
    joined = " ".join(cells)
    return re.search(r"[A-Za-z0-9_.]+\s*(?:=|:)\s*false\b", joined) is not None


def _source_has_literal_false(source_text: str, field_name: str) -> bool:
    if not field_name:
        return False
    return re.search(rf"\b{re.escape(field_name)}\s*:\s*false\b", source_text) is not None or re.search(
        rf"\b{re.escape(field_name)}\s*=\s*false\b",
        source_text,
    ) is not None


def _is_code_source(path: str) -> bool:
    return Path(path).suffix.lower() in {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".py"}


def _symbol_identifier_parts(symbol: str) -> list[str]:
    cleaned = symbol.strip().strip("`")
    if not cleaned or _verified_symbol_contains_assignment(cleaned):
        return []
    if re.search(r"[^A-Za-z0-9_.]", cleaned):
        return []
    return [part for part in cleaned.split(".") if re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", part)]


def _extract_ts_decl_block(source_text: str, owner: str) -> str | None:
    match = re.search(
        rf"(?m)^\s*(?:export\s+)?(?:interface|class|type)\s+{re.escape(owner)}\b[^\n]*",
        source_text,
    )
    if not match:
        return None
    start = match.start()
    brace_start = source_text.find("{", match.end())
    if brace_start == -1:
        next_decl = re.search(
            r"(?m)^\s*(?:export\s+)?(?:interface|class|type|function|const)\s+",
            source_text[match.end():],
        )
        end = match.end() + next_decl.start() if next_decl else len(source_text)
        return source_text[start:end]
    depth = 0
    for index in range(brace_start, len(source_text)):
        char = source_text[index]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return source_text[start:index + 1]
    return source_text[start:]


def _source_has_verified_symbol(source_text: str, symbol: str) -> bool:
    parts = _symbol_identifier_parts(symbol)
    if not parts:
        return True
    if len(parts) >= 2:
        owner, leaf = parts[-2], parts[-1]
        owner_block = _extract_ts_decl_block(source_text, owner)
        if owner_block is not None:
            return re.search(rf"\b{re.escape(leaf)}\b", owner_block) is not None
        return False
    return re.search(rf"\b{re.escape(parts[0])}\b", source_text) is not None


def _extract_verified_line_number(value: str) -> int | None:
    match = VERIFIED_LINE_RE.search(value)
    if not match:
        return None
    try:
        return int(match.group(1))
    except ValueError:
        return None


def _symbol_definition_line(source_path: str, source_text: str, symbol: str) -> int | None:
    parts = _symbol_identifier_parts(symbol)
    if not parts:
        return None
    name = parts[-1]
    suffix = Path(source_path).suffix.lower()
    if suffix == ".py":
        pattern = re.compile(
            rf"^\s*(?:async\s+def|def|class)\s+{re.escape(name)}\b",
            re.MULTILINE,
        )
    elif suffix in {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs"}:
        pattern = re.compile(
            rf"^\s*(?:export\s+)?(?:default\s+)?(?:(?:async\s+)?function|class|interface|type|const|let|var)\s+{re.escape(name)}\b",
            re.MULTILINE,
        )
    else:
        return None
    match = pattern.search(source_text)
    if not match:
        return None
    return source_text.count("\n", 0, match.start()) + 1


def _validate_verified_line_anchor(source_path: str, source_text: str, row: dict[str, str]) -> str | None:
    cited_line = _extract_verified_line_number(row.get("Verified line/section", ""))
    if cited_line is None:
        return None
    symbol = row.get("Verified path or symbol", "").strip().strip("`")
    definition_line = _symbol_definition_line(source_path, source_text, symbol)
    if definition_line is None or cited_line == definition_line:
        return None
    return (
        "Source Verification ACCEPT row cites "
        f"`{symbol}` at line {cited_line}, but `{source_path}` defines it at line {definition_line}; "
        "cite the symbol definition line, not a continuation or interior signature line"
    )


def _validate_false_invariant_against_source(
    source_path: str,
    source_text: str,
    row: dict[str, str],
) -> str | None:
    claimed = row.get("Claimed item", "")
    verified_symbol = row.get("Verified path or symbol", "")
    owner = row.get("Owning interface/function/schema", "")
    if not _claims_false_invariant(claimed, verified_symbol, owner):
        return None
    field_name = _symbol_field_name(verified_symbol or claimed)
    if _source_has_literal_false(source_text, field_name):
        return None
    return (
        "Source Verification ACCEPT row claims a false invariant for "
        f"`{field_name or verified_symbol.strip().strip('`')}` but `{source_path}` "
        "does not declare or assign that field as literal false"
    )


def _source_rows_for_symbol(rows: list[dict[str, str]]) -> list[tuple[str, str, str, str]]:
    refs: list[tuple[str, str, str, str]] = []
    for row in rows:
        if "ACCEPT" not in row.get("Disposition", "").upper():
            continue
        source_paths = _extract_paths(row.get("Source file", ""))
        if not source_paths:
            continue
        symbol = row.get("Verified path or symbol", "")
        if _verified_symbol_contains_assignment(symbol):
            continue
        owner = row.get("Owning interface/function/schema", "")
        field_name = _symbol_field_name(symbol or row.get("Claimed item", ""))
        if not field_name:
            continue
        for source_path in source_paths:
            refs.append((field_name, symbol, owner, source_path))
    return refs


def _non_table_blocks(text: str) -> list[str]:
    blocks: list[str] = []
    current: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            if current:
                blocks.append(" ".join(current))
                current = []
            continue
        if re.match(r"^(?:[-*]\s+|\d+\.\s+)", stripped) and current:
            blocks.append(" ".join(current))
            current = []
        if not stripped:
            if current:
                blocks.append(" ".join(current))
                current = []
            continue
        current.append(stripped)
    if current:
        blocks.append(" ".join(current))
    return blocks


def _validate_false_invariant_prose(text: str, rows: list[dict[str, str]]) -> list[str]:
    issues: list[str] = []
    blocks = _non_table_blocks(text)
    for field_name, symbol, owner, source_path in _source_rows_for_symbol(rows):
        source_text = _read_rel(source_path)
        if not source_text or _source_has_literal_false(source_text, field_name):
            continue
        owner_tokens = {token for token in (owner.strip("`"),) if token}
        symbol_parts = symbol.replace("`", "").split(".")
        if len(symbol_parts) > 1:
            owner_tokens.add(".".join(symbol_parts[:-1]))
            owner_tokens.update(part for part in symbol_parts[:-1] if part)
        owner_tokens.update(token for token in owner.replace("`", "").split(".") if token)
        for block in blocks:
            if not re.search(rf"`?{re.escape(field_name)}`?\s*(?:=|:)\s*false\b", block):
                continue
            if not any(token and token in block for token in owner_tokens):
                continue
            if re.search(
                r"connector-normalized|normalizes|normalise|advisory\s+packet\s+requires|connector\s+requires",
                block,
                re.IGNORECASE,
            ):
                continue
            issues.append(
                "Prose claims a false invariant for "
                f"`{field_name}` from `{owner.strip('`') or symbol.strip('`')}` but `{source_path}` "
                "does not declare or assign that field as literal false"
            )
            break
    return issues


def _validate_known_false_invariant_claims(text: str) -> list[str]:
    issues: list[str] = []
    for block in _non_table_blocks(text):
        if not re.search(r"\bMemoryGatewayDecision\b", block):
            continue
        if not re.search(r"\bcanReinject`?\s*(?:=|:)\s*false\b", block):
            continue
        if re.search(
            r"connector-normalized|not\s+source[- ](?:proof|verified)|not\s+source-claimed|boolean\s+field",
            block,
            re.IGNORECASE,
        ):
            continue
        issues.append(
            "Prose claims `MemoryGatewayDecision.canReinject=false`; the known source contract "
            "declares `canReinject` as a boolean unless a cited source proves a literal false assignment"
        )
        break
    return issues


def _is_future_work_order_output_reference(text: str, work_order_path: str) -> bool:
    for line in text.splitlines():
        if work_order_path not in line:
            continue
        lowered = line.lower()
        has_future_context = any(
            marker in lowered
            for marker in (
                "future",
                "hold",
                "dependency-gated",
                "dependency gated",
                "pending dependency-release",
                "pending dependency release",
                "next dispatch candidate",
            )
        )
        has_output_context = any(
            marker in lowered
            for marker in ("output", "authored", "created", "dispatch packet", "work order exists")
        )
        if has_future_context and has_output_context:
            return True
    return False


def _validate_referenced_work_order_closure(text: str, artifact_label: str) -> list[str]:
    if not _is_closed_status(_extract_status(text)):
        return []
    issues: list[str] = []
    for work_order_path in sorted(
        {
            path
            for path in _extract_paths(text)
            if path.replace("\\", "/").startswith("docs/work_orders/")
        }
    ):
        work_order_text = _read_rel(work_order_path)
        if not work_order_text:
            issues.append(f"closed {artifact_label} cites missing work order `{work_order_path}`")
            continue
        if not _is_closed_status(_extract_status(work_order_text)):
            if _is_future_work_order_output_reference(text, work_order_path):
                continue
            issues.append(
                f"closed {artifact_label} cites work order `{work_order_path}` whose status is not CLOSED"
            )
            continue
        work_order_finality = _validate_closed_artifact_finality(work_order_text, "work order")
        if work_order_finality:
            issues.append(
                f"closed {artifact_label} cites work order `{work_order_path}` with unresolved closure residue"
            )
    return issues


def _row_has_blocking_disposition(row: dict[str, str]) -> bool:
    disposition = row.get("Disposition", "").upper()
    return "BLOCKED_SOURCE_NOT_FOUND" in disposition or disposition == "BLOCKED"


def _validate_ready_source_blockers(text: str) -> list[str]:
    rows = _parse_markdown_tables(text)
    blocked = [row for row in rows if _row_has_blocking_disposition(row)]
    if not blocked:
        return []
    return [
        "dispatch/ready work order contains blocking Source Verification disposition; "
        "use HOLD/DRAFT until source facts are resolved"
    ]


def _validate_source_verification_disposition_discipline(text: str) -> list[str]:
    issues: list[str] = []
    for row in _parse_markdown_tables(text):
        raw_disposition = row.get("Disposition", "").strip().strip("`")
        disposition = raw_disposition.upper()
        if disposition and disposition not in ALLOWED_SOURCE_VERIFICATION_DISPOSITIONS:
            issues.append(
                "Source Verification disposition must be one of ACCEPT, REJECT, "
                f"or BLOCKED_SOURCE_NOT_FOUND; found `{raw_disposition}`"
            )
        joined = " ".join(row.values())
        if DEFERRED_SOURCE_VERIFICATION_RE.search(joined):
            issues.append(
                "Source Verification row defers source facts to worker/future verification; "
                "resolve before dispatch or set BLOCKED_SOURCE_NOT_FOUND"
            )
    return sorted(set(issues))


def _negative_search_evidence_section(text: str) -> str:
    for heading_fragment in (
        NEGATIVE_SEARCH_COLLISION_MARKER,
        "Negative Search Evidence",
        "Negative Search",
    ):
        section = _extract_section(text, heading_fragment)
        if section:
            return section
    return ""


def _extract_negative_search_tokens(text: str) -> set[str]:
    tokens: set[str] = set()
    for match in NEGATIVE_SEARCH_CLAIM_RE.finditer(text):
        window = text[max(0, match.start() - 220) : min(len(text), match.end() + 220)]
        tokens.update(re.findall(r"`([A-Za-z_][A-Za-z0-9_.:-]{2,})`", window))
        tokens.update(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*[A-Z][A-Za-z0-9_]*\b", window))
        tokens.update(re.findall(r"\b[A-Z][A-Z0-9_]{3,}\b", window))
    cleaned: set[str] = set()
    for token in tokens:
        stripped = token.strip().strip("`")
        if stripped.upper() in NEGATIVE_SEARCH_TOKEN_STOPWORDS:
            continue
        if "/" in stripped or "\\" in stripped:
            continue
        if re.match(r"^[0-9a-f]{6,40}$", stripped, re.IGNORECASE):
            continue
        cleaned.add(stripped)
    return cleaned


def _token_occurs_elsewhere(token: str, current_path: str) -> bool:
    code, out, _ = _run_git(["grep", "-Il", "--", token])
    if code == 0 and out:
        return any(line.strip().replace("\\", "/") != current_path for line in out.splitlines())
    if code in {1, 0}:
        return False

    skip_dirs = {".git", ".hg", ".svn", "node_modules", ".next", "__pycache__", ".venv", "venv"}
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(REPO_ROOT).as_posix()
        if rel == current_path:
            continue
        if any(part in skip_dirs for part in path.parts):
            continue
        try:
            if token in path.read_text(encoding="utf-8", errors="ignore"):
                return True
        except OSError:
            continue
    return False


def _collision_disposition_records_token(section: str, token: str) -> bool:
    for line in section.splitlines():
        if token not in line:
            continue
        if not re.search(
            r"collision|same-token|non-authoritative|different meaning|occurrence",
            line,
            re.IGNORECASE,
        ):
            continue
        if re.search(r"\b(?:none|no|zero|0)\b", line, re.IGNORECASE):
            return False
        return True
    return False


def _validate_negative_search_collision_discipline(
    path: str,
    text: str,
    artifact_label: str,
) -> list[str]:
    if not NEGATIVE_SEARCH_CLAIM_RE.search(text):
        return []

    issues: list[str] = []
    section = _negative_search_evidence_section(text)
    if not section:
        return [
            f"{artifact_label} contains `NOT FOUND` or `BLOCKED_SOURCE_NOT_FOUND` "
            f"but lacks `## {NEGATIVE_SEARCH_COLLISION_MARKER}` evidence"
        ]

    required_patterns = {
        "exact search roots": r"search roots?|roots?",
        "exact search command or query": r"search command|structured query|query",
        "coverage across source/tests/docs/JSON/external evidence": r"coverage|source|tests|docs|json|external",
        "same-token collision result": r"collision|same-token|non-authoritative|different meaning|occurrence",
        "absent-versus-collision disposition": r"disposition|absent|not binding|binding",
    }
    for label, pattern in required_patterns.items():
        if not re.search(pattern, section, re.IGNORECASE):
            issues.append(
                f"{artifact_label} negative-search evidence is missing {label}"
            )

    for token in sorted(_extract_negative_search_tokens(text)):
        if not _token_occurs_elsewhere(token, path):
            continue
        if _collision_disposition_records_token(section, token):
            continue
        issues.append(
            f"{artifact_label} claims `{token}` as not found while the same token "
            "appears elsewhere in the repo; record the collision/non-authoritative "
            "occurrence instead of a bare `NOT FOUND` claim"
        )
    return sorted(set(issues))


def _normalize_role_cell(value: str) -> str:
    cleaned = re.sub(r"`([^`]+)`", r"\1", value)
    cleaned = re.sub(r"[^A-Za-z0-9_./ -]+", " ", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip().lower()


def _role_bucket(role_cell: str) -> set[str]:
    normalized = _normalize_role_cell(role_cell)
    buckets: set[str] = set()
    if any(token in normalized for token in IMPLEMENTATION_ROLE_TOKENS):
        buckets.add("implementation")
    if any(token in normalized for token in REVIEW_ROLE_TOKENS):
        buckets.add("review")
    if any(token in normalized for token in ORCHESTRATION_ROLE_TOKENS):
        buckets.add("orchestration")
    return buckets


def _single_agent_multi_role_phrase_present(text: str) -> bool:
    return re.search(
        r"\b(single[-_ ]agent[-_ ]multi[-_ ]role|SINGLE_AGENT_MULTI_ROLE|one\s+agent\s+multiple\s+roles|"
        r"same\s+agent\s+(?:owns|performs|executes)[\s\S]{0,80}(?:worker|implementer|reviewer|committer)|"
        r"Codex\s+multi[- ]role|Claude\s+multi[- ]role|self[- ]review)\b",
        text,
        re.IGNORECASE,
    ) is not None


def _role_tables_imply_single_agent_multi_role(text: str) -> bool:
    for table in _parse_any_markdown_tables(text):
        owner_roles: dict[str, set[str]] = {}
        for row in table:
            role = _row_value(row, "Role", "Lane")
            owner = _row_value(row, "Owner", "Agent", "Actor", "Assignee")
            if not role or not owner:
                continue
            normalized_owner = _normalize_role_cell(owner)
            if not normalized_owner or normalized_owner in {"n/a", "na", "none", "operator"}:
                continue
            owner_roles.setdefault(normalized_owner, set()).update(_role_bucket(role))
        for buckets in owner_roles.values():
            if "implementation" in buckets and "review" in buckets:
                return True
            if {"orchestration", "implementation", "review"}.issubset(buckets):
                return True
    return False


def _needs_single_agent_multi_role_control(text: str) -> bool:
    return _single_agent_multi_role_phrase_present(text) or _role_tables_imply_single_agent_multi_role(text)


def _validate_single_agent_multi_role_control(text: str, artifact_label: str) -> list[str]:
    if not _needs_single_agent_multi_role_control(text):
        return []

    section = _extract_section(text, SINGLE_AGENT_MULTI_ROLE_MARKER)
    if not section:
        return [
            f"{artifact_label} uses single-agent multi-role execution but lacks "
            f"`## {SINGLE_AGENT_MULTI_ROLE_MARKER}`"
        ]

    required_patterns = {
        "role separation ledger": r"role separation|role ledger|role-by-role",
        "evidence basis independent of memory": r"evidence basis|diff|source|gate|test",
        "self-review boundary": r"self-review|not independent|independent review not claimed|no independent review",
        "escalation conditions": r"escalation|operator|external reviewer|stop condition",
        "gate sequence": r"gate sequence|reviewer-fast|pre-dispatch|pre-implementation|pre-closure|pre-push",
    }
    issues: list[str] = []
    for label, pattern in required_patterns.items():
        if not re.search(pattern, section, re.IGNORECASE):
            issues.append(
                f"{artifact_label} single-agent multi-role control block is missing {label}"
            )
    return sorted(set(issues))


def _requires_evidence_reuse_and_encoding_plan(text: str) -> bool:
    lowered = text.lower()
    direct_markers = (
        "prior verification",
        "prior manifest",
        "t11b",
        "source bundle",
        "extracted text",
        "extracted-text",
        "unicode path",
        "unicode-path",
    )
    if any(marker in lowered for marker in direct_markers):
        return True
    return re.search(
        r"(?:consume|consumes|cite|cites|use|uses|read|reads|load|loads|relies\s+on|relies\s+upon)"
        r"[\s\S]{0,140}external evidence digest"
        r"|external evidence digest[\s\S]{0,140}"
        r"(?:consume|consumes|cite|cites|use|uses|read|reads|load|loads|input|source)",
        text,
        re.IGNORECASE,
    ) is not None


def _field_value_from_block(block: str, field_name: str) -> str:
    match = re.search(
        rf"(?im)^\s*(?:[-*]\s*)?{re.escape(field_name)}\s*:\s*`?([^`\n]+?)`?\s*$",
        block,
    )
    return match.group(1).strip() if match else ""


def _is_missing_or_na(value: str) -> bool:
    normalized = value.strip().strip("`").lower()
    return not normalized or normalized in {"n/a", "na", "n/a with reason", "none", "tbd", "todo"}


def _validate_evidence_reuse_and_encoding_plan(text: str) -> list[str]:
    if not _requires_evidence_reuse_and_encoding_plan(text):
        return []
    block = _extract_section(text, EVIDENCE_REUSE_ENCODING_PLAN_MARKER)
    if not block:
        return [
            "dispatch/ready work order cites prior verification, external evidence, "
            "source bundle, T11B, extracted text, or Unicode-path evidence but lacks "
            f"`## {EVIDENCE_REUSE_ENCODING_PLAN_MARKER}`"
        ]

    issues: list[str] = []
    mode_value = _field_value_from_block(block, "verificationMode").strip().strip("`")
    modes_in_block = {
        mode
        for mode in EVIDENCE_REUSE_VERIFICATION_MODES
        if re.search(rf"\b{re.escape(mode)}\b", block)
    }
    if not mode_value:
        issues.append(f"`## {EVIDENCE_REUSE_ENCODING_PLAN_MARKER}` lacks `verificationMode`")
    elif mode_value not in EVIDENCE_REUSE_VERIFICATION_MODES:
        issues.append(
            f"`verificationMode` must be one of {sorted(EVIDENCE_REUSE_VERIFICATION_MODES)}; "
            f"found `{mode_value}`"
        )
    if len(modes_in_block) > 1:
        issues.append(
            f"`## {EVIDENCE_REUSE_ENCODING_PLAN_MARKER}` records multiple verification modes: "
            + ", ".join(sorted(modes_in_block))
        )

    prior_artifact = _field_value_from_block(block, "priorVerificationArtifact")
    prior_anchor = _field_value_from_block(block, "priorVerificationAnchor")
    recompute_reason = _field_value_from_block(block, "recomputeReason")
    unicode_handling = _field_value_from_block(block, "unicodePathHandling")
    extracted_authority = _field_value_from_block(block, "extractedTextAuthority")
    fresh_recompute = _field_value_from_block(block, "freshRecomputeRequired")

    if mode_value == "REUSE_PRIOR_VERIFICATION":
        if _is_missing_or_na(prior_artifact):
            issues.append("`REUSE_PRIOR_VERIFICATION` requires `priorVerificationArtifact`")
        if _is_missing_or_na(prior_anchor):
            issues.append("`REUSE_PRIOR_VERIFICATION` requires `priorVerificationAnchor`")
        if fresh_recompute.strip().strip("`").upper() not in {"NO", "FALSE"}:
            issues.append("`REUSE_PRIOR_VERIFICATION` requires `freshRecomputeRequired: NO`")
    elif mode_value == "RECOMPUTE_REQUIRED":
        if _is_missing_or_na(recompute_reason):
            issues.append("`RECOMPUTE_REQUIRED` requires a concrete `recomputeReason`")
    elif mode_value == "REVIEWER_RECOMPUTE_ONLY":
        if _is_missing_or_na(prior_artifact):
            issues.append("`REVIEWER_RECOMPUTE_ONLY` requires `priorVerificationArtifact`")

    if re.search(r"unicode|extracted[- ]text", text, re.IGNORECASE):
        if _is_missing_or_na(unicode_handling):
            issues.append("Unicode or extracted-text evidence requires `unicodePathHandling`")
        elif not re.search(r"literal|utf-?8|utf8", unicode_handling, re.IGNORECASE):
            issues.append("`unicodePathHandling` must require literal paths or UTF-8-safe readers")
    if re.search(r"extracted[- ]text", text, re.IGNORECASE):
        normalized_authority = extracted_authority.strip().strip("`")
        if normalized_authority not in {"SOURCE_AUTHORITY", "AUXILIARY_ONLY", "N/A with reason"}:
            issues.append(
                "`extractedTextAuthority` must be SOURCE_AUTHORITY, AUXILIARY_ONLY, or N/A with reason"
            )

    return issues


def _extract_role_routing_modes(section: str) -> set[str]:
    upper_section = section.upper()
    return {
        mode
        for mode in ROLE_ROUTING_MODES | PENDING_ROLE_ROUTING_MODES
        if mode in upper_section
    }


def _validate_intake_role_routing_decision(text: str, artifact_label: str) -> list[str]:
    section = _extract_section(text, INTAKE_ROLE_ROUTING_MARKER)
    if not section:
        return [
            f"dispatch/ready {artifact_label} lacks `## {INTAKE_ROLE_ROUTING_MARKER}`"
        ]

    issues: list[str] = []
    modes = _extract_role_routing_modes(section)
    allowed_modes = modes & ROLE_ROUTING_MODES
    pending_modes = modes & PENDING_ROLE_ROUTING_MODES
    if not allowed_modes and not pending_modes:
        issues.append(
            f"{artifact_label} intake role routing decision lacks a canonical route mode"
        )
    if pending_modes:
        issues.append(
            f"dispatch/ready {artifact_label} records pending role routing mode "
            f"`{sorted(pending_modes)[0]}`; keep status HOLD/DRAFT until routing is resolved"
        )
    if len(allowed_modes) > 1:
        issues.append(
            f"{artifact_label} intake role routing decision records multiple route modes: "
            f"{', '.join(sorted(allowed_modes))}"
        )

    required_patterns = {
        "intake summary": r"intake|user request|operator request|raw request|non-coder",
        "scope classification": r"scope|bounded|blast radius|changed paths|allowed scope",
        "risk sensitivity": r"risk|public-sync|provider|live|secret|legal|production|readiness",
        "selected role route": r"role route|routing mode|execution model|selected route|routeMode|route mode",
        "role separation basis": r"worker|reviewer|orchestrator|single-agent|multi-agent|single_agent|multi_agent",
        "escalation condition": r"escalation|operator checkpoint|external reviewer|hold|blocked|stop",
    }
    for label, pattern in required_patterns.items():
        if not re.search(pattern, section, re.IGNORECASE):
            issues.append(
                f"{artifact_label} intake role routing decision is missing {label}"
            )

    if "SINGLE_AGENT_MULTI_ROLE" in allowed_modes and SINGLE_AGENT_MULTI_ROLE_MARKER not in text:
        issues.append(
            f"{artifact_label} selects `SINGLE_AGENT_MULTI_ROLE` but lacks "
            f"`## {SINGLE_AGENT_MULTI_ROLE_MARKER}`"
        )

    return sorted(set(issues))


def _validate_dispatch_pending_dependency_language(text: str, artifact_label: str) -> list[str]:
    text = re.split(r"(?im)^##\s+.*Reviewer Closure Conversion.*$", text, maxsplit=1)[0]
    filtered_lines = [
        line
        for line in text.splitlines()
        if "forbiddenClosedEquivalentResidue" not in line
        and "pendingStatusTokensAllowedBeforeReview" not in line
    ]
    windows: list[str] = []
    for index, line in enumerate(filtered_lines):
        if not re.search(r"\b(?:Prerequisite|Prerequisites|Predecessor|Dependency|CLOSED_PASS)\b", line, re.IGNORECASE):
            continue
        next_line = filtered_lines[index + 1] if index + 1 < len(filtered_lines) else ""
        windows.append(f"{line} {next_line}".strip())
    if not any(PENDING_DEPENDENCY_LANGUAGE_RE.search(window) for window in windows):
        return []
    return [
        f"dispatch/ready {artifact_label} contains pending predecessor release language next to "
        "`CLOSED_PASS` evidence; keep status HOLD/DRAFT until the prerequisite closure commit exists"
    ]


def _validate_ready_dependency_release(text: str) -> list[str]:
    issues: list[str] = []
    issues.extend(_validate_dispatch_pending_dependency_language(text, "work order"))
    for row in (row for table in _parse_any_markdown_tables(text) for row in table):
        disposition = _row_value(row, "Disposition").strip().strip("`").upper()
        joined = " ".join(row.values())
        if disposition == "REQUIRED":
            issues.append(
                "dispatch/ready work order contains unresolved prerequisite disposition `REQUIRED`; "
                "release HOLD only after replacing it with source-backed ACCEPT evidence per "
                "docs/reference/CVF_WORK_ORDER_DEPENDENCY_RELEASE_EVIDENCE_STANDARD_2026-06-03.md"
            )
            break
        if disposition == "ACCEPT":
            continue
        if re.search(r"\bafter\s+(?:closure|T\d+\s+closure|[A-Z0-9_-]+\s+closure)\b", joined, re.IGNORECASE):
            issues.append(
                "dispatch/ready work order contains stale dependency placeholder prose such as `after closure`; "
                "cite the closed artifact path and commit before dispatch per "
                "docs/reference/CVF_WORK_ORDER_DEPENDENCY_RELEASE_EVIDENCE_STANDARD_2026-06-03.md"
            )
            break
    for match in re.finditer(
        r"`(?P<path>(?:docs|governance|EXTENSIONS|CVF_SESSION|scripts|sdk|\.github|\.private_reference)/[^`]+)`"
        r"[^\n`]*\bat commit\s+`(?P<commit>[0-9a-f]{7,40})`",
        text,
        re.IGNORECASE,
    ):
        path = match.group("path")
        commit = match.group("commit")
        if not _commit_contains_path(commit, path):
            issues.append(
                "dispatch/ready work order cites dependency artifact "
                f"`{path}` at commit `{commit}`, but that commit does not contain the path; "
                "cite the closure commit that contains the prerequisite artifact per "
                "docs/reference/CVF_WORK_ORDER_DEPENDENCY_RELEASE_EVIDENCE_STANDARD_2026-06-03.md"
            )
    return issues


def _looks_like_live_method_proof(text: str) -> bool:
    lowered = text.lower()
    return (
        "live proof" in lowered
        and ("provider method" in lowered or "json_mode" in lowered or "streaming" in lowered or "tool_call" in lowered)
    )


def _has_source_verified_executable_proof_path(text: str) -> bool:
    for row in _parse_markdown_tables(text):
        if "ACCEPT" not in row.get("Disposition", "").upper():
            continue
        joined = " ".join(row.values()).lower()
        if "executable" not in joined or "proof path" not in joined:
            continue
        if any(_exists_rel(source_path) for source_path in _extract_paths(row.get("Source file", ""))):
            return True
    return False


def _validate_ready_live_method_proof_path(text: str) -> list[str]:
    if not _looks_like_live_method_proof(text):
        return []
    if "/api/execute" not in text and "method flag" not in text.lower():
        return []
    if _has_source_verified_executable_proof_path(text):
        return []
    return [
        "dispatch/ready live-method proof cites generic `/api/execute` or a method flag "
        "without a source-verified executable proof path"
    ]


def _validate_accepted_source_rows(path: str, text: str) -> list[str]:
    issues: list[str] = []
    rows = _parse_markdown_tables(text)
    for row in rows:
        disposition = row.get("Disposition", "").upper()
        if "ACCEPT" not in disposition:
            continue
        verified_symbol = row.get("Verified path or symbol", "")
        if _verified_symbol_contains_assignment(verified_symbol):
            issues.append(
                "Source Verification `Verified path or symbol` must contain only a field/path/symbol, "
                "not a value assignment or type annotation"
            )
            continue
        source_cell = row.get("Source file", "")
        source_paths = _extract_paths(source_cell)
        if not source_paths:
            joined = " ".join(row.values()).lower()
            if "doc-only" in joined or "(new)" in joined:
                issues.append(
                    "New doc-only fields must be listed in a separate New Doc-Only Fields table, "
                    "not as Source Verification ACCEPT rows"
                )
                continue
            if "canonical" not in source_cell.lower() and "n/a" not in source_cell.lower():
                issues.append("Source Verification ACCEPT row lacks a concrete source file or canonical-contract marker")
            continue
        for source_path in source_paths:
            if not _exists_rel(source_path):
                issues.append(f"Source Verification ACCEPT cites missing source file `{source_path}`")
                continue
            claimed = row.get("Claimed item", "")
            source_text = _read_rel(source_path)
            if _is_code_source(source_path) and not _source_has_verified_symbol(source_text, verified_symbol):
                issues.append(
                    "Source Verification ACCEPT row cites symbol "
                    f"`{verified_symbol.strip().strip('`')}` but `{source_path}` does not contain that symbol "
                    "under the verified owner/path"
                )
            line_issue = _validate_verified_line_anchor(source_path, source_text, row)
            if line_issue:
                issues.append(line_issue)
            false_issue = _validate_false_invariant_against_source(source_path, source_text, row)
            if false_issue:
                issues.append(false_issue)
            joined = " ".join(row.values()).lower()
            if (
                source_path.startswith("docs/roadmaps/")
                and ("doc-only field" in joined or "advisorytype" in joined or "boundarymarker" in joined)
            ):
                issues.append(
                    "Source Verification ACCEPT for connector doc-only field cites a roadmap; "
                    "cite the connector spec after it exists or move the field to New Doc-Only Fields"
                )
            if re.search(r"\b(?:pending|planned|future)\b", row.get("Verified line/section", ""), re.IGNORECASE):
                issues.append(
                    "Source Verification ACCEPT uses pending/planned/future line or section language; "
                    "use BLOCKED_SOURCE_NOT_FOUND until the source exists"
                )
            if "values" not in f"{claimed} {verified_symbol}".lower():
                continue
            declared_values = _extract_declared_string_values(source_text, verified_symbol)
            if not declared_values:
                continue
            row_tokens = _row_literal_tokens(row)
            missing_values = sorted(value for value in declared_values if value not in row_tokens)
            if missing_values:
                issues.append(
                    "Source Verification ACCEPT row claims values for "
                    f"`{verified_symbol.strip().strip('`')}` but omits source value(s): {', '.join(missing_values)}"
                )
    issues.extend(_validate_false_invariant_prose(text, rows))
    issues.extend(_validate_known_false_invariant_claims(text))
    return issues


def _validate_no_empty_range_commands(text: str) -> list[str]:
    if re.search(r"--base\s+HEAD\s+--head\s+HEAD", text):
        return [
            "artifact records an empty `--base HEAD --head HEAD` verification range; "
            "use the actual base/head range or the autorun wrapper default for closure"
        ]
    return []


def _has_pending_content_status(statuses: set[str]) -> bool:
    return bool(statuses) and not statuses <= {"R"}


FINDING_MARKERS = ("## Quality Findings", "## Findings", "## Known Issues", "Known Issues", "| Finding |", "finding |")
FINDING_LEARNING_SECTION = "## Finding-To-Governance Learning Disposition"


def _validate_pending_artifact_evidence_finality(path: str, text: str, statuses: set[str]) -> list[str]:
    if not _has_pending_content_status(statuses):
        return []
    issues: list[str] = []
    if re.search(
        r"git\s+status\s+--short[^\n\r]{0,120}(?:→|->|:)\s*(?:`?clean`?|clean\b|worktree\s+clean)",
        text,
        re.IGNORECASE,
    ):
        issues.append(
            "pending changed artifact records `git status --short` as clean even though the artifact "
            "itself is not committed; record the actual pending status or commit first"
        )
    if re.search(
        r"(?:run_agent_autorun_workflow_gate|check_work_order_dispatch_quality|check_[A-Za-z0-9_]+)"
        r"[^\n\r]{0,180}--base\s+HEAD~1\s+--head\s+HEAD",
        text,
        re.IGNORECASE,
    ):
        issues.append(
            "pending changed artifact cites `--base HEAD~1 --head HEAD` gate evidence that does not "
            "prove the pending artifact; use a working-tree-aware validation or commit the artifact "
            "and rerun the real changed range"
        )
    if re.search(r"\bstaged\s+for\s+review\b", text, re.IGNORECASE) and "A" not in statuses and "M" not in statuses:
        issues.append(
            "artifact claims it is staged for review, but git status does not show staged content for this path"
        )
    if re.search(r"(?im)^\s*[-*]\s+`?git\s+status\s+--short`?\s*(?:->|→|:)", text) and path not in text:
        issues.append(
            "pending changed artifact records `git status --short` but omits its own pending path; "
            "record the actual pending status line for this artifact"
        )
    return issues


def _is_finding_bearing(text: str) -> bool:
    return any(marker in text for marker in FINDING_MARKERS)


def _validate_self_reported_gate_evidence_consistency(text: str) -> list[str]:
    issues: list[str] = []
    status = _extract_status(text).upper()
    blocking_status = any(token in status for token in ("BLOCKED", "HOLD"))
    gate_failures = re.findall(
        r"(?im)^\s*[-*]\s+`[^`\n]*(?:check_work_order_dispatch_quality|run_agent_autorun_workflow_gate|"
        r"check_corpus_completeness_report_integrity|check_corpus_to_knowledge_map_reconciliation)"
        r"[^`\n]*`\s*(?:->|→|:)\s*(?:`?FAIL`?|FAILED\b)",
        text,
    )
    if gate_failures and not blocking_status:
        issues.append(
            "artifact records a failed self-reported governance gate while status is not BLOCKED/HOLD; "
            "repair allowed-scope failures and rerun, or mark the artifact BLOCKED with return action"
        )
    if (
        _is_finding_bearing(text)
        and FINDING_LEARNING_SECTION not in text
        and re.search(
            r"(?im)^\s*[-*]\s+`[^`\n]*run_agent_autorun_workflow_gate[^`\n]*`\s*(?:->|→|:)\s*(?:`?PASS`?|PASSED\b)",
            text,
        )
    ):
        issues.append(
            "artifact records autorun gate PASS but is finding-bearing without "
            "`## Finding-To-Governance Learning Disposition`; rerun after adding the required section"
        )
    return issues


def _extract_accept_owner_map_concepts(source_text: str) -> list[str]:
    concepts: list[str] = []
    for raw_line in source_text.splitlines():
        stripped = raw_line.strip()
        if not (stripped.startswith("|") and "ACCEPT_AS_OWNER_MAP" in stripped):
            continue
        cells = [cell.strip().strip("`") for cell in stripped.strip("|").split("|")]
        if len(cells) < 2:
            continue
        concept = re.sub(r"\s+", " ", cells[0]).strip()
        if concept and concept.lower() != "concept":
            concepts.append(concept)
    return concepts


def _normalize_concept_text(value: str) -> str:
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"[^A-Za-z0-9]+", " ", value).lower()
    return re.sub(r"\s+", " ", value).strip()


def _concept_mentioned(text: str, concept: str) -> bool:
    normalized_text = _normalize_concept_text(text)
    normalized_concept = _normalize_concept_text(concept)
    if normalized_concept and normalized_concept in normalized_text:
        return True
    tokens = [
        token
        for token in normalized_concept.split()
        if token not in {"the", "and", "for", "with", "remaining", "items", "item"}
    ]
    if not tokens:
        return False
    # Long concept names may include explanatory parentheticals. Requiring every
    # token would make disposition tables brittle, so require the leading core.
    core_tokens = tokens[: min(4, len(tokens))]
    return all(re.search(rf"\b{re.escape(token)}\b", normalized_text) for token in core_tokens)


def _claims_all_accept_owner_map_coverage(text: str) -> bool:
    return re.search(
        r"(?:covers|cover|absorb|absorbs|covering)[\s\S]{0,180}"
        r"ACCEPT_AS_OWNER_MAP|ACCEPT_AS_OWNER_MAP[\s\S]{0,180}(?:all|remaining)",
        text,
        re.IGNORECASE,
    ) is not None


def _validate_accept_owner_map_coverage(text: str) -> list[str]:
    if not _claims_all_accept_owner_map_coverage(text):
        return []
    audit_text = _read_rel(IMPORTANT_FULL_SCAN_AUDIT_PATH)
    if not audit_text:
        return [
            f"artifact claims complete ACCEPT_AS_OWNER_MAP coverage but `{IMPORTANT_FULL_SCAN_AUDIT_PATH}` is missing"
        ]
    missing = [
        concept
        for concept in _extract_accept_owner_map_concepts(audit_text)
        if not _concept_mentioned(text, concept)
    ]
    if not missing:
        return []
    return [
        "artifact claims complete ACCEPT_AS_OWNER_MAP coverage but lacks disposition for: "
        + "; ".join(missing)
    ]


def _has_runtime_freshness_section(text: str) -> bool:
    return re.search(
        r"^##\s+(?:Current Runtime Freshness Verification|Runtime Freshness Verification|Repo Freshness Verification)\b",
        text,
        re.MULTILINE | re.IGNORECASE,
    ) is not None


def _has_absence_or_staleness_claim(text: str) -> bool:
    return re.search(
        r"\b(?:NOT in CVF|not implemented|completely absent|absent from CVF|"
        r"no registry|no learning orchestrator|hardcoded strings?|per-role only|"
        r"no typed execution strategy|no relevance scoring|"
        r"no registry update|"
        r"no provider/API key use|no provider calls?|must not call providers?|"
        r"do not call providers?)\b",
        text,
        re.IGNORECASE,
    ) is not None


def _validate_runtime_freshness_claims(text: str) -> list[str]:
    issues: list[str] = []
    if _has_absence_or_staleness_claim(text) and not _has_runtime_freshness_section(text):
        issues.append(
            "artifact makes absent/not-implemented/hardcoded runtime claims without a "
            "`Current Runtime Freshness Verification` section"
        )

    if "resolveProviderForRole" in text and "EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts" not in text:
        issues.append(
            "`resolveProviderForRole()` claim must cite current source "
            "`EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`"
        )

    provider_registry_claim = re.search(
        r"provider[\s\S]{0,120}(?:hardcoded|no registry|no model registry|no provider/API key use|no provider calls?)"
        r"|(?:hardcoded|no registry|no model registry|no provider/API key use|no provider calls?)[\s\S]{0,120}provider",
        text,
        re.IGNORECASE,
    )
    if provider_registry_claim:
        if (
            "EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts" not in text
            and "PROVIDER_CAPABILITY_REGISTRY" not in text
        ):
            issues.append(
                "provider registry absence/hardcoded claim must account for current "
                "`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and "
                "`PROVIDER_CAPABILITY_REGISTRY` surfaces"
            )

    if re.search(r"consolidation and decay[\s\S]{0,120}(?:NOT implemented|not implemented|absent)", text, re.IGNORECASE):
        if "EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts" not in text:
            issues.append(
                "memory consolidation/decay absence claim must account for current "
                "`EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts`"
            )

    if re.search(r"No learning orchestrator in CVF|learning orchestrator[\s\S]{0,80}NOT in CVF", text, re.IGNORECASE):
        if (
            "EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts" not in text
            and "EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/feedback.ledger.contract.ts" not in text
        ):
            issues.append(
                "learning-orchestrator absence claim must account for current learning-signal "
                "and feedback ledger surfaces"
            )

    return issues


def _validate_required_first_reads(text: str) -> list[str]:
    issues: list[str] = []
    section = _extract_section(text, "Required First Reads")
    for path in _extract_paths(section):
        if not _exists_rel(path):
            issues.append(f"Required First Reads cites missing path `{path}`")
    return issues


def _classify_size_guard_path(path: str) -> str:
    suffix = Path(path).suffix.lower()
    lower = path.lower()
    if suffix == ".md":
        return "active_markdown"
    if ".test." in lower or "/tests/" in lower:
        return "test_code"
    if suffix in {".tsx", ".jsx"}:
        return "frontend_component"
    return "general_source"


def _validate_near_threshold_owner_maintainability_plan(text: str) -> list[str]:
    issues: list[str] = []
    registry_path = REPO_ROOT / FILE_SIZE_REGISTRY_PATH
    if not registry_path.exists():
        return issues
    try:
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return [f"`{FILE_SIZE_REGISTRY_PATH}` is invalid JSON"]

    thresholds = registry.get("thresholds", {})
    margin = int(registry.get("nearHardRotationMarginLines", 25))
    min_shrink = int(registry.get("nearHardMinShrinkLines", 50))
    ownership_text = "\n".join(
        [
            _extract_allowed_scope_text(text),
            _extract_section(text, "Write Ownership"),
        ]
    )
    ownership_paths = set(_extract_paths(ownership_text))
    forbidden_paths = set(_extract_paths(_extract_forbidden_scope_text(text)))
    plan_text = _extract_section(text, NEAR_THRESHOLD_PLAN_MARKER)

    for owner in registry.get("proactiveOwnerSurfaces", []):
        if not isinstance(owner, dict) or owner.get("status") != "ACTIVE":
            continue
        owner_path = str(owner.get("path", "")).replace("\\", "/").strip()
        prefixes = [
            str(prefix).replace("\\", "/").strip()
            for prefix in owner.get("domainPrefixes", [])
            if str(prefix).strip()
        ]
        full_owner_path = REPO_ROOT / owner_path
        if not owner_path or not prefixes or not full_owner_path.exists():
            continue
        file_class = _classify_size_guard_path(owner_path)
        hard = int(thresholds.get(file_class, {}).get("hardThresholdLines", 0) or 0)
        lines = len(full_owner_path.read_text(encoding="utf-8", errors="replace").splitlines())
        if not hard or lines < max(1, hard - margin):
            continue
        adjacent_owned = sorted(
            path
            for path in ownership_paths
            if path != owner_path and any(path.startswith(prefix) for prefix in prefixes)
        )
        if not adjacent_owned:
            continue
        if not plan_text:
            issues.append(
                f"dispatch/ready work order enters registered near-threshold owner domain for `{owner_path}` "
                f"({lines}/{hard} lines) without `## {NEAR_THRESHOLD_PLAN_MARKER}`"
            )
            continue
        if owner_path not in ownership_paths:
            issues.append(
                f"dispatch/ready work order enters registered near-threshold owner domain for `{owner_path}` "
                "but does not include the owner entrypoint in Allowed scope or Write Ownership"
            )
        if owner_path in forbidden_paths:
            issues.append(
                f"dispatch/ready work order treats near-threshold owner entrypoint `{owner_path}` as forbidden-touch; "
                "split/shrink ownership is required instead of bypassing maintainability debt"
            )
        if owner_path not in plan_text:
            issues.append(
                f"`## {NEAR_THRESHOLD_PLAN_MARKER}` must cite near-threshold owner entrypoint `{owner_path}`"
            )
        if not re.search(r"\b(?:split|extract|rotate|archive)\b", plan_text, re.IGNORECASE):
            issues.append(
                f"`## {NEAR_THRESHOLD_PLAN_MARKER}` must name a split/extract/rotate/archive action for `{owner_path}`"
            )
        if not re.search(
            rf"Minimum shrink target:\s*{min_shrink}\s+lines\b",
            plan_text,
            re.IGNORECASE,
        ):
            issues.append(
                f"`## {NEAR_THRESHOLD_PLAN_MARKER}` must include `Minimum shrink target: {min_shrink} lines`"
            )
    return issues


def _validate_work_order(path: str, text: str) -> list[str]:
    issues: list[str] = []
    status = _extract_status(text)
    dispatching = "DISPATCHED" in status.upper() or "READY" in status.upper()
    issues.extend(_validate_status_token_hygiene(text, "work order"))
    issues.extend(_validate_closed_artifact_finality(text, "work order"))
    issues.extend(_validate_mandatory_remediation_escalation(text, "work order"))

    if dispatching and _is_roadmap_derived(text) and not _has_trace_matrix(text):
        issues.append("roadmap-derived work order is dispatch/ready without Roadmap-To-Work-Order Trace Matrix")

    if dispatching and not _has_worker_autonomy_clause(text):
        issues.append("dispatch/ready work order lacks Worker Autonomy / No-Question Rule")

    if dispatching:
        issues.extend(_validate_commit_mode_and_anchor_lifecycle(text))
        issues.extend(_validate_worker_completion_review_boundary(text))
        issues.extend(_validate_no_commit_reviewer_closure_contract(text))
        issues.extend(_validate_source_verification_table_shape(text))
        issues.extend(_validate_source_verification_disposition_discipline(text))
        issues.extend(_validate_intake_role_routing_decision(text, "work order"))
        issues.extend(_validate_single_agent_multi_role_control(text, "work order"))
        issues.extend(_validate_evidence_reuse_and_encoding_plan(text))
        issues.extend(_validate_protected_path_authorization_carrier(text))

    if dispatching and _is_connector_wave(path, text):
        wave_id = _extract_wave_id(path, text)
        if wave_id is not None and not _has_gc018_for_wave(wave_id):
            issues.append(f"LHW{wave_id} connector work order is dispatch/ready without fresh GC-018 baseline")
        if "Source Verification" not in text or not _source_table_has_required_columns(text):
            issues.append("dispatch/ready work order lacks a complete Source Verification table")

    if dispatching:
        issues.extend(_validate_required_first_reads(text))
        issues.extend(_validate_required_proof_manifest_atomic_literals(text))
        issues.extend(_validate_near_threshold_owner_maintainability_plan(text))
        if (
            ("Required Artifact Manifest" in text or "Required Proof Manifest" in text)
            and FULFILLMENT_MANIFEST_MARKER not in text
        ):
            issues.append(
                "work order has required artifact/proof manifests but lacks "
                f"`{FULFILLMENT_MANIFEST_MARKER}` marker"
            )
        blocking_precondition = re.search(
            r"(pre-?condition|gate condition|dispatch only after|only after)[\s\S]{0,240}CLOSED_PASS",
            text,
            re.IGNORECASE,
        )
        if blocking_precondition:
            issues.append("dispatch/ready status conflicts with unresolved CLOSED_PASS precondition language")
        issues.extend(_validate_ready_source_blockers(text))
        issues.extend(_validate_ready_dependency_release(text))
        issues.extend(_validate_ready_live_method_proof_path(text))

    issues.extend(_validate_accepted_source_rows(path, text))
    issues.extend(_validate_negative_search_collision_discipline(path, text, "work order"))
    issues.extend(_validate_no_empty_range_commands(text))
    issues.extend(_validate_accept_owner_map_coverage(text))
    issues.extend(_validate_runtime_freshness_claims(text))

    if re.search(r"install[\s\S]{0,120}always blocked|always blocked[\s\S]{0,120}install", text, re.IGNORECASE):
        issues.append("work order asserts `install` is always blocked; cite a source policy or map it to approval/escalation")

    return issues


def _validate_roadmap(path: str, text: str) -> list[str]:
    issues: list[str] = []
    status = _extract_status(text)
    issues.extend(_validate_status_token_hygiene(text, "roadmap"))
    issues.extend(_validate_closed_artifact_finality(text, "roadmap"))
    issues.extend(_validate_mandatory_remediation_escalation(text, "roadmap"))
    issues.extend(_validate_closed_roadmap_status_residue(text))
    issues.extend(_validate_referenced_work_order_closure(text, "roadmap"))
    if _is_connector_wave(path, text) and _is_dispatch_status(status) and not _is_hold_status(status):
        wave_id = _extract_wave_id(path, text)
        if wave_id is not None and not _has_gc018_for_wave(wave_id):
            issues.append(f"LHW{wave_id} connector roadmap is dispatch/ready without fresh GC-018 baseline")
    if _is_dispatch_status(status) and not _is_hold_status(status):
        issues.extend(_validate_dispatch_pending_dependency_language(text, "roadmap"))
        issues.extend(_validate_source_verification_disposition_discipline(text))
    issues.extend(_validate_accepted_source_rows(path, text))
    issues.extend(_validate_negative_search_collision_discipline(path, text, "roadmap"))
    issues.extend(_validate_no_empty_range_commands(text))
    issues.extend(_validate_accept_owner_map_coverage(text))
    issues.extend(_validate_runtime_freshness_claims(text))
    return issues


def _validate_baseline(path: str, text: str) -> list[str]:
    issues: list[str] = []
    issues.extend(_validate_status_token_hygiene(text, "baseline"))
    issues.extend(_validate_closed_artifact_finality(text, "baseline"))
    issues.extend(_validate_mandatory_remediation_escalation(text, "baseline"))
    issues.extend(_validate_referenced_work_order_closure(text, "baseline"))
    issues.extend(_validate_accepted_source_rows(path, text))
    issues.extend(_validate_negative_search_collision_discipline(path, text, "baseline"))
    issues.extend(_validate_no_empty_range_commands(text))
    issues.extend(_validate_accept_owner_map_coverage(text))
    issues.extend(_validate_runtime_freshness_claims(text))
    return issues


def _validate_fast_lane_audit(path: str, text: str) -> list[str]:
    issues: list[str] = []
    status = _extract_status(text)
    issues.extend(_validate_status_token_hygiene(text, "fast-lane audit"))
    issues.extend(_validate_closed_artifact_finality(text, "fast-lane audit"))
    issues.extend(_validate_mandatory_remediation_escalation(text, "fast-lane audit"))
    issues.extend(_validate_fast_lane_status_consistency(text))
    if "FAST_LANE_READY" in status.upper() and re.search(
        r"(pre-?condition|conditional|only after)[\s\S]{0,240}CLOSED_PASS",
        text,
        re.IGNORECASE,
    ):
        issues.append("FAST_LANE_READY audit has unmet/conditional CLOSED_PASS prerequisite; use HOLD_* until satisfied")
    if _is_connector_wave(path, text) and "FAST_LANE_READY" in status.upper():
        wave_id = _extract_wave_id(path, text)
        if wave_id is not None and not _has_gc018_for_wave(wave_id):
            issues.append(f"LHW{wave_id} fast-lane audit is ready without fresh GC-018 baseline")
    issues.extend(_validate_accepted_source_rows(path, text))
    issues.extend(_validate_negative_search_collision_discipline(path, text, "fast-lane audit"))
    issues.extend(_validate_no_empty_range_commands(text))
    return issues


def _validate_completion_or_spec(path: str, text: str) -> list[str]:
    issues: list[str] = []
    issues.extend(_validate_status_token_hygiene(text, "completion/spec artifact"))
    issues.extend(_validate_closed_artifact_finality(text, "completion/spec artifact"))
    issues.extend(_validate_mandatory_remediation_escalation(text, "completion/spec artifact"))
    issues.extend(_validate_referenced_work_order_closure(text, "completion/spec artifact"))
    issues.extend(_validate_accepted_source_rows(path, text))
    issues.extend(_validate_negative_search_collision_discipline(path, text, "completion/spec artifact"))
    issues.extend(_validate_no_empty_range_commands(text))
    issues.extend(_validate_connector_spec_line_count_claim(path, text))
    return issues


def _validate_connector_spec_line_count_claim(path: str, text: str) -> list[str]:
    normalized = path.replace("\\", "/")
    if not (
        normalized.startswith("docs/reference/CVF_LHW")
        and "CONNECTOR_SPEC" in normalized.upper()
    ):
        return []
    actual = len(text.splitlines())
    thresholds = {
        int(match.group(1))
        for match in re.finditer(
            r"(?im)\b(?:connector\s+spec|spec|artifact|file)[^\n]{0,80}"
            r"(?:<|under|below|no\s+more\s+than|max(?:imum)?)\s*(\d+)\s+lines?\b",
            text,
        )
    }
    for threshold in sorted(thresholds):
        if actual > threshold:
            return [
                f"connector spec claims a line-count threshold under {threshold} lines but file has {actual} lines"
            ]
    return []


def _extract_allowed_scope_text(text: str) -> str:
    patterns = (
        r"(?ims)^Allowed scope:\s*$([\s\S]*?)(?=^Forbidden scope:\s*$|^##\s+|\Z)",
        r"(?ims)^\*\*Allowed scope:\*\*\s*$([\s\S]*?)(?=^\*\*Forbidden scope:\*\*\s*$|^##\s+|\Z)",
        r"(?ims)^Allowed:\s*$([\s\S]*?)(?=^Forbidden:\s*$|^##\s+|\Z)",
        r"(?ims)^\*\*Allowed:\*\*\s*$([\s\S]*?)(?=^\*\*Forbidden:\*\*\s*$|^##\s+|\Z)",
    )
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    return ""


def _extract_forbidden_scope_text(text: str) -> str:
    patterns = (
        r"(?ims)^Forbidden scope:\s*$([\s\S]*?)(?=^##\s+|\Z)",
        r"(?ims)^\*\*Forbidden scope:\*\*\s*$([\s\S]*?)(?=^##\s+|\Z)",
        r"(?ims)^Forbidden:\s*$([\s\S]*?)(?=^##\s+|\Z)",
        r"(?ims)^\*\*Forbidden:\*\*\s*$([\s\S]*?)(?=^##\s+|\Z)",
    )
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    return ""


def _path_matches_allowed(path: str, allowed_path: str) -> bool:
    normalized = path.replace("\\", "/").strip()
    allowed = allowed_path.replace("\\", "/").strip().rstrip("/")
    return normalized == allowed or normalized.startswith(f"{allowed}/")


def _is_session_continuity_path(path: str) -> bool:
    normalized = path.replace("\\", "/")
    return normalized in {
        "CVF_SESSION_MEMORY.md",
        "CVF_SESSION/ACTIVE_SESSION_STATE.json",
    } or normalized.startswith("CVF_SESSION/handoffs/") or normalized.startswith("AGENT_HANDOFF")


def _validate_single_work_order_scope_range(changed_files: list[str]) -> list[dict[str, Any]]:
    normalized_files = sorted(path.replace("\\", "/") for path in changed_files)
    closed_work_orders: list[str] = []
    for path in normalized_files:
        if not path.startswith("docs/work_orders/") or "/archive/" in path:
            continue
        text = _read_rel(path)
        if text and _is_closed_status(_extract_status(text)):
            closed_work_orders.append(path)
    if len(closed_work_orders) != 1:
        return []

    work_order_path = closed_work_orders[0]
    text = _read_rel(work_order_path)
    allowed_scope = _extract_allowed_scope_text(text)
    if not allowed_scope:
        return []

    explicit_paths = _extract_paths(allowed_scope)
    allowed_lower = allowed_scope.lower()
    disallowed: list[str] = []
    for path in normalized_files:
        if path == work_order_path:
            continue
        if any(_path_matches_allowed(path, allowed_path) for allowed_path in explicit_paths):
            continue
        if "this work order" in allowed_lower and path == work_order_path:
            continue
        if "session continuity" in allowed_lower and _is_session_continuity_path(path):
            continue
        disallowed.append(path)

    if not disallowed:
        return []

    sample = ", ".join(disallowed[:8])
    suffix = "" if len(disallowed) <= 8 else f", ... (+{len(disallowed) - 8} more)"
    return [
        {
            "path": work_order_path,
            "issues": [
                "closed work-order changed range includes files outside its Allowed scope: "
                f"{sample}{suffix}"
            ],
        }
    ]


def _is_runtime_or_source_change(path: str) -> bool:
    normalized = path.replace("\\", "/")
    if normalized.endswith(".md") or normalized.endswith(".json"):
        return False
    return normalized.startswith(("EXTENSIONS/", "scripts/", "sdk/", "governance/compat/"))


def _work_order_runtime_activity(text: str, changed_files: list[str]) -> bool:
    normalized_files = [path.replace("\\", "/") for path in changed_files]
    if any(_is_runtime_or_source_change(path) for path in normalized_files):
        return True
    owned_section = _extract_section(text, "Write Ownership")
    required_section = _extract_section(text, "Required Artifact Manifest")
    declared_paths = _extract_paths(owned_section + "\n" + required_section)
    return any(
        any(_path_matches_pattern(changed_path, declared_path) for declared_path in declared_paths)
        for changed_path in normalized_files
    )


def _validate_work_order_fulfillment_manifests(changed_files: list[str]) -> list[dict[str, Any]]:
    normalized_files = sorted(path.replace("\\", "/") for path in changed_files)
    violations: list[dict[str, Any]] = []

    for work_order_path in normalized_files:
        if not work_order_path.startswith("docs/work_orders/") or "/archive/" in work_order_path:
            continue
        text = _read_rel(work_order_path)
        if FULFILLMENT_MANIFEST_MARKER not in text:
            continue
        status = _extract_status(text)
        if not _is_dispatch_status(status) or _is_hold_status(status):
            continue
        if not _work_order_runtime_activity(text, normalized_files):
            continue

        issues: list[str] = []
        required_tables = _section_tables(text, "Required Artifact Manifest")
        if not required_tables:
            issues.append("work order declares fulfillment manifest but lacks `## Required Artifact Manifest` table")
        for table in required_tables:
            for row in table:
                path = _clean_manifest_path(_row_value(row, "Path", "Artifact", "Required artifact"))
                required_at_handoff = _truthy_cell(_row_value(row, "Required at handoff", "Required", "Must exist"))
                if path and required_at_handoff and not _exists_rel(path):
                    issues.append(f"required handoff artifact is missing: `{path}`")

        pre_existing_tables = _section_tables(text, "Pre-Existing Dirty Path Exemptions")
        exempt_patterns = [
            _clean_manifest_path(_row_value(row, "Path", "Pattern"))
            for table in pre_existing_tables
            for row in table
            if _clean_manifest_path(_row_value(row, "Path", "Pattern"))
        ]
        for table in _section_tables(text, "Forbidden Path Manifest"):
            for row in table:
                pattern = _clean_manifest_path(_row_value(row, "Path", "Pattern", "Forbidden path"))
                if not pattern:
                    continue
                for changed_path in normalized_files:
                    if any(_path_matches_pattern(changed_path, exempt) for exempt in exempt_patterns):
                        continue
                    if _path_matches_pattern(changed_path, pattern):
                        issues.append(f"changed file violates forbidden path manifest: `{changed_path}` matches `{pattern}`")

        for table in _section_tables(text, "Required Proof Manifest"):
            for row in table:
                required = _truthy_cell(_row_value(row, "Required at handoff", "Required", "Must exist"))
                if not required:
                    continue
                path = _clean_manifest_path(_row_value(row, "Path", "Proof path"))
                literal = _row_value(row, "Required literal", "Literal", "Required token").strip().strip("`")
                if path and not _exists_rel(path):
                    issues.append(f"required proof file is missing: `{path}`")
                    continue
                if path and literal and literal not in _read_rel(path):
                    issues.append(f"required proof literal `{literal}` is missing from `{path}`")

        # Fix (C): validate Forbidden Filesystem State At Dispatch block.
        # If the work order has a Forbidden Path Manifest but no
        # Forbidden Filesystem State At Dispatch section, flag it so orchestrators
        # are reminded to record disk state before dispatch.
        # If the section exists, check that no row records PRESENT without a
        # documented exemption or governance resolution.
        has_forbidden_manifest = bool(list(_section_tables(text, "Forbidden Path Manifest")))
        if has_forbidden_manifest:
            ffs_tables = list(_section_tables(text, "Forbidden Filesystem State At Dispatch"))
            if not ffs_tables:
                issues.append(
                    "work order has a Forbidden Path Manifest but is missing "
                    "`## Forbidden Filesystem State At Dispatch` block; "
                    "orchestrator must record disk state of forbidden paths before dispatch"
                )
            else:
                for table in ffs_tables:
                    for row in table:
                        actual = _row_value(row, "Actual state at dispatch", "Actual state", "Actual").strip().upper()
                        fp = _clean_manifest_path(_row_value(row, "Forbidden path", "Path", "Forbidden"))
                        if actual == "PRESENT" and fp:
                            issues.append(
                                f"Forbidden Filesystem State records PRESENT for `{fp}` without "
                                "exemption; resolve (remove or govern) before dispatch"
                            )

        if issues:
            violations.append({"path": work_order_path, "issues": issues})

    return violations


def _validate_runtime_changes_against_referenced_work_orders(changed_files: list[str]) -> list[dict[str, Any]]:
    normalized_files = sorted(path.replace("\\", "/") for path in changed_files)
    runtime_changed = [path for path in normalized_files if _is_runtime_or_source_change(path)]
    if not runtime_changed:
        return []

    referenced_work_orders: set[str] = set()
    referring_artifacts: dict[str, set[str]] = {}
    for path in normalized_files:
        if not _is_target(path):
            continue
        text = _read_rel(path)
        for work_order_path in _extract_paths(text):
            normalized_work_order = work_order_path.replace("\\", "/")
            if normalized_work_order.startswith("docs/work_orders/"):
                referenced_work_orders.add(normalized_work_order)
                referring_artifacts.setdefault(normalized_work_order, set()).add(path)

    for path in normalized_files:
        if path.startswith("docs/work_orders/") and "/archive/" not in path:
            referenced_work_orders.add(path)
            referring_artifacts.setdefault(path, set()).add(path)

    violations: list[dict[str, Any]] = []
    for work_order_path in sorted(referenced_work_orders):
        work_order_text = _read_rel(work_order_path)
        if not work_order_text:
            continue
        status = _extract_status(work_order_text)
        if not _is_hold_status(status):
            continue
        ownership_text = "\n".join(
            _extract_section(work_order_text, heading)
            for heading in (
                "Scope / Target / Owner Boundary",
                "Required Artifact Manifest",
                "Write Ownership",
                "Work-Order Fulfillment Manifest",
            )
        )
        owned_patterns = sorted(set(_extract_paths(ownership_text)))
        matched_runtime = [
            changed_path
            for changed_path in runtime_changed
            if any(_path_matches_pattern(changed_path, pattern) for pattern in owned_patterns)
        ]
        if not matched_runtime:
            continue
        sample_runtime = ", ".join(matched_runtime[:6])
        suffix = "" if len(matched_runtime) <= 6 else f", ... (+{len(matched_runtime) - 6} more)"
        referrers = ", ".join(sorted(referring_artifacts.get(work_order_path, set()))[:4])
        violations.append(
            {
                "path": work_order_path,
                "issues": [
                    "changed range includes runtime/source files while referenced work order "
                    f"`{work_order_path}` is still `{status}`; release/downgrade the work order "
                    "before implementation. Runtime/source sample: "
                    f"{sample_runtime}{suffix}. Referring artifact(s): {referrers or 'unknown'}"
                ],
            }
        )
    return violations


def _validate_lhw_wave_closure_range(
    changed_files: list[str],
    base_ref: str | None = None,
) -> list[dict[str, Any]]:
    normalized_files = sorted(path.replace("\\", "/") for path in changed_files)
    violations: list[dict[str, Any]] = []
    for path in normalized_files:
        if not path.startswith("docs/roadmaps/") or "/archive/" in path:
            continue
        if len(_extract_wave_ids_from_path(path)) != 1:
            continue
        text = _read_rel(path)
        current_status = _extract_status(text)
        if not text or not _is_closed_status(current_status) or not _is_connector_wave(path, text):
            continue
        if base_ref:
            prior_text = _read_rel_at(base_ref, path)
            prior_status = _extract_status(prior_text) if prior_text else ""
            if prior_text and _is_closed_status(prior_status):
                continue
        wave_id = _extract_wave_id(path, text)
        if wave_id is None:
            continue
        present_tranches = {
            int(match.group(1))
            for changed_path in normalized_files
            for match in re.finditer(rf"LHW{wave_id}[-_]T([123])(?!\d)", changed_path, re.IGNORECASE)
        }
        missing = [f"T{index}" for index in (1, 2, 3) if index not in present_tranches]
        if missing:
            violations.append(
                {
                    "path": path,
                    "issues": [
                        f"closed LHW{wave_id} connector roadmap changed without full wave-range evidence; "
                        f"missing changed artifact(s) for {', '.join(missing)}"
                    ],
                }
            )
    return violations


def _is_target(path: str) -> bool:
    normalized = path.replace("\\", "/")
    if "/archive/" in normalized:
        return False
    return normalized.endswith(".md") and (
        normalized.startswith("docs/work_orders/")
        or normalized.startswith("docs/roadmaps/")
        or normalized.startswith("docs/baselines/")
        or normalized.startswith("docs/reviews/")
        or (
            normalized.startswith("docs/reference/CVF_LHW")
            and "CONNECTOR_SPEC" in normalized.upper()
        )
    )


def _validate_path(path: str) -> list[str]:
    text = _read_rel(path)
    if not text:
        return ["changed governed dispatch artifact is missing from workspace"]
    normalized = path.replace("\\", "/")
    if normalized.startswith("docs/work_orders/"):
        return _validate_work_order(normalized, text)
    if normalized.startswith("docs/roadmaps/"):
        return _validate_roadmap(normalized, text)
    if normalized.startswith("docs/baselines/"):
        return _validate_baseline(normalized, text)
    if normalized.startswith("docs/reviews/") and "FAST_LANE_AUDIT" in normalized.upper():
        return _validate_fast_lane_audit(normalized, text)
    if normalized.startswith("docs/reviews/") or (
        normalized.startswith("docs/reference/CVF_LHW") and "CONNECTOR_SPEC" in normalized.upper()
    ):
        return _validate_completion_or_spec(normalized, text)
    return []


def _classify(changed_files: list[str], base_ref: str | None = None) -> dict[str, Any]:
    targets = sorted(path.replace("\\", "/") for path in changed_files if _is_target(path))
    # Collect the set of file statuses so rename-only files can be skipped.
    changed_status: dict[str, set[str]] = {}
    try:
        for p, statuses in _get_changed(base_ref or "HEAD", "HEAD").items():
            changed_status[p.replace("\\", "/")] = statuses
    except RuntimeError:
        # Unit tests patch REPO_ROOT to a temporary non-git directory and pass
        # explicit changed files. In that mode, content validation should still
        # run even though rename/pre-existing-status optimization is unavailable.
        changed_status = {}
    violations = []
    for path in targets:
        statuses = changed_status.get(path, set())
        # Skip files that were only renamed/moved — content unchanged, no new violations possible.
        if statuses and statuses <= {"R"}:
            continue
        # Skip deleted files — they are no longer present in the workspace and
        # cannot be validated; the archive move is governed by a separate authority doc.
        if statuses and "D" in statuses:
            continue
        text = _read_rel(path)
        issues = _validate_path(path)
        issues.extend(_validate_pending_artifact_evidence_finality(path, text, statuses))
        issues.extend(_validate_self_reported_gate_evidence_consistency(text))
        if not issues:
            continue
        # Suppress pre-existing violations: if every issue was already present in the
        # committed (HEAD) version of the file, this commit did not introduce them.
        head_text = _read_rel_at("HEAD", path)
        if head_text:
            from functools import reduce as _reduce
            def _issues_for_text(p: str, t: str) -> list[str]:
                n = p.replace("\\", "/")
                if n.startswith("docs/work_orders/"):
                    return _validate_work_order(n, t)
                if n.startswith("docs/roadmaps/"):
                    return _validate_roadmap(n, t)
                if n.startswith("docs/baselines/"):
                    return _validate_baseline(n, t)
                if n.startswith("docs/reviews/") and "FAST_LANE_AUDIT" in n.upper():
                    return _validate_fast_lane_audit(n, t)
                if n.startswith("docs/reviews/") or (
                    n.startswith("docs/reference/CVF_LHW") and "CONNECTOR_SPEC" in n.upper()
                ):
                    return _validate_completion_or_spec(n, t)
                return []
            head_issues = set(_issues_for_text(path, head_text))
            new_issues = [i for i in issues if i not in head_issues]
            if not new_issues:
                continue
            issues = new_issues
        violations.append({"path": path, "issues": issues})
    violations.extend(_validate_single_work_order_scope_range(changed_files))
    violations.extend(_validate_lhw_wave_closure_range(changed_files, base_ref=base_ref))
    violations.extend(_validate_runtime_changes_against_referenced_work_orders(changed_files))
    violations.extend(_validate_work_order_fulfillment_manifests(changed_files))

    required_markers = {
        STANDARD_PATH: (
            "Roadmap-To-Work-Order Trace Matrix",
            "Negative And Fail-Condition Scan",
            "Mandatory Gate-Failure Remediation Protocol",
            "Worker Autonomy / No-Question Rule",
            "Pending Artifact Evidence Finality",
            COMMIT_MODE_ANCHOR_MARKER,
            "Self-Reported Gate Evidence Consistency",
            NEAR_THRESHOLD_PLAN_MARKER,
            FULFILLMENT_MANIFEST_MARKER,
            "Current Runtime Freshness Verification",
            NEGATIVE_SEARCH_COLLISION_MARKER,
            SINGLE_AGENT_MULTI_ROLE_MARKER,
            INTAKE_ROLE_ROUTING_MARKER,
            EVIDENCE_REUSE_ENCODING_PLAN_MARKER,
            DISPATCH_PACKET_LEARNING_MARKER,
            "ACCEPT_AS_OWNER_MAP coverage",
            THIS_SCRIPT_PATH,
        ),
        WORK_ORDER_TEMPLATE_PATH: (
            "Source Verification Block",
            "Roadmap-To-Work-Order Trace Matrix",
            "Mandatory Gate-Failure Remediation Protocol",
            "Worker Autonomy / No-Question Rule",
            "Pending Artifact Evidence Finality",
            COMMIT_MODE_ANCHOR_MARKER,
            "Self-Reported Gate Evidence Consistency",
            NEAR_THRESHOLD_PLAN_MARKER,
            FULFILLMENT_MANIFEST_MARKER,
            "Current Runtime Freshness Verification",
            NEGATIVE_SEARCH_COLLISION_MARKER,
            SINGLE_AGENT_MULTI_ROLE_MARKER,
            INTAKE_ROLE_ROUTING_MARKER,
            "ACCEPT_AS_OWNER_MAP coverage",
            THIS_SCRIPT_PATH,
        ),
        WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_PATH: (
            EXPORT_SURFACE_DECISION_MARKER,
            NEXT_TRANCHE_AUDIT_MINI_PACKAGE_MARKER,
            NEAR_THRESHOLD_TEMPLATE_OWNER_MARKER,
            DISPATCH_PACKET_LEARNING_MARKER,
            REQUIRED_PROOF_ATOMIC_LITERAL_MARKER,
        ),
        WORK_ORDER_FINALITY_ADDENDUM_PATH: (
            COMMIT_MODE_ANCHOR_MARKER,
            "Dependency Release And Next-Work-Order Refresh",
            "Two-Stage Handoff Finality",
            "Worker Pending-Return Gate",
            "Reviewer Closure Conversion Block",
        ),
        EVIDENCE_REUSE_ENCODING_STANDARD_PATH: (
            EVIDENCE_REUSE_ENCODING_PLAN_MARKER,
            "REUSE_PRIOR_VERIFICATION",
            "RECOMPUTE_REQUIRED",
            "REVIEWER_RECOMPUTE_ONLY",
            "unicodePathHandling",
        ),
        WORKER_AUTONOMY_STANDARD_PATH: (
            "Worker Autonomy Prompt",
            "Worker Autonomy / No-Question Rule",
            "Commit Mode And Base-Anchor Requirement",
            THIS_SCRIPT_PATH,
        ),
        HOOK_CHAIN_PATH: (THIS_SCRIPT_PATH,),
    }
    marker_violations: dict[str, list[str]] = {}
    for path, markers in required_markers.items():
        # Skip marker check for files that no longer exist on disk (e.g., archived files).
        if not (REPO_ROOT / path).exists():
            continue
        text = _read_rel(path)
        missing = [marker for marker in markers if marker not in text]
        if missing:
            marker_violations[path] = missing

    return {
        "timestamp": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "policy": STANDARD_PATH,
        "script": THIS_SCRIPT_PATH,
        "checkedFiles": targets,
        "checkedFileCount": len(targets),
        "violations": violations,
        "violationCount": len(violations),
        "markerViolations": marker_violations,
        "markerViolationCount": len(marker_violations),
        "compliant": not violations and not marker_violations,
    }


def _print_report(report: dict[str, Any], base: str, head: str, base_source: str) -> None:
    print("=== CVF Work Order Dispatch Quality Gate ===")
    print(f"Range: {base}..{head}")
    print(f"Base source: {base_source}")
    print(f"Policy: {report['policy']}")
    print(f"Files checked: {report['checkedFileCount']}")
    print(f"Violations: {report['violationCount']}")
    print(f"Marker violations: {report['markerViolationCount']}")

    if report["checkedFiles"]:
        print("\nChecked dispatch artifacts:")
        for path in report["checkedFiles"]:
            print(f"  - {path}")
    else:
        print("\nNo changed work-order, roadmap, or fast-lane review artifacts required dispatch-quality validation.")

    if report["violations"]:
        print("\nDispatch-quality violations:")
        for violation in report["violations"]:
            print(f"  - {violation['path']}")
            for issue in violation["issues"]:
                print(f"    - {issue}")

    if report["markerViolations"]:
        print("\nGuard wiring marker violations:")
        for path, markers in report["markerViolations"].items():
            print(f"  - {path}")
            for marker in markers:
                print(f"    - missing marker `{marker}`")

    if report["compliant"]:
        print("\nCOMPLIANT - dispatch-quality gates are satisfied for checked artifacts.")
    else:
        print("\nVIOLATION - keep the artifact in HOLD/DRAFT or fix the missing dispatch evidence before execution.")


def _run_check(base: str | None, head: str | None) -> tuple[dict[str, Any], str, str, str]:
    resolved_base, resolved_head, base_source = _resolve_range(base, head)
    changed = _get_changed(resolved_base, resolved_head)
    report = _classify(sorted(changed), base_ref=resolved_base)
    return report, resolved_base, resolved_head, base_source


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(errors="replace")

    parser = argparse.ArgumentParser(description="Enforce CVF work-order dispatch quality gates")
    parser.add_argument("--base", default=None)
    parser.add_argument("--head", default=None)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--enforce", action="store_true")
    args = parser.parse_args()

    try:
        report, base, head, base_source = _run_check(args.base, args.head)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        _print_report(report, base, head, base_source)

    return 1 if args.enforce and not report["compliant"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

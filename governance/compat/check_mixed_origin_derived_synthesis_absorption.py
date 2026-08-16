#!/usr/bin/env python3
"""Forward guard for mixed-origin derived-synthesis absorption evidence."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BASE_CANDIDATES = ("origin/main", "origin/master", "main", "master")
STANDARD_PATH = "docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md"
THIS_SCRIPT_PATH = "governance/compat/check_mixed_origin_derived_synthesis_absorption.py"
MARKER = "Mixed-origin derived synthesis: REQUIRED"
PROVENANCE_SECTION = "## Mixed-Origin Derived Synthesis Provenance"
DECISION_SECTION = "## Absorption Decision Vector"
CHAIN_SECTION = "## System-Chain Value Review"
EFFICIENCY_SECTION = "## Absorption Efficiency And Provenance Reuse"
ARTIFACT_CLASS = "artifactClass: PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE"
AUTHORITY_STATUS = "authorityStatus: NON_AUTHORITATIVE_UNTIL_REVIEWED"

GOVERNED_PREFIXES = (
    "docs/assessments/", "docs/audits/", "docs/baselines/", "docs/reference/",
    "docs/reviews/", "docs/roadmaps/", "docs/work_orders/",
)
ORIGIN_COLUMNS = (
    "Input or concept", "Origin class", "Evidence basis", "Claim type",
    "Validation method", "Current CVF owner", "Disposition",
)
ORIGIN_CLASSES = {
    "UPSTREAM_REPOSITORY_BACKED", "CVF_PUBLIC_DERIVED", "OPERATOR_REQUIREMENT",
    "OPERATOR_AGENT_CO_DESIGNED", "NOVEL_SYNTHESIS", "MIXED_ORIGIN",
    "ORIGIN_UNRESOLVED",
}
DECISION_COLUMNS = ("Decision axis", "Decision", "Evidence", "Cost boundary")
DECISION_AXES = ("Knowledge absorption", "Direct import", "Runtime activation", "Authority promotion")
CHAIN_COLUMNS = (
    "Chain component", "Evidence path", "Existing CVF owner/gap",
    "Value disposition", "Readiness disposition", "Next action",
)
MATURITY_VALUE_RE = re.compile(
    r"(?:UNREVIEWED|UNMERGED|UNPROVEN_BASELINE).{0,100}"
    r"(?:NO_NEW_VALUE|STOP_COST_EXCEEDS_VALUE|REJECT(?:ED)?)|"
    r"(?:NO_NEW_VALUE|STOP_COST_EXCEEDS_VALUE|REJECT(?:ED)?).{0,100}"
    r"(?:UNREVIEWED|UNMERGED|UNPROVEN_BASELINE)", re.IGNORECASE,
)
EFFICIENCY_CONTROLS = {
    "manifestLedgerReuse": {"REUSE_IF_FRESH", "REFRESH_WITH_NAMED_DRIFT", "NOT_AVAILABLE_WITH_REASON"},
    "semanticReviewUnit": {"CAPABILITY_CLUSTER"},
    "defaultValuePosture": {"PRESERVE_UNTIL_CONTRADICTED"},
    "additionalValueProbe": {"SKIP_UNLESS_NAMED_GAP", "REQUIRED_WITH_NAMED_GAP"},
    "latencyBudget": {"SINGLE_PASS_BOUNDED"},
    "intakePriority": {"LOCAL_SYNTHESIZED_PACK_FIRST"},
    "localSemanticInspection": {"FILE_AND_USE_CASE_CONTENT_REQUIRED"},
    "mappingAction": {"DIRECT_WORK_ORDER_FOR_HIGH_FIT_CLUSTERS"},
    "deliverySequence": {"WORK_ORDER_THEN_WORKER_THEN_INDEPENDENT_REVIEWER"},
    "namePatternInference": {"FORBIDDEN_AS_VALUE_DISPOSITION"},
    "upstreamConsultation": {"TARGETED_FOR_PROVENANCE_OR_GAP"},
}


def _git(args: list[str]) -> tuple[int, str]:
    proc = subprocess.run(["git", *args], cwd=REPO_ROOT, text=True,
                          encoding="utf-8", errors="replace",
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.returncode, proc.stdout.strip()


def _ref_exists(ref: str) -> bool:
    return _git(["rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}"]) [0] == 0


def _range(base: str | None, head: str | None) -> tuple[str, str, str]:
    resolved_head = head or "HEAD"
    if base:
        return base, resolved_head, "explicit:--base"
    env_base = os.getenv("CVF_COMPAT_BASE")
    if env_base:
        return env_base, resolved_head, "env:CVF_COMPAT_BASE"
    for ref in DEFAULT_BASE_CANDIDATES:
        if _ref_exists(ref):
            code, out = _git(["merge-base", ref, resolved_head])
            if code == 0 and out:
                return out, resolved_head, f"merge-base({ref},{resolved_head})"
    return "HEAD~1", resolved_head, "fallback:HEAD~1"


def _parse_name_status(output: str) -> set[str]:
    paths: set[str] = set()
    for line in output.splitlines():
        parts = line.split("\t")
        if len(parts) >= 2:
            path = parts[2] if parts[0].startswith(("R", "C")) and len(parts) >= 3 else parts[1]
            paths.add(path.replace("\\", "/"))
    return paths


def _changed(base: str, head: str) -> set[str]:
    paths: set[str] = set()
    for args in (["diff", "--name-status", f"{base}..{head}"],
                 ["diff", "--name-status"], ["diff", "--name-status", "--cached"]):
        code, out = _git(args)
        if code == 0:
            paths.update(_parse_name_status(out))
    code, out = _git(["ls-files", "--others", "--exclude-standard"])
    if code == 0:
        paths.update(line.replace("\\", "/") for line in out.splitlines() if line)
    return paths


def _governed(path: str) -> bool:
    return path.endswith(".md") and "/archive/" not in path and path.startswith(GOVERNED_PREFIXES)


def _section(text: str, header: str) -> str:
    match = re.search(rf"(?m)^{re.escape(header)}\s*$", text)
    if not match:
        return ""
    start = match.end()
    next_header = re.search(r"(?m)^##\s+", text[start:])
    return text[start:start + next_header.start()] if next_header else text[start:]


def _rows(section: str) -> list[list[str]]:
    result = []
    for line in section.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            row = [cell.strip().strip("`") for cell in stripped.strip("|").split("|")]
            if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in row):
                result.append(row)
    return result


def _table(path: str, section: str, columns: tuple[str, ...], kind: str) -> tuple[list[list[str]], list[dict[str, str]]]:
    rows = _rows(section)
    if not rows:
        return [], [{"path": path, "type": f"mixed_origin_{kind}_table_missing", "message": f"{kind} section needs a table"}]
    headers = {cell.casefold(): idx for idx, cell in enumerate(rows[0])}
    violations = []
    for column in columns:
        if column.casefold() not in headers:
            violations.append({"path": path, "type": f"mixed_origin_{kind}_column_missing", "message": f"missing column `{column}`"})
    return rows, violations


def check_text(path: str, text: str) -> list[dict[str, str]]:
    normalized = path.replace("\\", "/")
    if not _governed(normalized) or (normalized != STANDARD_PATH and MARKER not in text):
        return []
    violations: list[dict[str, str]] = []
    required = (
        MARKER, PROVENANCE_SECTION, DECISION_SECTION, CHAIN_SECTION,
        EFFICIENCY_SECTION, ARTIFACT_CLASS, AUTHORITY_STATUS,
    )
    for token in required:
        if token not in text:
            violations.append({"path": normalized, "type": "mixed_origin_required_marker_missing", "message": f"missing `{token}`"})

    provenance = _section(text, PROVENANCE_SECTION)
    rows, problems = _table(normalized, provenance, ORIGIN_COLUMNS, "provenance") if provenance else ([], [])
    violations.extend(problems)
    if len(rows) < 2 and provenance:
        violations.append({"path": normalized, "type": "mixed_origin_provenance_row_missing", "message": "provenance table needs at least one input row"})
    if rows and not problems:
        headers = {cell.casefold(): idx for idx, cell in enumerate(rows[0])}
        idx = headers["origin class"]
        for row in rows[1:]:
            if len(row) <= idx:
                continue
            tokens = set(re.findall(r"\b[A-Z][A-Z0-9_]{3,}\b", row[idx]))
            if not tokens or not tokens <= ORIGIN_CLASSES:
                violations.append({"path": normalized, "type": "mixed_origin_origin_class_invalid", "message": f"invalid origin class `{row[idx]}`"})

    decision = _section(text, DECISION_SECTION)
    rows, problems = _table(normalized, decision, DECISION_COLUMNS, "decision") if decision else ([], [])
    violations.extend(problems)
    if rows and not problems:
        headers = {cell.casefold(): idx for idx, cell in enumerate(rows[0])}
        axis_text = "\n".join(row[headers["decision axis"]] for row in rows[1:] if len(row) > headers["decision axis"])
        for axis in DECISION_AXES:
            if axis.casefold() not in axis_text.casefold():
                violations.append({"path": normalized, "type": "mixed_origin_decision_axis_missing", "message": f"missing decision axis `{axis}`"})

    chain = _section(text, CHAIN_SECTION)
    rows, problems = _table(normalized, chain, CHAIN_COLUMNS, "system_chain") if chain else ([], [])
    violations.extend(problems)
    if len(rows) < 2 and chain:
        violations.append({"path": normalized, "type": "mixed_origin_system_chain_row_missing", "message": "system-chain review needs at least one component row"})

    efficiency = _section(text, EFFICIENCY_SECTION)
    if efficiency:
        for key, allowed in EFFICIENCY_CONTROLS.items():
            match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*([A-Z][A-Z0-9_]*)\s*$", efficiency)
            if not match:
                violations.append({"path": normalized, "type": "mixed_origin_efficiency_control_missing", "message": f"missing `{key}` control"})
            elif match.group(1) not in allowed:
                violations.append({"path": normalized, "type": "mixed_origin_efficiency_control_invalid", "message": f"invalid `{key}` value `{match.group(1)}`"})

    if MATURITY_VALUE_RE.search(text):
        violations.append({"path": normalized, "type": "mixed_origin_maturity_used_as_value", "message": "maturity token is coupled to a no-value/reject/stop decision"})
    return violations


def run_check(base: str | None = None, head: str | None = None) -> dict[str, Any]:
    resolved_base, resolved_head, source = _range(base, head)
    checked, violations = [], []
    for path in sorted(_changed(resolved_base, resolved_head)):
        full = REPO_ROOT / path
        if not full.is_file() or not _governed(path):
            continue
        text = full.read_text(encoding="utf-8", errors="replace")
        if path != STANDARD_PATH and MARKER not in text:
            continue
        checked.append(path)
        violations.extend(check_text(path, text))
    return {"base": resolved_base, "head": resolved_head, "baseSource": source,
            "checked": checked, "violations": violations}


def main() -> int:
    parser = argparse.ArgumentParser(description="CVF mixed-origin derived-synthesis absorption guard")
    parser.add_argument("--base")
    parser.add_argument("--head")
    parser.add_argument("--enforce", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = run_check(args.base, args.head)
    print("=== CVF Mixed-Origin Derived Synthesis Absorption Guard ===")
    print(f"Range: {result['base']}..{result['head']} ({result['baseSource']})")
    print(f"Checked artifacts: {len(result['checked'])}")
    print(f"Violations: {len(result['violations'])}")
    if args.json:
        print(json.dumps(result, indent=2))
    for item in result["violations"]:
        print(f"- {item['path']}: {item['type']} - {item['message']}")
    if result["violations"] and args.enforce:
        print("VIOLATION - mixed-origin derived-synthesis evidence is incomplete.")
        return 1
    print("COMPLIANT - mixed-origin derived-synthesis evidence is aligned.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

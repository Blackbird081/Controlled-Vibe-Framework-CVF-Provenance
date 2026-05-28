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
HOOK_CHAIN_PATH = "governance/compat/run_local_governance_hook_chain.py"
THIS_SCRIPT_PATH = "governance/compat/check_work_order_dispatch_quality.py"

REQUIRED_SOURCE_COLUMNS = (
    "Claimed item",
    "Source file",
    "Verified line/section",
    "Verified path or symbol",
    "Owning interface/function/schema",
    "Disposition",
)

PATH_RE = re.compile(
    r"`?((?:docs|governance|EXTENSIONS|CVF_SESSION|scripts|sdk|\.github)/[^`\s|)]+)`?"
)
LHW_RE = re.compile(r"LHW[-_]?(\d+)(?!\d)", re.IGNORECASE)


def _run_git(args: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
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


def _exists_rel(path: str) -> bool:
    normalized = path.strip().strip("`").replace("\\", "/").rstrip(".,;:")
    return bool(normalized) and (REPO_ROOT / normalized).exists()


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
    match = LHW_RE.search(f"{path}\n{text}")
    return int(match.group(1)) if match else None


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
    for match in PATH_RE.finditer(text):
        path = match.group(1).replace("\\", "/").rstrip(".,;:")
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


def _has_trace_matrix(text: str) -> bool:
    return re.search(r"Roadmap[- ]To[- ]Work[- ]Order Trace Matrix", text, re.IGNORECASE) is not None


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
            if len(raw_cells) >= len(headers):
                rows.append(dict(zip(headers, raw_cells)))
            index += 1
        continue
    return rows


def _source_table_has_required_columns(text: str) -> bool:
    tables = _parse_markdown_tables(text)
    if not tables:
        return False
    return all(column in tables[0] for column in REQUIRED_SOURCE_COLUMNS)


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


def _validate_required_first_reads(text: str) -> list[str]:
    issues: list[str] = []
    section = _extract_section(text, "Required First Reads")
    for path in _extract_paths(section):
        if not _exists_rel(path):
            issues.append(f"Required First Reads cites missing path `{path}`")
    return issues


def _validate_work_order(path: str, text: str) -> list[str]:
    issues: list[str] = []
    status = _extract_status(text)
    dispatching = "DISPATCHED" in status.upper() or "READY" in status.upper()
    issues.extend(_validate_status_token_hygiene(text, "work order"))
    issues.extend(_validate_closed_artifact_finality(text, "work order"))

    if dispatching and _is_roadmap_derived(text) and not _has_trace_matrix(text):
        issues.append("roadmap-derived work order is dispatch/ready without Roadmap-To-Work-Order Trace Matrix")

    if dispatching and _is_connector_wave(path, text):
        wave_id = _extract_wave_id(path, text)
        if wave_id is not None and not _has_gc018_for_wave(wave_id):
            issues.append(f"LHW{wave_id} connector work order is dispatch/ready without fresh GC-018 baseline")
        if "Source Verification" not in text or not _source_table_has_required_columns(text):
            issues.append("dispatch/ready work order lacks a complete Source Verification table")

    if dispatching:
        issues.extend(_validate_required_first_reads(text))
        blocking_precondition = re.search(
            r"(pre-?condition|gate condition|dispatch only after|only after)[\s\S]{0,240}CLOSED_PASS",
            text,
            re.IGNORECASE,
        )
        if blocking_precondition:
            issues.append("dispatch/ready status conflicts with unresolved CLOSED_PASS precondition language")
        issues.extend(_validate_ready_source_blockers(text))
        issues.extend(_validate_ready_live_method_proof_path(text))

    issues.extend(_validate_accepted_source_rows(path, text))
    issues.extend(_validate_no_empty_range_commands(text))

    if re.search(r"install[\s\S]{0,120}always blocked|always blocked[\s\S]{0,120}install", text, re.IGNORECASE):
        issues.append("work order asserts `install` is always blocked; cite a source policy or map it to approval/escalation")

    return issues


def _validate_roadmap(path: str, text: str) -> list[str]:
    issues: list[str] = []
    status = _extract_status(text)
    issues.extend(_validate_status_token_hygiene(text, "roadmap"))
    issues.extend(_validate_closed_artifact_finality(text, "roadmap"))
    issues.extend(_validate_closed_roadmap_status_residue(text))
    if _is_connector_wave(path, text) and _is_dispatch_status(status) and not _is_hold_status(status):
        wave_id = _extract_wave_id(path, text)
        if wave_id is not None and not _has_gc018_for_wave(wave_id):
            issues.append(f"LHW{wave_id} connector roadmap is dispatch/ready without fresh GC-018 baseline")
    issues.extend(_validate_accepted_source_rows(path, text))
    issues.extend(_validate_no_empty_range_commands(text))
    return issues


def _validate_baseline(path: str, text: str) -> list[str]:
    issues: list[str] = []
    issues.extend(_validate_status_token_hygiene(text, "baseline"))
    issues.extend(_validate_closed_artifact_finality(text, "baseline"))
    issues.extend(_validate_accepted_source_rows(path, text))
    issues.extend(_validate_no_empty_range_commands(text))
    return issues


def _validate_fast_lane_audit(path: str, text: str) -> list[str]:
    issues: list[str] = []
    status = _extract_status(text)
    issues.extend(_validate_status_token_hygiene(text, "fast-lane audit"))
    issues.extend(_validate_closed_artifact_finality(text, "fast-lane audit"))
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
    issues.extend(_validate_no_empty_range_commands(text))
    return issues


def _validate_completion_or_spec(path: str, text: str) -> list[str]:
    issues: list[str] = []
    issues.extend(_validate_status_token_hygiene(text, "completion/spec artifact"))
    issues.extend(_validate_closed_artifact_finality(text, "completion/spec artifact"))
    issues.extend(_validate_accepted_source_rows(path, text))
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


def _validate_lhw_wave_closure_range(changed_files: list[str]) -> list[dict[str, Any]]:
    normalized_files = sorted(path.replace("\\", "/") for path in changed_files)
    violations: list[dict[str, Any]] = []
    for path in normalized_files:
        if not path.startswith("docs/roadmaps/") or "/archive/" in path:
            continue
        text = _read_rel(path)
        if not text or not _is_closed_status(_extract_status(text)) or not _is_connector_wave(path, text):
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


def _classify(changed_files: list[str]) -> dict[str, Any]:
    targets = sorted(path.replace("\\", "/") for path in changed_files if _is_target(path))
    violations = []
    for path in targets:
        issues = _validate_path(path)
        if issues:
            violations.append({"path": path, "issues": issues})
    violations.extend(_validate_single_work_order_scope_range(changed_files))
    violations.extend(_validate_lhw_wave_closure_range(changed_files))

    required_markers = {
        STANDARD_PATH: (
            "Roadmap-To-Work-Order Trace Matrix",
            "Negative And Fail-Condition Scan",
            THIS_SCRIPT_PATH,
        ),
        WORK_ORDER_TEMPLATE_PATH: (
            "Source Verification Block",
            "Roadmap-To-Work-Order Trace Matrix",
            THIS_SCRIPT_PATH,
        ),
        HOOK_CHAIN_PATH: (THIS_SCRIPT_PATH,),
    }
    marker_violations: dict[str, list[str]] = {}
    for path, markers in required_markers.items():
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
    report = _classify(sorted(changed))
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

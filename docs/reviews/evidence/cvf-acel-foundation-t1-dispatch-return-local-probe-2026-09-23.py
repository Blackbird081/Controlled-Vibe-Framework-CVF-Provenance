#!/usr/bin/env python3
"""Independent Local probe for ACEL Foundation T1 dispatch/return controls."""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
COMPAT = REPO_ROOT / "governance" / "compat"
sys.path.insert(0, str(COMPAT))


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, COMPAT / f"{name}.py")
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


dispatch = load("check_work_order_dispatch_quality")
quality = load("check_worker_return_quality_gate")

work_order_rel = (
    "docs/work_orders/"
    "CVF_AGENT_WORK_ORDER_ACEL_FOUNDATION_T1_DISPATCH_RETURN_LOOP_CONTROL_2026-09-23.md"
)
work_order_text = (REPO_ROOT / work_order_rel).read_text(encoding="utf-8")

no_surface = "\n".join(
    (
        "# Probe",
        "Status: DISPATCH_READY",
        "Commit mode: WORKER_MUST_NOT_COMMIT",
    )
)
no_surface_issues = dispatch._validate_ready_manifest_and_return_binding(no_surface)
actual_issues = dispatch._validate_ready_manifest_and_return_binding(work_order_text)
active = quality.diagnose_active_work_order(work_order_rel)

with tempfile.TemporaryDirectory() as temp:
    temp_root = Path(temp)
    missing_order = "docs/work_orders/CVF_PROBE_MISSING_RETURN.md"
    missing_return = "docs/reviews/CVF_PROBE_MISSING_RETURN.md"
    order_path = temp_root / missing_order
    order_path.parent.mkdir(parents=True)
    order_path.write_text(
        "\n".join(
            (
                "# Probe",
                f"Worker return path: `{missing_return}`",
                f"workerReturnPath: `{missing_return}`",
            )
        ),
        encoding="utf-8",
    )
    original_root = quality.REPO_ROOT
    quality.REPO_ROOT = temp_root
    try:
        missing = quality.diagnose_active_work_order(missing_order)
        escape = quality.diagnose_active_work_order("../outside.md")
    finally:
        quality.REPO_ROOT = original_root

stale = work_order_text.replace(
    "--base <executionBaseHead> --head HEAD --enforce",
    "--base dc935676838b08754a6b26d0a13813128df24785 --head HEAD --enforce",
    1,
)
stale_issues = dispatch._validate_stale_preclosure_dispatch_base(stale)
current_issues = dispatch._validate_stale_preclosure_dispatch_base(work_order_text)

assertions = {
    "no_surface_has_three_exact_failures": len(no_surface_issues) == 3,
    "actual_work_order_manifest_binding_clean": actual_issues == [],
    "actual_exact_return_clean": active.eligible and active.issues == (),
    "missing_exact_return_fails_closed": any("absent" in issue for issue in missing.issues),
    "containment_escape_rejected": any("repo-contained" in issue for issue in escape.issues),
    "dispatch_base_reuse_rejected": any("executionBaseHead" in issue for issue in stale_issues),
    "execution_base_command_accepted": current_issues == [],
}

print(json.dumps(assertions, indent=2, sort_keys=True))
raise SystemExit(0 if all(assertions.values()) else 1)

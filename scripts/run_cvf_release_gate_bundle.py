#!/usr/bin/env python3
"""
CVF Release Gate Bundle — 2026-04-21
Runs all release-readiness checks in sequence.

Release-quality governance proof requires live provider execution. Mock mode is
valid only for UI structure checks and saved provider-readiness receipts.

Usage:
  python scripts/run_cvf_release_gate_bundle.py
  python scripts/run_cvf_release_gate_bundle.py --mock
  python scripts/run_cvf_release_gate_bundle.py --dry-run
  python scripts/run_cvf_release_gate_bundle.py --json
  python scripts/run_cvf_release_gate_bundle.py --json --output cvf-release-gate-result.json --manifest-output cvf-release-gate-manifest.json
  python scripts/run_cvf_release_gate_bundle.py --e2e
  python scripts/run_cvf_release_gate_bundle.py --e2e-live

Flags:
  --mock      Use saved receipts for provider readiness; live governance E2E remains mandatory in the default gate
  --dry-run   Print what would run without executing anything
  --json      Machine-readable output
  --output    Write the machine-readable gate result to a JSON file
  --manifest-output  Write a live evidence manifest for the output JSON file
  --e2e       Targeted run: UI-only mock Playwright specs
  --e2e-live  Targeted run: live governance Playwright specs; requires a DashScope-compatible live key

Exit codes:
  0  All checks PASS (warnings allowed)
  1  One or more checks FAIL
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path
from types import SimpleNamespace

from build_cvf_live_evidence_manifest import build_manifest as build_live_evidence_manifest
from _local_env import bootstrap_repo_env

REPO_ROOT = Path(__file__).parent.parent
CVF_WEB = REPO_ROOT / "EXTENSIONS" / "CVF_v1.6_AGENT_PLATFORM" / "cvf-web"
GUARD_CONTRACT = REPO_ROOT / "EXTENSIONS" / "CVF_GUARD_CONTRACT"
PROVIDER_READINESS = REPO_ROOT / "scripts" / "check_cvf_provider_release_readiness.py"
SOT3_A5_ADAPTER = REPO_ROOT / "scripts" / "run_cvf_sot3_a5_release_proof.py"

# Fields that must be present with a required value for a SOT3 payload to be
# admitted as PASS-supporting. Mirrors the accepted A4 denominators; kept in
# sync with run_cvf_sot3_a5_release_proof.py's own admission logic, which is
# the actual source of truth for the underlying provider-call/owner-array
# validation. This dict only checks that the projected top-level fields the
# release JSON depends on are present and hold their required shape/value.
SOT3_REQUIRED_FIELD_CHECKS: list[tuple[str, object]] = [
    ("localNegativeGatePassed", True),
    ("negativeCaseCount", 19),
    ("zeroProviderCallCaseCount", 18),
    ("rollbackProviderCallCount", 1),
    ("recoveryProviderCallCount", 1),
    ("approvedContextIncluded", True),
    ("durableOwnerCorrelationComplete", True),
    ("httpStatus", 200),
]

# Required docs for the docs governance check
REQUIRED_DOCS = [
    REPO_ROOT / "docs" / "reference" / "CVF_RELEASE_CANDIDATE_TRUTH_PACKET_2026-04-21.md",
    REPO_ROOT / "docs" / "reference" / "CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md",
    REPO_ROOT / "docs" / "guides" / "CVF_DEMO_SCRIPT_2026-04-21.md",
]

# Patterns that indicate a committed secret
SECRET_PATTERNS = [
    r"sk-[A-Za-z0-9]{20,}",                 # OpenAI / Anthropic-style keys
    r"DASHSCOPE_API_KEY\s*=\s*['\"][^'\"]+", # Alibaba DashScope inline value
    r"DEEPSEEK_API_KEY\s*=\s*['\"][^'\"]+",  # DeepSeek inline value
    r"api[_-]?key\s*=\s*['\"][A-Za-z0-9_\-]{16,}['\"]",  # generic api_key = "..."
    r"-----BEGIN (RSA|EC|OPENSSH) PRIVATE KEY-----",      # private keys
    r"ghp_[A-Za-z0-9]{36}",                 # GitHub personal access token
    r"ANTHROPIC_API_KEY\s*=\s*['\"][^'\"]+", # Anthropic inline value
]

# Files/dirs to skip in secrets scan
SCAN_SKIP = {
    ".git", "node_modules", "__pycache__", ".next", "dist", "build",
    "coverage", ".nyc_output", "docs/audits", ".claude",  # receipts/local tool state contain masked or local keys
}

SCAN_EXTENSIONS = {".py", ".ts", ".tsx", ".js", ".jsx", ".env", ".json", ".md", ".yaml", ".yml", ".sh"}


def bootstrap_live_provider_env() -> None:
    bootstrap_repo_env()
    if os.environ.get("DASHSCOPE_API_KEY"):
        return
    for alias in ("ALIBABA_API_KEY", "CVF_ALIBABA_API_KEY", "CVF_BENCHMARK_ALIBABA_KEY"):
        value = os.environ.get(alias, "").strip()
        if value:
            os.environ["DASHSCOPE_API_KEY"] = value
            return


@dataclass
class CheckResult:
    name: str
    status: str          # PASS | WARN | FAIL | SKIP
    message: str
    detail: list[str] = field(default_factory=list)


def run_cmd(cmd: list[str], cwd: Path | None = None, timeout: int = 300) -> tuple[int, str, str]:
    try:
        r = subprocess.run(
            platform_cmd(cmd),
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return 1, "", "Command timed out"
    except Exception as e:
        return 1, "", str(e)


def platform_cmd(cmd: list[str]) -> list[str]:
    if os.name != "nt" or not cmd:
        return cmd
    exe = shutil.which(cmd[0])
    if exe:
        return [exe, *cmd[1:]]
    cmd_exe = shutil.which(f"{cmd[0]}.cmd")
    if cmd_exe:
        return [cmd_exe, *cmd[1:]]
    return cmd


def is_allowed_secret_line(path: Path, line: str) -> bool:
    lowered = line.lower()
    rel = path.relative_to(REPO_ROOT)
    parts = {p.lower() for p in rel.parts}

    if "tests" in parts or ".test." in path.name.lower() or path.name.lower().endswith(".spec.ts"):
        return True

    placeholder_markers = [
        "<your", "your-", "your_", "your_key", "your-key", "xxx", "...",
        "test-key", "dummy", "placeholder", "secret-123", "ds-key", "claude-key",
    ]
    return any(marker in lowered for marker in placeholder_markers)


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------

def check_web_build(dry_run: bool) -> CheckResult:
    name = "Web build (npm run build)"
    if dry_run:
        return CheckResult(name, "SKIP", "dry-run — would run: npm run build", [str(CVF_WEB)])
    if not CVF_WEB.exists():
        _LAST_E2E_DIAGNOSTIC = {
            "stage": "e2e_execution",
            "class": "dependency_unavailable",
            "retryable": False,
            "userAction": "restore_cvf_web_workspace",
            "safeMessage": "The cvf-web workspace was not available to the release runner.",
            "provider": None,
            "model": None,
            "httpStatus": None,
            "latencyMs": None,
            "traceOrReceipt": None,
        }
        return CheckResult(name, "FAIL", "cvf-web directory not found", [str(CVF_WEB)])
    code, stdout, stderr = run_cmd(["npm", "run", "build"], cwd=CVF_WEB, timeout=900)
    if code == 0:
        return CheckResult(name, "PASS", "Build succeeded")
    lines = (stdout + stderr).splitlines()
    errors = [l for l in lines if "error" in l.lower() or "Error" in l][:10]
    return CheckResult(name, "FAIL", "Build failed", errors or lines[-10:])


def check_ts_typecheck(dry_run: bool) -> CheckResult:
    name = "TypeScript check (guard contract)"
    if dry_run:
        return CheckResult(name, "SKIP", "dry-run — would run: npm run check", [str(GUARD_CONTRACT)])
    if not GUARD_CONTRACT.exists():
        return CheckResult(name, "FAIL", "CVF_GUARD_CONTRACT directory not found")
    code, stdout, stderr = run_cmd(["npm", "run", "check"], cwd=GUARD_CONTRACT, timeout=120)
    if code == 0:
        return CheckResult(name, "PASS", "TypeScript check clean")
    lines = (stdout + stderr).splitlines()
    errors = [l for l in lines if "error" in l.lower()][:10]
    return CheckResult(name, "FAIL", "TypeScript errors found", errors or lines[-10:])


def check_provider_readiness(dry_run: bool, mock: bool) -> CheckResult:
    name = "Provider readiness"
    if dry_run:
        return CheckResult(name, "SKIP", "dry-run — would run: check_cvf_provider_release_readiness.py --json")
    if not PROVIDER_READINESS.exists():
        return CheckResult(name, "FAIL", "Provider readiness script not found")
    code, stdout, stderr = run_cmd(
        [sys.executable, str(PROVIDER_READINESS), "--json"], timeout=30
    )
    if code != 0:
        return CheckResult(name, "FAIL", "Provider readiness evaluator failed", stderr.splitlines()[:5])
    try:
        data = json.loads(stdout)
        certified = data.get("certified_count", 0)
        canary = data.get("canary_pass_count", 0)
        status = data.get("status", "UNKNOWN")
        if certified > 0:
            return CheckResult(name, "PASS", f"CERTIFIED lanes: {certified} — status: {status}")
        elif canary > 0:
            return CheckResult(name, "WARN", f"No CERTIFIED lane; {canary} CANARY_PASS lane(s). Multi-provider operability proven.")
        else:
            return CheckResult(name, "FAIL", "No lane has passed a full canary")
    except json.JSONDecodeError:
        return CheckResult(name, "FAIL", "Provider readiness output is not valid JSON", stdout.splitlines()[:5])


def check_secrets(dry_run: bool) -> CheckResult:
    name = "Secrets scan"
    if dry_run:
        return CheckResult(name, "SKIP", f"dry-run — would scan {REPO_ROOT} for secret patterns")

    compiled = [re.compile(p) for p in SECRET_PATTERNS]
    hits: list[str] = []

    for path in REPO_ROOT.rglob("*"):
        # Skip irrelevant dirs
        if any(skip in path.parts for skip in SCAN_SKIP):
            continue
        if not path.is_file():
            continue
        if path.suffix not in SCAN_EXTENSIONS:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for line_no, line in enumerate(text.splitlines(), 1):
            for pat in compiled:
                if pat.search(line):
                    if is_allowed_secret_line(path, line):
                        continue
                    rel = path.relative_to(REPO_ROOT)
                    hits.append(f"{rel}:{line_no}")
                    break
        if len(hits) >= 20:
            break

    if hits:
        return CheckResult(name, "FAIL", f"Potential secrets found in {len(hits)} location(s)", hits)
    return CheckResult(name, "PASS", "No secret patterns detected")


_LAST_E2E_DIAGNOSTIC: dict | None = None


def build_e2e_diagnostic(output: str, mode: str, latency_ms: int | None = None) -> dict:
    """Classify an E2E failure without retaining provider output or secrets."""
    lowered = output.lower()
    http_match = re.search(r"(?:http(?: status)?|status)\D{0,8}(\d{3})", lowered)
    http_status = int(http_match.group(1)) if http_match else None

    if "cannot resolve" in lowered or "module not found" in lowered:
        failure_class = "dependency_resolution_failed"
        retryable = True
        user_action = "repair_dependency_resolution_then_retry"
        safe_message = "The E2E route did not compile because a dependency import could not be resolved."
    elif "timed out" in lowered or "timeout" in lowered:
        failure_class = "timeout"
        retryable = True
        user_action = "classify_timeout_stage_then_retry"
        safe_message = "The E2E run exceeded its bounded timeout."
    elif "no dashscope-compatible live key" in lowered:
        failure_class = "credential_unavailable"
        retryable = False
        user_action = "provide_operator_managed_live_key"
        safe_message = "A DashScope-compatible live key was not available to the release runner."
    else:
        failure_class = "e2e_failed"
        retryable = False
        user_action = "inspect_secret_safe_test_artifacts_before_retry"
        safe_message = f"The {mode} E2E suite failed; inspect the retained test artifacts before retrying."

    return {
        "stage": "e2e_execution",
        "class": failure_class,
        "retryable": retryable,
        "userAction": user_action,
        "safeMessage": safe_message,
        "provider": "alibaba" if mode == "live governance" else None,
        "model": None,
        "httpStatus": http_status,
        "latencyMs": latency_ms,
        "traceOrReceipt": None,
    }


def check_e2e(dry_run: bool, live: bool) -> CheckResult:
    global _LAST_E2E_DIAGNOSTIC
    mode = "live governance" if live else "UI mock"
    config = "playwright.config.ts" if live else "playwright.config.mock.ts"
    specs = [
        "tests/e2e/noncoder-governance-live.spec.ts",
        "tests/e2e/governance-gate-live.spec.ts",
        "tests/e2e/w113-workspace-web-live-proof.spec.ts",
    ] if live else [
        "tests/e2e/admin-rbac.spec.ts",
        "tests/e2e/provider-lane-ui.spec.ts",
    ]
    name = "E2E Playwright Governance (live)" if live else "E2E Playwright UI (mock)"
    if dry_run:
        cmd_str = f"npx playwright test --config {config} {' '.join(specs)} --reporter=line"
        return CheckResult(name, "SKIP", f"dry-run — would run: {cmd_str}", [str(CVF_WEB)])
    if not CVF_WEB.exists():
        _LAST_E2E_DIAGNOSTIC = build_e2e_diagnostic(
            "cvf-web workspace not found", mode
        )
        return CheckResult(name, "FAIL", "cvf-web directory not found", [str(CVF_WEB)])
    if live:
        bootstrap_live_provider_env()
    if live and not os.environ.get("DASHSCOPE_API_KEY"):
        message = "No DashScope-compatible live key set - live governance E2E is mandatory for release-quality CVF proof"
        _LAST_E2E_DIAGNOSTIC = build_e2e_diagnostic(message, mode)
        return CheckResult(
            name, "FAIL",
            message
        )
    cmd = ["npx", "playwright", "test", "--config", config, *specs, "--reporter=line"]
    started = time.monotonic()
    code, stdout, stderr = run_cmd(cmd, cwd=CVF_WEB, timeout=600)
    latency_ms = round((time.monotonic() - started) * 1000)
    output = (stdout + stderr).strip()
    lines = output.splitlines()
    summary = next((l for l in reversed(lines) if l.strip()), "")
    if code == 0:
        return CheckResult(name, "PASS", f"Playwright {mode} suite passed", [summary] if summary else [])
    # No automatic blind retry. Return the first failure and a diagnostic
    # summary; a later rerun may only happen after a human/worker records an
    # explicit result-changing action outside this bundle (per the A5 work
    # order's no-blind-retry requirement).
    _LAST_E2E_DIAGNOSTIC = build_e2e_diagnostic(output, mode, latency_ms)
    failures = [l for l in lines if "failed" in l.lower() or "error" in l.lower()][:8]
    return CheckResult(name, "FAIL", f"Playwright {mode} suite failed", failures or lines[-8:])


def check_docs_governance() -> CheckResult:
    name = "Docs governance (RC docs present)"
    missing = [str(d.relative_to(REPO_ROOT)) for d in REQUIRED_DOCS if not d.exists()]
    if missing:
        return CheckResult(name, "FAIL", f"{len(missing)} required RC doc(s) missing", missing)
    return CheckResult(name, "PASS", f"All {len(REQUIRED_DOCS)} required RC docs present")


def call_sot3_a5_adapter(output_path: Path, diagnostic_path: Path) -> tuple[dict | None, int]:
    """Invokes scripts/run_cvf_sot3_a5_release_proof.py --run as a subprocess.

    Returns (parsed_result_json_or_None, returncode). This is the only call
    site for the SOT3 A5 adapter; the release bundle never invokes Vitest or
    the provider route directly itself -- the adapter (which in turn invokes
    only the accepted A4 runner) owns that chain.
    """
    cmd = [
        sys.executable,
        str(SOT3_A5_ADAPTER),
        "--run",
        "--json",
        "--output", str(output_path),
        "--diagnostic-output", str(diagnostic_path),
    ]
    code, stdout, stderr = run_cmd(cmd, cwd=REPO_ROOT, timeout=600)
    try:
        data = json.loads(output_path.read_text(encoding="utf-8")) if output_path.exists() else None
    except (OSError, ValueError, json.JSONDecodeError):
        data = None
    return data, code


_LAST_SOT3_PAYLOAD: dict | None = None


def check_sot3(dry_run: bool, diagnostic_output: Path | None = None) -> CheckResult:
    """Mandatory SOT3 canonical release proof check.

    Only `--dry-run` may mark this SKIP. `--mock` has no effect on this
    check at all -- there is no mock-bypass parameter -- so `--mock` cannot
    cause SOT3 to report PASS without a real adapter invocation.

    The parsed `sot3` payload (or a secret-safe absent/malformed marker) is
    cached in the module-level `_LAST_SOT3_PAYLOAD` so `main()` can project it
    as a top-level `sot3` object in the release JSON without re-running the
    adapter a second time. When `diagnostic_output` is provided, the A5
    adapter's own secret-safe diagnostic is persisted there (for both PASS
    and FAIL) so it can also be hashed into the live evidence manifest.
    """
    global _LAST_SOT3_PAYLOAD
    name = "SOT3 canonical release proof (A5)"
    if dry_run:
        _LAST_SOT3_PAYLOAD = {"overall": "SKIP", "reason": "dry_run"}
        return CheckResult(
            name, "SKIP",
            "dry-run - would run: python scripts/run_cvf_sot3_a5_release_proof.py --run --json",
            [str(SOT3_A5_ADAPTER)],
        )
    if not SOT3_A5_ADAPTER.exists():
        _LAST_SOT3_PAYLOAD = {"overall": "FAIL", "reason": "adapter_script_not_found"}
        return CheckResult(name, "FAIL", "SOT3 A5 adapter script not found", [str(SOT3_A5_ADAPTER)])

    with tempfile.TemporaryDirectory(prefix="cvf-release-sot3-") as tmp:
        output_path = Path(tmp) / "sot3-a5-result.json"
        tmp_diagnostic_path = Path(tmp) / "sot3-a5-diagnostic.json"
        data, code = call_sot3_a5_adapter(output_path, tmp_diagnostic_path)
        if diagnostic_output is not None and tmp_diagnostic_path.exists():
            diagnostic_output.parent.mkdir(parents=True, exist_ok=True)
            diagnostic_output.write_text(tmp_diagnostic_path.read_text(encoding="utf-8"), encoding="utf-8")

    if data is None or "sot3" not in data or not isinstance(data.get("sot3"), dict):
        _LAST_SOT3_PAYLOAD = {"overall": "FAIL", "reason": "missing_or_malformed_payload", "adapterReturnCode": code}
        return CheckResult(name, "FAIL", "SOT3 payload missing or malformed", [f"adapter returncode={code}"])

    sot3 = data["sot3"]
    _LAST_SOT3_PAYLOAD = sot3

    if sot3.get("overall") != "PASS":
        admission_failures = sot3.get("admissionFailures") or []
        return CheckResult(name, "FAIL", "SOT3 proof did not PASS", admission_failures[:8] or [f"overall={sot3.get('overall')}"])

    mismatches = [
        f"{field}!={expected}(got {sot3.get(field)!r})"
        for field, expected in SOT3_REQUIRED_FIELD_CHECKS
        if sot3.get(field) != expected
    ]
    if mismatches:
        return CheckResult(name, "FAIL", "SOT3 payload failed strict field admission", mismatches[:8])

    return CheckResult(name, "PASS", "SOT3 canonical release proof PASS with full owner correlation", [])


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

ICONS = {"PASS": "PASS", "WARN": "WARN", "FAIL": "FAIL", "SKIP": "SKIP"}
BAR = "=" * 68


def print_results(results: list[CheckResult], date: str) -> int:
    print(f"\n{BAR}")
    print(f"  CVF RELEASE GATE BUNDLE — {date}")
    print(BAR)

    for r in results:
        icon = ICONS[r.status]
        print(f"  [{icon:<4}] {r.name}")
        print(f"         {r.message}")
        for d in r.detail[:5]:
            print(f"           {d}")

    print(f"\n{'-' * 68}")
    passes = sum(1 for r in results if r.status == "PASS")
    warns = sum(1 for r in results if r.status == "WARN")
    fails = sum(1 for r in results if r.status == "FAIL")
    skips = sum(1 for r in results if r.status == "SKIP")
    print(f"  PASS: {passes}  WARN: {warns}  FAIL: {fails}  SKIP: {skips}")
    if fails:
        print(f"\n  GATE RESULT: FAIL ({fails} check(s) failed)")
    elif warns:
        print(f"\n  GATE RESULT: PASS ({warns} warning(s))")
    else:
        print(f"\n  GATE RESULT: PASS")
    print(BAR + "\n")
    return 1 if fails else 0


def result_payload(results: list[CheckResult], date: str, sot3: dict | None = None) -> dict:
    """Builds the machine-readable release JSON payload.

    `sot3` is the top-level SOT3 evidence object. A missing, malformed, or
    non-PASS SOT3 payload always makes `gate_result` FAIL, independent of
    every other check's status -- including the dry-run case, where SOT3 is
    SKIP and can never support a PASS claim. Callers that omit `sot3`
    entirely (legacy call shape) are treated as a missing payload only when
    a SOT3-named check is present in `results`; when no SOT3-related check is
    part of this payload at all (a caller building a non-release, non-SOT3
    payload shape), `sot3` is omitted from gate-result computation.
    """
    fails = sum(1 for r in results if r.status == "FAIL")
    has_sot3_check = any(r.name.startswith("SOT3") for r in results)

    sot3_payload = sot3
    if sot3_payload is None and has_sot3_check:
        sot3_payload = {"overall": "ABSENT", "reason": "sot3_payload_not_provided"}

    sot3_blocks_pass = False
    if has_sot3_check or sot3_payload is not None:
        sot3_blocks_pass = not (isinstance(sot3_payload, dict) and sot3_payload.get("overall") == "PASS")

    gate_result = "FAIL" if (fails or sot3_blocks_pass) else "PASS"

    payload: dict = {
        "date": date,
        "gate_result": gate_result,
        "checks": [
            {"name": r.name, "status": r.status, "message": r.message, "detail": r.detail}
            for r in results
        ],
    }
    if sot3_payload is not None:
        payload["sot3"] = sot3_payload
    return payload


def write_json_payload(payload: dict, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def build_secret_safe_rerun_command(args: argparse.Namespace) -> str:
    parts = ["python", "scripts/run_cvf_release_gate_bundle.py"]
    if args.mock:
        parts.append("--mock")
    if args.dry_run:
        parts.append("--dry-run")
    if args.e2e:
        parts.append("--e2e")
    if args.e2e_live:
        parts.append("--e2e-live")
    if getattr(args, "sot3_diagnostic_output", None):
        parts.append("--sot3-diagnostic-output <path>")
    if getattr(args, "e2e_diagnostic_output", None):
        parts.append("--e2e-diagnostic-output <path>")
    parts.append("--json")
    return " ".join(parts)


def write_live_evidence_manifest(
    evidence_paths: list[Path],
    manifest_path: Path,
    rerun_command: str,
    anchor_id: str,
    anchor_url: str,
) -> None:
    """Hashes every path in `evidence_paths` into one manifest.

    When both the release result JSON and the SOT3 A5 diagnostic JSON are
    supplied (`--output` and `--sot3-diagnostic-output` both present), the
    manifest hashes both artifacts, not just one.
    """
    manifest = build_live_evidence_manifest(
        SimpleNamespace(
            evidence=[str(p) for p in evidence_paths],
            command=rerun_command,
            anchor_id=anchor_id,
            anchor_url=anchor_url,
        )
    )
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def json_output(payload: dict) -> int:
    fails = 1 if payload["gate_result"] == "FAIL" else 0
    print(json.dumps(payload, indent=2))
    return 1 if fails else 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="CVF Release Gate Bundle")
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Use saved provider readiness receipts; live governance E2E remains mandatory in the default gate",
    )
    parser.add_argument("--dry-run", action="store_true", dest="dry_run", help="Print what would run without executing")
    parser.add_argument("--json", action="store_true", dest="json_out", help="Machine-readable JSON output")
    parser.add_argument("--output", type=Path, help="Write the machine-readable gate result to a JSON file")
    parser.add_argument(
        "--manifest-output",
        type=Path,
        help="Write a live evidence manifest for the JSON output file",
    )
    parser.add_argument("--manifest-anchor-id", default="", help="Optional external immutable anchor identifier")
    parser.add_argument("--manifest-anchor-url", default="", help="Optional external immutable anchor URL")
    parser.add_argument(
        "--sot3-diagnostic-output",
        type=Path,
        help="Write the SOT3 A5 secret-safe diagnostic to this JSON path; also hashed into the manifest when --manifest-output is supplied",
    )
    parser.add_argument(
        "--e2e-diagnostic-output",
        type=Path,
        help="Write the secret-safe E2E failure diagnostic, or JSON null on success; also hash it into the evidence manifest",
    )
    parser.add_argument("--e2e", action="store_true", dest="e2e", help="Targeted run: UI-only mock Playwright specs")
    parser.add_argument(
        "--e2e-live",
        action="store_true",
        dest="e2e_live",
        help="Targeted run: live governance Playwright specs (requires a DashScope-compatible live key)",
    )
    args = parser.parse_args()
    if args.manifest_output and not args.output:
        parser.error("--manifest-output requires --output so the manifest has a concrete evidence artifact")

    from datetime import date
    today = date.today().isoformat()

    if args.dry_run and not args.json_out:
        print(f"\nCVF Release Gate Bundle — DRY RUN ({today})")
        print("The following checks would run:\n")

    results: list[CheckResult] = [
        check_web_build(args.dry_run),
        check_ts_typecheck(args.dry_run),
        check_provider_readiness(args.dry_run, args.mock),
        check_secrets(args.dry_run),
        check_docs_governance(),
    ]

    if args.e2e:
        results.append(check_e2e(args.dry_run, live=False))
    if args.e2e_live:
        results.append(check_e2e(args.dry_run, live=True))
    if not args.e2e and not args.e2e_live:
        results.append(check_e2e(args.dry_run, live=False))
        results.append(check_e2e(args.dry_run, live=True))

    # SOT3 is a mandatory check in the default canonical release path. It is
    # appended once per run regardless of --e2e/--e2e-live scoping; only
    # --dry-run marks it SKIP, and --mock has no bypass effect on it at all.
    results.append(check_sot3(args.dry_run, diagnostic_output=args.sot3_diagnostic_output))

    payload = result_payload(results, today, sot3=_LAST_SOT3_PAYLOAD)
    if args.output:
        write_json_payload(payload, args.output)
    if args.e2e_diagnostic_output:
        args.e2e_diagnostic_output.parent.mkdir(parents=True, exist_ok=True)
        args.e2e_diagnostic_output.write_text(
            json.dumps(_LAST_E2E_DIAGNOSTIC, indent=2) + "\n",
            encoding="utf-8",
        )
    if args.manifest_output:
        evidence_paths = [args.output]
        if args.sot3_diagnostic_output and Path(args.sot3_diagnostic_output).exists():
            evidence_paths.append(args.sot3_diagnostic_output)
        if args.e2e_diagnostic_output and Path(args.e2e_diagnostic_output).exists():
            evidence_paths.append(args.e2e_diagnostic_output)
        write_live_evidence_manifest(
            evidence_paths,
            args.manifest_output,
            build_secret_safe_rerun_command(args),
            args.manifest_anchor_id,
            args.manifest_anchor_url,
        )

    if args.json_out:
        sys.exit(json_output(payload))
    else:
        sys.exit(print_results(results, today))


if __name__ == "__main__":
    main()

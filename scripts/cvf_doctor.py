#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path

from _local_env import bootstrap_repo_env


REPO_ROOT = Path(__file__).resolve().parent.parent
CVF_WEB = REPO_ROOT / "EXTENSIONS" / "CVF_v1.6_AGENT_PLATFORM" / "cvf-web"


@dataclass
class DoctorCheck:
    id: str
    status: str
    classification: str
    message: str
    detail: str = ""
    remediation: str = ""


def command_version(command: str, args: list[str]) -> tuple[bool, str]:
    exe = shutil.which(command)
    if not exe:
        return False, ""
    try:
        result = subprocess.run(
            [exe, *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
        )
    except Exception:
        return True, "version check failed"
    output = (result.stdout or result.stderr).strip().splitlines()
    return True, output[0] if output else ""


def is_port_listening(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.2)
        return sock.connect_ex(("127.0.0.1", port)) == 0


def path_writable(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        with tempfile.NamedTemporaryFile(prefix=".cvf-doctor-", dir=path, delete=True):
            return True
    except Exception:
        return False


def has_any_env_key(names: list[str]) -> bool:
    return any(os.environ.get(name, "").strip() for name in names)


def build_checks() -> list[DoctorCheck]:
    checks: list[DoctorCheck] = []

    node_ok, node_version = command_version("node", ["--version"])
    checks.append(DoctorCheck(
        "node_available",
        "PASS" if node_ok else "FAIL",
        "OPTIONAL" if node_ok else "BLOCKER",
        "Node is available." if node_ok else "Node is not available on PATH.",
        node_version,
        "Install Node.js before running cvf-web." if not node_ok else "",
    ))

    npm_ok, npm_version = command_version("npm", ["--version"])
    checks.append(DoctorCheck(
        "npm_available",
        "PASS" if npm_ok else "FAIL",
        "OPTIONAL" if npm_ok else "BLOCKER",
        "npm is available." if npm_ok else "npm is not available on PATH.",
        npm_version,
        "Install npm before running cvf-web." if not npm_ok else "",
    ))

    python_ok, python_version = command_version(sys.executable, ["--version"])
    checks.append(DoctorCheck(
        "python_available",
        "PASS" if python_ok else "FAIL",
        "OPTIONAL" if python_ok else "BLOCKER",
        "Python is available.",
        python_version,
    ))

    required_paths = [
        ("repo_root", REPO_ROOT, "Repository root exists."),
        ("cvf_web_dir", CVF_WEB, "cvf-web directory exists."),
        ("cvf_web_package_json", CVF_WEB / "package.json", "cvf-web package.json exists."),
        ("cvf_web_package_lock", CVF_WEB / "package-lock.json", "cvf-web package-lock.json exists."),
        ("governance_dir", REPO_ROOT / "governance", "governance directory exists."),
        ("extensions_dir", REPO_ROOT / "EXTENSIONS", "EXTENSIONS directory exists."),
        ("release_gate_script", REPO_ROOT / "scripts" / "run_cvf_release_gate_bundle.py", "Release gate script exists."),
    ]
    for check_id, path, message in required_paths:
        exists = path.exists()
        checks.append(DoctorCheck(
            check_id,
            "PASS" if exists else "FAIL",
            "OPTIONAL" if exists else "BLOCKER",
            message if exists else f"Missing required path: {path.relative_to(REPO_ROOT)}",
            str(path.relative_to(REPO_ROOT)) if path.exists() else "",
        ))

    env_example = CVF_WEB / ".env.example"
    checks.append(DoctorCheck(
        "cvf_web_env_example",
        "PASS" if env_example.exists() else "FAIL",
        "OPTIONAL" if env_example.exists() else "BLOCKER",
        ".env.example is available for local setup." if env_example.exists() else "cvf-web .env.example is missing.",
        str(env_example.relative_to(REPO_ROOT)),
        "Add a tracked env template or update setup docs to a tracked template path." if not env_example.exists() else "",
    ))

    env_local = CVF_WEB / ".env.local"
    checks.append(DoctorCheck(
        "cvf_web_env_local",
        "PASS" if env_local.exists() else "WARN",
        "OPTIONAL" if env_local.exists() else "WARNING",
        ".env.local exists." if env_local.exists() else ".env.local is not present.",
        str(env_local.relative_to(REPO_ROOT)),
        "Copy .env.example to .env.local and fill only the keys you want to use." if not env_local.exists() else "",
    ))

    node_modules = CVF_WEB / "node_modules"
    checks.append(DoctorCheck(
        "cvf_web_node_modules",
        "PASS" if node_modules.exists() else "WARN",
        "OPTIONAL" if node_modules.exists() else "WARNING",
        "cvf-web dependencies appear installed." if node_modules.exists() else "cvf-web node_modules is absent.",
        str(node_modules.relative_to(REPO_ROOT)),
        "Run npm ci inside EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web." if not node_modules.exists() else "",
    ))

    for port in (3000, 3001):
        busy = is_port_listening(port)
        checks.append(DoctorCheck(
            f"port_{port}",
            "WARN" if busy else "PASS",
            "WARNING" if busy else "OPTIONAL",
            f"Port {port} is already listening." if busy else f"Port {port} is free.",
            "",
            "Stop the existing process or choose a different port." if busy else "",
        ))

    checks.append(DoctorCheck(
        "repo_root_writable",
        "PASS" if path_writable(REPO_ROOT) else "FAIL",
        "OPTIONAL" if path_writable(REPO_ROOT) else "BLOCKER",
        "Repository root is writable." if path_writable(REPO_ROOT) else "Repository root is not writable.",
    ))
    checks.append(DoctorCheck(
        "cvf_web_writable",
        "PASS" if path_writable(CVF_WEB) else "FAIL",
        "OPTIONAL" if path_writable(CVF_WEB) else "BLOCKER",
        "cvf-web directory is writable." if path_writable(CVF_WEB) else "cvf-web directory is not writable.",
    ))

    provider_present = has_any_env_key([
        "DASHSCOPE_API_KEY",
        "ALIBABA_API_KEY",
        "CVF_ALIBABA_API_KEY",
        "CVF_BENCHMARK_ALIBABA_KEY",
        "DEEPSEEK_API_KEY",
    ])
    checks.append(DoctorCheck(
        "provider_key_presence",
        "PASS" if provider_present else "WARN",
        "OPTIONAL" if provider_present else "WARNING",
        "At least one supported provider key is present in process env." if provider_present else "No supported provider key detected in process env.",
        "secret values are never printed",
        "Use cvf_provider_check.py for secret-safe provider readiness." if not provider_present else "",
    ))

    return checks


def summarize(checks: list[DoctorCheck]) -> str:
    if any(c.status == "FAIL" and c.classification == "BLOCKER" for c in checks):
        return "BLOCKED"
    if any(c.status == "WARN" for c in checks):
        return "WARN"
    return "PASS"


def main() -> int:
    parser = argparse.ArgumentParser(description="CVF fresh-clone/runtime readiness doctor.")
    parser.add_argument("--json", action="store_true", help="Output JSON.")
    args = parser.parse_args()

    loaded_env_files = bootstrap_repo_env()
    checks = build_checks()
    status = summarize(checks)
    payload = {
        "status": status,
        "repo_root": str(REPO_ROOT),
        "cvf_web": str(CVF_WEB),
        "loaded_env_files": [str(path.relative_to(REPO_ROOT)) for path in loaded_env_files],
        "checks": [asdict(check) for check in checks],
    }

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"CVF Doctor: {status}")
        for check in checks:
            line = f"[{check.status}] {check.id}: {check.message}"
            print(line)
            if check.remediation:
                print(f"  -> {check.remediation}")

    return 1 if status == "BLOCKED" else 0


if __name__ == "__main__":
    raise SystemExit(main())

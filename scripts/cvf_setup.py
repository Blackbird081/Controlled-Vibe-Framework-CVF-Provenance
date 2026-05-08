#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
CVF_WEB = REPO_ROOT / "EXTENSIONS" / "CVF_v1.6_AGENT_PLATFORM" / "cvf-web"
ENV_EXAMPLE = CVF_WEB / ".env.example"
ENV_LOCAL = CVF_WEB / ".env.local"
DOCTOR = REPO_ROOT / "scripts" / "cvf_doctor.py"
PROVIDER_CHECK = REPO_ROOT / "scripts" / "cvf_provider_check.py"


@dataclass
class SetupStep:
    id: str
    status: str
    message: str
    action: str = ""
    detail: dict = field(default_factory=dict)


def run_json_command(cmd: list[str], cwd: Path = REPO_ROOT, timeout: int = 120) -> tuple[int, dict | None, str]:
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
    except Exception as exc:
        return 1, None, str(exc)
    try:
        data = json.loads(result.stdout)
    except Exception:
        data = None
    return result.returncode, data, result.stderr.strip()


def ensure_env_local(write_env: bool) -> SetupStep:
    if ENV_LOCAL.exists():
        return SetupStep(
            "env_local",
            "PASS",
            ".env.local already exists.",
            detail={"path": str(ENV_LOCAL.relative_to(REPO_ROOT))},
        )
    if not ENV_EXAMPLE.exists():
        return SetupStep(
            "env_local",
            "BLOCKED",
            ".env.example is missing; cannot create .env.local.",
            action="Restore the tracked cvf-web .env.example template.",
        )
    if not write_env:
        return SetupStep(
            "env_local",
            "NEEDS_ACTION",
            ".env.local is missing.",
            action="Run with --write-env or copy .env.example to .env.local manually.",
            detail={"template": str(ENV_EXAMPLE.relative_to(REPO_ROOT))},
        )
    shutil.copyfile(ENV_EXAMPLE, ENV_LOCAL)
    return SetupStep(
        "env_local",
        "CREATED",
        ".env.local created from .env.example.",
        action="Fill provider keys in .env.local before live governance runs.",
        detail={"path": str(ENV_LOCAL.relative_to(REPO_ROOT))},
    )


def maybe_install_dependencies(run_install: bool) -> SetupStep:
    node_modules = CVF_WEB / "node_modules"
    if node_modules.exists():
        return SetupStep(
            "dependencies",
            "PASS",
            "cvf-web dependencies appear installed.",
            detail={"path": str(node_modules.relative_to(REPO_ROOT))},
        )
    if not run_install:
        return SetupStep(
            "dependencies",
            "NEEDS_ACTION",
            "cvf-web dependencies are not installed.",
            action="Run npm ci inside EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web, or re-run setup with --install.",
        )
    result = subprocess.run(
        ["npm", "ci"],
        cwd=CVF_WEB,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=300,
    )
    return SetupStep(
        "dependencies",
        "PASS" if result.returncode == 0 else "BLOCKED",
        "npm ci completed." if result.returncode == 0 else "npm ci failed.",
        detail={"returncode": result.returncode},
    )


def provider_step(provider: str, live: bool) -> SetupStep:
    if provider == "none":
        return SetupStep(
            "provider",
            "SKIP",
            "Provider validation skipped.",
            action="Run cvf_provider_check.py later when a provider key is configured.",
        )
    cmd = [sys.executable, str(PROVIDER_CHECK), "--provider", provider, "--json"]
    if live:
        cmd.append("--live")
    code, data, stderr = run_json_command(cmd, timeout=60)
    if data is None:
        return SetupStep(
            "provider",
            "BLOCKED",
            "Provider check did not return valid JSON.",
            detail={"returncode": code, "stderr": stderr[:300]},
        )
    status = data.get("status", "UNKNOWN")
    mapped = "PASS" if status in {"READY_UNVALIDATED", "LIVE_VALIDATED"} else "NEEDS_ACTION"
    return SetupStep(
        "provider",
        mapped,
        f"{provider} provider check: {status}.",
        action="Fill .env.local with a provider key." if status == "MISSING_KEY" else "",
        detail={
            "provider": provider,
            "status": status,
            "key_present": bool(data.get("key_present")),
            "live_validation": data.get("live_validation"),
            "secret_policy": data.get("secret_policy"),
        },
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Guided CVF first-run setup orchestrator.")
    parser.add_argument("--json", action="store_true", help="Output JSON.")
    parser.add_argument("--write-env", action="store_true", help="Create .env.local from .env.example if missing.")
    parser.add_argument("--install", action="store_true", help="Run npm ci inside cvf-web if dependencies are missing.")
    parser.add_argument("--provider", choices=["none", "alibaba", "deepseek"], default="alibaba")
    parser.add_argument("--live-provider-check", action="store_true", help="Run minimal live provider validation.")
    args = parser.parse_args()

    steps: list[SetupStep] = []

    doctor_code, doctor_data, doctor_stderr = run_json_command([sys.executable, str(DOCTOR), "--json"])
    steps.append(SetupStep(
        "doctor",
        "PASS" if doctor_code == 0 else "BLOCKED",
        f"cvf_doctor.py returned {doctor_data.get('status') if doctor_data else 'invalid output'}.",
        detail={"returncode": doctor_code, "stderr": doctor_stderr[:300]},
    ))
    steps.append(ensure_env_local(args.write_env))
    steps.append(maybe_install_dependencies(args.install))
    steps.append(provider_step(args.provider, args.live_provider_check))
    steps.append(SetupStep(
        "start_web",
        "READY",
        "Start CVF Web when dependencies and env are ready.",
        action="cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web && npm run dev",
        detail={"url": "http://localhost:3000"},
    ))
    steps.append(SetupStep(
        "first_governed_run",
        "READY",
        "Use the Web Settings panel to confirm provider settings, then run a trusted form.",
        action="For release-quality governance proof, run python scripts/run_cvf_release_gate_bundle.py --json.",
    ))

    blocked = any(step.status == "BLOCKED" for step in steps)
    needs_action = any(step.status == "NEEDS_ACTION" for step in steps)
    status = "BLOCKED" if blocked else ("NEEDS_ACTION" if needs_action else "READY")
    payload = {
        "status": status,
        "repo_root": str(REPO_ROOT),
        "cvf_web": str(CVF_WEB),
        "steps": [asdict(step) for step in steps],
        "boundary": "Guided first-run setup; not zero-friction and not GA.",
    }

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"CVF Setup: {status}")
        for step in steps:
            print(f"[{step.status}] {step.id}: {step.message}")
            if step.action:
                print(f"  -> {step.action}")

    return 1 if blocked else 0


if __name__ == "__main__":
    raise SystemExit(main())

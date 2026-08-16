#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
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


# ---------------------------------------------------------------------------
# Capability environment snapshot (read-only, secret-free, non-mutating).
#
# This section is fully isolated from the full-mode doctor above: it never
# calls bootstrap_repo_env(), build_checks(), is_port_listening(), or
# path_writable(). It observes only a small fixed allow-list of local
# commands (git/python/node/npm/npx) via discovery plus a bounded --version
# probe, and it never grants capability, execution, mutation, activation, or
# approval authority -- it is evidence only, per the accepted Minimal
# CVF-Native Snapshot Contract at
# docs/reference/capability_preflight_bootstrap/CVF_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_CONTRACT.md.
# ---------------------------------------------------------------------------

SNAPSHOT_TTL_SECONDS = 300  # fixed 5-minute TTL, per the minimal contract
SNAPSHOT_SCHEMA_VERSION = "cvf.capabilityEnvironmentSnapshot.v1"

SNAPSHOT_COMMANDS: tuple[str, ...] = ("git", "python", "node", "npm", "npx")

SNAPSHOT_SCOPE = "WORKSPACE_LOCAL"
SNAPSHOT_OBSERVATION_CLASS = "READ_ONLY_CLI_AVAILABILITY_VERSION"

AVAILABILITY_AVAILABLE = "AVAILABLE"
AVAILABILITY_MISSING = "MISSING"
AVAILABILITY_UNKNOWN = "UNKNOWN"

# Redacted path-class enum. The snapshot never emits a raw absolute
# executable path; it emits one of these coarse, non-identifying classes.
PATH_CLASS_SYSTEM_PATH = "SYSTEM_PATH"
PATH_CLASS_PROJECT_LOCAL = "PROJECT_LOCAL"
PATH_CLASS_USER_PATH = "USER_PATH"
PATH_CLASS_UNKNOWN_PATH_CLASS = "UNKNOWN_PATH_CLASS"
PATH_CLASS_NOT_DISCOVERED = "NOT_DISCOVERED"

VERIFICATION_PASS = "PASS"
VERIFICATION_WARN = "WARN"
VERIFICATION_FAIL = "FAIL"
VERIFICATION_UNKNOWN = "UNKNOWN"

VERSION_TEXT_MAX_LENGTH = 80


@dataclass
class CommandObservation:
    name: str
    availability: str
    pathClass: str
    version: str = ""


@dataclass
class CapabilitySnapshot:
    schemaVersion: str
    snapshotId: str
    observedAt: str
    expiresAt: str
    scope: str
    observationClass: str
    ttlSeconds: int
    commands: list[CommandObservation] = field(default_factory=list)
    verificationStatus: str = VERIFICATION_UNKNOWN
    reasons: list[str] = field(default_factory=list)


def classify_path_class(resolved_path: str) -> str:
    """Maps a resolved executable path to a coarse, non-identifying class.

    Never returns or embeds the raw path itself.
    """
    if not resolved_path:
        return PATH_CLASS_NOT_DISCOVERED
    try:
        normalized = resolved_path.replace("\\", "/").lower()
    except Exception:
        return PATH_CLASS_UNKNOWN_PATH_CLASS
    try:
        repo_root_normalized = str(REPO_ROOT).replace("\\", "/").lower()
    except Exception:
        repo_root_normalized = ""
    if repo_root_normalized and normalized.startswith(repo_root_normalized):
        return PATH_CLASS_PROJECT_LOCAL
    system_markers = (
        "/usr/bin", "/usr/local/bin", "/bin/", "windows/system32",
        "program files", "/opt/",
    )
    if any(marker in normalized for marker in system_markers):
        return PATH_CLASS_SYSTEM_PATH
    user_markers = ("/home/", "/users/", "appdata", ".local/bin", ".nvm")
    if any(marker in normalized for marker in user_markers):
        return PATH_CLASS_USER_PATH
    return PATH_CLASS_UNKNOWN_PATH_CLASS


def bound_version_text(raw: str) -> str:
    """Returns one bounded line or a redaction marker for unsafe output."""
    if not raw:
        return ""
    single_line = raw.strip().splitlines()[0] if raw.strip() else ""
    lowered = single_line.lower()
    unsafe_markers = ("secret", "token", "credential", "api_key", "apikey", "path=")
    repo_root = str(REPO_ROOT).replace("\\", "/").lower()
    normalized = single_line.replace("\\", "/")
    contains_absolute_path = bool(
        re.search(r"(?:^|\s)(?:[A-Za-z]:/|/(?:[^\s]+))", normalized)
    )
    if (
        any(marker in lowered for marker in unsafe_markers)
        or (repo_root and repo_root in normalized.lower())
        or contains_absolute_path
    ):
        return "[REDACTED_UNSAFE_VERSION_OUTPUT]"
    return single_line[:VERSION_TEXT_MAX_LENGTH]


def observe_command(
    name: str,
    *,
    which_fn=shutil.which,
    version_probe_fn=None,
) -> CommandObservation:
    """Observes a single command's availability, redacted path class, and a
    bounded version string.

    `which_fn` and `version_probe_fn` are injectable call sites so tests can
    be fully hermetic (no real subprocess/PATH dependency required). If
    `version_probe_fn` is None, a default bounded subprocess probe is used.
    `version_probe_fn(resolved_path: str) -> str` must return the raw
    version output on success and raise on failure/timeout/non-zero/unusable
    output; the caller here classifies any exception as UNKNOWN.
    """
    resolved_path = which_fn(name)
    if not resolved_path:
        return CommandObservation(
            name=name,
            availability=AVAILABILITY_MISSING,
            pathClass=PATH_CLASS_NOT_DISCOVERED,
            version="",
        )

    path_class = classify_path_class(resolved_path)
    probe = version_probe_fn or _default_version_probe
    try:
        raw_version = probe(resolved_path)
        if not raw_version or not raw_version.strip():
            raise ValueError("empty or unusable version probe output")
    except Exception:
        return CommandObservation(
            name=name,
            availability=AVAILABILITY_UNKNOWN,
            pathClass=path_class,
            version="",
        )

    return CommandObservation(
        name=name,
        availability=AVAILABILITY_AVAILABLE,
        pathClass=path_class,
        version=bound_version_text(raw_version),
    )


def _default_version_probe(resolved_path: str) -> str:
    """Bounded, timeout-guarded --version probe. Never invoked in hermetic
    tests, which inject `version_probe_fn` instead."""
    result = subprocess.run(
        [resolved_path, "--version"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=10,
    )
    if result.returncode != 0:
        raise RuntimeError(f"version probe returned non-zero: {result.returncode}")
    output = (result.stdout or result.stderr or "").strip()
    if not output:
        raise ValueError("version probe produced no usable output")
    return output


def build_capability_snapshot(
    *,
    commands: tuple[str, ...] = SNAPSHOT_COMMANDS,
    now_fn=None,
    which_fn=shutil.which,
    version_probe_fn=None,
    id_fn=None,
) -> CapabilitySnapshot:
    """Pure, injectable snapshot builder.

    Does NOT call bootstrap_repo_env(), build_checks(), is_port_listening(),
    path_writable(), or any mutating/network-adjacent helper. `now_fn` and
    `id_fn` are injectable so tests can assert exact observedAt/expiresAt and
    a stable/predictable snapshot identity without real clock/uuid calls.
    """
    now = (now_fn or (lambda: datetime.now(timezone.utc)))()
    observed_at = now
    expires_at = now + timedelta(seconds=SNAPSHOT_TTL_SECONDS)
    snapshot_id = (id_fn or (lambda: str(uuid.uuid4())))()

    observations = [
        observe_command(name, which_fn=which_fn, version_probe_fn=version_probe_fn)
        for name in commands
    ]

    reasons: list[str] = []
    missing = [o.name for o in observations if o.availability == AVAILABILITY_MISSING]
    unknown = [o.name for o in observations if o.availability == AVAILABILITY_UNKNOWN]
    if missing:
        reasons.append(f"missing command(s): {', '.join(missing)}")
    if unknown:
        reasons.append(f"unknown/unverifiable command(s): {', '.join(unknown)}")

    if missing:
        verification_status = VERIFICATION_FAIL
    elif unknown:
        verification_status = VERIFICATION_WARN
    elif not observations:
        verification_status = VERIFICATION_UNKNOWN
        reasons.append("no commands observed")
    else:
        verification_status = VERIFICATION_PASS

    return CapabilitySnapshot(
        schemaVersion=SNAPSHOT_SCHEMA_VERSION,
        snapshotId=snapshot_id,
        observedAt=observed_at.isoformat(),
        expiresAt=expires_at.isoformat(),
        scope=SNAPSHOT_SCOPE,
        observationClass=SNAPSHOT_OBSERVATION_CLASS,
        ttlSeconds=SNAPSHOT_TTL_SECONDS,
        commands=observations,
        verificationStatus=verification_status,
        reasons=reasons,
    )


def _parse_iso_timestamp(value: str) -> datetime | None:
    if not value or not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value)
    except (ValueError, TypeError):
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return parsed


def verify_snapshot_freshness(
    snapshot: CapabilitySnapshot,
    *,
    now_fn=None,
) -> tuple[bool, str]:
    """Pure freshness verification with no side effects.

    Returns (is_fresh, reason). An expired snapshot or malformed/unparseable
    time is fail-closed (`is_fresh=False`) with an explicit reason string --
    never silently treated as fresh. Freshness alone never grants execution,
    mutation, activation, approval, or owner authority.
    """
    now = (now_fn or (lambda: datetime.now(timezone.utc)))()
    if now.tzinfo is None or now.utcoffset() is None:
        return False, "malformed_or_unparseable_current_time"

    if snapshot.schemaVersion != SNAPSHOT_SCHEMA_VERSION:
        return False, "unsupported_snapshot_schema_version"

    if snapshot.ttlSeconds != SNAPSHOT_TTL_SECONDS:
        return False, "snapshot_ttl_mismatch"

    expires_at = _parse_iso_timestamp(snapshot.expiresAt)
    if expires_at is None:
        return False, "malformed_or_unparseable_expiresAt"

    observed_at = _parse_iso_timestamp(snapshot.observedAt)
    if observed_at is None:
        return False, "malformed_or_unparseable_observedAt"

    if expires_at - observed_at != timedelta(seconds=SNAPSHOT_TTL_SECONDS):
        return False, "snapshot_ttl_window_mismatch"

    if observed_at > now:
        return False, "snapshot_observed_in_future"

    if now > expires_at:
        return False, "snapshot_expired"

    return True, ""


def snapshot_is_ready(snapshot: CapabilitySnapshot, *, now_fn=None) -> tuple[bool, str]:
    """Aggregate readiness: fresh AND every observed command is AVAILABLE.

    Fail-closed: any MISSING/UNKNOWN command, or an expired/malformed
    snapshot, makes this non-ready with an explicit reason. This is evidence
    about observed local state only; it never grants capability, execution,
    mutation, activation, or approval authority.
    """
    fresh, freshness_reason = verify_snapshot_freshness(snapshot, now_fn=now_fn)
    if not fresh:
        return False, freshness_reason

    command_names = tuple(command.name for command in snapshot.commands)
    if command_names != SNAPSHOT_COMMANDS:
        return False, "snapshot_command_set_mismatch"

    not_available = [
        c.name for c in snapshot.commands if c.availability != AVAILABILITY_AVAILABLE
    ]
    if not_available:
        return False, f"command(s) not AVAILABLE: {', '.join(not_available)}"

    if not snapshot.commands:
        return False, "no commands observed"

    if snapshot.verificationStatus != VERIFICATION_PASS:
        return False, "snapshot_verification_not_pass"

    return True, ""


def snapshot_to_payload(snapshot: CapabilitySnapshot, *, now_fn=None) -> dict:
    """Serializes the snapshot to a secret-safe JSON-ready dict.

    Never includes a raw absolute executable path, raw repository absolute
    path, PATH listing, environment-variable name/value, credential
    value/status, or raw subprocess output beyond one bounded version line.
    """
    ready, readiness_reason = snapshot_is_ready(snapshot, now_fn=now_fn)
    payload = asdict(snapshot)
    payload["ready"] = ready
    if readiness_reason:
        payload["readinessReason"] = readiness_reason
    return payload


def run_capability_snapshot_cli(*, now_fn=None, which_fn=shutil.which, version_probe_fn=None) -> tuple[dict, int]:
    """Builds a snapshot, serializes it, and computes the CLI exit code.

    Exits 0 only when the snapshot is fresh AND all five commands are
    AVAILABLE. Any MISSING/UNKNOWN/expired/malformed state exits non-zero --
    this is real environment evidence, not a bug.
    """
    snapshot = build_capability_snapshot(
        now_fn=now_fn, which_fn=which_fn, version_probe_fn=version_probe_fn
    )
    payload = snapshot_to_payload(snapshot, now_fn=now_fn)
    exit_code = 0 if payload["ready"] else 1
    return payload, exit_code


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
    parser.add_argument(
        "--capability-snapshot",
        action="store_true",
        help=(
            "Emit a read-only, secret-free capability environment snapshot "
            "(git/python/node/npm/npx availability, redacted path class, "
            "bounded version, and TTL-based freshness) instead of running "
            "the full doctor. Fully isolated from env bootstrap and the "
            "full-mode checks: it is evidence only, never authority."
        ),
    )
    args = parser.parse_args()

    if args.capability_snapshot:
        payload, exit_code = run_capability_snapshot_cli()
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print(f"CVF Capability Snapshot: {'READY' if payload['ready'] else 'NOT_READY'}")
            for command in payload["commands"]:
                print(f"[{command['availability']}] {command['name']}: {command['version']}")
            if payload.get("readinessReason"):
                print(f"  -> {payload['readinessReason']}")
        return exit_code

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

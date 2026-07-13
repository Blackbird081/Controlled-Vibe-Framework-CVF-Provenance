#!/usr/bin/env python3
"""CVF SOT3-ACT-A3 real-provider approved-context live-proof runner.

Bounded runner for the SOT3-ACT-A3 work order. Bootstraps the operator-local
Alibaba/DashScope key via `bootstrap_repo_env`, invokes the exact
route-adjacent live test named in the work order's fulfillment manifest
through a one-use cryptographic permit, reads the secret-safe observation the test writes
to a temporary JSON side file, builds the dated receipt, and generates the
canonical hash manifest via `scripts/build_cvf_live_evidence_manifest.py`.

Invocation control: each runner process creates one short-lived nonce permit
bound to its observation path. The live test consumes the permit before it can
resolve a provider key, and records a secret-safe call ledger immediately
before the network boundary. Direct/ad-hoc Vitest invocation therefore skips
the live suite before provider access. A later runner invocation is justified
only when the prior receipt records a complete, retryable diagnostic per
`docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`, and
the operator/worker records what changed before rerun. The operator declared
Alibaba provider calls unmetered for this recovery on 2026-07-13; diagnostic
and diminishing-return stop rules still apply.

Authorization: docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import secrets
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
CVF_WEB_DIR = REPO_ROOT / "EXTENSIONS" / "CVF_v1.6_AGENT_PLATFORM" / "cvf-web"
LIVE_TEST_RELATIVE_PATH = "src/app/api/execute/route.sot3-activation.alibaba.live.test.ts"

sys.path.insert(0, str(REPO_ROOT / "scripts"))
from _local_env import bootstrap_repo_env  # noqa: E402

ALIBABA_KEY_ALIASES = (
    "ALIBABA_API_KEY",
    "DASHSCOPE_API_KEY",
    "CVF_BENCHMARK_ALIBABA_KEY",
    "CVF_ALIBABA_API_KEY",
)


def resolve_key_alias() -> str | None:
    import os

    for alias in ALIBABA_KEY_ALIASES:
        value = os.environ.get(alias, "").strip()
        if value:
            return alias
    return None


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def build_blocked_receipt(
    *,
    execution_base_head: str,
    started_at: str,
    finished_at: str,
    diagnostic: dict[str, Any],
    observed_call_count: int,
    key_alias_used: str | None,
) -> dict[str, Any]:
    return {
        "schemaVersion": "cvf.sot3ActA3LiveReceipt.v1",
        "batchId": "SOT3-ACT-A3",
        "executionBaseHead": execution_base_head,
        "startedAtUtc": started_at,
        "finishedAtUtc": finished_at,
        "overall": "BLOCKED",
        "claim": "N/A with reason: overall is BLOCKED; no A3 proof claim is made",
        "callBudget": {
            "operatorQuotaPolicy": "ALIBABA_PROVIDER_UNMETERED_2026-07-13",
            "runnerInvocationLimit": 1,
            "priorBlockedCallCount": 3,
            "observedCallCount": observed_call_count,
            "taskObservedCallCount": 3 + observed_call_count,
            "attempts": [],
        },
        "providerProof": {
            "provider": "alibaba",
            "model": "qwen-turbo",
            "keyAliasUsed": key_alias_used,
            "httpStatus": None,
            "success": False,
            "latencyMs": None,
            "outputLength": None,
        },
        "correlation": {
            "governanceReceiptId": None,
            "envelopeId": None,
            "sot3RecordId": None,
            "sot3IntegrityHash": None,
            "sot3RequestId": None,
            "traceCount": None,
            "packetIds": [],
            "kernelDecisionIds": [],
            "truthReceiptIds": [],
            "truthReferenceIds": [],
            "flowPackageIds": [],
        },
        "contextObservation": {
            "approvedContextHash": None,
            "providerSystemPromptHash": None,
            "approvedContextIncluded": None,
            "providerRequestObserved": False,
            "rawPromptPersisted": False,
        },
        "secretSafety": {
            "rawKeyPersisted": False,
            "rawProviderBodyPersisted": False,
            "rawOutputPersisted": False,
            "fullPromptPersisted": False,
        },
        "diagnostic": diagnostic,
    }


def build_pass_receipt(
    *,
    execution_base_head: str,
    started_at: str,
    finished_at: str,
    observation: dict[str, Any],
) -> dict[str, Any]:
    return {
        "schemaVersion": "cvf.sot3ActA3LiveReceipt.v1",
        "batchId": "SOT3-ACT-A3",
        "executionBaseHead": execution_base_head,
        "startedAtUtc": started_at,
        "finishedAtUtc": finished_at,
        "overall": observation["overall"],
        "claim": (
            "REAL_PROVIDER_APPROVED_CONTEXT_PROVEN_BOUNDED"
            if observation["overall"] == "PASS"
            else "N/A with reason: overall is not PASS"
        ),
        "callBudget": {
            "operatorQuotaPolicy": "ALIBABA_PROVIDER_UNMETERED_2026-07-13",
            "runnerInvocationLimit": 1,
            "priorBlockedCallCount": 3,
            "observedCallCount": observation["observedCallCount"],
            "taskObservedCallCount": 3 + observation["observedCallCount"],
            "attempts": [
                {
                    "attempt": 1,
                    "httpStatus": observation["httpStatus"],
                    "success": observation["success"],
                    "latencyMs": observation["latencyMs"],
                }
            ],
        },
        "providerProof": {
            "provider": observation["provider"],
            "model": observation["model"],
            "keyAliasUsed": observation["keyAliasUsed"],
            "httpStatus": observation["httpStatus"],
            "success": observation["success"],
            "latencyMs": observation["latencyMs"],
            "outputLength": observation["outputLength"],
        },
        "correlation": {
            "governanceReceiptId": observation["governanceReceiptId"],
            "envelopeId": observation["envelopeId"],
            "sot3RecordId": observation["sot3RecordId"],
            "sot3IntegrityHash": observation["sot3IntegrityHash"],
            "sot3RequestId": observation["sot3RequestId"],
            "traceCount": observation["traceCount"],
            "packetIds": observation["packetIds"],
            "kernelDecisionIds": observation["kernelDecisionIds"],
            "truthReceiptIds": observation["truthReceiptIds"],
            "truthReferenceIds": observation["truthReferenceIds"],
            "flowPackageIds": observation["flowPackageIds"],
        },
        "contextObservation": {
            "approvedContextHash": observation["approvedContextHash"],
            "providerSystemPromptHash": observation["providerSystemPromptHash"],
            "approvedContextIncluded": observation["approvedContextIncluded"],
            "providerRequestObserved": observation["providerRequestObserved"],
            "rawPromptPersisted": False,
        },
        "secretSafety": {
            "rawKeyPersisted": observation["rawKeyPersisted"],
            "rawProviderBodyPersisted": observation["rawProviderBodyPersisted"],
            "rawOutputPersisted": observation["rawOutputPersisted"],
            "fullPromptPersisted": observation["fullPromptPersisted"],
        },
        "diagnostic": observation["diagnostic"],
    }


def run_live_test(
    observation_output_path: Path,
    permit_path: Path,
    call_ledger_path: Path,
) -> tuple[int, str, int]:
    import os

    permit_token = secrets.token_urlsafe(32)
    permit = {
        "schemaVersion": "cvf.sot3ActA3RunnerPermit.v1",
        "batchId": "SOT3-ACT-A3R",
        "tokenHash": hashlib.sha256(permit_token.encode("utf-8")).hexdigest(),
        "observationPathHash": hashlib.sha256(
            str(observation_output_path).encode("utf-8")
        ).hexdigest(),
        "expiresAtEpochMs": int(datetime.now(timezone.utc).timestamp() * 1000) + 120_000,
    }
    permit_path.write_text(json.dumps(permit, sort_keys=True) + "\n", encoding="utf-8")
    env_overrides = {
        "CVF_SOT3_A3_OBSERVATION_OUTPUT_PATH": str(observation_output_path),
        "CVF_SOT3_A3_RUN_PERMIT_PATH": str(permit_path),
        "CVF_SOT3_A3_RUN_PERMIT_TOKEN": permit_token,
        "CVF_SOT3_A3_CALL_LEDGER_PATH": str(call_ledger_path),
    }

    merged_env = {**os.environ, **env_overrides}
    result = subprocess.run(
        ["npx", "vitest", "run", LIVE_TEST_RELATIVE_PATH],
        cwd=CVF_WEB_DIR,
        env=merged_env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    output = (result.stdout or "") + (result.stderr or "")
    observed_call_count = 0
    if call_ledger_path.exists():
        try:
            ledger = json.loads(call_ledger_path.read_text(encoding="utf-8"))
            observed_call_count = int(ledger.get("observedCallCount", 0))
        except (OSError, ValueError, TypeError, json.JSONDecodeError):
            observed_call_count = 0
    return result.returncode, output, observed_call_count


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", required=True, help="Output receipt JSON path.")
    parser.add_argument("--manifest", required=True, help="Output manifest JSON path.")
    parser.add_argument(
        "--execution-base-head",
        default="",
        help="Clean HEAD captured before edits. Defaults to `git rev-parse --short HEAD`.",
    )
    parser.add_argument(
        "--skip-live-invocation",
        action="store_true",
        help=(
            "Do not invoke the live test process at all; only rebuild the "
            "receipt/manifest from an already-produced observation file at "
            "the path given by --observation-file. Use when a prior durable "
            "observation is the authorized evidence source."
        ),
    )
    parser.add_argument(
        "--observation-file",
        default="",
        help="Existing observation JSON path to reuse with --skip-live-invocation.",
    )
    return parser.parse_args(argv)


def resolve_execution_base_head(explicit: str) -> str:
    if explicit:
        return explicit
    result = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else "UNKNOWN"


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    started_at = utc_now_iso()
    execution_base_head = resolve_execution_base_head(args.execution_base_head)
    receipt_path = Path(args.receipt)
    manifest_path = Path(args.manifest)

    loaded_env_files = bootstrap_repo_env()
    key_alias = resolve_key_alias()

    if not key_alias:
        diagnostic = {
            "stage": "auth",
            "class": "missing_api_key",
            "retryable": False,
            "userAction": "check_api_key",
            "safeMessage": (
                "No Alibaba/DashScope key alias was present after governed local "
                f"bootstrap of {[str(p) for p in loaded_env_files]}."
            ),
        }
        receipt = build_blocked_receipt(
            execution_base_head=execution_base_head,
            started_at=started_at,
            finished_at=utc_now_iso(),
            diagnostic=diagnostic,
            observed_call_count=0,
            key_alias_used=None,
        )
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print("BLOCKED: no Alibaba/DashScope key alias available.")
        return 1

    if args.skip_live_invocation:
        if not args.observation_file:
            print("VIOLATION: --skip-live-invocation requires --observation-file", file=sys.stderr)
            return 2
        observation_path = Path(args.observation_file)
        if not observation_path.exists():
            diagnostic = {
                "stage": "unknown",
                "class": "unknown_error",
                "retryable": False,
                "userAction": "do_not_retry_without_new_evidence",
                "safeMessage": (
                    "Live invocation was intentionally skipped (call-budget ceiling reached) "
                    "and no prior observation file was found to rebuild the receipt from."
                ),
            }
            receipt = build_blocked_receipt(
                execution_base_head=execution_base_head,
                started_at=started_at,
                finished_at=utc_now_iso(),
                diagnostic=diagnostic,
                observed_call_count=0,
                key_alias_used=key_alias,
            )
            receipt_path.parent.mkdir(parents=True, exist_ok=True)
            receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            print("BLOCKED: no observation file available and live invocation was skipped.")
            return 1
        observation = json.loads(observation_path.read_text(encoding="utf-8"))
        receipt = build_pass_receipt(
            execution_base_head=execution_base_head,
            started_at=started_at,
            finished_at=utc_now_iso(),
            observation=observation,
        )
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"Wrote receipt from existing observation (overall={receipt['overall']}): {receipt_path}")
    else:
        with tempfile.TemporaryDirectory(prefix="cvf-sot3-a3-obs-") as tmp:
            observation_path = Path(tmp) / "observation.json"
            permit_path = Path(tmp) / "runner-permit.json"
            call_ledger_path = Path(tmp) / "call-ledger.json"
            returncode, output, observed_call_count = run_live_test(
                observation_path,
                permit_path,
                call_ledger_path,
            )
            print(output)
            if returncode != 0 or not observation_path.exists():
                diagnostic = {
                    "stage": "provider",
                    "class": "unknown_error",
                    "retryable": False,
                    "userAction": "inspect_receipt",
                    "safeMessage": (
                        "The live test process failed or did not produce an observation file. "
                        "See captured stdout/stderr for a secret-safe summary."
                    ),
                }
                receipt = build_blocked_receipt(
                    execution_base_head=execution_base_head,
                    started_at=started_at,
                    finished_at=utc_now_iso(),
                    diagnostic=diagnostic,
                    observed_call_count=observed_call_count,
                    key_alias_used=key_alias,
                )
                receipt_path.parent.mkdir(parents=True, exist_ok=True)
                receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
                print("BLOCKED: live test process failed. See receipt diagnostic.")
                return 1
            observation = json.loads(observation_path.read_text(encoding="utf-8"))
            receipt = build_pass_receipt(
                execution_base_head=execution_base_head,
                started_at=started_at,
                finished_at=utc_now_iso(),
                observation=observation,
            )
            receipt_path.parent.mkdir(parents=True, exist_ok=True)
            receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            print(f"Wrote receipt (overall={receipt['overall']}): {receipt_path}")

    manifest_cmd = [
        sys.executable,
        str(REPO_ROOT / "scripts" / "build_cvf_live_evidence_manifest.py"),
        "--evidence",
        str(receipt_path),
        "--command",
        (
            "python scripts/run_cvf_sot3_a3_live_proof.py --receipt "
            f"{receipt_path} --manifest {manifest_path}"
        ),
        "--output",
        str(manifest_path),
    ]
    manifest_result = subprocess.run(
        manifest_cmd,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    print(manifest_result.stdout)
    if manifest_result.returncode != 0:
        print(manifest_result.stderr, file=sys.stderr)
        return manifest_result.returncode

    return 0 if json.loads(receipt_path.read_text(encoding="utf-8"))["overall"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

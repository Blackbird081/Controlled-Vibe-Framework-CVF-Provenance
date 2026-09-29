#!/usr/bin/env python3
"""Read-only local reconciliation of one Q001 receipt attempt against a ledger snapshot."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def _block_hash(block: dict) -> str:
    payload = {key: block[key] for key in ("timestamp", "previous_hash", "event")}
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()


def reconcile(ledger_path: Path, attempt_id: str) -> dict:
    result = {
        "status": "INVALID_SNAPSHOT",
        "safeToRetry": False,
        "ledgerBlocks": None,
        "ledgerSha256": None,
        "matches": 0,
    }
    try:
        raw = ledger_path.read_bytes()
        result["ledgerSha256"] = hashlib.sha256(raw).hexdigest()
        chain = json.loads(raw)
        if not isinstance(chain, list):
            return result
        result["ledgerBlocks"] = len(chain)
        previous = "GENESIS"
        matches = []
        for index, block in enumerate(chain):
            if not isinstance(block, dict) or not isinstance(block.get("event"), dict):
                return result
            if block.get("previous_hash") != previous or block.get("hash") != _block_hash(block):
                return result
            previous = block["hash"]
            if block["event"].get("request_id") == attempt_id:
                matches.append((index, block))
        result["matches"] = len(matches)
        if not matches:
            result["status"] = "NOT_FOUND_IN_SNAPSHOT"
        elif len(matches) > 1:
            result["status"] = "DUPLICATE_OR_CONFLICT"
        else:
            index, block = matches[0]
            decision = block["event"].get("decision")
            if not isinstance(decision, dict) or decision.get("final_decision") not in {
                "ALLOW", "DENY", "REVIEW", "ESCALATE", "SANDBOX"
            }:
                result["status"] = "INVALID_SNAPSHOT"
                return result
            result.update({
                "status": "FOUND_ONE",
                "blockIndex": index,
                "blockHash": block["hash"],
                "decision": decision["final_decision"],
            })
    except (OSError, ValueError, KeyError, TypeError, UnicodeError):
        pass
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, required=True, help="Exact local ledger snapshot path")
    parser.add_argument("--attempt-id", required=True, help="Receipt attempt ID shown by the export route")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if not args.attempt_id.startswith("artifact-proof-") or len(args.attempt_id) > 200:
        parser.error("attempt ID must be a bounded artifact-proof ID")
    result = reconcile(args.ledger, args.attempt_id)
    if args.json:
        print(json.dumps(result, sort_keys=True))
    else:
        print(f"{result['status']}: blocks={result['ledgerBlocks']} matches={result['matches']} "
              f"safe_to_retry={result['safeToRetry']}")
    return 0 if result["status"] == "FOUND_ONE" else 2


if __name__ == "__main__":
    raise SystemExit(main())

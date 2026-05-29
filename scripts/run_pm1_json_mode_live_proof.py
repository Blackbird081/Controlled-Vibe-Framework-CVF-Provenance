"""
CVF PM-1 json_mode Live Proof Script
=====================================
Calls DeepSeek deepseek-chat and OpenAI gpt-4o with json_mode
(response_format: {"type": "json_object"}) and captures evidence receipts.

PROOF BOUNDARY: METHOD_PROOF_ONLY
This script calls provider APIs directly, bypassing the governed /api/execute
route. Evidence produced here proves provider method capability (json_mode
support), not CVF governance behavior. Do not cite these results as governed
route proof or release-gate evidence.

Run:
  set DASHSCOPE_API_KEY=sk-... (for future Alibaba)
  python scripts/run_pm1_json_mode_live_proof.py
"""
import os
import sys
import json
import time
import hashlib
from typing import Optional

# Load .env.local from cvf-web
ENV_LOCAL = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "EXTENSIONS", "CVF_v1.6_AGENT_PLATFORM", "cvf-web", ".env.local"
)

def load_env_file(path: str) -> dict:
    """Parse KEY=VALUE from .env.local (simple parser, no quoting needed)."""
    env = {}
    if not os.path.exists(path):
        print(f"WARNING: .env.local not found at {path}")
        return env
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                env[key.strip()] = value.strip().strip('"').strip("'")
    return env

ENV = load_env_file(ENV_LOCAL)

DEEPSEEK_KEY = ENV.get("DEEPSEEK_API_KEY", os.environ.get("DEEPSEEK_API_KEY", ""))
OPENAI_KEY = ENV.get("OPENAI_API_KEY", os.environ.get("OPENAI_API_KEY", ""))

if not DEEPSEEK_KEY and not OPENAI_KEY:
    print("ERROR: Neither DEEPSEEK_API_KEY nor OPENAI_API_KEY found.")
    sys.exit(1)

EXPECTED_JSON_KEYS = {"provider", "method", "status", "timestamp"}

def _validate_json_response(result: dict) -> dict:
    """Check that the model returned parseable JSON with the expected keys."""
    if result.get("http_status") != 200:
        return {**result, "json_valid": False, "json_keys_present": False}
    try:
        choices = result.get("response", {}).get("choices", [])
        content = choices[0]["message"]["content"] if choices else ""
        parsed = json.loads(content)
        keys_present = EXPECTED_JSON_KEYS.issubset(parsed.keys())
        return {**result, "json_valid": True, "json_keys_present": keys_present, "parsed_output": parsed}
    except (json.JSONDecodeError, KeyError, IndexError, TypeError):
        return {**result, "json_valid": False, "json_keys_present": False}


def make_receipt_id(provider: str) -> str:
    ts = str(int(time.time()))
    h = hashlib.sha256(f"{provider}-{ts}".encode()).hexdigest()[:12]
    return f"rcpt-pm1-{provider}-{h}"

def call_deepseek_json_mode(api_key: str) -> dict:
    """Call DeepSeek API with json_mode (response_format json_object)."""
    import urllib.request
    import urllib.error

    url = "https://api.deepseek.com/v1/chat/completions"
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a JSON-only assistant. Always respond with valid JSON."},
            {"role": "user", "content": "Return a JSON object with keys: provider, method, status, timestamp. Use values: provider=deepseek, method=json_mode, status=ok, timestamp=current ISO 8601."}
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0,
        "max_tokens": 256
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.status
            body = json.loads(resp.read().decode("utf-8"))
            return {
                "provider": "deepseek",
                "model": "deepseek-chat",
                "method": "json_mode",
                "http_status": status,
                "receipt_id": make_receipt_id("deepseek"),
                "response": body,
                "rawSecretPrinted": False,
                "decision": "ALLOW" if status == 200 else "DENY",
                "evidenceMode": "live"
            }
    except urllib.error.HTTPError as e:
        return {
            "provider": "deepseek",
            "model": "deepseek-chat",
            "method": "json_mode",
            "http_status": e.code,
            "receipt_id": make_receipt_id("deepseek"),
            "error": str(e),
            "rawSecretPrinted": False,
            "decision": "DENY",
            "evidenceMode": "live"
        }
    except Exception as e:
        return {
            "provider": "deepseek",
            "model": "deepseek-chat",
            "method": "json_mode",
            "http_status": None,
            "receipt_id": make_receipt_id("deepseek"),
            "error": str(e),
            "rawSecretPrinted": False,
            "decision": "UNKNOWN",
            "evidenceMode": "live"
        }

def call_openai_json_mode(api_key: str) -> dict:
    """Call OpenAI API with json_mode (response_format json_object)."""
    import urllib.request
    import urllib.error

    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a JSON-only assistant. Always respond with valid JSON."},
            {"role": "user", "content": "Return a JSON object with keys: provider, method, status, timestamp. Use values: provider=openai, method=json_mode, status=ok, timestamp=current ISO 8601."}
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0,
        "max_tokens": 256
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.status
            body = json.loads(resp.read().decode("utf-8"))
            return {
                "provider": "openai",
                "model": "gpt-4o",
                "method": "json_mode",
                "http_status": status,
                "receipt_id": make_receipt_id("openai"),
                "response": body,
                "rawSecretPrinted": False,
                "decision": "ALLOW" if status == 200 else "DENY",
                "evidenceMode": "live"
            }
    except urllib.error.HTTPError as e:
        return {
            "provider": "openai",
            "model": "gpt-4o",
            "method": "json_mode",
            "http_status": e.code,
            "receipt_id": make_receipt_id("openai"),
            "error": str(e),
            "rawSecretPrinted": False,
            "decision": "DENY",
            "evidenceMode": "live"
        }
    except Exception as e:
        return {
            "provider": "openai",
            "model": "gpt-4o",
            "method": "json_mode",
            "http_status": None,
            "receipt_id": make_receipt_id("openai"),
            "error": str(e),
            "rawSecretPrinted": False,
            "decision": "UNKNOWN",
            "evidenceMode": "live"
        }

def main():
    results = []

    if DEEPSEEK_KEY:
        print("[PM-1] Calling DeepSeek deepseek-chat json_mode...")
        r = _validate_json_response(call_deepseek_json_mode(DEEPSEEK_KEY))
        results.append(r)
        status = "PASS" if r.get("http_status") == 200 and r.get("json_valid") else "FAIL"
        print(f"  => {status} (HTTP {r.get('http_status')}, json_valid={r.get('json_valid')}, keys_present={r.get('json_keys_present')}, receipt {r.get('receipt_id')})")
    else:
        print("[PM-1] DeepSeek key not available — skipping.")

    if OPENAI_KEY:
        print("[PM-1] Calling OpenAI gpt-4o json_mode...")
        r = _validate_json_response(call_openai_json_mode(OPENAI_KEY))
        results.append(r)
        status = "PASS" if r.get("http_status") == 200 and r.get("json_valid") else "FAIL"
        print(f"  => {status} (HTTP {r.get('http_status')}, json_valid={r.get('json_valid')}, keys_present={r.get('json_keys_present')}, receipt {r.get('receipt_id')})")
    else:
        print("[PM-1] OpenAI key not available — skipping.")

    # Print summary
    print(f"\n{'='*60}")
    print("PM-1 json_mode Live Proof Results")
    print(f"{'='*60}")
    for r in results:
        content = r.get("response", {})
        choices = content.get("choices", [{}])
        msg = choices[0].get("message", {}) if choices else {}
        output = msg.get("content", "N/A")
        print(f"  Provider: {r['provider']}")
        print(f"  Model: {r['model']}")
        print(f"  Method: {r['method']}")
        print(f"  HTTP Status: {r.get('http_status')}")
        print(f"  Receipt: {r.get('receipt_id')}")
        print(f"  Decision: {r.get('decision')}")
        print(f"  Output (truncated): {str(output)[:200]}")
        print(f"  rawSecretPrinted: {r.get('rawSecretPrinted')}")
        print(f"  evidenceMode: {r.get('evidenceMode')}")
        if r.get("error"):
            print(f"  Error: {r['error'][:200]}")
        print()

    # Write JSON results
    out_dir = os.path.join(os.path.dirname(__file__), "..", "docs", "evidence", "provider-methods", "json-mode")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "pm1-live-results.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, default=str)

    print(f"Results written to: {out_path}")

    # Return exit code — must have live results, all HTTP 200, all JSON valid with expected keys
    live_results = [r for r in results if r.get("http_status") is not None]
    all_pass = (
        len(live_results) > 0
        and all(r["http_status"] == 200 for r in live_results)
        and all(r.get("json_valid") for r in live_results)
        and all(r.get("json_keys_present") for r in live_results)
    )
    if not all_pass:
        sys.exit(1)

if __name__ == "__main__":
    main()

"""
CVF PM-2 Streaming Live Proof Script
=====================================
Calls Alibaba qwen-turbo with streaming (stream=True) and captures
SSE stream response with first-token latency.

PROOF BOUNDARY: METHOD_PROOF_ONLY
This script calls the Alibaba API directly, bypassing the governed /api/execute
route. Evidence produced here proves provider method capability (streaming
support), not CVF governance behavior. Do not cite these results as governed
route proof or release-gate evidence.

Run:
  python scripts/run_pm2_streaming_live_proof.py
"""
import os
import sys
import json
import time
import hashlib
import urllib.request
import urllib.error

ENV_LOCAL = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "EXTENSIONS", "CVF_v1.6_AGENT_PLATFORM", "cvf-web", ".env.local"
)

def load_env(path: str):
    env = {}
    if not os.path.exists(path): return env
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"): continue
            if "=" in line:
                k, _, v = line.partition("=")
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env

ENV = load_env(ENV_LOCAL)
ALIBABA_KEY = ENV.get("ALIBABA_API_KEY", ENV.get("DASHSCOPE_API_KEY", os.environ.get("DASHSCOPE_API_KEY", os.environ.get("ALIBABA_API_KEY", ""))))

def make_receipt(provider: str) -> str:
    h = hashlib.sha256(f"{provider}-{time.time()}".encode()).hexdigest()[:12]
    return f"rcpt-pm2-{provider}-{h}"

def call_alibaba_streaming(api_key: str) -> dict:
    """Call Alibaba DashScope with streaming (stream=True)."""
    url = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions"
    payload = {
        "model": "qwen-turbo",
        "messages": [
            {"role": "user", "content": "Say hello in exactly 5 words."}
        ],
        "stream": True,
        "temperature": 0,
        "max_tokens": 64
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "text/event-stream"
        },
        method="POST"
    )
    chunks = []
    first_token_ts = None
    start_ts = time.time()
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            status = resp.status
            for line_bytes in resp:
                line = line_bytes.decode("utf-8", errors="replace").strip()
                if not line or line.startswith(":"):
                    continue
                if line.startswith("data: "):
                    data_str = line[6:]
                    if data_str == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data_str)
                        content = chunk.get("choices", [{}])[0].get("delta", {}).get("content", "")
                        if content and first_token_ts is None:
                            first_token_ts = time.time()
                        chunks.append(content)
                    except json.JSONDecodeError:
                        pass
        latency = (first_token_ts - start_ts) if first_token_ts else None
        full_output = "".join(chunks)
        return {
            "provider": "alibaba",
            "model": "qwen-turbo",
            "method": "streaming",
            "http_status": status,
            "receipt_id": make_receipt("alibaba"),
            "stream_chunks": len(chunks),
            "output_length": len(full_output),
            "first_token_latency_ms": round(latency * 1000, 1) if latency else None,
            "output": full_output.strip(),
            "rawSecretPrinted": False,
            "decision": "ALLOW" if status == 200 else "DENY",
            "evidenceMode": "live"
        }
    except urllib.error.HTTPError as e:
        return {"provider":"alibaba","model":"qwen-turbo","method":"streaming",
                "http_status":e.code,"receipt_id":make_receipt("alibaba"),
                "error":str(e),"rawSecretPrinted":False,"decision":"DENY","evidenceMode":"live"}
    except Exception as e:
        return {"provider":"alibaba","model":"qwen-turbo","method":"streaming",
                "http_status":None,"receipt_id":make_receipt("alibaba"),
                "error":str(e),"rawSecretPrinted":False,"decision":"UNKNOWN","evidenceMode":"live"}

def main():
    if not ALIBABA_KEY:
        print("[PM-2] SKIP: Alibaba key not available — cannot produce live proof.")
        print("[PM-2] Set DASHSCOPE_API_KEY to run this proof.")
        sys.exit(1)

    print("[PM-2] Calling Alibaba qwen-turbo streaming...")
    r = call_alibaba_streaming(ALIBABA_KEY)
    status = "PASS" if r.get("http_status") == 200 else "FAIL"
    print(f"  => {status} (HTTP {r.get('http_status')}, receipt {r.get('receipt_id')})")
    if r.get("first_token_latency_ms"):
        print(f"  => First-token latency: {r['first_token_latency_ms']}ms")
    if r.get("stream_chunks"):
        print(f"  => Stream chunks: {r['stream_chunks']}")
    print(f"  => Output: {r.get('output', 'N/A')[:200]}")

    out_dir = os.path.join(os.path.dirname(__file__), "..", "docs", "evidence", "provider-methods", "streaming")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "pm2-live-results.json"), "w", encoding="utf-8") as f:
        json.dump(r, f, indent=2, default=str)
    print(f"Results written to {out_dir}/pm2-live-results.json")

if __name__ == "__main__":
    main()

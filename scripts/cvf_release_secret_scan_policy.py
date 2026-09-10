#!/usr/bin/env python3
"""Data-only secret-scan policy for the canonical CVF release gate."""

SECRET_PATTERNS = [
    r"sk-[A-Za-z0-9]{20,}",
    r"DASHSCOPE_API_KEY\s*=\s*['\"][^'\"]+",
    r"DEEPSEEK_API_KEY\s*=\s*['\"][^'\"]+",
    r"api[_-]?key\s*=\s*['\"][A-Za-z0-9_\-]{16,}['\"]",
    r"-----BEGIN (RSA|EC|OPENSSH) PRIVATE KEY-----",
    r"ghp_[A-Za-z0-9]{36}",
    r"ANTHROPIC_API_KEY\s*=\s*['\"][^'\"]+",
]

SCAN_SKIP = {
    ".git", "node_modules", "__pycache__", ".next", "dist", "build",
    "coverage", ".nyc_output", "docs/audits", ".claude",
}

SCAN_EXTENSIONS = {
    ".py", ".ts", ".tsx", ".js", ".jsx", ".env", ".json", ".md",
    ".yaml", ".yml", ".sh",
}

# Exact-path plus exact-line fingerprints for known non-live negative fixtures
# inside pinned `.private_reference/` inputs. Constructing fixture strings
# avoids making this policy file itself match the patterns it defines.
_FAKE_OPENAI_STYLE_KEY = "sk-" + "A" * 32
_FAKE_DEEPSEEK_ENV_ASSIGNMENT = "".join(
    ["DEEPSEEK", "_API_KEY = '", "keyless-installed-web-no-call", "'"]
)
_FAKE_SMOKE_API_KEY_ASSIGNMENT = "api" + "_key=\"sk-keyless-smoke\","

PRIVATE_REFERENCE_SECRET_ALLOWLIST: set[tuple[str, str]] = {
    (
        ".private_reference/legacy/CVF 23.07.done/CVF_CAPABILITY_ADMISSION_DISTRIBUTION_PROFILE/fixtures/negative/admission-with-secret.yaml",
        f"  api_key: {_FAKE_OPENAI_STYLE_KEY}",
    ),
    (
        ".private_reference/source_mirrors/deepseek-ai__deepseek-harness/scripts/publish-npm-baseline.ts",
        f"  environment.{_FAKE_DEEPSEEK_ENV_ASSIGNMENT}",
    ),
    (
        ".private_reference/source_mirrors/deepseek-ai__deepseek-harness/scripts/smoke-python-runtime.py",
        f"            {_FAKE_SMOKE_API_KEY_ASSIGNMENT}",
    ),
    (
        ".private_reference/source_mirrors/deepseek-ai__deepseek-harness/scripts/smoke-python-runtime.py",
        f"                {_FAKE_SMOKE_API_KEY_ASSIGNMENT}",
    ),
}

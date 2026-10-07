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
    # Ignored execution scratch/archive is outside the source candidate.
    # Keep other .cvf paths and candidate/build artifacts in scan scope.
    ".cvf/runtime",
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

# Reviewed test/parser/example inputs; raw key values are never embedded here.
# Whole-file byte identity protects PEM bodies and all surrounding content.
# These exact pins do not exempt any directory, test family or new finding.
RELEASE_SECRET_FIXTURE_FINGERPRINTS: set[tuple[str, str, int, str]] = {
    (
        '.private_reference/source_mirrors/affaan-m__ECC/tests/hooks/governance-capture.test.js',
        '44b364d5a58288b3d04d5f301abf14c1b4c181a743ab5b59ecc49265f9dfe082',
        36, '139d5d89baaefbf6f5997a12c72c049d67ee9d7e0d346f9cd8d88ae6ea79fb1d',
    ),
    (
        '.private_reference/source_mirrors/affaan-m__ECC/tests/hooks/governance-capture.test.js',
        '44b364d5a58288b3d04d5f301abf14c1b4c181a743ab5b59ecc49265f9dfe082',
        42, '4d592275b0855f2250b73a230bfc3e04e1c2a0626a81610d606a993c29e64f15',
    ),
    (
        '.private_reference/source_mirrors/affaan-m__ECC/tests/hooks/governance-capture.test.js',
        '44b364d5a58288b3d04d5f301abf14c1b4c181a743ab5b59ecc49265f9dfe082',
        48, '67e868fc49790f5dad6dc21aa360f990e757a87b9ca2f81c7a72c33a884d1c14',
    ),
    (
        '.private_reference/source_mirrors/affaan-m__ECC/tests/hooks/governance-capture.test.js',
        '44b364d5a58288b3d04d5f301abf14c1b4c181a743ab5b59ecc49265f9dfe082',
        54, '4a58a514731c7a1e72dd9d79be6449c59a4a5e2446c6f7535c9c4553dfe763be',
    ),
    (
        '.private_reference/source_mirrors/affaan-m__ECC/tests/hooks/governance-capture.test.js',
        '44b364d5a58288b3d04d5f301abf14c1b4c181a743ab5b59ecc49265f9dfe082',
        135, '680ac6a60a7333b78eaf0e9d745a45eb3dab78002b7ee3339bd9260c4b67bef0',
    ),
    (
        '.private_reference/source_mirrors/affaan-m__ECC/tests/hooks/governance-capture.test.js',
        '44b364d5a58288b3d04d5f301abf14c1b4c181a743ab5b59ecc49265f9dfe082',
        642, 'a89480b26e165623d06cefefbdfcfd41170697457011e69825e463f1f19084a5',
    ),
    (
        '.private_reference/source_mirrors/affaan-m__ECC/tests/hooks/pre-bash-commit-quality.test.js',
        'a7b4ef3b6a0f4ad38c60dd8f350efcfd10490426f7e1d0bb2b3ca31ab0bbaa59',
        215, '9b0ed5aa7b0e02aeb71fad8b489db511fac1e603c377075feadb37f52b746bfd',
    ),
    (
        '.private_reference/source_mirrors/affaan-m__ECC/tests/hooks/pre-bash-commit-quality.test.js',
        'a7b4ef3b6a0f4ad38c60dd8f350efcfd10490426f7e1d0bb2b3ca31ab0bbaa59',
        217, 'c87024337b2b781c13873791a7085b624f4b2cf55946be1b8f261b1507ccd250',
    ),
    (
        '.private_reference/source_mirrors/affaan-m__ECC/tests/hooks/pre-bash-commit-quality.test.js',
        'a7b4ef3b6a0f4ad38c60dd8f350efcfd10490426f7e1d0bb2b3ca31ab0bbaa59',
        221, '2a6d5e043ba8641fc7d48cce0a952cf6890662525081a913a90a2d868cae8f14',
    ),
    (
        '.private_reference/source_mirrors/agentgateway__agentgateway/controller/test/e2e/testdata/dynamic-ca-cert/dynamic-ca-cert-invalid-ca.yaml',
        '22a5811f94aa31bed1c2aa96c3a47d6681c1f12c1d9ad5da63f13fc6dec07f4f',
        37, '486820a239f22c0eb427596ad5a98bf88c3d46c021d692bdae992924f6dea304',
    ),
    (
        '.private_reference/source_mirrors/agentgateway__agentgateway/controller/test/e2e/testdata/dynamic-ca-cert/dynamic-ca-cert.yaml',
        '54cf1cbd89427e755cc742c7581ae1b4ad447a949931348a175566f83b7688da',
        27, '486820a239f22c0eb427596ad5a98bf88c3d46c021d692bdae992924f6dea304',
    ),
    (
        '.private_reference/source_mirrors/agentgateway__agentgateway/examples/netbird-agent-network/kubernetes/README.md',
        '86cc8270e50f849f4328e4558cf4e13b9b48b05be1fbceb29b4bdc677e4154d6',
        131, 'c6ee6ebed3b210de6e799c64ac30539c19f5a8b7f44e2a575f69c3cac9d3975d',
    ),
    (
        '.private_reference/source_mirrors/Blackbird081__everything-claude-code/tests/hooks/governance-capture.test.js',
        '44b364d5a58288b3d04d5f301abf14c1b4c181a743ab5b59ecc49265f9dfe082',
        36, '139d5d89baaefbf6f5997a12c72c049d67ee9d7e0d346f9cd8d88ae6ea79fb1d',
    ),
    (
        '.private_reference/source_mirrors/Blackbird081__everything-claude-code/tests/hooks/governance-capture.test.js',
        '44b364d5a58288b3d04d5f301abf14c1b4c181a743ab5b59ecc49265f9dfe082',
        42, '4d592275b0855f2250b73a230bfc3e04e1c2a0626a81610d606a993c29e64f15',
    ),
    (
        '.private_reference/source_mirrors/Blackbird081__everything-claude-code/tests/hooks/governance-capture.test.js',
        '44b364d5a58288b3d04d5f301abf14c1b4c181a743ab5b59ecc49265f9dfe082',
        48, '67e868fc49790f5dad6dc21aa360f990e757a87b9ca2f81c7a72c33a884d1c14',
    ),
    (
        '.private_reference/source_mirrors/Blackbird081__everything-claude-code/tests/hooks/governance-capture.test.js',
        '44b364d5a58288b3d04d5f301abf14c1b4c181a743ab5b59ecc49265f9dfe082',
        54, '4a58a514731c7a1e72dd9d79be6449c59a4a5e2446c6f7535c9c4553dfe763be',
    ),
    (
        '.private_reference/source_mirrors/Blackbird081__everything-claude-code/tests/hooks/governance-capture.test.js',
        '44b364d5a58288b3d04d5f301abf14c1b4c181a743ab5b59ecc49265f9dfe082',
        135, '680ac6a60a7333b78eaf0e9d745a45eb3dab78002b7ee3339bd9260c4b67bef0',
    ),
    (
        '.private_reference/source_mirrors/Blackbird081__everything-claude-code/tests/hooks/governance-capture.test.js',
        '44b364d5a58288b3d04d5f301abf14c1b4c181a743ab5b59ecc49265f9dfe082',
        642, 'a89480b26e165623d06cefefbdfcfd41170697457011e69825e463f1f19084a5',
    ),
    (
        '.private_reference/source_mirrors/Blackbird081__everything-claude-code/tests/hooks/pre-bash-commit-quality.test.js',
        'f1bcbd7b3f32bdd44bb8fc4fda583e58d3779737a925af51f8e1d519b006000c',
        214, '9b0ed5aa7b0e02aeb71fad8b489db511fac1e603c377075feadb37f52b746bfd',
    ),
    (
        '.private_reference/source_mirrors/Blackbird081__everything-claude-code/tests/hooks/pre-bash-commit-quality.test.js',
        'f1bcbd7b3f32bdd44bb8fc4fda583e58d3779737a925af51f8e1d519b006000c',
        216, 'c87024337b2b781c13873791a7085b624f4b2cf55946be1b8f261b1507ccd250',
    ),
    (
        '.private_reference/source_mirrors/Blackbird081__everything-claude-code/tests/hooks/pre-bash-commit-quality.test.js',
        'f1bcbd7b3f32bdd44bb8fc4fda583e58d3779737a925af51f8e1d519b006000c',
        220, '2a6d5e043ba8641fc7d48cce0a952cf6890662525081a913a90a2d868cae8f14',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/ai/test/bedrock-mantle-auth.test.ts',
        'f3e4f6b998318b19b5d2dc41830981de7ee2d0c8e0448a8be3faf4636f62fdda',
        142, 'c34506ab92ae36ebef1d6bb7117e216fa26048b9bb2c7f6ece448dfdb023de57',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/ai/test/bedrock-mantle-auth.test.ts',
        'f3e4f6b998318b19b5d2dc41830981de7ee2d0c8e0448a8be3faf4636f62fdda',
        211, '19d76df61979cbde23c28b8f0b0830c60d67b4d02b8f2d1e2c373e3da635d3cc',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/ai/test/openai-codex-responses-lite.test.ts',
        'bd0fc20171f76091487932aaadc2af3c7daa743e12bae9f0bd7f01ba111d12a8',
        1242, '943c329cd075dfab971fcc5baea93b75bf9f6c345aaaa8438efcadc862f5e259',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/ai/test/transform-messages-redact-sensitive.test.ts',
        '51b95fee99c48ce00b3e688a65cf723d49f5f635a8946e51882ccaf7af4e4743',
        28, 'a86745371023ecc9061c2f423d0df427b47e4c628b4ffa5a305495625e452032',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/ai/test/transform-messages-redact-sensitive.test.ts',
        '51b95fee99c48ce00b3e688a65cf723d49f5f635a8946e51882ccaf7af4e4743',
        144, '9a64bc22029b2e2a3d1b624e156616ffa925bd14b042684a9abb85c9a399e973',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/ai/test/transform-messages-redact-sensitive.test.ts',
        '51b95fee99c48ce00b3e688a65cf723d49f5f635a8946e51882ccaf7af4e4743',
        178, 'bcc865cf351c2ddf7b10307ee89eb0cb328896880ab1420b36f5bd88c7824e47',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/ai/test/transform-messages-redact-sensitive.test.ts',
        '51b95fee99c48ce00b3e688a65cf723d49f5f635a8946e51882ccaf7af4e4743',
        211, '0a701b9233056c41f89d4096ad998fdaf31aaac455f54fb61416142767f3ba1c',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/catalog/test/issue-830-repro.test.ts',
        '67eedc70ce0e68cd440b6352f3a22c44ae01f860676a06bd5a5a185d60305388',
        14, '0f291f1b9b89feb19166771593123a84064ba32798e9d8d5f06fc715685e2c6b',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/coding-agent/test/acp-session-effects.test.ts',
        '026c5557df075a4835088d32199bbd0feb9e22fff481bf7101b019ef72514221',
        19, '4c194200de7d94dec45f9718e200ee7ac0647045bd4338031655ec004c3a74f9',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/coding-agent/test/default-model-ambient-bedrock.test.ts',
        '4fba6d302fc44dc0fee7448a6225b0679be9db57e354089e110f05cfb416133d',
        70, 'a528a4ee58c7e926bf62ce11d6af0b243e24bd5eb8e2a6587b5e90ae196c9bf1',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/coding-agent/test/memory-redaction.test.ts',
        '001ed5b3903009151bf9815368d9e5e477f430d6d9300aab3b9673a7e5369a8d',
        13, '154c9febac6d93e2d75bf4eb8abadeb8d52e1a7e4eb94d3acf3f2fd9dcdfee2a',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/coding-agent/test/secrets-obfuscator.test.ts',
        '0cbe1a46d592d4ac9f9920820d11f8ccff82749c89cdb65153bb09bce8415a45',
        636, 'faa2dfb3b3dc776144ff5e0f0764e4fac3616f5c3b40e8e83a6ab73d1f2657ef',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/coding-agent/test/secrets-obfuscator.test.ts',
        '0cbe1a46d592d4ac9f9920820d11f8ccff82749c89cdb65153bb09bce8415a45',
        655, 'faa2dfb3b3dc776144ff5e0f0764e4fac3616f5c3b40e8e83a6ab73d1f2657ef',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/coding-agent/test/skillshare/pack.test.ts',
        'b07c3ca63be564c4d6deba85c92bbb9c3aaa882e008005d42358efa3ec5e1e66',
        138, '7344d09c8b91d5e514c48a3c692e130c9e77f812f089aa172dadde814ff1c5f6',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/coding-agent/test/skillshare/pack.test.ts',
        'b07c3ca63be564c4d6deba85c92bbb9c3aaa882e008005d42358efa3ec5e1e66',
        140, 'e6b8c187a64426afdbc3845fcfb552a220f6a06e5c81d8c96a33849ee00558a7',
    ),
    (
        '.private_reference/source_mirrors/can1357__oh-my-pi/packages/snapcompact/research/anthropic_api.py',
        '92b8c1aff0d3d14e7fe5b2ff29dd13bb0b4f557ede0f34a6f933f5d4caeeb72e',
        21, '2fca14961906782dc97d7cbb74e3c42d9ab8d162986c8e52594975c5b4f29eba',
    ),
    (
        '.private_reference/source_mirrors/deepseek-ai__deepseek-harness/docs/user/guide/python-sdk.md',
        '704942a7125ca0897929c0a39353763492910cd52ceed94b6dc13f3cba6374fc',
        53, '1c0a6d8c76a1800e1f1b4869a0d144dd365b6a7643955857b2d94d7acf080932',
    ),
    (
        '.private_reference/source_mirrors/deepseek-ai__deepseek-harness/docs/user/guide/python-sdk.zh.md',
        '18206141255c55c0fe0eb657d9824a20b63e70313210e9e8c6be76f328202637',
        53, '1c0a6d8c76a1800e1f1b4869a0d144dd365b6a7643955857b2d94d7acf080932',
    ),
    (
        '.private_reference/source_mirrors/deepseek-ai__deepseek-harness/packages/session/session-telemetry-otel/tests/loader-composition.e2e.ts',
        '562d82395b7c72e463cdb7b472a1a508a8a6ace0d9e38d9ae792317b586260aa',
        26, 'e15344a52b4b903ee0a17cb2ef1b818451aed8c14c4a2f0b24f072e744136b43',
    ),
    (
        '.private_reference/source_mirrors/deepseek-ai__deepseek-harness/packages/session/session-telemetry-otel/tests/fixtures/driver.ts',
        'a824de1b4c3e4f2628aead157ee483a3e0a288a4a56bf1cb246cb7413fea1a59',
        38, '015f9082dc7c51f577ca3d459d23cba6680599f6f3dc544119cd1952bcc6a83f',
    ),
    (
        '.private_reference/source_mirrors/deepseek-ai__deepseek-harness/packages/web/web-search-deepseek/tests/deepseek.spec.ts',
        'e88e37c017f0bbd4c7fe96460f32ff200b2553c0cdbf03a4d29c1a14b0e15da9',
        464, '40100fd94a02db827e0502bc36ed011e70352edad5b2029088986257fdc46b76',
    ),
    (
        '.private_reference/source_mirrors/deepseek-ai__deepseek-harness/python/sdk/tests/test_bundled_runtime.py',
        'a73ae288f6b39e74777ccdb35b93a087455c5fbe57fe061dc145495c8b27cc8d',
        80, 'e9aa4df0d7e3539b6dad9fcb9b67370c5d3b3825b5fc1cadde91e4f02df31f88',
    ),
    (
        '.private_reference/source_mirrors/heygen-com__hyperframes/packages/cli/src/telemetry/agent_runtime.test.ts',
        'bd66157746d2ea78a021b4d5a898a723c51556006ad21d8af3758f923162b5e1',
        435, '1cd659a43f8e5320725f86d834953801d418ca6cfe5635aa75c358dee0e912a4',
    ),
    (
        '.private_reference/source_mirrors/heygen-com__hyperframes/packages/cli/src/telemetry/agent_runtime.ts',
        '73f10e69ff7f8a4cc004046c2efa320e69e2770bf6c18443c5c7d004c2b8f04e',
        315, '59ff0c165a30c2fd013f825549cb59000780be312b8cb994ca757cd13da2bba6',
    ),
    (
        '.private_reference/source_mirrors/heygen-com__hyperframes__f16e509832d4/packages/cli/src/telemetry/agent_runtime.test.ts',
        'bd66157746d2ea78a021b4d5a898a723c51556006ad21d8af3758f923162b5e1',
        435, '1cd659a43f8e5320725f86d834953801d418ca6cfe5635aa75c358dee0e912a4',
    ),
    (
        '.private_reference/source_mirrors/heygen-com__hyperframes__f16e509832d4/packages/cli/src/telemetry/agent_runtime.ts',
        '73f10e69ff7f8a4cc004046c2efa320e69e2770bf6c18443c5c7d004c2b8f04e',
        315, '59ff0c165a30c2fd013f825549cb59000780be312b8cb994ca757cd13da2bba6',
    ),
    (
        '.private_reference/source_mirrors/spinabot__brigade/src/agents/auth-env-fallback.test.ts',
        '8fc847b2482848d0c63aadf3770b9c4d42a55e0d83cec1652a8534e21f26ed29',
        34, '21c648f584c5cb51c80acab2f7ba678bc4dacb9b99479dcfcb82d43e9819015b',
    ),
    (
        '.private_reference/source_mirrors/spinabot__brigade/src/providers/catalog.test.ts',
        '3e9483cb1770992f5e9ace868319eccf5c72c17911b6db3984e03d3c88305477',
        94, 'a945040098db78cf4ff8f009c3ae9634c0c44f6a60542a2d138bd293cedb6c63',
    ),
    (
        '.private_reference/source_mirrors/yc-software__qm/cli/test/docker-secrets.test.ts',
        'e7823ed9fec9efe1e65aef379c49c57ffcabf74b72612a9f9a962529cf832862',
        125, 'c7a2b7af129013909660d095df0d3a0ef4121ec61bedcfefb088bf146e527c40',
    ),
    (
        '.private_reference/source_mirrors/yc-software__qm/cli/test/fly-sandbox.test.ts',
        'e24384d811c8e052c0a20c95e2507e2dd83d11104bc31cf7ad326c73217fbc78',
        296, 'a47d28a21d359785ace044ae2696f066510393dd304a346636b7a71cc02261ad',
    ),
    (
        '.private_reference/source_mirrors/yc-software__qm/cli/test/init.test.ts',
        '1bfc1adfa583591f94f7e28bd66e2bce6e2be131eb391547087573fe7002f505',
        67, '593584b615f42498c22cb4bffcbc6155d3e9f78f3a90a425462d2172ad769335',
    ),
    (
        '.private_reference/source_mirrors/yc-software__qm/cli/test/init.test.ts',
        '1bfc1adfa583591f94f7e28bd66e2bce6e2be131eb391547087573fe7002f505',
        159, '3f1d29d87048b6a8d0ce1eeae97c14bd7667ea5e7edf1213ecd66847efad3e28',
    ),
    (
        '.private_reference/source_mirrors/yc-software__qm/cli/test/init.test.ts',
        '1bfc1adfa583591f94f7e28bd66e2bce6e2be131eb391547087573fe7002f505',
        263, 'c9cff197a30414e68603ec797a5bd7b3482d6fe33f9ad94f5d47e2871b245d0c',
    ),
    (
        '.private_reference/source_mirrors/yc-software__qm/cli/test/setup.test.ts',
        '02bf1bb87797c465658f6844b2c67667d474d55a224a7cb65719815d71dc3051',
        84, 'e6d3641d44caaf02c25ef00759e6e99fe3a09219058f63f06ad3c1006a08c892',
    ),
    (
        '.private_reference/source_mirrors/yc-software__qm/skills-seed/browse/SKILL.md',
        'b994e3f2a53279712d0be1f8873664d4a1df96b5f2d392519b7c507223c4e37b',
        250, '6ae987f7ae51a6985cd76ff7acda9661e2a2d1f20fd3caca563401fee36e847a',
    ),
    (
        '.private_reference/source_mirrors/yc-software__qm/skills-seed/browse/SKILL.md',
        'b994e3f2a53279712d0be1f8873664d4a1df96b5f2d392519b7c507223c4e37b',
        285, 'e0d259e668ea545b5d9864bcba965e9cfa83d832c6d89134694a645ce6b2c943',
    ),
    (
        '.private_reference/source_mirrors/Yeachan-Heo__oh-my-claudecode/src/cli/__tests__/launch-secure-transport.test.ts',
        '4c66c686e9fc2a718f7414bab82ef89c0a8af3e7b8fcc1c6bb098a9a0b9dc89a',
        47, 'b61914a7c82e74a6c8cc00f14ceb061b0444ae7e58a12c95ecf9745e668af466',
    ),
    (
        '.private_reference/source_mirrors/Yeachan-Heo__oh-my-claudecode/src/cli/__tests__/launch.test.ts',
        'f61746c63cf44226736e8013d7d8c6f0a59ab6025a476bf3c8039feda1c687e5',
        373, 'c0bf6c881a33168d258f6aa13fe237a900a4face0823847699aaf100b952fdb0',
    ),
    (
        '.private_reference/source_mirrors/Yeachan-Heo__oh-my-claudecode/src/cli/__tests__/launch.test.ts',
        'f61746c63cf44226736e8013d7d8c6f0a59ab6025a476bf3c8039feda1c687e5',
        2243, 'daab0d07ca670b0caf38e13bd611f01f65eff7ccbf424f942cbcc822ea9e609f',
    ),
    (
        '.private_reference/source_mirrors/Yeachan-Heo__oh-my-claudecode/src/cli/__tests__/launch.test.ts',
        'f61746c63cf44226736e8013d7d8c6f0a59ab6025a476bf3c8039feda1c687e5',
        2376, 'd80d8ba84949103c8dbe2558907333aa8e03313beba1128fc2f02a85db066a33',
    ),
    (
        '.private_reference/source_mirrors/Yeachan-Heo__oh-my-claudecode/src/__tests__/hud-api-key-source.test.ts',
        '85fe2f67098b7c2aef603c2d0adb641269b8403f3dfc29810ab682445cb2c049',
        68, '687f2befb5b8ae8d09b18012d6a3c0023773708fca4179797e22e90017f22753',
    ),
    (
        '.private_reference/source_mirrors/Yeachan-Heo__oh-my-claudecode/src/__tests__/hud-api-key-source.test.ts',
        '85fe2f67098b7c2aef603c2d0adb641269b8403f3dfc29810ab682445cb2c049',
        89, '687f2befb5b8ae8d09b18012d6a3c0023773708fca4179797e22e90017f22753',
    ),
    (
        '.private_reference/source_mirrors/Yeachan-Heo__oh-my-claudecode/src/__tests__/hud-api-key-source.test.ts',
        '85fe2f67098b7c2aef603c2d0adb641269b8403f3dfc29810ab682445cb2c049',
        103, '687f2befb5b8ae8d09b18012d6a3c0023773708fca4179797e22e90017f22753',
    ),
    (
        '.private_reference/source_mirrors/Yeachan-Heo__oh-my-claudecode/src/__tests__/hud/usage-api.test.ts',
        'a6d096d37e367c4955385a3fbbe52a44b82ce6ba6ed65943d42334612c5d723e',
        2503, '058239b2262788927772e378d1983691dddc4d32b396c4e662affcc9857373da',
    ),
    (
        '.private_reference/source_mirrors/Yeachan-Heo__oh-my-claudecode/src/__tests__/hud/usage-api.test.ts',
        'a6d096d37e367c4955385a3fbbe52a44b82ce6ba6ed65943d42334612c5d723e',
        2530, '49cb1fff4c8f4943c2914e20ebc1db1bc5857e1564d4c5aa6c6d26893b69c8f0',
    ),
    (
        '.private_reference/source_mirrors/Yeachan-Heo__oh-my-claudecode/src/__tests__/hud/usage-api.test.ts',
        'a6d096d37e367c4955385a3fbbe52a44b82ce6ba6ed65943d42334612c5d723e',
        2556, '1a68a8e18a1222b68b976dd4403604e39b4e637bc205fed9ca57852d43590933',
    ),
    (
        '.private_reference/source_mirrors/Yeachan-Heo__oh-my-claudecode/src/__tests__/rate-limit-wait/daemon-bootstrap.test.ts',
        '3f2ed09c235eaffe52b5ec7175bd0beb7f0c4be8b2e3d267daad12c29d7270f3',
        66, 'c9ff5a9f42643a2d96efd66a7c6bc23bfddbb3c32c09d5069a5888de1bda7750',
    ),
    (
        'EXTENSIONS/CVF_PLANE_FACADES/src/index.test.ts',
        '29ecd221cd233bcb08203cd10a1bc1d208d0961e54ce465f60a63448c8875b19',
        214, '160dcc51f5518252640320e81878b6bb6e7d03f7d19c0851cd27cc577fafe5c6',
    ),
    (
        'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.test.ts',
        'f65705564060daa9d913d3afd38237eaf6d6b408939f59605ea5053b52b7d47f',
        148, 'e8879763895c762d69e04c653f98f1fc7079ee0556237c6558fcf127ab7ca1d7',
    ),
    (
        'EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/edge-security.test.ts',
        'f4b47ef58cd8267297493ea514e18b591a03ea8dc447d11c6eb1c0636eb55fcf',
        19, 'a9a4746b3cf2c1268cce209ba9001ee0293eecdf57589a6febc18812dcaf8a3e',
    ),
    (
        'EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/edge-security.test.ts',
        'f4b47ef58cd8267297493ea514e18b591a03ea8dc447d11c6eb1c0636eb55fcf',
        20, '1d7de50566b406287153a1321519aa4bfeeb4fca8011b5f2f9de5ee9825a46c8',
    ),
    (
        'EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/edge-security.test.ts',
        'f4b47ef58cd8267297493ea514e18b591a03ea8dc447d11c6eb1c0636eb55fcf',
        40, '8fb842178a1cc08ddb85cc1e6004cf776dcdc77ed209a29068b7fa0060da3f6b',
    ),
    (
        'EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/edge-security.test.ts',
        'f4b47ef58cd8267297493ea514e18b591a03ea8dc447d11c6eb1c0636eb55fcf',
        44, '77ff0ec4df0ab0c5171346ff6e4481c6c575445f9d5df0e5797626bb603ad8d2',
    ),
    (
        'EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/edge-security.test.ts',
        'f4b47ef58cd8267297493ea514e18b591a03ea8dc447d11c6eb1c0636eb55fcf',
        51, '655d7f33c89582cf1d04b618f836ef13f2e23815e0fcc547c631a84d1fc6ffc1',
    ),
    (
        'EXTENSIONS/CVF_v1.8.1_ADAPTIVE_OBSERVABILITY_RUNTIME/tests/v1.8.1.test.ts',
        '7dd99ba695d324e9b25366890922f83f24d8cb29a2dd79f1b506493f776cf71c',
        27, 'fb00c5f883574b5826ba5c4a52f61072788ab209e0784471be564b2e3d52a78e',
    ),
    (
        'governance/compat/test_downstream_gate_profile.py',
        '2a42e6d66f39511349999fc44bc2b66e65a2e21945d1dd20569e8e99773bc740',
        476, '03102b6951b078f994e43dff3a617e90ff922fd4d8ca2413a63231af25064112',
    ),
}

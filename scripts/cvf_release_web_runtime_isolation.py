#!/usr/bin/env python3
"""Isolated Next.js environments for the canonical CVF release gate.

This module contains data-only subprocess policy. It performs no filesystem,
network, provider, or process action when imported.
"""

# Structural-build-only Auth.js placeholders. `auth.ts` fails closed outside
# test/development unless these values exist. They are never used for live
# authentication because the build output is not launched as a deployment.
WEB_BUILD_STRUCTURAL_ENV = {
    "NEXTAUTH_SECRET": "release-gate-structural-build-secret",
    "NEXTAUTH_URL": "http://localhost:3000",
    "GITHUB_ID": "release-gate-structural-build-placeholder",
    "GITHUB_SECRET": "release-gate-structural-build-placeholder",
    "GOOGLE_ID": "release-gate-structural-build-placeholder",
    "GOOGLE_SECRET": "release-gate-structural-build-placeholder",
}

# Production build, mock dev, and live dev must not share a Next.js distDir.
# Reuse can expose a partially rewritten JSON manifest to another process and
# surface as `Unexpected end of JSON input`, unrelated to product behavior.
WEB_BUILD_DIST_DIR = ".next-cvf-release-gate-build"

# Separate ports protect the second Playwright lane from slow Windows child-
# process teardown. `localhost` is canonical under ADIF-0035 so browser
# navigation, Auth.js callbacks, and Playwright request contexts stay aligned.
E2E_RUNTIME_ENV = {
    False: {
        "NEXT_DIST_DIR": ".next-cvf-release-gate-e2e-mock",
        "CVF_PLAYWRIGHT_PORT": "3011",
        "PLAYWRIGHT_BASE_URL": "http://localhost:3011",
    },
    True: {
        "NEXT_DIST_DIR": ".next-cvf-release-gate-e2e-live",
        "CVF_PLAYWRIGHT_PORT": "3012",
        "PLAYWRIGHT_BASE_URL": "http://localhost:3012",
    },
}

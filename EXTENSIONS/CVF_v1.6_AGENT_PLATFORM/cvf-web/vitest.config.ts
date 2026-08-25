import { defineConfig } from 'vitest/config';
import path from 'node:path';

// EAFR-R1D. Live/real-provider tests are selectable only through a deliberate
// opt-in: either `--mode live`, which the live runner script passes explicitly,
// or `CVF_ALLOW_LIVE_TESTS=1` for operators driving vitest directly. Both
// signals are intentionally distinct from any provider API key, so ambient
// credentials alone can never widen selection, and neither is a key the shared
// test setup loads from a local env file, so a developer's `.env.local` cannot
// silently enable live selection.
const DEFAULT_IGNORED_PATHS = [
    '**/node_modules/**',
    '**/dist/**',
    '**/.next/**',
];

const LIVE_TEST_PATTERNS = [
    'src/**/*.live.test.{ts,tsx}',
    'src/**/*.live.spec.{ts,tsx}',
];

export default defineConfig(({ mode }) => {
    // One resolved decision drives both barriers, so selection and activation
    // can never disagree: the exclusion below, and the `CVF_ALLOW_LIVE_TESTS`
    // value handed to test workers, come from this single value.
    const liveTestsEnabled = mode === 'live' || process.env.CVF_ALLOW_LIVE_TESTS === '1';

    return {
        resolve: {
            alias: {
                '@': path.resolve(__dirname, './src'),
            },
        },
        test: {
            environment: 'jsdom',
            setupFiles: ['./src/test/setup.ts'],
            include: ['src/**/*.{test,spec}.{ts,tsx}'],
            // EAFR-R1D selection barrier. Real-provider and other live tests must
            // never be collected by a default (non-live) run. A filename convention
            // alone proved insufficient once, so this config-level exclusion is the
            // second barrier and does not depend on any script string staying
            // correct. The exclusion lifts only under an explicit live opt-in, which
            // the live runner passes and no default run ever supplies.
            exclude: liveTestsEnabled
                ? [...DEFAULT_IGNORED_PATHS]
                : [...DEFAULT_IGNORED_PATHS, ...LIVE_TEST_PATTERNS],
            // Propagate the resolved opt-in to test workers. Vite `mode` is
            // config-time only and never reaches `process.env` inside a test file,
            // so the activation barrier in real-provider tests reads this value.
            env: {
                CVF_ALLOW_LIVE_TESTS: liveTestsEnabled ? '1' : '0',
            },
            testTimeout: 15000,
            hookTimeout: 15000,
            coverage: {
                provider: 'v8',
                reporter: ['text', 'json-summary', 'html'],
                thresholds: {
                    statements: 80,
                    branches: 70,
                    functions: 80,
                    lines: 82,
                },
                exclude: [
                    'node_modules/',
                    '.next/',
                    'src/test/',
                    '**/*.d.ts',
                ],
            },
        },
    };
});

import { afterEach, vi } from 'vitest';
import { cleanup } from '@testing-library/react';
import { loadLocalEnvFiles } from './load-local-env';
import { createProviderExecutionFetchGuard } from './provider-execution-guard';

loadLocalEnvFiles();

// Provider traffic is a delegated capability, not a consequence of collecting
// a live test or finding an ambient API key. The orchestrator must inject a
// bounded grant whose subject, delegation, provider, expiry, and call budget
// all match. Without it, known provider hosts fail before the network call.
globalThis.fetch = createProviderExecutionFetchGuard(globalThis.fetch.bind(globalThis));

afterEach(() => {
    cleanup();
    vi.clearAllMocks();
});

if (!HTMLElement.prototype.scrollIntoView) {
    HTMLElement.prototype.scrollIntoView = () => { };
}

if (!window.matchMedia) {
    window.matchMedia = ((query: string) => ({
        matches: false,
        media: query,
        onchange: null,
        addListener: () => { },
        removeListener: () => { },
        addEventListener: () => { },
        removeEventListener: () => { },
        dispatchEvent: () => false,
    })) as typeof window.matchMedia;
}

Object.defineProperty(navigator, 'clipboard', {
    value: {
        writeText: vi.fn(),
    },
    configurable: true,
});

window.alert = vi.fn();
window.confirm = vi.fn(() => true);

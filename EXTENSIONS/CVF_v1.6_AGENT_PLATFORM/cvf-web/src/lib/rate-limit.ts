import { NextRequest } from 'next/server';

type Bucket = { count: number; resetAt: number };
const WINDOW_MS = 60 * 1000;
const UNSUPPORTED_BACKEND_RETRY_AFTER_SECONDS = 60;

export type RateLimitBackendStatus = {
    schemaVersion: 'cvf.rateLimitBackend.v1';
    configuredStore: string;
    activeStore: 'memory' | 'none';
    distributed: false;
    configurationStatus:
        | 'ACTIVE_MEMORY_PROCESS_LOCAL'
        | 'BLOCKED_REDIS_ADAPTER_NOT_INSTALLED'
        | 'BLOCKED_UNSUPPORTED_STORE';
    claimBoundary: string;
};

type RateLimitResult = {
    allowed: boolean;
    retryAfterSeconds: number;
    backendStatus: RateLimitBackendStatus;
};

export interface RateLimitStore {
    consume(key: string, limit: number, now?: number): RateLimitResult;
    reset(): void;
}

export class MemoryRateLimitStore implements RateLimitStore {
    private readonly buckets = new Map<string, Bucket>();

    consume(key: string, limit: number, now = Date.now()): RateLimitResult {
        const bucket = this.buckets.get(key) || { count: 0, resetAt: now + WINDOW_MS };
        if (now > bucket.resetAt) {
            bucket.count = 0;
            bucket.resetAt = now + WINDOW_MS;
        }
        bucket.count += 1;
        this.buckets.set(key, bucket);
        if (bucket.count > limit) {
            const retryAfterSeconds = Math.max(1, Math.ceil((bucket.resetAt - now) / 1000));
            return { allowed: false, retryAfterSeconds, backendStatus: memoryBackendStatus() };
        }
        return { allowed: true, retryAfterSeconds: 0, backendStatus: memoryBackendStatus() };
    }

    reset(): void {
        this.buckets.clear();
    }
}

const userStore = new MemoryRateLimitStore();
const providerStore = new MemoryRateLimitStore();

function limits() {
    return {
        maxRequests: Number(process.env.CVF_RATE_LIMIT ?? 30),
        providerQuota: Number(process.env.CVF_PROVIDER_QUOTA_PER_MIN ?? 30),
    };
}

function getClientIp(headers: Headers): string {
    const forwarded = headers.get('x-forwarded-for') || headers.get('x-real-ip');
    if (forwarded) {
        return forwarded.split(',')[0].trim();
    }
    return headers.get('cf-connecting-ip') || 'unknown';
}

function memoryBackendStatus(): RateLimitBackendStatus {
    return {
        schemaVersion: 'cvf.rateLimitBackend.v1',
        configuredStore: 'memory',
        activeStore: 'memory',
        distributed: false,
        configurationStatus: 'ACTIVE_MEMORY_PROCESS_LOCAL',
        claimBoundary: 'process_local_memory_only_no_distributed_rate_limit_claim',
    };
}

function blockedBackendStatus(configuredStore: string): RateLimitBackendStatus {
    if (configuredStore === 'redis') {
        return {
            schemaVersion: 'cvf.rateLimitBackend.v1',
            configuredStore,
            activeStore: 'none',
            distributed: false,
            configurationStatus: 'BLOCKED_REDIS_ADAPTER_NOT_INSTALLED',
            claimBoundary: 'redis_requested_but_no_adapter_installed_no_distributed_rate_limit_claim',
        };
    }
    return {
        schemaVersion: 'cvf.rateLimitBackend.v1',
        configuredStore,
        activeStore: 'none',
        distributed: false,
        configurationStatus: 'BLOCKED_UNSUPPORTED_STORE',
        claimBoundary: 'unsupported_rate_limit_store_no_distributed_rate_limit_claim',
    };
}

export function getRateLimitBackendStatus(env: NodeJS.ProcessEnv = process.env): RateLimitBackendStatus {
    const configuredStore = (env.CVF_RATE_LIMIT_STORE ?? 'memory').trim().toLowerCase() || 'memory';
    if (configuredStore === 'memory') {
        return memoryBackendStatus();
    }
    return blockedBackendStatus(configuredStore);
}

function blockedResult(backendStatus: RateLimitBackendStatus): RateLimitResult {
    return {
        allowed: false,
        retryAfterSeconds: UNSUPPORTED_BACKEND_RETRY_AFTER_SECONDS,
        backendStatus,
    };
}

export function getRateLimiter() {
    return {
        backendStatus() {
            return getRateLimitBackendStatus();
        },
        consume(request: NextRequest, userId?: string, provider?: string) {
            const backendStatus = getRateLimitBackendStatus();
            if (backendStatus.configurationStatus !== 'ACTIVE_MEMORY_PROCESS_LOCAL') {
                return blockedResult(backendStatus);
            }
            const { maxRequests, providerQuota } = limits();
            const key = userId || getClientIp(request.headers);
            const res1 = userStore.consume(key, maxRequests);
            if (!res1.allowed) return res1;
            if (provider) {
                const res2 = providerStore.consume(`${key}:${provider}`, providerQuota);
                if (!res2.allowed) return res2;
            }
            return { allowed: true, retryAfterSeconds: 0, backendStatus };
        }
    };
}

export function resetRateLimitStoresForTest(): void {
    userStore.reset();
    providerStore.reset();
}

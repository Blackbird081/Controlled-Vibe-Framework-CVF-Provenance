import { mkdtempSync, rmSync } from 'fs';
import { tmpdir } from 'os';
import { join, resolve } from 'path';
import { afterEach, describe, expect, it } from 'vitest';
import { listGovernanceJobs, redactGovernanceJobOutput, submitGovernanceJob } from './web-governance-jobs';

const roots: string[] = [];

function makeContext() {
    const repoRoot = mkdtempSync(join(tmpdir(), 'cvf-jobs-'));
    roots.push(repoRoot);
    let id = 0;
    return {
        repoRoot,
        auditPath: resolve(repoRoot, '.cvf', 'runtime', 'web-governance-jobs.jsonl'),
        now: () => '2026-05-08T00:00:00.000Z',
        idFactory: () => `id-${++id}`,
    };
}

describe('web governance jobs', () => {
    afterEach(() => {
        for (const root of roots.splice(0)) {
            rmSync(root, { recursive: true, force: true });
        }
    });

    it('runs an authorized allowlisted diagnostic job with fixed argv and audit events', async () => {
        const context = makeContext();
        const result = await submitGovernanceJob({
            jobType: 'cvf_doctor',
            role: 'operator',
            requestedBy: 'tester',
            authMode: 'authenticated',
            localMode: false,
            requestIpClass: 'loopback',
        }, {
            ...context,
            runCommand: async (command, argv) => ({
                stdout: JSON.stringify({ ok: true, command, argv }),
                stderr: '',
                exitCode: 0,
                timedOut: false,
                errorClass: null,
            }),
        });

        expect(result.status).toBe('succeeded');
        expect(result.latestEvent.fixedArgv).toEqual(['scripts/cvf_doctor.py', '--json']);
        const audit = listGovernanceJobs(context);
        expect(audit.events.map((event) => event.eventType)).toEqual(['requested', 'running', 'succeeded']);
        expect(audit.jobs[0].status).toBe('succeeded');
    });

    it('blocks read-only roles before launching a job and audits the policy block', async () => {
        const context = makeContext();
        let launched = false;
        const result = await submitGovernanceJob({
            jobType: 'provider_check',
            provider: 'alibaba',
            role: 'viewer',
            requestedBy: 'viewer',
            authMode: 'authenticated',
            localMode: false,
            requestIpClass: 'loopback',
        }, {
            ...context,
            runCommand: async () => {
                launched = true;
                return { stdout: '', stderr: '', exitCode: 0, timedOut: false, errorClass: null };
            },
        });

        expect(result.status).toBe('blocked_by_policy');
        expect(result.decisionReason).toBe('read_only_role_cannot_trigger');
        expect(launched).toBe(false);
        expect(listGovernanceJobs(context).events.map((event) => event.eventType)).toEqual(['requested', 'blocked_by_policy']);
    });

    it('blocks invalid provider lane input before launching provider checks', async () => {
        const context = makeContext();
        let launched = false;
        const result = await submitGovernanceJob({
            jobType: 'provider_check',
            provider: 'not-a-provider',
            role: 'operator',
            requestedBy: 'operator',
            authMode: 'authenticated',
            localMode: false,
            requestIpClass: 'loopback',
        }, {
            ...context,
            runCommand: async () => {
                launched = true;
                return { stdout: '', stderr: '', exitCode: 0, timedOut: false, errorClass: null };
            },
        });

        expect(result.status).toBe('blocked_by_policy');
        expect(result.decisionReason).toBe('invalid_provider');
        expect(launched).toBe(false);
    });

    it('runs provider checks as live validation with fixed argv', async () => {
        const context = makeContext();
        const result = await submitGovernanceJob({
            jobType: 'provider_check',
            provider: 'deepseek',
            role: 'operator',
            requestedBy: 'operator',
            authMode: 'authenticated',
            localMode: false,
            requestIpClass: 'loopback',
        }, {
            ...context,
            runCommand: async (_command, argv) => ({
                stdout: JSON.stringify({ status: 'LIVE_VALIDATED', argv }),
                stderr: '',
                exitCode: 0,
                timedOut: false,
                errorClass: null,
            }),
        });

        expect(result.status).toBe('succeeded');
        expect(result.latestEvent.handlerId).toBe('scripts.cvf_provider_check.json.live');
        expect(result.latestEvent.fixedArgv).toEqual(['scripts/cvf_provider_check.py', '--provider', 'deepseek', '--live', '--json']);
    });

    it('allows anonymous local mode only for read-only diagnostics', async () => {
        const context = makeContext();
        const allowed = await submitGovernanceJob({
            jobType: 'cvf_doctor',
            role: 'anonymous_local',
            requestedBy: 'local',
            authMode: 'anonymous_local',
            localMode: true,
            requestIpClass: 'loopback',
        }, {
            ...context,
            runCommand: async () => ({ stdout: 'ok', stderr: '', exitCode: 0, timedOut: false, errorClass: null }),
        });
        const blocked = await submitGovernanceJob({
            jobType: 'provider_check',
            provider: 'alibaba',
            role: 'anonymous_local',
            requestedBy: 'local',
            authMode: 'anonymous_local',
            localMode: true,
            requestIpClass: 'loopback',
        }, context);

        expect(allowed.status).toBe('succeeded');
        expect(blocked.status).toBe('blocked_by_policy');
        expect(blocked.decisionReason).toBe('anonymous_local_trigger_not_allowed');
    });

    it('redacts known secrets and high entropy tokens before persistence', async () => {
        const context = makeContext();
        const secret = 'dashscope-super-secret-token-12345678901234567890';
        const result = await submitGovernanceJob({
            jobType: 'release_gate_dry_readiness',
            role: 'owner',
            requestedBy: 'owner',
            authMode: 'authenticated',
            localMode: false,
            requestIpClass: 'loopback',
        }, {
            ...context,
            runCommand: async () => ({
                stdout: `DASHSCOPE_API_KEY=${secret} token=${secret}`,
                stderr: '',
                exitCode: 0,
                timedOut: false,
                errorClass: null,
            }),
        });

        expect(result.latestEvent.stdoutSummary).not.toContain(secret);
        expect(result.latestEvent.stdoutSummary).toContain('[REDACTED]');
    });

    it('marks timed out commands as timed_out', async () => {
        const context = makeContext();
        let observedTimeoutMs = 0;
        const result = await submitGovernanceJob({
            jobType: 'docs_governance_check',
            role: 'admin',
            requestedBy: 'admin',
            authMode: 'authenticated',
            localMode: false,
            requestIpClass: 'loopback',
            timeoutMsOverride: 5,
        }, {
            ...context,
            runCommand: async (_command, _argv, options) => {
                observedTimeoutMs = options.timeoutMs;
                return {
                stdout: '',
                stderr: 'timeout',
                exitCode: null,
                timedOut: true,
                errorClass: 'timeout',
                };
            },
        });

        expect(result.status).toBe('timed_out');
        expect(observedTimeoutMs).toBe(5);
        expect(result.latestEvent.timeoutMs).toBe(5);
        expect(result.latestEvent.timedOut).toBe(true);
        expect(result.latestEvent.errorClass).toBe('timeout');
    });

    it('redacts standalone output helper without needing a job run', () => {
        expect(redactGovernanceJobOutput('DEEPSEEK_API_KEY=abc123superlongsecretvalue', {
            NODE_ENV: 'test',
            DEEPSEEK_API_KEY: 'abc123superlongsecretvalue',
        } as NodeJS.ProcessEnv)).toBe('DEEPSEEK_API_KEY=[REDACTED]');
    });
});

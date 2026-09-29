import { afterEach, describe, expect, it } from 'vitest';
import { execFileSync } from 'node:child_process';
import { existsSync, mkdtempSync, mkdirSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import {
  consumeRepositoryGrantInvocation,
  loadCommittedRepositoryCapabilityGrant,
  resolveCanonicalRepositoryRoot,
} from './repository-capability-owner.source';

const GRANT_V1_REF = 'governance/capability-grants/cadp-ai-t2a-owner-binding-grant.v1.json';
const GRANT_REF = 'governance/capability-grants/cadp-ai-t2a-owner-binding-grant.v2.json';
const REOPEN_STEP = process.env.CVF_T2A_REOPEN_STEP;
const REOPEN_INVOCATION_ID = process.env.CVF_T2A_REOPEN_INVOCATION_ID;
const cleanup: string[] = [];

afterEach(() => {
  while (cleanup.length) rmSync(cleanup.pop()!, { recursive: true, force: true });
});

function useFreshState(): void {
  // Binding uses the canonical repository-private state path; callers cannot
  // redirect or reset it with cwd, a function argument, or an environment key.
}

describe('committed repository capability source', () => {
  it('keeps drifted v1 fail-closed while accepting additive v2', () => {
    expect(() => loadCommittedRepositoryCapabilityGrant(GRANT_V1_REF)).toThrow();
    const grant = loadCommittedRepositoryCapabilityGrant(GRANT_REF);
    expect(grant.grantId).toBe('cadp-ai-t2a-owner-binding-grant-v2');
    expect(grant.workOrderVersion).toBe('2026-08-13.2');
    expect(grant.grantHash).toMatch(/^[0-9a-f]{64}$/);
  });

  it('reads the exact committed grant and verifies every pinned artifact hash', () => {
    useFreshState();
    const grant = loadCommittedRepositoryCapabilityGrant(GRANT_REF);
    expect(grant.repositoryId).toBe('CVF_PRIVATE_PROVENANCE');
    expect(grant.artifacts.map(({ artifactType }) => artifactType).sort())
      .toEqual(['freeze', 'receipt', 'review', 'work_order']);
    expect(Object.isFrozen(grant)).toBe(true);
    expect(Object.isFrozen(grant.artifacts)).toBe(true);
  });

  it('rejects caller objects, traversal, absolute paths, dirty-only and uncommitted paths', () => {
    useFreshState();
    for (const input of [
      {} as unknown, '../grant.json', 'governance/capability-grants/../x.json',
      'C:/tmp/grant.json', 'governance\\capability-grants\\x.json',
      'governance/capability-grants/not-committed.json',
    ]) expect(() => loadCommittedRepositoryCapabilityGrant(input)).toThrow();
  });

  it('derives repository identity from module location and ignores alternate Git environment', () => {
    useFreshState();
    const alternate = mkdtempSync(join(tmpdir(), 'cvf-alternate-repo-'));
    cleanup.push(alternate);
    const alternateGit = join(alternate, '.git');
    mkdirSync(alternateGit);
    const canonical = resolveCanonicalRepositoryRoot();
    const prior = {
      GIT_DIR: process.env.GIT_DIR,
      GIT_WORK_TREE: process.env.GIT_WORK_TREE,
      GIT_OBJECT_DIRECTORY: process.env.GIT_OBJECT_DIRECTORY,
    };
    try {
      process.env.GIT_DIR = alternateGit;
      process.env.GIT_WORK_TREE = alternate;
      process.env.GIT_OBJECT_DIRECTORY = join(alternateGit, 'objects');
      expect(resolveCanonicalRepositoryRoot()).toBe(canonical);
      expect(loadCommittedRepositoryCapabilityGrant(GRANT_REF).repositoryId).toBe('CVF_PRIVATE_PROVENANCE');
    } finally {
      for (const [key, value] of Object.entries(prior)) {
        if (value === undefined) delete process.env[key]; else process.env[key] = value;
      }
    }
  });

  it('does not allow an environment variable to redirect durable owner state', () => {
    const alternate = mkdtempSync(join(tmpdir(), 'cvf-owner-state-redirect-'));
    cleanup.push(alternate);
    const decoy = join(alternate, 'decoy.db');
    const prior = process.env.CVF_CAPABILITY_OWNER_STATE_PATH;
    try {
      process.env.CVF_CAPABILITY_OWNER_STATE_PATH = decoy;
      expect(loadCommittedRepositoryCapabilityGrant(GRANT_REF).repositoryId).toBe('CVF_PRIVATE_PROVENANCE');
      expect(existsSync(decoy)).toBe(false);
    } finally {
      if (prior === undefined) delete process.env.CVF_CAPABILITY_OWNER_STATE_PATH;
      else process.env.CVF_CAPABILITY_OWNER_STATE_PATH = prior;
    }
  });

  it('preserves durable duplicate and contiguous retry behavior for v2', () => {
    const grant = loadCommittedRepositoryCapabilityGrant(GRANT_REF);
    const invocationId = `cadp-t2a-r1-${process.pid}-${Date.now()}`;
    expect(() => consumeRepositoryGrantInvocation(grant, invocationId, 0)).not.toThrow();
    expect(() => consumeRepositoryGrantInvocation(grant, invocationId, 0)).toThrow();
    expect(() => consumeRepositoryGrantInvocation(grant, invocationId, 1)).not.toThrow();
    expect(() => consumeRepositoryGrantInvocation(grant, invocationId, 3)).toThrow();
    expect(() => consumeRepositoryGrantInvocation(grant, invocationId, 2)).not.toThrow();
  });

  it('proves durable replay protection after an independent process reopen', () => {
    if (REOPEN_STEP) return;
    const invocationId = `cadp-t2a-reopen-${process.pid}-${Date.now()}`;
    const vitestCli = join(process.cwd(), 'node_modules', 'vitest', 'vitest.mjs');
    for (const step of ['consume', 'reopen'] as const) {
      execFileSync(process.execPath, [
        vitestCli, 'run', '--pool', 'forks',
        'src/contracts/repository-capability-owner.source.test.ts',
        '-t', 'executes one durable reopen step',
      ], {
        cwd: process.cwd(),
        env: {
          ...process.env,
          CVF_T2A_REOPEN_STEP: step,
          CVF_T2A_REOPEN_INVOCATION_ID: invocationId,
        },
        stdio: 'pipe',
      });
    }
  });

  it('executes one durable reopen step', () => {
    if (!REOPEN_STEP) return;
    expect(REOPEN_INVOCATION_ID).toBeTruthy();
    const grant = loadCommittedRepositoryCapabilityGrant(GRANT_REF);
    if (REOPEN_STEP === 'consume') {
      expect(() => consumeRepositoryGrantInvocation(grant, REOPEN_INVOCATION_ID!, 0)).not.toThrow();
      return;
    }
    expect(REOPEN_STEP).toBe('reopen');
    expect(() => consumeRepositoryGrantInvocation(grant, REOPEN_INVOCATION_ID!, 0)).toThrow();
    expect(() => consumeRepositoryGrantInvocation(grant, REOPEN_INVOCATION_ID!, 1)).not.toThrow();
  });
});

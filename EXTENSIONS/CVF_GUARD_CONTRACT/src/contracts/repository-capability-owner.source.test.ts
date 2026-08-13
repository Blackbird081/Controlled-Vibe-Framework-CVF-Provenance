import { afterEach, describe, expect, it } from 'vitest';
import { existsSync, mkdtempSync, mkdirSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import {
  loadCommittedRepositoryCapabilityGrant,
  resolveCanonicalRepositoryRoot,
} from './repository-capability-owner.source';

const GRANT_REF = 'governance/capability-grants/cadp-ai-t2a-owner-binding-grant.v1.json';
const cleanup: string[] = [];

afterEach(() => {
  while (cleanup.length) rmSync(cleanup.pop()!, { recursive: true, force: true });
});

function useFreshState(): void {
  // Binding uses the canonical repository-private state path; callers cannot
  // redirect or reset it with cwd, a function argument, or an environment key.
}

describe('committed repository capability source', () => {
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
});

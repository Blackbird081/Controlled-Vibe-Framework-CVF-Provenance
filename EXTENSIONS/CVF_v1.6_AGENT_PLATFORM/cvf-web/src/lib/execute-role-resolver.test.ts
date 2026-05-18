import { describe, expect, it } from 'vitest';
import {
  resolveExecutionCVFRole,
  resolveExecutionOutputClass,
} from './execute-role-resolver';

describe('execute role resolver', () => {
  it('maps service-token execution to SERVICE_AGENT boundary role', () => {
    expect(resolveExecutionCVFRole(null, true)).toEqual({
      allowed: true,
      role: 'SERVICE_AGENT',
      permissionRole: 'SERVICE_AGENT',
      source: 'service_token',
      inputRole: 'service',
    });
  });

  it('maps owner and admin RBAC roles to OPERATOR', () => {
    expect(resolveExecutionCVFRole({ role: 'owner' }, false).permissionRole).toBe('OPERATOR');
    expect(resolveExecutionCVFRole({ role: 'admin' }, false).permissionRole).toBe('OPERATOR');
  });

  it('maps developer, reviewer, and viewer RBAC roles to bounded CVF roles', () => {
    expect(resolveExecutionCVFRole({ role: 'developer' }, false).permissionRole).toBe('BUILDER');
    expect(resolveExecutionCVFRole({ role: 'reviewer' }, false).permissionRole).toBe('REVIEWER');
    expect(resolveExecutionCVFRole({ role: 'viewer' }, false).permissionRole).toBe('OBSERVER');
  });

  it('denies unknown and missing roles without widening authority', () => {
    expect(resolveExecutionCVFRole({ role: 'intern' }, false)).toMatchObject({
      allowed: false,
      role: null,
      permissionRole: null,
      source: 'denied',
      inputRole: 'intern',
    });
    expect(resolveExecutionCVFRole({}, false)).toMatchObject({
      allowed: false,
      role: null,
      permissionRole: null,
      source: 'denied',
      inputRole: null,
    });
  });

  it('maps app_builder_complete to artifact output class', () => {
    expect(resolveExecutionOutputClass('app_builder_complete', 'development', 'simple')).toEqual({
      outputClass: 'artifact',
      source: 'template_id',
    });
  });

  it('keeps code mode as the bounded code_patch route-test output class', () => {
    expect(resolveExecutionOutputClass('unknown', 'development', 'code')).toEqual({
      outputClass: 'code_patch',
      source: 'default',
    });
  });
});

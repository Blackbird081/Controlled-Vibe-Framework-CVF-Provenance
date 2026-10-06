const TEXT_FIELDS = [
    'templateId', 'templateName', 'intent', 'provider', 'model', 'mode',
    'imageUrl', 'imageBase64', 'mimeType', 'cvfPhase', 'cvfRiskLevel',
    'governanceFamily', 'qbsFamily', 'skillPreflightDeclaration',
    'skillPreflightRecordRef', 'knowledgeContext', 'knowledgeCollectionId', 'approvalId',
] as const;

function isRecord(value: unknown): value is Record<string, unknown> {
    return value !== null && typeof value === 'object' && !Array.isArray(value);
}

/** Shape checks before existing normalization; downstream owners retain semantic/authority checks. */
export function validateExecuteRequestShape(value: unknown): string | undefined {
    if (!isRecord(value)) return 'Execution payload must be a JSON object.';
    for (const field of TEXT_FIELDS) {
        if (value[field] != null && typeof value[field] !== 'string') return `${field} must be a string.`;
    }
    if (typeof value.templateName !== 'string' || !value.templateName.trim() ||
        typeof value.intent !== 'string' || !value.intent.trim() || value.inputs === undefined) {
        return 'Missing required fields: templateName, inputs, intent';
    }
    if (!isRecord(value.inputs)) return 'inputs must be a JSON object.';
    // Preserve legacy scalar-to-string normalization while rejecting nested structures.
    if (Object.values(value.inputs).some(input => input !== null && !['string', 'number', 'boolean'].includes(typeof input))) {
        return 'Input values must be scalar text, numbers, booleans or null.';
    }
    if (value.skillPreflightPassed != null && typeof value.skillPreflightPassed !== 'boolean') return 'skillPreflightPassed must be a boolean.';
    for (const field of ['skillIds', 'fileScope']) {
        if (value[field] != null && (!Array.isArray(value[field]) || !value[field].every(item => typeof item === 'string'))) {
            return `${field} must be a string array.`;
        }
    }
    return undefined;
}

import {
  WEIGHTING_DOCTRINE_VERSION,
  WEIGHTING_DOCTRINE_CONFIDENCE_GATE,
  WEIGHTING_DOCTRINE_WEIGHTS,
  applyWeightingDoctrine,
  type WeightingDoctrineOutcome,
} from 'cvf-learning-plane-foundation';
import { TruthModelContract } from 'cvf-learning-plane-foundation';
import type { PatternInsight } from 'cvf-learning-plane-foundation';

export const LEARNING_PLANE_READOUT_VERSION = "cvf.learningPlaneReadout.wd1.v1";

export interface LearningPlaneReadout {
  contractVersion: typeof LEARNING_PLANE_READOUT_VERSION;
  doctrineVersion: typeof WEIGHTING_DOCTRINE_VERSION;
  confidenceGate: typeof WEIGHTING_DOCTRINE_CONFIDENCE_GATE;
  weights: typeof WEIGHTING_DOCTRINE_WEIGHTS;
  outcome: WeightingDoctrineOutcome;
  compositeScore: number;
  scoreClass: string;
  isProvisional: boolean;
  advisoryNote: string;
  runtimeScoringAuthorized: false;
}

/**
 * Builds a LearningPlaneReadout for inclusion in /api/execute ALLOW responses.
 *
 * Uses the current execution as a single synthetic insight (ACCEPT/HEALTHY)
 * to represent the live session. The actual doctrine outcome depends on the
 * historical confidence level passed in.
 *
 * confidenceLevel defaults to 0.7 (LP-LP2 calibrated value) when not provided,
 * which means the doctrine is applied (isProvisional=false) by default for
 * sessions with sufficient calibration history.
 */
export function buildLearningPlaneReadout(
  role: string,
  confidenceLevel = 0.7,
): LearningPlaneReadout {
  const insight: PatternInsight = {
    insightId: `lp-readout-${Date.now()}`,
    analyzedAt: new Date().toISOString(),
    sourceLedgerId: `route-execute-${role}`,
    dominantPattern: 'ACCEPT',
    acceptRate: 1.0,
    retryRate: 0,
    escalateRate: 0,
    rejectRate: 0,
    healthSignal: 'HEALTHY',
    summary: `Live governed execution via /api/execute. Role: ${role}.`,
    insightHash: `route-hash-${role}-${Date.now()}`,
  };

  const model = new TruthModelContract({
    computeConfidence: () => confidenceLevel,
  }).build([insight]);

  const doctrineResult = applyWeightingDoctrine(model);

  return {
    contractVersion: LEARNING_PLANE_READOUT_VERSION,
    doctrineVersion: WEIGHTING_DOCTRINE_VERSION,
    confidenceGate: WEIGHTING_DOCTRINE_CONFIDENCE_GATE,
    weights: WEIGHTING_DOCTRINE_WEIGHTS,
    outcome: doctrineResult.outcome,
    compositeScore: doctrineResult.truthScore.compositeScore,
    scoreClass: doctrineResult.truthScore.scoreClass,
    isProvisional: doctrineResult.truthScore.isProvisional,
    advisoryNote: doctrineResult.doctrineNote,
    runtimeScoringAuthorized: false,
  };
}

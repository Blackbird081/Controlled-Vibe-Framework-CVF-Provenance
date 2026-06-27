# CVF Agent Workspace Review Queue Pointer

Memory class: POINTER_RECORD

Status: ACTIVE_QUEUE_POINTER

docType: reference

Queue mode: QUEUE_SKELETON_ONLY

Mapped lane: `review`

## Purpose

Identify the future review queue-family location without creating runtime queue
records.

## Scope / Target / Owner Boundary

Target: review queue-family pointer.

Owner boundary: documentation pointer only. This folder does not store
executable queue records, schedule work, call providers, public-sync, edit
registries, or claim production/public readiness.

## Claim Boundary

This pointer is structural only. It does not authorize runtime execution,
provider/live proof, UI, public-sync, registry edits, production readiness, or
public readiness.

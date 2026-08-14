# Runbook: queue dependency unavailable

## Trigger and impact

Use when readiness or `lab_dependency_ready` reports that the queue cannot be
used. Liveness may remain healthy while job submissions fail.

## Diagnose

1. Confirm `/health/live` and `/health/ready` separately.
2. Inspect Redis container state, health output, and recent logs.
3. Resolve the configured `REDIS_HOST` from inside the API container.
4. Test TCP connectivity on port 6379 without exposing Redis to the host.
5. Check whether failures began after a configuration or network change.

## Mitigate

TODO: document restart, rollback, or configuration recovery conditions. Do not
restart blindly before preserving evidence.

## Verify

Readiness returns 200, a new job returns 202, the worker records completion,
Prometheus shows dependency readiness, and no unexpected Redis port is exposed.

## Escalate

Escalate before any action that discards persistent queue data. This training
stack is ephemeral, but a production queue may not be.

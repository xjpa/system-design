# Runbook: API unavailable

## Trigger and impact

Use when the API target cannot be scraped or clients cannot connect. Confirm
impact from a client perspective before assuming the alert is correct.

## Diagnose

1. Record incident start time and the exact failing request.
2. Check container state and recent events without restarting anything.
3. Check API logs from five minutes before the first symptom.
4. Test liveness from the host and from the Prometheus container.
5. Check port publication, network membership, and resource pressure.

## Mitigate

TODO: write the smallest reversible mitigation for the failure you observed.

## Verify

Run liveness, readiness, job submission, metrics scrape, and worker-log checks.
Watch for recurrence before closing. Record commands and timestamps.

## Escalate

Escalate when mitigation risks data loss, requires credentials you do not own,
or the same symptom returns after one rollback. Preserve logs and failed state.

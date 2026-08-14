# Deployment and rollback record

## Preconditions

- Artifact reference and digest:
- Target environment:
- Required approval:
- Configuration changes:

## Deploy

Record the command or workflow run, start/end timestamps, and observed revision.
Do not copy credentials, account IDs, or temporary addresses.

## Verify

Record liveness, readiness, one submitted job, worker completion, scrape health,
and error signal results.

## Rollback

Name the prior immutable artifact and the exact rollback mechanism. Record the
same verification evidence after rollback.

## Teardown

Record local stack, local cluster, and optional cloud cleanup. Explain what the
automated state check can prove and what still requires console inspection.

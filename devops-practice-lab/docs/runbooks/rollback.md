# Runbook: application rollback

1. Record the failing image digest/tag and symptom.
2. Identify the last image that passed smoke checks; never use mutable `latest`.
3. Redeploy that exact image through the same deployment mechanism.
4. Verify liveness, readiness, one job, worker completion, and error metrics.
5. Monitor for recurrence and preserve the failed image for investigation.
6. Open follow-up work; rollback restores service but does not explain failure.

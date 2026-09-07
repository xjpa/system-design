# 05 — Observability and incident response

## Outcome

You can move from a user-visible symptom to logs, metrics, dependency evidence,
a tested recovery, and a blameless account of what should improve.

## Mental model

Monitoring asks known questions with dashboards and alerts. Observability lets
you ask new questions using emitted state. An alert should identify an
actionable symptom, carry severity and ownership, and link to a runbook. It
should not claim a root cause before investigation.

## Lessons

1. Start the full stack and use `make observe`. Generate jobs, then find request
   count, dependency readiness, worker completion logs, and scrape health.
2. Complete `alert.exercise.yml`; run `python3 check.py`.
3. Without reading `scripts/incident.py`, have someone choose `dependency`,
   `worker`, `api`, `latency`, `errors`, or `configuration`. Record a timeline
   while diagnosing. Use `cpu` and `disk` for safe evidence-only drills.
4. Form two hypotheses before changing anything. Test the cheapest, safest one
   first. Recover, run smoke checks, then watch metrics stabilize.
5. Fill the incident template without blaming a person or listing “be more
   careful” as corrective action.

## Operational artifacts

- Complete both runbooks under `docs/runbooks/`.
- Copy `docs/templates/postmortem.md` to `artifacts/05-postmortem.md`.
- Export or screenshot the dashboard only after recording the useful queries in
  text so the evidence remains reviewable.

## Reflection

- Why can a dashboard be green while users still fail?
- What is the difference between mitigation and root-cause correction?
- Which signal would have shortened detection or diagnosis?

## Definition of done

The alert check passes, three injected scenarios are recovered from symptoms,
each recovery is verified, and the postmortem assigns concrete system actions.

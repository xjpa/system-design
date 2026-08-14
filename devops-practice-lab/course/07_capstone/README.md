# 07 — Capstone: operate a service

## Mission

Take responsibility for the lab service through its complete lifecycle. Do not
follow a command transcript: use the runbooks, automation, evidence, and mental
models built in earlier modules.

## Required demonstration

1. Start from a clean clone and run the workstation check.
2. Run unit and repository checks; build and scan an immutable image.
3. Deploy locally through Compose and prove liveness, readiness, queue flow,
   metrics collection, and structured logging.
4. Explain the pipeline from commit to protected manual deployment and perform
   a local rollback to a previous immutable tag.
5. Produce and review a Terraform plan. Optionally execute the guarded AWS
   lifecycle; local validation remains sufficient when cloud spend is declined.
6. Deploy to kind, diagnose a failed rollout from events, and recover it.
7. Ask another person to inject an unknown supported incident. Keep a timeline,
   mitigate it, verify recovery, and write the postmortem.
8. Run `make verify`, remove local/cloud resources, and record teardown evidence.

## Portfolio review

All required files are listed in `portfolio-checklist.md`. Remove placeholders,
private information, raw credentials, account identifiers, and temporary IPs
before committing. Diagrams must show trust and dependency boundaries, not only
tool logos.

## Competency rubric

Score each item 0 (cannot explain), 1 (can follow with help), or 2 (can perform
and explain independently):

| Competency | 0–2 |
| --- | ---: |
| Inspect Linux processes, permissions, capacity, and logs | |
| Diagnose DNS, TCP, HTTP, and dependency failures | |
| Write defensive Bash or Python automation | |
| Build and harden a container image | |
| Explain CI gates, artifacts, promotion, and rollback | |
| Read and safely apply Terraform plans | |
| Write idempotent configuration management | |
| Apply IAM, network, secret, and cost boundaries | |
| Query logs and metrics and design actionable alerts | |
| Diagnose and roll back a Kubernetes deployment | |
| Lead a structured incident investigation | |
| Write clear runbooks, decisions, and postmortems | |

Aim for at least 19/24 with no zero. A lower score is a repeat map, not a
failure. Redo the weakest incident or exercise without viewing prior work.

## Interview review

Explain aloud:

1. Trace a commit to a running container and identify every trust boundary.
2. A process is alive but traffic receives 503. What do you inspect and why?
3. How do Terraform and Ansible responsibilities differ in this lab?
4. How would you reduce deployment risk without slowing all feedback?
5. What does an alert prove, and what does it not prove?
6. What would change for multiple regions, persistent data, or strict uptime?

## Definition of done

The system is reproducible, observable, recoverable, documented, free of
secrets and private target information, and fully torn down when not in use.

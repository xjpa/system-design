# DevOps Practice Lab

Learn to deliver and operate a small service: inspect Linux systems, diagnose
networks, write automation, build containers, create CI/CD pipelines, define
cloud infrastructure, monitor behavior, and recover from incidents.

The required course runs locally. The AWS exercises are optional, deliberately
short-lived, and include teardown checks. Nothing in this lab promises that a
cloud resource is free.

## How the lab works

Each numbered module follows the same loop:

1. Read the module README and predict what each command will do.
2. Run the worked example.
3. Complete one `TODO` at a time.
4. Run the named check and diagnose its first failure.
5. Produce the operational artifact before moving on.

The sample application is already written. It is intentionally small because
the subject is operating software, not application feature development.

## Start here

Requirements: Python 3.10+, Git, Make, curl, and Docker with Compose. Terraform,
Ansible, AWS CLI, kubectl, and kind are needed only in their respective modules.

```bash
cd devops-practice-lab
make doctor
make test
make build
make up
make smoke
make down
```

Copy `.env.example` to `.env` only when you want to override defaults. Never
commit credentials or a populated `.env` file.

## Learning path

| Order | Module | Outcome |
| ---: | --- | --- |
| 00 | `workstation_and_linux` | Inspect processes, files, permissions, and environment |
| 01 | `networking_and_scripting` | Diagnose DNS, ports, HTTP, and automate checks |
| 02 | `containers` | Build and run a least-privilege containerized service |
| 03 | `ci_cd` | Test, scan, publish, deploy, and roll back predictably |
| 04 | `infrastructure_and_cloud` | Provision a short-lived AWS host and configure it |
| 05 | `observability_and_incidents` | Use logs, metrics, dashboards, alerts, and incident practice |
| 06 | `kubernetes_fundamentals` | Deploy and roll back the service on a local cluster |
| 07 | `capstone` | Demonstrate an end-to-end operations workflow |

Recommended pace is six weeks at 6–8 hours per week. For four weeks, pair
00–01, 02–03, 04–05, and 06–07.

## The system you operate

```text
client -> API -> Redis queue -> worker
            \\-> Prometheus -> Grafana
logs ----------------> Loki
```

The API exposes:

- `GET /health/live` — process liveness
- `GET /health/ready` — dependency readiness
- `GET /metrics` — Prometheus text metrics
- `POST /jobs` — enqueue a small JSON job

The service supports safe failure injection with environment variables so you
can practice diagnosis without damaging your machine.

## Stable commands

```text
make doctor             inspect local prerequisites
make test               run application unit tests
make build              build the application image
make up / make down     start or stop the local platform
make smoke              verify the running platform
make observe            print dashboard and query locations
make incident SCENARIO=dependency
make recover            remove failure overrides and restart
make verify             run repository-level offline checks
make aws-plan           preview optional AWS resources
make aws-apply          create them after explicit acknowledgement
make aws-destroy        remove lab-managed resources
```

## Cost and safety boundary

The AWS track creates a VPC, one public subnet, security controls, an IAM
instance profile, and one small EC2 instance. It intentionally avoids NAT
gateways, load balancers, managed databases, and managed Kubernetes. Public IPv4
and compute may still cost money. Set an account budget before the exercise,
apply only during a study session, and destroy immediately afterward.

## Definition of done

Finish the course when all automated checks pass and the capstone portfolio
contains an architecture diagram, CI/CD diagram, two runbooks, an architecture
decision record, a security checklist, deployment notes, teardown evidence, and
one blameless incident report. Use the rubric in `course/07_capstone/README.md`
to choose what to repeat.

## Hints policy

Use help in this order: command `--help`, the last error line, the module hints,
official documentation, then a colleague or AI. Ask for a hint or review of
your diagnosis before requesting a complete solution.

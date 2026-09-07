# 02 — Containers

## Outcome

You can explain and build an image, run it with least privilege, connect
services through Compose, persist only intentional data, and diagnose startup
or health-check failures.

## Lessons

1. Read `app/Dockerfile` from top to bottom. For every line, state whether it
   changes the image at build time or process behavior at runtime.
2. Run `docker build --tag devops-practice-lab:local app`, inspect its history,
   and confirm its configured user is not root.
3. Complete `exercise.Dockerfile`, build it from this directory, and run
   `python3 check.py`.
4. Start only Redis and the API with Compose. Explain how the internal backend
   network keeps Redis off the host network.
5. Change one ignored file and show that Docker cache reuses the correct layers.

```bash
docker build -f course/02_containers/exercise.Dockerfile -t lab-exercise app
docker inspect --format '{{.Config.User}}' lab-exercise
```

## Operational artifact

Create `artifacts/02-container-review.md` documenting image tag, image digest,
runtime user, exposed port, health check, writable paths, and three hardening
choices.

## Reflection

- What is the difference between an image, container, volume, and network?
- Why do `USER`, read-only filesystems, and pinned base versions matter?
- Why is `depends_on` not a substitute for application retry behavior?

## Definition of done

The exercise image builds, its user is `app`, the filesystem is read-only under
Compose, and `make smoke` succeeds.

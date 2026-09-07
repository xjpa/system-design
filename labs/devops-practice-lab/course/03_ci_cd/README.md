# 03 — Continuous integration and delivery

## Outcome

You can design a pipeline that provides fast evidence, publishes immutable
artifacts once, promotes the same artifact, protects deployment, and makes
rollback routine.

## Pipeline model

```text
commit -> unit checks -> static/IaC checks -> image build -> security scan
       -> smoke test -> publish immutable image -> approved deployment -> verify
```

## Lessons

1. Read `.github/workflows/devops-lab-ci.yml` and label every step as feedback,
   artifact creation, security gate, or cleanup.
2. Complete `pipeline-order.txt`. Run `python3 check.py`.
3. Create a branch that intentionally breaks one unit test. Predict which jobs
   run, confirm locally, then repair it before committing.
4. Explain why the release workflow uses a commit-derived image tag and why the
   deployment workflow accepts an image reference instead of rebuilding.
5. Practice the rollback procedure in `docs/runbooks/rollback.md` locally.
6. Build `vulnerable.exercise.Dockerfile` only as a scanner exercise, scan it,
   record the finding, and remove the image afterward. Never deploy it.

## Operational artifact

Copy `docs/templates/cicd-diagram.md` to `artifacts/03-cicd-diagram.md` and fill
in triggers, gates, artifacts, credentials, approval, verification, and rollback.

## Reflection

- Which pipeline step should fail fastest?
- What is the difference between continuous delivery and deployment here?
- Why must cleanup run even after a failed smoke test?

## Definition of done

The local commands corresponding to each CI stage pass; you can identify the
exact immutable artifact to roll back to; secrets are not available to pull
request code from untrusted forks.

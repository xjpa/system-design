# 06 — Kubernetes fundamentals

## Outcome

You can explain the desired-state loop, deploy the lab to a local kind cluster,
inspect scheduling and probes, change configuration, diagnose a failed rollout,
and roll back.

## Lessons

1. Create a cluster: `kind create cluster --name devops-lab`.
2. Run `make k8s-load` and `make k8s-up`. Observe Pods, ReplicaSets,
   Deployments, Services, events, and container logs in namespace `devops-lab`.
3. Port-forward the API and run the smoke script with the forwarded port.
4. Complete `deployment.exercise.yml`; run `python3 check.py` and compare it to
   the reference deployment only afterward.
5. Set an invalid image, watch rollout status and events, then use rollout undo.
6. Break readiness without liveness. Explain why the Pod remains running but is
   removed from Service endpoints.

```bash
kubectl -n devops-lab port-forward service/api 8080:8080
kubectl -n devops-lab rollout status deployment/api
kubectl -n devops-lab rollout history deployment/api
kubectl -n devops-lab rollout undo deployment/api
```

Delete the namespace and cluster after practice.

## Operational artifact

Create `artifacts/06-rollout.md` with the desired/observed state, relevant event,
failed revision, rollback command, and verification output.

## Reflection

- How do Deployment, ReplicaSet, Pod, and Service responsibilities differ?
- Why must readiness and liveness answer different questions?
- Which parts would require a different design on a production cluster?

## Definition of done

The manifest check passes, two replicas become ready, a bad rollout fails
without replacing all healthy capacity, rollback succeeds, and the cluster is
deleted afterward.

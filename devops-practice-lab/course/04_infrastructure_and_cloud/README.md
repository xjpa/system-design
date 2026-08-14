# 04 — Infrastructure, configuration, and cloud

## Outcome

You can distinguish provisioning from host configuration, preview changes,
apply a small secure environment, and prove that it was removed.

The AWS portion is optional. Read `infra/COSTS.md` before authenticating.

## Lessons

1. Complete `network.exercise.tf`; use `terraform fmt` and `terraform validate`
   in an isolated temporary directory. No provider credentials are needed for
   syntax practice.
2. Read the real Terraform configuration. Draw its dependency graph before
   running `terraform graph`.
3. Generate a disposable SSH key, discover your public `/32`, copy
   `terraform.tfvars.example` to the ignored `terraform.tfvars`, then run plan.
4. Inspect every planned resource. Apply only after the cost guard and budget.
5. Generate `infra/ansible/inventory.ini` from the Terraform output and run the
   playbook twice. The second run should report no unnecessary changes.
6. Deploy, smoke test, destroy, and run the destroy check in one study session.

## Boundaries

- Terraform owns cloud resources and their relationships.
- Ansible owns packages, services, users, directories, and host configuration.
- The deployment pipeline owns which immutable application version runs.
- Secrets belong in credential stores or protected CI environments, never Git.

## Operational artifact

Save a redacted plan summary and destroy-check output in
`artifacts/04-cloud-lifecycle.md`. Never paste account IDs, public addresses,
key material, or credentials.

## Reflection

- Why does Terraform state require protection?
- What makes an Ansible play idempotent?
- Which ingress rules are necessary, and why is unrestricted SSH rejected?

## Definition of done

Local validation passes. If you choose the cloud track, the host is reachable
only from the configured CIDR, the playbook is idempotent, the API passes a
smoke test, and state plus console inspection show successful teardown.

# GitHub-to-AWS deployment identity

The manual deployment workflow uses GitHub's short-lived OIDC identity. It does
not accept long-lived AWS access keys.

Before using that optional workflow, an AWS administrator must create or reuse
the account's GitHub OIDC provider and a role whose trust policy restricts
`sub` to this repository and the protected `devops-lab` environment. Store only
the role ARN as the environment secret `AWS_DEPLOY_ROLE_ARN`.

The role needs only these actions against the tagged lab instance:

- describe the instance so the workflow can resolve its ID;
- send and inspect Systems Manager commands;
- no permission to create, modify, or delete infrastructure.

Require an environment reviewer. Inspect the requested immutable image input
before approval. Account-level identity bootstrapping is intentionally separate
from the disposable lab Terraform state: destroying a study environment must
not delete a shared identity provider or silently weaken its trust policy.

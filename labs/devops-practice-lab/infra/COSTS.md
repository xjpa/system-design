# Cloud cost boundary

This optional exercise can create billable resources. Pricing and free-tier
eligibility vary by account, region, and date. Check the AWS pricing pages for
your chosen region before every session.

The configuration creates one small EC2 instance, one public IPv4 address while
the instance runs, basic networking, and optionally an account budget. It does
not create a NAT gateway, load balancer, managed database, or managed cluster.

Before apply:

1. Configure an AWS account budget and verified alert email.
2. Use a non-production sandbox account when possible.
3. Review `terraform plan`; expect only resources from this directory.
4. Set `LAB_ACCEPT_CLOUD_COST=YES_DESTROY_AFTER_STUDY` for this terminal.
5. Limit the session to 60–90 minutes.

After the exercise:

```bash
make aws-destroy
make aws-destroy-check
```

Also confirm in the AWS console that no instance or unexpected resource remains.
Terraform can only report resources represented in its current state.

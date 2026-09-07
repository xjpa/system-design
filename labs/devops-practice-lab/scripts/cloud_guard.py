#!/usr/bin/env python3
import os


if os.getenv("LAB_ACCEPT_CLOUD_COST", "") != "YES_DESTROY_AFTER_STUDY":
    raise SystemExit(
        "Cloud apply blocked. Read infra/COSTS.md, set an account budget, then export "
        "LAB_ACCEPT_CLOUD_COST=YES_DESTROY_AFTER_STUDY for this terminal."
    )
print("Cost acknowledgement present. Remember: make aws-destroy && make aws-destroy-check")

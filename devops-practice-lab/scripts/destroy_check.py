#!/usr/bin/env python3
import json
import subprocess


result = subprocess.run(
    ["terraform", "-chdir=infra/terraform", "show", "-json"],
    capture_output=True,
    text=True,
)
if result.returncode:
    raise SystemExit("Cannot read Terraform state. Run terraform init or inspect the state manually.")
state = json.loads(result.stdout or "{}")
resources = state.get("values", {}).get("root_module", {}).get("resources", [])
managed = [item["address"] for item in resources if item.get("mode") == "managed"]
if managed:
    raise SystemExit("Managed resources remain:\n  " + "\n  ".join(managed))
print("Terraform state contains no managed resources. Save this output as teardown evidence.")

#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md", "Makefile", "compose.yml", "app/Dockerfile",
    "platform/prometheus/prometheus.yml", "platform/kubernetes/kustomization.yaml",
    "infra/terraform/main.tf", "infra/ansible/playbook.yml",
]
missing = [item for item in required if not (ROOT / item).exists()]
modules = sorted((ROOT / "course").glob("[0-9][0-9]_*"))
if len(modules) != 8:
    raise SystemExit(f"Expected 8 course modules, found {len(modules)}")
missing_readmes = [str(path.relative_to(ROOT)) for path in modules if not (path / "README.md").exists()]
if missing or missing_readmes:
    raise SystemExit("Missing required paths: " + ", ".join(missing + missing_readmes))
print(f"Repository structure passed: {len(modules)} modules and {len(required)} core paths.")

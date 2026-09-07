from pathlib import Path

text = (Path(__file__).parent / "deployment.exercise.yml").read_text()
required = [
    "replicas: 2", "revisionHistoryLimit: 3", "livenessProbe:", "readinessProbe:",
    "requests:", "limits:", "runAsNonRoot: true", "allowPrivilegeEscalation: false",
]
missing = [item for item in required if item not in text]
if "TODO" in text:
    missing.append("all TODOs")
if missing:
    raise SystemExit("Deployment still needs: " + ", ".join(missing))
print("Static manifest check passed. Apply it and inspect rollout behavior.")

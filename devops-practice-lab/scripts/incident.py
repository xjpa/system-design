#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path


scenario = sys.argv[1] if len(sys.argv) > 1 else "dependency"
commands = {
    "dependency": ["docker", "compose", "stop", "redis"],
    "worker": ["docker", "compose", "pause", "worker"],
    "api": ["docker", "compose", "stop", "api"],
}
overrides = {
    "latency": "RESPONSE_DELAY_MS: '2000'",
    "errors": "ERROR_RATE: '0.5'",
    "configuration": "REDIS_HOST: queue-name-does-not-exist",
}
evidence = {
    "cpu": "course/05_observability_and_incidents/fixtures/cpu_pressure.txt",
    "disk": "course/05_observability_and_incidents/fixtures/disk_pressure.txt",
}
override_path = Path("compose.incident.yml")

if scenario == "recover":
    subprocess.run(["docker", "compose", "unpause", "worker"], check=False)
    if override_path.exists():
        override_path.unlink()
    subprocess.run(["docker", "compose", "up", "-d", "redis", "api", "worker"], check=True)
    print("Recovery actions applied. Run `make smoke` and verify metrics before closing the incident.")
elif scenario in commands:
    subprocess.run(commands[scenario], check=True)
    print(f"Scenario '{scenario}' injected. Begin with symptoms; do not read this script during diagnosis.")
elif scenario in overrides:
    override_path.write_text(
        "services:\n  api:\n    environment:\n      " + overrides[scenario] + "\n"
    )
    subprocess.run(
        [
            "docker", "compose", "-f", "compose.yml", "-f", str(override_path),
            "up", "-d", "--no-deps", "--force-recreate", "api",
        ],
        check=True,
    )
    print(f"Scenario '{scenario}' injected. Observe client behavior, logs, and metrics before changing state.")
elif scenario in evidence:
    print(Path(evidence[scenario]).read_text())
    print("This is a safe evidence-only scenario. Write a hypothesis, next check, mitigation, and escalation condition.")
else:
    choices = sorted(set(commands) | set(overrides) | set(evidence))
    raise SystemExit("Unknown scenario. Choose: " + ", ".join(choices))

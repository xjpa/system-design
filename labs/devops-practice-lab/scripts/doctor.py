#!/usr/bin/env python3
import shutil
import subprocess


REQUIRED = ("python3", "git", "make", "curl", "docker")
OPTIONAL = ("terraform", "ansible-playbook", "aws", "kubectl", "kind")


def version(command: str) -> str:
    try:
        arguments = [command, "--version"]
        if command == "kubectl":
            arguments = [command, "version", "--client"]
        result = subprocess.run(
            arguments, capture_output=True, text=True, timeout=5
        )
        return (result.stdout or result.stderr).splitlines()[0]
    except (OSError, subprocess.TimeoutExpired, IndexError):
        return "installed"


missing = []
print("Required tools")
for tool in REQUIRED:
    path = shutil.which(tool)
    print(f"  {'OK' if path else 'MISSING':7} {tool:18} {version(tool) if path else ''}")
    if not path:
        missing.append(tool)

print("\nLater-module tools")
for tool in OPTIONAL:
    path = shutil.which(tool)
    print(f"  {'OK' if path else 'optional':7} {tool:18} {version(tool) if path else ''}")

if shutil.which("docker"):
    compose = subprocess.run(
        ["docker", "compose", "version"], capture_output=True, text=True
    )
    if compose.returncode:
        missing.append("docker compose")
    daemon = subprocess.run(
        ["docker", "info"], capture_output=True, text=True, timeout=10
    )
    if daemon.returncode:
        missing.append("running Docker daemon")

if missing:
    raise SystemExit("\nInstall or start required tools: " + ", ".join(missing))
print("\nWorkstation is ready for the local core.")

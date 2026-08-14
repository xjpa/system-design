from pathlib import Path

text = (Path(__file__).parent / "exercise.Dockerfile").read_text().upper()
requirements = {
    "an unprivileged user": "USER APP",
    "the service port": "EXPOSE 8080",
    "a liveness check": "HEALTHCHECK",
}
missing = [description for description, marker in requirements.items() if marker not in text]
if "TODO:" in text:
    missing.append("all TODO markers removed after implementing them")
if missing:
    raise SystemExit("Container exercise still needs: " + ", ".join(missing))
print("Static Dockerfile check passed. Build and inspect the image to finish verification.")

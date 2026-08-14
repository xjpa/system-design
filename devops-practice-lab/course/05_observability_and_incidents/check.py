from pathlib import Path

text = (Path(__file__).parent / "alert.exercise.yml").read_text()
requirements = ["rate(", "lab_http_errors_total", "lab_http_requests_total", "for: 2m", "runbook:"]
missing = [item for item in requirements if item not in text]
if "TODO" in text:
    missing.append("remove every TODO")
if missing:
    raise SystemExit("Alert exercise missing: " + ", ".join(missing))
print("Static alert check passed. Load the rule into Prometheus and test real behavior.")

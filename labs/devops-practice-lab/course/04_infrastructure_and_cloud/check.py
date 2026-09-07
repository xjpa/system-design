from pathlib import Path

text = (Path(__file__).parent / "network.exercise.tf").read_text()
missing = []
if "TODO" in text:
    missing.append("remove TODO placeholders")
if "validation" not in text:
    missing.append("add input validation")
if "cidrsubnet(" not in text:
    missing.append("derive the subnet with cidrsubnet")
if missing:
    raise SystemExit("Infrastructure exercise: " + ", ".join(missing))
print("Static exercise check passed. Run terraform fmt and validate in an isolated directory.")

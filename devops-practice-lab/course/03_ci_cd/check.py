from pathlib import Path

lines = [
    line.strip() for line in (Path(__file__).parent / "pipeline-order.txt").read_text().splitlines()
    if line.strip() and not line.startswith("#")
]
expected = ["unit-test", "build", "security-scan", "smoke-test", "publish", "deploy"]
if lines != expected:
    raise SystemExit("Pipeline order is not safe yet. Expected feedback before publish and publish before deploy.")
print("Pipeline ordering check passed. Explain why each boundary is placed there.")

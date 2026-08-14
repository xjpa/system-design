from pathlib import Path

text = (Path(__file__).parent / "20_triage.sh").read_text()
failures = []
if "return 1\n}" in text:
    failures.append("require_command still always fails")
if 'echo "TODO"' in text:
    failures.append("disk_summary still prints its placeholder")
if "command -v" not in text:
    failures.append("use the shell's command lookup rather than searching directories yourself")
if "df" not in text:
    failures.append("disk_summary should observe filesystem capacity with df")
if failures:
    raise SystemExit("Not ready:\n- " + "\n- ".join(failures))
print("Module 00 exercise check passed. Run the script and inspect its actual output.")

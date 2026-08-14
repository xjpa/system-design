from pathlib import Path
import subprocess
import sys

lesson = Path(__file__).parent / "10_http_probe.py"
if 'return "TODO"' in lesson.read_text():
    raise SystemExit("classify still returns the TODO placeholder")
result = subprocess.run([sys.executable, str(lesson)])
raise SystemExit(result.returncode)

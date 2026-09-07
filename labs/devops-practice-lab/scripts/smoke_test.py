#!/usr/bin/env python3
import json
import os
import time
import urllib.error
import urllib.request


base = f"http://127.0.0.1:{os.getenv('APP_PORT', '8080')}"


def request(path: str, data: dict | None = None) -> tuple[int, str]:
    body = json.dumps(data).encode() if data else None
    headers = {"Content-Type": "application/json"} if data else {}
    candidate = urllib.request.Request(base + path, data=body, headers=headers)
    try:
        with urllib.request.urlopen(candidate, timeout=3) as response:
            return response.status, response.read().decode()
    except urllib.error.HTTPError as error:
        return error.code, error.read().decode()


for attempt in range(30):
    try:
        status, _ = request("/health/ready")
        if status == 200:
            break
    except OSError:
        pass
    time.sleep(1)
else:
    raise SystemExit("API did not become ready; inspect: docker compose logs api redis")

checks = [
    ("liveness", request("/health/live")[0] == 200),
    ("readiness", request("/health/ready")[0] == 200),
    ("enqueue", request("/jobs", {"task": "smoke-test"})[0] == 202),
    ("metrics", "lab_http_requests_total" in request("/metrics")[1]),
]
for name, passed in checks:
    print(f"{'PASS' if passed else 'FAIL'} {name}")
if not all(passed for _, passed in checks):
    raise SystemExit(1)

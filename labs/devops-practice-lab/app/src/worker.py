import json
import os
import time

from .logging_utils import log
from .redis_protocol import command


def main() -> None:
    host = os.getenv("REDIS_HOST", "redis")
    port = int(os.getenv("REDIS_PORT", "6379"))
    log("worker_started")
    while True:
        try:
            response = command(host, port, "BLPOP", "jobs", "2", timeout=3)
            if response.startswith(b"*2"):
                payload = response.rsplit(b"\r\n", 2)[-2].decode()
                task = json.loads(payload).get("task", "unknown")
                time.sleep(0.1)
                log("job_completed", task=task)
        except (OSError, ValueError, json.JSONDecodeError) as error:
            log("worker_retry", level="WARNING", reason=type(error).__name__)
            time.sleep(2)


if __name__ == "__main__":
    main()

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import random
import time
from urllib.parse import urlparse

from .config import Config
from .logging_utils import log
from .redis_protocol import enqueue, ping


STARTED_AT = time.monotonic()
REQUESTS = {"total": 0, "errors": 0, "jobs": 0}


class Handler(BaseHTTPRequestHandler):
    config = Config.from_env()

    def log_message(self, format: str, *args: object) -> None:
        return

    def _respond(self, status: int, body: object, content_type: str = "application/json") -> None:
        payload = body.encode() if isinstance(body, str) else json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def _before_request(self) -> bool:
        REQUESTS["total"] += 1
        if self.config.response_delay_ms:
            time.sleep(self.config.response_delay_ms / 1000)
        if random.random() < self.config.error_rate:
            REQUESTS["errors"] += 1
            self._respond(500, {"error": "injected failure"})
            return False
        return True

    def do_GET(self) -> None:
        started = time.monotonic()
        if not self._before_request():
            return
        path = urlparse(self.path).path
        if path == "/health/live":
            status, body = 200, {"status": "alive"}
        elif path == "/health/ready":
            ready = not self.config.force_unready and ping(
                self.config.redis_host, self.config.redis_port
            )
            status, body = (200, {"status": "ready"}) if ready else (
                503,
                {"status": "not ready", "dependency": "queue"},
            )
        elif path == "/metrics":
            ready = int(ping(self.config.redis_host, self.config.redis_port))
            metrics = (
                "# HELP lab_http_requests_total HTTP requests received.\n"
                "# TYPE lab_http_requests_total counter\n"
                f"lab_http_requests_total {REQUESTS['total']}\n"
                f"lab_http_errors_total {REQUESTS['errors']}\n"
                f"lab_jobs_enqueued_total {REQUESTS['jobs']}\n"
                f"lab_dependency_ready {ready}\n"
                f"lab_process_uptime_seconds {time.monotonic() - STARTED_AT:.3f}\n"
            )
            self._respond(200, metrics, "text/plain; version=0.0.4")
            return
        else:
            status, body = 404, {"error": "not found"}
        self._respond(status, body)
        log("http_request", method="GET", path=path, status=status,
            duration_ms=round((time.monotonic() - started) * 1000, 2))

    def do_POST(self) -> None:
        if not self._before_request():
            return
        path = urlparse(self.path).path
        if path != "/jobs":
            self._respond(404, {"error": "not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length))
            if not isinstance(payload, dict) or not str(payload.get("task", "")).strip():
                raise ValueError("task is required")
            enqueue(self.config.redis_host, self.config.redis_port, json.dumps(payload))
        except (ValueError, json.JSONDecodeError):
            REQUESTS["errors"] += 1
            self._respond(400, {"error": "body must contain a non-blank task"})
            return
        except OSError:
            REQUESTS["errors"] += 1
            self._respond(503, {"error": "queue unavailable"})
            return
        REQUESTS["jobs"] += 1
        self._respond(202, {"status": "queued"})
        log("job_queued", task=payload["task"])


def main() -> None:
    config = Handler.config
    server = ThreadingHTTPServer(("0.0.0.0", config.port), Handler)
    log("api_started", port=config.port)
    server.serve_forever()


if __name__ == "__main__":
    main()

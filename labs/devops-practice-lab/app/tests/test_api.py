import io
import json
import os
import sys
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.api import Handler
from src.config import Config


class ApiTests(unittest.TestCase):
    def handler(self, path: str) -> Handler:
        handler = Handler.__new__(Handler)
        handler.path = path
        handler.config = Config(
            port=8080,
            redis_host="queue",
            redis_port=6379,
            response_delay_ms=0,
            error_rate=0,
            force_unready=False,
        )
        handler._respond = Mock()
        return handler

    @patch("src.api.log")
    @patch("src.api.ping", return_value=True)
    def test_readiness_checks_dependency(self, dependency: Mock, _log: Mock) -> None:
        handler = self.handler("/health/ready")
        handler.do_GET()
        dependency.assert_called_once_with("queue", 6379)
        handler._respond.assert_called_once_with(200, {"status": "ready"})

    @patch("src.api.log")
    def test_liveness_does_not_check_dependency(self, _log: Mock) -> None:
        handler = self.handler("/health/live")
        with patch("src.api.ping") as dependency:
            handler.do_GET()
        dependency.assert_not_called()
        handler._respond.assert_called_once_with(200, {"status": "alive"})

    @patch("src.api.log")
    @patch("src.api.enqueue")
    def test_enqueues_valid_job(self, enqueue: Mock, _log: Mock) -> None:
        handler = self.handler("/jobs")
        body = json.dumps({"task": "test"}).encode()
        handler.headers = {"Content-Length": str(len(body))}
        handler.rfile = io.BytesIO(body)
        handler.do_POST()
        enqueue.assert_called_once_with("queue", 6379, json.dumps({"task": "test"}))
        handler._respond.assert_called_once_with(202, {"status": "queued"})

    @patch("src.api.ping", return_value=True)
    def test_metrics_use_prometheus_text_format(self, _dependency: Mock) -> None:
        handler = self.handler("/metrics")
        handler.do_GET()
        status, body, content_type = handler._respond.call_args.args
        self.assertEqual(status, 200)
        self.assertIn("lab_dependency_ready 1", body)
        self.assertIn("lab_http_requests_total", body)
        self.assertIn("text/plain", content_type)


if __name__ == "__main__":
    unittest.main()

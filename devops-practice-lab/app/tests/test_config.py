import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.config import Config
from src.redis_protocol import encode_command


class ConfigTests(unittest.TestCase):
    def test_defaults_are_safe(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            config = Config.from_env()
        self.assertEqual(config.port, 8080)
        self.assertEqual(config.error_rate, 0)
        self.assertFalse(config.force_unready)

    def test_rejects_invalid_error_rate(self) -> None:
        with patch.dict(os.environ, {"ERROR_RATE": "2"}, clear=True):
            with self.assertRaises(ValueError):
                Config.from_env()

    def test_encodes_redis_command(self) -> None:
        self.assertEqual(encode_command("PING"), b"*1\r\n$4\r\nPING\r\n")


if __name__ == "__main__":
    unittest.main()

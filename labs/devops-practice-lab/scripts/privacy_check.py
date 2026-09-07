#!/usr/bin/env python3
"""Reject private target identifiers without storing those identifiers in the repo."""
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DENIED = {
    "42d9ba25f1405ba524bf9812652bda180fa26326db968ee46d5fa60cccdba8f7": 11,
    "5580a4465833c1437107164569202441f9e94c07db7ff4d0e9b1ed7d64461c95": 12,
    "f8730a052e3c3dd26cdc49495bb5d67c864dc7f7e7de02f381e81df0209df7d6": 10,
    "8e24bc50ebd40625583eeca1ea45ce3fe7d012dd0b11ee6b281e81e8df0b2588": 15,
    "2b828fea56a7d5ab292e4c6218d9750a10478799b1b6267b5610ce70dee14fb5": 14,
}
skip = {".git", ".terraform", "__pycache__", "artifacts"}
violations = []
for path in ROOT.rglob("*"):
    if not path.is_file() or any(part in skip for part in path.parts):
        continue
    try:
        text = path.read_text(errors="strict").lower()
    except (UnicodeDecodeError, OSError):
        continue
    for digest, length in DENIED.items():
        if any(
            hashlib.sha256(text[index:index + length].encode()).hexdigest() == digest
            for index in range(max(0, len(text) - length + 1))
        ):
            violations.append(str(path.relative_to(ROOT)))
            break
if violations:
    raise SystemExit("Private target identifier found in:\n  " + "\n  ".join(violations))
print("Privacy check passed.")

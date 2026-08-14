"""The tiny subset of Redis RESP needed by the lab; no package install needed."""

import socket


def encode_command(*parts: str) -> bytes:
    encoded = [f"*{len(parts)}\r\n".encode()]
    for part in parts:
        raw = part.encode()
        encoded.extend((f"${len(raw)}\r\n".encode(), raw, b"\r\n"))
    return b"".join(encoded)


def command(host: str, port: int, *parts: str, timeout: float = 1.0) -> bytes:
    with socket.create_connection((host, port), timeout=timeout) as connection:
        connection.sendall(encode_command(*parts))
        return connection.recv(65536)


def ping(host: str, port: int) -> bool:
    try:
        return command(host, port, "PING").startswith(b"+PONG")
    except OSError:
        return False


def enqueue(host: str, port: int, payload: str) -> None:
    response = command(host, port, "RPUSH", "jobs", payload)
    if not response.startswith(b":"):
        raise ConnectionError("Redis rejected the queue write")

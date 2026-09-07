from dataclasses import dataclass
import os


def _boolean(name: str, default: str = "false") -> bool:
    return os.getenv(name, default).strip().lower() in {"1", "true", "yes"}


@dataclass(frozen=True)
class Config:
    port: int
    redis_host: str
    redis_port: int
    response_delay_ms: int
    error_rate: float
    force_unready: bool

    @classmethod
    def from_env(cls) -> "Config":
        config = cls(
            port=int(os.getenv("APP_PORT", "8080")),
            redis_host=os.getenv("REDIS_HOST", "127.0.0.1"),
            redis_port=int(os.getenv("REDIS_PORT", "6379")),
            response_delay_ms=int(os.getenv("RESPONSE_DELAY_MS", "0")),
            error_rate=float(os.getenv("ERROR_RATE", "0")),
            force_unready=_boolean("FORCE_UNREADY"),
        )
        if config.port < 1 or config.port > 65535:
            raise ValueError("APP_PORT must be between 1 and 65535")
        if config.response_delay_ms < 0:
            raise ValueError("RESPONSE_DELAY_MS cannot be negative")
        if not 0 <= config.error_rate <= 1:
            raise ValueError("ERROR_RATE must be between 0 and 1")
        return config

import json
import sys
from datetime import datetime, timezone


def log(event: str, level: str = "INFO", **fields: object) -> None:
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": level,
        "event": event,
        **fields,
    }
    print(json.dumps(record, separators=(",", ":")), file=sys.stdout, flush=True)

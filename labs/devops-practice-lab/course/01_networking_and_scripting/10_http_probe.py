"""Complete the classifier, then use it against the running lab API."""
import urllib.error
import urllib.request


def classify(status: int) -> str:
    # TODO: return "healthy" for 2xx, "caller-error" for 4xx,
    # and "service-error" for 5xx. Return "unexpected" otherwise.
    return "TODO"


def probe(url: str) -> int:
    try:
        with urllib.request.urlopen(url, timeout=3) as response:
            print(f"{classify(response.status)}: HTTP {response.status} {url}")
            return 0 if 200 <= response.status < 300 else 1
    except urllib.error.HTTPError as error:
        print(f"{classify(error.code)}: HTTP {error.code} {url}")
        return 1
    except OSError as error:
        print(f"transport-error: {type(error).__name__}: {url}")
        return 2


assert classify(200) == "healthy"
assert classify(404) == "caller-error"
assert classify(503) == "service-error"

if __name__ == "__main__":
    raise SystemExit(probe("http://127.0.0.1:8080/health/ready"))

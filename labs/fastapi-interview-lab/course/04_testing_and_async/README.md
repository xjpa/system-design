# 04 — Testing and async

Prerequisites: topics 00–03. This topic teaches how to verify an HTTP contract,
replace infrastructure in tests, and reason accurately about asynchronous I/O.

## Python you need for testing

### Protocols: describing required behavior

A Protocol describes methods an object must provide:

~~~python
from typing import Protocol

class ProfileReader(Protocol):
    def get_name(self, profile_id: int) -> str | None: ...
~~~

The ellipsis means the protocol declares a method without implementing it. Any
object with a compatible get_name method can be used. It does not need to
inherit from ProfileReader.

This is structural typing: compatibility depends on behavior and shape. It lets
production code use a database reader while tests use a small fake.

### Recording calls in a fake

~~~python
class FakeProfileReader:
    def __init__(self, names: dict[int, str]) -> None:
        self.names = names
        self.requested_ids: list[int] = []

    def get_name(self, profile_id: int) -> str | None:
        self.requested_ids.append(profile_id)
        return self.names.get(profile_id)
~~~

The fake returns controlled data and records interactions. A test can assert
both the HTTP result and an important dependency call.

Test-double vocabulary:

- A fake has a lightweight working implementation.
- A stub returns predetermined answers.
- A spy records how it was called.
- A mock is commonly configured with expected interactions.

These categories overlap in casual conversation; describe what the double does
instead of arguing over its label.

### Generators, yield, and cleanup

A function containing yield is a generator:

~~~python
from collections.abc import Iterator

def temporarily_enable() -> Iterator[str]:
    print("setup")
    try:
        yield "ready"
    finally:
        print("cleanup")
~~~

next(generator) runs through yield and returns the yielded value. Calling next
again resumes after yield. finally runs even when an assertion fails. The
exercise uses this shape to ensure dependency overrides are removed.

FastAPI tests often use pytest fixtures for the same setup/yield/cleanup
pattern. The standalone lesson avoids requiring pytest.

## Testing the contract

TestClient drives the full FastAPI request path:

~~~python
response = client.get("/profiles/7")

assert response.status_code == 200
assert response.json() == {"id": 7, "name": "Ada"}
~~~

Useful assertions cover:

- method and path;
- status code;
- response JSON and important headers;
- validation failures;
- authentication/error behavior;
- important persistence or outbound side effects.

Do not test decorator internals. Test behavior a client can observe and a few
meaningful collaborations with dependencies.

## Dependency overrides

FastAPI maps the original dependency function to a replacement:

~~~python
fake = FakeProfileReader({7: "Ada"})
app.dependency_overrides[profile_reader] = lambda: fake

try:
    client = TestClient(app)
    response = client.get("/profiles/7")
finally:
    app.dependency_overrides.clear()
~~~

The key must be the exact dependency function used in Depends. Always clear
overrides or one test can contaminate another.

An invalid typed path should fail before the endpoint and reader run. A recorded
call list is a useful way to prove that ordering.

## Python you need for async

### Coroutines and await

Calling a normal function runs it immediately. Calling an async function creates
a coroutine; await runs it until it completes while allowing the event loop to
run other work during waits:

~~~python
import asyncio

async def fetch_name(profile_id: int) -> str:
    await asyncio.sleep(0.01)
    return f"profile-{profile_id}"

async def read_name(profile_id: int) -> dict[str, str]:
    name = await fetch_name(profile_id)
    return {"name": name}
~~~

Forgetting await often leaves a coroutine object where the result was expected.

### Parsing and concurrent independent work

~~~python
raw = "1,2,3"
ids = [int(part) for part in raw.split(",")]
names = await asyncio.gather(*(fetch_name(item_id) for item_id in ids))
~~~

split produces string pieces. int converts each piece. The star unpacks the
generated awaitables as separate arguments to gather. gather preserves result
order even if operations finish in a different order.

Only gather independent operations. If the second action depends on the first
result, await them sequentially.

## What async does and does not do

Async is useful when work spends time waiting for async-compatible network,
database, or file operations. While one request waits, the event loop can
advance another.

Async does not:

- make CPU-heavy work faster;
- make blocking libraries non-blocking;
- eliminate races around shared state;
- replace timeouts, connection pools, or error handling.

time.sleep blocks the event-loop thread. In async code, use asyncio.sleep for a
delay and async clients for real I/O. CPU-heavy work usually belongs in a
process, worker queue, or carefully managed executor.

FastAPI also supports normal def endpoints and runs them in a thread pool. A
normal def can be clearer when the whole call chain uses blocking libraries.
Do not choose async merely because it looks more advanced.

## Exercises

### 04.10 — Endpoint tests and overrides

Implement the endpoint against its reader protocol. Observe how the fake
controls returned data, records calls, and is cleaned up.

~~~bash
python course/04_testing_and_async/10_testing_endpoints.py
~~~

### 04.20 — Async endpoints

Await one operation, parse comma-separated IDs, and gather independent
operations concurrently.

~~~bash
python course/04_testing_and_async/20_async_endpoints.py
~~~

## Common mistakes

- Replacing the wrong function in dependency_overrides.
- Forgetting cleanup after a test.
- Testing only status 200 and ignoring error contracts.
- Calling an async function without await.
- Awaiting independent operations one by one when concurrency is desired.
- Calling time.sleep or a blocking HTTP client inside async code.
- Claiming async makes CPU calculations faster.

## Readiness check

1. Why can both a production reader and FakeReader satisfy a Protocol?
2. What should happen to an override after a test?
3. What does await allow the event loop to do?
4. When is asyncio.gather appropriate, and when is it not?

# 04 — Testing and async

Prerequisite: topics 00–03.

1. `10_testing_endpoints.py` — test contracts and replace dependencies.
2. `20_async_endpoints.py` — use awaitable I/O and explain blocking.

Interview checkpoint: test observable behavior rather than decorator internals.
Explain that `async def` enables concurrency only when slow operations yield
control with `await`; it does not make CPU work faster.

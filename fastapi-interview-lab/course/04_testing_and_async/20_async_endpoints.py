"""LESSON 04.20: Async endpoints and concurrent I/O.

Run: python course/04_testing_and_async/20_async_endpoints.py

`await` pauses this coroutine while an operation waits and lets the event loop
run other work. `asyncio.gather` starts independent awaitables concurrently.
Never use time.sleep or a blocking HTTP client inside async endpoint code.
"""

import asyncio

from fastapi import FastAPI
from fastapi.testclient import TestClient


app = FastAPI()


async def fetch_label(task_id: int) -> str:
    """A deterministic stand-in for async database or HTTP I/O."""
    await asyncio.sleep(0.01)
    return f"task-{task_id}"


@app.get("/labels/{task_id}")
async def get_label(task_id: int) -> dict[str, str]:
    # TODO: await fetch_label and return {"label": the_result}.
    raise NotImplementedError


@app.get("/labels")
async def get_labels(ids: str) -> dict[str, list[str]]:
    # TODO: Parse a comma-separated string such as "1,2,3" into integers.
    # Call fetch_label for every ID concurrently with asyncio.gather, then
    # return {"labels": labels}. Assume the input is well formed in this lesson.
    raise NotImplementedError


def run_tests() -> None:
    client = TestClient(app)

    assert client.get("/labels/4").json() == {"label": "task-4"}
    response = client.get("/labels", params={"ids": "1,2,3"})
    assert response.status_code == 200
    assert response.json() == {"labels": ["task-1", "task-2", "task-3"]}

    print("Lesson 04.20 passed: async I/O is awaited and composed concurrently.")


if __name__ == "__main__":
    run_tests()


# INTERVIEW QUESTIONS
# 1. Why would time.sleep(1) be harmful inside get_labels?
# 2. Would async make a CPU-heavy image transformation faster? Why not?
# 3. When is a normal `def` endpoint the clearer choice?

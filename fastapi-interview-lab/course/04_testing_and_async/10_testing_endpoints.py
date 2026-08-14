"""LESSON 04.10: Endpoint testing and dependency overrides.

Run: python course/04_testing_and_async/10_testing_endpoints.py

Good API tests assert the contract: status, body, headers, validation, and
important side effects. FastAPI dependency overrides replace external systems
without changing production endpoint code.
"""

from collections.abc import Iterator
from typing import Annotated, Protocol

from fastapi import Depends, FastAPI, HTTPException
from fastapi.testclient import TestClient


class TaskReader(Protocol):
    def get_title(self, task_id: int) -> str | None: ...


class ProductionReader:
    def get_title(self, task_id: int) -> str | None:
        # Imagine a real database query here.
        return None


def task_reader() -> TaskReader:
    return ProductionReader()


app = FastAPI()


@app.get("/tasks/{task_id}")
def get_task(
    task_id: int,
    reader: Annotated[TaskReader, Depends(task_reader)],
) -> dict[str, object]:
    # TODO: Ask reader for the title. Raise HTTPException(404, "Task not found")
    # when it returns None; otherwise return {"id": task_id, "title": title}.
    raise NotImplementedError


class FakeReader:
    def __init__(self, titles: dict[int, str]) -> None:
        self.titles = titles
        self.requested_ids: list[int] = []

    def get_title(self, task_id: int) -> str | None:
        self.requested_ids.append(task_id)
        return self.titles.get(task_id)


def client_using(fake: FakeReader) -> Iterator[TestClient]:
    """Worked example: install an override and always clean it up."""
    app.dependency_overrides[task_reader] = lambda: fake
    try:
        yield TestClient(app)
    finally:
        app.dependency_overrides.clear()


def run_tests() -> None:
    fake = FakeReader({7: "Test through the API"})
    client_iterator = client_using(fake)
    client = next(client_iterator)
    try:
        found = client.get("/tasks/7")
        assert found.status_code == 200
        assert found.json() == {"id": 7, "title": "Test through the API"}
        assert fake.requested_ids == [7]

        missing = client.get("/tasks/8")
        assert missing.status_code == 404
        assert missing.json() == {"detail": "Task not found"}
        assert fake.requested_ids == [7, 8]

        invalid = client.get("/tasks/not-an-integer")
        assert invalid.status_code == 422
        assert fake.requested_ids == [7, 8]  # validation ran before the endpoint
    finally:
        try:
            next(client_iterator)
        except StopIteration:
            pass

    assert app.dependency_overrides == {}
    print("Lesson 04.10 passed: tests control dependencies and assert contracts.")


if __name__ == "__main__":
    run_tests()

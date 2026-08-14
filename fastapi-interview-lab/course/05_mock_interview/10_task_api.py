"""MOCK INTERVIEW: Build a small task API.

Run: python course/05_mock_interview/10_task_api.py
Suggested time: 45 minutes after completing topics 00-04.

Contract:
- POST /tasks creates a task and returns 201 plus a Location header.
- GET /tasks lists tasks, optionally filtered by completed, with limit 1..100.
- GET /tasks/{id} returns a task or 404.
- PATCH /tasks/{id} changes only supplied fields.
- DELETE /tasks/{id} returns 204 or 404.
- Blank titles are invalid after whitespace is stripped.

Keep the in-memory storage. Do not add unrequested architecture during the
timer. You may add private helper functions.
"""

from typing import Annotated, Any

from fastapi import FastAPI, HTTPException, Query, Response, status
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field, field_validator


class TaskCreate(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=80)]

    @field_validator("title", mode="before")
    @classmethod
    def normalize_title(cls, value: Any) -> Any:
        # TODO: let non-strings continue to normal type validation; strip and
        # reject blank strings.
        raise NotImplementedError


class TaskPatch(BaseModel):
    title: Annotated[str | None, Field(min_length=1, max_length=80)] = None
    completed: bool | None = None

    @field_validator("title", mode="before")
    @classmethod
    def normalize_optional_title(cls, value: Any) -> Any:
        # TODO: preserve None, let other non-strings continue to normal type
        # validation, and otherwise strip and reject blank strings.
        raise NotImplementedError


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


app = FastAPI(title="Task Interview API")
tasks: dict[int, Task] = {}
next_id = 1


def require_task(task_id: int) -> Task:
    # TODO
    raise NotImplementedError


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, response: Response) -> Task:
    # TODO
    raise NotImplementedError


@app.get("/tasks", response_model=list[Task])
def list_tasks(
    completed: bool | None = None,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
) -> list[Task]:
    # TODO: filter, order by ID, and limit without mutating storage.
    raise NotImplementedError


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    # TODO
    raise NotImplementedError


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, patch: TaskPatch) -> Task:
    # TODO: reject explicit null fields with 422 and preserve omitted fields.
    raise NotImplementedError


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> None:
    # TODO
    raise NotImplementedError


def run_tests() -> None:
    global next_id
    tasks.clear()
    next_id = 1
    client = TestClient(app)

    first = client.post("/tasks", json={"title": "  Write API  "})
    second = client.post("/tasks", json={"title": "Test API"})
    assert first.status_code == 201
    assert first.headers["location"] == "/tasks/1"
    assert first.json() == {"id": 1, "title": "Write API", "completed": False}
    assert second.json()["id"] == 2

    assert client.post("/tasks", json={"title": "  "}).status_code == 422
    assert client.get("/tasks/999").status_code == 404
    assert client.get("/tasks/not-an-int").status_code == 422

    changed = client.patch("/tasks/2", json={"completed": True})
    assert changed.json() == {"id": 2, "title": "Test API", "completed": True}
    assert client.patch("/tasks/2", json={"title": None}).status_code == 422

    incomplete = client.get("/tasks", params={"completed": False, "limit": 1})
    assert incomplete.json() == [first.json()]
    assert client.get("/tasks", params={"limit": 0}).status_code == 422

    assert client.delete("/tasks/1").status_code == 204
    assert client.get("/tasks/1").status_code == 404
    assert client.delete("/tasks/1").status_code == 404

    print("Mock interview passed: the task API satisfies its HTTP contract.")


if __name__ == "__main__":
    run_tests()


# DISCUSS AFTER CODING
# 1. What changes if two workers create a task at the same time?
# 2. Where would a database transaction belong?
# 3. How would you add pagination without breaking existing clients?
# 4. Which tests would you keep in a production test suite?

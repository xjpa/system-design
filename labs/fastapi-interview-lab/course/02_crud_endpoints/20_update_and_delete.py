"""LESSON 02.20: PATCH and DELETE.

Run: python course/02_crud_endpoints/20_update_and_delete.py

PATCH changes only fields supplied by the client. In Pydantic v2,
model_dump(exclude_unset=True) distinguishes "omitted" from "sent explicitly".
DELETE returns 204 after a successful removal and 404 for a missing resource.
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field


class TaskPatch(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=80)
    completed: bool | None = None


class Task(BaseModel):
    id: int
    title: str
    completed: bool


app = FastAPI()
tasks: dict[int, Task] = {1: Task(id=1, title="Original", completed=False)}


def require_task(task_id: int) -> Task:
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, patch: TaskPatch) -> Task:
    task = require_task(task_id)
    # TODO: Get only explicitly supplied fields, reject an explicit null with
    # HTTP 422, create a changed copy with model_copy(update=...), store it,
    # and return it. An empty JSON object is a valid no-op.
    raise NotImplementedError


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> None:
    # TODO: Require the task, delete it from tasks, and return None.
    raise NotImplementedError


def run_tests() -> None:
    tasks.clear()
    tasks[1] = Task(id=1, title="Original", completed=False)
    client = TestClient(app)

    changed = client.patch("/tasks/1", json={"completed": True})
    assert changed.status_code == 200
    assert changed.json() == {"id": 1, "title": "Original", "completed": True}

    unchanged = client.patch("/tasks/1", json={})
    assert unchanged.status_code == 200
    assert unchanged.json() == changed.json()
    assert client.patch("/tasks/1", json={"title": None}).status_code == 422
    assert client.patch("/tasks/999", json={"completed": True}).status_code == 404

    deleted = client.delete("/tasks/1")
    assert deleted.status_code == 204
    assert deleted.content == b""
    assert client.delete("/tasks/1").status_code == 404

    print("Lesson 02.20 passed: partial updates preserve omitted fields.")


if __name__ == "__main__":
    run_tests()

"""LESSON 02.10: Create and read CRUD endpoints.

Run: python course/02_crud_endpoints/10_create_and_read.py

CRUD means Create, Read, Update, Delete. This lesson uses a dictionary as a
small repository. The endpoint functions should express HTTP behavior; helper
functions remove repeated lookup logic.
"""

from fastapi import FastAPI, HTTPException, Response, status
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=80)


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


app = FastAPI()
tasks: dict[int, Task] = {}
next_id = 1


def require_task(task_id: int) -> Task:
    # TODO: Return tasks[task_id], or raise HTTPException(404, "Task not found").
    raise NotImplementedError


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, response: Response) -> Task:
    global next_id
    # TODO: Build and store a Task, advance next_id, set the Location header,
    # and return the created task.
    raise NotImplementedError


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    # TODO: Return tasks ordered by ascending ID.
    raise NotImplementedError


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    # TODO: Delegate to require_task.
    raise NotImplementedError


def run_tests() -> None:
    global next_id
    tasks.clear()
    next_id = 1
    client = TestClient(app)

    first = client.post("/tasks", json={"title": "Implement POST"})
    second = client.post("/tasks", json={"title": "Implement GET"})
    assert first.status_code == 201
    assert first.headers["location"] == "/tasks/1"
    assert first.json() == {"id": 1, "title": "Implement POST", "completed": False}
    assert second.json()["id"] == 2
    assert client.get("/tasks").json() == [first.json(), second.json()]
    assert client.get("/tasks/2").json() == second.json()

    missing = client.get("/tasks/999")
    assert missing.status_code == 404
    assert missing.json() == {"detail": "Task not found"}

    print("Lesson 02.10 passed: create and read behavior forms a clear contract.")


if __name__ == "__main__":
    run_tests()

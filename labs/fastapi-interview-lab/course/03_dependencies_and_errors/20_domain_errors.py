"""LESSON 03.20: Translate domain errors at the API boundary.

Run: python course/03_dependencies_and_errors/20_domain_errors.py

Application/domain code should not need to know HTTP status codes. An exception
handler translates a meaningful Python error into the transport contract.
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel


class TaskAlreadyCompleted(Exception):
    def __init__(self, task_id: int) -> None:
        self.task_id = task_id
        super().__init__(f"Task {task_id} is already completed")


class Task(BaseModel):
    id: int
    completed: bool


app = FastAPI()
tasks = {1: Task(id=1, completed=False), 2: Task(id=2, completed=True)}


@app.exception_handler(TaskAlreadyCompleted)
def handle_already_completed(
    request: Request, error: TaskAlreadyCompleted
) -> JSONResponse:
    # TODO: Return status 409 and JSON:
    # {"error": "task_already_completed", "task_id": <the ID>}.
    raise NotImplementedError


@app.post("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: int) -> Task:
    # TODO: Return a 404 JSON error for an unknown task. Raise
    # TaskAlreadyCompleted when appropriate. Otherwise mark the task complete.
    raise NotImplementedError


def run_tests() -> None:
    tasks[1] = Task(id=1, completed=False)
    tasks[2] = Task(id=2, completed=True)
    client = TestClient(app)

    assert client.post("/tasks/1/complete").json() == {"id": 1, "completed": True}

    conflict = client.post("/tasks/2/complete")
    assert conflict.status_code == 409
    assert conflict.json() == {"error": "task_already_completed", "task_id": 2}

    missing = client.post("/tasks/999/complete")
    assert missing.status_code == 404
    assert missing.json() == {"detail": "Task not found"}

    print("Lesson 03.20 passed: domain failures have stable HTTP representations.")


if __name__ == "__main__":
    run_tests()

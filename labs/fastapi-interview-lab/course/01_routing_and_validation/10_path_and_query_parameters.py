"""LESSON 01.10: Path and query parameters.

Run: python course/01_routing_and_validation/10_path_and_query_parameters.py

Use a path parameter to identify a resource: /tasks/42.
Use query parameters to modify a collection view: /tasks?completed=true&limit=5.
Type hints are executable API rules: FastAPI parses and validates inputs.
"""

from typing import Annotated

from fastapi import FastAPI, Query
from fastapi.testclient import TestClient


app = FastAPI()
TASKS = [
    {"id": 1, "title": "Read prompt", "completed": True},
    {"id": 2, "title": "Code endpoint", "completed": False},
    {"id": 3, "title": "Test errors", "completed": False},
]


@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> dict[str, object]:
    # TODO: Return the task with the matching ID. A later lesson introduces
    # proper 404 handling; raise LookupError if no task matches for now.
    raise NotImplementedError


@app.get("/tasks")
def list_tasks(
    completed: bool | None = None,
    limit: Annotated[int, Query(ge=1, le=50)] = 20,
) -> list[dict[str, object]]:
    # TODO: If completed is not None, filter by it. Return at most limit tasks.
    # Do not mutate TASKS.
    raise NotImplementedError


def run_tests() -> None:
    client = TestClient(app, raise_server_exceptions=False)

    assert client.get("/tasks/2").json()["title"] == "Code endpoint"
    assert client.get("/tasks/not-an-int").status_code == 422

    response = client.get("/tasks", params={"completed": "false", "limit": 1})
    assert response.status_code == 200
    assert response.json() == [TASKS[1]]
    assert client.get("/tasks", params={"limit": 0}).status_code == 422
    assert client.get("/tasks", params={"limit": 51}).status_code == 422

    print("Lesson 01.10 passed: path and query inputs are typed and validated.")


if __name__ == "__main__":
    run_tests()

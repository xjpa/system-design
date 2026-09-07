"""LESSON 00.20: HTTP contracts and status codes.

Run: python course/00_http_and_fastapi/20_http_contracts.py

Useful interview defaults:
- GET reads and should not change state.
- POST creates or triggers an action.
- A successful GET is normally 200 OK.
- A successful creation is normally 201 Created.
- A successful deletion may be 204 No Content.
- Location tells a client where a newly created resource can be fetched.
"""

from fastapi import FastAPI, Response, status
from fastapi.testclient import TestClient


app = FastAPI()
next_id = 1


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(response: Response) -> dict[str, object]:
    global next_id
    # TODO: Create {"id": next_id, "title": "Practice HTTP"}, increment
    # next_id, set Location to /tasks/<id>, and return the task.
    raise NotImplementedError


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> None:
    # A 204 response deliberately has no response body.
    return None


def run_tests() -> None:
    global next_id
    next_id = 1
    client = TestClient(app)

    created = client.post("/tasks")
    assert created.status_code == 201
    assert created.json() == {"id": 1, "title": "Practice HTTP"}
    assert created.headers["location"] == "/tasks/1"

    deleted = client.delete("/tasks/1")
    assert deleted.status_code == 204
    assert deleted.content == b""

    print("Lesson 00.20 passed: the API communicates with HTTP semantics.")


if __name__ == "__main__":
    run_tests()

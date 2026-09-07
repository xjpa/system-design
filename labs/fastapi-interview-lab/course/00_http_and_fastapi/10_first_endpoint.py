"""LESSON 00.10: Your first FastAPI endpoint.

Run: python course/00_http_and_fastapi/10_first_endpoint.py

An API endpoint joins an HTTP method and a path to a Python function:

    @app.get("/hello")       # GET is the method; /hello is the path
    def hello():             # FastAPI calls this function for matching requests
        return {"message": "Hello"}  # dictionaries become JSON

Implement the two TODO endpoints, then run the file again.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient


app = FastAPI(title="Interview Tasks")


# WORKED EXAMPLE
@app.get("/hello")
def hello() -> dict[str, str]:
    return {"message": "Hello"}


# YOUR TURN 1
# TODO: Add GET /health returning {"status": "ok"}.


# YOUR TURN 2
# TODO: Add GET /tasks returning an empty JSON list.


def run_tests() -> None:
    client = TestClient(app)

    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}

    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []

    print("Lesson 00.10 passed: your FastAPI app serves JSON endpoints.")


if __name__ == "__main__":
    run_tests()

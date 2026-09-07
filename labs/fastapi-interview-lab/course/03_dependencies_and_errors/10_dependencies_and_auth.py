"""LESSON 03.10: Dependencies and bearer authentication.

Run: python course/03_dependencies_and_errors/10_dependencies_and_auth.py

Depends asks FastAPI to compute a value before calling the endpoint. It is
useful for authentication, database sessions, shared parameters, and services.
This token comparison is intentionally tiny; production auth must verify a
signed token or session and must use secure secret management.
"""

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.testclient import TestClient


app = FastAPI()
bearer = HTTPBearer(auto_error=False)
TOKENS = {"interview-token": "Ada"}


def current_user(
    credentials: Annotated[
        HTTPAuthorizationCredentials | None, Depends(bearer)
    ],
) -> str:
    # TODO: If credentials are absent or the token is unknown, raise a 401
    # HTTPException with detail "Invalid credentials" and a WWW-Authenticate
    # header containing "Bearer". Otherwise return the associated user name.
    raise NotImplementedError


@app.get("/me")
def read_me(user: Annotated[str, Depends(current_user)]) -> dict[str, str]:
    return {"name": user}


@app.post("/tasks")
def create_task(
    user: Annotated[str, Depends(current_user)],
) -> dict[str, str]:
    return {"title": "Protected task", "created_by": user}


def run_tests() -> None:
    client = TestClient(app)

    missing = client.get("/me")
    assert missing.status_code == 401
    assert missing.headers["www-authenticate"] == "Bearer"
    assert client.get(
        "/me", headers={"Authorization": "Bearer wrong"}
    ).status_code == 401

    headers = {"Authorization": "Bearer interview-token"}
    assert client.get("/me", headers=headers).json() == {"name": "Ada"}
    assert client.post("/tasks", headers=headers).json()["created_by"] == "Ada"

    print("Lesson 03.10 passed: one dependency protects multiple endpoints.")


if __name__ == "__main__":
    run_tests()

"""LESSON 01.20: Request bodies and Pydantic models.

Run: python course/01_routing_and_validation/20_request_models.py

A model documents, parses, and validates JSON. Constraints belong near the
field they constrain. Keep business rules that need repositories or services
out of request schemas.
"""

from typing import Annotated, Any, Literal

from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field, field_validator


class TaskCreate(BaseModel):
    # TODO: title must contain 1-80 characters after surrounding whitespace is
    # removed. priority must be "low", "medium", or "high" and defaults to
    # "medium".
    title: Annotated[str, Field(min_length=1, max_length=80)]
    priority: Literal["low", "medium", "high"] = "medium"

    @field_validator("title", mode="before")
    @classmethod
    def title_must_not_be_blank(cls, value: Any) -> Any:
        # TODO: If value is not a string, return it unchanged so normal type
        # validation can report the problem. Otherwise strip whitespace and
        # raise ValueError if the result is empty.
        raise NotImplementedError


class TaskResponse(BaseModel):
    id: int
    title: str
    priority: Literal["low", "medium", "high"]
    completed: bool


app = FastAPI()


@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(task: TaskCreate) -> dict[str, object]:
    # TODO: Return a dictionary with ID 1, the validated fields, and completed
    # false. FastAPI validates and serializes it through TaskResponse.
    raise NotImplementedError


def run_tests() -> None:
    client = TestClient(app)

    response = client.post("/tasks", json={"title": "  Practice models  "})
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "title": "Practice models",
        "priority": "medium",
        "completed": False,
    }

    assert client.post("/tasks", json={"title": "   "}).status_code == 422
    assert client.post(
        "/tasks", json={"title": "Test", "priority": "urgent"}
    ).status_code == 422
    assert client.post("/tasks", json={}).status_code == 422

    print("Lesson 01.20 passed: request and response shapes are explicit.")


if __name__ == "__main__":
    run_tests()

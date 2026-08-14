# 01 — Routing and validation

Prerequisite: topic 00. This topic teaches how request data becomes typed
Python values and how Pydantic validates JSON bodies.

## Python you need

### Parameters, defaults, None, and union types

~~~python
def describe(name: str, active: bool = True) -> dict[str, object]:
    return {"name": name, "active": active}
~~~

name is required. active is optional because it has a default.

None means no value. The type bool | None permits a Boolean or no value:

~~~python
completed: bool | None = None
~~~

Do not write if completed for an optional Boolean filter; it cannot distinguish
False from None. Write:

~~~python
if completed is not None:
    # apply the filter for True or False
~~~

### Loops, list comprehensions, and slices

~~~python
scores = [10, 3, 8, 2]
passing = [score for score in scores if score >= 8]
first_two = passing[:2]
~~~

A comprehension makes a new list. A slice returns at most the requested number
of items. Neither needs to mutate the original list.

To find a dictionary by ID:

~~~python
for profile in profiles:
    if profile["id"] == profile_id:
        return profile
raise LookupError("profile not found")
~~~

Dictionary fields use square brackets. Object fields use dot notation.

### Classes and Pydantic models

~~~python
from pydantic import BaseModel

class ProfileCreate(BaseModel):
    name: str
    age: int
~~~

The class inherits parsing and validation behavior from BaseModel. An instance
uses dot access: profile.name.

A validator can normalize input:

~~~python
from typing import Any
from pydantic import BaseModel, field_validator

class ProfileCreate(BaseModel):
    name: str

    @field_validator("name", mode="before")
    @classmethod
    def normalize_name(cls, value: Any) -> Any:
        if not isinstance(value, str):
            return value
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("name cannot be blank")
        return cleaned
~~~

Mode before makes constraints apply after trimming. Returning other types lets
Pydantic report the normal type error. ValueError becomes a validation response.

## Where request data belongs

| Location | Example | Use |
| --- | --- | --- |
| Path | /tasks/42 | Identity of one resource |
| Query | /tasks?completed=false | Filtering, sorting, pagination |
| Header | Authorization: Bearer token | Metadata and authentication |
| Body | {"title": "Practice"} | Structured create/update data |

A path placeholder and function parameter must have the same name:

~~~python
@app.get("/profiles/{profile_id}")
def get_profile(profile_id: int) -> dict[str, object]:
    return {"id": profile_id}
~~~

FastAPI parses the path text as int. Invalid typed input produces 422 before the
endpoint function runs.

Parameters not in the path become query parameters:

~~~python
@app.get("/profiles")
def list_profiles(active: bool | None = None) -> list[dict[str, object]]:
    ...
~~~

## Constraints and models

Annotated attaches FastAPI rules to a Python type:

~~~python
from typing import Annotated
from fastapi import Query

limit: Annotated[int, Query(ge=1, le=100)] = 20
~~~

ge means greater than or equal; le means less than or equal.

Separate input and output models because the client should not choose
server-owned fields such as IDs:

~~~python
from typing import Literal
from pydantic import BaseModel, Field

class ProfileCreate(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    role: Literal["student", "mentor"] = "student"

class ProfileResponse(BaseModel):
    id: int
    name: str
    role: Literal["student", "mentor"]
~~~

Literal allows only listed values. A response_model documents and validates the
public output shape. Pydantic should check local shape and field rules; services
should check rules needing application state, such as duplicate emails.

## Exercises

### 01.10 — Path and query parameters

Find one task by ID, optionally filter by a Boolean, then apply a limit. Test
completed is not None, make a new list, and slice it.

~~~bash
python course/01_routing_and_validation/10_path_and_query_parameters.py
~~~

### 01.20 — Request models

Normalize a title, constrain priority values, and build the response from a
validated request. Use task.title and task.priority, not dictionary indexing.

~~~bash
python course/01_routing_and_validation/20_request_models.py
~~~

## Common mistakes

- Using if completed, which skips a requested false filter.
- Mutating the source list during filtering.
- Mixing dictionary indexing and object attribute access.
- Returning the original title rather than the normalized validator result.
- Manually handling type errors FastAPI already turns into 422.

## Readiness check

1. Why is an ID usually in the path but limit in the query?
2. Why must an optional Boolean distinguish False from None?
3. When does FastAPI return 422 without entering the endpoint?
4. Why use different creation and response models?

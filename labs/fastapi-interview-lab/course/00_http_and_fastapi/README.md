# 00 — HTTP and FastAPI

Read this page before opening the exercises. It teaches the Python and web
vocabulary they assume.

## Python you need

### Functions, return values, dictionaries, and lists

~~~python
def greeting() -> dict[str, str]:
    return {"message": "Hello"}
~~~

- def starts a function definition.
- greeting is its name.
- The parentheses hold inputs; this function has none.
- The arrow is a type hint saying the return value is a dictionary with string
  keys and string values.
- return sends a value back to the caller.
- Indentation marks the function body.

FastAPI calls endpoint functions for you. A Python dictionary becomes a JSON
object, and a Python list becomes a JSON array:

| Python | JSON |
| --- | --- |
| dict | object |
| list | array |
| str | string |
| int or float | number |
| True or False | true or false |
| None | null |

Return a dictionary, not a string containing JSON syntax.

### Variables and global

Assignment stores a value under a name. Reading a module-level variable inside
a function works normally. Assigning a new value to it requires global:

~~~python
next_number = 1

def take_number() -> int:
    global next_number
    current = next_number
    next_number += 1
    return current
~~~

This is acceptable for a small exercise. It is not safe production ID
generation when requests or server processes run concurrently.

## HTTP: the minimum mental model

An HTTP request has a method, path, optional headers, optional query parameters,
and an optional body. A response has a status code, headers, and an optional
body, often JSON.

Describe an endpoint before coding:

~~~text
GET /profiles/7
input: profile ID 7 in the path
success: 200 with a JSON profile
failure: 404 if profile 7 does not exist
~~~

Common contracts:

| Intent | Method | Typical success |
| --- | --- | --- |
| Read resources | GET | 200 OK |
| Create a resource | POST | 201 Created |
| Replace a resource | PUT | 200 or 204 |
| Partially change a resource | PATCH | 200 OK |
| Delete a resource | DELETE | 204 No Content |

The status code is behavior. A 201 tells the client that a resource was
created. A 204 means success with no response body.

## FastAPI building blocks

Create one application object and decorate route functions:

~~~python
from fastapi import FastAPI

app = FastAPI()

@app.get("/profiles")
def list_profiles() -> list[dict[str, str]]:
    return [{"name": "Ada"}]
~~~

The decorator registers the method and path. Do not omit the @ sign or put
unrelated code between the decorator and function.

To control a successful status and response header:

~~~python
from fastapi import Response, status

@app.post("/profiles", status_code=status.HTTP_201_CREATED)
def create_profile(response: Response) -> dict[str, object]:
    profile = {"id": 8, "name": "Grace"}
    response.headers["Location"] = "/profiles/8"
    return profile
~~~

FastAPI supplies the Response argument. Location tells a client where the new
resource can be fetched.

## How the checks work

TestClient sends in-process requests; no live server or port is required:

~~~python
from fastapi.testclient import TestClient

client = TestClient(app)
response = client.get("/profiles")

assert response.status_code == 200
assert response.json() == [{"name": "Ada"}]
~~~

An assert stops with AssertionError when its condition is false. Treat the
first failure as feedback: implement one TODO and rerun.

## Exercises

### 00.10 — First endpoint

File: 10_first_endpoint.py

Register two GET routes and return a dictionary and a list. Before starting,
explain def, return, the route decorator, curly braces, and square brackets.

~~~bash
python course/00_http_and_fastapi/10_first_endpoint.py
~~~

### 00.20 — HTTP contracts

File: 20_http_contracts.py

Return 201, set Location, increment an ID, and preserve an empty body for 204.

~~~bash
python course/00_http_and_fastapi/20_http_contracts.py
~~~

## Common mistakes

- Returning a JSON-looking string instead of a Python dictionary.
- Writing app.get without the @ sign.
- Returning content with 204 No Content.
- Incrementing next_id before saving its current value.
- Starting Uvicorn even though TestClient already runs the app.

## Readiness check

1. What are the method, path, inputs, success response, and errors of an endpoint?
2. What Python value produces a JSON object?
3. How do 200, 201, and 204 differ?
4. What does a route decorator do?

If you can answer those aloud, start exercise 00.10.

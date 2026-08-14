# FastAPI Interview Practice Lab

Learn the Python API skills commonly exercised in coding interviews by building
small pieces of a task-tracking API. The format mirrors the OOP practice lab:
every lesson is one self-contained Python file with a short tutorial, a worked
example, focused TODOs, and executable checks.

The goal is not to memorize FastAPI decorators. It is to be able to turn an
HTTP contract into clear Python code, explain your choices, and verify the
behavior under interview time pressure.

## What you will learn

- HTTP methods, routes, status codes, headers, and JSON responses
- path parameters, query parameters, and request bodies
- Pydantic validation and response models
- CRUD behavior and the differences between `PUT` and `PATCH`
- dependency injection, simple bearer authentication, and error handling
- endpoint tests with `TestClient`
- when `async def` helps and when blocking work is still a problem
- a repeatable approach to live API coding interviews

## Setup

Use Python 3.10 or newer. From this directory, create an isolated environment
and install the small dependency set:

```bash
cd fastapi-interview-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Then run the first lesson:

```bash
python course/00_http_and_fastapi/10_first_endpoint.py
```

An unfinished lesson is expected to stop at its first failed assertion. Solve
one TODO, rerun the same command, and use the next failure as feedback.

## Learning path

| Order | Topic | Interview skill |
| ---: | --- | --- |
| 00 | `http_and_fastapi` | Read an HTTP contract and build an app |
| 01 | `routing_and_validation` | Convert requirements into typed inputs |
| 02 | `crud_endpoints` | Implement resource behavior and status codes |
| 03 | `dependencies_and_errors` | Separate cross-cutting policy from endpoints |
| 04 | `testing_and_async` | Prove behavior and discuss concurrency |
| 05 | `mock_interview` | Solve and explain a complete prompt |

See [the course index](course/README.md) for lesson order and commands.

## The scenario

You are implementing an API for interview-practice tasks. A task has an ID,
title, completion state, and priority. Clients can create, list, fetch, update,
and delete tasks. Later lessons add authentication and error handling.

Each file deliberately creates its own tiny app and in-memory state. Production
applications should split routers, schemas, services, and persistence into
modules, but doing so here would hide the interview concept being practiced.

## The interview loop

Use this loop for every exercise:

1. Restate the contract: method, path, inputs, success response, and errors.
2. Give one concrete request/response example before coding.
3. Implement the smallest happy path.
4. Add validation and negative cases one at a time.
5. Run the checks after every meaningful change.
6. Explain one tradeoff and one production improvement aloud.

When the code passes, redo the exercise with a 25-minute timer. In an interview,
narrate assumptions instead of silently guessing. A correct, modest endpoint
with explicit tradeoffs is stronger than an overbuilt architecture you cannot
finish.

## Optional live server

The checks do not require opening a port. To explore a completed lesson with
Swagger UI, run (example):

```bash
uvicorn course.00_http_and_fastapi.10_first_endpoint:app --reload
```

Then visit `http://127.0.0.1:8000/docs`. Numeric module names can be awkward in
some tools; if your shell or editor objects, copy the completed app to `app.py`
and run `uvicorn app:app --reload`.

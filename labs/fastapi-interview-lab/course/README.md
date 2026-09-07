# Course index

Complete the numbered directories in order. Before opening a Python exercise,
read that topic's README completely. It teaches the Python syntax, FastAPI
concepts, parallel examples, and common mistakes assumed by its exercises.

Every exercise is standalone and runs from fastapi-interview-lab. You never
need a completed earlier file as an import, but later exercises assume you
understand earlier concepts.

~~~text
00_http_and_fastapi
  10_first_endpoint.py
  -> 20_http_contracts.py
01_routing_and_validation
  10_path_and_query_parameters.py
  -> 20_request_models.py
02_crud_endpoints
  10_create_and_read.py
  -> 20_update_and_delete.py
03_dependencies_and_errors
  10_dependencies_and_auth.py
  -> 20_domain_errors.py
04_testing_and_async
  10_testing_endpoints.py
  -> 20_async_endpoints.py
05_mock_interview
  10_task_api.py
~~~

## Topic guides

| Topic | Read first | Python preparation | API preparation |
| --- | --- | --- | --- |
| 00 | [HTTP and FastAPI](00_http_and_fastapi/README.md) | Functions, returns, dictionaries, lists, globals | HTTP contracts, routes, JSON, statuses |
| 01 | [Routing and validation](01_routing_and_validation/README.md) | Parameters, None, loops, classes, validators | Path/query/body inputs, Pydantic, 422 |
| 02 | [CRUD endpoints](02_crud_endpoints/README.md) | Dictionary storage, copies, lambdas, any | CRUD, 404, PATCH, omitted versus null |
| 03 | [Dependencies and errors](03_dependencies_and_errors/README.md) | Objects, lookup, custom exceptions | Depends, bearer auth, error translation |
| 04 | [Testing and async](04_testing_and_async/README.md) | Protocols, fakes, generators, coroutines | Overrides, contract tests, async I/O |
| 05 | [Mock interview](05_mock_interview/README.md) | Combined review | Timed implementation and narration |

## Learning rhythm

For each exercise:

1. Read the entire topic README.
2. Read the exercise contract and tests before editing.
3. Predict the first failed check.
4. Implement only the next TODO.
5. Rerun the same file.
6. Once green, answer the topic readiness questions aloud.
7. Change one test input and predict the result.

The checks use FastAPI TestClient, so they exercise routing, serialization,
validation, dependencies, and errors without starting a server.

## If Python is still unfamiliar

Pause and try a tiny version in a scratch file. For example, filter a plain list
before filtering API results. The
[OOP Practice Lab](../../oop-practice-lab/README.md) teaches Python in more
detail; its topics 00–05 are the fallback for syntax gaps.

You are ready for topic 00 if you can run a Python file and recognize a
function. Each later Python feature is introduced in its topic guide.

## When a check fails

Read the last traceback lines first:

- AssertionError means the response differs from the expected contract.
- NotImplementedError means you reached an unfinished TODO.
- A 422 response usually means validation rejected input before the endpoint.
- A 500 response or propagated exception usually means endpoint code crashed.

Write: “I sent ___, expected ___, but received ___.” Then inspect only the next
TODO and the matching section of the topic README.

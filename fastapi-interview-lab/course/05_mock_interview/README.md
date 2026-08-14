# 05 — Mock interview

Prerequisites: topics 00–04. This page is your pre-interview playbook. The
exercise combines earlier concepts without introducing new framework features.

## What the interviewer is evaluating

The task is not only about making tests green. A strong candidate:

1. clarifies the HTTP contract;
2. turns requirements into small cases;
3. writes readable, typed Python;
4. handles invalid and missing input deliberately;
5. checks progress frequently;
6. explains tradeoffs without building unrequested infrastructure.

## Python and FastAPI recap

Keep this mapping in your head:

| Requirement | Tool |
| --- | --- |
| Typed JSON input | Pydantic BaseModel |
| Normalize one field | field_validator |
| ID in URL | typed path parameter |
| Optional filter | query parameter with None default |
| Limit range | Annotated plus Query |
| Missing resource | raise HTTPException with 404 |
| Create resource | POST, 201, Location |
| Partial update | model_dump with exclude_unset |
| Copy a model | model_copy with update |
| Delete successfully | 204 and no body |
| Exercise the full route | TestClient |

Important Python reminders:

- Dictionary lookup: tasks.get(task_id)
- Store by ID: tasks[task.id] = task
- Delete: del tasks[task_id]
- Sort objects: sorted(items, key=lambda item: item.id)
- Filter optional Boolean: completed is None or task.completed == completed
- Take a limit: items[:limit]
- Reject any null change: any(value is None for value in changes.values())
- Assign a module counter: declare global next_id inside the function

## Convert the prompt into a contract table

Before writing code, produce something like:

| Method and path | Input | Success | Failure |
| --- | --- | --- | --- |
| POST /tasks | JSON title | 201, task, Location | 422 |
| GET /tasks | completed, limit | 200, list | 422 |
| GET /tasks/{id} | integer ID | 200, task | 404 or 422 |
| PATCH /tasks/{id} | partial JSON | 200, task | 404 or 422 |
| DELETE /tasks/{id} | integer ID | 204, empty | 404 or 422 |

Say your assumptions aloud. For example: “I will treat PATCH with an empty
object as a no-op and reject explicit null because stored fields are required.”

## A safe implementation order

Do not attempt the whole API at once:

1. Read the supplied models and tests.
2. Implement title normalization.
3. Implement require_task once.
4. Implement POST and verify ID, storage, status, and Location.
5. Implement GET one and GET many.
6. Implement PATCH using explicitly supplied fields.
7. Implement DELETE.
8. Run all checks.
9. Refactor only duplication that is now obvious.

This order establishes storage and shared lookup before operations that depend
on them.

## Think in tiny examples

For filtering:

~~~text
stored: incomplete ID 1, complete ID 2
query: completed=false, limit=1
result: only ID 1
~~~

For PATCH:

~~~text
stored: title "Test", completed false
body: {"completed": true}
result: title remains "Test", completed becomes true
~~~

For errors:

~~~text
GET /tasks/999 -> 404 because integer ID is valid but absent
GET /tasks/nope -> 422 because path cannot become an integer
~~~

Writing examples first prevents several common condition and validation bugs.

## How to narrate while coding

Useful narration is short and concrete:

- “I am centralizing the 404 so every member route behaves consistently.”
- “I need is not None here because false is a meaningful filter.”
- “exclude_unset preserves fields the client omitted.”
- “The dictionary is a test-friendly stand-in; production storage needs atomic
  ID generation and durable transactions.”
- “I will get the contract passing before considering module separation.”

Avoid narrating every keystroke. Explain decisions, assumptions, and observed
test failures.

## Production follow-up answers

### What breaks with simultaneous creation?

The module-level next_id increment is not an atomic database operation. Multiple
workers also have separate memory. Production code would let a database
generate IDs or use collision-resistant IDs and enforce uniqueness.

### Where do transactions belong?

A repository or application-service boundary should coordinate the database
transaction. Route functions should not scatter commit logic across branches.

### How would storage change?

Introduce an interface with operations such as add, get, list, update, and
delete. Inject a database-backed implementation. Keep the HTTP contract and
Pydantic boundary separate from persistence models.

### How would pagination evolve?

Define deterministic ordering, accept cursor or offset parameters, cap page
size, and return navigation metadata. Preserve existing defaults when possible.

### What else would production need?

Authentication and authorization, migrations, uniqueness constraints,
structured logs, metrics, timeouts, request IDs, configuration, security
review, and integration tests. Mention these as follow-ups; do not build all of
them in a 45-minute exercise.

## Exercises

File: 10_task_api.py

First pass: work without a timer and consult earlier topic READMEs. Before
editing, keep a clean starter copy. On the second pass, redo it in 45 minutes
while explaining your decisions aloud.

~~~bash
python course/05_mock_interview/10_task_api.py
~~~

Suggested time allocation:

| Minutes | Work |
| ---: | --- |
| 0–5 | Restate contract and inspect tests |
| 5–15 | Validation, helper, create/read |
| 15–30 | List/filter, patch, delete |
| 30–38 | Negative cases and full test run |
| 38–45 | Refactor lightly and discuss production |

## Common mistakes

- Coding before clarifying omitted versus null PATCH behavior.
- Overwriting title when only completed was supplied.
- Using truthiness for optional Boolean filters.
- Duplicating 404 logic in every endpoint.
- Forgetting deterministic list ordering.
- Adding a database, Docker, or layered package before the requested API works.
- Going silent after a failure instead of stating what it revealed.

## Final readiness check

Explain without notes:

1. Why creation returns 201 and Location.
2. Why absent integer IDs return 404 but non-integer IDs return 422.
3. How PATCH preserves omitted values.
4. Why the in-memory store is acceptable for this exercise but not production.
5. What you would implement next if given another hour.

When those answers are comfortable, begin the timed pass.

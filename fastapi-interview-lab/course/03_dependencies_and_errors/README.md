# 03 — Dependencies and errors

Prerequisites: topics 00–02. This topic separates shared policy from route
functions and translates application failures into stable HTTP responses.

## Python you need

### Calling objects and reading attributes

An object groups data and behavior:

~~~python
credentials.scheme
credentials.credentials
~~~

The first attribute might contain Bearer and the second the token. Use dot
notation because credentials is an object, not a dictionary.

### Membership and dictionary lookup

~~~python
users_by_token = {"valid-token": "Ada"}
user = users_by_token.get(token)

if user is None:
    raise ValueError("unknown token")
~~~

Dictionary get returns None for a missing key. This avoids two separate lookups.

### Custom exceptions

An exception is a Python object representing a failure:

~~~python
class ProfileAlreadyActive(Exception):
    def __init__(self, profile_id: int) -> None:
        self.profile_id = profile_id
        super().__init__(f"Profile {profile_id} is already active")
~~~

raise creates the failure path. Attributes carry structured context to a
handler. Catch or translate only errors you know how to handle.

## What dependency injection means

A dependency is a value or operation an endpoint needs but should not build
inside itself. FastAPI resolves Depends before calling the endpoint:

~~~python
from typing import Annotated
from fastapi import Depends, FastAPI

def current_language() -> str:
    return "en"

@app.get("/welcome")
def welcome(language: Annotated[str, Depends(current_language)]) -> dict[str, str]:
    return {"language": language}
~~~

FastAPI calls current_language and passes its result as language. This is useful
for authentication, database sessions, shared query parsing, and application
services.

Benefits:

- one rule protects many endpoints;
- endpoint code focuses on its main action;
- tests can replace dependencies;
- cleanup and lifecycle policy can live in one place.

Do not call current_language() in the parameter default. Depends needs the
function itself, not the result of calling it.

## Bearer authentication

A request may send:

~~~text
Authorization: Bearer interview-token
~~~

HTTPBearer parses that header into credentials. With auto_error=False, missing
credentials become None so your dependency controls the error response.

Authentication asks who the caller is. Authorization asks whether that caller
may perform a particular action. The exercise implements only tiny
authentication; a production system should verify signed tokens or server-side
sessions, expiration, issuer, and permissions. Never treat a plain lookup table
as production security.

A 401 response should advertise the expected authentication scheme:

~~~python
raise HTTPException(
    status_code=401,
    detail="Invalid credentials",
    headers={"WWW-Authenticate": "Bearer"},
)
~~~

Use 401 when valid authentication is missing. Use 403 when identity is known
but that identity lacks permission.

## Errors at different layers

Keep transport vocabulary at the API edge:

~~~text
endpoint -> application/domain behavior -> raises meaningful Python error
endpoint exception handler -> converts it to status + JSON
~~~

Domain code should be usable without HTTP. It can raise
ProfileAlreadyActive; an API handler decides that the failure means 409
Conflict:

~~~python
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(ProfileAlreadyActive)
def handle_already_active(
    request: Request,
    error: ProfileAlreadyActive,
) -> JSONResponse:
    return JSONResponse(
        status_code=409,
        content={"error": "profile_already_active", "profile_id": error.profile_id},
    )
~~~

The request parameter is required by the handler interface even when this
handler does not inspect it.

### Choosing common error statuses

| Status | Meaning in these labs |
| --- | --- |
| 400 | Request is malformed beyond normal schema validation |
| 401 | Missing or invalid authentication |
| 403 | Authenticated but not permitted |
| 404 | Named resource does not exist |
| 409 | Request conflicts with current resource state |
| 422 | Typed or constrained input is invalid |
| 500 | Unexpected server bug; do not expose internal details |

Use consistent error JSON so clients do not parse human prose to identify an
error type.

## Exercises

### 03.10 — Dependencies and authentication

Validate optional bearer credentials, return the associated user, and protect
two endpoints with the same dependency.

~~~bash
python course/03_dependencies_and_errors/10_dependencies_and_auth.py
~~~

### 03.20 — Domain errors

Complete a state-changing action, use 404 for a missing task, raise a meaningful
exception for a conflict, and translate that exception to stable 409 JSON.

~~~bash
python course/03_dependencies_and_errors/20_domain_errors.py
~~~

## Common mistakes

- Calling a dependency while declaring Depends instead of passing the function.
- Accessing credential object fields with dictionary syntax.
- Returning HTTPException instead of raising it.
- Responding 200 with an error-shaped body.
- Using 401 and 403 interchangeably.
- Catching every Exception and hiding programming bugs as client errors.
- Putting HTTPException imports inside reusable domain logic.

## Readiness check

1. What happens before an endpoint with a Depends parameter runs?
2. How are authentication and authorization different?
3. Why does a 401 bearer response include WWW-Authenticate?
4. Why translate a custom application exception at the API boundary?

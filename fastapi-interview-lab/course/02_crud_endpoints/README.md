# 02 — CRUD endpoints

Prerequisites: topics 00–01. This topic combines routing and validation into a
small in-memory resource API.

## Python you need

### Dictionaries as keyed storage

The exercises store Pydantic objects by integer ID:

~~~python
profiles: dict[int, Profile] = {}
profiles[7] = Profile(id=7, name="Ada")

found = profiles.get(7)       # object or None
same = profiles[7]            # object or KeyError
del profiles[7]               # remove the entry
~~~

Use get when missing data is an expected branch. Dictionary iteration yields
keys; values() yields the stored objects:

~~~python
ordered = sorted(profiles.values(), key=lambda profile: profile.id)
~~~

The lambda is a small unnamed function used here to select the sort key.

### Mutability and copying models

Assignment does not copy an object:

~~~python
second_name = first_name
~~~

Both names refer to the same value. Pydantic provides model_copy for a changed
copy:

~~~python
changed = profile.model_copy(update={"name": "Grace"})
~~~

Storing changed back in the dictionary makes the update visible to later
requests without modifying unspecified fields.

### Keyword arguments and dictionary unpacking

Double-star unpacking turns dictionary entries into named arguments:

~~~python
changes = {"name": "Grace"}
changed = profile.model_copy(update=changes)
~~~

You will not need to manually branch once for every patch field.

## CRUD and resource routes

CRUD means create, read, update, delete:

| Operation | Route | Expected behavior |
| --- | --- | --- |
| Create | POST /tasks | Allocate ID, store, return 201 |
| Read collection | GET /tasks | Return zero or more tasks |
| Read member | GET /tasks/{id} | Return task or 404 |
| Partial update | PATCH /tasks/{id} | Change supplied fields or 404 |
| Delete | DELETE /tasks/{id} | Remove and return 204 or 404 |

Collection routes operate on the set. Member routes identify one item.

## Reusing lookup behavior

Repeated missing-resource behavior belongs in one helper:

~~~python
from fastapi import HTTPException

def require_profile(profile_id: int) -> Profile:
    profile = profiles.get(profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
~~~

Raising HTTPException stops the endpoint and creates an HTTP response. Returning
HTTPException would mistakenly serialize it as successful data.

404 means the named resource does not exist. It is different from 422, which
means the request could not pass input validation.

## Creating safely in the exercise

The practice sequence is:

1. Save the current next_id in a local variable.
2. Construct the Task from validated input.
3. Store it under that ID.
4. Advance next_id.
5. Set Location to the member route.
6. Return the created object.

The module-level counter and dictionary disappear on restart and are not safe
across multiple workers. They deliberately stand in for a database so the
exercise focuses on the API contract.

## PATCH: omitted is different from null

Consider these bodies:

~~~json
{}
~~~

~~~json
{"completed": false}
~~~

~~~json
{"title": null}
~~~

The first omits every field, the second explicitly supplies False, and the third
explicitly supplies null. A partial update must preserve omitted fields:

~~~python
changes = patch.model_dump(exclude_unset=True)
~~~

exclude_unset keeps explicitly supplied values, including False and None, while
removing omitted fields. If this API forbids clearing fields, reject any
explicit None:

~~~python
if any(value is None for value in changes.values()):
    raise HTTPException(status_code=422, detail="Fields cannot be null")
~~~

any returns True when at least one element is truthy. An empty changes
dictionary makes model_copy a valid no-op.

### PUT versus PATCH

- PUT normally replaces the complete resource representation.
- PATCH changes only specified fields.

Say which behavior you implement. Interviews often test whether omitted fields
are accidentally erased.

## Exercises

### 02.10 — Create and read

Implement a shared lookup, create two resources with increasing IDs, return
Location, list by ascending ID, and map missing IDs to 404.

~~~bash
python course/02_crud_endpoints/10_create_and_read.py
~~~

### 02.20 — Update and delete

Extract explicitly supplied fields, reject explicit null, copy and store the
updated model, and delete only after the shared lookup succeeds.

~~~bash
python course/02_crud_endpoints/20_update_and_delete.py
~~~

## Common mistakes

- Returning None from a lookup and letting later code fail with a 500.
- Raising KeyError and exposing an internal storage detail.
- Forgetting to store the copied updated model.
- Using model_dump without exclude_unset and overwriting omitted fields.
- Rejecting False because it is falsy.
- Returning JSON content from a 204 deletion.

## Readiness check

1. Why does dictionary get help implement a 404 branch?
2. What is the difference between omitted, false, and null in PATCH?
3. Why must the changed model be stored again?
4. Which limitations of the in-memory dictionary would you mention in an interview?

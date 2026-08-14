# Course index

Complete the numbered directories and files in order. Every lesson is
standalone and is run from `fastapi-interview-lab`.

```text
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
```

Each lesson contains its exact command. Use this rhythm:

1. Read the contract and predict the first failing check.
2. Implement only the next TODO.
3. Rerun the file.
4. Once green, answer the interview questions in comments or aloud.
5. Change one test input and predict the response before running it.

The checks use FastAPI's `TestClient`, so they exercise routing, serialization,
validation, dependencies, and error handling without starting a real server.

# 01 — Routing and validation

Prerequisite: topic 00.

1. `10_path_and_query_parameters.py` — distinguish resource identity from filters.
2. `20_request_models.py` — validate JSON request bodies with Pydantic.

Interview checkpoint: explain which inputs belong in the path, query string,
headers, and body. Know that FastAPI returns 422 when typed input validation
fails before the endpoint runs.

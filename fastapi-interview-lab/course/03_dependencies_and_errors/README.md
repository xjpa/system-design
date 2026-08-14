# 03 — Dependencies and errors

Prerequisite: topics 00–02.

1. `10_dependencies_and_auth.py` — reuse authentication policy with `Depends`.
2. `20_domain_errors.py` — translate application errors into HTTP responses.

Interview checkpoint: keep authentication and shared lookup rules out of route
bodies. Explain that authentication answers “who are you?” while authorization
answers “may you perform this action?”

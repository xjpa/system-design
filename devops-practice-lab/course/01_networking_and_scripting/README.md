# 01 — Networking and scripting

## Outcome

You can trace a request through name resolution, address, port, connection,
HTTP response, and application dependency—and automate that diagnosis without
hiding useful evidence.

## Mental model

DNS answers “which address?”, TCP answers “can these endpoints connect?”, TLS
answers “is the peer and channel trusted?”, and HTTP carries application
semantics. A successful ping does not prove an HTTP service works; an HTTP 503
can prove the network works while the application is unready.

## Lessons

1. With the stack running, compare `curl -v`, `curl -sS`, and `curl -f` against
   `/health/live`, `/health/ready`, and a missing route.
2. Use `lsof -nP -iTCP:8080 -sTCP:LISTEN` on macOS or `ss -ltnp` on Linux.
3. Complete `10_http_probe.py`, then run its checks.
4. Run `make incident SCENARIO=dependency`. Predict live and ready responses,
   test them, then `make recover`.

## Operational artifact

Create `artifacts/01-network-flow.md` with this chain filled in using observed
values: `name -> address -> port -> process/container -> route -> dependency`.

## Reflection

- What distinguishes “connection refused,” timeout, HTTP 404, and HTTP 503?
- Which health endpoint should a scheduler use before sending traffic?

## Definition of done

`python3 check.py` and `python3 10_http_probe.py` pass, and your diagnostic script
returns a nonzero exit status for an unhealthy service.

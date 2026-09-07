FROM python:3.12-slim

# WORKED EXAMPLE: a fixed working directory makes relative paths predictable.
WORKDIR /app

# TODO: create an unprivileged system user and group named app.
COPY src/ ./src/
# TODO: switch to the app user before runtime.
# TODO: document port 8080 and add a liveness HEALTHCHECK.

CMD ["python", "-m", "src.api"]

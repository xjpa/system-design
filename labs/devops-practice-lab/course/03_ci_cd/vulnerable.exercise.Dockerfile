# Training fixture: intentionally unsupported runtime for a scanner exercise.
# Do not deploy or copy this base choice into another Dockerfile.
FROM python:3.8-slim
USER nobody
CMD ["python", "--version"]

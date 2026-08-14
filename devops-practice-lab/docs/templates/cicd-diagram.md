# CI/CD flow

Replace the placeholders and annotate credential/trust boundaries.

```text
[trigger]
   -> [fast feedback]
   -> [artifact build: immutable identity ____]
   -> [security/quality gates]
   -> [artifact registry]
   -> [approval + short-lived identity]
   -> [deployment]
   -> [verification]
   -> [rollback target ____]
```

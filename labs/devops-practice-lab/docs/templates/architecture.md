# System architecture

## Context

Who uses the system and what outcome do they need?

## Components and flow

Replace the placeholders and show protocols, ports, dependency direction,
network boundaries, and where state exists.

```text
[client] --HTTP--> [API] --RESP/TCP--> [queue] --> [worker]
                       |
                       +--> [metrics and logs] --> [operators]
```

## Trust and failure boundaries

Identify identities, credential sources, public entry points, private services,
and what happens when each dependency becomes slow or unavailable.

## Capacity and recovery assumptions

State what this training design deliberately does not solve, including durable
data, high availability, backups, multi-region operation, and traffic spikes.

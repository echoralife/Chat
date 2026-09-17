# Agent design notes

An agent does not need to be a large framework. At minimum it needs a state transition loop and clear boundaries around side effects.

```text
input → observe → retrieve → construct context → decide → act
                    ↑                              │
                    └────────── remember ◄─────────┘
```

## State

State should be explicit. Hidden global state makes trajectories difficult to reproduce and evaluate.

## Memory

Not every observation deserves permanent storage. Future experiments can introduce an importance gate before persistence, then combine importance with relevance and recency during recall.

## Tools

Tool selection should be inspectable. The rule-based router in this repository is intentionally simple: it provides a deterministic baseline against which learned or LLM-based routers can be compared.

## Tracing

Each meaningful transition should emit a trace event with timing and metadata. This makes it possible to answer questions such as where latency is spent, why a tool was selected, and which memories influenced a response.

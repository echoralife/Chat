# Architecture notes

Neural Lab intentionally separates four concerns that are often coupled inside agent frameworks.

## Memory

`VectorMemory` owns storage and ranking. It accepts vectors rather than generating them, which keeps the component model-agnostic and easy to test.

## Representation

Embedding is injected as a callable. A production implementation could use a local transformer, hosted embedding API, multimodal encoder, or handcrafted feature vector without changing the memory interface.

## Agent loop

`TinyAgent` demonstrates a minimal stateful loop:

```text
observation ──► embedding ──► memory
                               │
query ───────► embedding ──────┤
                               ▼
                         ranked recall
                               │
                               ▼
                            context
```

The trace records important state transitions and can later support trajectory visualization or evaluation.

## Evaluation

Retrieval is measurable independently from generation. Reciprocal rank, precision@k, and hit rate provide a small baseline for comparing retrieval strategies before introducing an LLM into the loop.

## Future experiments

A useful next layer is a persistent backend with timestamps and metadata. From there, retrieval can combine similarity, recency, importance, and lexical overlap:

```text
score = α·semantic + β·lexical + γ·recency + δ·importance
```

Keeping scoring explicit makes behavior inspectable and allows controlled ablations.

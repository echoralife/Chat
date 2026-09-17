# Retrieval experiments

Retrieval quality is treated as a first-class subsystem rather than an implementation detail.

## Pipeline

1. Normalize and chunk source text.
2. Generate a representation for each chunk.
3. Produce semantic and lexical candidate scores.
4. Blend signals with an explicit weighting function.
5. Optionally apply recency or importance weighting.
6. Evaluate ranking before sending context to a generator.

## Why hybrid retrieval?

Vector similarity is useful for paraphrases and conceptual matches, while lexical scoring preserves exact identifiers, rare names, error codes, and domain terminology. A hybrid score can retain both behaviors.

## Evaluation

The included metrics cover three useful questions:

- **MRR:** how early does the first relevant result appear?
- **Precision@k:** how much of the retrieved context is useful?
- **Hit rate:** did retrieval find anything relevant at all?

For serious experiments, evaluate on a held-out query set and report latency alongside quality. A retrieval method that gains a small amount of ranking quality while increasing latency by an order of magnitude may not be a useful tradeoff.

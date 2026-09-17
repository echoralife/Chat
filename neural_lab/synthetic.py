"""Deterministic synthetic retrieval datasets."""

import random

TOPICS = ["attention", "embeddings", "retrieval", "agents", "vision", "optimization"]


def retrieval_cases(count: int = 20, seed: int = 7) -> list[dict[str, str]]:
    rng = random.Random(seed)
    cases = []
    for index in range(count):
        topic = rng.choice(TOPICS)
        cases.append({
            "id": f"case-{index:03d}",
            "query": f"explain {topic} concept {index}",
            "relevant": f"note about {topic} concept {index}",
        })
    return cases

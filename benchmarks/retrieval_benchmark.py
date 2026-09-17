"""Micro-benchmark for vector retrieval latency."""

import random
import time

from neural_lab.memory import VectorMemory


rng = random.Random(42)
dimensions = 64
store = VectorMemory(dimensions)
for i in range(5_000):
    store.add(f"memory-{i}", [rng.random() for _ in range(dimensions)])

query = [rng.random() for _ in range(dimensions)]
start = time.perf_counter()
for _ in range(100):
    store.search(query, limit=5)
elapsed = time.perf_counter() - start

print(f"items={len(store):,}")
print(f"queries=100")
print(f"mean_ms={elapsed / 100 * 1000:.2f}")

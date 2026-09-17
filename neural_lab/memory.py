"""Small, dependency-free vector memory primitives."""

from dataclasses import dataclass
from math import sqrt
from typing import Iterable


@dataclass(frozen=True)
class Memory:
    text: str
    vector: tuple[float, ...]
    score: float = 0.0


def cosine_similarity(a: Iterable[float], b: Iterable[float]) -> float:
    left, right = tuple(a), tuple(b)
    if len(left) != len(right):
        raise ValueError("vectors must have equal dimensions")
    dot = sum(x * y for x, y in zip(left, right))
    norm_a = sqrt(sum(x * x for x in left))
    norm_b = sqrt(sum(y * y for y in right))
    return 0.0 if not norm_a or not norm_b else dot / (norm_a * norm_b)


class VectorMemory:
    """In-memory semantic store using cosine similarity."""

    def __init__(self, dimensions: int):
        if dimensions < 1:
            raise ValueError("dimensions must be positive")
        self.dimensions = dimensions
        self._items: list[Memory] = []

    def add(self, text: str, vector: Iterable[float]) -> None:
        values = tuple(float(v) for v in vector)
        if len(values) != self.dimensions:
            raise ValueError(f"expected {self.dimensions} dimensions")
        self._items.append(Memory(text=text, vector=values))

    def search(self, query: Iterable[float], limit: int = 5) -> list[Memory]:
        values = tuple(float(v) for v in query)
        if len(values) != self.dimensions:
            raise ValueError(f"expected {self.dimensions} dimensions")
        ranked = [Memory(m.text, m.vector, cosine_similarity(values, m.vector)) for m in self._items]
        return sorted(ranked, key=lambda item: item.score, reverse=True)[: max(0, limit)]

    def __len__(self) -> int:
        return len(self._items)

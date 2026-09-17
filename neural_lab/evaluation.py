"""Simple information-retrieval metrics."""


def reciprocal_rank(results: list[str], relevant: set[str]) -> float:
    for rank, item in enumerate(results, start=1):
        if item in relevant:
            return 1.0 / rank
    return 0.0


def precision_at_k(results: list[str], relevant: set[str], k: int) -> float:
    if k <= 0:
        return 0.0
    window = results[:k]
    return sum(item in relevant for item in window) / k


def hit_rate(results: list[str], relevant: set[str], k: int) -> float:
    return float(any(item in relevant for item in results[: max(k, 0)]))

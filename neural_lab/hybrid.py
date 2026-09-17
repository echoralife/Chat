"""Hybrid lexical/vector ranking."""

from dataclasses import dataclass


@dataclass(frozen=True)
class RankedItem:
    text: str
    semantic: float
    lexical: float
    score: float


def combine(text: str, semantic: float, lexical: float, alpha: float = 0.7) -> RankedItem:
    if not 0 <= alpha <= 1:
        raise ValueError("alpha must be between zero and one")
    score = alpha * semantic + (1 - alpha) * lexical
    return RankedItem(text, semantic, lexical, score)


def rank(items: list[RankedItem]) -> list[RankedItem]:
    return sorted(items, key=lambda item: item.score, reverse=True)

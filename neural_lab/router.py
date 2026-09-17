"""Rule-based tool routing baseline."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Route:
    tool: str
    confidence: float


KEYWORDS = {
    "search": {"find", "search", "lookup", "latest", "web"},
    "calculator": {"calculate", "sum", "multiply", "percent", "equation"},
    "memory": {"remember", "recall", "previous", "earlier", "memory"},
}


def route(text: str) -> Route:
    tokens = set(text.lower().split())
    scores = {tool: len(tokens & words) for tool, words in KEYWORDS.items()}
    tool, hits = max(scores.items(), key=lambda pair: pair[1])
    return Route(tool if hits else "respond", min(1.0, hits / 2) if hits else 0.5)

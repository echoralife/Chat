"""Structured trajectory tracing for agent experiments."""

from dataclasses import asdict, dataclass
import json
import time


@dataclass(frozen=True)
class Span:
    name: str
    started_at: float
    duration_ms: float
    metadata: dict[str, str]


class Trace:
    def __init__(self) -> None:
        self.spans: list[Span] = []

    def record(self, name: str, started_at: float, metadata: dict[str, str] | None = None) -> None:
        self.spans.append(Span(name, started_at, (time.time() - started_at) * 1000, metadata or {}))

    def to_json(self) -> str:
        return json.dumps([asdict(span) for span in self.spans], indent=2)

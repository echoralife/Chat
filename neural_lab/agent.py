"""A tiny stateful agent loop for local experiments."""

from dataclasses import dataclass, field
from typing import Callable

from .memory import VectorMemory


@dataclass
class TraceEvent:
    kind: str
    payload: str


@dataclass
class TinyAgent:
    memory: VectorMemory
    embed: Callable[[str], list[float]]
    trace: list[TraceEvent] = field(default_factory=list)

    def observe(self, text: str) -> None:
        self.memory.add(text, self.embed(text))
        self.trace.append(TraceEvent("observe", text))

    def recall(self, query: str, limit: int = 3) -> list[str]:
        matches = self.memory.search(self.embed(query), limit=limit)
        self.trace.append(TraceEvent("recall", query))
        return [match.text for match in matches]

    def context(self, query: str, limit: int = 3) -> str:
        memories = self.recall(query, limit)
        return "\n".join(f"- {memory}" for memory in memories)

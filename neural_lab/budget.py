"""Approximate context-window accounting."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Budget:
    maximum: int
    reserved_output: int = 0

    @property
    def available(self) -> int:
        return max(0, self.maximum - self.reserved_output)


def estimate_tokens(text: str) -> int:
    """Fast model-agnostic approximation: roughly four characters/token."""
    return max(1, (len(text) + 3) // 4) if text else 0


def fits(text: str, budget: Budget) -> bool:
    return estimate_tokens(text) <= budget.available
